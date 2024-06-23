# Use an official Python runtime as a parent image
FROM python:3.8-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get -y install nano \
    && apt-get clean \
    && apt-get install -y postgresql-client

# Install specific pip version
RUN python -m pip install --upgrade "pip==23.0.1"

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/
ENV DEBUG=1

# Expose port
EXPOSE 8000

# Run entrypoint script
CMD ["sh", "entrypoint.sh"]
