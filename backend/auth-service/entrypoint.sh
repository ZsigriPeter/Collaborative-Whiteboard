#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Running seed script..."
python manage.py seed

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
