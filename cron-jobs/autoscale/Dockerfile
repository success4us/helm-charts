# Use the official Python 3.x image as the base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the kubeconfig file into the Docker image
COPY kubeconfig.yaml /app/kubeconfig.yaml

# Set the KUBECONFIG environment variable to the kubeconfig file path
ENV KUBECONFIG=/app/kubeconfig.yaml

# Copy your Python script and other necessary files to the container
COPY get-pods.py /app/
# Add any other dependencies or files your script may require

# Install any Python dependencies
RUN pip install kubernetes

# Define environment variables (if needed)
ENV THRESHOLD_GIB=190
ENV INCREASE_SIZE_GIB=5

# Run the Python script when the container starts
CMD [ "python", "get-pods.py" ]
