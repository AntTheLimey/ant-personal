# Gates

The four gate scripts, when each runs, and what a failure means.
Loaded by every job.

## The gates, and when each runs

Four scripts run here, and which of them apply depends on the job: the
table under "Ask which job this is before you start" in SKILL.md is
the one place that is decided. Run every gate that applies before
calling a page done, and report its numbers.

**A gate that exits non-zero has not been passed, and neither has one
whose output reads `FAIL`.** That is a failure to fix before the page
is done, rather than a number to report. Fix what the gate names, run
it again, and report the numbers from the run that passed.

Run `check-sources.py` on the ledger the moment it arrives, before you
write a word, on an overhaul. The gate fails a `V` entry that cites
only a hand-written page:

    <skill>/check-sources.py <ledger>

A fix, a restyle, a restructure and a new page build no ledger, so
this gate does not run on them.

The phrase gate is `check-ledger.py`. `check-sources.py`'s own
docstring calls it that. It runs on an overhaul and on a new
page. A restyle and a restructure keep the page's own wording as the
starting point and skip it, and a fix touches one claim and skips it
too. It takes two files, the text the draft may have copied from and
the draft, and takes `--allow <accepted.txt>` naming phrases the gate
should not fail on. **The source and the draft are never the same
file.** The draft passed in both slots reports every sequence in it as
shared, which measures the invocation rather than the draft. Run each
of the below that applies, after the draft exists, at `--n 5` and
again at `--n 4`.

On an overhaul, measure the old page against the draft. This run
reports how much of that page's phrasing reached the draft by any
route:

    <skill>/check-ledger.py <old-page> <draft> --allow <accepted.txt>

On an overhaul, measure the ledger against the draft. This run narrows
the one above to what came through the ledger:

    <skill>/check-ledger.py <ledger> <draft> --allow <accepted.txt>

On an overhaul and on a new page, measure the brief against the draft,
a channel a finished page has shared sequences with before:

    <skill>/check-ledger.py <brief> <draft> --allow <accepted.txt>

The script prints its first operand as the source and its second as
the ledger, whatever you pass. The second is your draft in every run,
so report it as the draft.

**Rewrite once, then allow what must repeat.** After the first run,
rewrite each shared sequence once. A sequence still shared that the
page must repeat, such as its title, a product term or a label as the
screen spells it, goes in an allow file beside the draft, one phrase
per line. A trailing `# reason` after the phrase is a comment, not
part of it. A one-word phrase is ignored, because it would excuse
every sequence containing that word. Backticks inside a phrase do
nothing, since code spans are already stripped from both pages before
comparison. **Never a second rewrite pass.** The allow file ships with
the draft, so a reviewer can see what was excused.

The `--allow` flag may name a file that does not exist yet: the first
run needs none, and a missing file allows nothing rather than failing
the run. A sequence passes once it lies inside an allowed phrase, or
contains one whole, so a two- or three-word product term excuses every
longer sequence built around it.

Code spans and double-quoted strings are stripped from both sides
before comparison. Each paragraph is unwrapped onto one line first, so
a code span or a quoted label broken across the 79-column wrap is
still stripped whole, and prose sitting between two quoted strings is
still measured.

A shared sequence is re-expressed, never padded around. A phrase that
is vocabulary already shipped in a sibling page stays: consistency
beats novelty there.

Run `signals.py` on the draft, on a restyle, a restructure, an
overhaul and a new page:

    <skill>/signals.py <draft>

See "Reading signals" in writing.md.

**A crossed bound fails the run.** The script exits non-zero and marks
the line `FAIL`, so the rule above applies to it as it does to the
other gates.

Run `check-mechanics.py` on the draft, on every job:

    <skill>/check-mechanics.py <draft>

This docset uses US spelling. The script catches a British spelling
from a fixed word list, and a sentence that opens on a quoted string
that is itself a complete sentence. It is a word list, not a
dictionary: it catches the listed forms only, so a spelling it does
not list still gets fixed the moment you see it.

The script also fails a word or construction the rules name outright,
from style-standard.md or writing.md. That covers the banned words,
the named idioms and hedges, the register swaps, the standard-verb
rule, the product and interface nouns, and the signposting to delete
on sight. More than two of the accumulation words on one page fails
it too. A quoted product string is exempt, as style-standard.md
defines under "Words".

On a fix, a finding in a sentence the fix did not change is listed in
the hand-back and not fixed; only a finding in a sentence the fix
changed must be fixed before the page is done. A restyle, a
restructure, an overhaul and a new page fix every finding, because
wording is in their scope.

