#!/usr/bin/env python3
"""Fail a fact ledger that marks a page's claim as verified.

    <skill>/check-sources.py <ledger.md>

An entry marked `st: V` asserts the claim was verified against
source. A documentation page is not a source. It is evidence that a
page says something, which is what `st: U` is for.

This gate was written after a ledger passed the phrase gate at n=5
and n=4 with 24 of its 55 entries marked V on the strength of another
docs page — five of them on the strength of the very page the ledger
had been extracted from. The builder had been told in its own
dispatch that a sibling page is the weakest authority there is. The
mark is self-assigned, so nothing contradicted it.

Generated reference pages under `docs/reference/` are exempt: they
are produced from the cobra command tree and cannot drift from the
binary. A dated probe log under `research/` is exempt too: it is a
record of a live measurement against the API, not prose that cites
nothing.

Exit 0 when every V entry cites something other than a hand-written
page, 1 otherwise.
"""

import pathlib
import re
import sys

SOURCE_RE = re.compile(r"[\w./-]+\.(?:go|ya?ml|txt|md|json|sql|sh|py)")


GENERATED = ("reference/", "research/")


def hand_written_page(ref):
    if not ref.endswith(".md"):
        return False
    return not any(seg in ref for seg in GENERATED)


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    path = pathlib.Path(argv[0])
    text = path.read_text()

    blocks = [b for b in re.split(r"\n(?=F\d+\.)", text)
              if re.match(r"F\d+\.", b)]
    bad = []
    for block in blocks:
        num = re.match(r"(F\d+)\.", block).group(1)
        status = re.search(r"st:\s*([VUCS])", block)
        src = re.search(r"src:(.*?)(?:\n\s*st:|\Z)", block, re.S)
        if not status or status.group(1) != "V" or not src:
            continue
        refs = SOURCE_RE.findall(src.group(1))
        if refs and all(hand_written_page(r) for r in refs):
            bad.append((num, " ".join(src.group(1).split())))

    print(f"ledger {path}: {len(blocks)} F entries")
    if not bad:
        print("PASS — every V entry cites a source that is not a "
              "hand-written page.")
        return 0

    print(f"FAIL — {len(bad)} V entries are verified against a docs "
          f"page and nothing else.")
    print("Settle each against the Go source, a spec, a probe log or "
          "the generated\nreference, or mark it U.\n")
    for num, src in bad:
        print(f"    {num}  {src}")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
