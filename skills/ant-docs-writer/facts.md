# Facts

Loaded by fix, overhaul and new page. Restyle and restructure verify
nothing against source, so nothing here binds them.

A fix takes the source for each claim it was asked to change, and
adds no fact beyond those. Several claims are still one fix: work
them together, source kept beside each.

## Ask first

Your reader is a constant: a competent developer who doesn't know
this product. What varies page to page is where the truth lives,
which decides both what you can write and the page's shape. Ask
before gathering, on a fix, overhaul or new page:

- Which codebases may be read — a page about another framework needs
  facts about that framework, not pgEdge source.
- What structure to compare the page against, named if borrowed from
  elsewhere, so a fresh writer can reproduce or question it.
- Whether real resources may be created, run and torn down to verify
  behavior; say so on the artifact where the answer is no.
- Where measurements are recorded — get the probe-log path if one
  exists; say so rather than treating an unrecorded measurement as
  known.

Look up everything else rather than asking. A skill that asks what it
could have discovered spends the requester's scarcest resource.

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

On an overhaul and a new page, build the fact list from these before
writing; record each fact with the file and line that settles it.

## What may go on the page

- Fix, overhaul, new page: every command and flag exists in the
  generated reference, and every behavioral claim traces to a live
  capture, a spec field, the product's own source, or an existing
  gated page.
- A claim with no source stays out; write what's true in its place,
  and record the source as you write the claim.
- Attribute a runtime number only to a surface you checked. Where you
  can't source the display surface, print the number without the
  attribution sentence — never attribute a number to a screenshot.
- Overhaul, new page: a rewrite may add a fact the checklist
  requires, sourced and explained in the pull request, and a step
  that follows from a sourced fact, saying which fact it follows
  from. Scope every claim to the exact command/module checked, per
  "Editing existing text" in writing.md.

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
adapt against. Fix: the same fields go directly into the hand-back
instead of a separate file, one row per claim changed.

## The ledger (overhaul only)

Dispatch a separate agent to build the ledger from the old page
before any writing starts — the writer never reads that page. The
ledger records what the old page covered, never what is true, and
stays apart from the fact list. Never let an entry cross from ledger
to fact list without being settled against source first.

The writer never reads the old page, not once, not for reference —
read the ledger instead. Filter the excluded page out of every glob
search too, not just avoid opening it directly: a search that returns
it is exposure just the same.

An entry is three fragment lines: a note under ~15 words, the source
file:line, and a status:

| Status | Means |
|---|---|
| V | Verified against something other than a hand-written page. The generated reference is exempt from that exclusion; a sibling docs page is not. |
| C | A spec description a measurement contradicts — a measurement outranks upstream documentation. |
| U | Unverified. |
| S | (situation, as stated on the old page) |

Write an entry as the situation, never as the missing thing: framed
as an absence, it reaches the page as an absence, and no gate can see
it.

Group by topic, sort headings and entries alphabetically, number from
F1 in that order — and say so to the writer: this order carries no
editorial judgment and must not be followed as the page's order.
