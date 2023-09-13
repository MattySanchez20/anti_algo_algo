# Use an official Python 3.10 image as the parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code into the container
COPY . /app

ENV PATH="/usr/bin/google-chrome:${PATH}"

# installing all packages for python
RUN pip install -r requirements.txt

# Specify the command to run your script (replace script.py with your script's filename)
CMD ["python", "origin.py"]
