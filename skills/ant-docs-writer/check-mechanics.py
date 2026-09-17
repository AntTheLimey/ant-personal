#!/usr/bin/env python3
"""Fail a docs page on spelling, a quoted-string opener or a named word.

    <skill>/check-mechanics.py <page.md> [<page.md> ...]

Four checks. The first two are defects no cold reader caught in 18
reps; the last two are the words and constructions style-standard.md
and writing.md name, which a cold reader otherwise has to find:

- British spelling. The docset is US English. The check is a word
  list, not a dictionary, so it catches the listed forms and nothing
  else. Headings, image alt text, table cells and indented lines are
  checked, since step prose shares its indent with code. Fenced code,
  inline code and double-quoted strings are not, because a quoted
  product string is reproduced as the product prints it.
- A sentence that opens on a quoted string that is itself a complete
  sentence, such as
  "`Could not start the restore.` is a red notification". The reader
  crosses two sentence ends before reaching the verb.
- A word or phrase the rules name as banned: the banned words, the
  named idioms and hedges, the register swaps, the command verbs, the
  product and interface nouns, and the signposting to delete on sight.
  Matched across line breaks. Each finding names the replacement.
- Accumulation: more than two of "actually", "critical", "matters",
  "exactly", "rather than" or "at scale" on one page.

Every check skips fenced code, inline code, double-quoted strings, link
targets and HTML comments. A word inside a quoted product string is
the product's word, and stays.

An unclosed fence is reported too, since nothing after it is checked.

Exit 0 when no page has a finding, 1 when one does, 2 when a page
could not be read or no page was given.
"""

import pathlib
import re
import sys

# British form -> US form. A form listed here also matches with the
# suffixes in SUFFIXES and after any prefix, so "organis" covers
# organise, reorganised and organisational. ALLOWED holds the US words
# a stem still reaches.
STEMS = {
    "organis": "organiz", "recognis": "recogniz", "customis": "customiz",
    "initialis": "initializ", "authoris": "authoriz",
    "prioritis": "prioritiz", "optimis": "optimiz", "minimis": "minimiz",
    "maximis": "maximiz", "normalis": "normaliz", "serialis": "serializ",
    "deserialis": "deserializ", "synchronis": "synchroniz",
    "standardis": "standardiz", "summaris": "summariz",
    "utilis": "utiliz", "realis": "realiz", "finalis": "finaliz",
    "visualis": "visualiz", "categoris": "categoriz",
    "specialis": "specializ", "emphasis": "emphasiz",
    "apologis": "apologiz", "capitalis": "capitaliz",
    "centralis": "centraliz", "localis": "localiz",
    "sanitis": "sanitiz", "tokenis": "tokeniz",
    "parameteris": "parameteriz", "containeris": "containeriz",
    "virtualis": "virtualiz", "stabilis": "stabiliz",
    "generalis": "generaliz", "characteris": "characteriz",
    "familiaris": "familiariz", "personalis": "personaliz",
    "randomis": "randomiz", "itemis": "itemiz", "modernis": "moderniz",
    "memoris": "memoriz", "materialis": "materializ",
    "criticis": "criticiz", "monetis": "monetiz",
    "analys": "analyz",
    "paralys": "paralyz", "catalys": "catalyz",
    "colour": "color", "behaviour": "behavior", "favour": "favor",
    "honour": "honor", "labour": "labor", "neighbour": "neighbor",
    "flavour": "flavor", "humour": "humor", "rumour": "rumor",
    "harbour": "harbor", "endeavour": "endeavor", "rigour": "rigor",
    "vigour": "vigor", "odour": "odor", "savour": "savor",
    "labell": "label", "cancell": "cancel", "modell": "model",
    "travell": "travel", "signall": "signal", "levell": "level",
    "channell": "channel", "tunnell": "tunnel", "fuell": "fuel",
    "totall": "total",
}

# The ending after a stem. An -ise stem alone is not a word, so the
# empty ending only ever matches a whole -our word such as colour.
SUFFIXES = (r"(?:e|es|ed|ing|ings|er|ers|ation|ations|ational|"
            r"ationally|able|ably|s|ite|ites|al|ally|ful|less|hood|"
            r"hoods)?")

WORDS = {
    "licence": "license", "licences": "licenses", "defence": "defense",
    "offence": "offense", "pretence": "pretense", "centre": "center",
    "centres": "centers", "centred": "centered", "metre": "meter",
    "metres": "meters", "litre": "liter", "fibre": "fiber",
    "calibre": "caliber", "judgement": "judgment",
    "judgements": "judgments", "acknowledgement": "acknowledgment",
    "acknowledgements": "acknowledgments", "grey": "gray",
    "programme": "program", "programmes": "programs", "cheque": "check",
    "whilst": "while", "amongst": "among", "afterwards": "afterward",
    "towards": "toward", "backwards": "backward",
    "catalogue": "catalog", "catalogues": "catalogs",
    "dialogue": "dialog", "dialogues": "dialogs", "analogue": "analog",
    "learnt": "learned", "spelt": "spelled", "enrolment": "enrollment",
    "instalment": "installment", "fulfil": "fulfill",
    "fulfils": "fulfills", "skilful": "skillful", "wilful": "willful",
    "ageing": "aging", "artefact": "artifact", "artefacts": "artifacts",
    "sceptical": "skeptical", "manoeuvre": "maneuver",
    "orientated": "oriented", "storey": "story", "mould": "mold",
    "practise": "practice", "practised": "practiced",
    "practising": "practicing", "greyed": "grayed", "greying": "graying",
    "defences": "defenses", "offences": "offenses",
    "fulfilment": "fulfillment", "centring": "centering",
}

# US words a stem still reaches: the noun emphasis, the plurals of
# analysis, paralysis and catalysis, and cancellation, which keeps its
# double l. Matched on the word's ending, so overemphasis passes too.
ALLOWED = ("emphasis", "analyses", "paralyses", "catalyses",
           "cancellation", "cancellations")

STEM_RE = re.compile(
    r"\b([a-z]*?)(" + "|".join(sorted(STEMS, key=len, reverse=True)) +
    r")(" + SUFFIXES + r")\b", re.I)
WORD_RE = re.compile(r"\b(" + "|".join(WORDS) + r")\b", re.I)

# A sentence start: the start of a line, after list or heading markup
# and optional bold, or after a sentence end on the same line. The
# quoted string must end on a word before its stop, so an ellipsis or a
# bare "?" is not a sentence of its own.
OPENER_RE = re.compile(
    r"(?:^\s*(?:[-*+]\s+|\d+[.)]\s+|>\s*|#{1,6}\s+)?(?:\*\*|__)?"
    r"|\|\s*(?:\*\*|__)?"
    r"|(?<!\be\.g)(?<!\bi\.e)[.!?](?:\*\*|__)?\s*(?:\*\*|__)?"
    r"(?<=[\s*_]))"
    r"(`[^`]*[\w>)\]'\"][.!?]`|\"[^\"]*[\w>)\]'][.!?]\"|"
    r"“[^”]*[\w>)\]'][.!?]”)"
    r"\s+[a-z]")


# (pattern, replacement advice). Case-insensitive, whole words, and a
# space in a pattern matches any run of whitespace, line breaks
# included. Each entry is a rule stated in style-standard.md,
# writing.md or product-vocabulary.md; a word only a careful reader
# could judge is not here.
NAMED = [
    (r"leverag(?:e|es|ed|ing)", "banned word"),
    (r"utiliz(?:e|es|ed|ing|ation)", "banned word, use \"use\""),
    (r"ensur(?:e|es|ed|ing)", "banned word"),
    (r"seamless(?:ly)?", "banned word"),
    (r"best-in-class", "banned word"),
    (r"synerg(?:y|ies)", "banned word"),
    (r"paradigm shifts?", "banned phrase"),
    (r"stakeholder alignment", "banned phrase"),
    (r"carr(?:y|ies|ied|ying) weight", "idiom, use \"matter\""),
    (r"a way back", "idiom, use \"a way to undo it\""),
    (r"the shape of it", "idiom, use \"the structure\""),
    (r"lands wrong", "idiom"),
    (r"worth knowing", "idiom and signposting, state the fact"),
    (r"pretty much", "conversational hedge"),
    (r"simply", "conversational hedge"),
    (r"of course", "conversational hedge"),
    (r"surfac(?:ed|ing)", "register, use \"shows\" or \"appears\""),
    (r"surfaces (?:in|on|as|when|after|once|within|up)",
     "register, use \"appears\" or \"shows\""),
    (r"ahead of", "register, use \"before\""),
    (r"(?:can|could|will|may|might) \w+ more of them",
     "register, name what there is more of"),
    (r"verbs?", "use \"command\""),
    (r"poll(?:s|ed|ing)?", "jargon, write \"run X until Y\""),
    (r"query an? command", "you run a command"),
    (r"hit an? endpoint", "jargon"),
    (r"fire an? request", "jargon"),
    (r"grab an? value", "you read a value"),
    (r"PostgreSQL", "use \"Postgres\""),
    (r"pgEdge Cloud", "retired name, use \"pgEdge Starfleet\""),
    (r"(?<!pgEdge\s)(?<!pgEdge\s\s)Starfleet",
     "write \"pgEdge Starfleet\""),
    (r"unmeasured", "use \"unknown\""),
    (r"not recorded here", "use \"unknown\""),
    (r"pop-?ups?", "use \"dialog\""),
    (r"modals?", "use \"dialog\""),
    (r"panels?", "use \"pane\", or \"section\" inside a dialog"),
    (r"this section covers|this page (?:covers|uses|has)",
     "signposting, delete it"),
    (r"now that we have", "signposting, delete it"),
    (r"it is worth noting", "signposting, delete it"),
    (r"importantly", "signposting, delete it"),
    (r"crucially", "signposting, delete it"),
    (r"pay special attention", "signposting, delete it"),
    (r"the catch is", "signposting, delete it"),
    (r"note that", "signposting, delete it"),
    (r"and this is why it bites", "signposting, delete it"),
    (r"coming soon", "forward-looking, describe what is"),
    (r"we", "do not write \"we\""),
]
NAMED_RE = [(re.compile(r"(?<![\w-])" + pat.replace(" ", r"\s+") +
                        r"(?![\w-])", re.I), advice)
            for pat, advice in NAMED]

TICS = ["actually", "critical", "matters", "exactly", "rather than",
        "at scale"]
TIC_LIMIT = 2


BLANK = "\u00b7"


def mask(line):
    """Blank inline code, quoted strings, URLs and link targets.

    The blank is a middle dot, not a space, so a named phrase cannot
    match across a masked span: "the `app` user" is not "the user".
    """
    line = re.sub(r"``.*?``|`[^`]*`", lambda m: BLANK * len(m.group()),
                  line)
    line = re.sub(r"\"[^\"]*\"|“[^”]*”",
                  lambda m: BLANK * len(m.group()), line)
    line = re.sub(r"\]\([^)]*\)|\]\[[^\]]*\]|^\s*\[[^\]]+\]:.*$",
                  lambda m: BLANK * len(m.group()), line)
    line = re.sub(r"<!--.*?-->", lambda m: BLANK * len(m.group()), line)
    line = re.sub(r"https?://\S+", lambda m: BLANK * len(m.group()), line)
    return line


def cased(us, word):
    if word.isupper():
        return us.upper()
    if word[0].isupper():
        return us[0].upper() + us[1:]
    return us


def spelling(line):
    found = []
    for m in STEM_RE.finditer(line):
        word = m.group(0)
        if word.lower().endswith(ALLOWED):
            continue
        prefix, stem, suffix = m.groups()
        # A bare -is or -ys stem is never an English word, so a match
        # with no ending is Latin, such as borealis.
        if not suffix and stem.lower().endswith(("is", "ys")):
            continue
        us = (prefix + STEMS[stem.lower()] + suffix).lower()
        found.append((m.start(), word, cased(us, word)))
    for m in WORD_RE.finditer(line):
        word = m.group(0)
        found.append((m.start(), word, cased(WORDS[word.lower()], word)))
    return sorted(found)


PARAGRAPH_MASKS = [
    r"``.*?``",
    r"`[^`\n]*(?:\n[^`\n]*)?`",
    r"\"[^\"\n]*(?:\n[^\"\n]*)?\"",
    r"\u201c[^\u201d\n]*(?:\n[^\u201d\n]*)?\u201d",
    r"\]\([^)]*\)",
    r"\]\[[^\]]*\]",
    r"^\s*\[[^\]]+\]:.*$",
    r"<!--.*?-->",
    r"https?://\S+",
]


def named(lines):
    """Named words and tics over the checked lines, across line breaks.

    lines is a list of (line number, raw text). Consecutive lines of one
    paragraph are joined with a newline, so a phrase wrapped at 79
    columns still matches, and a code span or a quoted string wrapped
    across one line break is still masked. A blank line, or a gap where
    a fence or a comment was skipped, joins with a barrier instead, so
    no phrase matches across it. Masking keeps every offset, and each
    match is mapped back to the line it starts on.
    """
    barrier = "\n" + BLANK + "\n"
    starts, parts, pos, prev = [], [], 0, None
    for n, text in lines:
        if parts:
            sep = "\n"
            if prev is None or n != prev + 1 or not text.strip() \
                    or not parts[-1].strip():
                sep = barrier
            parts.append(sep)
            pos += len(sep)
        starts.append((pos, n))
        parts.append(text)
        pos += len(text)
        prev = n
    joined = "".join(parts)
    for pat in PARAGRAPH_MASKS:
        joined = re.sub(pat, lambda m: re.sub(r"[^\n]", BLANK, m.group()),
                        joined, flags=re.M)

    def where(offset):
        line_start, n = max(s for s in starts if s[0] <= offset)
        return n, offset - line_start + 1

    found = []
    for rx, advice in NAMED_RE:
        for m in rx.finditer(joined):
            n, col = where(m.start())
            word = " ".join(m.group().split())
            found.append((n, col, f"\"{word}\": {advice}"))
    for tic in TICS:
        rx = re.compile(r"(?<![\w-])" + tic.replace(" ", r"\s+") +
                        r"(?![\w-])", re.I)
        hits = list(rx.finditer(joined))
        for m in hits[TIC_LIMIT:]:
            n, col = where(m.start())
            found.append((n, col, f"\"{tic}\" {len(hits)} times on the "
                                  f"page, more than {TIC_LIMIT}"))
    return found


def check(text):
    findings = []
    checked = []
    fence, fence_line, comment = None, 0, False
    for n, raw in enumerate(text.splitlines(), 1):
        # A fence closes only on its own character, at least as long as
        # the opener, with nothing after it. A nested ``` inside a ````
        # block would otherwise end the block early, or reopen one, and
        # silently pass the rest of the page.
        m = re.match(r"^\s*(`{3,}|~{3,})(.*)$", raw)
        if fence:
            if (m and m.group(1)[0] == fence[0]
                    and len(m.group(1)) >= len(fence)
                    and not m.group(2).strip()):
                fence = None
            continue
        if m:
            fence, fence_line = m.group(1), n
            continue
        if comment:
            if "-->" in raw:
                comment = False
            continue
        if re.search(r"<!--(?!.*-->)", raw):
            comment = True
            raw = raw[:raw.index("<!--")]
        checked.append((n, raw))
        for col, word, us in spelling(mask(raw)):
            findings.append((n, col + 1,
                             f"British spelling \"{word}\", "
                             f"use \"{us}\""))
        for m in OPENER_RE.finditer(raw):
            findings.append((n, m.start(1) + 1,
                             f"sentence opens on {m.group(1)}, a "
                             f"complete sentence of its own"))
    findings.extend(named(checked))
    findings.sort()
    if fence:
        findings.append((fence_line, 1, "fence never closes, so nothing "
                                        "after it was checked"))
    return findings


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    sys.stdout.reconfigure(encoding="utf-8")
    total, unread = 0, 0
    for arg in argv:
        p = pathlib.Path(arg)
        try:
            text = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as err:
            unread += 1
            print(f"{p}: not checked: {err}", file=sys.stderr)
            continue
        findings = check(text)
        total += len(findings)
        for n, col, text in findings:
            print(f"{p}:{n}:{col}: {text}")
        print(f"{p.name:<44} {len(findings)} finding"
              f"{'' if len(findings) == 1 else 's'}")
    print()
    if unread:
        print(f"ERROR — {unread} page{'' if unread == 1 else 's'} could "
              f"not be read, {total} finding{'' if total == 1 else 's'} "
              f"on the rest.")
        return 2
    if not total:
        print(f"PASS — no finding on {len(argv)} "
              f"page{'' if len(argv) == 1 else 's'}.")
        return 0
    print(f"FAIL — {total} finding{'' if total == 1 else 's'}. "
          f"Fix the prose and run it again.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
