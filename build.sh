#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

: '
DJANGO_SUPERUSER_USERNAME=admin2 DJANGO_SUPERUSER_PASSWORD=pestaninha123 \
python manage.py createsuperuser --email=vitorpestanatr@gmail.com --noinput
 '