from fastapi import FastAPI

app = FastAPI(title="inventory-api")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/items")
def list_items() -> list[dict]:
    return [{"sku": "A-100", "qty": 12}, {"sku": "B-200", "qty": 0}]
