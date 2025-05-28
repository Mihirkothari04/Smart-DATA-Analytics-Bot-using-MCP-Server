# User Guide

This guide explains how to use the Smart Data Analyst Bot to analyze your data using natural language queries.

## Overview

The Smart Data Analyst Bot allows you to:

1. Ask questions about your data in natural language
2. Get SQL queries automatically generated and executed
3. View visualizations of your data
4. Receive narrative explanations and insights

## Using the Web Interface

### Accessing the Application

Once the application is running, access it through your web browser at:
```
http://localhost:8501
```

### Asking Questions

1. Type your question in the text input field at the top of the page
2. Click the "Analyze" button or press Enter
3. Wait for the system to process your query (this may take a few seconds)
4. View the results, including text analysis and visualizations

### Example Questions

Here are some example questions you can ask:

- **Trend Analysis**: "Show me the 6-month sales trend for Product A"
- **Comparisons**: "Compare revenue by region for the last quarter"
- **Rankings**: "What are our top 5 customers by order value?"
- **Growth Metrics**: "Show monthly sales growth rate for 2024"
- **Performance Analysis**: "Which products had the biggest decline last month?"

### Understanding Results

The results page contains:

1. **Analysis**: A textual explanation of the data findings, including trends, patterns, and insights
2. **Visualization**: A chart or graph that visually represents the data
3. **Context**: Additional information that helps interpret the results

## Advanced Usage

### Refining Questions

If your initial question doesn't yield the expected results, try:

- Being more specific about time periods (e.g., "last 6 months" instead of "recent")
- Specifying metrics clearly (e.g., "by revenue" instead of "by performance")
- Naming entities exactly as they appear in the database (e.g., "Product A" not "ProductA")

### Combining Analyses

You can ask complex questions that combine multiple analyses:

- "Compare sales of Product A and Product B over the last 6 months and highlight any months where Product B outsold Product A"
- "Show me the correlation between customer segment and average order value, broken down by region"

## Troubleshooting

### Common Issues

- **No Data Found**: Ensure you're referring to products, regions, or customers that exist in the database
- **Unclear Visualization**: Try rephrasing your question to be more specific about what you want to visualize
- **Slow Response**: Complex queries may take longer to process, especially those requiring multiple data transformations

### Getting Help

If you encounter persistent issues:

1. Check that all services are running correctly
2. Verify that the database contains the data you're querying
3. Consult the technical documentation for more detailed information
