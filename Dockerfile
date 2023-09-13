# # Use an official Python 3.10 image as the parent image
FROM python:3.10-slim

# Set environment variables
ENV TZ=UTC

# Set the working directory in the container
WORKDIR /app

# Copy files to working directory
COPY . /app

RUN pip install -r requirements.txt

# Start your Selenium script when the container runs
CMD ["python", "origin.py"]
