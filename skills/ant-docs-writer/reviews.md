# Reviews

Loaded by every job.

## Which reviews run

| Job | Reviews |
|---|---|
| fix | Correctness review of the changed claims only. No cold read. |
| restyle | Meaning check (you, against the diff), then cold read. |
| restructure | Meaning check (you, against the diff), then cold read. |
| overhaul | Correctness review and cold read, in parallel. Screenshot check where a page states what a screen shows and an image is available. |
| new page | Correctness review and cold read, in parallel. Screenshot check where a page states what a screen shows and an image is available. |

Every review but one is performed by someone other than the writer,
after the draft exists, since a writer cannot be their own cold
reader. The one exception is the meaning check: you run it yourself,
against your own diff, before anything else touches the page. Run
every review a job gets, even on a small change, since each finds
defects the other would not; a fix runs one review only, covering
every claim it changed. On restyle and restructure, do the meaning
check and fix what it found before dispatching the cold read, so the
cold reader always reads settled text. On overhaul and new page,
correctness review and cold read still run in parallel. Run the
screenshot check wherever it applies.

## Correctness review

The reviewer checks every claim on the page against its source, on an
overhaul and a new page. Add a fact-list entry the moment a claim goes
on the page, so the reviewer verifies against a record built alongside
the draft. On a fix, an overhaul and a new page, a claim with no
source beside it does not go on the page.

## Meaning check

On a restyle and a restructure, read the word-diff between the old
page and the new page yourself — no separate agent, before the cold
read is dispatched, before you call the page done. Check for:

- Every fact added, dropped or changed.
- Every condition, number, scope or hazard that was weakened, widened
  or lost.
- Whether any section moved from where it stood in the old page.

On a restyle, every moved section is a defect unless the hand-back
names it under the one allowed ordering exception (moving a stated
hazard into Before You Start). On a restructure, a moved section is
expected; check only that the move carried its facts.

Fix what you find immediately. There is no report to hand off and
nothing to reconcile against another review, since nothing else has
read the page yet.

This replaces the separate-agent version 1.4.8 shipped. Measured on
2026-09-21 across a five-restyle sample, that agent found two real
defects (a flattened field name, a register slip carrying a fact) at
roughly a third of the cold read's cost — enough, at the time, to keep
paying for it. A later 16-page batch changed the answer: the same
agent, dispatched once and measured, cost 74,356 tokens and found
nothing, while reading the diff yourself, done on the batch's other
pages, is what caught that batch's one real regression (a wrong flag
name). Both real defects found across both samples were a same-length
wrong value swapped for a right one — not a size mismatch a cheap
script could reliably flag, but exactly the kind of thing a careful
read of the diff catches. Doing it yourself costs nothing beyond the
diff you already produced; paying an agent to independently re-derive
the same read has not, on this evidence, found anything the self-read
would have missed.

## Cold read

Run it yourself before calling the page done, on every job that gets
one. Do not defer it as a recommendation and do not wait to be asked;
never skip it on a job that gets one. Where a job gets a cold read, it
is the only check that catches an ordering defect, since every other
check is applied by someone who knows the page's purpose. On a restyle
and a restructure, dispatch it only once your own meaning check is
done and fixed, so it always reads settled text.

Give the cold-read agent the page and style-standard.md, handed over
unchanged, and nothing else. The reviewer gets no repository context
at all and reads as the customer. The page's links are not the cold
reader's job: whether a linked page answers the question it points to
is that page's own review, not this one's. Where a sentence sends the
reader to a link for something they need to act, the reviewer reports
it as an unanswered question and does not follow it.

Where a job is working a doc set (several pages in one restyle,
restructure or overhaul run) and a prior page's cold read has already
surfaced a cross-page pattern that is filed as its own tracked issue,
carry that issue forward to every later dispatch in the run as a known
finding: name it in one line the reviewer can match against what it
would otherwise find. This does not exempt any page from its own cold
read; it stops the same already-filed defect from being independently
rediscovered, and the orchestrator from re-verifying it, on every page
that repeats it.

Dispatch prompt:

> You have never seen this product. Read only the page at
> `<path>` and the attached style standard. Do not follow any links
> on the page; where a link is the only way to act on something the
> page tells you, report it as an unanswered question instead.
> [If the run has known findings:] The following are already filed as
> cross-page issues and do not need rediscovering: `<known findings,
> one per line, by their filed reference>`. Report an instance of one
> only if this page's own fix should happen now; otherwise skip it.
> Record any belief you infer rather than read as a guess. Report
> where you got lost, what you could not type, where the page breaks
> the attached standard, and what you would search the web for
> instead.

Report format: one line on task completion, then one line per
finding giving the quoted text, the kind, and the matching detail,
with the fields separated by "|". No cap, no summary, no praise.
Finding kinds:

- guess
- unanswered question
- would do wrong
- breaks the standard

A would-do-wrong finding is the one that matters most, since no other
review produces it.

## Screenshot check

Gated on two conditions together: an on-screen claim in the draft, and
an available image of that screen. The writer dispatches a separate
reviewer with image access to compare each on-screen claim against the
screenshot and report every mismatch. Settle a mismatch against the
product: correct the prose where the product agrees with the image,
and flag the image for recapture where it agrees with the prose.

## Applying findings

A wrong fact is the only finding a review can compel. Even then the
reviewer does not write the correction; the writer decides how the
right fact reaches the reader. Everything else a review says is a
suggestion: take what improves the page and refuse the rest, naming
the reason in the report. "The reader cannot act differently on this"
and "this belongs to the page I link to" are complete reasons to
refuse a finding.

Refusing is normal and often right. A review reads a page closely,
one finding at a time, which is the reading that makes every omission
look like a gap. Taking all of them is how a page fills back up with
the fluff the last pass removed.

On an overhaul and a new page, apply each review's findings as soon
as it returns; where both name the same sentence, apply the
fact-bearing finding (correctness review) first. On a restyle and a
restructure, your own meaning check is already fixed before the cold
read is even dispatched, so there is nothing from it left to apply;
the cold read is the only review the job produces, and you apply its
findings when it returns. Run the gates once, after the job's review
has returned and its findings are applied. A second review round
happens only when a review found a wrong fact or a defect in the work
itself; the cold read's findings (guess, unanswered question, would do
wrong, breaks the standard) are never wrong-fact findings and so never
compel one on their own.

Fix what a cold read found, then report what it found. A reported and
unactioned finding is worse than none.
