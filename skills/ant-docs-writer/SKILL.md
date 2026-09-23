---
name: ant-docs-writer
description: "Write, edit or review consumer-facing pgEdge documentation: docs pages, README files, in-app copy, the CLI's embedded llms reference and the shipped agent skills. Use this skill for any page a customer or an agent reads, in pgedge-cli or product-ui. Triggers on: 'write a docs page', 'edit this guide', 'review this documentation', 'fix this README', 'write a tooltip', 'write the llms page', or any request to produce or change customer-facing technical text. Do NOT use for blogs, framing docs, JIRA stories, marketing copy or creative writing, which belong to ant-voice-writer."
---

# ant-docs-writer

The reader is a competent developer who does not know this product.
They are at work, may not be a native English speaker, and may be
reading under pressure. Write formal, plain US English in complete
sentences, addressed to "you". Formal means precise, not longer.

Load `product-vocabulary.md` on every job. Load `in-app-copy.md` for
in-app copy and `agent-pages.md` for a page an agent reads.

## Jobs

Decide the job before writing. Where the request does not say and
there is an existing page, ask: restyle or overhaul.

| Job | Scope |
|---|---|
| Fix | Changes only the facts it was asked to change. No style edits. |
| Restyle | Rewords the page. Facts and section order stay, except that a hazard the page already states may move into Before You Start. |
| Overhaul | Re-establishes every fact from source, and decides the order afresh. |
| New page | Takes its facts from source, and its shape from them. |

## Facts

- Take facts from the generated command reference, the product's own
  code, a vendored spec or a probe log. Where two disagree, a
  measurement beats a spec. A sibling docs page settles nothing, and
  a screenshot is not a source.
- A claim with no source stays off the page. Scope each claim to the
  exact command checked, since the same sentence stated generally is
  often false for a sibling.
- Take from the brief which codebases may be read and whether real
  resources may be created. Look up everything else.
- An overhaul gathers its facts from source before reading the old
  page, and writes without the old page open, so the old phrasing
  cannot carry over. The old page is read afterward, for coverage.

## Writing

- A step is 20 words at most, other prose 25. One instruction per
  sentence. Put the condition before the command.
- Use the active voice and present tense, and name the actor when
  more than one could act. Use "it" only when its referent is in the
  same sentence.
- Open with a sentence saying what the reader can do, then define the
  three or four terms the page leans on, before their first use.
- Order by the reader's task: what they need first, the task, what
  goes wrong, where to go next. Reference material sits after the
  first step that needs it.
- Explain why where the reason changes what the reader does. Keep a
  "because", and do not make the reader reconstruct it.
- Say what the reader sees and can do, never how the platform works
  inside. A number stays only where the reader acts on it. A list of
  cases that will age becomes the general term.
- Delete a sentence the reader would not act differently without, and
  a sentence that restates the page. State an absence only where the
  reader would reach for the missing thing, then say what to do
  instead.
- No trace of the page's history: no issue numbers, dates, "previously"
  or "as of", and no evidence such as "measured" or a fixture name.
  Evidence goes in the pull request.
- Never name a competitor. Tools the reader uses (psql, an ORM) are
  fine.

## Steps and hazards

- A step is an imperative. Its expected result, limit and reason go in
  the step itself, never in a note after it.
- Every command step is runnable as written: full prefix, and a
  placeholder for every value, such as `<db-id>`. A placeholder is
  lowercase and hyphenated, and the page names the command or screen
  that produces its value.
- Before You Start holds only what is specific to this page: a value
  the reader must have and where it comes from, a failure condition,
  or an irreversible action they can reach. Never a login, a shell, a
  network or an account. With nothing specific, there is no section.
- A hazard is an unrecoverable outcome. Mark one or two per page at
  most. State what is lost and when the reader finds out, in the step,
  in the page's ordinary voice. Place it where the reader would take
  the shortcut, and name that shortcut.
- A destructive command is shown interactively, with its prompt.
  Never print its skip-the-prompt flag in a copyable command.

## Format

- One `#` heading. Headings are gerund phrases in title case that
  hold the noun a reader would search for. Before You Start, Next
  Steps and Troubleshooting keep their standard wording.
- A sentence follows every heading, and a sentence ending in a colon
  introduces every list, table and code block.
- A troubleshooting entry gets its own `###` heading named for the
  symptom, then says what the reader sees, the cause and what to do.
- Wrap Markdown at 79 columns, never splitting a link or a table row.
  Leave a blank line before a list. Indent a step's content by four
  spaces.
- Link text is the target page's own title. Command output is pasted
  only from a real run, never composed.
- One noun per concept, and one wording per repeated action. Quote
  anything the reader must find on screen exactly as it renders.
- Vary sentence length, and do not repeat one sentence shape
  ("not X, but Y") until it has a rhythm.

## Gates

Run both scripts from this skill's directory on the draft. They catch
the house style's word, spelling, punctuation and readability rules,
and name the fix for each finding. Every job but a fix passes both.

    <skill>/check-mechanics.py <page.md>
    <skill>/signals.py <page.md>

A fix runs check-mechanics.py against the old page and passes that:

    old=$(mktemp); git show main:<page.md> > "$old"
    <skill>/check-mechanics.py --baseline "$old" <page.md>

A British spelling in link text whose target is outside the change is
the one finding reported and left.

## Review

- Fix, overhaul, new page: someone other than the writer checks every
  changed claim against its source. On an overhaul, that reviewer also
  lists each fact on the old page that the new page lacks. On a new
  page, the reviewer lists any flag or behavior of the documented
  commands that a reader needs and the page omits.
- Restyle: read your own old-versus-new diff for a fact added, dropped
  or changed, and a condition, number or hazard weakened. Watch for a
  same-length wrong value, such as a swapped flag name.
- Only a wrong fact compels a change. Take the other findings that
  help the reader, and refuse the rest with a reason.

## Hand back

The job done, the gate results, and each review finding with what
changed. A fix, overhaul or new page also hands back a table of each
claim it changed or wrote, with its source file:line.
