FROM python:latest

ARG sentry_dsn
ENV SENTRY_DSN $sentry_dsn


WORKDIR /usr/src/app/

COPY . .
COPY requirements.txt .

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip install -r requirements.txt

EXPOSE 8000

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind","0.0.0.0:8000","oc_lettings_site.wsgi"]