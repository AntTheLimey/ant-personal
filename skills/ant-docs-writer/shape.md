## The content checklist

Run all seven before writing a sentence, and again before opening a
pull request. Each is a question with a failing answer, not a
preference. Passing all seven is not done: a page passes this list and
still fails a reader who does not already know it, so the checks under
"Reviews" are the last gate and you dispatch them yourself.

**On a restyle or a restructure, an item that fails for want of a fact
is not fixed by adding one.** Report it in the hand-back instead, with
its number, under the job-scope rule in "When two rules conflict".
Item 6 is the case this comes up most: a restructure may build the
missing save-first step only from a fact already on the page, never a
new one.

**1. Can the reader do every action exactly as described?** On a
command-line page, a command needs its full prefix, a placeholder for
every value, and every flag a non-interactive run needs; one that
silently assumes a default the reader does not have is unrunnable for
everyone else. On a console page, every control is quoted exactly as it
renders, and the page says where the screen is and what puts the reader
on it.

The connection flag (`--base-url` or `--profile`) is the exception, and
it is **assumed, not stated**. A reader who has no authenticated
profile cannot have reached a page about restoring their database, so
telling them to log in spends attention on the one prerequisite every
reader already met. The page that sets the profile up states it; every
other page is silent about it.

**The exception is a command that destroys something.** There the flag
answers a different question: not whether the reader is authenticated
but **which tenant the command runs against**, and a reader holding a
profile per environment can drop the wrong database from a command that
reads correctly. A destructive step prints the flag in the step itself.
This is reader safety, so it outranks the silence above.

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
"note" appears. Reading only the blocks labeled NOTE is how this item
gets passed by mistake.

**The test is whether removing it changes an action, not whether it is
indented.** An indented paragraph that explains the step it sits under,
names the flag that changes what the reader types, or gives the limit
the result must fall inside, is part of that step and stays there. A
step is allowed to be more than one line.

## The shape of the page

### The reader wants the least that works

A customer opens this page to do one thing and leave. They are not
reading the product, they are getting past it. **An overhaul that
returns a longer page has usually failed**, whatever else it fixed,
because the reader now hunts for the same instruction through more
text.

Measure it. `wc -c` on the old page and on the draft gives the
comparison without opening either, and a byte count is not a reading.
Where the draft is longer, name what the extra bytes bought: a missing
step, a hazard, a definition the reader could not do without. Length
that bought nothing comes out. The commonest sources of it are a
warning restated as a command, a mechanism explained where a
consequence would do, and a caveat written three times because it felt
important each time.

### Deciding the order

This section governs a restructure, an overhaul and a new page. On a
restyle the section order does not change, apart from the one ordering
move named under restyle in "Ask which job this is before you start".

**Fixing the sentences of a badly organized page produces a badly
organized page with better sentences.** In a restructure or an
overhaul the order of the sections is part of the work, not the part
you inherit. Decide the shape before you write a word, and expect to
move, merge, split or drop a section.

Order a page by what the reader is doing, in the order they do it:

1. What this page gets them, in one sentence.
2. What they need before starting.
3. The task itself, in the order it happens.
4. The things that go wrong, after the thing that goes right.
5. Where to go next.

**A troubleshooting entry is three things in one order**: what the
reader sees, what causes it, what to do. Name the entry for what they
saw, not for the cause, because the symptom is all they have when they
arrive. One `###` per entry so each is linkable.

Reference material the task leans on goes into its own section, placed
after the first step that needs it. A conceptual model the reader must
hold before step one goes into the opening as terms, one sentence each,
never as a section of its own at the top of the page.

**The commonest defect is a page ordered by the product's internals.**
It opens with a taxonomy of what exists, explains the model, and
reaches the reader's task somewhere in the middle. Ask what the reader
came to do, and find it in the shape you are planning. Where it sits
below the halfway mark, the page is upside down and reordering it is
the main work.

Two orderings are wrong however good the prose:

- A destructive action printed before the step that makes it
  survivable. Reader safety, rank 1.
- A definition placed after the sentence that leans on it. Checklist
  item 4.

A ledger, where the job has one, carries no order, so the shape is
always yours to decide. Say in the pull request how you decided it, so
a reviewer knows the shape was a decision rather than an inheritance.

**Placing a step first does not stop a reader skipping it.** A cold
reader given a page whose first procedure existed solely to prevent an
unrecoverable loss said they would have skipped it, because it read as
an optional convenience layer and nothing on the page was formatted as
a stop sign. Order is necessary and it is not sufficient. See "Marking
a step the reader will otherwise skip".

**The one ordering move a fix or a restyle may make is defined under
those jobs in "Ask which job this is before you start", not here.**
Where it applies, say in the pull request why the diff is larger than
the request.

**On a new page the shape is the whole risk.** There is no prior
structure to inherit and no reviewer comparing against one, so a
badly indexed page ships looking finished. Two things guard it: the
source-of-truth question above, because a page can only be indexed on
facts you were able to gather; and the full heading tree written down
before a word of prose, so the shape is arguable while it is still
cheap to change.

**Write the full heading tree to a file beside the draft, before a
word of prose, on a new page.** One line per heading, saying what that
heading establishes for the reader. The file is handed over with the
draft. An unwritten tree is not arguable, so the file is the point.
Where the finished page ends up differently shaped, say so rather than
quietly revising the tree to match.

**On a restructure or an overhaul, write the short heading tree to a
file beside the draft, before a word of prose.** The headings only, one
per line, in the order already decided under "Deciding the order",
with no rationale line: the file exists to fix that decision, not to
justify it. It is handed over with the draft the same way.

## How a page opens

Every page opens with a sentence. A gerund or a noun phrase standing in
for one is a fragment however long it runs, and twenty-six guides opened
that way before anyone noticed. This applies to the first sentence of
the body, never to the heading above it, which is a different rule
entirely and is given below.

The opening gets a new reader ready before it teaches anything:

- What the page does, or what has gone wrong.
- The three or four terms the page leans on, one sentence each. Define
  them as facts about the product, not as an announcement about the
  page. "A `hot` backup is the fastest to restore from" is the
  definition; "This page uses three terms" is a sentence about the
  page, and the page is not the subject.

Say what the reader can do before what the product cannot. A page that
opens with five things the product does not do has told the reader
nothing they can act on.

**No inline index of the page's own sections, anywhere on the page.**
Not a bulleted list of
links to the headings below, not "This page has eight sections:", not a
table of contents under any name. MkDocs Material renders the heading
tree in the right-hand pane on every page, so an inline copy is a
second navigation the reader has to reconcile with the real one, and it
goes stale the first time a heading is renamed. A README is the one
exception, because it renders on GitHub, which has no such pane.

**The page is not the subject of its own sentences.** "This page
covers", "this page uses", "on this page", "below we will" are all the
page talking about itself instead of about the product. Write the fact:
"A restore replaces the current data with the data in the backup you
select", never "This page explains what a restore does". A reader who
wanted to know what the page contains has the heading and the
navigation pane.

Headings are gerund phrases in title case: "Backing up and Restoring a
pgEdge Starfleet Managed Database", "Understanding a Backup",
"Rotating a Credential". The first of those carries the full edition
name because a heading counts as the name's first appearance.
The exception is a conventional navigational heading, which is a fixed
label the reader scans for rather than a description: "Next Steps",
"Troubleshooting", "Before You Start", "Prerequisites". Those keep
their standard wording.

**The noun a customer would search for goes inside the gerund phrase.**
"Comparing the Database Sizes" contains "database sizes" and is
findable. "Making Your Choice" contains nothing and is not. If the
gerund is hiding the searchable noun, the heading is wrong, not the
rule.
This is the house form, it is what the existing pages use, and an
imperative heading is the common way to break it. Name what the section
contains, in words a customer would search for. Never a sentence, never
a question with no answer, never a judgment, and never a dash carrying
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

