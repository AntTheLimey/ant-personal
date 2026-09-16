# Writing

The prose rules every job loads: sentences, steps, hazards,
descriptive prose, punctuation, signposting, format and repository
mechanics.

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
- The quoted-product-string exemption is in style-standard.md, under
  "Words".

**Checking the caps.** `<skill>/signals.py` reports one number for the
caps: how many prose sentences run past 25 words. That is not the STE
counting above: a backticked span counts as nothing, and text in
parentheses counts word by word. The script never measures the 20-word
step cap, so read the steps for that one. Where the number is not zero,
find the sentences by reading. The script strips code, tables and
headings before it counts, so read that same prose and nothing else. A
page with more than a handful over the cap has a structural problem
rather than a sentence problem. That count is a signal rather than a
bound, and sets no exit status. Only the two bounds below do.

## Reading signals

Run `<skill>/signals.py <page>` before finishing and report what it
says. It measures prose only: fenced code, indented blocks, tables and
headings are stripped first, because a docs page is mostly not prose
and counting the commands makes the number meaningless. After the
numbers it prints a verdict line per bound, naming the bound and the
value it measured, and exits non-zero where one is crossed.

**Reading ease has a floor of 58.** Everything overhauled through this
skill sits at 61 to 62 without anyone aiming for it. Everything
nobody has touched sits below the band. The floor catches the page
that is drifting, not the page that is trying.

**Flesch-Kincaid grade has a ceiling of 8.0.** On pages like these the
vocabulary is fixed by the product and syllable density barely moves,
so the grade is close to a restatement of mean sentence length: 8.0
means a mean sentence of about 13 to 15 words.

**The ceiling is a target for the prose and never a license to drop a
clause.** The cheap way to a short sentence is to cut the clause
carrying the condition, and that makes a worse page than missing the
ceiling by a grade. Where a fact needs a long sentence, split the
sentence, not the fact.

**Watch the connectives.** Measured cost of reaching the ceiling,
on the one page where it was tested: two places where "because" had
been cut and the reader had to reconstruct why one sentence followed
from the other. A sentence pair that leans on an unstated causal link
is a sentence pair that should have kept its connective and paid the
grade.

The pipeline reaches about grade 8 on its own. Treat the ceiling as a
tripwire that catches the page that did not, rather than as the thing
that makes a page readable.

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
- **Before You Start, or Prerequisites under its other sanctioned
  name, holds what is specific to THIS page and nothing else.** Only
  four kinds of entry earn a place: a value the reader must
  have in hand before step one, with the command or screen that
  produces it; a condition specific to this task that makes it fail;
  an irreversible action reachable before its guard; and, on a console
  page, the screen step one begins on and the route to it. The database
  ID being restored and the backup ID being restored from are entries.
  An authenticated profile, a supported shell, a network connection and
  an account are not, because they are true of every page and a reader
  who lacked one would not be here. **If nothing page-specific
  survives, the page carries no Before You Start section.** An empty
  section that exists to match the other pages costs the reader the
  attention it takes to read and teaches them the heading is skippable
  on the page where it matters.
- **A page-specific precondition goes in that section wherever you
  discovered it**, so a reader who meets the list has met every
  condition this page can predict. A condition left in a later section
  is one the reader reaches after the failure it predicts.
- **A step whose command changes something says so in that step.** The
  reader needs it where they are about to act, not in an opening
  paragraph they read four minutes earlier. Say what changes, in the
  same sentence that gives the command. Where the change cannot be
  undone, "Marking a step the reader will otherwise skip" applies on
  top of this.
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
that changed their behavior, and it commands nothing.

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

**On a restyle or a restructure, this rule reaches only a hazard
already stated somewhere on the page.** On a restyle, moving it into
Before You Start is the one ordering exception the job allows, named
in the hand-back. On a restructure, moving it is ordinary reordering.
Neither job invents a hazard with no existing statement on the page:
that is reported in the hand-back as a gap, with this rule as the
reason.

**Ask what the reader will do instead of this step, and answer that.**
The instinct beats the instruction every time it is not named. The
three instincts a cold read found on one page were to rotate the
supplied credentials as hygiene, to use the SQL statement rather than
the command, and to create the test objects as the role already
connected. All three succeed, none errors, and every one breaks
something silently.

**A warning goes where the instinct fires, not where the topic lives.**
The rule that changing a password in SQL desynchronizes the platform's
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

## Punctuation

- No em-dashes. Use a comma, a period or parentheses.
- No semicolons in new text. Write two sentences. Never strip a
  semicolon out of text that already exists, because a punctuation-only
  edit hides the technical change underneath it in review.
- Do not start a sentence with And, But, So, Or or Yet. "And" is almost
  always deletable, because a following sentence adding to the previous
  one is the default reading anyway. "So" becomes "Thus" or "As a
  result". "But" becomes "However,", which reads as stiff beside a blog
  and correct beside the formal register these pages are written in.
- Use a hyphen for a compound modifier before a noun: read-only role,
  copy-on-write branch, single-node database.

## No signposting

A sentence that carries no information, and only points at
information, is slower than the thing it points at. Delete it.

Delete on sight: "this section covers", "this page covers", "this page
uses", "this page has", "now that we have", "it is worth noting",
"importantly", "crucially", "pay special attention", "the catch is",
"note that", "worth knowing", "and this is why it bites". State the
fact and stop.

A lead-in sentence carries a fact. It never restates the heading above
it.

**A structural lead-in is not signposting.** The sentence introducing a
list or a table is required by the format rules and is exempt from this
section. Keep it to one clause that names what the list holds, ending
in a colon: "A restore needs three values:" is fine. What stays banned
is the sentence that tells the reader how to feel about what follows,
restates the heading it sits under, or makes the page its own subject.

No forward-looking text. Not "yet", "coming", "planned", "soon", or
"today" used as a temporal hedge. Describe what is.

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
  never composed by hand and never tidied up afterward. This rule is
  about output blocks. It says nothing about screenshots, which are a
  product decision and not a style one.

**A README is a page.** The sentence rules, the word rules and the
79-character wrap all apply. What does not apply is the page-opening
shape: a README opens with what the thing is and how to install it,
not with what the reader will be able to do. It is also the one page
that may carry a linked index of its own sections, and only when it
runs past a screen, because GitHub renders it with no navigation pane.

## Editing text that already exists

- Keep the fact, drop the archaeology. "Since #448, --interval is a
  lookback" becomes "--interval is a lookback."
- Never delete a technical claim unless the same claim already stands
  elsewhere on the page. A history sentence often carries the only
  statement of a current behavior.
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
  from a preference. This is the difference between a fix and a
  restyle under "The shape of the page" in shape.md, and it is why the
  jobs are worth separating before you start rather than after.

## No internal history, and no internal names

A page carries no trace of how it was made or who made it.

- No issue or pull-request numbers, no ticket ids, no commit hashes, no
  dates, no "measured on", no attempt counts, no tenant, profile,
  fixture or colleague names, no internal service names, no source-code
  symbols, and no build or test names offered as proof of a claim.
  Write "the platform" or "the API".
- No archaeology. "Previously", "used to", "an earlier version", "we
  decided", "shipped in", "since version N", "as of". State current
  behavior in the present tense with no citation.
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

## Say less, or say nothing

Every sentence sorts into one of two outcomes, and the sort happens
before any rewording.

**On a restyle or a restructure, only a restatement sorts to delete.**
The writer may delete a sentence where the same fact still stands
elsewhere on the page. A fact whose only statement on the page looks
safe to cut is not deleted: neither job re-verifies what the reader
needs, and the meaning check reports any other drop as a defect. Leave
it in, and list it in the hand-back as a deletion candidate.

On a fix, an overhaul and a new page, sort every sentence by this
question:

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
- **It is a reason for behavior the page already states.**
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

## Repository mechanics

- **Never edit inside a generated block.** Change the command or the
  source the block is generated from, then regenerate. Text typed
  between generated markers is overwritten.
- A new page gets its navigation entry and its changelog entry in the
  same change that adds it.
- Run the documentation gates before opening a pull request: the test
  suite, the prose linter, and the reference drift check.

Guides live under `docs/` in a directory per edition, and a page whose
commands name one edition belongs in that edition's directory rather
than at the root. Root-level markdown is UPPERCASE. Everything under
`docs/` is lowercase. Add the nav entry in the same change as the
page, never after.

**Every link is checked before the page ships.** A cross-reference to
a page that moved is a defect of the same rank as a wrong fact,
because the reader ends up somewhere that no longer answers them. Link
by relative path, use the target's own title as the link text, and
open the target to confirm it says what you are sending the reader
there for.

