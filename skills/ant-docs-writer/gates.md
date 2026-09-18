# Gates

Loaded by every job.

Which of the four gate scripts run for a job is stated in each gate's
own heading below. Run every gate that applies before calling a page
done, and report its numbers. A gate that exits non-zero, or whose
output reads FAIL, has not been passed: fix what it names, rerun it,
and report only the numbers from the run that passed.

A fix is the one job that ends on a failing gate, because the carve-out
under check-mechanics.py leaves untouched sentences alone. There, report
the findings from the failing run and say which sentences they sit in.
On every other job a failing gate means the page is not done.

Invoke each script by its path from `<skill>/`, since the working
directory is the documentation repository, not the skill directory.
Locate the base directory via the skill's own announced path, or with
`find ~/.claude -path '*ant-docs-writer*' -name 'signals.py'`.

## check-sources.py (overhaul only)

    <skill>/check-sources.py <ledger.md>

Fails a ledger entry marked `st: V` that cites only a hand-written
page. A documentation page is not a source; it is evidence that a
page says something, which `st: U` is for. Generated reference and a
dated probe log under `research/` both count as a source; only a
sibling guide does not. Run it on the ledger the moment it arrives,
before writing a word.

## check-ledger.py (the phrase gate; overhaul and new page only)

A fix, a restyle and a restructure skip it.

    <skill>/check-ledger.py <source.md> <ledger.md> [--n 5]
        [--allow accepted.txt]

The source and the target must never be the same file. The script
always reports its second operand as "the ledger" whatever is passed;
report that operand as the draft in every run.

Run each applicable comparison at `--n 5` and again at `--n 4`, after
the draft exists:

- Overhaul: old page as source, draft as target. Measures how much of
  the old page's phrasing reached the draft by any route.
- Overhaul: ledger as source, draft as target. Narrows the old-page
  run to phrasing that came through the ledger.
- Overhaul and new page: brief as source, draft as target.

After the first run, rewrite each shared sequence once. Never a
second rewrite pass.

**Allow file.** A sequence the page must repeat (a title, a product
term, a screen-spelled label) goes in an allow file beside the draft,
one phrase per line. A trailing `# reason` after the phrase is a
comment; a one-word phrase is ignored. A missing `--allow` file allows
nothing rather than failing the run. A sequence passes when it lies
inside an allowed phrase, or contains one whole. The allow file ships
with the draft, so a reviewer can see what was excused.

**What the script strips.** Code spans, double-quoted strings and a
sequence containing an identifier with an underscore (such as
`pg_dump`) are stripped from both sides before comparing, and each
paragraph is unwrapped onto one line first, so a wrapped span is
still stripped whole. A shared sequence is re-expressed, never padded
around; a phrase already shipped as vocabulary on a sibling page may
stay shared.

## check-mechanics.py (every job)

    <skill>/check-mechanics.py <page.md> [<page.md> ...]

Runs on the draft on every job. Catches:

- British spelling, word-list only.
- A sentence opening on a quoted string that is itself a complete
  sentence.
- A banned word, idiom, hedge, register swap, standard-verb violation,
  or product or interface noun error named in style-standard.md,
  writing.md or product-vocabulary.md.
- More than two uses of one accumulation word. A quoted product
  string is exempt from the spelling, named-word and accumulation
  checks; the opener check still reads it.
- A precondition true of every page: the login statement in any of
  its wordings, anywhere on the page; and, inside a Before You Start
  or Prerequisites section, a profile, a network connection, a shell,
  an account, or nothing at all. This is the writing.md rule that no
  writer applied on pgEdge/pgedge-cli#520, so it is checked here
  rather than trusted to a reader. The fix is deletion, and a section
  left empty by it goes too.

A step's own indented prose is checked; the step's indented code is
not. The two are told apart by column, not by a flat four-space rule:
code is whatever sits four columns past the list item's own content,
so a bare four-space indent outside any list is still code.

On a fix, a finding in a sentence the fix did not change is listed in
the hand-back and left unfixed; a finding in a sentence the fix did
change must be fixed before the page is done. A restyle, restructure,
overhaul and new page fix every finding, since wording is in their
scope.

## signals.py (restyle, restructure, overhaul, new page)

    <skill>/signals.py <page.md> [<page.md> ...]

Run on the draft before finishing; report what it says. Strips code,
tables and headings first and measures prose only, since a docs page
is mostly not prose — but a step's own indented prose stays in the
count, by the same column rule check-mechanics.py uses, so a
step-heavy page is not scored on a fraction of itself. Reports Flesch
reading ease, Flesch-Kincaid grade, mean sentence length and syllable
density, with a verdict per bound. A crossed bound fails the run the
same as any other gate.

"Reading signals" in writing.md holds the two bounds and what to do
about a crossed one. They are stated there rather than here so that a
change to either lands in one file.
