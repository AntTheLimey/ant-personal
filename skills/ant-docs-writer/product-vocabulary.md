# Product vocabulary

Treat every word choice below as a settled decision to apply, not a
preference to reopen or debate.

A rule saying a feature doesn't exist is different: a negative goes
stale the moment the feature ships, with nothing to fail and warn a
writer. Before repeating one (the missing certificate authority, an
unreleased feature) on a new page, check it against the current
product rather than this file.

## Product and architecture boundaries

- Where the interface still renders the retired name "pgEdge Cloud",
  write the current name on the page and raise the stale string as a
  defect.
- Cloud and Enterprise are separate stories, never on one page. Cloud:
  console, API, managed service — no on-prem, air-gapped, K8s or VM
  material. Enterprise: self-managed deployment, with a
  customer-facing Control Plane.
- The Control Plane never appears in Managed copy at all.
- A command is code, not a name: exact spelling, lowercase, no
  "pgEdge" — same for a repository name, package name or
  configuration key.
- Write "Managed", never "PAYG", unless the on-screen badge itself
  reads PAYG, in which case quote the badge.

## Backups

- Describe a backup kind by its outcome, never its mechanism: a "hot"
  backup is fastest to restore from; a "durable" backup is kept apart
  from the database's own storage and is slower to restore.
- Never use "volume", "object storage", "base backup", "snapshot", or
  a backup engine's name. Never state what a durable backup survives.

## Security and networking

- The platform publishes no certificate authority via CLI or API.
  Connections use `sslmode=require`, which checks neither the
  server's certificate nor its host. Never write a recipe depending
  on a platform-issued CA — stricter libpq modes are the client's own
  to add.
- Managed databases have a source-IP allowlist, scoped separately per
  database and per deployed service. A page whose reader connects
  from outside says which address needs a rule.
- Never route a reader who wants network isolation to the self-managed
  product on the grounds that Managed cannot do it.

## Unreleased features

- Read replicas are not described. A feature carrying a "Coming soon"
  badge gets no explanatory text.

## AI features

- For AI retrieval and model-serving features, say what the feature
  does, what it needs, and how to reach it. Say nothing about
  authentication in either direction.

## Console vocabulary

Inert on a command-line page: a page with no console object takes
none of these words.

| Term | Use for | Never |
|---|---|---|
| pane | A region of a page that stays on the page | panel |
| section | A labeled region inside a dialog or wizard | panel |
| screen | What fills the window outside a dialog |  |
| page | A screen with a navigation entry and a URL |  |
| dialog | An overlay that takes focus and must be completed or dismissed | popup, modal |
| wizard | A dialog with numbered steps | dialog, for the single-screen case |
| tab | What switches a pane's content without leaving the page |  |
| card | A bordered block holding one resource or summary |  |
| banner | A state report spanning the top of a page or pane |  |
| notification | A transient, dismissible state report |  |
| drop-down | Always hyphenated | dropdown |
| field | Typed input |  |
| toggle | A two-state control |  |
| select | The standard verb for a button |  |
| tooltip | Hover or focus text holding no instruction the reader must have |  |
| badge | A small marker reporting one attribute on a row or card | tag, chip, pill |
| row | One entry in a listing pane | entry, item |
| progress bar | How far a running operation has gone |  |
| step list | The stages beside a progress bar |  |
| stage | One entry in a step list | step |

Pane wins over panel, and dialog wins over popup, even though panel
and popup are both common, because the register is formal.

A page needing both "wizard" and "dialog" is describing two objects,
so say which is which. Call one of a wizard's own steps a "wizard
step", and never renumber the writer's own procedure steps to match
the wizard's.

## Replication readings

Read in pairs; either alone is ambiguous.

- Read an empty replication-lag reading beside slot state and WAL
  retention: an inactive, WAL-retaining slot means the replica is
  gone. An empty lag reading alone, with no replicas, is ordinary.
- An empty subscriptions reading on a database using the pgEdge
  replication extension is never evidence that replication is broken.
