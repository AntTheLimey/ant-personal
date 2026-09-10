# Pages an agent reads

The CLI's embedded reference pages and its shipped skills are read by
AI agents driving the CLI, not by people. Everything in `SKILL.md`
applies unless this file says otherwise. STE was written for a human
reader, so the divergences are worth stating rather than assuming.

## What changes

**Precision outranks elegance.** Never weaken or strengthen an
instruction while editing around it. A rewrite that turns "refuses"
into "may refuse" has changed the contract, and an agent acts on the
difference.

**The one-instruction-per-sentence rule gets stricter, not looser.** A
human reading a compound instruction slows down. An agent executes the
first half and drops the second, or runs both as a single call. This is
the STE rule that transfers hardest.

**The 20 and 25 word caps become targets rather than limits.** An agent
parses a long sentence without difficulty. Ambiguity is still the
enemy, so the caps stay useful as a discipline, but a 30-word sentence
that removes an ambiguity beats two shorter ones that leave it.

**A page is reached second, never first.** An agent reads the index,
learns which page answers its question, then reads that one page. So
each page is self-contained about its own resource, and repeats nothing
the index already owns: authentication, exit codes, IDs and paging live
in the index.

**Terms are never inferred.** An agent will not work out from context
that "node" and "instance" are different things. Every distinction the
page depends on is stated on the page, in the same words every time.

## Format divergences

The docs pages and the agent pages format code differently, and mixing
them breaks the build gates:

- Pages under `docs/` use 4-space indented code blocks, never fences.
- The `llms` pages and the shipped skills use fences, introduced by an
  `**Example:**` style label or by a lead-in sentence ending in a
  colon.

The `**Example:**` label has four accepted forms. A bare label on its
own line is the default. A qualified label such as `**Example (AWS):**`
names a variant. Prose ending in a colon needs no label at all, and
adding one after a colon reads badly. A `**Step N:**` heading in a
workflow recipe covers the fences underneath it.

The shipped skills use no label at all today. Leave that alone, or
converge it deliberately, but not in passing.

## Prose beats a pasted block, and here the reason is measured

Describe output in prose. A prose claim that names a field or a status
value is machine-checked by the reference gates. A pasted block is
checked far more thinly: its header line, its status cells, and little
else. Every other value in it, and every line it is missing, is checked
by nothing.

A sweep of the example-output blocks the references carried found
roughly half of them wrong, while the two references that pasted none
had none to fix. So a pasted block is mostly a claim nothing verifies,
and a sentence is a claim something does.

Scope the sentence to the command actually checked. A claim written for
`database get` is often false for `task get`, which prints a different
shape entirely.

Where a block does earn its place, capture it from a live call or
derive it from the format literal that prints it. Never compose one by
hand, and never tidy one up.

## Two mechanical traps

**Backticked snake_case is read as an API field claim.** A build gate
treats any entirely snake_case token in backticks as an assertion that
the field exists. Do not add one, and do not re-backtick an existing
word, without checking the field is real.

**A shell example must never swallow an exit status.** No pipe from a
`pgedge` call, no unchecked capture, no `&&` chain that hides a
failure. Redirect to a file, check the status, then process the file.
Gates enforce this across every reference page and every skill.

## Generated blocks

The command blocks in these pages are generated from the command tree
and are not editable by hand. Change the command, then regenerate.
Anything typed between the generated markers is overwritten on the next
build.
