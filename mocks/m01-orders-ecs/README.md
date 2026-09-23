# M01: Mock interview, orders service on ECS

**Treat this exactly like the interview.** Set a 50-minute timer, share your screen with nobody in particular (or record yourself), and **talk the whole time**.

> "Hi Tom, thanks for joining. This is our orders service. It runs as a container on AWS ECS Fargate. The deployment's been failing, and a colleague who worked on it has gone on holiday. We've got the app, the Dockerfile and the Terraform. Could you take a look and talk us through how you'd investigate?"

**What "done" looks like:**
- The image builds, runs locally and serves `/health` on `localhost:8000`.
- `terraform validate` and `plan` pass in `infra/`.
- The Terraform would actually work when applied, and traffic could reach the container.
- You've flagged anything you'd raise in a code review.

```bash
# Docker
docker build -t orders-api .
docker run --rm -p 8000:8000 orders-api

# Terraform (offline mode, so apply won't work, as expected)
cd infra
terraform init
terraform validate
terraform plan
```

**There are around ten issues** across the Dockerfile and Terraform, from "won't build" to "would fail on apply" to "I'd flag this in review". Several only show up if you compare **files against each other**: the port the app uses, the port the container declares, the port the firewall allows.

**No hints for mocks.** Use the docs, as you would in the interview. Afterwards, compare with `solutions/mocks/m01.md` and score yourself using the rubric in the root README.
