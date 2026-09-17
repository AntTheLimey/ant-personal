#!/usr/bin/env python3
"""Classify which lines of a Markdown page are an indented code block.

A four-space indent is code only relative to what contains it. At the
top level the container column is 0, so a bare four-space indent is
code, same as a page with no lists at all. Inside a list item, the
item's own text sits at the column where the marker ends: only a
further four columns past that is a nested code block. This docset
writes a step's prose at the first column and the step's command at
the second, and check-mechanics.py and signals.py both need to tell
the two apart the same way, hence this shared helper.

    from indent import indented_code_lines

indented_code_lines(text) returns the 1-based line numbers that are an
indented code block. A fenced (``` or ~~~) block is tracked only so a
line that looks like a list marker inside one is never mistaken for a
real list; a fenced line itself is never returned, since each caller
already has its own fence handling.
"""

import re

FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
LIST_MARKER_RE = re.compile(r"^(?:[-*+]|\d+[.)])(?: +)")


def indented_code_lines(text):
    code = set()
    stack = []  # content column of each open list level, outer to inner
    fence = None
    for n, line in enumerate(text.splitlines(), 1):
        m = FENCE_RE.match(line)
        if fence:
            if (m and m.group(1)[0] == fence[0]
                    and len(m.group(1)) >= len(fence)
                    and not m.group(2).strip()):
                fence = None
            continue
        if m:
            fence = m.group(1)
            continue
        if not line.strip():
            continue
        if line.startswith("\t"):
            code.add(n)
            continue
        indent = len(line) - len(line.lstrip(" "))
        while stack and indent < stack[-1]:
            stack.pop()
        baseline = stack[-1] if stack else 0
        marker = LIST_MARKER_RE.match(line[indent:])
        if marker and indent < baseline + 4:
            stack.append(indent + len(marker.group(0)))
            continue
        if indent >= baseline + 4:
            code.add(n)
    return code
