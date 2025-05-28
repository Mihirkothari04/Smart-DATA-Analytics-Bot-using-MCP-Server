import os
import json
import requests
from typing import Dict, Any, List

# MCP Server URLs
SQLITE_MCP_SERVER = os.getenv("SQLITE_MCP_SERVER", "http://localhost:8000")
VEGALITE_MCP_SERVER = os.getenv("VEGALITE_MCP_SERVER", "http://localhost:8001")  # Updated port

# Define MCP client functions
def call_sqlite_mcp(tool_name, **kwargs):
    """Call SQLite MCP server tool."""
    url = f"{SQLITE_MCP_SERVER}/mcp/tools/{tool_name}"
    try:
        response = requests.post(url, json=kwargs)
        if response.status_code != 200:
            return {"error": f"Status code: {response.status_code}, Message: {response.text}"}
        return response.json()
    except Exception as e:
        return {"error": f"Exception: {str(e)}"}

def call_vegalite_mcp(tool_name, **kwargs):
    """Call VegaLite MCP server tool."""
    url = f"{VEGALITE_MCP_SERVER}/mcp/tools/{tool_name}"
    try:
        response = requests.post(url, json=kwargs)
        if response.status_code != 200:
            return {"error": f"Status code: {response.status_code}, Message: {response.text}"}
        return response.json()
    except Exception as e:
        return {"error": f"Exception: {str(e)}"}

def process_query(query: str) -> Dict[str, Any]:
    """
    Process a natural language query and return the response.
    
    In a production environment, this would use an actual LLM.
    For this demo, we simulate the LLM's response with a predefined flow.
    
    Args:
        query: Natural language query from the user
        
    Returns:
        dict: Response containing text explanation and visualization (if any)
    """
    print(f"Processing query: {query}")
    
    # For demo purposes, we'll simulate the steps an LLM would take
    
    # 1. Get database schema
    print("Step 1: Getting database schema...")
    schema = call_sqlite_mcp("get_schema")
    if "error" in schema:
        print(f"Error getting schema: {schema['error']}")
        return {
            "text": f"Error accessing database: {schema['error']}",
            "visualization": None
        }
    
    # 2. Generate and execute SQL query based on the natural language query
    print("Step 2: Generating and executing SQL query...")
    
    # For demo, we'll use a predefined query for "Show me the 6-month sales trend for Product A"
    if "Product A" in query and ("trend" in query or "sales" in query):
        sql_query = """
        SELECT 
            strftime('%Y-%m', date) as month,
            SUM(revenue) as total_revenue
        FROM 
            sales
        JOIN 
            products ON sales.product_id = products.product_id
        WHERE 
            products.product_name = 'Product A'
            AND date >= date('now', '-6 months')
        GROUP BY 
            strftime('%Y-%m', date)
        ORDER BY 
            month ASC
        """
        
        # Execute the query
        results = call_sqlite_mcp("execute_query", query=sql_query)
        if "error" in results:
            print(f"Error executing query: {results['error']}")
            return {
                "text": f"Error querying database: {results['error']}",
                "visualization": None
            }
        
        # 3. Analyze the results
        print("Step 3: Analyzing results...")
        
        # 4. Generate visualization
        print("Step 4: Generating visualization...")
        
        # Save data for visualization
        data_save_response = call_vegalite_mcp("save_data", data=results, name="product_a_sales")
        if "error" in data_save_response:
            print(f"Error saving data: {data_save_response['error']}")
            # Continue without visualization
        else:
            print(f"Data saved successfully: {data_save_response}")
        
        # Create Vega-Lite spec for a line chart
        vega_spec = {
            "mark": "line",
            "encoding": {
                "x": {"field": "month", "type": "temporal", "title": "Month"},
                "y": {"field": "total_revenue", "type": "quantitative", "title": "Revenue ($)"}
            },
            "title": "6-Month Sales Trend for Product A"
        }
        
        # Generate the visualization
        viz_response = call_vegalite_mcp("visualize_data", data_name="product_a_sales", spec=vega_spec, format="png")
        if "error" in viz_response:
            print(f"Error generating visualization: {viz_response['error']}")
            visualization = None
        else:
            visualization = viz_response.get("content") if viz_response.get("format") == "png" else None
        
        # 5. Prepare the response
        analysis_text = """
## Analysis of Product A Sales Trend (Last 6 Months)

I've analyzed the 6-month sales trend for Product A from December 2024 to May 2025.

### Key Findings:
- **Overall Trend**: Product A shows a strong upward trend in sales over the 6-month period
- **Total Revenue**: $61,800.00
- **Monthly Average**: $10,300.00
- **Growth Rate**: 400% increase from December ($3,600) to May ($18,000)

### Significant Changes:
- **February 2025**: 166% increase from January, possibly due to seasonal demand
- **April 2025**: 20% increase from March, coinciding with promotional activities
- **May 2025**: 25% increase from April, reaching the highest point in the period

The consistent month-over-month growth suggests strong market demand for Product A, with particularly notable acceleration in the February-March period.
        """
        
        return {
            "text": analysis_text,
            "visualization": visualization
        }
    
    # Default response for other queries
    return {
        "text": "I'm sorry, I can only process specific demo queries at this time. Please try asking about the 6-month sales trend for Product A.",
        "visualization": None
    }
