#!/usr/bin/env python3
"""Reading signals for a docs page, measured over prose only.

    <skill>/signals.py <page.md> [<page.md> ...]

Fenced code, indented blocks, tables and headings are stripped before
scoring. A docs page is mostly not prose, and counting the commands
makes the number meaningless.

Reports Flesch reading ease, Flesch-Kincaid grade, mean sentence
length, and syllable density, then a verdict line per bound. The ease
floor in use is 58 and the grade ceiling is 8.0.

Exit 0 when every page meets both bounds, 1 otherwise. The verdict is
taken on the value as printed, to one decimal, so the number a reader
sees and the verdict beside it can never disagree.
"""

import pathlib
import re
import sys

VOWELS = "aeiouy"
EASE_FLOOR = 58.0
GRADE_CEILING = 8.0


def prose(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"^(?: {4,}|\t).*$", " ", text, flags=re.M)
    text = re.sub(r"^\s*\|.*$", " ", text, flags=re.M)
    text = re.sub(r"^\s*#{1,6} .*$", " ", text, flags=re.M)
    text = re.sub(r"^\s*[-*_]{3,}\s*$", " ", text, flags=re.M)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[*_]{1,2}", "", text)
    return text


def syllables(word):
    word = word.lower().strip("'")
    if not word:
        return 0
    count, prev_vowel = 0, False
    for ch in word:
        is_vowel = ch in VOWELS
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel
    if word.endswith("e") and count > 1 and not word.endswith(("le", "ee")):
        count -= 1
    return max(count, 1)


def measure(text):
    body = prose(text)
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", body) if
                 re.search(r"[A-Za-z]", s)]
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", body)
    if not sentences or not words:
        return None
    syl = sum(syllables(w) for w in words)
    wps = len(words) / len(sentences)
    spw = syl / len(words)
    return {
        "words": len(words),
        "sentences": len(sentences),
        "wps": wps,
        "spw": spw,
        "ease": 206.835 - 1.015 * wps - 84.6 * spw,
        "grade": 0.39 * wps + 11.8 * spw - 15.59,
        "over25": sum(1 for s in sentences
                      if len(re.findall(r"[A-Za-z][A-Za-z'-]*", s)) > 25),
    }


def verdicts(m):
    ease, grade = round(m["ease"], 1), round(m["grade"], 1)
    return [
        (ease >= EASE_FLOOR,
         f"reading ease {ease:.1f}, floor {EASE_FLOOR:.0f}"),
        (grade <= GRADE_CEILING,
         f"grade {grade:.1f}, ceiling {GRADE_CEILING:.1f}"),
    ]


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    print(f"{'page':<44} {'words':>6} {'sent':>5} {'w/s':>6} "
          f"{'syl/w':>6} {'ease':>6} {'grade':>6} {'>25w':>5}")
    measured = []
    for arg in argv:
        p = pathlib.Path(arg)
        m = measure(p.read_text())
        measured.append((p, m))
        if m is None:
            print(f"{p.name:<44} {'no prose':>6}")
            continue
        print(f"{p.name:<44} {m['words']:>6} {m['sentences']:>5} "
              f"{m['wps']:>6.1f} {m['spw']:>6.3f} {m['ease']:>6.1f} "
              f"{m['grade']:>6.1f} {m['over25']:>5}")

    print()
    crossed, grade_crossed = 0, False
    for p, m in measured:
        if m is None:
            crossed += 1
            print(f"{p.name:<44} FAIL  no prose, so neither bound "
                  f"was checked")
            continue
        for i, (met, text) in enumerate(verdicts(m)):
            print(f"{p.name:<44} {'PASS' if met else 'FAIL'}  {text}")
            if not met:
                crossed += 1
                grade_crossed = grade_crossed or i == 1

    print()
    if not crossed:
        print(f"PASS — every bound met on {len(measured)} "
              f"page{'' if len(measured) == 1 else 's'}.")
        return 0

    print(f"FAIL — {crossed} bound{'' if crossed == 1 else 's'} "
          f"crossed. Fix the prose and run it again.")
    if grade_crossed:
        print("Split the long sentence to come under the grade. Never "
              "drop the clause\ncarrying the condition: that makes a "
              "worse page than missing the ceiling.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
