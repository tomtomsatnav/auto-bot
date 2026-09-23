# T06: AWS IAM

**Offline AWS**, as in T04. (`aws_iam_policy_document` is built locally, so you can inspect the generated JSON in `plan` output.)

**Scenario:** An ECS task role that lets the orders API **read** files from the artifacts bucket, and nothing more. This is your home turf from security work, so lean into it in the interview.

**Goal:** `validate` and `plan` pass, the role would attach correctly when applied, the service can actually read objects, and the permissions follow least privilege.

```bash
terraform init
terraform validate
terraform plan
```

**Time box:** 25 minutes. There are **four** bugs.

<details><summary>Hint 1</summary>

A `data "aws_iam_policy_document"` produces an object. Which of its attributes is the JSON string that `assume_role_policy` wants? (Look at how `aws_iam_policy.s3_read` does it.)
</details>

<details><summary>Hint 2</summary>

Check the docs for `aws_iam_role_policy_attachment`. Does `role` want an ARN or a name?
</details>

<details><summary>Hint 3</summary>

`s3:ListBucket` applies to the *bucket*. `s3:GetObject` applies to *objects inside it*. Do those have the same ARN?
</details>

Solution: `solutions/terraform/t06.md`
