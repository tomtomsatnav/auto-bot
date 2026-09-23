FROM python:3.12-slim

ARG DATABASE_URL=postgresql://billing:changeme@db:5432/billing
ARG APP_ENV=production

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8000
CMD ["uvicorn main:app --host 0.0.0.0 --port 8000"]
