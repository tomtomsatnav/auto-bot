from fastapi import FastAPI

app = FastAPI(title="catalogue-api")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/products")
def products() -> list[dict]:
    return [{"id": 1, "name": "Widget"}, {"id": 2, "name": "Gadget"}]
