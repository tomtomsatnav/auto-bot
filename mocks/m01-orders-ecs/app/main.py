import os

from fastapi import FastAPI

APP_ENV = os.getenv("APP_ENV", "development")

app = FastAPI(title="orders-api")

ORDERS = [
    {"id": 1001, "status": "shipped"},
    {"id": 1002, "status": "processing"},
]


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "env": APP_ENV}


@app.get("/orders")
def list_orders() -> list[dict]:
    return ORDERS
