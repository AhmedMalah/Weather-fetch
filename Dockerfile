FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
COPY weather_script.py .

RUN pip install --no-cache-dir -r requirements.txt

