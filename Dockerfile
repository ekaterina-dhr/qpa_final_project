FROM python:3.10-alpine

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt /app

COPY ./ ./
