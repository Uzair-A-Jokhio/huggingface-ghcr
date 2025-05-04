# Use the official Python image as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the FastAPI application code into the container
COPY app/* /app

# Expose the port FastAPI will run on
ENTRYPOINT ["uvicorn"]

# Command to run the FastAPI application
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000"]