# Style standard

The voice is formal technical documentation. The reader is at work,
may not be a native English speaker, and may be reading under
pressure.

## Register

Write complete, plain human sentences. Take facts only from the given
inputs; never carry over their phrasing, cadence or sentence shape.

| Say | Not | Why |
|---|---|---|
| exit status 1 | exit 1 | full name, never a shorthand |
| matter | bites | no idiom |
| needs | wants | plain over conversational |
| shows | surfaces | plain over conversational |
| when the restore completes | once the restore completes | "once" keeps its counting sense ("returned once") |

- No hedge or intensifier: "just", "simply", "of course", "actually".
  "Simply" tells a stuck reader they shouldn't be stuck.
- Give a thing no intent, memory or body; name what happens. "Nothing
  your application holds needs changing" has no referent; "the
  connection string doesn't change, so the application needs no edit"
  does. A record, response or field may still "hold" a value.
- Formal means precise and unmarked, not longer.
- Register binds every sentence, including phrasing inherited from a
  ledger or the old page — except a fix's untouched text.
- "You" is fine and usually right. Never "we" or "the user" for the
  reader.

## Vocabulary consistency

- One fixed noun per concept per page, decided before writing; a
  quoted product string using a different noun isn't a violation.
- A quoted product string (button label, error message, field name,
  status value) is reproduced exactly, exempt from every
  wording/vocabulary rule: quote it, or paraphrase outside the
  quotes, never edit inside it. A dialog literally named `Taking
  Pre-Restore Snapshot` keeps that wording quoted even while
  surrounding prose uses the settled term for the action.
- A vocabulary sweep is its own pull request, never folded into a
  fix; a page commissioned for rewriting treats vocabulary as part of
  that change.
- Product truth outranks the one-noun rule: where one noun would drop
  a claim, use two and keep the claim.
- One fixed wording per repeated action; don't vary phrasing across
  steps describing it.

## Verbs

- Say "command", never "verb".
- Choose a verb by its literal sense, not an idiomatic one that
  contradicts it: a trial "provides" a size, not "covers" it — this
  governs a feature's own behavior, not a document's content ("the
  guide covers X" is the fixed verb below, not a violation).
- Prefer the precise verb over the general one: "retains", not
  "keeps"; "navigates", not "moves".
- A control named in prose takes its verb ("selecting Back"), never a
  bare label standing for the action.
- One fixed verb per kind of object:

  | Object | Verb |
  |---|---|
  | Command | run |
  | Page or dialog | open |
  | Control | select |
  | Value | read |
  | Flag | pass |
  | Document (what it explains) | covers |

  "Pass" is the user's own action ("pass `--role` to
  `rotate-password`"). It doesn't cover a command naming its own
  argument — "`cluster create` takes a `--cloud-account-id`"
  describes the interface, not a violation — nor a flag as subject,
  which uses "sets": "`--format` sets `uri`", never "takes".

- Write "run X until Y" for repeated reading. "Poll" is jargon for
  every asynchronous procedure, not a fixed verb for any object.

## Spelling

- pgEdge documentation is US English: behavior, color, initialize,
  center, license, catalog. The standard is set by the public docs
  repository.
- A page written in British spelling is the defect, not the rule. Do
  not read the page you were handed, or its neighbors, as evidence
  that the standard is British.
- Link text is the target page's own title (writing.md), so a British
  word in link text is fixed by retitling the target page and every
  link to it in the same change. Never change the link text alone.
  When the target page is outside the change, this is the one finding
  any job reports and leaves.
- A quoted product string keeps the product's spelling.

## Product names

- Write "Postgres", never "PostgreSQL".
- Product names are proper nouns taking no article, except "the
  Control Plane", which always takes one.
- The product is "pgEdge Starfleet". "Starfleet" never appears
  without "pgEdge" before it. "pgEdge Cloud" is retired and never
  appears.
- Its editions are pgEdge Starfleet Managed and pgEdge Starfleet
  BYOC, shortened to Managed/BYOC after first use, only inside
  pgEdge Starfleet documentation.

## Screen fidelity

- Nothing "carries" a value: a screen, field or badge "shows" or
  "displays" one; a record or response "holds" or "has" one.
- Anything the reader must find, match or click on screen (a button
  label, field name, status value, error message) is quoted from the
  screen verbatim.
- Descriptive prose uses the formal term even where the interface
  shows an abbreviation or a casual word.
- In a table, quote a column of values the reader matches against the
  screen; use the formal term for a column the writer wrote to
  organize the page. When unsure which kind of column it is, quote
  it.

## Settings, time and tense

- A setting "sets" or "determines" a value, never "fixes" one.
- State a time bound as either a wait ("appears within about a
  minute") or a window ("stays for about a minute"), never a form
  that reads as both.
- Write "unknown", never "unmeasured" or "not recorded here".
- Use the present tense for product behavior. Use the past tense only
  for one event the reader has already lived through.

## Banned and rationed

- Never use: leverage, utilize, ensure, seamless, best-in-class,
  synergy, paradigm shift, stakeholder alignment, load-bearing.
- Avoid three negations in a row ("no adapter, no driver patch, no
  extra package"). Say what is true, not a list of what is absent.
- Avoid repeating the same sentence or paragraph skeleton twice
  running, such as "not X, but Y".
- Vary sentence length. A page where every sentence is the same size
  reads as generated.
- Limit any one accumulation word (actually, critical, matters,
  exactly, rather than, at scale) to two uses per page.

A word list catches "leverage" and "seamless", not a shape repeated
until it has a rhythm — and shapes outlast the vocabulary tells
across model generations. Read a draft once for structure alone.
