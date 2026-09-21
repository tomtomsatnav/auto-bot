# T02: count and for_each

**Runs fully on your Mac.** This uses the `local` and `random` providers.

**Scenario:** Each service needs its own `.env` file with a generated database password.

**Goal:** `apply` creates `output/auth.env`, `output/payments.env` and `output/notifications.env`, each with a different password, and the output lists all three file paths.

```bash
terraform init
terraform validate
terraform apply
cat output/*.env
```

**Time box:** 25 minutes. There are **three** bugs.

**Part 2 (important):** Once it works, remove `"auth"` from the list and run `terraform plan`. Read the plan carefully: which files does it want to destroy or recreate, and why is that bad? Then refactor `local_file.env` to use `for_each` so removing one service only affects that service.

**Part 3 (review):** A secret is being written to a file. What would you flag about how it appears in `plan` output and state?

<details><summary>Hint 1</summary>

`for_each` needs a map or a *set*. You have a list. Look up the `toset()` function.
</details>

<details><summary>Hint 2</summary>

With `for_each`, resources are keyed by the item (`["auth"]`), not by a number (`[0]`).
</details>

<details><summary>Hint 3</summary>

When a resource uses `count`, `local_file.env` is a list of resources. How do you get one attribute from every item? Look up "splat expressions".
</details>

Solution: `solutions/terraform/t02.md`
