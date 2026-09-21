from fastapi import FastAPI

app = FastAPI(title="pricing-api")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/price/{sku}")
def price(sku: str) -> dict:
    return {"sku": sku, "price_gbp": 9.99}
