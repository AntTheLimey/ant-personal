# Facts

Sourcing, fact-checking and the ledger, loaded in full on an overhaul
and a new page; a fix loads only "Never invent".

## Ask what your sources are, before you gather anything

Your reader is a constant: a competent developer who does not know
this product. They need no account of SQL, HTTP, cron or their own
framework, and they need every term that belongs to us.

What varies from page to page is **where the truth lives**, and that
decides both what you can write and what shape the page takes. Ask
before you gather, because a source you were never given is a fact you
will never have, and nothing downstream recovers it.

Four things to settle, and they are the only questions worth spending
the requester's attention on:

- **Which codebases may I read?** Ours is rarely all of them. A page
  about using this product from someone else's framework is mostly
  facts about that framework, and reading our source produces none of
  them.
- **What should I compare this against?** Name it if a structure was
  borrowed from somewhere. A shape we took and never wrote down is one
  a fresh writer can neither reproduce nor question.
- **May I create, run and tear down real resources to verify
  behavior?** Where the answer is no, say so on the artifact, so that
  an unmeasured claim is visible rather than silently absorbed.
- **Where are the measurements?** A measurement recorded outside the
  probe-log directory is a measurement lost. If probe logs exist, get
  their path. If a measurement was taken and never written down, say
  so rather than treating it as known.

Everything else, look up. **A skill that asks what it could have
discovered spends the one thing the requester has least of.**

### Where to look

- **The generated command reference.** Produced from the command tree,
  so it cannot drift from the binary. Truth for verbs, flags,
  defaults and help text. In pgedge-cli that is `docs/reference/`.
- **`pgedge llms`** for the agent reference: the index first, then the
  module.
- **The product's own code.** Read it for the order of operations,
  what is validated locally, and which exit status each failure takes.
- **The vendored specs**, remembering they are what the platform says
  about itself.
- **The probe logs**, which are what someone watched it do.

When two disagree, the stronger one is the source of truth: a
measurement beats a spec, a generated reference cannot be wrong
about a flag, and a sibling page settles nothing.

**Build the fact list from these sources before you write, on an
overhaul and on a new page.** Record each fact with the file and line
that settles it, in a file beside the draft. The fact list is what you
write from, so a fact you did not gather is one the page cannot carry.
A new page has nothing else, and an overhaul has only the ledger
beside the fact list. A fix takes the source for the one changed claim
and carries it as a single fact-list entry in the hand-back. A restyle
or a restructure takes the page's own facts as the page states them
and builds no fact list. "Two artifacts, and the old page is not one
of them" defines the fact list and the ledger.

## Never invent

A restyle or a restructure sources nothing here: both take the page's
own claims as given and verify nothing against source. Where a rule
below asks for a source or for new material, it binds a fix, an
overhaul and a new page. "Say less, or say nothing" in writing.md
governs what a restyle or a restructure may still cut.

- On a fix, an overhaul and a new page: every command and flag exists
  in the generated reference, and every behavioral claim traces to a
  live capture, a spec field, the product's own source, or an existing
  gated page. A claim with no source stays out, and what is true goes
  in its place. Record the source as you write the claim, in the fact
  list under "Reviews" in reviews.md.
- **Keep the consequence, drop the mechanism.** The reader is told what
  they can do and see, never how the platform does it. "Rotating the
  credential for the app role restarts AI services" is the right weight.
  Not the container, not the startup sequence, not which process read
  what.
- **No list of cases that will age.** "A restore, resize, service change
  or credential rotation" becomes "a modification". A list like that is
  wrong the day the fifth case ships.
- **No scope creep.** A field, a badge or a section explains itself and
  not a neighboring feature. Sizing rules belong in the resize flow,
  not on a storage panel.
- **A number stays in prose only when the reader acts on it.** "About
  ten seconds" earns its place. "Twenty-one of twenty-one attempts" does
  not. Link to the one page that owns a number rather than restating it
  where it will go stale.
- **Where those two pull apart, ask where the reader acts.** A number
  they act on while reading this page stays on this page. A number they
  act on somewhere else is a link. A price in a size table is the first
  kind, because the reader is choosing a size from that table, so the
  table keeps its prices. The same price quoted in a sentence about
  billing is the second kind, and links out.
- **Attribute a runtime number only to a surface you checked.** "The
  console shows these prices" is a claim like any other and needs a
  source. Where you cannot source where the number is displayed, print
  the number without the attribution sentence rather than writing one
  you cannot support. Never attribute a number to a screenshot.
- **A mismatch between the prose and a kept image is settled by the
  product, never by trusting either one.** Check the on-screen claim
  against the live screen or the source that renders it. Where the
  product agrees with the image, the prose is wrong: correct it. Where
  the product agrees with the prose, the image is stale: write what
  the source says, flag the image for recapture in the pull request,
  and say nothing on the page about the discrepancy. Never write prose
  backward to match a stale screenshot.
- **A screenshot is not a source.** It is evidence that something
  appeared on screen once, and it goes stale silently. A value that
  exists only at runtime, such as a price the console fetches from a
  billing service, may still be stated: attribute it to what the console
  shows, never present it as a contract, and re-check it whenever the
  page is touched.
- **On an overhaul or a new page, a rewrite may add facts, and often
  must.** The content checklist in shape.md asks for things a page
  frequently does not have, and the answer is to go and find them
  rather than to leave the item failing. Source every addition and say
  where it came from in the pull request. What a rewrite may never do
  is add a fact it did not verify. A fix changes the one fact it was
  asked to change and adds no other. A restyle or a restructure adds
  none at all, under the job-scope rule in "When two rules conflict"
  in SKILL.md.
- **On an overhaul or a new page, a rewrite may add a step**, when the
  checklist requires one and the step follows from a fact that is
  sourced. A procedure that identifies something by when it happened
  needs a step telling the reader to record that, or the
  identification is unusable. Say in the pull request which fact the
  step follows from.
- **State an absence in the form "no X does Y", scoped to what you
  checked.** "No command in the reference reads whether the tier is
  enabled" is a claim you can support. "There is no way to check"
  is not, because you searched rather than proved. On a console page
  the scope is a screen rather than a reference: "the wizard offers no
  control for this" is supportable, "the console cannot do it" is not.
  Follow it with what the reader should do instead, and record the
  search in the pull request. A search that found nothing is evidence,
  not proof.
- Scope every claim to the command and the module actually checked. The
  same sentence written generally is often false for the sibling.
- A caveat is written for the reader, not as a lab note. "Recorded from
  observation" tells the reader the author guessed. "The API publishes
  no list of values for this field, so treat anything other than X as a
  fault" tells them what to do.
- The measurement is the reason a sentence is true. It is never the
  sentence. Dates, sample counts, fixture names and the words
  "measured", "polled" and "probe" live in the pull request, not on the
  page.

## Two artifacts, and the old page is not one of them

You build a **fact list** from source: the generated reference, the
product's own code, the vendored specs, the probe logs. It feeds
shaping and writing, on an overhaul and on a new page.

**The fact list is a file, written before any prose and completed as
the draft is written, then handed over with the draft.** It sits
beside the draft, and each entry takes the form under "Fact list entry
form" below. Reporting that you built one is not building one.

On an overhaul, a separate agent builds a **ledger** from the page you
are replacing. It is a record of what that page covered. It is never a
record of what is true.

Different provenance, different trust. Keep them apart, and never let
an entry cross from the ledger to the fact list without being settled
against source first.

### The writer never reads the old page

**This applies to an overhaul only.** A restyle and a restructure work
from the page itself, because they keep its facts as the page states
them.

Not once, not for reference, not to check a heading. Read the ledger
instead. A writer that has read the page reproduces its phrasing from
memory without meaning to, and its ordering along with it.

Name the excluded file as a path to filter out of every glob, not
only as a file not to open. `docs/managed/*.md` contains it and so
does any recursive grep. A prohibition on opening a file does not
survive a wildcard: two writers in one run were exposed exactly that
way.

### Ledger entry form

Three lines, fragments, nothing liftable as prose:

    F<n>. <note, under about 15 words>
          src: <file:line that verifies it>
          st: V|U|C|S

`V` verified against source. `U` unsourced, asserted by the page
alone. `C` contradicted by source. `S` stale.

**`V` means verified against something that is not a hand-written
page.** The generated reference is exempt, because it is produced from
the command tree and cannot drift from the binary. A sibling docs page
is the weakest authority there is: a false sentence in one reached a
ledger, a writer and a finished page, and the same claim was still
live two review rounds later.

**A spec description that a measurement contradicts is `C`, not `V`.**
A measurement outranks upstream documentation. A vendored spec is what
the platform says about itself, and it has been wrong.

**Write every entry as the situation, never as the missing thing.** An
entry framed as an absence reaches the page as an absence, and no gate
can see it: `F119. No delete verb exists` became "No command deletes a
backup" on a finished page, and the two share no words. Write what the
reader does instead.

### Sort it, and say so

Group by topic. Sort the headings alphabetically, and the entries
within each heading. Number from F1 in the sorted order. Ordering
leaks separately from phrasing, so a ledger in page order hands the
writer the page's structure back.

Tell the writer in as many words that the order carries no editorial
judgment and must not be followed.

### Fact list entry form

One entry per fact, four fields, and a fifth on an overhaul:

    fact: <the fact, as a sentence>
    source: <file:line that settles it>
    disposition: keep | adapt | drop
    heading: <where it landed on the page, once drafted>
    ledger: <the ledger entry id, on an overhaul>

`source` is always a file and line that settles the fact, never a
ledger entry id alone: the ledger is a record of what the old page
covered, not of what is true, so an id cannot stand as source. On an
overhaul, record the ledger entry id too, in `ledger`, alongside the
source that settled it.

`disposition` records what an overhaul did with a fact the ledger
carried: `keep` unchanged, `adapt` with a few words saying how, or
`drop` with a few words saying why. On a new page every fact keeps
`disposition: keep`, since there is no ledger to adapt against.
`heading` is filled in as the draft reaches that heading, not written
up front.

On a fix, the same fields cover the one changed claim, carried
directly in the hand-back rather than as a separate file.

