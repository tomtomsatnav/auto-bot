# D02: System packages

**Scenario:** The reporting team added PostgreSQL support. `pip install` works on their laptops, but the image build now fails.

**Symptom:** `docker build` fails during `pip install`.

**Goal:** The image builds and `/health` returns the psycopg2 version. Then review the Dockerfile as you would in a code review: there are **two** more things you'd flag, even though they don't break the build.

```bash
docker build -t d02 .
docker run --rm -p 8000:8000 d02
curl localhost:8000/health
```

**Time box:** 20 minutes.

<details><summary>Hint 1</summary>

Scroll up through the pip output to the first real error, not the last line. What program does it say it can't find?
</details>

<details><summary>Hint 2</summary>

`psycopg2` is compiled from source. `slim` images leave out compilers and development headers to stay small. What needs installing with `apt-get`, and in which `RUN` step?
</details>

<details><summary>Hint 3 (review points)</summary>

Think about layer caching: what happens to a separate `RUN apt-get update` layer weeks later? And what triggers `pip install` to rerun on every code change?
</details>

Solution: `solutions/docker/d02.md`
