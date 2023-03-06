FROM python:latest

WORKDIR /usr/src/app/

COPY . .
COPY requirements.txt .

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "oc_lettings_site.wsgi", "-b :8080"]