# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables to ensure Python outputs logs and errors
ENV PYTHONUNBUFFERED 1

# Install system dependencies required for mysqlclient and build tools
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libmariadb-dev \
    pkg-config \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt to the container
COPY requirements.txt /app/

# Install the Python dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Django project into the container
COPY . /app/

# Expose the port that Django will run on (default is 8000)
EXPOSE 8000

# Command to run the Django server by default when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

