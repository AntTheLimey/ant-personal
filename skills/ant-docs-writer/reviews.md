# Reviews

The review each job runs, the cold-read and meaning-check dispatches,
and who a finding binds. Every job loads at least one section here.

## Reviews

Review composition follows the job, set out in the table under "Ask
which job this is before you start" in SKILL.md. A fix gets a
correctness review of the changed claim. A restyle and a restructure
get a meaning check and a cold read, run in parallel. An overhaul and
a new page get a correctness review and a cold read, run in parallel,
plus a screenshot check on any page that states what a screen shows,
where an image of it is available. One fix round runs on every job. A
second round runs only where the first found a wrong fact or a defect
in the work itself. Each review is performed by someone other than the
writer, after the draft exists. A writer cannot be their own cold
reader, because you cannot un-know the page you just wrote.

**Run the cold read yourself before calling the page done, on every
job that gets one.** Do not hand it back as a recommendation and do
not wait to be asked. Dispatch a fresh agent that has none of your
context and give it the page, the pages it links to, and
`style-standard.md`, handed over unchanged: never retyped, trimmed or
excerpted. Give it nothing else.

The correctness reviewer checks every claim on the page against its
source, on an overhaul and a new page. On a fix, it checks the one
changed claim only, and there is no cold read.

**The fact list** is what makes that possible. Add an entry the moment
a claim goes on the page, so the reviewer verifies against a record
built alongside the draft rather than rediscovering each source. "Fact
list entry form" under "Two artifacts, and the old page is not one of
them" in facts.md gives its fields. On a fix, an overhaul and a new
page, a claim you cannot put a source beside does not go on the page.

The cold-read reviewer gets no repository context at all, only the
page, the pages it links to, and `style-standard.md`, handed over
unchanged. They read as the customer and report where they got lost,
what they could not type, where the page breaks the standard, and what
they would search the web for instead.

### The meaning check

On a restyle and a restructure, a separate agent, not the writer,
verifies that the rewrite kept the page's facts, since neither job
re-verifies against source. Give it the old page and the new page and
nothing else. It reports:

- every fact added, dropped or changed
- every condition, number, scope or hazard that was weakened, widened
  or lost
- whether any section moved from where it stood in the old page

On a restyle, every moved section is reported. A move the hand-back
names under the ordering exception in "Ask which job this is before
you start" in SKILL.md is not a defect. Any other move is, because a
restyle keeps the section order fixed otherwise. On a restructure a
moved section is expected, and the report exists to confirm the move
carried the facts the section held, not to flag the move. The meaning
check does not comment on style. Its findings are wrong facts, so "A
reviewer owns facts, the writer owns the page" applies to them the
same way it applies to the correctness reviewer's findings.

Dispatch it with:

> You check meaning, not style. You have the old page and the new
> page and nothing else. Compare them and report: every fact added,
> dropped or changed. Every condition, number, scope or hazard that
> was weakened, widened or lost. Whether any section moved from where
> it stood in the old page. Say nothing about wording, sentence length
> or tone. Where you are not sure whether a change is a difference in
> meaning or only in phrasing, report it and say which you think it
> is.

### A reviewer owns facts, the writer owns the page

**A wrong fact is the only thing a review can compel.** Where a claim
does not match its source, it is corrected, no argument. Even then the
reviewer does not get to write the correction: the writer decides how
the right fact reaches the reader, and may find the whole sentence was
not worth keeping.

**Everything else a review says is a suggestion.** What goes in, what
stays out, what order it runs in, how it is worded, whether a caveat
earns its line. The writer takes what improves the page and refuses the
rest, naming the reason in the report.

Refusing is normal and often right. A review reads a page closely, one
finding at a time, which is the reading that makes every omission look
like a gap. Taking all of them is how a page fills back up with the
fluff the last pass removed. "The reader cannot act differently on
this" and "this belongs to the page I link to" are complete reasons.

A second review round happens only when the first found a wrong fact or
a defect in the work itself. A round spent on suggestions is a round
spent making the page longer.

Where a job runs a pair of reviews, each finds defects the other would
not, and neither substitutes for it. Run both, even on a small change,
and run the screenshot check too wherever it applies. A fix runs one
review only, and that review stands alone.

**Where a job gets a cold read, it is the only gate that catches an
ordering defect, and that is why it is never skipped there.** Every
rule in this skill is applied by someone who already knows what the
page is for, so a step whose reason sits sixty lines below it, or a
precondition parked after the failure it predicts, passes the
checklist and passes the prose rules. Only a reader with no context
skips the step and tells you they skipped it.

Ask the cold reader for what they had to guess, what they would have
done wrong, and where the page breaks the attached standard. A page
can read well and still be executed in the wrong order.

### The cold-read dispatch

The cold reader is not a fact checker. The cold reader checks
phrasing, style, legibility and comprehension. Completing the task
only shows whether the page achieves that.

Give the agent the page's path, the pages it links to, and
`style-standard.md`, handed over unchanged: never retyped, trimmed or
excerpted. Give it nothing else: no repository access, no web search,
no other skill files, no explanation of the product. The file carries
its own quoted-product-string exemption, so a contraction or a banned
word inside a quoted UI label is not reported. Tell it:

> You are a cold reader. You have never seen this product. Read only
> this file, the pages it links to, and the attached style standard.
> Whatever the page does not tell you, you do not know. A
> cross-reference inside the standard points at text you do not have.
> Ignore it. Report: could you complete the task, and if not, the
> first sentence at which you were stuck. Every place you had to
> guess, quoting the sentence and naming the readings. Every question
> the page raises and does not answer. Anything you would have done
> wrong, and what the consequence would have been. Where the page
> breaks the attached standard, quoting the sentence and the rule.
> Read alt text and headings as page vocabulary too. What the page
> does well. Judge only what is on the page. If you find yourself
> reasoning "it presumably works like X", record that as a guess
> instead.

The fourth answer is the one that matters. "I would have skipped that
step because it reads as ceremony" is a defect report, and no other
review produces it.

**On an overhaul and a new page, a page that states what a screen
shows gets a separate check against the image, run alongside the cold
read, where an image of that screen is available.** Both conditions
gate it: a field, a label, a button, a message or a sequence on screen
stated in the draft, and an image to check it against. A page that
carries a screenshot but describes nothing on it skips this check, and
so does a page that describes a screen but has no image of it. Either
way, its on-screen facts rest on the fact list instead. The
writer dispatches it, and a separate agent, someone other than the
writer, performs it with image access and the page. That agent
compares each on-screen claim in the draft against the screenshot and
reports every mismatch. Settle a mismatch against the product, under
the rule in "Never invent" in facts.md. Where the product agrees with
the image, the prose is wrong and is corrected. Where the product
agrees with the prose, the image is stale and is flagged for
recapture. Its findings go into the same fix round as the cold read's.

**Fix what it found, then say what it found.** A cold read reported and
not acted on is worse than none, because the page now ships with the
defect and a record that you knew.

