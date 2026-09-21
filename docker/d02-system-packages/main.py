import psycopg2
from fastapi import FastAPI

app = FastAPI(title="reporting-api")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "db_driver": psycopg2.__version__}
