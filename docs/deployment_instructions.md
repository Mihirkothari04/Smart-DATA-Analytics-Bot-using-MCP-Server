# Deployment Instructions

This document provides detailed instructions for deploying the Smart Data Analyst Bot.

## Prerequisites

- Python 3.8+
- Docker and Docker Compose (optional, for containerized deployment)
- Git (optional, for version control)

## Option 1: Local Development Setup

### Step 1: Clone or Extract the Repository

If you received the code as a zip file:
```bash
unzip smart-data-analyst-bot.zip -d smart-data-analyst-bot
cd smart-data-analyst-bot
```

### Step 2: Set Up Python Environment

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Initialize the Database

```bash
# Navigate to the database directory
cd database

# Initialize the database with sample data
python init_database.py

# Return to the project root
cd ..
```

### Step 4: Start the MCP Servers

Open two separate terminal windows:

Terminal 1 (SQLite MCP Server):
```bash
# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Set environment variables
export DB_PATH="./database/sample_data.db"  # On Windows: set DB_PATH=./database/sample_data.db

# Start the SQLite MCP Server
cd mcp_servers/sqlite_server
python server.py
```

Terminal 2 (VegaLite MCP Server):
```bash
# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Start the VegaLite MCP Server
cd mcp_servers/vegalite_server
python server.py
```

### Step 5: Start the Web Interface

Open a third terminal window:

```bash
# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Set environment variables
export SQLITE_MCP_SERVER="http://localhost:8000"  # On Windows: set SQLITE_MCP_SERVER=http://localhost:8000
export VEGALITE_MCP_SERVER="http://localhost:8001"  # On Windows: set VEGALITE_MCP_SERVER=http://localhost:8001
export LLM_API_KEY="your_api_key_here"  # On Windows: set LLM_API_KEY=your_api_key_here

# Start the Streamlit web interface
cd web_interface
streamlit run app.py
```

The web interface will be available at http://localhost:8501

## Option 2: Docker Deployment

### Step 1: Clone or Extract the Repository

```bash
unzip smart-data-analyst-bot.zip -d smart-data-analyst-bot
cd smart-data-analyst-bot
```

### Step 2: Configure Environment Variables

Create a `.env` file in the project root:

```
# LLM Configuration
LLM_API_KEY=your_api_key_here

# Server Configuration
HOST=0.0.0.0
PORT=8501
```

### Step 3: Build and Start the Containers

```bash
# Build and start all containers
docker-compose up -d
```

The web interface will be available at http://localhost:8501

### Step 4: Verify Deployment

Check that all containers are running:

```bash
docker-compose ps
```

You should see three containers running:
- sqlite-mcp-server
- vegalite-mcp-server
- web-interface

## Customization Options

### Using Your Own Database

To use your own database instead of the sample data:

1. Replace the SQL script in `database/init_db.sql` with your own schema and data
2. Run the database initialization step again
3. Update the database path in the environment variables or `.env` file

### Configuring the LLM

The system is designed to work with OpenAI's GPT models by default. To use a different LLM:

1. Modify the `llm_integration/llm_agent.py` file to use your preferred LLM provider
2. Update the environment variables or `.env` file with the appropriate API key

## Troubleshooting

### Common Issues

1. **Port Conflicts**: If you encounter "Address already in use" errors, change the port numbers in the server files and update the environment variables accordingly.

2. **Database Connection Errors**: Verify that the database path is correct and that the SQLite database file exists.

3. **API Key Issues**: Ensure that your LLM API key is valid and properly set in the environment variables.

4. **Visualization Errors**: If chart generation fails, check that all required dependencies are installed and that the data format matches the expected schema.

### Logs

To view logs in Docker deployment:

```bash
# View logs for all containers
docker-compose logs

# View logs for a specific container
docker-compose logs sqlite-mcp-server
```

## Next Steps

After deployment, refer to the [User Guide](user_guide.md) for instructions on using the Smart Data Analyst Bot.
