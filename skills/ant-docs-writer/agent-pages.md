# Agent pages

Loaded when the page is one an agent reads: the CLI's embedded llms
reference and shipped agent skills.

Everything else in this skill applies to an agent page unless this
file states a divergence.

## Precision over elegance

- Precision outranks elegance. Never weaken or strengthen an
  instruction while editing around it.
- The one-instruction-per-sentence rule is stricter, not looser, than
  for a human page. An agent executes only the first half of a
  compound instruction, or runs both as one call.
- The 20/25-word caps (in SKILL.md) are targets, not
  limits. A longer sentence that removes ambiguity beats two shorter
  ones that leave it.
- Every distinction the page depends on is stated on the page itself,
  in the same words every time. Terms are never inferred.

## Structure

- An agent page is reached second, after an index. Each page is
  self-contained about its own resource and repeats nothing the index
  already owns: authentication, exit codes, IDs, paging.
- Pages under `docs/` use 4-space indented code blocks, never fences.
  The `llms` pages and shipped skills use fences instead.
- The shipped skills use no example label at all today. Leave that
  alone, or converge it deliberately, never in passing.

## Field claims and shell safety

- Backticked, entirely snake_case text is read by a build gate as an
  API field-existence claim. Never backtick one without confirming
  the field is real. A placeholder is lowercase and hyphenated inside
  angle brackets (`<db-id>`); never the underscored form of a real
  field name.
- A shell example must never swallow a `pgedge` call's exit status: no
  pipe, unchecked capture, or `&&` chain hiding a failure. Redirect to
  a file and check the status.
