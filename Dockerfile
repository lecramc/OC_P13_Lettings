FROM python:latest

WORKDIR /usr/src/app/

COPY . .
COPY requirements.txt .

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip install -r requirements.txt

EXPOSE 8000

RUN python oc_lettings_site/manage.py collectstatic --noinput

CMD ["gunicorn", "oc_lettings_site.wsgi"]