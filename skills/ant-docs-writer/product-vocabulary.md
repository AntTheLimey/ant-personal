# Settled product wording

These are decisions, not preferences. Apply them and do not reopen
them. They are here rather than in a separate rules file so that a
writer never has to hold two documents open at once.

## Backups

**Describe a backup kind by its outcome, never by its mechanism.**

- A **hot** backup is the fastest to restore from.
- A **durable** backup is kept apart from the database's own storage,
  and is slower to restore.

The words "volume", "object storage", "base backup", "snapshot" and the
names of backup engines do not appear. What a durable backup survives
is not published, so state nothing about it.

## The Cloud and Enterprise boundary

The two are separate stories and never appear in one page.

- **Cloud** is the console, the API and the managed service behind
  them. No on-premises, air-gapped, Kubernetes or virtual-machine
  deployment appears in Cloud material.
- **Enterprise** is where self-managed deployment lives, and where the
  Control Plane is a customer-facing thing rather than an internal one.

The Control Plane does not appear in Managed copy at all.

## The limits of Managed

Where a reader reaches for one of these, say plainly what to do
instead, and never invent a workaround.

- The platform publishes no certificate authority through the CLI or
  the API. Connections are encrypted at `sslmode=require`, which does
  not check the server's certificate or its host. The stricter libpq
  modes are the client's own to add against its own trust store, so
  never write a recipe that depends on a CA the platform hands out.
- Read replicas and branching are not described. A feature carrying a
  "Coming soon" badge gets no explanatory text.

## Network access

Managed databases have a source-IP allowlist. A database accepts a new
connection only from an address on it, a new database is closed, and
each deployed service has a list of its own. Any page whose reader
connects from outside says which address needs a rule.

Do not route a reader who wants network isolation to the self-managed
product on the grounds that Managed cannot do it.

## AI services

For retrieval and model-serving features, say what the feature does,
what it needs, and how to reach it. Say nothing about authentication in
either direction: "secured", "protected" and "authenticated" do not
appear.

## The name of the product

**The product is pgEdge Starfleet. The word "Starfleet" never appears
without "pgEdge" in front of it.** Not in a heading, not in prose, not
in a link, not in alt text, not after the full name has already been
used once. There is no short form of the product name.

**pgEdge Cloud is retired.** It was the previous name for this product
and it does not appear in anything newly written. Where the interface
still renders it, the interface is stale: write the current name and
raise the string as a defect.

The two editions take the full name and then a short form:

- **pgEdge Starfleet Managed**, shortened to **Managed**.
- **pgEdge Starfleet BYOC**, shortened to **BYOC**.

Use the full edition name on its first appearance in a page, and the
short form after that, but only within the pgEdge Starfleet
documentation, where the reader already knows what they are reading.
Anywhere else, the edition keeps its full name every time.

**A command is code, not a name.** `pgedge starfleet managed database
list` is typed exactly as the command is spelled, lowercase and without
"pgEdge" in front, because it is a string the reader types rather than
a reference to the product. The same holds for a repository name, a
package name and a configuration key.

## Other product names

These are proper nouns and take no article: pgEdge Enterprise Postgres,
pgEdge Distributed Postgres, pgEdge Postgres MCP Server, pgEdge RAG
Server, pgEdge Anonymizer, pgEdge Docloader, Spock. The one exception is
**the Control Plane**, which always takes one.

Write "Postgres", not "PostgreSQL". Write "Managed", not "PAYG", unless
the badge on screen already reads PAYG, in which case quote the badge.

## Console vocabulary

The console has no settled vocabulary, and the shipped pages show it.
`creating_managed.md` calls one object a dialog in its opening and a
wizard in its troubleshooting section. Across the documentation, pane
outnumbers panel 99 to 13, and popup outnumbers dialog 22 to 15 for
the same kind of object. Pick from this list and use one word for one
thing for the whole page.

- A **pane** is a region of a page that stays on the page. Not panel.
- A **section** is a labeled region inside a dialog or a wizard. Pane
  is for a page, section is for what sits inside an overlay, and
  neither is panel.
- A **screen** is what fills the window when the reader is not in a
  dialog: the welcome screen, the sign-in screen. A **page** is a
  screen with a navigation entry and a URL.
- A **dialog** is an overlay that takes focus and must be completed or
  dismissed. Not popup, not modal, both of which name the same object
  and one of which is too informal for this register.
- A **wizard** is a dialog with numbered steps. Use it only where the
  steps exist, and use dialog for the single-screen case. A page that
  needs both words is describing two objects, so say which is which.
  One of its steps is a **wizard step**, named that way so it cannot be
  confused with a numbered step in your own procedure. Do not number
  your steps to match the wizard's: number the reader's actions, and
  name a wizard step only where the reader must recognize it on screen.
- A **tab** switches the content of a pane without leaving the page.
- A **card** is a bordered block holding one resource or one summary.
- A **banner** spans the top of a page or a pane and reports state. A
  **notification** appears, is transient, and can be dismissed.
- A **drop-down** is hyphenated, always. Never dropdown.
- A **field** takes typed input. A **toggle** has two states. A
  **button** is selected, per the standard verb list in `SKILL.md`.
- A **tooltip** appears on hover or focus and holds no instruction the
  reader must have.
- A **badge** is a small marker on a row or a card reporting one
  attribute, such as a backup's kind or a "Coming soon" label. Not tag,
  not chip, not pill.
- A **row** is one entry in a pane that lists things. Not entry, not
  item. A **card** is the bordered form of the same thing.
- A **progress bar** shows how far a running operation has gone. A
  **step list** is the list of stages beside it, and one of those is a
  **stage**, never a step, so it cannot be confused with a step in your
  own procedure.

Two of these overturn current usage on purpose: pane wins over panel
even though both are in the corpus, and popup is retired in favor of
dialog even though it is the more common of the two, because the
register is formal and popup is not.

**This list is inert on a command-line page.** A page with no console
object on it takes none of these words and needs none of them.

## Replication and diagnostics

Replication lag has its own analyses, and they are read in pairs
because either alone is ambiguous.

- An empty lag reading beside a slot that is inactive and holding a
  large amount of write-ahead log means the replica is gone and the log
  is still being retained for it.
- An empty lag reading on its own is the ordinary result on a database
  with no replicas.
- A subscriptions reading is empty on a database using the pgEdge
  replication extension, which keeps its own catalog. An empty result
  there is never evidence that replication is broken.
