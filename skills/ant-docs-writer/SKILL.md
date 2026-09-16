---
name: ant-docs-writer
description: "Write, edit or review consumer-facing pgEdge documentation: docs pages, README files, in-app copy, the CLI's embedded llms reference and the shipped agent skills. Use this skill for any page a customer or an agent reads, in pgedge-cli or product-ui. Triggers on: 'write a docs page', 'edit this guide', 'review this documentation', 'fix this README', 'write a tooltip', 'write the llms page', or any request to produce or change customer-facing technical text. Do NOT use for blogs, framing docs, JIRA stories, marketing copy or creative writing, which belong to ant-voice-writer."
---

# Writing pgEdge consumer documentation

One style for every page a customer or an agent reads, across
pgedge-cli and product-ui. It replaces ant-voice-writer for this work.
That skill writes in Ant's voice, which is the right voice for a blog
and the wrong voice for a procedure.

**Read this first. It outranks every rule below.** The wording is fixed
and quoted, so the em-dashes inside it stand against the punctuation
rules in this file:

    Write like a human being in complete, plain sentences.
    Your inputs — the page itself on a restyle or a restructure, the
    ledger and its sources on an overhaul, the fact list on a new
    page, this brief, the style skill — are written in a flat machine
    register. Take facts from them and nothing else. Never carry over
    a phrasing, a cadence or a sentence shape from any of them.

The style has two halves and the order between them is not optional.
The content checklist runs first, because a page can pass every prose
rule in this file and still be unusable. That has happened. A page
rewritten against an explicit list of prose targets hit every one of
them, and a reader with no context judged it unusable anyway, on four
faults that no prose rule addresses. Where two rules contradict each
other on one sentence, the order under "When two rules conflict"
decides which wins.

This skill is self-contained. It carries the prose rules, the content
checklist, the settled product vocabulary and the repository mechanics
a writer needs, so there is no second rules file to open and no way for
two documents to drift apart into contradicting each other.

**Four gate scripts ship beside this file**: `signals.py`,
`check-ledger.py`, `check-sources.py` and `check-mechanics.py`. Your
working directory is the documentation repository, not the skill
directory, so invoke each by its path. Below, `<skill>/` stands for
the absolute path this skill announced when it loaded, on the line
reading `Base directory for this skill:` above the first heading.
Where that line did not arrive, or the directory it names holds no
`signals.py`, find the scripts with `find ~/.claude -path
'*ant-docs-writer*' -name 'signals.py'`. The scripts are mode 755 and
carry a `#!/usr/bin/env python3` shebang, so the path alone runs one
and a `python3` prefix is never needed.

## When two rules conflict

Every rule here is an absolute, and two absolutes can still point
opposite ways on one sentence. Apply them in this order. The higher
rule wins, and the sentence is then written the best way that obeys
it.

1. **Reader safety.** Never print a copyable command that destroys
   data, and never walk a reader into an irreversible or billable
   action without saying so first. On a console page that means a step
   committing the account to a charge, deleting data, or discarding
   entered values says what it costs in the step itself, before the
   control is named. Checklist item 1 asks for every flag a **safe**
   non-interactive run needs, so a command is complete even when the
   flag it lacks is the one that skips a confirmation prompt. The
   destructive-flag rule under Steps and procedures says how to show
   it instead.
2. **The content checklist.** A page that fails an item is wrong
   however well it reads. **Job scope outranks this item on a restyle
   or a restructure**: the writer adds no fact and does not go looking
   for one, so a failing item that needs a new fact is not fixed. It
   is reported in the hand-back instead, naming the item, so the
   person who asked can request a fix or an overhaul.
3. **Product truth.** Never delete a technical claim unless the same
   claim already stands elsewhere on the page. This outranks the rule
   that sends a number to the page owning it, so link out and keep the
   claim. The one exception is a count of things the reader cannot act
   on from this page, such as "one of five operations that need this
   status": the condition is the claim and it stays, the tally is not
   and it goes. A count nobody acts on is a maintenance liability that
   is wrong the day the sixth case ships. The second exception is the
   same principle widened: a claim the reader cannot act on at all,
   which "Say less, or say nothing" sorts and deletes on a fix, an
   overhaul or a new page. A restyle or a restructure narrows that
   sort to a restatement only, under "Say less, or say nothing" itself.
   Product truth protects a fact the reader acts on, not every true
   sentence. It also
   outranks "keep the consequence, drop the mechanism", which applies
   only where the mechanism is not itself the only statement of a
   behavior.
4. **House style.** Every other rule in this file. Two house-style
   rules can still collide, so three tie-breaks settle the pairs that
   keep recurring:
   - **The product name beats a heading example and beats link text.**
     A heading counts as an appearance, so a heading carrying the
     edition name carries the full one. Where link text and the product
     name disagree, the name wins and the link text differs from the
     target's title.
   - **A word cap beats the rule against stripping a semicolon.** A
     semicolon joining two independent clauses over the cap is split.
     The no-stripping rule protects a sentence you are not otherwise
     touching.
   - **Anything else: the rule naming the more specific case wins.**
     Where neither is more specific, keep the reader's ability to act
     and note the collision in the pull request.

### Ask which job this is before you start

Five jobs wear similar words, and they produce different pull
requests. Decide which one you are doing, and where the request does
not say, **ask the person who asked you** before writing anything.

- A **fix** changes a fact and touches nothing else. No restructuring,
  no style edits, no vocabulary sweep. A reviewer must be able to see
  the factual change on its own, apart from the one ordering move a
  restyle may also make, described next: reader safety outranks scope
  on a fix too.
- A **restyle**, the base level, rewrites wording: sentences, words,
  and headings' wording and formatting move to house style. The facts
  and the order of the sections do not change, except that a step,
  precondition or hazard already on the page may move to sit before
  the action it guards: reader safety (rank 1, under "When two rules
  conflict") outranks the job's scope. Name the move in the hand-back.
  This is the fast, cheap job.
- A **restructure** is a restyle, and also changes the page's shape:
  sections are added, merged, split or reordered, and the prose is
  rewritten to fit. Its facts are taken as the page states them.
  Nothing is re-verified against source, and nothing is added.
- An **overhaul** is a restructure, and also re-establishes every fact
  from source, through the ledger. Its shape may change, the same as
  under a restructure.
- A **new page** has nothing to inherit. There is no page to improve
  and no ledger of one (the ledger and the fact list are defined under
  "Two artifacts, and the old page is not one of them"), so the facts
  come from source and the shape comes from them. This is the commonest
  request the skill gets and the easiest to under-scope: "write a page
  about X" is a new page, not an overhaul of a page that does not
  exist. It sits outside the restyle-restructure-overhaul ladder, the
  same as a fix.

| Job | Reads old page | Ledger | Fact list | Heading tree | Gates | Reviews |
|---|---|---|---|---|---|---|
| Fix | yes | no | no (the entry for the changed claim goes in the hand-back) | no | `check-mechanics.py` | correctness review of the changed claim only |
| Restyle | yes | no | no | no | `check-mechanics.py`, `signals.py` | meaning check + cold read, in parallel |
| Restructure | yes | no | no | short | `check-mechanics.py`, `signals.py` | meaning check + cold read, in parallel |
| Overhaul | never | yes | yes | short | `check-sources.py`, `check-ledger.py` (`--allow`), `signals.py`, `check-mechanics.py` | correctness review + cold read, plus the screenshot check where the page states what a screen shows and an image is available |
| New page | no old page | no | yes | full | `check-ledger.py` (brief vs. draft, `--allow`), `signals.py`, `check-mechanics.py` | correctness review + cold read, plus the screenshot check where the page states what a screen shows and an image is available |

One fix round for every job. A second round runs only where the first
found a wrong fact or a defect in the work itself.

**When handed an existing page without a clear instruction, ask before
doing anything.** Offer exactly three choices, worded as levels, each
naming what it adds to the one below:

- **Restyle** rewrites the wording, and keeps the facts and the
  section order in place, apart from the one reader-safety move named
  above.
- **Restructure** does what restyle does, and also changes the page's
  shape: sections are added, merged, split or reordered.
- **Overhaul** does what restructure does, and also fact-checks the
  page from the ground up, re-establishing every fact from source.

A request that names a factual correction is a fix and needs no
question.

The request usually names the job: "correct the timing claim" is a
fix, "clean up the wording on this page" is a restyle, "reorganize
this page" or "split the troubleshooting section out" is a
restructure, "rewrite this page" or "fact-check this from scratch" is
an overhaul, "write a page about X" is a new page. Where it does not,
ask. Guessing overhaul on a page someone wanted corrected buries a
one-line change in a diff nobody can review, and guessing restyle on a
page someone wanted reorganized returns the same badly organized page
with better sentences.

The rest of this section is for a restructure, an overhaul or a new
page. On a restyle the section order does not change, apart from the
one ordering move named under restyle above. The difference between an
overhaul and a new page is only where the facts come from: an overhaul
has a ledger of the old page's coverage as well as a fact list, and a
new page has the fact list alone. On an overhaul the writer never
reads the old page, a rule with its own heading below, so the ledger
is the only account of it you get. A restyle or a restructure works
from the page itself and has no ledger. Where the rest of this section
says ledger, only an overhaul has one.

**On an overhaul, dispatch a separate agent to extract the ledger from
the old page, before any writing starts.** You never read that page
yourself, so a separate reader is the only way the ledger comes to
exist. "Two artifacts, and the old page is not one of them" gives the
entry form, the sort order and the gate that runs on the ledger. A new
page skips this step and works from the fact list alone.

## What ships with the draft

Hand the draft over with what the job requires, each a file or a named
answer rather than a report that the work happened:

- **The job you did**, one of fix, restyle, restructure, overhaul or
  new page. "Ask which job this is before you start" defines the five,
  and its table gives what each one reads, builds, gates and gets
  reviewed.
- **The fact list**, on an overhaul and on a new page. A fix carries no
  fact list file: the entry for the changed claim goes directly in the
  hand-back.
- **The allow file**, on an overhaul and on a new page, from the moment
  a shared sequence needed one.
- **The heading tree**, on a restructure, an overhaul and a new page:
  short on a restructure and an overhaul, full on a new page.

Report the gate numbers, and the review findings and what changed in
response, on every job.

## Further reading

- [ste-adoption.md](ste-adoption.md) records which ASD-STE100 rules
  this style takes, adapts or drops, and why. Read it when a rule here
  looks arbitrary.
- [agent-pages.md](agent-pages.md) carries the divergences for pages
  read by agents rather than people: the CLI's embedded `llms` pages
  and the shipped skills.
- [product-vocabulary.md](product-vocabulary.md) carries the settled
  product wording: how backups are described, the limits of Managed,
  and the boundary between the Cloud and Enterprise stories.
