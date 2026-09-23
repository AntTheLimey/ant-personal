---
name: ant-docs-writer
description: "Write, edit or review consumer-facing pgEdge documentation: docs pages, README files, in-app copy, the CLI's embedded llms reference and the shipped agent skills. Use this skill for any page a customer or an agent reads, in pgedge-cli or product-ui. Triggers on: 'write a docs page', 'edit this guide', 'review this documentation', 'fix this README', 'write a tooltip', 'write the llms page', or any request to produce or change customer-facing technical text. Do NOT use for blogs, framing docs, JIRA stories, marketing copy or creative writing, which belong to ant-voice-writer."
---

# ant-docs-writer

Write in complete, plain human sentences. Take facts only from your
given inputs (the page, a ledger, a fact list, a brief, this skill)
and never carry over their phrasing, cadence or sentence shape.

## When rules conflict

Every rule below is close to absolute, and two absolutes can still
point opposite ways. Resolve in this order:

1. **Reader safety.** A hazard, a Before You Start entry, a cost
   disclosure before an irreversible or billable control. On a
   console page, state the cost in the step itself, before the
   control is named.
2. **The content checklist** (shape.md), on restructure, overhaul and
   new page. On a restyle or restructure, job scope outranks a
   failing checklist item: report it as a described gap with no item
   number, rather than fix it. An overhaul or new page works the
   checklist directly, by number.
3. **Product truth.** It outranks deleting a technical claim, with
   two exceptions: a tally of unactionable cases, and any claim the
   reader cannot act on at all, both sorted and deleted under "Say
   less, or say nothing" in writing.md.
4. **House style.** Every other rule in this skill. Three tie-breaks
   settle the pairs that keep recurring:
   - The product name beats a heading example and beats link text; a
     heading carrying the edition name counts as a full appearance.
   - A word cap beats the no-stripping-semicolons rule; a semicolon
     joining two independent clauses over the cap is split.
   - Otherwise the more specific rule wins. Where neither is more
     specific, keep the reader's ability to act and note the
     collision in the pull request.

Apply the higher-ranked rule, then satisfy the lower one the best way
that still obeys it.

## The five jobs

Decide which job applies before writing; ask the requester when the
request does not say. Restyle, restructure and overhaul are
cumulative levels; fix and new page sit outside that ladder.

| Job | Scope |
|---|---|
| Fix | Changes the facts it was asked to change and touches nothing else: no restructuring, style edits or vocabulary sweep, apart from the one reader-safety hazard move a restyle may also make. Takes the source for each changed claim and carries it as a fact-list entry in the hand-back, one per claim. Adds no fact beyond those requested. |
| Restyle | Rewrites wording only. Facts and section order stay fixed, except the one hazard move, named in the hand-back. Takes the page's own facts as stated, builds no fact list, and adds no new fact. |
| Restructure | A restyle that also reorders, merges, splits or adds sections. Facts are taken as the page states them: nothing re-verified or added, and no fact list is built. |
| Overhaul | A restructure that also re-establishes every fact from source through the ledger. May add a fact or a step the content checklist requires, sourced and explained in the pull request. |
| New page | Has no page or ledger to inherit. Facts come from source and shape comes from them. May add any fact the checklist requires, sourced and explained in the pull request. |

A request that names one or more factual corrections is a fix and
needs no clarifying question. When handed an existing page with no clear
instruction otherwise, ask before doing anything, offering exactly
three named levels: restyle, restructure, overhaul, each stated as
what it adds over the one below.

## Load list per job

Every job loads `style-standard.md`, `writing.md` and
`product-vocabulary.md`.

| Job | Also loads |
|---|---|
| Fix | (nothing more: "Doing a fix" below is the whole job) |
| Restyle | `gates.md`, `reviews.md` |
| Restructure | `gates.md`, `reviews.md`, `shape.md` |
| Overhaul | `gates.md`, `reviews.md`, `shape.md`, `facts.md`, `ledger.md` |
| New page | `gates.md`, `reviews.md`, `shape.md`, `facts.md` |

Two files are surface add-ons, loaded only when the page itself is
that surface: `in-app-copy.md` for in-app copy, `agent-pages.md` for a
page an agent reads.

## Doing a fix

- Take each changed claim from source: the generated command
  reference, the product's own code, a vendored spec or a probe log.
  Where two disagree, a measurement beats a spec. A sibling docs page
  settles nothing.
- A claim with no source stays out; write what is true in its place.
- Touch no sentence for style alone. A finding in a sentence you did
  not change is not yours.
- Run the gate against the old page, which reports only what the
  change introduced, and fix every finding it reports:

      old=$(mktemp); git show main:<page.md> > "$old"
      <skill>/check-mechanics.py --baseline "$old" <page.md>

  `<skill>` is this skill's own directory.

- Someone other than the writer checks each changed claim against its
  source. Only a wrong fact compels a change.

## What ships with the draft

Hand back, on every job: the skill files read, by name; which of the
five jobs was done; and the gate numbers plus review findings and what
changed in response.

| Job | Also hand back |
|---|---|
| Fix | One row per changed claim: the claim, its source file:line, its heading. |
| Overhaul, new page | The fact list; the allow file, from the point a shared sequence first needed one. |
| Restructure, overhaul | The short heading tree. |
| New page | The full heading tree. |
