#!/bin/bash

# Run database migrations
python manage.py makemigrations jobsapp resume_cv accounts tags oauth2_provider
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Check if DEBUG is set to 1, then run the development server
if [ "$DEBUG" = "1" ]; then
  exec python manage.py runserver 0.0.0.0:8000
else
  # Otherwise, run Gunicorn
  exec gunicorn jobs.wsgi:application --bind 0.0.0.0:8000 --workers 2
fi
