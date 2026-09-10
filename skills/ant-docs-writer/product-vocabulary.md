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

## What Managed does not offer

Say so plainly rather than inventing a workaround.

- There is no network allowlist and no published certificate authority.
  Route a reader who needs network isolation to the self-managed
  product, and never write a certificate-verification recipe.
- Read replicas and branching are not described. A feature carrying a
  "Coming soon" badge gets no explanatory text.

## AI services

For retrieval and model-serving features, say what the feature does,
what it needs, and how to reach it. Say nothing about authentication in
either direction: "secured", "protected" and "authenticated" do not
appear.

## Product names

These are proper nouns and take no article: pgEdge Cloud, pgEdge
Enterprise Postgres, pgEdge Distributed Postgres, pgEdge Postgres MCP
Server, pgEdge RAG Server, pgEdge Anonymizer, pgEdge Docloader, Spock.
The one exception is **the Control Plane**, which always takes one.

Write "Postgres", not "PostgreSQL". Write "Managed", not "PAYG", unless
the badge on screen already reads PAYG, in which case quote the badge.

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
