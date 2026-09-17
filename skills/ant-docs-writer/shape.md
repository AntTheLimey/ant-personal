# Shape

Loaded by restructure, overhaul and new page.

## Content checklist

Run all eight items before writing and again before opening a pull
request. Passing all eight is necessary but not sufficient; the
reviews in reviews.md are the last gate.

1. **Every step is runnable as written.**
   - A command-line step needs its full prefix, a placeholder for
     every value, and every flag a safe non-interactive run needs.
   - A console step quotes every control exactly as it renders, and
     says where the screen is and what puts the reader on it.
   - The connection flag (`--base-url`/`--profile`) is assumed and
     unstated: a reader without one could not have reached the page.
     A destructive command prints its connection flag in the step
     anyway, because there it answers which tenant the command runs
     against, not whether the reader is authenticated.
2. Name what the reader would do instead of the written step, and
   say what it costs. A step naming no command also fails this item,
   because the reader invents one.
3. Every placeholder gets a sentence naming the command or screen
   that produces its value.
4. The page must work for a reader who did not create the resource:
   say where the value lives now and what to do without it.
5. Every term the procedure depends on is defined, on the page, before
   the first sentence that leans on it.
6. The page answers the question its own opening raises.
7. No step destroys something a later step needs. Read the procedure
   as a sequence and track state.
8. Strip every note and re-read the procedure. If the reader can no
   longer finish it, move that information into a step. The test is
   whether removing a block changes an action, not whether the block
   is indented; a step is allowed to be more than one line.

## Page length (overhaul)

Measure length with `wc -c` on the old page and the draft. Where the
draft is longer, name what the extra bytes bought, and cut length
that bought nothing. The reader wants the least that works: a warning
restated as a command, a mechanism explained where a consequence
would do, and a caveat written three times because it felt important
each time, are all length that bought nothing.

## Section order (restructure and overhaul)

Decide the section order as part of the work; it is not inherited
from the old page, and a ledger carries no order. The commonest defect
is a page ordered by the product's internals: it opens with a
taxonomy of what exists, explains the model, and reaches the reader's
task somewhere in the middle. Where the task sits below the halfway
mark, the page is upside down and reordering it is the main work.

Order by what the reader is doing: what the page gets them, what they
need first, then the task. After the task, order what goes wrong, then
where to go next.

- Reference material a task leans on goes in its own section, placed
  after the first step that needs it.
- A conceptual model the reader must hold before step one goes into
  the opening as one-sentence terms, never as a top section of its
  own.
- The two orderings that are always wrong, in writing.md, bind here
  too: they are the commonest way a reordered page breaks.

## Heading tree

- New page: write the full heading tree to a file beside the draft
  before any prose, one line per heading saying what it establishes.
  Hand the file over with the draft.
- Restructure and overhaul: write the short heading tree (headings
  only, no rationale line) to a file beside the draft before any
  prose. Hand it over with the draft.
- Where the finished page ends up shaped differently from the written
  tree, say so rather than quietly revising the tree to match.

On a new page the shape is the whole risk: there is no prior structure
to inherit and no reviewer comparing against one, so a badly indexed
page ships looking finished. The source-of-truth questions in
facts.md and the heading tree, written before a word of prose, are
what guard it.
