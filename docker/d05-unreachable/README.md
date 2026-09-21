# D05: Unreachable and unhealthy

**Scenario:** The platform standard is that every service listens on **8080** inside the container and has a working health check. This service builds and "runs", but nothing can reach it, and the orchestrator keeps marking it unhealthy.

**Symptoms:**
1. `curl localhost:8080/health` fails.
2. After about 30 seconds, `docker ps` shows `(unhealthy)`.

**Goal:** Following the platform standard, the app listens on 8080 in the container, is reachable on `localhost:8080`, and shows `(healthy)`.

```bash
docker build -t d05 .
docker run -d --name d05 -p 8080:8080 d05
curl localhost:8080/health
docker ps   # watch the STATUS column
```

**Time box:** 20 minutes. There are **three** separate problems.

<details><summary>Hint 1</summary>

`docker exec d05 python -c "import urllib.request; print(urllib.request.urlopen('http://localhost:8000/health').read())"`. If that works inside the container but curl fails from your Mac, what does that tell you?
</details>

<details><summary>Hint 2</summary>

`docker inspect d05 --format '{{json .State.Health}}'` shows the health check output. What does it say about `curl`?
</details>

<details><summary>Hint 3</summary>

Does `EXPOSE` actually change which port the app listens on?
</details>

Solution: `solutions/docker/d05.md`
