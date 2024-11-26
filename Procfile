release: python manage.py migrate --noinput
web: waitress-serve --port=$PORT mewconomics.wsgi:application