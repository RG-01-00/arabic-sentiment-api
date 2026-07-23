FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    transformers \
    torch --index-url https://download.pytorch.org/whl/cpu \
    scikit-learn \
    pydantic

# Copy application
COPY main.py .
COPY sentiment_engine.py .

# Run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]