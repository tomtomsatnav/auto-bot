import os

from fastapi import FastAPI

APP_ENV = os.getenv("APP_ENV", "development")

app = FastAPI(title="accounts-api")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "env": APP_ENV}
