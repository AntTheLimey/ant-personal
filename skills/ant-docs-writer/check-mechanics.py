#!/usr/bin/env python3
"""Fail a docs page on spelling, a quoted-string opener or a named word.

    <skill>/check-mechanics.py <page.md> [<page.md> ...]

Five checks. The first two are defects no cold reader caught in 18
reps; the next two are the words and constructions style-standard.md
and writing.md name, which a cold reader otherwise has to find; the
last is a rule three writers loaded and none applied:

- British spelling. pgEdge documentation is US English, set by the
  public docs repository (behavior 34:2, color 43:1, initialize 17:0,
  measured 2026-09-18); a docset that reads British is the defect.
  The check is a word list, not a dictionary, so it catches the
  listed forms and nothing else. Headings, image alt text and table cells are checked. A step's
  indented prose is checked too, but an indented code block is not,
  since the two share an indent and only a list-aware column tells
  them apart. Fenced code, inline code and double-quoted strings are
  not, because a quoted product string is reproduced as the product
  prints it.
- A sentence that opens on a quoted string that is itself a complete
  sentence, such as
  "`Could not start the restore.` is a red notification". The reader
  crosses two sentence ends before reaching the verb.
- A word or phrase the rules name as banned: the banned words, the
  named idioms and hedges, the register swaps, the command verbs, the
  product and interface nouns, the signposting to delete on sight, and
  a shorthand standing in for a technical thing's full name. Matched
  across line breaks. Each finding names the replacement.
- Accumulation: more than two of "actually", "critical", "matters",
  "exactly", "rather than" or "at scale" on one page.
- A precondition true of every page. Anywhere on the page: "you need
  to be logged in", "an authenticated profile" and the other forms of
  the login statement. Inside a Before You Start or Prerequisites
  section only: a profile, a network connection, a shell or an
  account, and a section with nothing in it. Matched by the sentence,
  not the heading, since six of the pages that carried it stated it in
  an unheaded opening paragraph.

Every check skips fenced code, an indented code block, inline code,
double-quoted strings, link targets and HTML comments. A word inside a
quoted product string is the product's word, and stays.

An unclosed fence is reported too, since nothing after it is checked.

Exit 0 when no page has a finding, 1 when one does, 2 when a page
could not be read or no page was given.
"""

import pathlib
import re
import sys

from indent import indented_code_lines

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
    # "every" and "each" are left out: "once every hour" is a
    # frequency, not a clause about time, and "when every hour" is
    # nonsense. The participles catch the elliptical "Once enabled,".
    (r"once (?:the|you|a|an|it|that|this|they|there|all|both|your|its|"
     r"enabled|disabled|created|deleted|complete|completed|started|"
     r"finished|done|ready|applied|set)",
     "temporal \"once\", use \"when\""),
    (r"(?:can|could|will|may|might) \w+ more of them",
     "register, name what there is more of"),
    (r"verbs?", "use \"command\""),
    # Not "exit status N": "status" between "exit" and the number means
    # the full name is already there. A quoted or coded literal such as
    # `exit 1` or "exit 1" is masked before this ever runs.
    (r"exits? \d+", "shorthand, use \"exit status N\""),
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

# A precondition true of every page, stated anywhere on it. These are
# the sentences pgEdge/pgedge-cli#520 removed from 21 pages after the
# rule in writing.md, loaded on every job, produced no edit and no
# report three times out of three (ant-personal#14). The login command
# itself sits in inline code, so it is masked; what these match is the
# prose around it.
UNIVERSAL = "universal precondition, true of every page: delete it"
PRECONDITION = [
    # The subject is "you": "the role must be logged in to the source"
    # describes a role, not the reader.
    (r"you (?:need to|must|have to|will need to|'ll need to|should) "
     r"(?:already )?(?:be )?(?:logged in|log in|logged on|log on|"
     r"signed in|sign in|authenticated?)", UNIVERSAL),
    (r"you (?:need|will need|'ll need|must have|should have) an? "
     r"(?:authenticated|logged-in|active|valid|working) "
     r"(?:profile|session|login)", UNIVERSAL),
    (r"an authenticated profile", UNIVERSAL),
    # Not "authenticate with": that is the generated Short text of
    # `auth login` on the reference page.
    (r"authenticate (?:first|before)", UNIVERSAL),
    (r"creates the profile (?:that )?every command", UNIVERSAL),
]

# Inside a Before You Start or Prerequisites section only: the four
# entries writing.md names as never page-specific. Elsewhere on a page
# "a network connection" may be the subject, so these do not run
# page-wide.
SECTION_HEADING_RE = re.compile(
    r"^\s*#{2,6}\s+(?:before you (?:start|begin)|prerequisites?)\s*:?\s*$",
    re.I)
SECTION_ONLY = [
    (r"(?:an? |the )?(?:authenticated|active|logged-in) profile",
     UNIVERSAL),
    # "a network connection" is the rule's own example; "network
    # access" is the title of the guide these sections link to.
    (r"an? (?:working |stable )?(?:network|internet) connection",
     UNIVERSAL),
    (r"an? (?:supported |working |unix |posix )?shell"
     r"(?! variable| session| script| prompt| function)", UNIVERSAL),
    (r"an? (?:pgedge |starfleet )?account\b", UNIVERSAL),
    (r"(?:logged|signed|log|sign) (?:in|on)", UNIVERSAL),
]


def compile_rules(rules):
    return [(re.compile(r"(?<![\w-])" + pat.replace(" ", r"\s+") +
                        r"(?![\w-])", re.I), advice)
            for pat, advice in rules]


NAMED_RE = compile_rules(NAMED + PRECONDITION)
SECTION_RE = compile_rules(SECTION_ONLY)

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


def named(lines, section_lines=()):
    """Named words and tics over the checked lines, across line breaks.

    section_lines holds the line numbers inside a Before You Start
    section; SECTION_RE runs over the same joined text and keeps only a
    match starting on one of them, so a phrase both rule sets match is
    deduplicated once, in one offset space.

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

    found, spans = [], []
    for rx, advice in NAMED_RE:
        for m in rx.finditer(joined):
            spans.append((m.start(), m.end(), advice))
    for rx, advice in SECTION_RE:
        for m in rx.finditer(joined):
            if where(m.start())[0] in section_lines:
                spans.append((m.start(), m.end(), advice))
    # Two rules matching one stretch of text ("you need to be logged
    # in" and "be logged in") is one finding, the longer one.
    for start, end, advice in spans:
        if any(s <= start and end <= e and (s, e) != (start, end)
               and a == advice for s, e, a in spans):
            continue
        n, col = where(start)
        word = " ".join(joined[start:end].split())
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


def sections(lines):
    """Split the checked lines into Before You Start sections.

    Returns (heading line number, [(n, raw), ...] body) per section
    whose heading SECTION_HEADING_RE matches. The body runs to the next
    heading of any level. The lines are the checked ones, so a fence or
    an indented command inside the section is already gone from it.
    """
    out, current = [], None
    for n, raw in lines:
        if re.match(r"^\s*#{1,6}\s+\S", raw):
            current = None
            if SECTION_HEADING_RE.match(raw):
                current = (n, [])
                out.append(current)
            continue
        if current is not None:
            current[1].append((n, raw))
    return out


def check(text):
    findings = []
    checked = []
    code_lines = indented_code_lines(text)
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
        if n in code_lines:
            continue
        checked.append((n, raw))
        for col, word, us in spelling(mask(raw)):
            findings.append((n, col + 1,
                             f"British spelling \"{word}\", "
                             f"use \"{us}\""))
        for m in OPENER_RE.finditer(raw):
            findings.append((n, m.start(1) + 1,
                             f"sentence opens on {m.group(1)}, a "
                             f"complete sentence of its own"))
    section_lines = set()
    for heading, body in sections(checked):
        if not any(raw.strip() for _, raw in body):
            findings.append((heading, 1, "Before You Start is empty: "
                                         "carry no section"))
        section_lines.update(n for n, _ in body)
    findings.extend(named(checked, section_lines))
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
