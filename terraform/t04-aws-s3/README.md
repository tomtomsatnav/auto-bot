# T04: AWS S3 bucket

**Offline AWS.** `providers.tf` uses fake credentials so `init`, `validate` and `plan` work without an AWS account. `apply` won't work, and that's expected.

**Scenario:** A private, versioned, encrypted artifacts bucket for build outputs.

**Goal:** `validate` and `plan` pass cleanly, **and** you'd be happy to approve this in a code review, knowing it would succeed when applied for real.

```bash
terraform init
terraform validate
terraform plan
```

**Time box:** 20 minutes. There are **four** bugs: two that `validate` catches, and two that only careful reading (or a real `apply`) would catch.

**Docs you'll want open:** search "terraform aws_s3_bucket_versioning" and "terraform aws_s3_bucket_public_access_block", and read the Argument Reference.

<details><summary>Hint 1</summary>

For the validation error on versioning, read the list of allowed values in the error message. Case matters.
</details>

<details><summary>Hint 2</summary>

Work out what the bucket name will actually be. Look up the S3 bucket naming rules. Would AWS accept it?
</details>

<details><summary>Hint 3</summary>

Read each of the four public access block settings in the docs. Is this bucket fully private?
</details>

Solution: `solutions/terraform/t04.md`
