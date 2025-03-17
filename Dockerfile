# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 (or your app's port) for access to the app
EXPOSE 8000

# Command to run the app (you might need to adjust this depending on your setup)
CMD ["python", "app/main.py"]
