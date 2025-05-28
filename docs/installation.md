# Installation and Setup Guide

This guide will walk you through setting up the Smart Data Analyst Bot on your system.

## Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Git

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smart-data-analyst-bot.git
cd smart-data-analyst-bot
```

### 2. Set Up Python Environment

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory with the following variables:

```
# LLM Configuration
LLM_API_KEY=your_api_key_here
LLM_MODEL=gpt-4

# Database Configuration
DB_PATH=./database/sample_data.db

# Server Configuration
HOST=0.0.0.0
PORT=8501
```

### 4. Set Up Sample Database

```bash
# Initialize the database with sample data
python scripts/init_database.py
```

### 5. Start the MCP Servers

```bash
# Start the SQLite MCP Server
docker-compose up -d sqlite-mcp-server

# Start the VegaLite MCP Server
docker-compose up -d vegalite-mcp-server
```

### 6. Launch the Web Interface

```bash
# Start the Streamlit web interface
streamlit run web_interface/app.py
```

## Docker Deployment (Alternative)

To deploy the entire system using Docker:

```bash
# Build and start all containers
docker-compose up -d
```

The web interface will be available at http://localhost:8501

## Troubleshooting

If you encounter issues:

1. Check that all required ports are available
2. Verify that environment variables are correctly set
3. Ensure Docker is running properly
4. Check logs with `docker-compose logs`

## Next Steps

After installation, see the [User Guide](user_guide.md) for instructions on using the Smart Data Analyst Bot.
