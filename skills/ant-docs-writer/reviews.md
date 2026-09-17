# Reviews

Loaded by every job.

## Which reviews run

| Job | Reviews |
|---|---|
| fix | Correctness review of the changed claims only. No cold read. |
| restyle | Meaning check and cold read, in parallel. |
| restructure | Meaning check and cold read, in parallel. |
| overhaul | Correctness review and cold read, in parallel. Screenshot check where a page states what a screen shows and an image is available. |
| new page | Correctness review and cold read, in parallel. Screenshot check where a page states what a screen shows and an image is available. |

Each review is performed by someone other than the writer, after the
draft exists, since a writer cannot be their own cold reader. Run both
reviews of a pair even on a small change, since each finds defects the
other would not; a fix runs one review only, covering every claim it
changed. Run the screenshot check
wherever it applies.

## Correctness review

The reviewer checks every claim on the page against its source, on an
overhaul and a new page. Add a fact-list entry the moment a claim goes
on the page, so the reviewer verifies against a record built alongside
the draft. On a fix, an overhaul and a new page, a claim with no
source beside it does not go on the page.

## Meaning check

On a restyle and a restructure, a separate agent runs a meaning check
comparing only the old page and the new page, and nothing else. It
reports:

- Every fact added, dropped or changed.
- Every condition, number, scope or hazard that was weakened, widened
  or lost.
- Whether any section moved from where it stood in the old page.

On a restyle, every moved section is a defect unless the hand-back
names it under the one allowed ordering exception (moving a stated
hazard into Before You Start). On a restructure, a moved section is
expected; the check confirms only that the move carried its facts.

The meaning check never comments on style. Its findings are wrong-fact
findings, owned the same way a correctness reviewer's are.

## Cold read

Run it yourself before calling the page done, on every job that gets
one. Do not defer it as a recommendation and do not wait to be asked;
never skip it on a job that gets one. Where a job gets a cold read, it
is the only check that catches an ordering defect, since every other
check is applied by someone who knows the page's purpose.

Give the cold-read agent the page, the pages it links to, and
style-standard.md, handed over unchanged, and nothing else. The
reviewer gets no repository context at all and reads as the customer.

Dispatch prompt:

> You have never seen this product. Read only the page at
> `<path>`, the pages it links to, and the attached style standard.
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

Apply a review's findings as soon as it returns, then the second
review's findings when they arrive, all within one fix round. Where
both reviews name the same sentence, apply the fact-bearing finding
(meaning check or correctness review) first. Run the gates once, after
both reviews' findings are applied. A second review round happens only
when the first found a wrong fact or a defect in the work itself.

Fix what a cold read found, then report what it found. A reported and
unactioned finding is worse than none.
