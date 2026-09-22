# Reviews

Loaded by every job.

## Which reviews run

| Job | Reviews |
|---|---|
| fix | Correctness review, changed claims only |
| restyle | Meaning check (self) → cold read |
| restructure | Meaning check (self) → cold read |
| overhaul | Correctness review + cold read (parallel) + screenshot check* |
| new page | Correctness review + cold read (parallel) + screenshot check* |

*Screenshot check gates on both: an on-screen claim in the draft, and
an available image of that screen.

Run every review a job gets, even on a small change — each catches
what the other doesn't. Meaning check is the one review you perform
yourself; every other review is done by someone other than the
writer, since a writer can't be their own cold reader.

## Correctness review

Overhaul, new page: the reviewer checks every claim against its
source. Add a fact-list entry the moment a claim is drafted, so the
reviewer works from a record built alongside the page, not a re-read.
Fix, overhaul, new page: a claim with no source beside it doesn't go
on the page.

## Meaning check

Restyle, restructure: read the old-vs-new diff yourself, before
dispatching the cold read, before calling the page done. No agent —
you already hold both versions in context from writing the reword.

Check for:

| Subject | Change |
|---|---|
| Fact | added, dropped, or changed |
| Condition, number, scope, hazard | weakened, widened, or lost |
| Section | moved from where it stood in the old page |

Restyle: a moved section is a defect, except the one allowed move (a
stated hazard into Before You Start) — name it in the hand-back.
Restructure: a moved section is expected; check only that it carried
its facts.

Fix what you find immediately — nothing else has read the page yet,
so there's nothing to reconcile against.

The failure mode that matters: a same-length wrong value swapped for
a right one (a flag name, a field name), not a size mismatch a script
could flag. That's what a careful diff read catches and a size-based
check would miss.

## Cold read

The only check applied by someone with no idea what the page is
for — the only one that catches an ordering defect. Never skip it,
never defer it, on every job that gets one.

Restyle, restructure: dispatch only once your own meaning check is
fixed, so it always reads settled text.

**Batch it.** A doc-set run (several pages restyled, restructured or
overhauled together) gets one cold-read dispatch per batch of up to 6
pages, not one per page: load style-standard.md once, hand over the
batch in the order a customer would navigate it, and read it once, in
order, as that reader. A run longer than 6 pages is further batches
of up to 6, each a fresh "never seen this product" read carrying
nothing from the batch before it. Report findings tagged by page
path.

Pin the dispatch to Sonnet. Use a higher model only where the user
asks for one by name; never downgrade to save cost. Most of what
check-mechanics.py already catches mechanically (spelling, banned
words, verb-table matches) never reaches cold read — what's left is
the would-do-wrong finding, which takes real reasoning about what an
unfamiliar reader would misunderstand, and is harder, not easier,
once a dispatch covers several pages at once.

Give the reviewer the batch's pages and style-standard.md, unchanged,
and nothing else — no repository context. The page's own links are
someone else's job: whether a linked page answers what it points to
is that page's review, not this one's. Where a sentence sends the
reader to a link to act on something, report it as an unanswered
question and don't follow it.

Where a prior batch's cold read surfaced a cross-page pattern already
filed as its own tracked issue, carry it forward into every later
batch's dispatch as a known finding, named in one line. This doesn't
exempt any page from its own read; it stops the same filed defect
being independently rediscovered, and re-verified, batch after batch.

Dispatch prompt:

> You have never seen this product. Read only these pages, in this
> order, and the attached style standard: `<path list>`. Do not
> follow a link off any of them; where a link is the only way to act
> on something a page tells you, report it as an unanswered question
> instead. [If known findings exist:] These are already filed as
> cross-page issues and don't need rediscovering: `<known findings,
> one per line, by their filed reference>` — report an instance only
> if this page's own fix should happen now. Record any belief you
> infer rather than read as a guess. Per page, report where you got
> lost, what you could not type, and what you would search the web
> for instead.

Report format: one line on completion, then one line per finding —
`path | quoted text | kind | detail`. No cap, no summary, no praise.

- guess
- unanswered question
- would do wrong — matters most, since no other review produces it

Style-standard.md compliance is not a cold-read finding kind: named
words, register swaps and the verb table are check-mechanics.py's
job, gated before cold read is ever dispatched. The residual judgment
calls (vocabulary consistency, register rhythm) have produced a false
positive against zero confirmed unique catches. Style-standard.md
still goes to the reviewer — it sets the reader persona (competence,
pressure, screen-fidelity expectations) that shapes what counts as a
guess or a would-do-wrong.

## Screenshot check

Gated on an on-screen claim plus an available image of that screen.
Dispatch a separate reviewer with image access to compare each claim
against the screenshot and report every mismatch. Settle against the
product, not either source alone: correct the prose where the product
agrees with the image; flag the image for recapture where it agrees
with the prose.

## Applying findings

A wrong fact is the only finding a review can compel — and even then
the reviewer doesn't write the correction, the writer decides how the
right fact reaches the reader. Everything else is a suggestion: take
what improves the page, refuse the rest, name the reason. "The reader
can't act differently on this" and "this belongs to the page I link
to" are complete reasons to refuse.

Refusing is normal and often right. A review reads closely, one
finding at a time — the reading that makes every omission look like a
gap. Taking all of them is how a page fills back up with the fluff
the last pass removed.

Overhaul, new page: apply each review's findings as it returns; where
both name the same sentence, apply the fact-bearing one
(correctness review) first. Restyle, restructure: your meaning check
is already fixed before the cold read is dispatched, so cold read is
the only review left to apply. Run the gates once, after the job's
reviews are applied.

A second review round happens only when a review found a wrong fact
or a defect in the work itself. Cold-read findings (guess, unanswered
question, would do wrong) are never wrong-fact findings, so never
compel one alone.

Fix what a cold read found, then report what it found. A reported and
unactioned finding is worse than none.
