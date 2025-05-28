# Smart Data Analyst Bot

A fully-automated AI service that turns natural language questions into data queries and charts using the Model Context Protocol (MCP).

## Overview

This project implements a Smart Data Analyst Bot that allows users to ask questions about data in natural language. The system:

1. Processes natural language queries
2. Translates them into SQL queries
3. Retrieves data from a database
4. Generates appropriate visualizations
5. Provides narrative explanations of the results

## Architecture

The system follows a modular architecture using MCP to connect components:

- **LLM Client**: Interprets user queries and orchestrates the process
- **Database MCP Server**: Provides database connectivity (SQLite)
- **Visualization MCP Server**: Generates charts and visualizations (Vega-Lite)
- **Web Interface**: Provides user interaction (Streamlit)

## Features

- Natural language query processing
- Automated SQL query generation
- Dynamic chart creation based on query context
- Narrative explanations of data insights
- Web-based user interface

## Technology Stack

- **Database**: SQLite with jparkerweb/mcp-sqlite
- **Visualization**: VegaLite MCP Server
- **LLM Integration**: LangChain with MCP
- **Web Interface**: Streamlit
- **Deployment**: Docker Containers

## Project Structure

```
smart_data_analyst_bot/
├── docker/                  # Docker configuration files
├── database/                # Database setup and sample data
├── mcp_servers/             # MCP server implementations
│   ├── sqlite_server/       # SQLite MCP server
│   └── vegalite_server/     # VegaLite MCP server
├── llm_integration/         # LLM integration with MCP
├── web_interface/           # Streamlit web application
├── tests/                   # Test cases and examples
└── docs/                    # Documentation
```

## Getting Started

See the [Installation Guide](docs/installation.md) for setup instructions.
