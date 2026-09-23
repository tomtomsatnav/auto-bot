# T03: Modules

**Runs fully on your Mac.**

**Scenario:** A reusable `service-config` module is called twice, once for the API and once for a background worker. A module is just a folder of Terraform that you call like a function: inputs are its `variable`s, and outputs are its `output`s.

**Goal:**
- `apply` succeeds, and the worker's config says port `9000`.
- The JSON files land in `t03-modules/output/`, **not** somewhere inside `modules/`.

```bash
terraform init      # yes, init can fail too, so read it
terraform validate
terraform apply
find . -name "*.json"
```

**Time box:** 25 minutes. There are **four** bugs.

<details><summary>Hint 1</summary>

`init` fails first. Compare the `source` paths with the actual folder names.
</details>

<details><summary>Hint 2</summary>

Which module variables have no `default`? What happens if a caller doesn't pass them?
</details>

<details><summary>Hint 3</summary>

`module.<name>.<output>`: the output name must match an `output` block *inside the module*.
</details>

<details><summary>Hint 4</summary>

Look up the difference between `path.module` and `path.root`.
</details>

Solution: `solutions/terraform/t03.md`
