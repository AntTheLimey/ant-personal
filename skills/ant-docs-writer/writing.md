# Writing

Loaded by every job.

## Sentences

- A step is 20 words at most; descriptive prose is 25 words at most.
- Count words the STE way: a backticked or quoted span, a number, a
  number-with-unit, an abbreviation, a hyphenated word and a
  parenthetical each count as one word.
- The caps apply per prose sentence: bullets, indented text and
  lead-ins alike. A table cell and image alt text are exempt.
- One instruction per sentence, unless two actions happen at the same
  time. "Remove and discard the old spec" is one action in two verbs;
  "Save the spec and run the restore" is two steps.
- Put a condition first, then a comma, then the command.
- Write in the active voice and the present tense.
- A passive verb that omits the actor is a defect whenever more than
  one candidate could be the actor; name the actor. "The resource is
  busy and should be retried" reads as though the resource is
  retried; the operation is retried.
- Write in the singular: "the database", not "databases".
- Do not use "it" unless the referent is in the same sentence; name
  the thing again.
- Never omit a word to shorten a sentence, and never use a
  contraction; omitting a word makes a sentence shorter and harder.

## Reading signals

Run `signals.py` on the draft before finishing, on a restyle,
restructure, overhaul or new page, and report what it says. It strips
code, tables and headings first and measures prose only.

- Reading ease has a floor of 58. Overhauled pages sit at 61-62
  unaimed; the floor catches drift, not a page that is trying.
- Grade (Flesch-Kincaid) has a ceiling of 8.0, close to a mean
  sentence of 13 to 15 words. Treat it as a tripwire, not the thing
  that makes a page readable: never a license to cut a clause
  carrying a condition. Where a fact needs a long sentence, split the
  sentence, not the fact.
- Keep a causal connective ("because") rather than cutting it; do not
  make the reader reconstruct why one sentence follows another.
- The script's 20/25-word sentence-length count sets no exit status;
  only the reading-ease floor and the grade ceiling fail a run.

## Punctuation

- No em-dashes; use a comma, a period or parentheses. The verbatim
  quoted core instruction in SKILL.md is the one exempt text.
- No semicolons in new text; write two sentences instead. Never strip
  a semicolon from existing text: a punctuation-only edit would hide
  the technical change underneath it.
- Do not start a sentence with And, But, So, Or or Yet:

  | Opens with | Fix |
  |---|---|
  | And | delete it |
  | So | "Thus" or "As a result" |
  | But | "However," |

- Use a hyphen for a compound modifier before a noun: read-only role,
  copy-on-write branch, single-node database.

## Signposting

- Delete a sentence that carries no information and only points at
  information. Delete on sight: "this section covers", "it is worth
  noting", "note that", "this page covers". State the product fact
  instead; the page is never the subject of its own sentences.
- A structural lead-in introducing a list or table is not
  signposting: keep it to one clause naming what the list holds,
  ending in a colon.
- No forward-looking text: "yet", "coming", "planned", "soon", "today"
  as a hedge. Describe what is.
- No inline index of the page's own sections: no bulleted link list,
  no "this page has N sections", no table of contents. A README is
  the one exception, since GitHub renders it with no navigation pane.

## Paragraphs and flow

- One topic per sentence, one topic per paragraph, six sentences at
  most per paragraph.
- Open a paragraph with its topic sentence; the topic sentences alone
  should outline the page.
- Give information gradually; a sentence introducing three new nouns
  at once gets read twice.
- Carry the thread between sentences by repeating the key noun as the
  next sentence's subject, rather than reaching for a connective.
  Four true sentences read as a list:

  > A restore rebuilds the named nodes from the repository. Everything
  > written since the backup is lost. The backup configuration is
  > cleared. Schedules go with it.

  Repeating the noun turns them into one line of reasoning:

  > A restore rebuilds the named nodes from the repository. The
  > restore also discards everything written since the backup, and
  > clears the database's backup configuration. That configuration
  > holds every schedule, so the schedules go with it.

## Openings

- Every page opens with a sentence; a gerund or noun-phrase fragment
  does not count, however long it runs.
- The opening states what the page does, or what has gone wrong, and
  defines the three or four terms the page leans on, one sentence
  each, as facts about the product, never as an announcement about
  the page.
- Say what the reader can do before what the product cannot; an
  opening built from things the product doesn't do gives nothing to
  act on.

## Steps

- Write a step in the imperative, not a passive or modal description.
- Do not put "must" before an imperative unless the instruction guards
  against data loss or an unrecoverable state.
- A note gives information only, never an instruction; an imperative
  inside a note makes it a step, so convert it.
- A limit, tolerance or expected result of a step goes in the step
  itself, right after the action, never in a separate note.
- A step whose point is not obvious carries its own reason, in the
  step, especially where skipping it is unrecoverable; a reader who
  has already skipped it gets nothing from a reason parked elsewhere.
- Numbered lists are for sequences only; steps that work in any order
  are bullets. Number steps in true sequence, not repeated "1.". A run
  of steps stays a numbered list, not a run of headings. The exception
  is a lookup list (symptoms, error messages, states the reader scans
  to find their case): never number it, and give each entry its own
  `###` heading instead of a bullet.
- Indent everything belonging to a numbered step by four spaces.
- An indented block under a bullet reads as a note, and the content
  checklist (shape.md) counts it as one; a bullet needing a second
  sentence keeps it in the same paragraph. A bullet needing more than
  prose is usually a step in disguise and should become one.
- "Before You Start" (or "Prerequisites") holds only entries specific
  to this page: a value the reader must have, with its producing
  command or screen (a database ID and the backup ID it restores from
  are entries); a task-specific failure condition; a reachable
  irreversible action; and, on a console page, the starting screen and
  the route to it.
- An entry true of every page (an authenticated profile, a supported
  shell, a network connection, an account) does not belong there. If
  nothing page-specific survives, carry no Before You Start section;
  an empty one costs attention and teaches the heading is skippable. A
  page-specific precondition goes in at the point it was discovered,
  so a reader meeting the list has met every condition the page can
  predict.
- A step whose command changes something says so in that same step,
  not in an opening paragraph read earlier. Do not print a destructive
  flag in a copyable command; show it running interactively, prompt
  intact, and describe the skipping flag in the text. The scripted
  (flag-included) form belongs on the automation page, not the
  interactive procedure.
- A step that tells the reader to become someone else gives them the
  means (host, port, database name) in that same step. A step that
  needs a table gets the table in its own section, linked from the
  step, not nested inside a list item.

## Hazards

- A hazard is written in the same voice as the rest of the page; do
  not harden the register because the stakes rose. State the fact of
  what silently goes wrong, the strongest hazard sentence a page can
  carry, then stop; do not follow it with an imperative that repeats
  the same fact.
- Ration hazard marking to one or two per page, only for outcomes that
  are genuinely unrecoverable; a mistake the reader can undo, repeat
  or retry needs no marking. A page with six marked hazards has none:
  the reader learns the marking means nothing.
- A step preventing an unrecoverable outcome states the consequence in
  the step itself: what the reader loses and when they find out.
- A marked hazard names, in the third person, the shortcut the reader
  would take instead and its cost, naming the action and object in
  full, and sits on its own line: use the repository's admonition
  rendering, or a short line opening with what is lost.
- Every irreversible action the reader can reach before its guard
  belongs in Before You Start, named individually; naming one and
  omitting others reads as permission for the rest.
- On a restyle or restructure, hazard placement reaches only a hazard
  already stated on the page. Moving a stated hazard into Before You
  Start is the one ordering exception a restyle may make, named in the
  hand-back. Neither job invents a new hazard with no existing
  statement on the page; report a missing one as a gap in the
  hand-back instead.
- Ask what the reader will do instead of the written step, and address
  that instinct directly, not only the step as written. Place a
  warning where the reader's instinct fires, not only where the topic
  lives; write it in both places if they differ. This overrides
  "state a caveat once per section" below.

## Format

- Markdown is greedy-wrapped at 79 characters; never split a link or a
  table row regardless of line length.
- One `#` heading per file; every heading is followed by at least one
  sentence before any list, table or code block.
- Blank line before the first item of every list; the lead-in ends in
  a colon.
- Use bullets for anything countable, tables for comparisons, prose
  for reasoning; more than four items is a list, not a sentence.
- No bold used as a heading and no standalone bold label, since MkDocs
  can promote either into the navigation pane.
- Alt text describes what the image shows as a noun phrase, exempt
  from the sentence rules and word caps, and never carries a fact
  found nowhere else on the page.
- A placeholder is lowercase and hyphenated inside angle brackets
  (`<db-id>`); never the underscored form of a real field name, which
  a build gate reads as a claim the field exists.
- An image sits inside the step or under the heading it illustrates,
  indented to match; it does not substitute for the heading's required
  sentence.
- Link text is the target page's own title.
- A page's navigation label matches its `#` heading, or a shortened
  form keeping the gerund; change the navigation file in the same
  pull request as a heading rename.

## Code blocks and output

- Introduce every code block with a sentence, ending in a colon, that
  names the command and says what it does. Four forms introduce a
  fenced block: a bare "**Example:**"; a qualified "**Example
  (AWS):**"; prose ending in a colon; or a "**Step N:**" heading
  covering its own fences. Never add a label after a colon that
  already introduces the block.
- Describe command output in prose; paste a block only where prose
  cannot teach the shape, and then only text captured from a real
  call, never composed or tidied by hand.

## Headings

- Headings are gerund phrases in title case, except the fixed
  conventional navigational headings ("Next Steps", "Troubleshooting",
  "Before You Start", "Prerequisites"), which keep their standard
  wording.
- A heading using the full edition name counts as that name's first
  appearance on the page.
- The searchable noun a customer would search for goes inside the
  gerund phrase; a heading hiding it is wrong, not the rule. An
  imperative heading is the common way to break this.
- Never write a heading as a sentence, a question with no answer, a
  judgment, or with a dash carrying a second clause.
- A README follows every sentence, word and wrap rule, but opens with
  what the thing is and how to install it, not with what the reader
  will do. It is the one page allowed a linked index of its own
  sections, only past a screen's length.

## Troubleshooting entries

A troubleshooting entry states, in order, what the reader sees, what
causes it, what to do. Name the entry for the symptom, not the cause,
and give it its own `###` heading.

## Two orderings that are always wrong

A destructive action printed before the step that makes it
survivable, and a definition placed after the sentence that leans on
it. Placing a hazard step first does not stop a reader skipping it;
order is necessary and not sufficient on its own.

## Editing existing text

- Keep the fact, drop the archaeology: "Since #448, --interval is a
  lookback" becomes "--interval is a lookback".
- Never delete a technical claim unless the same claim already stands
  elsewhere on the page.
- An observation is not a bound; state the sampled range, never a
  floor or ceiling implied from it: "can return 29 or 34", never "as
  few as 29".
- A caveat kept on one surface (docs page, reference page, skill,
  tooltip) is kept at matching confidence on every parallel surface.
- Scope every claim to the exact command and module actually checked;
  the same sentence written generally is often false for a sibling.
- A renamed heading must be grepped for and updated everywhere it is
  quoted, including wrapped across a line break. Check the rename did
  not orphan a "This" with no antecedent in the sentence below the old
  heading.
- State a caveat once per section; three restatements read as a lab
  notebook. The instinct-placement rule above overrides this where
  the two conflict.
- On a fix, in a pull request that changes facts, do not touch a
  sentence for style alone; voice and punctuation changes to existing
  text go in their own pull request.

## No internal history

- A page carries no trace of its own history or authorship: no
  issue/PR numbers, ticket ids, commit hashes, dates, or "measured on"
  attempt counts, no tenant, profile, fixture or colleague, no
  internal service, source symbol, or build/test name offered as
  proof.
- No archaeology language ("previously", "used to", "an earlier
  version", "since version N", "as of"); state current behavior in
  the present tense with no citation. A statement of current state
  ("The repository is internal") is not archaeology and stays.
- Evidence lives in the pull request, never on the page; never leave a
  sourcing HTML comment in a customer-facing page. Dates, sample
  counts, fixture names and the words "measured", "polled" and
  "probe" stay in the pull request: the measurement is the reason a
  sentence is true, never the sentence itself.
- Write a caveat for the reader's action, never as a lab note: "no
  list of values for this field, so treat anything other than X as a
  fault" is right; "recorded from observation" is not.

## Say less, or say nothing

- Keep the consequence, drop the mechanism: tell the reader what they
  can do and see, never how the platform does it internally.
- No list of cases that will age: "a restore, resize, service change
  or credential rotation" becomes "a modification".
- No scope creep: a field, badge or section explains only itself, not
  a neighboring feature.
- A number stays in prose only when the reader acts on it; otherwise
  link to the one page that owns it. Where "act here" and "link out"
  pull apart, ask where the reader acts: a price in a size table they
  are choosing from stays; the same price in a billing sentence links
  out.
- Never name a competitor or another vendor's database service.
  Third-party tools the reader actually uses (psql, pgAdmin, an ORM,
  an IDE) are fine. A migration page may name the source service it
  migrates from, on that page only.
- A changelog entry describes the product, never the work done.
- On a fix, an overhaul and a new page: sort every sentence by "would
  the reader act wrong without this fact". Delete it if no. If yes,
  keep the fact and cut everything propping it up: make the product
  the subject, never the documentation, and state what the reader
  sees, not what causes it. Cut a "so" clause from a sentence that
  explains itself, and stop after one sentence. Delete a sentence the
  reader would have assumed anyway, one restating a reason the page
  already gives, or one it already carries.
- On a restyle or restructure, only a restatement (the same fact
  stated elsewhere on the page) sorts to delete. A fact stated once
  is kept, and listed in the hand-back as a deletion candidate, never
  cut.
- An absence claim ("no command deletes a backup") sorts to delete
  unless a reader would genuinely reach for the missing thing, such as
  "This CLI has no command that deletes a backup" or "`backup create`
  has no `--wait`, and neither has `backup get`". Where a reader would
  reach for it, say what to do instead, never state the absence more
  briefly. A section built entirely of negatives is the same failure
  at section scale.

## Repository mechanics

- Never edit inside a generated block; change the source it is
  generated from, then regenerate.
- A new page gets its navigation entry and its changelog entry in the
  same change that adds it.
- Run the documentation gates (test suite, prose linter, reference
  drift check) before opening a pull request.
- Guides live under `docs/` in a directory per edition, matching the
  edition their commands name; root-level markdown is UPPERCASE,
  everything under `docs/` is lowercase.
- Every link is checked before the page ships: link by relative path,
  use the target's own title as link text, and open the target to
  confirm it answers what the reader was sent there for.
