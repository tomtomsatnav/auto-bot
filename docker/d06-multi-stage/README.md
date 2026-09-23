# D06: Multi-stage build

**Scenario:** Someone converted the Dockerfile to a multi-stage build to shrink the image. It hasn't worked since. This is the hardest Docker drill: each fix reveals the next error.

**Goal:** It builds, runs and serves `/health`, and the final image is noticeably smaller than a single-stage `python:3.12` build (compare with `docker images`).

```bash
docker build -t d06 .
docker run --rm -p 8000:8000 d06
curl localhost:8000/health
```

**Time box:** 30 minutes. There are **three** problems.

<details><summary>Hint 1</summary>

The build error mentions a path. Where did the builder stage actually create the virtualenv?
</details>

<details><summary>Hint 2</summary>

"executable file not found in $PATH": the venv's `bin` folder exists, but does the shell know to look there? Look up `ENV PATH`.
</details>

<details><summary>Hint 3</summary>

If you get `ModuleNotFoundError` even though the packages were installed, run `docker run --rm -it --entrypoint sh d06`, then `ls /opt/venv/lib/`. Compare that with the Python version in the runtime image.
</details>

Solution: `solutions/docker/d06.md`
