# Known Limitations and Workarounds

This document outlines known limitations of the Smart Data Analyst Bot and provides workarounds where applicable.

## Visualization Limitations

### Altair to_image Method

**Issue**: The current implementation uses Altair's `to_image()` method for generating PNG visualizations. However, this method may not be available in all environments, resulting in an error during chart generation.

**Workaround**: The system is designed to gracefully handle this limitation by still providing textual analysis even when visualization fails. For environments where `to_image()` is not available, you can modify the VegaLite MCP Server to return JSON specifications instead of PNG images:

1. Open `mcp_servers/vegalite_server/server.py`
2. Locate the `generate_visualization()` function
3. Replace the PNG generation code with:

```python
# Instead of trying to generate PNG
# png_data = chart.to_image(format="png")
# base64_png = base64.b64encode(png_data).decode("utf-8")
# return {"format": "png", "content": base64_png}

# Return the JSON spec instead
return {"format": "json", "content": chart.to_dict()}
```

4. Update the web interface to render Vega-Lite JSON specifications using a JavaScript library like vega-embed.

## LLM Integration Limitations

### Demo Mode

**Issue**: The current implementation includes a demo mode that simulates LLM responses for the specific query "Show me the 6-month sales trend for Product A" without requiring an actual LLM API key.

**Workaround**: To use the system with a real LLM:

1. Obtain an API key from your preferred LLM provider (e.g., OpenAI)
2. Set the `LLM_API_KEY` environment variable
3. Modify `llm_integration/llm_agent.py` to use the actual LLM API instead of the demo responses

## Database Limitations

### Read-Only Queries

**Issue**: For security reasons, the SQLite MCP Server only allows SELECT queries and blocks any data modification operations.

**Workaround**: If you need to modify data:

1. Use direct database access outside the MCP server for data modifications
2. Implement a separate authenticated API for data modifications with proper authorization controls

## Performance Considerations

### Concurrent Users

**Issue**: The current implementation is designed for demonstration purposes and may not handle multiple concurrent users efficiently.

**Workaround**: For production deployment with multiple users:

1. Implement connection pooling for database access
2. Add caching for frequently accessed data and visualizations
3. Consider scaling the MCP servers horizontally behind a load balancer

## Browser Compatibility

**Issue**: The web interface is tested primarily with modern browsers (Chrome, Firefox, Safari) and may have display issues with older browsers.

**Workaround**: Ensure users access the application with an up-to-date browser for the best experience.
