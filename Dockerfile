# Use an official Python runtime as a parent image
FROM python:3.8-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update \
    && apt-get -y install nano \
    && apt-get clean

# Install specific pip version
RUN python -m pip install --upgrade "pip==23.0.1"

# Install Python dependencies
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# Copy project files
COPY . /usr/src/app/
ENV DEBUG=1
# Copy sample environment file
RUN cp .env.dev.sample .env

# Expose port
EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --noinput

# Apply database migrations
RUN python manage.py makemigrations jobsapp resume_cv accounts tags oauth2_provider --settings=jobs.settings

# Run entrypoint script
CMD ["sh", "entrypoint.sh"]
