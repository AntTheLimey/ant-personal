## Register

The voice is formal technical documentation. The reader is at work,
may not be a native English speaker, and may be reading under
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
- **No anthropomorphism. A thing does nothing that needs intent,
  memory or a body.** That general test is the rule; know, want, see,
  care, remember, think, decide, expect, believe, try and forget are
  examples of it failing, and the ninth verb you reach for is bound by
  the test even though it is not listed here. Name what actually
  happens instead: "nothing your application holds needs changing"
  fails, because it names no referent the reader can check, and "the
  connection string does not change, so the application needs no edit"
  says the same thing about things that exist. This is the idiom rule's
  hardest case, because an anthropomorphism reads as plain English to
  whoever wrote it. **"Holds" is not on this list**: a record, a
  response or a field holds a value, which is the wording required
  under "Words". What failed in the example was the application as
  subject, not the verb.
- **Prefer the plain formal word or phrase where two mean the same
  thing and differ only in register.** "Needs", not "wants". "Shows",
  not "surfaces". "Before", not "ahead of". This applies to whole
  constructions, not only to single words: "a restore can report
  additional steps", not "a restore can report more of them".
- **Formal does not mean longer.** It means precise and unmarked. A
  sentence that has to be read twice for its tone is as broken as one
  that has to be read twice for its grammar.
- **These rules bind every sentence in a rewrite, including the ones
  that came from the page you are replacing.** A phrase that reached
  you through a fact ledger is still a phrase you are publishing under
  your own name. Inheriting an idiom is not a reason to keep it, and
  "it was already there" is not a defense a reader ever sees. This is
  the "do not touch a sentence for style alone" rule does not reach.
  That rule governs a **fix** job, where the diff must stay readable
  enough to review. **An overhaul, a restructure and a restyle are all
  bound by the register rules**: in an overhaul every sentence is new,
  a restructure rewrites all wording, because it includes a restyle,
  and a restyle has sentences, words and headings in scope by
  definition.
- **"You" is allowed and is usually the right answer.** Removing it
  tends to produce the agentless passive this file bans two rules
  higher up. "After you authenticate" beats "after authentication is
  complete". Do not write "we", and do not write "the user" about the
  person reading the page.

## Words

- One noun for one concept, for the whole page. Write the page's
  vocabulary down before writing the page: pick "node" or "instance",
  "task" or "operation", "rule" or "monitor", and never alternate. A
  single page once used rule, script, sweep, monitor and poll for the
  same thing. The rule governs your own words: **a quoted
  product string using a different noun is not a violation**, because
  those are the product's words. Quote the error exactly and use your
  own noun in the prose around it.
- The one-noun rule applies within the change you are already making. A
  page-wide vocabulary sweep is its own pull request, never something
  folded into a factual fix, because a reviewer cannot then tell the two
  apart. This scopes a **fix**, not a rewrite. A page commissioned for
  rewriting is one change, and its vocabulary is part of that change.
- The one-noun rule is house style, so product truth outranks it. Where
  the only way to use one noun is to drop a claim, keep the claim and
  use two nouns. See "When two rules conflict".
- One wording for one repeated action. If step 2 says "apply a small
  quantity of oil to the threads", step 6 does not say "lubricate".
  Different wording for the same action reads as a different action.
- "Command", never "verb". "Verb" is the CLI team's word.
- **Choose a verb by its literal sense, not its idiomatic one.** A free
  trial does not "cover" the smallest size, because covering is
  obscuring; it provides it. A page does not "cover" a topic; it
  describes one. A verb whose plain meaning contradicts the action makes
  a reader stop, and it translates badly.
- **Prefer the precise verb to the general one.** The wizard "retains"
  an entry rather than "keeps" it, the reader "navigates" between steps
  rather than "moves" between them, and `Back` "does not discard any
  entered value" rather than "loses nothing".
- **A control named in prose takes its verb.** Write "selecting Back",
  or "the Back button", never a bare label standing in for the action.
- One verb per kind of object, and the standard verb is the plain one.
  You **run** a command. You **open** a page or a dialog. You **select**
  a control. You **read** a value, a field or a status. You **pass** a
  flag to a command, and a flag **sets** a value. For repeated reading,
  write "run X until Y" rather than "poll". Every asynchronous
  procedure needs this and "poll" is jargon. Not "query a command",
  not "hit an endpoint", not "fire a request", not "grab a value". This
  is the one-wording rule applied to the verb rather than the phrase,
  and it is the rule that catches "Read `database get`", which sounds
  right and is not: you run it.
- "Postgres", not "PostgreSQL".
- Product names are proper nouns and take no article: pgEdge Starfleet,
  Spock, pgEdge Postgres MCP Server. The exception is "the Control
  Plane", which always takes one.
- **The product is pgEdge Starfleet, and "Starfleet" never appears
  without "pgEdge" in front of it.** Its editions are pgEdge Starfleet
  Managed and pgEdge Starfleet BYOC, shortened to Managed and BYOC after
  first use inside the pgEdge Starfleet documentation. "pgEdge Cloud" is
  the retired name and does not appear. `product-vocabulary.md` carries
  the whole ruling, including why a command is not a name.
- Nothing "carries" a value. A screen, field or badge "shows" or
  "displays" one; a record or a response "holds" or "has" one.
- When the product's own word for a thing differs from the word the
  documentation uses, the answer depends on what the word is doing.
  **Anything the reader must find, match or click is quoted from the
  screen exactly**: a button label, a field name, a status value, an
  error message. **Descriptive prose uses the formal term**, even when
  the interface uses an abbreviation or a casual one. A size chip
  reading "2 GB RAM" is described as memory, and the reader still finds
  the chip because the chip's own words are quoted where they matter.
  **A table is the hard case, because a header or a cell can be
  either.** A column of values the reader matches against the screen is
  quoted from the screen and left alone, abbreviations included. A
  column the writer wrote to organize the page takes the formal term.
  When you cannot tell which one you are looking at, quote it. A reader
  who has to expand an abbreviation has lost a second, and one who
  cannot find the row has lost the page.
- A setting "sets" or "determines" a value. It does not "fix" one,
  which reads as a bug fix. "Fixed" is not the word for immutable.
- **A time bound says whether it is a wait or a window.** "Up to about
  a minute" reads as both: appears within a minute, or is visible for
  only a minute. Those are opposite instructions. Write "appears within
  about a minute" or "stays for about a minute", never the form that
  carries both.
- "Unknown", never "unmeasured" or "not recorded here". The reader does
  not care what the author got around to.
- **The present tense describes behavior. The past tense is for one
  event the reader has already lived through.** The test is who the
  sentence is about. A troubleshooting entry saying what a message
  means whenever it appears is behavior, so "the payment step cannot
  open a checkout session" is right there. A recovery step pointing at
  something the reader's own earlier run produced is one event, so "the
  backup created when the restore started" keeps its past tense. When
  in doubt the sentence is behavior, because a page describes a
  product and not a session.
- Banned outright: leverage, utilize, ensure, seamless, best-in-class,
  synergy, paradigm shift, stakeholder alignment.

### Constructions that read as a machine

Word lists catch "leverage" and "seamless". They do not catch a shape
repeated until it has a rhythm, and shapes survive across model
generations after the vocabulary tells have gone. Read a draft once
looking only at structure.

- **Negative parallelism.** "No adapter, no driver patch and no extra
  package." Three negations in a row sound authoritative and assert
  something nobody checked: that page's promise was false for JDBC,
  and the page covered no JVM framework, so it never met the case
  that disproved it. **Say what is true, not a list of what is
  absent.**
- **The same skeleton twice running.** Two consecutive sentences or
  paragraphs built on one frame, most often "not X, but Y" or a
  labeling construction reused.
- **Uniform sentence length.** A page where every sentence is the same
  size reads as generated even when each is good. Vary it.
- **Accumulation.** Words that are fine once and a tic at three. Count
  them after drafting: "actually", "critical", "matters", "exactly",
  "rather than", "at scale". More than two of any one on a page is too
  many.

