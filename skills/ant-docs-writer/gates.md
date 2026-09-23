# Gates

| Gate | Runs on |
|---|---|
| check-sources.py | overhaul only |
| check-ledger.py (phrase gate) | overhaul, new page |
| check-mechanics.py | restyle, restructure, overhaul, new page |
| signals.py | restyle, restructure, overhaul, new page |

Run every gate that applies before calling a page done, and report
its numbers. A gate that exits non-zero, or reads FAIL, hasn't
passed: fix what it names, rerun it, report only the numbers from the
run that passed.

Invoke each script by its path from `<skill>/`: the working directory
is the documentation repository, not the skill directory. Find the
base via the skill's own announced path, or `find ~/.claude -path
'*ant-docs-writer*' -name 'signals.py'`.

## check-sources.py

    <skill>/check-sources.py <ledger.md>

Fails a ledger entry marked `st: V` that cites only a hand-written
page — a documentation page is evidence a page says something
(`st: U`), not a source. Generated reference and a dated probe log
under `research/` both count as a source; a sibling guide doesn't.
Run it on the ledger the moment it arrives, before writing a word.

## check-ledger.py — the phrase gate

    <skill>/check-ledger.py <source.md> <ledger.md> [--n 5]
        [--allow accepted.txt]

Source and target must never be the same file. The script always
calls its second operand "the ledger"; report that operand as the
draft in every run.

Run each applicable comparison at `--n 5` and `--n 4`, after the
draft exists:

| Comparison | Job | Measures |
|---|---|---|
| old page → draft | overhaul | phrasing reaching the draft by any route |
| ledger → draft | overhaul | phrasing reaching the draft through the ledger |
| brief → draft | overhaul, new page | — |

After the first run, rewrite each shared sequence once — never a
second rewrite pass.

**Allow file.** A sequence the page must repeat (a title, a product
term, a screen-spelled label) goes in an allow file beside the draft,
one phrase per line; a trailing `# reason` is a comment, a one-word
phrase is ignored. A missing `--allow` file allows nothing rather
than failing the run. A sequence passes inside an allowed phrase, or
containing one whole. The allow file ships with the draft, so a
reviewer sees what was excused.

**What it strips.** Code spans, double-quoted strings, and any
sequence containing an underscored identifier (`pg_dump`), from both
sides before comparing; each paragraph is unwrapped onto one line
first, so a wrapped span still strips whole. A shared sequence is
re-expressed, never padded around; a phrase already shipped as
vocabulary on a sibling page may stay shared.

## check-mechanics.py

    <skill>/check-mechanics.py <page.md> [<page.md> ...]

Catches:

- British spelling (word list; style-standard.md, "Spelling").
- A sentence opening on a quoted string that's itself a complete
  sentence.
- A banned word, idiom, hedge, register swap, standard-verb
  violation, or product/interface noun error (style-standard.md,
  writing.md, product-vocabulary.md).
- More than two uses of one accumulation word. A quoted product
  string is exempt from spelling, named-word and accumulation checks;
  the opener check still reads it.
- The universal precondition: the login statement in any wording,
  anywhere; and, inside Before You Start/Prerequisites, a profile, a
  network connection, a shell, an account, or nothing at all — a
  writing.md rule a writer reliably loads and still misses, checked
  here rather than trusted to a reader. Fix is deletion; an emptied
  section goes too.

A step's own indented prose is checked, its indented code is not —
told apart by column, not a flat four-space rule: code is whatever
sits four columns past the list item's own content, so a bare
four-space indent outside any list is still code.

Fix every finding, with one exception: a spelling finding in link text
whose target is outside the change — fixing it means retitling the
target and every link to it together, so when the target can't be
touched, list it in the hand-back, leave it, and the gate stays red on
it.

## signals.py

    <skill>/signals.py <page.md> [<page.md> ...]

Run before finishing; report what it says. Strips code, tables and
headings first, measures prose only — a docs page is mostly not
prose, but a step's own indented prose stays in the count (same
column rule as check-mechanics.py), so a step-heavy page isn't scored
on a fraction of itself. Reports Flesch reading ease, Flesch-Kincaid
grade, mean sentence length and syllable density, with a verdict per
bound. A crossed bound fails the run like any other gate.

The two bounds and what to do about a crossed one are in writing.md's
"Reading signals", so a change to either lands in one file.
