# Cheat sheet

## Opening script (say this before touching anything)

> "First I'll read through to understand what this is meant to do. [One-sentence summary.] Then I'll [build it / run init and validate], work through errors one at a time, and verify each fix before moving on."

Then for each bug: **what I see → what I think it means → how I'll check → the fix → proof it worked.**

---

## Docker

### Commands
| Command | Use |
|---|---|
| `docker build -t name .` | Build (read from the **first** error, not the last line) |
| `docker build --no-cache -t name .` | Rule out stale cache |
| `docker build --progress=plain -t name .` | Full output from every step |
| `docker run --rm -p HOST:CONTAINER name` | Run in the foreground to see output directly |
| `docker ps -a` | Include exited containers; check the exit code |
| `docker logs <container>` | Why it crashed |
| `docker exec -it <container> sh` | Look around inside a running container |
| `docker run --rm -it --entrypoint sh name` | Get a shell in an image whose CMD crashes |
| `docker inspect <container> --format '{{json .State.Health}}'` | Health check output |
| `docker history name --no-trunc` | What each layer did (and any leaked build args) |
| `docker images` | Image sizes |

### Exit codes
- `0`: finished normally (for a server, that usually means the command ended when it shouldn't have)
- `1`: application error, so check the logs
- `126` or `127`: command not executable or not found (CMD problems, PATH, missing binary)
- `137`: killed, usually out of memory

### Usual suspects
- A file "not found" that exists → `.dockerignore` or build context
- `pip install` fails on slim → missing `gcc` or `-dev` headers
- `executable file not found` → exec-form CMD split wrongly, or `PATH`
- `KeyError` or missing config → `ARG` vs `ENV`, or env var name mismatch
- `PermissionError` → non-root user and root-owned directory; `chown` before `USER`
- Runs but unreachable → `0.0.0.0` bind; port mismatch; `EXPOSE` does nothing by itself
- Unhealthy → `curl` isn't in slim images; wrong port in the health check
- Slow rebuilds → code copied before dependencies

---

## Terraform

### The loop
```bash
terraform init          # after any provider or module change
terraform fmt           # tidy formatting, which also catches some syntax slips
terraform validate      # syntax, references, types
terraform plan          # what will actually change: read the summary line
```

### Useful extras
| Command | Use |
|---|---|
| `terraform console` | Evaluate expressions: `cidrsubnet(...)`, `var.x`, `toset(...)` |
| `terraform state list` | What Terraform thinks exists |
| `terraform state show <addr>` | Details of one resource |
| `terraform plan -target=<addr>` | Focus on one resource while debugging (not for normal use) |
| `TF_LOG=DEBUG terraform plan` | Provider and API detail (very noisy) |

### Reading an error
```
Error: <WHAT is wrong>
  on <FILE> line <N>, in <BLOCK>:
  <the offending line>
<HINT - often says exactly what to do>
```

### Usual suspects
- **Matching game:** `var.x` ↔ `variable "x"`; `type.name` ↔ `resource "type" "name"`; `module.m.out` ↔ `output "out"` inside the module
- **Quotes:** text vs reference; use `"${ref}"` to put a reference inside text
- **Types:** string / number / bool / list / map; `[ ]` for lists, `{ }` for maps
- **count** → `res[0]`, `res[*].attr`; **for_each** → `res["key"]`, needs a set or map (`toset()`)
- **Object vs attribute:** `aws_vpc.main` vs `aws_vpc.main.id`; `data.x.y` vs `data.x.y.json`
- **Allowed values** are case-sensitive (`"Enabled"`, not `"enabled"`)
- **Required blocks and arguments:** check the Argument Reference
- **Passes plan, fails apply:** naming rules, name vs ARN, CIDR overlaps, service constraints (Fargate needs `awsvpc`)
- **Passes apply, fails at runtime:** ports across files, IAM resource ARNs (`bucket` vs `bucket/*`), log group names
- **Plan wants to destroy on a refactor** → `moved` blocks

### Docs
Search **"terraform <resource_type>"** and go to `registry.terraform.io`. Then read, in order: **Example Usage → Argument Reference → Attribute Reference.**

---

## Security points to raise (your strength, so use it)
- Non-root containers; secrets never baked into images
- `.dockerignore` to keep `.env`, `.git` and `*.tfstate` out of images
- State files contain secrets: remote backend, encrypted, access-controlled
- `0.0.0.0/0` on anything that isn't public HTTP(S) is a red flag
- Security group references over CIDR ranges
- IAM least privilege: no `*:*`; split bucket-level and object-level resources
- S3: all four public access block settings on
- Immutable image tags, not `:latest`
