FROM python:3.7.5-slim-buster

COPY . /app

RUN python /app/main.py