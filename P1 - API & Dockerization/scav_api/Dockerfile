# Use a lightweight Python base image
FROM python:3.11-slim

# Install system dependencies, including FFMPEG
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    build-essential \
    ffmpeg

# Set the working directory in the container
WORKDIR /app

# Copy application requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port for FastAPI
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
