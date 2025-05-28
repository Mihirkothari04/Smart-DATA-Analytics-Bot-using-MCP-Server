import os
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional, Union
import sqlite3

# Initialize FastAPI app
app = FastAPI(title="SQLite MCP Server")

# Get database path from environment variable
DB_PATH = os.getenv("DB_PATH", "/app/database/sample_data.db")

# Define models
class QueryRequest(BaseModel):
    query: str

class SchemaResponse(BaseModel):
    tables: List[str]
    table_schemas: Dict[str, List[Dict[str, str]]]

# Helper functions
def get_db_connection():
    """Create a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")

def get_schema():
    """Get the database schema."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    
    # Get schema for each table
    table_schemas = {}
    for table in tables:
        cursor.execute(f"PRAGMA table_info({table});")
        columns = [{"name": row[1], "type": row[2]} for row in cursor.fetchall()]
        table_schemas[table] = columns
    
    conn.close()
    return {"tables": tables, "table_schemas": table_schemas}

def execute_query(query):
    """Execute an SQL query and return the results."""
    if not query.strip().lower().startswith(("select", "with")):
        raise HTTPException(status_code=400, detail="Only SELECT queries are allowed for security reasons")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        columns = [description[0] for description in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        return results
    except sqlite3.Error as e:
        conn.close()
        raise HTTPException(status_code=400, detail=f"Query execution error: {str(e)}")

# Define API endpoints for MCP tools
@app.post("/mcp/tools/get_schema", response_model=SchemaResponse)
async def tool_get_schema():
    """
    Get the database schema including tables and their columns.
    """
    return get_schema()

@app.post("/mcp/tools/execute_query")
async def tool_execute_query(request: QueryRequest):
    """
    Execute a read-only SQL query on the SQLite database.
    """
    return execute_query(request.query)

@app.post("/mcp/tools/get_table_data")
async def tool_get_table_data(table_name: str, limit: Optional[int] = 10):
    """
    Get data from a specific table with an optional limit.
    """
    query = f"SELECT * FROM {table_name} LIMIT {limit}"
    return execute_query(query)

# Define MCP resources endpoint
@app.get("/mcp/resources/schema")
async def resource_schema():
    """Database schema resource."""
    schema = get_schema()
    return {
        "tables": {
            table: {
                "columns": {
                    column["name"]: {"type": column["type"]}
                    for column in schema["table_schemas"][table]
                }
            }
            for table in schema["tables"]
        }
    }

# Add a simple health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
