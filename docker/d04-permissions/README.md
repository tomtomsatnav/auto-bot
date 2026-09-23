# D04: Permissions

**Scenario:** Security review asked for containers to stop running as root, so `USER appuser` was added. Now the container crashes. A colleague's proposed fix is to delete the `USER` line. **Don't accept that fix.**

**Symptom:** The container exits on startup.

**Goal:** Runs as `appuser` (check with `docker exec <container> whoami`), and this works:

```bash
docker build -t d04 .
docker run -d --name d04 -p 8000:8000 d04
curl -X PUT localhost:8000/notes/hello -H 'Content-Type: application/json' -d '{"text": "hi"}'
curl localhost:8000/notes
```

**Stretch:** Remove the container and start a new one. Are your notes still there? How would you fix that?

**Time box:** 20 minutes.

<details><summary>Hint 1</summary>

The container exits, so use `docker ps -a` and `docker logs d04`. What kind of error is it, and which path?
</details>

<details><summary>Hint 2</summary>

Who owns `/app` inside the image? `WORKDIR` creates directories as whichever user is active at that point. Which user is that?
</details>

<details><summary>Hint 3 (stretch)</summary>

Look up `docker volume create` and the `-v` flag.
</details>

Solution: `solutions/docker/d04.md`
