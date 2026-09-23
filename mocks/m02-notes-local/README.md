# M02: Mock interview, notes service (fully runnable)

**Runs completely on your Mac.** Terraform uses the Docker provider to build the image and run the container, so every fix can be tested for real, including `apply`.

> "This is a small notes service. Terraform builds the image and runs it locally with persistent storage. It worked on the original author's machine, apparently. Can you get it running and talk us through what you find?"

**What "done" looks like:**

```bash
cd infra
terraform init
terraform apply
curl localhost:8080/health
curl -X PUT localhost:8080/notes/todo -H 'Content-Type: application/json' -d '{"text": "prep for Faculty"}'
curl localhost:8080/notes/todo
docker ps          # STATUS should say (healthy) after about 30 seconds

# Persistence test: notes must survive the container being replaced
terraform apply -replace=docker_container.notes
curl localhost:8080/notes/todo

terraform destroy  # clean up
```

**Time box:** 45 minutes. There are **six** issues across the Terraform and Dockerfile. Your tools: `terraform validate/plan/apply`, `docker ps -a`, `docker logs notes-api`, `docker exec`, `docker inspect`.

**Mac note:** The Docker provider connects to `unix:///var/run/docker.sock`. Docker Desktop provides this by default (Settings → Advanced → "Allow the default Docker socket to be used"). If you use Colima or OrbStack instead, set `host` in the provider block to that tool's socket path.

**No hints.** Afterwards, compare with `solutions/mocks/m02.md`.
