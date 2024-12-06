# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variable to ensure Python output is not buffered
ENV PYTHONUNBUFFERED 1

# Install system dependencies required for building some Python packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libmariadb-dev \
        pkg-config \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Upgrade pip before installing dependencies
RUN pip install --upgrade pip

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Command to run the application (modify based on your needs)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
