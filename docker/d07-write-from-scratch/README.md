# D07: Write a Dockerfile from scratch

**Scenario:** The interview email mentions "a simple Dockerfile example". This drill is that: a blank page.

Write a `Dockerfile` **and** `.dockerignore` for this app, without looking at earlier drills. Requirements:

1. Uses a pinned, small Python 3.12 base image.
2. Dependencies are installed in their own cached layer, so editing `main.py` doesn't reinstall packages.
3. Runs as a non-root user.
4. Reachable on `localhost:8000` from your Mac.
5. `APP_ENV` defaults to `production` in the image, but can be overridden at runtime.
6. Has a `HEALTHCHECK` that works in a slim image.
7. `.dockerignore` keeps out things that shouldn't be in an image.

```bash
docker build -t d07 .
docker run -d --name d07 -p 8000:8000 d07
curl localhost:8000/health                       # env should be "production"
docker run --rm -e APP_ENV=staging -p 8001:8000 d07   # env should be "staging"
docker exec d07 whoami                           # should NOT be root
```

**Time box:** 20 minutes. Then repeat it on another day. It should get faster each time.

Model answer: `solutions/docker/d07.md`
