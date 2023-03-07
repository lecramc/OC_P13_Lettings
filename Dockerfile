FROM python:latest

WORKDIR /usr/src/app/

COPY . .
COPY requirements.txt .

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip install -r requirements.txt

EXPOSE 8000

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--workers", "1","oc_lettings_site.wsgi"]