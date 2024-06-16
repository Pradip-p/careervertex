#!/bin/bash
# Wait until PostgreSQL is ready
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "Waiting for PostgreSQL to start..."
  sleep 1
done

echo "PostgreSQL is up and running!"

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py makemigrations jobsapp resume_cv accounts tags oauth2_provider
python manage.py migrate

# Continue with your Django application startup command
exec "$@"
