FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["gunicorn", "vendorhub_core.wsgi:application", "--bind", "0.0.0.0:8000"]
COPY . .