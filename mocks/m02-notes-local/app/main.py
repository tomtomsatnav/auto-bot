import os
from pathlib import Path

from fastapi import FastAPI, HTTPException

NOTES_DIR = Path(os.environ["NOTES_DIR"])
NOTES_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="notes-api")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/notes")
def list_notes() -> list[str]:
    return sorted(p.stem for p in NOTES_DIR.glob("*.txt"))


@app.get("/notes/{name}")
def read_note(name: str) -> dict:
    path = NOTES_DIR / f"{name}.txt"
    if not path.exists():
        raise HTTPException(status_code=404, detail="Note not found")
    return {"name": name, "text": path.read_text()}


@app.put("/notes/{name}")
def write_note(name: str, body: dict) -> dict:
    (NOTES_DIR / f"{name}.txt").write_text(str(body.get("text", "")))
    return {"saved": name}
