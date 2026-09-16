# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

### Changed

- **The edit job is renamed restyle**, and stays the fast, cheap job:
  wording only, facts and section order untouched.
- **The fact set and the claim-to-source list merge into one fact
  list.** Each entry carries the fact, its source, its disposition on
  an overhaul (keep, adapt or drop), and, once drafted, the heading it
  landed under.
- **The heading tree splits into a short form and a full form.** A
  restructure and an overhaul write the short form, headings only, no
  rationale line. A new page writes the full form, one line per
  heading saying what it establishes.
- **The screenshot check runs on what a page states, not on whether it
  carries an image.** A page that shows a screenshot but describes
  nothing on it no longer gets the check.
- **`check-ledger.py` strips double-quoted strings the same as a code
  span.** On the PR #27 page this dropped its n5 count against the
  ledger from 2 shared sequences to 0 on quote stripping alone, and
  its n4 count from 8 to 3, with the remaining 3 passing under a
  four-line allow file. The brief's own title sequences pass the same
  way. A positive control held: the rejected 1.3.0 page against its
  original still fails at 339 shared sequences.

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
