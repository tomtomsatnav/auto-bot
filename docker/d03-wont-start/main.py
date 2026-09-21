import os

from fastapi import FastAPI

# Fail fast if required config is missing. This is deliberate.
DATABASE_URL = os.environ["DATABASE_URL"]
APP_ENV = os.getenv("APP_ENV", "development")

app = FastAPI(title="billing-api")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "env": APP_ENV}


@app.get("/config")
def config() -> dict:
    # Only expose the host, never the credentials
    host = DATABASE_URL.split("@")[-1].split("/")[0]
    return {"database_host": host, "env": APP_ENV}
