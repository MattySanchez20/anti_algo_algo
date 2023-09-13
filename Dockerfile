# Use an official Python 3.10 image as the parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR .

# Copy the local poetry.lock and pyproject.toml into the container
COPY pyproject.toml poetry.lock ./

# Install poetry and project dependencies
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copy the rest of the application code into the container
COPY . .

# Specify the command to run your script (replace script.py with your script's filename)
CMD ["python", "script.py"]
