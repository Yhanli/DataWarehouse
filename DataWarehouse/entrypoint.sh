pipenv run python manage.py migrate --no-input
pipenv run python manage.py collectstatic --no-input

pipenv run gunicorn --workers 5 DataWarehouse.wsgi:application --bind 0.0.0.0:8000
