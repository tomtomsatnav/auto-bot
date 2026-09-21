# D01: Build context

**Scenario:** A colleague added a `.dockerignore` to speed up builds. Since then, the image won't build. They say "it was working before I tidied up".

**Symptoms:**
1. `docker build` fails.
2. Once you get it building, the container exits straight away.

**Goal:** `curl localhost:8000/health` returns `{"status":"ok"}`.

```bash
docker build -t d01 .
docker run --rm -p 8000:8000 d01
curl localhost:8000/health
```

**Time box:** 15 minutes. Talk out loud as you go.

<details><summary>Hint 1</summary>

Read the build error carefully. Which file does it say is missing? Does that file exist in the folder? If it exists, what could stop Docker from seeing it?
</details>

<details><summary>Hint 2</summary>

For the second problem, think about where `COPY app/ .` puts `main.py` inside the image, and where uvicorn is being told to look (`app.main`).
</details>

Solution: `solutions/docker/d01.md`
