#!/bin/sh

# Wait a few seconds for DB
sleep 3

echo "Running migrations..."
python manage.py migrate

echo "Running seed script..."
python manage.py seed

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
