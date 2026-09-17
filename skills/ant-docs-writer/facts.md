# Facts

Loaded by fix, overhaul and new page. A restyle and a restructure
verify nothing against source, so nothing here binds them.

A fix takes the source for each claim it was asked to change, and adds
no fact beyond those. A fix of several claims is still one fix: work
them together, and keep each one's source beside it.

## Ask first

Your reader is a constant: a competent developer who does not know
this product. What varies page to page is where the truth lives, and
that decides both what you can write and the page's shape. Ask before
gathering, on a fix, overhaul or new page:

- Which codebases may be read. A page about another framework needs
  facts about that framework, not from reading pgEdge source.
- What structure to compare the page against, and name it if borrowed
  from elsewhere, so a fresh writer can reproduce or question it.
- Whether real resources may be created, run and torn down to verify
  behavior. Where the answer is no, say so on the artifact.
- Where measurements are recorded. Get the probe-log path if one
  exists; say so rather than treating an unrecorded measurement as
  known.

Look up everything else rather than asking. A skill that asks what it
could have discovered spends the requester's scarcest resource.

## Source hierarchy

- Treat the generated command reference as truth for verbs, flags,
  defaults and help text: it is produced from the command tree.
- Read `pgedge llms`, index first then module, for the agent
  reference.
- Read the product's own code for the order of operations, what is
  validated locally, and which exit status each failure takes.
- Treat the vendored specs as what the platform says about itself, and
  probe logs as what someone watched it do.
- When two sources disagree, the stronger wins: a measurement beats a
  spec, a generated reference cannot be wrong about a flag, and a
  sibling page settles nothing.

On an overhaul and a new page, build the fact list from these sources
before writing; record each fact with the file and line that settles
it.

## What may go on the page

- On a fix, an overhaul and a new page: every command and flag exists
  in the generated reference, and every behavioral claim traces to a
  live capture, a spec field, the product's own source, or an
  existing gated page.
- A claim with no source stays out, and what is true goes in its
  place. Record the source as you write the claim.
- Attribute a runtime number only to a surface you checked. Where you
  cannot source the display surface, print the number without the
  attribution sentence, and never attribute a number to a screenshot.
- On an overhaul or a new page, a rewrite may add a fact the checklist
  requires, sourced and explained in the pull request, and may add a
  step the checklist requires when it follows from a sourced fact;
  say in the pull request which fact the step follows from. Scope
  every claim this way to the exact command and module actually
  checked, per "Editing existing text" in writing.md.

## Screenshots

A screenshot is not a source. It is evidence something appeared on
screen once, and it goes stale silently.

- Settle a mismatch between prose and a kept image against the
  product, never by trusting either on its own.
- Where the product agrees with the image, correct the prose. Where
  the product agrees with the prose, flag the image for recapture in
  the pull request and say nothing on the page about the discrepancy.
- A runtime-only value, such as a console-fetched price, may still be
  stated if attributed to what the console shows. Never present it as
  a contract, and re-check it whenever the page is touched.

## Absence claims

State an absence in the form "no X does Y", scoped to exactly what was
checked: a reference for a CLI claim, a screen for a console claim.
Follow it with what the reader should do instead, and record the
search that supports it in the pull request.

## The fact list

Build it as a file, written before any prose and completed as the
draft is written, then handed over with the draft. Reporting that a
fact list was built does not count as building it.

An entry has these fields:

| Field | Value |
|---|---|
| fact | The claim. |
| source | A file:line, never a ledger id alone. |
| disposition | keep / adapt / drop, with a reason for adapt or drop. |
| heading | Filled in when drafted. |
| ledger id | Overhaul only. |

On a new page, every fact keeps `disposition: keep`, since there is no
ledger to adapt against. On a fix, the same fields go directly into
the hand-back instead of a separate file, one row per claim changed.

## The ledger (overhaul only)

On an overhaul, dispatch a separate agent to build the ledger from the
old page before any writing starts, since the writer never reads that
page. The ledger records what the old page covered, never what is
true, and stays apart from the fact list. Never let an entry cross
from the ledger to the fact list without being settled against source
first.

The writer never reads the old page, not once and not for reference;
read the ledger instead. Filter the excluded old page out of every
glob search, not only avoid opening it directly: two writers in one
run were exposed to it exactly that way.

An entry is three fragment lines: a note under about 15 words, the
source file:line, and a status:

| Status | Means |
|---|---|
| V | Verified against something other than a hand-written page. The generated reference is exempt from that exclusion; a sibling docs page is not. |
| C | A spec description a measurement contradicts. A measurement outranks upstream documentation. |
| U | Unverified. |
| S | (situation, as stated on the old page) |

Write an entry as the situation, never as the missing thing: an entry
framed as an absence reaches the page as an absence, and no gate can
see it.

Group the ledger by topic, sort headings and entries alphabetically,
and number from F1 in that order. Tell the writer explicitly that this
order carries no editorial judgment and must not be followed.
