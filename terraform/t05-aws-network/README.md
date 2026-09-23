# T05: AWS networking

**Offline AWS**, as in T04.

**Scenario:** A standard VPC with a public and a private subnet in each of two availability zones, internet access for the public subnets, and a security group for a Postgres database that only the application should reach.

Draw it on paper first. It genuinely helps, and it's a great thing to do out loud in the interview.

**Goal:** `validate` and `plan` pass, and the design would actually work when applied.

```bash
terraform init
terraform validate
terraform plan
terraform console   # try: cidrsubnet("10.0.0.0/16", 8, 0)  then  cidrsubnet("10.0.0.0/16", 8, 1)
```

**Time box:** 30 minutes. There are **five** bugs: three caught by `validate`, one a logic bug that `plan` happily accepts, and one security issue.

<details><summary>Hint 1</summary>

`vpc_id` expects a string ID. What does `aws_vpc.main` on its own give you?
</details>

<details><summary>Hint 2</summary>

With `count`, `aws_subnet.public` is a list. Each association needs *one* subnet.
</details>

<details><summary>Hint 3</summary>

Use `terraform console` to work out every subnet's CIDR block. Do any clash?
</details>

<details><summary>Hint 4</summary>

Who can reach port 5432? Is that "only the application"?
</details>

Solution: `solutions/terraform/t05.md`
