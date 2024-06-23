#!/bin/bash
# Wait until PostgreSQL is ready
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "Waiting for PostgreSQL to start..."
  sleep 1
done

echo "PostgreSQL is up and running!"
python manage.py collectstatic --noinput
python manage.py makemigrations jobsapp accounts oauth2_provider
python manage.py migrate
# Continue with your Django application startup command
exec "$@"
