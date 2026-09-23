# Facts

Take from the brief which codebases may be read, whether real
resources may be created to verify behavior, and where probe logs
live. Ask only when the brief is silent and someone is there to
answer; look up everything else.

## Source hierarchy

| Source | Authority for |
|---|---|
| Generated command reference | Verbs, flags, defaults, help text — produced from the command tree |
| `pgedge llms` (index, then module) | The agent reference |
| Product's own code | Order of operations, local validation, exit status per failure |
| Vendored specs | What the platform says about itself |
| Probe logs | What someone watched it do |

When two disagree, the stronger wins: a measurement beats a spec, a
generated reference can't be wrong about a flag, a sibling page
settles nothing.

Build the fact list from these before
writing; record each fact with the file and line that settles it.

## What may go on the page

- Every command and flag exists in the generated reference, and every
  behavioral claim traces to a live capture, a spec field, the
  product's own source, or an existing gated page.
- A claim with no source stays out; write what's true in its place,
  and record the source as you write the claim.
- Attribute a runtime number only to a surface you checked. Where you
  can't source the display surface, print the number without the
  attribution sentence — never attribute a number to a screenshot.
- A rewrite may add a fact the checklist requires, sourced and
  explained in the pull request, and a step that follows from a
  sourced fact, saying which fact it follows from. Scope every claim
  to the exact command/module checked, per "Editing existing text" in
  writing.md.

## Screenshots

A screenshot is not a source — it's evidence something appeared on
screen once, and it goes stale silently.

- Settle a mismatch between prose and a kept image against the
  product, never by trusting either alone.
- Product agrees with the image → correct the prose. Product agrees
  with the prose → flag the image for recapture in the pull request;
  say nothing on the page about the discrepancy.
- A runtime-only value (a console-fetched price) may be stated if
  attributed to what the console shows — never as a contract, and
  re-checked whenever the page is touched.

## Absence claims

State an absence as "no X does Y", scoped to exactly what was checked
(a reference for a CLI claim, a screen for a console claim). Follow
it with what to do instead, and record the supporting search in the
pull request.

## The fact list

Build it as a file, written before any prose and completed as the
draft is written, then handed over with it. Reporting that a fact
list was built does not count as building it.

| Field | Value |
|---|---|
| fact | The claim. |
| source | A file:line, never a ledger id alone. |
| disposition | keep / adapt / drop, with a reason for adapt or drop. |
| heading | Filled in when drafted. |
| ledger id | Overhaul only. |

New page: every fact keeps `disposition: keep` — there's no ledger to
adapt against.
