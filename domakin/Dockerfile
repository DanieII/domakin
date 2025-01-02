FROM python:3.13.1-slim-bookworm

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

RUN apt-get update && apt-get install -y nodejs npm

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
