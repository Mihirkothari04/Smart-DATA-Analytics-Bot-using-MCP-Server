import os
import json
import base64
import io
from typing import Dict, Any, List, Optional, Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import altair as alt
from PIL import Image

# Initialize FastAPI app
app = FastAPI(title="VegaLite MCP Server")

# In-memory data storage
data_store = {}

# Define models
class DataSaveRequest(BaseModel):
    data: List[Dict[str, Any]]
    name: str

class VisualizationRequest(BaseModel):
    data_name: str
    spec: Dict[str, Any]
    format: str = "png"  # "png" or "json"

# Helper functions
def save_data_to_store(data, name):
    """Save data to in-memory store."""
    try:
        # Convert to pandas DataFrame for easier manipulation
        df = pd.DataFrame(data)
        data_store[name] = df
        return {"status": "success", "message": f"Data saved as '{name}'", "rows": len(df)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error saving data: {str(e)}")

def generate_visualization(data_name, spec, format_type="png"):
    """Generate visualization from data and Vega-Lite spec."""
    if data_name not in data_store:
        raise HTTPException(status_code=404, detail=f"Data '{data_name}' not found")
    
    try:
        # Get data from store
        df = data_store[data_name]
        
        # Create Altair chart from Vega-Lite spec
        chart_spec = spec.copy()
        
        # If data is not in the spec, add it
        if "data" not in chart_spec:
            chart_spec["data"] = {"name": data_name}
        
        # Create chart
        chart = alt.Chart.from_dict(chart_spec)
        chart = chart.encode(
            **{k: v for k, v in chart_spec.get("encoding", {}).items()}
        )
        
        # Return based on format
        if format_type.lower() == "json":
            return {"format": "json", "content": chart.to_dict()}
        else:  # PNG format
            # Save chart as PNG
            png_data = chart.to_image(format="png")
            base64_png = base64.b64encode(png_data).decode("utf-8")
            return {"format": "png", "content": base64_png}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error generating visualization: {str(e)}")

# Define API endpoints for MCP tools
@app.post("/mcp/tools/save_data")
async def tool_save_data(request: DataSaveRequest):
    """
    Save data to the server for later visualization.
    """
    return save_data_to_store(request.data, request.name)

@app.post("/mcp/tools/visualize_data")
async def tool_visualize_data(request: VisualizationRequest):
    """
    Generate a visualization from data using Vega-Lite specification.
    """
    return generate_visualization(request.data_name, request.spec, request.format)

@app.get("/mcp/tools/list_datasets")
async def tool_list_datasets():
    """
    List all available datasets in the server.
    """
    return {
        "datasets": {
            name: {
                "rows": len(df),
                "columns": df.columns.tolist()
            }
            for name, df in data_store.items()
        }
    }

@app.get("/mcp/tools/get_dataset_info")
async def tool_get_dataset_info(name: str):
    """
    Get information about a specific dataset.
    """
    if name not in data_store:
        raise HTTPException(status_code=404, detail=f"Dataset '{name}' not found")
    
    df = data_store[name]
    return {
        "name": name,
        "rows": len(df),
        "columns": df.columns.tolist(),
        "dtypes": {col: str(df[col].dtype) for col in df.columns},
        "sample": df.head(5).to_dict(orient="records")
    }

# Define MCP resources endpoint
@app.get("/mcp/resources/datasets")
async def resource_datasets():
    """Datasets resource."""
    return {
        name: {
            "rows": len(df),
            "columns": df.columns.tolist()
        }
        for name, df in data_store.items()
    }

# Add a simple health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8001, reload=True)  # Changed port to 8001
