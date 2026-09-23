# D03: Won't start

**Scenario:** The billing API image builds fine in CI, but the container never starts.

**Symptom:** `docker run` fails immediately. Once that's fixed, the app crashes on startup.

**Goal:**
- The container starts and `/health` returns `"env": "production"`.
- `DATABASE_URL` is supplied **when the container runs**, not baked into the image.
- `/config` returns `"database_host": "db.internal:5432"`.

```bash
docker build -t d03 .
docker run --rm -p 8000:8000 d03
# once fixed, you should be running something like:
docker run --rm -p 8000:8000 -e DATABASE_URL=postgresql://billing:secret@db.internal:5432/billing d03
```

**Time box:** 20 minutes.

<details><summary>Hint 1</summary>

Read the `docker run` error word for word. What executable does Docker think it's looking for? Compare the `CMD` line with the ones from earlier drills.
</details>

<details><summary>Hint 2</summary>

`docker logs` or the terminal output will show a `KeyError`. Look up the difference between `ARG` and `ENV`: which one still exists once the container is running?
</details>

<details><summary>Hint 3</summary>

Try `docker history d03 --no-trunc`. What can anyone with the image see? Why is that a problem for a database URL?
</details>

Solution: `solutions/docker/d03.md`
