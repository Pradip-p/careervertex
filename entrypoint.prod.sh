#!/bin/bash
# Wait until PostgreSQL is ready
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "Waiting for PostgreSQL to start..."
  sleep 1
done

echo "PostgreSQL is up and running!"

# Continue with your Django application startup command
exec "$@"
