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
