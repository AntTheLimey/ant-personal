# What this style takes from ASD-STE100

ASD-STE100 Simplified Technical English, Issue 9, is the foundation for
the prose half of this style. This file records which of its rules were
taken, which were adapted and which were dropped, with rule numbers, so
that nobody has to re-derive the decision from a 434-page standard.

No job loads this file. It records where the rules came from, and the
rules themselves live in `skills/ant-docs-writer/`.

STE is a controlled language written for aerospace maintenance manuals
read by non-native English speakers. Two things follow. Its sentence
and procedure rules transfer to software documentation almost
unchanged. Its controlled dictionary does not.

## Taken unchanged

| Rule | What it says |
|------|--------------|
| 4.1 | Write short and clear sentences. |
| 4.2 | Do not omit words or use contractions to shorten a sentence. |
| 4.3 | Use a vertical list for complex text. |
| 5.1 | A procedure step is 20 words at most. |
| 5.2 | One instruction per sentence, unless the actions are simultaneous. |
| 5.3 | Write instructions in the imperative. |
| 5.4 | Condition first, then a comma, then the command. |
| 5.5 | A note gives information, never an instruction. |
| 6.1 | Give information gradually. |
| 6.2 | Use key words to give the text a logical structure. |
| 6.3 | Descriptive prose is 25 words at most per sentence. |
| 6.4 | Use paragraphs to group related information. |
| 6.5 | One topic per paragraph, opened by a topic sentence. |
| 6.6 | No more than six sentences in a paragraph. |
| 8.2 | Hyphens connect words that are directly related. |
| 9.4 | One wording for one repeated action, throughout. |
| 1.11 | One noun for one thing, throughout. |
| 3.6 | Use the active voice. |
| 3.7 | Describe an action with a verb, not a nominalisation. |

Rule 5.5 also carries the test this style adopts as checklist item 8:
read the procedure with every note removed, and confirm the reader can
still finish it. If they cannot, the note held a step.

Rule 6.2 is the one most likely to be skipped and the one that pays
most. It is what makes capped sentences read as prose rather than as a
list, and neither of the two rules files it replaces had it.

## Adapted

**Rule 4.4, connecting words.** STE encourages And, But and Thus at the
start of a sentence, precisely because it bans the semicolon and caps
sentence length, which removes the alternatives. This style keeps that
reasoning for "But", which has no short substitute, and drops it for
And, So, Or and Yet, which do. The register the pgEdge docs pages are
written in is the reason, and it was a judgment call rather than a
finding.

**Rule 8.1, the semicolon.** STE bans it outright. This style bans it in
new text and never strips one from existing text, because a
punctuation-only edit hides the technical change underneath it in
review.

**Rules 8.4 to 8.7, word count.** The operative version of this now
lives in `skills/ant-docs-writer/writing.md`, because a writer should
not have to open a second file to know how to count. What follows is
why it is generous.

STE's counting method is what makes the 20 and 25 word caps checkable,
and it is generous in the way this work needs. A number counts as one
word. An abbreviation counts as one
word. Quoted text counts as one word, so a backticked command counts as
one however long it runs. Parenthetical text counts as one word. A
hyphenated word counts as one. Without this, no sentence containing
`pgedge starfleet managed database rotate-password` could fit in a step.

**Section 7, safety instructions.** Nothing in this documentation risks
injury, so "warning" and "caution" in STE's sense do not apply. The
structure does. A destructive command gets the command or the condition
first, then a sentence saying what is lost and whether it can be
recovered. Rule 7.3, give the risk and not just the prohibition, is why
"a restore has no undo" is followed by what to do instead.

**Rule 9.3, phrasal verbs.** STE bans them because two words together
can carry a meaning neither word has. Kept as a caution rather than a
ban: prefer "configure" to "set up", and never write "setup" where a
verb is meant.

**GR-1, the conjunction "that".** STE recommends writing "make sure
that the valve is open" rather than "make sure the valve is open",
because the conjunction marks where the main clause ends. Adopted as a
preference. It costs one word and removes a re-read.

## Dropped

**The controlled dictionary, Part 2, roughly 2,700 approved words.**
Not enforceable here without a checker, and it would not have caught
the faults it was being considered for. Every undefined term on the
page that prompted this work was a Technical Noun, which STE permits
freely under rules 1.5 and 1.6. The vocabulary problem this style
actually has is one word doing four jobs on a single page, and rules
1.11 and 9.4 catch that without the dictionary.

**Rules 1.2 to 1.4, and 3.1 to 3.5, approved parts of speech, verb
forms and tenses.** These exist to serve the dictionary. Without it
they have nothing to check against.

**Rules 1.5 and 1.12, technical noun and verb categories.** Same
reason.

## Where STE has nothing to offer

STE is a prose standard, and every item on the content checklist sits
outside it. A page can obey all sixty-odd STE rules and still print a
command the reader cannot run, ask for a value it never says how to
find, raise a question in its opening that it never answers, and
destroy in one step what a later step tells the reader to retype. That
is not a criticism of STE. It is the reason the checklist runs first.
