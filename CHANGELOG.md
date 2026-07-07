# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

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
