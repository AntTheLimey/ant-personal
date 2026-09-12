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
faults that no prose rule addresses. Where two rules contradict each
other on one sentence, the order under "When two rules conflict"
decides which wins.

This skill is self-contained. It carries the prose rules, the content
checklist, the settled product vocabulary and the repository mechanics
a writer needs, so there is no second rules file to open and no way for
two documents to drift apart into contradicting each other.

## When two rules conflict

Every rule here is an absolute, and two absolutes can still point
opposite ways on one sentence. Apply them in this order. The higher
rule wins, and the sentence is then written the best way that obeys
it.

1. **Reader safety.** Never print a copyable command that destroys
   data, and never walk a reader into an irreversible or billable
   action without saying so first. On a console page that means a step
   committing the account to a charge, deleting data, or discarding
   entered values says what it costs in the step itself, before the
   control is named. Checklist item 1 asks for every flag a **safe**
   non-interactive run needs, so a command is complete even when the
   flag it lacks is the one that skips a confirmation prompt. The
   destructive-flag rule under Steps and procedures says how to show
   it instead.
2. **The content checklist.** A page that fails an item is wrong
   however well it reads.
3. **Product truth.** Never delete a technical claim unless the same
   claim already stands elsewhere on the page. This outranks the rule
   that sends a number to the page owning it, so link out and keep the
   claim. The one exception is a count of things the reader cannot act
   on from this page, such as "one of five operations that need this
   status": the condition is the claim and it stays, the tally is not
   and it goes. A count nobody acts on is a maintenance liability that
   is wrong the day the sixth case ships. The second exception is the
   same principle widened: a claim the reader cannot act on at all,
   which "Say less, or say nothing" sorts and deletes. Product truth
   protects a fact the reader acts on, not every true sentence. It also
   outranks "keep the consequence, drop the mechanism", which applies
   only where the mechanism is not itself the only statement of a
   behaviour.
4. **House style.** Every other rule in this file. Two house-style
   rules can still collide, so three tie-breaks settle the pairs that
   keep recurring:
   - **The product name beats a heading example and beats link text.**
     A heading counts as an appearance, so a heading carrying the
     edition name carries the full one. Where link text and the product
     name disagree, the name wins and the link text differs from the
     target's title.
   - **A word cap beats the rule against stripping a semicolon.** A
     semicolon joining two independent clauses over the cap is split.
     The no-stripping rule protects a sentence you are not otherwise
     touching.
   - **Anything else: the rule naming the more specific case wins.**
     Where neither is more specific, keep the reader's ability to act
     and note the collision in the pull request.

## The content checklist

Run all seven before writing a sentence, and again before opening a
pull request. Each is a question with a failing answer, not a
preference. Passing all seven is not done: a page passes this list and
still fails a reader who does not already know it, so the cold read
under "Reviews" is the last gate and you run it yourself.

**1. Can the reader do every action exactly as described?** On a
command-line page, a command needs its full prefix, a placeholder for
every value, and every flag a non-interactive run needs; one that
silently assumes a default the reader does not have is unrunnable for
everyone else. On a console page, every control is quoted exactly as it
renders, and the page says where the screen is and what puts the reader
on it.

The connection flag (`--base-url` or `--profile`) is the exception, and
it is stated **once** per page, in a "Before You Start" section near
the top that names the flag and the command that sets it in a profile.
Repeating it on every block is noise that goes stale. A page with no
such section fails this item even when every command is otherwise
complete.

A console page needs the same section for a different reason. It has
no connection flag, so instead it names what the reader must have
before starting, the screen each value comes from, and the screen the
first step begins on. A console page that drops the reader into step
one with no route to that screen fails this item exactly as a
command-line page with no profile section does.

**1b. What will the reader do instead of the step you wrote?** Name
the shortcut that works right now and say what it costs. A step that
prevents an unrecoverable loss fails this item unless the page refuses
the instinctive alternative by name. "Connect over TLS" fails it too,
for a smaller reason: it names no command, so the reader invents one.

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

A note is any block that could be lifted out without changing a single
thing the reader does. That includes an indented paragraph under a list
item, an admonition and a parenthetical aside, whether or not the word
"note" appears. Reading only the blocks labelled NOTE is how this item
gets passed by mistake.

**The test is whether removing it changes an action, not whether it is
indented.** An indented paragraph that explains the step it sits under,
names the flag that changes what the reader types, or gives the limit
the result must fall inside, is part of that step and stays there. A
step is allowed to be more than one line.

## Sentences

- A step is 20 words at most. Descriptive prose is 25 words at most.
  The extra five words in prose exist to pay for a "because", and
  spending them on one is the point of the split.
- Count words the way STE counts them, or no step holding a real command
  can ever fit: backticked or quoted text counts as one word however
  long it runs, a number counts as one, a number with its unit counts as
  one, an abbreviation counts as one, a hyphenated word counts as one,
  and text in parentheses counts as one. The caps apply **per sentence**,
  not per step or per paragraph, and they apply to every sentence a
  reader reads: a bullet, an indented paragraph under a step and a
  lead-in are all prose. Two things are exempt: a table cell, which is
  not a sentence, and image alt text.
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
- **A quoted product string is reproduced exactly and is exempt from
  every rule in this skill**, this file and every file beside it,
  including the banned words in `product-vocabulary.md`. Button labels,
  error messages, field names and status values are quoted so the
  reader can match them against the screen, so a contraction, an
  em-dash, a capital or a banned word inside one stays. A dialog really
  named `Taking Pre-Restore Snapshot` is quoted with its snapshot
  intact, and your own prose around it still uses the settled word.
  Quote it or paraphrase it outside quotation marks. Never correct it.

## Steps and procedures

- Write a step in the imperative. Not "the test can be continued", but
  "continue the test".
- Do not put "must" in front of an imperative unless the instruction
  guards against data loss or an unrecoverable state.
- A note gives information and never an instruction. An imperative in a
  note has turned that note into a step, so make it one.
- A limit, a tolerance or the expected result of a step goes in the
  step, immediately after the action, never in a note beside it.
- **A step whose point is not obvious carries its reason, in the step.**
  A reader skips what looks like ceremony. "Record the current time"
  reads as ceremony, and the sentence that makes it essential, that
  nothing else identifies the backup taken before a restore, is worth
  nothing to a reader who has already skipped the step. Where skipping
  a step is unrecoverable, the reason goes in the step and nowhere
  else. A cold reader who skips a step you thought was obvious has
  found a defect in the step, not in the reader.
- Numbered lists are for sequences only. If the steps work in any
  order, they are bullets. Number the steps in sequence, `1.` then `2.`
  then `3.`, rather than repeating `1.` and letting the renderer count.
  Indent everything belonging to a step by four spaces.
- **Every precondition goes in Before You Start, all of them.** A
  condition that makes the task fail is a precondition wherever you
  discovered it, so a reader who meets the list has met the whole list.
  A condition left in a later section is one the reader reaches after
  the failure it predicts.
- **Do not print a destructive flag in a copyable command.** Show the
  command as it runs interactively, with the prompt intact, and describe
  the flag that skips the prompt in the step beside it. A reader
  following the page at a terminal should have to type the flag that
  removes their confirmation prompt. The scripted form belongs on the
  automation page, not here.
- **A step that tells the reader to become someone else gives them the
  means, in that step.** "Connect as the role manager" is unusable
  until the reader has a host, a port and a database name, and a step
  that withholds those sends them back to the session they already
  have, which is the one the step exists to get them out of. A
  prerequisite of a step is part of that step, not of the step after
  it.
- A step that needs a table gets the table in its own section, and the
  step links to it. A table nested inside a list item is fragile to
  render and hard to read.

## Marking a step the reader will otherwise skip

A hazard is written in the same voice as the rest of the page. The
register does not harden because the stakes rose, and a page that
starts issuing orders reads as though it does not trust the reader,
who is a professional doing their job. **What makes a warning land is
the fact it carries, not the force of the telling.**

The strongest sentence a hazard can carry is what silently goes wrong:
"`ALTER ROLE app PASSWORD` runs without error, so nothing warns you"
does the whole job. A cold reader singled that out as the one warning
that changed their behaviour, and it commands nothing.

**State the consequence, then stop.** Do not follow it with an
imperative that repeats it. "Rotating a built-in password before the
role manager exists costs you control of every role `admin` created"
is finished. Appending "Do not rotate a built-in password until the
role manager exists" adds no fact, and turns an explanation into an
order. One or the other, and the consequence is the one that teaches.

**Ration this.** The treatment below is expensive, in the reader's
attention and in the length of the page, and it works because it is
rare. A page with six marked hazards has none: the reader learns that
the marking means nothing and skims all six. **One or two per page, for
outcomes that are genuinely unrecoverable.** Everything else is a
clause inside the step, or is left out.

The test is not "could this go wrong". It is "can they undo it". A
mistake the reader can repeat, reverse or retry needs no marking at
all, however annoying. A permanent loss of data, access or control
gets the full treatment, and almost nothing else does.

A step that prevents an unrecoverable outcome needs three things, and
it needs all three:

1. **The consequence, in the step**, stated as what the reader loses
   and when they find out. Not "this keeps control of your roles", but
   "at the next reconcile every role you created becomes permanently
   unalterable, with no recovery".
2. **The shortcut the reader would otherwise take, and its cost.** A
   reader already connected as an administrator will do the thing that
   works right now. Describe that path and what it costs them, in the
   third person: "a role created as `admin` is the one a reconcile
   orphans". Not "this is the mistake this step prevents", which
   scolds a reader who has not made it yet.
   **Name the action and its object in full.** A sentence about
   "creating the role as `admin`", printed under a step that
   legitimately creates a role as `admin`, reads as the page
   contradicting what it just instructed. A cold reader hit exactly
   that and could not tell which role was meant.
3. **Its own line, so the eye catches it.** A hazard buried mid
   paragraph is skimmed. Where the repository renders admonitions, use
   one. Otherwise give it a short line of its own, opening with what is
   lost. Separation is what earns the attention, not capitals, not
   bold, and not a raised voice.

**Every irreversible action the reader can reach before its guard
belongs in Before You Start, by name.** Listing one is worse than
listing none, because a reader who finds one hazard named reads the
silence about the others as permission. Write these as conditions
rather than commands: "two things cost you control of a role, and both
are easy to do before you reach step 2". Ask which actions a reader
could take in the minutes before they reach the protective step, and
name each of them there. A cold reader created a role as `admin`
within five minutes, against a page whose Before You Start named only
the rotation.

**Ask what the reader will do instead of this step, and answer that.**
The instinct beats the instruction every time it is not named. The
three instincts a cold read found on one page were to rotate the
supplied credentials as hygiene, to use the SQL statement rather than
the command, and to create the test objects as the role already
connected. All three succeed, none errors, and every one breaks
something silently.

**A warning goes where the instinct fires, not where the topic lives.**
The rule that changing a password in SQL desynchronises the platform's
stored copy belongs beside the first mention of a password, not in the
section about passwords at the foot of the page. A reader meets the
temptation long before they meet the section that owns it. Where the
warning belongs in two places, write it in both: this is the one case
that outranks "state a caveat once per section".

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
  column the writer wrote to organise the page takes the formal term.
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
- **The present tense describes behaviour. The past tense is for one
  event the reader has already lived through.** The test is who the
  sentence is about. A troubleshooting entry saying what a message
  means whenever it appears is behaviour, so "the payment step cannot
  open a checkout session" is right there. A recovery step pointing at
  something the reader's own earlier run produced is one event, so "the
  backup created when the restore started" keeps its past tense. When
  in doubt the sentence is behaviour, because a page describes a
  product and not a session.
- Banned outright: leverage, utilize, ensure, seamless, best-in-class,
  synergy, paradigm shift, stakeholder alignment.

## Punctuation

- No em-dashes. Use a comma, a period or parentheses.
- No semicolons in new text. Write two sentences. Never strip a
  semicolon out of text that already exists, because a punctuation-only
  edit hides the technical change underneath it in review.
- Do not start a sentence with And, But, So, Or or Yet. "And" is almost
  always deletable, because a following sentence adding to the previous
  one is the default reading anyway. "So" becomes "Thus" or "As a
  result". "But" becomes "However,", which reads as stiff beside a blog
  and correct beside the semi-formal register these pages are written
  in.
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

**A structural lead-in is not signposting.** The sentence introducing a
list, a table or the opening's section index is required by the format
rules and is exempt from this section. Keep it to one clause that names
what the list holds, ending in a colon: "This page has four sections:"
is fine. What stays banned is the sentence that tells the reader how to
feel about what follows, or restates the heading it sits under.

No forward-looking text. Not "yet", "coming", "planned", "soon", or
"today" used as a temporal hedge. Describe what is.

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
  behaviour?** Where the answer is no, say so on the artifact, so that
  an unmeasured claim is visible rather than silently absorbed.
- **Where are the measurements?** A measurement recorded outside the
  probe-log directory is a measurement lost. If probe logs exist, get
  their path; if a measurement was taken and never written down, say
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

## The shape of the page

### Ask which job this is before you start

Three jobs wear the same words, and they produce different pull
requests. Decide which one you are doing, and where the request does
not say, **ask the person who asked you** before writing anything.

- A **fix** changes a fact and touches nothing else. No restructuring,
  no style edits, no vocabulary sweep. A reviewer must be able to see
  the factual change on its own.
- An **edit** improves the prose inside the structure the page has.
  Sentences, words, headings and formatting are in scope. The order of
  the sections is not.
- An **overhaul** rewrites the page, its shape included.

The request usually names the job: "correct the timing claim" is a fix,
"bring this page into style" is an edit, "rewrite this page" is an
overhaul. Where it does not, ask. Guessing overhaul on a page someone
wanted corrected buries a one-line change in a diff nobody can review,
and guessing edit on a page someone wanted rebuilt returns the same
badly organised page with better sentences.

The rest of this section is for an overhaul.

### The reader wants the least that works

A customer opens this page to do one thing and leave. They are not
reading the product, they are getting past it. **An overhaul that
returns a longer page has usually failed**, whatever else it fixed,
because the reader now hunts for the same instruction through more
text.

Measure it. Where the rewrite is longer than the source, name what the
extra words bought: a missing step, a hazard, a definition the reader
could not do without. Length that bought nothing comes out. The
commonest sources of it are a warning restated as a command, a
mechanism explained where a consequence would do, and a caveat written
three times because it felt important each time.

### Deciding the order

**Fixing the sentences of a badly organised page produces a badly
organised page with better sentences.** In an overhaul the order of the
sections is part of the work, not the part you inherit. Decide the
shape before you write a word, and expect to move, merge, split or drop
a section.

Order a page by what the reader is doing, in the order they do it:

1. What this page gets them, in one sentence.
2. What they need before starting.
3. The task itself, in the order it happens.
4. The things that go wrong, after the thing that goes right.
5. Where to go next.

Reference material the task leans on goes into its own section, placed
after the first step that needs it. A conceptual model the reader must
hold before step one goes into the opening as terms, one sentence each,
never as a section of its own at the top of the page.

**The commonest defect is a page ordered by the product's internals.**
It opens with a taxonomy of what exists, explains the model, and
reaches the reader's task somewhere in the middle. Read the source
page and ask what the reader came to do. If the answer appears below
the halfway mark, the page is upside down and reordering it is the
main work.

Two orderings are wrong however good the prose:

- A destructive action printed before the step that makes it
  survivable. Reader safety, rank 1.
- A definition placed after the sentence that leans on it. Checklist
  item 4.

Where the source's order is already the reader's order, keep it. Say
in the pull request that you checked, so a reviewer knows the shape
was a decision rather than an inheritance.

**Placing a step first does not stop a reader skipping it.** A cold
reader given a page whose first procedure existed solely to prevent an
unrecoverable loss said they would have skipped it, because it read as
an optional convenience layer and nothing on the page was formatted as
a stop sign. Order is necessary and it is not sufficient. See "Marking
a step the reader will otherwise skip".

**One ordering defect is worth fixing even in a fix or an edit**: a
destructive action printed before the step that makes it survivable.
That is reader safety, rank 1, and it outranks the scope of the job.
Move it, and say in the pull request why the diff is larger than the
request.

## How a page opens

Every page opens with a sentence. A gerund or a noun phrase standing in
for one is a fragment however long it runs, and twenty-six guides opened
that way before anyone noticed. This applies to the first sentence of
the body, never to the heading above it, which is a different rule
entirely and is given below.

The opening gets a new reader ready before it teaches anything:

- What the page does, or what has gone wrong.
- A linked index of the sections, when there are more than three. It
  lists **every** heading on the page, navigational ones included. A
  cold reader who counts eight headings under a sentence promising five
  starts wondering what else was dropped. Navigational headings do not
  count toward the threshold that triggers the index, and they do
  appear in it once it exists.
- The three or four terms the page leans on, one sentence each.
- Which commands change something.
- What to collect before starting, and the command or screen that
  produces each value.

Say what the reader can do before what the product cannot. A page that
opens with five things the product does not do has told the reader
nothing they can act on.

Headings are gerund phrases in title case: "Backing up and Restoring a
pgEdge Starfleet Managed Database", "Understanding a Backup",
"Rotating a Credential". The first of those carries the full edition
name because a heading counts as the name's first appearance.
The exception is a conventional navigational heading, which is a fixed
label the reader scans for rather than a description: "Next Steps",
"Troubleshooting", "Before You Start", "Prerequisites". Those keep
their standard wording, and they do not count toward the number of
sections that triggers a linked index in the opening. They are listed
in that index once it exists, because an index that does not match the
page reads as an out-of-date page.

**The noun a customer would search for goes inside the gerund phrase.**
"Comparing the Database Sizes" contains "database sizes" and is
findable. "Making Your Choice" contains nothing and is not. If the
gerund is hiding the searchable noun, the heading is wrong, not the
rule.
This is the house form, it is what the existing pages use, and an
imperative heading is the common way to break it. Name what the section
contains, in words a customer would search for. Never a sentence, never
a question with no answer, never a judgement, and never a dash carrying
a second clause.

A run of steps is a numbered list, not a run of headings. Promoting each
step to its own heading fills the navigation pane with fragments and
loses the sequence. Indent anything belonging to a step by four
spaces.

That four-space rule is for a numbered step. A bullet is different: an
indented block under a bullet reads as a note, and the checklist counts
it as one. So a bullet that needs a second sentence keeps it in the
same paragraph.

A bullet that needs more than prose is usually a step wearing the wrong
clothes, and the answer is to make it one. The exception is a lookup:
a list of symptoms, error messages or states the reader scans to find
their own case. Those are not a sequence and must not be numbered. Give
each entry its own `###` heading instead, so the block belongs to a
heading rather than to a bullet.

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
- Alt text describes what the image shows, as a noun phrase. It is
  exempt from the sentence rules and the word caps, because it is not a
  sentence. It never carries a fact found nowhere else on the page: a
  reader who cannot see the image must still be able to finish.
- A placeholder is lowercase and hyphenated inside angle brackets,
  `<db-id>` and `<backup-id>`. Never use the underscored form of a real
  field name, which build gates read as a claim that the field exists.
- An image sits inside the step or under the heading it illustrates,
  indented to match. An image does not satisfy the rule that a heading
  is followed by a sentence: write the sentence, then place the image.
- Link text is the target page's own title. A link whose text has
  drifted from the heading it points at is the same defect as a stale
  cross-reference.
- A page's navigation label matches its `#` heading, or is a shortened
  form of it that keeps the gerund. Two names for one page is how a
  reader loses it. A navigation entry that disagrees with a converted
  page is unconverted work, not a reason to leave the heading alone:
  change the navigation file in the same pull request.
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
  from a preference. This is the fix job under "The shape of the
  page", and it is why the three jobs are worth separating before you
  start rather than after.

## No internal history, and no internal names

A page carries no trace of how it was made or who made it.

- No issue or pull-request numbers, no ticket ids, no commit hashes, no
  dates, no "measured on", no attempt counts, no tenant, profile,
  fixture or colleague names, no internal service names, no source-code
  symbols, and no build or test names offered as proof of a claim.
  Write "the platform" or "the API".
- No archaeology. "Previously", "used to", "an earlier version", "we
  decided", "shipped in", "since version N", "as of". State current
  behaviour in the present tense with no citation.
- A statement of current state is not history. "The repository is
  internal" stays true until it is not, and stays in the text.
- **Evidence lives outside the page**, in the pull request. Never leave
  an HTML comment carrying a source in a page a customer reads.
- **Never name a competitor or another vendor's database service.**
  Third-party tools the reader actually uses, such as psql, pgAdmin, an
  ORM or an IDE, are fine. A page describing a migration may name the
  service it migrates from, on that page only.
- A changelog entry describes the product, never the work. What the
  reader gets, never what was swept, counted or removed.

## Never invent

- Every command and flag exists in the generated reference. Every
  behavioural claim traces to a live capture, a spec field, the
  product's own source, or an existing gated page. A claim with no
  source stays out, and what is true goes in its place.
- **Keep the consequence, drop the mechanism.** The reader is told what
  they can do and see, never how the platform does it. "Rotating the
  credential for the app role restarts AI services" is the right weight.
  Not the container, not the startup sequence, not which process read
  what.
- **No list of cases that will age.** "A restore, resize, service change
  or credential rotation" becomes "a modification". A list like that is
  wrong the day the fifth case ships.
- **No scope creep.** A field, a badge or a section explains itself and
  not a neighbouring feature. Sizing rules belong in the resize flow,
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
- **When a kept image contradicts the verified prose, the prose is
  right.** Write what the source says, flag the image for recapture in
  the pull request, and say nothing on the page about the discrepancy.
  Never write prose backwards to match a stale screenshot.
- **A screenshot is not a source.** It is evidence that something
  appeared on screen once, and it goes stale silently. A value that
  exists only at runtime, such as a price the console fetches from a
  billing service, may still be stated: attribute it to what the console
  shows, never present it as a contract, and re-check it whenever the
  page is touched.
- **A rewrite may add facts, and often must.** The content checklist
  asks for things a page frequently does not have, and the answer is to
  go and find them rather than to leave the item failing. Source every
  addition and say where it came from in the pull request. What a
  rewrite may never do is add a fact it did not verify.
- **A rewrite may add a step**, when the checklist requires one and the
  step follows from a fact that is sourced. A procedure that identifies
  something by when it happened needs a step telling the reader to
  record that, or the identification is unusable. Say in the pull
  request which fact the step follows from.
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

## Say less, or say nothing

Every sentence sorts into one of two outcomes, and the sort happens
before any rewording.

**Would the reader act wrong without this fact?**

- **No. Delete the sentence.** Not shorten it. It is true and it is
  gone.
- **Yes. Keep the fact and cut everything propping it up.** One
  sentence, naming what the product does and what the reader sees.

### Sorting to delete

- **They would have assumed it.** People assume an API validates its
  own values, that a command they cannot find does not exist, that a
  resource is not usable before it is ready. Confirming an assumption
  spends attention and returns nothing.
- **It is a reason for behaviour the page already states.**
- **The page already carries it.**

### Sorting to rewrite

The fact stays. Everything holding it up goes.

- **The product is the subject, never the documentation.** "byoc
  publishes no version enum, so `--pg-version 99` is the API's to
  refuse" becomes "The API refuses unavailable pg versions."
- **State what the reader sees, not what causes it.** "A database still
  being created has no host yet, and the command exits 1" becomes "The
  CLI exits 1 until the database finishes creating."
- **Cut the "so" clause.** A sentence that explains itself is two
  sentences, and the second is usually the one to drop.
- One sentence. Then stop.

### An absence

"The API publishes no list of values for status". "This CLI has no
command that deletes a backup". "backup create has no --wait, and
neither has backup get". "There is no cluster to build, no nodes to
place and no cloud account to attach".

These sort to delete: nobody was looking for the thing. They also
cannot be checked by anything, so they rot one feature at a time while
every gate stays green.

Where a reader would genuinely reach for the missing thing, the
replacement says what to do instead, never what is missing more
briefly.

A section built entirely of negatives, "what this does not offer", is
the same failure at section scale.

## In-app copy

Tooltips, help icons, confirm dialogs and empty states are documentation
too, written to a tighter budget.

- **Define the thing the copy sits on, in plain words, and stop.** One
  sentence is the norm and two is the ceiling. "Active database
  connections out of maximum allotted" is the model answer.
- **If the label already says it, write nothing.** A badge reading
  "Running" needs no tooltip explaining that it is running. "None" is a
  valid answer. The test: does the text say something the label and the
  value do not.
- **No timing or transition claims.** Not "about ten seconds", not "the
  old password may still work". The status change is the signal. A docs
  page may give a duration where the reader needs one to act. In-app
  copy never does.
- **A failed state names the one action available.** Nothing about
  bookkeeping.
- **A confirm dialog states the action and the one consequence the user
  must know.** Not the timing, not what reads what at startup.
- **When one sentence is not enough, keep the one sentence and link.**
  The link goes to the page that owns the detail.
- Buttons carry no hover tooltip. The explanation sits in a help icon
  beside the control. An icon-only button keeps its short hover label,
  which is its accessible name and not an explanation.

## Repository mechanics

- **Never edit inside a generated block.** Change the command or the
  source the block is generated from, then regenerate. Text typed
  between generated markers is overwritten.
- A new page gets its navigation entry and its changelog entry in the
  same change that adds it.
- Run the documentation gates before opening a pull request: the test
  suite, the prose linter, and the reference drift check.

## Two artifacts, and the old page is not one of them

A **fact set** is discovered from source: the generated reference, the
product's own code, the vendored specs, the probe logs. It feeds
shaping and writing, and it exists on every job including one with no
old page at all.

A **ledger** is extracted from the page you are replacing. It is a
record of what that page covered. It is never a record of what is
true.

Different provenance, different trust. Keep them apart, and never let
an entry cross from one to the other without being settled against
source first.

### The writer never reads the old page

Not once, not for reference, not to check a heading. Read the ledger
instead. A writer that has read the page reproduces its phrasing from
memory without meaning to, and its ordering along with it.

Name the excluded file as a path to filter out of every glob, not
only as a file not to open. `docs/managed/*.md` contains it and so
does any recursive grep. A prohibition on opening a file does not
survive a wildcard: two writers in one run were exposed exactly that
way.

### Entry form

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

Group by topic, then sort alphabetically — headings, and entries
within each heading. Number from F1 in the sorted order. Ordering
leaks separately from phrasing, so a ledger in page order hands the
writer the page's structure back.

Tell the writer in as many words that the order carries no editorial
judgement and must not be followed.

### The gates, and when each runs

Run all three before calling a page done, and report the numbers.

    ./check-sources.py <ledger>

After the ledger is built, before the writer sees it. Fails a `V`
entry that cites only a hand-written page.

    ./check-ledger.py <old page> <new page>
    ./check-ledger.py <ledger> <new page>

After the draft exists, at `--n 5` and again at `--n 4`. The first
catches phrasing that reached the page through the ledger. The second
catches phrasing invented in the brief, which is a channel nobody was
measuring until a finished page shared eleven sequences with its own
brief.

A shared sequence is re-expressed, never padded around. A phrase that
is vocabulary already shipped in a sibling page stays: consistency
beats novelty there.

    ./signals.py <new page>

See "Reading signals".

**Counts are signals, not scores.**

## Reviews

Every documentation change gets two reviews and one fix round. Both are
performed by someone other than the writer, after the draft exists. A
writer cannot be their own cold reader, because you cannot un-know the
page you just wrote.

**Run the cold read yourself before calling the page done.** Do not
hand it back as a recommendation and do not wait to be asked. Dispatch
a fresh agent that has none of your context and give it the page and
nothing else.

The correctness reviewer checks every claim against its source. The
writer supplies a claim-to-source list so the reviewer verifies claims
rather than rediscovering them.

The cold-read reviewer gets no repository context at all, only the page
and the pages it links to. They read as the customer and report where
they got lost, what they could not type, and what they would search the
web for instead.

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

The two find different defects and neither finds the other's. Run both,
even on a small change.

**The cold read is the only gate that catches an ordering defect**, and
that is why it is not optional. Every rule in this file is applied by
someone who already knows what the page is for, so a step whose reason
sits sixty lines below it, or a precondition parked after the failure
it predicts, passes the checklist and passes the prose rules. Only a
reader with no context skips the step and tells you they skipped it.

Ask the cold reader for what they had to guess and what they would have
done wrong, not for whether the page reads well. A page can read well
and still be executed in the wrong order.

### The cold-read dispatch

Give the agent the page's path and nothing else. No repository access,
no web search, no skill files, no explanation of the product. Tell it:

> You are a cold reader. You have never seen this product. Read only
> this file. Whatever it does not tell you, you do not know. You are a
> competent engineer handed this page and told to do what it describes.
> Report: could you complete the task, and if not, the first sentence
> at which you were stuck. Every place you had to guess, quoting the
> sentence and naming the readings. Every question the page raises and
> does not answer. Anything you would have done wrong, and what the
> consequence would have been. What the page does well. Judge only what
> is on the page. If you find yourself reasoning "it presumably works
> like X", record that as a guess instead.

The fourth answer is the one that matters. "I would have skipped that
step because it reads as ceremony" is a defect report, and no other
review produces it.

**Fix what it found, then say what it found.** A cold read reported and
not acted on is worse than none, because the page now ships with the
defect and a record that you knew.

## Further reading

- [ste-adoption.md](ste-adoption.md) records which ASD-STE100 rules
  this style takes, adapts or drops, and why. Read it when a rule here
  looks arbitrary.
- [agent-pages.md](agent-pages.md) carries the divergences for pages
  read by agents rather than people: the CLI's embedded `llms` pages
  and the shipped skills.
- [product-vocabulary.md](product-vocabulary.md) carries the settled
  product wording: how backups are described, what Managed does and
  does not offer, and the boundary between the Cloud and Enterprise
  stories.
