pipenv run python manage.py migrate --noinput
pipenv run python manage.py collectstatic --noinput

pipenv run gunicorn --workers 5 DataWarehouse.wsgi:application --bind 0.0.0.0:8000
