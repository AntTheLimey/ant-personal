#!/usr/bin/env python3
"""Fail a fact ledger that carries the source page's phrasing.

A ledger exists to strip the old page's prose and keep only its facts.
The first one written for this experiment shared 143 five-word
sequences with the page it extracted, so every rewrite built from it
inherited the page's constructions — including three writers under an
explicit instruction never to carry a phrasing over. They could not
obey: nothing told them which phrases were inherited.

This is the gate that would have caught it.

    <skill>/check-ledger.py <source.md> <ledger.md> [--n 5]
        [--allow accepted.txt]

Exit 0 when no shared sequence survives, 1 otherwise, listing what did.

Code spans, double-quoted strings and indented blocks are stripped from
both sides first: a command or a UI label is meant to be repeated
verbatim. A sequence containing an identifier with an underscore is
exempt for the same reason — pg_dump and app_read_only are proper
nouns, not prose.

--allow names a file of phrases, one per line, that the page must
repeat: its title, a product term, a label as the screen spells it.
A shared sequence falling inside an allowed phrase is reported as
allowed and does not fail the run. Without this, a writer rewrites the
page's own vocabulary pass after pass chasing a gate that cannot pass.
"""

import argparse
import pathlib
import re
import sys


def tokens(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"^(?: {4,}|\t).*$", " ", text, flags=re.M)
    # Unwrap each paragraph onto one line, so a code span or a quoted
    # label broken by the 79-column wrap is still stripped as a whole.
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    text = re.sub(r"`[^`\n]*`", " ", text)
    text = re.sub(r"\"[^\"\n]*\"|\u201c[^\u201d\n]*\u201d", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    return re.findall(r"[A-Za-z][A-Za-z_']*", text.lower())


def grams(words, n):
    return [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]


def phrases(path):
    """The allowed phrases, tokenized as the pages are.

    A missing file allows nothing, so the first run, before the file
    exists, reports shared sequences instead of crashing. A trailing
    "# reason" is not part of the phrase. A one-word phrase is ignored:
    it would excuse every sequence containing that word.
    """
    p = pathlib.Path(path)
    if not p.exists():
        print(f"allow file {path} does not exist yet; nothing allowed",
              file=sys.stderr)
        return []
    out = []
    for line in p.read_text().splitlines():
        line = re.sub(r"(^|\s)#.*$", "", line).replace('"', " ")
        words = tokens(line)
        if len(words) >= 2:
            out.append(tuple(words))
        elif words:
            print(f"allow file: one-word phrase ignored: {line.strip()}",
                  file=sys.stderr)
    return out


def inside(small, big):
    k = len(small)
    return any(big[i:i + k] == small for i in range(len(big) - k + 1))


def is_allowed(gram, allow):
    """A sequence inside an allowed phrase, or containing one whole."""
    return any(inside(gram, p) or inside(p, gram) for p in allow)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("ledger")
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--allow")
    a = ap.parse_args()

    src = tokens(pathlib.Path(a.source).read_text())
    led = tokens(pathlib.Path(a.ledger).read_text())
    sg, lg = set(grams(src, a.n)), set(grams(led, a.n))

    shared = {g for g in sg & lg if not any("_" in w for w in g)}
    allow = phrases(a.allow) if a.allow else []
    ok = {g for g in shared if is_allowed(g, allow)}
    shared -= ok

    print(f"source {a.source}: {len(sg)} distinct {a.n}-word sequences")
    print(f"ledger {a.ledger}: {len(lg)}")
    print()
    for g in sorted(ok):
        print("    allowed:", " ".join(g))
    if ok:
        print()
    if not shared:
        print(f"PASS — no {a.n}-word sequence is shared.")
        return 0

    pct = len(shared) / len(sg) * 100
    print(f"FAIL — {len(shared)} shared, {pct:.0f}% of the source's "
          f"phrasing survives into the ledger.")
    print("Rewrite each of these in note form; do not paraphrase them.\n")
    for g in sorted(shared):
        print("   ", " ".join(g))
    return 1


if __name__ == "__main__":
    sys.exit(main())
