# Style standard

Loaded by every job. Handed unchanged to a cold reader.

The voice is formal technical documentation. The reader is at work,
may not be a native English speaker, and may be reading under
pressure.

## Register

- Write complete, plain human sentences. Take facts only from the
  given inputs; never carry over their phrasing, cadence or sentence
  shape.
- Name a technical thing by its full name, never a shorthand the
  reader has to guess: "exit status 1", not "exit 1".
- Use no idiom. A plain word exists: "matter", not "bites".
- Use no conversational hedge or intensifier: "just", "simply", "of
  course", "actually". "Simply" tells a stuck reader they should not
  be stuck.
- Give a thing no intent, memory or body; name what actually happens.
  "Nothing your application holds needs changing" names no referent
  and fails; "the connection string does not change, so the
  application needs no edit" says the same thing about things that
  exist. A record, response or field may still "hold" a value.
- Prefer the plain formal word where two differ only in register:
  "needs" not "wants", "shows" not "surfaces".
- Write "when", not "once", to introduce a clause about time: "when
  the restore completes". "Once" keeps its counting sense, as in
  "the secret is returned once".
- Formal means precise and unmarked, not longer.
- Register rules bind every sentence in a rewrite, including phrasing
  inherited from a ledger or the old page. Only a fix's no-style-touch
  rule exempts untouched text.
- "You" is allowed and usually correct. Never write "we" or "the
  user" for the reader.

## Vocabulary consistency

- Fix one noun for one concept for the whole page, decided before
  writing. A quoted product string using a different noun is not a
  violation.
- A quoted product string (button label, error message, field name,
  status value) is reproduced exactly and is exempt from every
  wording and vocabulary rule in this skill. A dialog really named
  `Taking Pre-Restore Snapshot` is quoted with its wording intact,
  even though prose around it uses the settled word for that action.
  Quote it, or paraphrase it outside the quotation marks; never edit
  inside it.
- A page-wide vocabulary sweep is its own pull request, never folded
  into a fix. A page commissioned for rewriting treats vocabulary as
  part of that one change.
- Product truth outranks the one-noun rule: where one noun would drop
  a claim, keep the claim and use two nouns.
- Use one fixed wording for one repeated action. Do not vary the
  phrasing across steps describing the same action.

## Verbs

- Say "command", never "verb".
- Choose a verb by its literal sense, not an idiomatic one that
  contradicts the action: a trial "provides" a size, not "covers" it.
  This governs a feature's own behavior, not what a document explains;
  "the [guide] covers [topic]" is the fixed verb for a linked
  document's content (see the object table) and is not a violation of
  this rule.
- Prefer the precise verb over the general one: "retains", not
  "keeps"; "navigates", not "moves".
- A control named in prose takes its verb ("selecting Back"), never a
  bare label standing for the action.
- Use one fixed verb per kind of object:

  | Object | Verb |
  |---|---|
  | Command | run |
  | Page or dialog | open |
  | Control | select |
  | Value | read |
  | Flag | pass |
  | Document (what it explains) | covers |

  "Pass" governs the user's own action ("pass `--role` to
  `rotate-password`"). It does not cover a command naming what it
  accepts as an argument: "`[Command]` takes `[Flag]`" ("`cluster
  create` takes a `--cloud-account-id`") describes the command's
  interface, not a user action or a flag setting a value, and is not
  a violation of this table. Where a flag itself is the grammatical
  subject taking a value, use "sets": "`--format` sets `uri`", never
  "`--format` takes `uri`".

- Write "run X until Y" for repeated reading. "Poll" is jargon for
  every asynchronous procedure and is not a fixed verb for any one
  object.

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
  any job reports and leaves; gates.md names it.
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

A word list catches "leverage" and "seamless". It does not catch a
shape repeated until it has a rhythm, and shapes survive across model
generations after the vocabulary tells have gone. Read a draft once
looking only at structure.
