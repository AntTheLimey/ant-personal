# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

### Changed

- **The two-line register directive now lives in the file**, quoted,
  where a writer meets it before any other rule. It had been
  prepended by hand on every dispatch.

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
