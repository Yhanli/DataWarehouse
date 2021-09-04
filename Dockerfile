FROM python:3.8.12-alpine
RUN apk add --update --no-cache --virtual gcc g++ musl-dev python3-dev libffi-dev openssl-dev

RUN pip install --upgrade pip
RUN pip install pipenv
ENV PROJECT_DIR /var/www/html

COPY . ${PROJECT_DIR}/
WORKDIR ${PROJECT_DIR}

#COPY ./req.txt .

#RUN pip install -r req.txt
#RUN pipenv run pip install -U pip
RUN pipenv sync

WORKDIR ${PROJECT_DIR}/DataWarehouse

ENTRYPOINT ["sh", "./entrypoint.sh"]