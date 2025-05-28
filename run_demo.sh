#!/bin/bash

# This script runs an end-to-end demo of the Smart Data Analyst Bot

echo "Starting Smart Data Analyst Bot Demo..."

# Step 1: Initialize the database
echo "Step 1: Initializing database with sample data..."
cd /home/ubuntu/smart_data_analyst_bot/database
python init_database.py

# Step 2: Start the SQLite MCP Server
echo "Step 2: Starting SQLite MCP Server..."
cd /home/ubuntu/smart_data_analyst_bot/mcp_servers/sqlite_server
export DB_PATH="/home/ubuntu/smart_data_analyst_bot/database/sample_data.db"
python server.py &
SQLITE_PID=$!
echo "SQLite MCP Server started with PID: $SQLITE_PID"
sleep 3  # Give the server time to start

# Step 3: Start the VegaLite MCP Server
echo "Step 3: Starting VegaLite MCP Server..."
cd /home/ubuntu/smart_data_analyst_bot/mcp_servers/vegalite_server
python server.py &
VEGALITE_PID=$!
echo "VegaLite MCP Server started with PID: $VEGALITE_PID"
sleep 3  # Give the server time to start

# Step 4: Run a test query
echo "Step 4: Running a test query..."
cd /home/ubuntu/smart_data_analyst_bot
export SQLITE_MCP_SERVER="http://localhost:8000"
export VEGALITE_MCP_SERVER="http://localhost:8001"  # Updated port
export LLM_API_KEY="demo_key"  # This is a placeholder for the demo

# Create a simple test script
cat > test_query.py << 'EOF'
import sys
sys.path.append('./llm_integration')
from llm_agent import process_query

# Run the test query
result = process_query("Show me the 6-month sales trend for Product A")
print("\nRESULT:")
print(result["text"])
print("\nDemo completed successfully!")
EOF

# Run the test
python test_query.py

# Step 5: Clean up
echo "Step 5: Cleaning up..."
kill $SQLITE_PID
kill $VEGALITE_PID
rm test_query.py

echo "Demo completed!"
echo "In a production environment, you would access the web interface at http://localhost:8501"
