import streamlit as st
import requests
import json
import base64
from PIL import Image
import io
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import LLM agent
import sys
sys.path.append('../llm_integration')
from llm_agent import process_query

# Set page configuration
st.set_page_config(
    page_title="Smart Data Analyst Bot",
    page_icon="📊",
    layout="wide"
)

# App title and description
st.title("Smart Data Analyst Bot")
st.markdown("""
Ask questions about your data in natural language and get visualizations and insights.
""")

# Sidebar with information
with st.sidebar:
    st.header("About")
    st.info("""
    This Smart Data Analyst Bot uses AI to:
    
    - Process natural language questions
    - Query databases automatically
    - Generate appropriate visualizations
    - Provide insights and explanations
    
    Powered by MCP (Model Context Protocol)
    """)
    
    st.header("Example Questions")
    st.markdown("""
    - Show me the 6-month sales trend for Product A
    - Compare revenue by region for the last quarter
    - What are our top 5 customers by order value?
    - Show monthly sales growth rate for 2024
    - Which products had the biggest decline last month?
    """)

# Main interface
query = st.text_input("Ask a question about your data:", placeholder="e.g., Show me the 6-month sales trend for Product A")

if st.button("Analyze", type="primary") or query:
    if query:
        with st.spinner("Analyzing your data..."):
            # Process the query
            response = process_query(query)
            
            # Display the text response
            st.markdown("### Analysis")
            st.write(response["text"])
            
            # Display visualization if available
            if response.get("visualization"):
                st.markdown("### Visualization")
                try:
                    image_data = base64.b64decode(response["visualization"])
                    image = Image.open(io.BytesIO(image_data))
                    st.image(image, use_column_width=True)
                except Exception as e:
                    st.error(f"Error displaying visualization: {str(e)}")
    else:
        st.warning("Please enter a question to analyze.")

# Footer
st.markdown("---")
st.markdown("Smart Data Analyst Bot - Powered by MCP (Model Context Protocol)")
