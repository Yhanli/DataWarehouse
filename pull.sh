sudo git pull
pipenv sync
pipenv run python DataWarehouse/manage.py migrate
pipenv run python DataWarehouse/manage.py collectstatic --noinput