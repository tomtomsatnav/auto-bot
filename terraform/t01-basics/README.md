# T01: Basics

**Runs fully on your Mac.** The `local` provider just writes files, so you can `apply` for real with no cloud account.

**Scenario:** This config generates an app's JSON config file plus a README pointing to it. It doesn't work.

**Goal:**
- `terraform apply` succeeds.
- `output/orders-api-dev.json` contains 3 replicas and debug `true`.
- `output/README.txt` contains the **actual path** of the config file.

```bash
terraform init
terraform validate
terraform plan
terraform apply
cat output/*.json output/README.txt
terraform destroy   # clean up when done
```

**Time box:** 15 minutes. There are **five** bugs. `validate` finds four; you'll only spot the fifth by reading the result.

<details><summary>Hint 1</summary>

Use the matching game: every `var.x` against `variables.tf`, and every `resource_type.name` against what's declared.
</details>

<details><summary>Hint 2</summary>

What type does each variable say it is? Is the default actually that type?
</details>

<details><summary>Hint 3</summary>

Open `output/README.txt` after applying. Is that the path, or just text? Look up "string interpolation" (`${...}`).
</details>

Solution: `solutions/terraform/t01.md`
