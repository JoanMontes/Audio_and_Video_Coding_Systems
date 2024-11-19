# Use a lightweight Linux base image
FROM python:3.11

# Update package list and install FFmpeg
RUN pip install ffmpeg

# Set the default command to FFmpeg
CMD ["ffmpeg", "-version"]