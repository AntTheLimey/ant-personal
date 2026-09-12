#!/usr/bin/env python3
"""Fail a fact ledger that carries the source page's phrasing.

A ledger exists to strip the old page's prose and keep only its facts.
The first one written for this experiment shared 143 five-word
sequences with the page it extracted, so every rewrite built from it
inherited the page's constructions — including three writers under an
explicit instruction never to carry a phrasing over. They could not
obey: nothing told them which phrases were inherited.

This is the gate that would have caught it.

    ./check-ledger.py <source.md> <ledger.md> [--n 5]

Exit 0 when no shared sequence survives, 1 otherwise, listing what did.

Code spans and indented blocks are stripped from both sides first: a
command is meant to be repeated verbatim. A sequence containing an
identifier with an underscore is exempt for the same reason —
pg_dump and app_read_only are proper nouns, not prose.
"""

import argparse
import pathlib
import re
import sys


def tokens(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"^(?: {4,}|\t).*$", " ", text, flags=re.M)
    text = re.sub(r"https?://\S+", " ", text)
    return re.findall(r"[A-Za-z][A-Za-z_']*", text.lower())


def grams(words, n):
    return [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("ledger")
    ap.add_argument("--n", type=int, default=5)
    a = ap.parse_args()

    src = tokens(pathlib.Path(a.source).read_text())
    led = tokens(pathlib.Path(a.ledger).read_text())
    sg, lg = set(grams(src, a.n)), set(grams(led, a.n))

    shared = {g for g in sg & lg if not any("_" in w for w in g)}

    print(f"source {a.source}: {len(sg)} distinct {a.n}-word sequences")
    print(f"ledger {a.ledger}: {len(lg)}")
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
