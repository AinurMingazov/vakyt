FROM python:3.12.11-slim
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

