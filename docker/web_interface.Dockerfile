FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "web_interface/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
