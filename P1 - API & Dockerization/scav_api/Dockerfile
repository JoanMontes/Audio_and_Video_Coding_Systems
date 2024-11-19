# We select the base image of the container
FROM python:3.11

# We select the working directory for the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# We install the requirements and ffmpeg
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install ffmpeg

# Copy everything in the working directory
COPY . .

# Expose the port 
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
