# Platform debugging drills

Hands-on Docker and Terraform debugging practice, modelled on a platform engineering technical interview: *"debug some Terraform configurations, fix a Docker image build, and write a simple Dockerfile, while talking us through your approach."*

Every exercise is broken on purpose. Each README describes the **symptom**, not the cause, as in real life.

## Setup (MacBook)

```bash
# Docker Desktop: https://www.docker.com/products/docker-desktop/  (then open it once)
docker --version

# Terraform
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
terraform -version

# Optional but handy
brew install jq
```

Check both work before the interview day, on the laptop you'll actually use.

## What's inside

| Folder | Runs | What it trains |
|---|---|---|
| `docker/d01`–`d06` | Fully local | Build context, system packages, ARG/ENV, permissions, ports and health checks, multi-stage builds |
| `docker/d07` | Fully local | Writing a Dockerfile from a blank page |
| `terraform/t01`–`t03` | Fully local (`apply` works) | References, types, count/for_each, modules |
| `terraform/t04`–`t06` | Offline AWS (`validate` and `plan` work; `apply` doesn't) | Realistic S3, VPC and IAM configs |
| `terraform/t07` | Fully local | State: refactoring without destroying anything |
| `mocks/m01` | Docker local + offline AWS | Full mock interview: container on ECS Fargate |
| `mocks/m02` | Fully local | Full mock interview: Terraform deploying Docker, with every fix testable |
| `solutions/` | – | Fixes, explanations and interview phrasing. **Don't peek early.** |

"Offline AWS" uses fake credentials so you can `plan` without an AWS account. Some bugs in those drills only fail on a real `apply`, so you have to find them by reading, as a reviewer would.

## How to practise

1. **Set a timer** for the time box in each README.
2. **Talk out loud the whole time.** It feels odd, but it's half of what the interviewers score. Record yourself sometimes.
3. **Use the docs, not the solutions.** The interview is open book, so practise finding answers in the Terraform Registry and Docker docs.
4. Getting stuck? Open the hints in the README **one at a time**.
5. After finishing, read the solution's "Say this in the interview" section, even if you got everything.
6. **Reset and repeat** the ones you found hard a few days later:
   ```bash
   git checkout -- .          # restore all broken files
   git clean -fdX             # remove Terraform state, .terraform and output/ (ignored files only)
   ```

## Suggested two-week plan (about 4 hours a day)

| Days | Focus |
|---|---|
| 1–2 | D01–D04, then D07 from memory |
| 3–4 | D05–D06, then D07 again (it should be faster) |
| 5–6 | T01–T03 (local, apply everything) |
| 7–8 | T04–T06 (AWS), with the Registry docs open |
| 9 | T07, then redo whichever T drills felt shakiest |
| 10 | **M02** mock, timed |
| 11 | **M01** mock, timed |
| 12 | Reset everything; redo both mocks and any weak drills |
| 13 | Light review of `CHEATSHEET.md`; D07 once more |
| 14 | Rest. Check your laptop setup and screen sharing. |

## Self-scoring rubric (for mocks)

Score each 1–3 after every mock:

| Area | 1 | 3 |
|---|---|---|
| **Approach** | Jumped straight to editing | Read and explained the system first, then ran init/validate/plan or build/run |
| **Reading errors** | Guessed | Quoted the error, found the line, explained the cause |
| **Communication** | Silent stretches | Narrated hypotheses: "I think X because Y, so I'll check Z" |
| **Verification** | Assumed fixed | Proved it: curl, `docker ps`, plan summary, logs |
| **Beyond the bug** | Only fixed errors | Raised security, caching and review points without being asked |
| **Collaboration** | Solo | Checked assumptions: "Is it OK if I change the Dockerfile rather than the app?" |

## Publishing this repo

```bash
cd platform-debugging-drills
git init && git add . && git commit -m "Initial debugging drills"
gh repo create platform-debugging-drills --private --source=. --remote=origin --push
```
(No `gh`? Run `brew install gh && gh auth login` first, or create the empty private repo on github.com and follow its "push an existing repository" instructions.)
