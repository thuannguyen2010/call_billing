#!/bin/bash
echo "--> Starting web process"
python manage.py migrate
python manage.py runserver 0.0.0.0:8000