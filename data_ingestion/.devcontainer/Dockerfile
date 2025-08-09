# .devcontainer/Dockerfile
FROM python:3.11-slim

# Install pip packages
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Optional: Create a working directory
WORKDIR /workspace
