# T07: Refactor without destroying anything

**Runs fully on your Mac.** This is about **state**: Terraform's record of what it created. There's nothing "broken" in the code, but applying it as-is would cause an outage in real life.

**Steps:**

```bash
# 1. Create the "production" infrastructure
terraform init
terraform apply
cat output/*.txt           # note the pet name, e.g. "api on quick-badger"

# 2. A colleague refactored the code (renamed things, switched to for_each)
cp v2/main.tf main.tf
terraform plan
```

Read that plan. It wants to **destroy** everything and **create** it again, including a brand-new random name. In real life that could be a database or a load balancer, so imagine the outage.

**Goal:** Change the code (not the state file by hand) so `terraform plan` shows the resources being **moved**, with **0 to add, 0 to change, 0 to destroy**. Then apply, and check that the pet name hasn't changed.

**Time box:** 25 minutes.

<details><summary>Hint 1</summary>

`terraform state list` shows what Terraform thinks exists, using the *old* addresses.
</details>

<details><summary>Hint 2</summary>

Search "terraform moved block". You need one for each resource that changed address.
</details>

<details><summary>Hint 3</summary>

A for_each resource's address includes its key: `local_file.service["api"]`.
</details>

To reset and try again: `rm -rf .terraform* terraform.tfstate* output && git checkout main.tf`.

Solution: `solutions/terraform/t07.md`
