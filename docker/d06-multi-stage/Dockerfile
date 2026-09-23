# ---- build stage ----
FROM python:3.11 AS builder

WORKDIR /build
COPY requirements.txt .
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# ---- runtime stage ----
FROM python:3.12-slim

WORKDIR /app
COPY --from=builder /build/venv /opt/venv
COPY main.py .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
