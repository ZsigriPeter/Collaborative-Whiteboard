#!/bin/sh
set -e

python manage.py migrate --noinput
python manage.py makemigrations --merge --no-input || true   # harmless if no changes
python manage.py migrate --noinput
python manage.py seed
python manage.py runserver 0.0.0.0:8001
