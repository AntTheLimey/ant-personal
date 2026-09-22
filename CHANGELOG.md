# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.4.10] — 2026-09-22

### Changed

- **Cold read is batched and moved to a cheaper model.** Previously
  one dispatch per page, reloading style-standard.md from scratch
  each time; a doc-set run now gets one dispatch per batch of up to 6
  pages, read once in navigation order, with findings tagged by page
  path. Dispatches on Haiku by default — a bounded, mechanical
  match-against-a-style-guide task with no repository context to
  reason over — escalating to Sonnet only where Haiku's output is
  unreliable. Neither lever is locked to any measured number yet;
  both need a real restyle batch to validate.
- **Second compression pass on the skill's markdown**, after 1.4.9's
  first pass only moved wording around instead of cutting it (a "see
  CHANGELOG.md" pointer sentence was itself called out as the same
  kind of filler). This pass converts prose mappings to tables and
  arrows and cuts words while preserving every rule and its
  disambiguating example. Measured word count, `skills/ant-docs-writer/*.md`:

  | File | Before | After |
  |---|---|---|
  | reviews.md | 1441 | 1147 |
  | style-standard.md | 1209 | 1079 |
  | gates.md | 973 | 845 |
  | facts.md | 1084 | 1004 |
  | product-vocabulary.md | 860 | 804 |
  | writing.md | 3065 | 2990 |
  | shape.md | 695 | 693 |

  Total 10,645 → 9,880 words (-7%) across the markdown files;
  `SKILL.md`, `agent-pages.md` and `in-app-copy.md` were already
  tight enough that no cut was worth making. `writing.md`'s cut is
  the smallest of the group: its density is mostly inherent — one
  rule per line, each with a disambiguating example — not padding.

## [1.4.9] — 2026-09-22

### Changed

- **Meaning check is a self-read, not a dispatched agent** (#26).
  1.4.8 kept it as a separate agent on a five-restyle sample where it
  found two real defects (a flattened field name, a register slip
  carrying a fact) at roughly a third of the cold read's cost. A later
  16-page batch reversed that: the same agent, dispatched once and
  measured, cost 74,356 tokens and found nothing, while the writer
  reading the diff themselves — already happening ad hoc on the
  batch's other pages — caught that batch's one real regression (a
  wrong flag name). Both real defects across both samples were a
  same-length wrong value swapped for a right one, which a
  size-mismatch script heuristic would not reliably flag, so the fix
  is doing the read yourself rather than building a cheaper automated
  stand-in for it.
- **Cold read carries an already-filed, cross-page finding forward**
  instead of rediscovering it on every page of a doc-set run (#22). A
  pattern flagged once and tracked as its own issue is named in later
  dispatches within the same run so it isn't independently
  re-derived, at full dispatch cost, on every page that repeats it.
- **The Verbs table's ambiguous "Flag" row is split** (#23). One row
  covering two constructions ("pass" and "sets a value") produced
  false positives against an established, pervasive convention this
  doc set already uses ("`[Command]` takes `[Flag]`") and against
  "`[guide]` covers `[topic]`" (misread as the provides-not-covers
  idiom rule, which governs a feature's own behavior, not a
  document's content). Both are now named as explicit non-violations.
- **`check-mechanics.py` gates the "exit N" shorthand** (#25).
  style-standard.md already named the rule ("exit status N", not
  "exit N"); a cold read was hand-finding it repeatedly at full agent
  cost. Added as a `NAMED` entry, the same way "verb" -> "command"
  already is.
- **Removed internal history from the skill's own instruction files.**
  `writing.md` tells a writer never to leave a page carrying "no
  issue/PR numbers... dates... measured... attempt counts"; several of
  the skill's own operating files (`style-standard.md`,
  `product-vocabulary.md`, `gates.md`, `facts.md`, `reviews.md`,
  `check-mechanics.py`, `check-ledger.py`, `check-sources.py`) were not
  holding themselves to that rule, carrying dated measurements, issue
  numbers, page names and incident narratives inline in files loaded
  on every job. Cut down to the current rule; the evidence for each
  one is in this changelog instead.

## [1.4.8] — 2026-09-21

### Changed

- **Cold read no longer follows a page's outbound links** (#18). In
  the 2026-09-21 restyle run the cold read was the largest single
  spend, and 18 of them running in parallel had to be killed; on a hub
  page that meant five to eight extra pages fetched for a check whose
  job is only to find where a reader of the page itself gets lost. It
  now reads the page and `style-standard.md` alone, and reports a link
  the reader needs to act on as an unanswered question instead of
  following it.
- **A restyle keeps its meaning check, and now runs it before the cold
  read instead of in parallel** (#19). Measured across five completed
  restyles, the meaning check caught two real defects — a flattened
  field name and a register slip that carried a fact — at roughly a
  third of the cold read's cost, a rate no cheaper substitute (a
  writer's own read-back, a numeric/condition/hazard gate, or a
  per-batch check) would have reliably matched. Running it first means
  the cold read only ever reads text the meaning check has already
  settled, instead of reading a draft that a wrong-fact fix is about
  to change.

## [1.4.7] — 2026-09-18

### Added

- **`style-standard.md` states the spelling standard** (#11). pgEdge
  documentation is US English, set by the public docs repository and
  measured 2026-09-18 (behavior 34 to 2, color 43 to 1, initialize 17
  to 0, center 8 to 0); the pgedge-docs skill's own prose is US too.
  pgedge-cli's British docset ("behaviour" 43 to 1) is the outlier, so
  the gate keeps its rule and a writer is told not to read the page
  in hand as evidence against it. A British word in link text is
  fixed by retitling the target page and every link to it together;
  when the target is outside the change, it is the one finding any
  job reports and leaves, and `gates.md` names the exception. Two
  writers on pgEdge/pgedge-cli#520 changed link text alone and both
  edits were reverted. This replaces 1.4.5's "noted, not changed".

## [1.4.6] — 2026-09-18

### Added

- **`check-mechanics.py` gates the Before You Start rule** (#14). A
  precondition true of every page is a finding: the login statement
  in any of its wordings ("you need to be logged in", "you need an
  authenticated profile", "creates the profile every command below
  uses") anywhere on the page, and, inside a Before You Start or
  Prerequisites section, a profile, a network connection, a shell, an
  account, or an empty section. Matched by the sentence, not the
  heading, since six of the pages that carried it stated it in an
  unheaded opening paragraph. Measured against pgedge-cli's docs as
  they stood before pgEdge/pgedge-cli#520: 19 pages carried the
  statement and the gate flags all 19 (#520 touched two more for
  other reasons); on current `main` and on the five shipped skills it
  flags nothing, and the other four checks' 208 findings on those 21
  pages are byte-identical between the old script and this one. "Authenticate with" is deliberately not
  matched: it is the generated `auth login` Short text on the
  reference page.
- Two rules matching one stretch of text ("you need to be logged in"
  and "be logged in") now report once, as the longer match.

### Changed

- **`product-vocabulary.md` no longer lists branching as unreleased.**
  pgEdge/pgedge-cli#523 shipped the `database branch` commands and
  their reference page, and #525 the skill workflows, so the negative
  the 1.4.5 review-trigger note asked writers to re-check had gone
  stale within a day. Read replicas stay on the list.

## [1.4.5] — 2026-09-17

### Fixed

- **`check-mechanics.py` and `signals.py` now agree on what an
  indented block is**, via a shared `indent.py` classifier. Code is
  whatever sits four columns past its container's own content column
  — four past 0 at the top level, four past a list item's marker
  inside one — rather than a flat four-space rule. Previously
  `check-mechanics.py` read every indented shell command as prose
  (pgEdge/pgedge-cli#520 edited a literal `postgresql://` string to
  clear a spelling finding on one), and `signals.py` stripped a
  step's own indented prose along with its code, scoring a
  step-heavy page on a fraction of itself.
- **`check-sources.py` accepts a dated probe log under `research/`**
  as a source for a ledger entry marked `st: V`, alongside the
  existing exemption for generated reference pages. It previously
  rejected the strongest source a ledger entry can have — a live
  measurement — on the same grounds as a sibling guide citing
  nothing.
- **`product-vocabulary.md` flags its own negative claims** (the
  missing certificate authority, an unreleased feature) for a check
  against the current product before a new page repeats one. A
  feature shipping does not fail the gate the way a wrong word does.

### Noted, not changed

- `check-mechanics.py`'s US-spelling rule stays as written. The
  pgedge-cli docset's prose is measurably British (`behaviour` 43:1,
  `catalogue` 22:0, `analyse` 20:3), so the rule keeps producing a
  false "fix" on a restyle of an old page until the docset itself is
  swept to US English in a dedicated pass.

## [1.4.4] — 2026-09-17

### Added

- **A rule against the temporal "once"**, in `style-standard.md` and
  in `check-mechanics.py`: write "when the restore completes", not
  "once the restore completes". The counting sense ("returned once, at
  creation") stays, so the gate matches "once" only where a clause
  about time follows it. Across the 88 pages of both docsets, "once"
  appears 109 times and the gate flags 53, every one of them a
  temporal clause. It is deliberately incomplete: a temporal "once"
  followed by an inline-code span or a proper noun is missed, and
  "once every hour" is left alone because it states a frequency.
- **ASD-STE100 rule 3.7**, in `writing.md`. The provenance record
  listed it as taken unchanged, but no rules file ever carried it.

### Changed

- **`ste-adoption.md` moves to `docs/`.** No job loaded it and no file
  referenced it, so it shipped in every install unreachable. It is a
  provenance record, not a rule, and it now says so. The skill payload
  drops from 60,226 B to 55,194 B. Per-job load does not drop: a restyle
  reads 672 B more than it did, because the rules this release adds
  and the contradiction it resolves cost more text than the duplicates
  removed.
- **The two orderings that are always wrong are stated once**, in
  `writing.md`. `shape.md` now points at them instead of repeating
  them.
- **The readability bounds are stated once**, in `writing.md`.
  `gates.md` described the same floor and ceiling, so either could
  drift from the other.
- **The content checklist is eight items, numbered 1 to 8.** Item 1b
  was a separate requirement wearing item 1's number.

### Fixed

- **A fix job could not satisfy `gates.md`.** Its opening rule said a
  failing gate means the page is not done; the carve-out under
  `check-mechanics.py` said to leave findings in untouched sentences
  alone. Both bind a fix, so the gate could never pass. A fix is now
  named as the one job that ends on a failing gate.
- **The fix job is no longer written for exactly one claim.**
  `facts.md` and `SKILL.md` described "the one changed claim"
  throughout, leaving a brief carrying three corrections undefined.
  Found by running a three-claim fix.
- **`facts.md` no longer opens by explaining restyle and
  restructure**, neither of which loads it.

## [1.4.3] — 2026-09-16

### Changed

- **SKILL.md splits into eight files, each loaded only by the jobs
  that need it**, in place of one 1,695-line, 88,848-byte file every
  job read in full:

      SKILL.md            4,962 B  top rule, conflicts, jobs, ships, reading
      style-standard.md   5,509 B  Register, Words
      writing.md         17,787 B  sentences through repository mechanics
      shape.md            4,160 B  checklist, shape, openings
      facts.md            6,110 B  sources, never invent, two artifacts
      gates.md            4,031 B  the gates
      reviews.md          4,872 B  reviews
      in-app-copy.md      1,129 B  in-app copy

  SKILL.md is now the router: a load list names the files each job
  reads, and "What ships with the draft" requires the files read as
  the first item in the hand-back. Every cross-reference that used to
  say "above", "below" or "this file" now names the file the rule
  moved to. A restyle loads SKILL.md plus style-standard.md,
  writing.md, gates.md, product-vocabulary.md and reviews.md: 41,519
  bytes, against 105,938 bytes for the whole 1.4.2 skill. A 1.4.2
  restyle measured 16.5 minutes, 6.6 of them before the first draft,
  loading a 106 KB skill of which a restyle uses only part. Nothing is
  re-measured yet: this release does not claim a speed-up.
- **The cold reader and the correctness reviewer get style-standard.md
  handed over unchanged, never an extract.** Three places in
  reviews.md used to instruct an agent to copy out `## Register`
  through the end of `### Constructions that read as a machine`, plus
  the quoted-product-string exemption; all three now hand over the
  file whole. The exemption itself moved into style-standard.md, out
  of a bullet under writing.md's `## Sentences`, so the handed-over
  file carries it.
- **check-mechanics.py gates the words and constructions the rules
  name outright**, not only spelling and a quoted-sentence opener. It
  checks the banned words, the named idioms and hedges, the register
  swaps, the command verbs, the product and interface nouns, and the
  signposting to delete on sight, from style-standard.md and
  writing.md, matched across line breaks, plus the accumulation limit
  of two per page. Masked spans block a phrase match, so "the `app`
  user" is not "the user". On the 1.4.2 restyle's input page it
  reports the cold read's two findings and nine it missed: six
  "popup", two "a way back" and a third "rather than". On its output
  it reports the eight "popup" the writer kept.
- **check-mechanics.py masks a quoted string or code span wrapped
  across a line break, and joins a phrase match at a barrier no
  paragraph gap crosses.** A quoted string or code span broken at 79
  columns was masked line by line, so a banned word inside it was
  flagged; a phrase could also match across a blank line, a skipped
  fence or a skipped comment. "more of them" no longer flags "one or
  more of them": the rule now needs the modal-verb construction it
  names. "load-bearing" is gone, having no rule in the skill; the
  panel advice now names "section" inside a dialog, as
  product-vocabulary.md does; "carried weight", "carrying weight" and
  "and this is why it bites" are added; "this section uses/has" is no
  longer matched. All seven reproducing inputs from the review pass.
  Corpus of 89 pages: 1,347 findings, down from 1,401 before 122eeb0's
  "the user" removal; the restyle input page and the persona-test page
  are unchanged at 14 each.
- **The cold-read report format is fixed, and the fix round starts on
  the first review back.** Measured on the 1.4.2 restyle: the meaning
  check took 1.5 minutes, and the cold read took 5.5 minutes, most of
  it writing the report. The cold-read prompt in reviews.md now asks
  for a first line on task completion, then one pipe-delimited line
  per finding (the quoted sentence, heading or alt text, the kind, and
  the matching detail), with no summary, no praise, and no cap on the
  count. reviews.md also states that the writer applies a review's
  findings as soon as it returns rather than waiting for the second,
  resolves a finding both reviews name in favor of the fact-bearing
  one, and runs the gates once after both are applied. This does not
  claim a speed-up; nothing is re-measured yet.
- **The skill is rebuilt from a 399-rule ledger**, replacing the ten
  hand-edited `.md` files above in place; `ste-adoption.md` is
  untouched. Five rules were dropped as duplicates or restatements of
  an existing gate: R141, R234, R236a, R236b, R238. Total size: from
  104,153 bytes to 54,681 bytes; restyle load (SKILL.md,
  style-standard.md, writing.md, gates.md, product-vocabulary.md,
  reviews.md): from 74,884 bytes to 41,519 bytes.

  An A/B test restyled the PR #27 console backups page once per arm,
  on sonnet, from identical briefs, run in parallel (RESULT.md in the
  `docs_writing/experiments/skill-rebuild/` research directory): OLD
  read the pre-rebuild skill (104,153 B, restyle load 74,884 B), NEW
  read the rebuilt skill (54,647 B, restyle load 41,485 B, before the
  "|" separator below was restored). NEW ties OLD on every quality
  measure scored — words, check-mechanics.py, signals.py ease/grade,
  "popup" count, cold-read report bytes — and reached cold-read return
  in 12.8 minutes against 19.2, 33% faster. n=1 per arm, so the timing
  difference is indicative, not settled; OLD hit its account's session
  limit during its fix round after both reviews had returned, so OLD's
  fix round and token count were not measured. The A/B run surfaced
  one defect: NEW's cold-read dispatch had lost the "|" field
  separator that reviews.md's format depends on, restored in
  reviews.md as part of this port.

---

## [1.4.2] — 2026-09-16

### Added

- **Restructure, a job between restyle and overhaul.** Restyle,
  restructure and overhaul are now levels, each adding one layer to
  the one below: restyle rewrites wording only, restructure adds a
  shape change on top of that (sections added, merged, split or
  reordered, facts taken as the page states them), and overhaul adds
  re-establishing every fact from source on top of both. The 1.4.1
  rebuild of the PR #27 page took 34 minutes, most of it rewrite
  passes against a phrase gate that could not pass on the page's own
  UI labels and product terms, for a page that only needed its wording
  and shape changed, not a full fact re-check.
- **A meaning check, run on restyle and restructure.** A separate
  agent compares the old page against the new one and reports every
  fact added, dropped or changed, without commenting on style. Neither
  job re-verifies against source, so nothing else was watching for a
  fact that moved or dropped during a rewrite.
- **`--allow` on every `check-ledger.py` invocation, and the allow
  file that ships beside a draft.** A phrase the page must repeat,
  such as its title, a product term or a label as the screen spells
  it, is listed there once and excused, rather than rewritten pass
  after pass chasing a gate that could not pass.
- **`check-ledger.py` accepts an allow file that does not exist yet.**
  The first run, before anyone has written one, reports shared
  sequences instead of crashing. A sequence now passes when it lies
  inside an allowed phrase or contains one whole, so a two- or
  three-word product term excuses every longer sequence built around
  it. A trailing `# reason` is a comment, not part of the phrase, and
  a one-word phrase is ignored, because it would excuse every sequence
  containing that word.

### Changed

- **The edit job is renamed restyle**, and stays the fast, cheap job:
  wording only, facts untouched, section order untouched apart from
  one reader-safety move.
- **The fact set and the claim-to-source list merge into one fact
  list.** Each entry carries the fact, its source, its disposition on
  an overhaul (keep, adapt or drop), and, once drafted, the heading it
  landed under.
- **The heading tree splits into a short form and a full form.** A
  restructure and an overhaul write the short form, headings only, no
  rationale line. A new page writes the full form, one line per
  heading saying what it establishes.
- **The screenshot check runs on what a page states and requires an
  image to check it against, not on whether the page carries one.** A
  page that shows a screenshot but describes nothing on it, and a page
  that describes a screen but has no image of it, both skip the check.
- **`check-ledger.py` strips double-quoted strings the same as a code
  span, and unwraps each paragraph first.** Unwrapping means a code
  span or a quoted label broken across the 79-column wrap is still
  stripped whole. On the PR #27 page this dropped its n5 count against
  the ledger from 2 shared sequences to 0 on quote stripping alone,
  and its n4 count from 8 to 3, with the remaining 3 passing under a
  four-line allow file. The brief's own title sequences pass the same
  way. A positive control held: the rejected 1.3.0 page against its
  original still fails, at 343 shared sequences (339 before
  unwrapping).

---

## [1.4.1] — 2026-09-16

### Changed

- **The cold reader gets the style standard.** Three reps without it
  filed 112 findings, 22.3% actionable. Three reps with it filed 78
  findings, 52.6% actionable, at 13.7 actionable findings per rep
  against 8.3. Every reviewer with the standard beat every reviewer
  without it. Deprivation stays scoped to the product, never to house
  style.
- **The cold-read prompt drops the persona sentence.** Its measured
  effect on real findings was about one extra finding across three
  reps in both the deprived and the not-deprived arms, the same
  direction each time and inside the noise at three reps per arm.
  Product deprivation changes what a cold reader finds: zero
  imported-knowledge findings across six deprived reps, fifteen
  across six reps that were not deprived.
- **Alt text and headings are named as in scope for the cold read.**
  Six reviews hunted terminology drift, and none caught "pane" in the
  body against "page" in an image's alt text, because nothing told a
  reviewer to read alt text and headings as page vocabulary.
- **The register is formal technical voice, not semi-formal.** Set at
  the direction of pgEdge's technical writer.

### Added

- **`check-mechanics.py`, a fourth gate script.** No reviewer across
  18 reps caught a British spelling in a US docset, or a sentence
  opening on a quoted string that ends in a period. Across 89 pages in
  pgedge-cli and pgedge-starfleet-docs it found 193 British spellings
  and 14 quoted-sentence openers, with a sample of each spelling word
  and all 14 openers inspected and genuine. Positive control: it found
  all three defects a cold reader missed on the experiment page, two
  instances of "afterwards" and one quoted-sentence opener. Negative
  control: a US word list produced zero findings.
- **A separate check for screenshot claims, resolved against the
  product.** A cold reader has no image access. The defect "the page
  claims a backup ID field the screen does not have" was found by 0
  of 6 deprived reps and 3 of 6 reviewers who could see the product. A
  mismatch between the draft and a screenshot is now settled by
  checking the live product, never by trusting either the prose or
  the image.

---

## [1.4.0] — 2026-09-15

### Removed

- **The linked section index at the top of a page.** MkDocs Material
  renders the heading tree in the right-hand pane, so an inline copy
  was a second navigation that went stale on the first rename. A
  README keeps the option, because GitHub has no such pane. Raised
  twice in review on pgEdge/pgedge-starfleet-docs#27: "we have a
  navigation pane in the upper-right pane for content like this" and
  "we don't use inline TOC's in documentation (except for the README
  file)".

### Changed

- **Before You Start is scoped to the page.** It carried every
  precondition, including the authenticated profile every reader
  already had. It now holds four kinds of entry, all page-specific:
  a value needed before step one with the command or screen producing
  it, a condition specific to this task, an irreversible action
  reachable before its guard, and a console page's starting screen.
  **A page with nothing page-specific carries no such section.**
- **The connection flag is assumed, not stated.** A reader with no
  profile could not have reached a page about restoring their
  database.
- **The page is no longer the subject of its own sentences.** "This
  page covers", "this page uses", "this page has" and "on this page"
  join the delete-on-sight list. Term definitions stay; the
  announcement introducing them goes. Same review: "referring to the
  page is not generally a good practice for technical writing".

### Added

- **A ban on anthropomorphism**, under Register. Software does not
  hold, know, want, see, care, remember, think or decide. The idiom
  rule already covered the class and did not fire on "nothing your
  application holds needs changing", so the case is now named: same
  review, "applications don't have hands. What does that even mean?"
- **The plain-formal-word rule now reaches whole constructions**, not
  only single words. "A restore can report additional steps", not
  "a restore can report more of them".
- **The register rules bind phrasing inherited from the page being
  replaced.** A phrase that arrives through a fact ledger is still
  published under the writer's own name. Both new findings were
  phrasing the rewrite carried over rather than invented.
- **A step whose command changes something says so in that step.**
  This is where the requirement dropped from the page opening now
  lives. The reviewer objected to the claim sitting in the intro
  paragraph, not to its existing, and a reader four minutes past the
  intro is about to run the command.
- **The connection flag is still printed on a destructive step.** It
  answers a different question there: which tenant the command runs
  against, not whether the reader is authenticated. A reader holding a
  profile per environment can otherwise drop the wrong database from a
  command that reads correctly.

---

## [1.3.0] — 2026-09-12

### Added

- **The three gate scripts now ship with the skill.**
  `check-ledger.py`, `check-sources.py` and `signals.py` sit beside
  `SKILL.md` and are invoked from there, rather than being referenced
  without being vendored.
- **The writing pipeline the skill never carried.** A fact set is
  discovered from source; a ledger is extracted from the page being
  replaced and the writer never reads that page directly. Ledger
  entries are three-line fragments marked `V` (verified), `U`
  (unsourced), `C` (contradicted) or `S` (stale), sorted by topic and
  alphabetically within it, numbered from `F1`. The three gates run
  at named points: `check-sources.py` once the ledger is built,
  `check-ledger.py` at `--n 5` and again at `--n 4` once a draft
  exists, `signals.py` before the page is called done.
- **Four source-of-truth questions**, settled before gathering: which
  codebases may be read, what to compare the shape against, whether
  real resources may be created to verify behavior, and where
  measurements are recorded.
- **A fourth job, "new page"**, alongside fix, edit and overhaul, with
  its own rule to write the heading tree down before a word of prose.
- **A section naming constructions that read as a machine** — negative
  parallelism, a repeated sentence skeleton, uniform sentence length,
  and word accumulation — none of which a banned-word list catches.
- **A reading-ease floor of 58 and a Flesch-Kincaid grade ceiling of
  8.0**, both measured by `signals.py` against prose only, with the
  ceiling treated as a tripwire rather than a target to write for.
- **Six gaps closed by an audit**: checking the 25-word cap by running
  `signals.py` instead of reading for it; a three-part order for a
  troubleshooting entry; a README treated explicitly as a page; guides
  placed per edition under `docs/` with the nav entry added in the
  same change; every link checked before a page ships; and the
  claim-to-source list given its own definition.
- **A hand-back section.** A draft ships with the job name, the fact
  set, the heading tree and the claim-to-source list beside it, so the
  stages the skill named as instructions now have somewhere to land.
- **A verdict and an exit status on `signals.py`.** The script prints
  a line per bound saying whether it was met and with what value, and
  exits non-zero when one is crossed. The grade failure says to split
  the sentence rather than drop the clause carrying the condition.

### Changed

- **The two-line register directive now lives in the file**, quoted,
  where a writer meets it before any other rule. It had been
  prepended by hand on every dispatch.
- **`<skill>/` now names the base directory the harness announces**
  when the skill loads, with a fallback for a dispatch that announced
  none. The three usage strings that taught `./script.py` were
  corrected to match.
- **A non-zero exit or a `FAIL` line is a failure to fix** before the
  page is done, rather than a number to report. Each `check-ledger.py`
  run is introduced separately, so the draft cannot be passed in both
  slots.

## [1.2.0] — 2026-09-10

### Added

- **New `ant-docs-writer` skill.** One documentation style for every page a
  customer or an agent reads, across pgedge-cli, product-ui and the Starfleet
  docs. Four files, self-contained, referencing nothing outside the skill
  directory.

  - A seven-item **content checklist** that runs before any prose rule,
    because a page can pass every prose rule and still be unusable.
  - A **precedence order** for when two rules collide: reader safety, the
    content checklist, product truth, then house style, with tie-breaks
    inside house style for the pairs that recur.
  - A **page-shape** section. The three jobs a documentation request can be
    (a fix, an edit, an overhaul) are named, and the skill asks which one it
    is rather than guessing, since a factual correction that arrives as a
    restructured page buries the line a reviewer needed to see.
  - **Marking a step the reader will otherwise skip**, rationed to one or two
    genuinely unrecoverable outcomes a page, written as consequences rather
    than orders.
  - A **cold read** the skill runs itself before calling a page done, with the
    dispatch prompt carried in the file.
  - A prose half derived from **ASD-STE100 Issue 9**, and a settled product
    vocabulary including console nouns.

  Two reference files sit beside it: `ste-adoption.md` records which STE rules
  were taken, adapted or dropped and why, and `agent-pages.md` carries the
  divergences for pages read by agents rather than people.

### Changed

- **`ant-voice-writer` no longer covers product documentation.** "documentation"
  is removed from its trigger list, the description routes docs pages, README
  files, in-app copy and the CLI reference to `ant-docs-writer`, and the skill
  now opens with a section saying so before its voice profile. The skill had no
  technical-documentation mode, so a docs writer landed on its calibration
  note, which says the default is medium-to-long sentences and "if you're
  unsure, write it longer". Blogs, framing docs, JIRA stories, marketing and
  creative work are unaffected.

## [1.1.0] — 2026-07-07

### Added

- **Blog Writing section in ant-voice-writer.** Rules for separating thought
  leadership from product marketing, watching for word accumulation, avoiding
  "breaking change" and vanity-metric language, and detecting structural slop.
- **New banned and accumulation-prone vocabulary.** Banned "breaking change,"
  "moreover/furthermore/additionally," "pivotal/crucial," "testament,"
  "underscore," and more. Added an accumulation watch-list ("at scale,"
  "actually," "matters," "exactly," "critical," "rather than," "in practice")
  where frequency, not the word itself, is the tell.
- **Expanded blog-creator review checklist.** Added negative-parallelism,
  rhetorical-question-plus-micro-answer, tailing-participial-clause,
  fractal-summary, Latinate-bias, and uniform-sentence-length detectors, plus
  a repeated-sentence-skeleton pass and a proven short-sentence-ratio fix.
- **Automated release pipeline.** `plugin.json` is now the single source of
  truth for the version; merging a bump to `main` auto-tags and publishes a
  GitHub Release with per-skill zips via `.github/workflows/release.yml` and
  `scripts/build-skill-zips.sh`.

### Changed

- **Em-dash rule hardened.** Both the voice skill and the review checklist now
  call out em-dash creep during edit passes and require re-checking after
  every round of edits, not just the initial draft.
- **Version removed from `marketplace.json`.** Version now lives only in
  `plugin.json` to avoid drift between the two manifests.

## [1.0.0] — 2026-04-07

### Added

- Initial plugin with three skills: `ant-voice-writer`, `blog-creator`, and
  `executive-review`.
