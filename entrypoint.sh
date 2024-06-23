#!/bin/bash

# Run database migrations


# Collect static files
python manage.py collectstatic --noinput
python manage.py makemigrations jobsapp  accounts oauth2_provider
python manage.py migrate

# Check if DEBUG is set to 1, then run the development server
if [ "$DEBUG" = "1" ]; then
  exec python manage.py runserver 0.0.0.0:8000
else
  # Otherwise, run Gunicorn
  exec gunicorn jobs.wsgi:application --bind 0.0.0.0:8000 --workers 2
fi
