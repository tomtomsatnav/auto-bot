import os
from pathlib import Path

from fastapi import FastAPI

UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", "/app/data/uploads"))
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="docs-api")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.put("/notes/{name}")
def write_note(name: str, body: dict) -> dict:
    path = UPLOAD_DIR / f"{name}.txt"
    path.write_text(str(body.get("text", "")))
    return {"saved": str(path)}


@app.get("/notes")
def list_notes() -> list[str]:
    return sorted(p.stem for p in UPLOAD_DIR.glob("*.txt"))
