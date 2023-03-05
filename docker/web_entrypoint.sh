#!/bin/bash
echo "Apply database migrations"
python manage.py migrate --noinput

echo "Start Server"
python manage.py runserver 0.0.0.0:8000
