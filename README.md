# ant-personal

Personal productivity skills for Claude. Voice-matched writing, a
documentation style for the pgEdge repositories, blog creation with
automated review, and executive document review simulation.

## Skills

| Skill | Description |
|-------|-------------|
| **ant-voice-writer** | Write in Ant's voice across professional, creative, academic, and personal contexts. Covers JIRA stories, framing docs, marketing copy, fiction, poetry, worldbuilding, and analytical essays. Not used for product documentation. |
| **ant-docs-writer** | One documentation style for every page a customer or an agent reads, across pgedge-cli and product-ui. A content checklist that runs before any prose rule, plus prose rules derived from ASD-STE100. |
| **blog-creator** | End-to-end blog creation workflow: topic exploration, vault research, voice-matched drafting, automated review, user feedback for voice skill improvement, and final polish. |
| **executive-review** | Simulate C-suite executive reviews of product documents, individually or as a structured committee debate that converges on consensus. |

## Installation

```
/plugin marketplace add AntTheLimey/ant-personal
/plugin install ant-personal
```

## Releases

Versioning is automatic. The `version` field in
`.claude-plugin/plugin.json` is the single source of truth (SemVer).

To cut a release:

1. Bump `version` in `.claude-plugin/plugin.json`
2. Add a matching entry to [`CHANGELOG.md`](CHANGELOG.md)
3. Merge to `main`

On merge, `.github/workflows/release.yml` reads the version, and if the
tag `v<version>` does not already exist, builds per-skill zips and
publishes a GitHub Release with generated notes. Merges that don't bump
the version produce no release.

## License

[MIT](LICENSE)
