FROM python:3.7.5-slim-buster

COPY . /app

CMD python /app/main.py