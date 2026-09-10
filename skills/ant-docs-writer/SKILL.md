---
name: ant-docs-writer
description: "Write, edit or review consumer-facing pgEdge documentation: docs pages, README files, in-app copy, the CLI's embedded llms reference and the shipped agent skills. Use this skill for any page a customer or an agent reads, in pgedge-cli or product-ui. Triggers on: 'write a docs page', 'edit this guide', 'review this documentation', 'fix this README', 'write a tooltip', 'write the llms page', or any request to produce or change customer-facing technical text. Do NOT use for blogs, framing docs, JIRA stories, marketing copy or creative writing, which belong to ant-voice-writer."
---

# Writing pgEdge consumer documentation

One style for every page a customer or an agent reads, across
pgedge-cli and product-ui. It replaces ant-voice-writer for this work.
That skill writes in Ant's voice, which is the right voice for a blog
and the wrong voice for a procedure.

The style has two halves and the order between them is not optional.
The content checklist runs first, because a page can pass every prose
rule in this file and still be unusable. That has happened. A page
rewritten against an explicit list of prose targets hit every one of
them, and a reader with no context judged it unusable anyway, on four
faults that no prose rule addresses.

What this skill does not carry: product decisions and repo mechanics.
Those stay in each repository's own `CONSUMER-DOCS-RULES.md`, which
names the backup vocabulary, the settled product rulings, the build
gates and the navigation files. Read this skill first, then that file.

## The content checklist

Run all seven before writing a sentence, and again before opening a
pull request. Each is a question with a failing answer, not a
preference.

**1. Can the reader type every command exactly as printed?** A command
needs its full prefix, the connection flag the reader's setup requires
(`--base-url` or `--profile`), a placeholder for every value, and every
flag a non-interactive run needs. A command that silently assumes a
default the reader does not have is unrunnable for everyone else.

**2. Does the page say where every value it asks for comes from?**
Every placeholder gets a sentence naming the command or the screen that
produces it. A page that asks for a database ID and never says how to
find one has handed the reader a search engine, not an instruction.

**3. Does the page work for a reader who did not create the resource?**
"The spec you submitted" and "the password you chose" both fail for the
operator who inherited the system. Say where the value lives now, and
what to do when the reader does not have it.

**4. Is every term defined before the first sentence that leans on it?**
On the page, in one sentence, not behind a link the reader has to open
mid-incident. This applies hardest to a distinction the procedure
depends on, such as instance against node against host.

**5. Does the page answer the question its own opening raises?** An
opening that says a backup runs per node owes the reader an answer to
"then does backing up one node back up the database". A question raised
and dropped is worse than one never raised.

**6. Does any step destroy something a later step needs?** Read the
procedure as a sequence and track state. A restore that clears the
configuration a later recovery step tells the reader to retype needs a
step that saves it first, before the destructive one.

**7. Strip every note and read the procedure again.** If the reader can
no longer finish it, the information in that note belongs in a step.
Move it and repeat the test.

## Sentences

- A step is 20 words at most. Descriptive prose is 25 words at most.
  The extra five words in prose exist to pay for a "because", and
  spending them on one is the point of the split.
- One instruction per sentence, unless two actions happen at the same
  time. "Remove and discard the old spec" is one action in two verbs.
  "Save the spec and run the restore" is two steps.
- Put a condition first, then a comma, then the command. "When the
  status is available, read the password back."
- Write in the active voice, in the present tense.
- A passive verb that leaves out who performs the action is a defect
  whenever more than one candidate is nearby. "A message saying the
  resource is busy and should be retried" reads as though the resource
  is retried. The operation is retried. Name it.
- Write in the singular. "The database", not "databases". The singular
  usually turns a passive sentence active on its own.
- Do not use "it" unless the referent is in the same sentence. Name the
  thing again.
- Never omit a word to make a sentence shorter, and never use a
  contraction. A sentence missing its subject, verb or article is
  shorter and harder.

## Steps and procedures

- Write a step in the imperative. Not "the test can be continued", but
  "continue the test".
- Do not put "must" in front of an imperative unless the instruction
  guards against data loss or an unrecoverable state.
- A note gives information and never an instruction. An imperative in a
  note has turned that note into a step, so make it one.
- A limit, a tolerance or the expected result of a step goes in the
  step, immediately after the action, never in a note beside it.
- Numbered lists are for sequences only. If the steps work in any
  order, they are bullets.

## Descriptive prose

- One topic per sentence. One topic per paragraph. Six sentences at
  most in a paragraph.
- Open a paragraph with its topic sentence. A reader who copies out
  only the topic sentences should end up with an outline of the page.
- Give information gradually. A sentence that introduces three new
  nouns at once will be read twice.

Carry the thread between sentences by repeating the key noun as the
subject of the next one, rather than by reaching for a connective.
Short sentences are what the 20 and 25 word caps give you, and without
a thread they read as a disconnected list:

    A restore rebuilds the named nodes from the repository.
    Everything written since the backup is lost. The backup
    configuration is cleared. Schedules go with it.

Four true sentences, and the reader has to work out the relationship
between them. Repeating the noun does that work instead:

    A restore rebuilds the named nodes from the repository. The
    restore also discards everything written since the backup, and
    clears the database's backup configuration. That configuration
    holds every schedule, so the schedules go with it.

The subjects chain: restore, restore, configuration, configuration.
Nothing starts with a conjunction and it still reads as prose.

This is the same move as "do not use it unless the referent is in the
same sentence", arrived at from the other side. That rule forces you to
repeat the noun to prevent ambiguity. This one tells you the repetition
is also what creates the flow, which is the difference between doing it
grudgingly and doing it deliberately. A writer who knows only the first
reason repeats the noun, finds the result choppy, and reaches for
"However," to fix a problem they did not have.

## Register

The voice is semi-formal technical documentation. The reader is at
work, may not be a native English speaker, and may be reading under
pressure. Every rule below follows from that.

- **Name a technical thing by its full name.** "exit status 1", not
  "exit 1". "the connection string", not "the string". Shorthand is
  something the writer knows and the reader has to guess.
- **No idiom.** "Carry weight", "a way back", "the shape of it", "lands
  wrong", "bites", "worth knowing" are invisible to a native speaker
  and opaque to everybody else. There is always a plain word: "matter",
  "a way to undo it", "the structure".
- **No conversational hedges or intensifiers.** "Pretty much", "just",
  "simply", "of course", "actually". "Simply" is the worst of them,
  because it tells a reader who is stuck that they should not be.
- **Prefer the plain formal word where two words mean the same thing
  and differ only in register.** "Needs", not "wants". "Shows", not
  "surfaces". "Before", not "ahead of".
- **Formal does not mean longer.** It means precise and unmarked. A
  sentence that has to be read twice for its tone is as broken as one
  that has to be read twice for its grammar.

## Words

- One noun for one concept, for the whole page. Write the page's
  vocabulary down before writing the page: pick "node" or "instance",
  "task" or "operation", "rule" or "monitor", and never alternate. A
  single page once used rule, script, sweep, monitor and poll for the
  same thing.
- One wording for one repeated action. If step 2 says "apply a small
  quantity of oil to the threads", step 6 does not say "lubricate".
  Different wording for the same action reads as a different action.
- "Command", never "verb". "Verb" is the CLI team's word.
- One verb per kind of object, and the standard verb is the plain one.
  You **run** a command. You **open** a page or a dialog. You **select**
  a control. You **read** a value, a field or a status. You **pass** a
  flag to a command, and a flag **sets** a value. Not "query a command",
  not "hit an endpoint", not "fire a request", not "grab a value". This
  is the one-wording rule applied to the verb rather than the phrase,
  and it is the rule that catches "Read `database get`", which sounds
  right and is not: you run it.
- "Postgres", not "PostgreSQL".
- Product names are proper nouns and take no article: pgEdge Cloud,
  Spock, pgEdge Postgres MCP Server. The exception is "the Control
  Plane", which always takes one.
- A screen, field or badge "shows" or "displays" a value. It does not
  "carry" one.
- A setting "sets" or "determines" a value. It does not "fix" one,
  which reads as a bug fix. "Fixed" is not the word for immutable.
- "Unknown", never "unmeasured" or "not recorded here". The reader does
  not care what the author got around to.
- Banned outright: leverage, utilize, ensure, seamless, best-in-class,
  synergy, paradigm shift, stakeholder alignment.

## Punctuation

- No em-dashes. Use a comma, a period or parentheses.
- No semicolons in new text. Write two sentences. Never strip a
  semicolon out of text that already exists, because a punctuation-only
  edit hides the technical change underneath it in review.
- Do not start a sentence with And, So, Or or Yet. "And" is almost
  always deletable, because a following sentence adding to the previous
  one is the default reading anyway. "So" becomes "Thus" or "As a
  result".
- "But" at the start of a sentence is allowed where that sentence
  qualifies the one before it. Nothing short replaces it, and the
  alternative, "However,", is stiffer than anything else in this file.
- Use a hyphen for a compound modifier before a noun: read-only role,
  copy-on-write branch, single-node database.

## No signposting

A sentence that carries no information, and only points at
information, is slower than the thing it points at. Delete it.

Delete on sight: "this section covers", "now that we have", "it is
worth noting", "importantly", "crucially", "pay special attention",
"the catch is", "note that", "worth knowing", "and this is why it
bites". State the fact and stop.

A lead-in sentence carries a fact. It never restates the heading above
it.

No forward-looking text. Not "yet", "coming", "planned", "soon", or
"today" used as a temporal hedge. Describe what is.

## How a page opens

Every page opens with a sentence. A gerund or a noun phrase standing in
for one is a fragment however long it runs, and twenty-six guides opened
that way before anyone noticed. This applies to the first sentence of
the body, never to the heading above it, which is a different rule
entirely and is given below.

The opening gets a new reader ready before it teaches anything:

- What the page does, or what has gone wrong.
- A linked index of the sections, when there are more than three.
- The three or four terms the page leans on, one sentence each.
- Which commands change something.
- What to collect before starting, and the command or screen that
  produces each value.

Say what the reader can do before what the product cannot. A page that
opens with five things the product does not do has told the reader
nothing they can act on.

Headings are gerund phrases in title case: "Backing up and Restoring a
Managed Database", "Understanding a Backup", "Rotating a Credential".
This is the house form, it is what the existing pages use, and an
imperative heading is the common way to break it. Name what the section
contains, in words a customer would search for. Never a sentence, never
a question with no answer, never a judgement, and never a dash carrying
a second clause.

A run of steps is a numbered list, not a run of headings. Promoting each
step to its own heading fills the navigation pane with fragments and
loses the sequence. Indent anything belonging to a step by four
spaces.

## Format

- Markdown, greedy-wrapped at 79 characters: fill each line as far as it
  will go before breaking, rather than breaking early at a comma or a
  phrase. Never split a link or a table row, whatever the line length.
- One `#` heading per file. Every heading is followed by at least one
  sentence before any list, table or code block.
- Blank line before the first item of every list. The lead-in ends in a
  colon and the bullets complete it.
- Bullets for anything countable, tables for comparisons, prose for
  reasoning. More than four items is a list, not a sentence.
- No bold used as a heading and no standalone bold label. MkDocs can
  promote either into the navigation pane.
- Introduce every code block with a sentence, ending in a colon, that
  names the command and says what it does.
- Describe command output in prose. Paste a block only where prose
  cannot teach the shape, and then only text captured from a real call,
  never composed by hand and never tidied up afterwards. This rule is
  about output blocks. It says nothing about screenshots, which are a
  product decision and not a style one.

## Editing text that already exists

- Keep the fact, drop the archaeology. "Since #448, --interval is a
  lookback" becomes "--interval is a lookback."
- Never delete a technical claim unless the same claim already stands
  elsewhere on the page. A history sentence often carries the only
  statement of a current behaviour.
- An observation is not a bound. Two samples of 29 and 34 columns
  become "can return 29 or 34", never "as few as 29".
- A caveat kept on one surface is kept on every parallel surface. The
  docs page, the reference page, the skill and the tooltip must agree
  about how confident a claim is.
- A renamed heading is quoted somewhere. Grep for the old name,
  including wrapped across a line break, before calling the rename
  done.
- A rename orphans the sentence under it. A "This" with no antecedent
  means the old heading was the antecedent.
- State a caveat once per section. Three restatements read as a lab
  notebook.
- In a pull request that changes facts, do not touch a sentence for
  style alone. Voice and punctuation changes to existing text go in
  their own pull request, so a reviewer can tell a technical change
  from a preference.

## Never invent

- Every command and flag exists in the generated reference. Every
  behavioural claim traces to a live capture, a spec field or an
  existing gated page. A claim with no source stays out, and what is
  true goes in its place.
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

## Reviews

Every documentation change gets two reviews and one fix round.

The correctness reviewer checks every claim against its source. The
writer supplies a claim-to-source list so the reviewer verifies claims
rather than rediscovering them.

The cold-read reviewer gets no repository context at all, only the page
and the pages it links to. They read as the customer and report where
they got lost, what they could not type, and what they would search the
web for instead.

The two find different defects and neither finds the other's. Run both,
even on a small change.

## Further reading

- [ste-adoption.md](ste-adoption.md) records which ASD-STE100 rules
  this style takes, adapts or drops, and why. Read it when a rule here
  looks arbitrary.
- [agent-pages.md](agent-pages.md) carries the divergences for pages
  read by agents rather than people: the CLI's embedded `llms` pages
  and the shipped skills.
