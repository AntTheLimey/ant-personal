# The ledger

Dispatch a separate agent to build the ledger from the old page
before any writing starts — the writer never reads that page. The
ledger records what the old page covered, never what is true, and
stays apart from the fact list. Never let an entry cross from ledger
to fact list without being settled against source first.

The writer never reads the old page, not once, not for reference —
read the ledger instead. Filter the excluded page out of every glob
search too, not just avoid opening it directly: a search that returns
it is exposure just the same.

An entry is three fragment lines: a note under ~15 words, the source
file:line, and a status:

| Status | Means |
|---|---|
| V | Verified against something other than a hand-written page. The generated reference is exempt from that exclusion; a sibling docs page is not. |
| C | A spec description a measurement contradicts — a measurement outranks upstream documentation. |
| U | Unverified. |
| S | (situation, as stated on the old page) |

Write an entry as the situation, never as the missing thing: framed
as an absence, it reaches the page as an absence, and no gate can see
it.

Group by topic, sort headings and entries alphabetically, number from
F1 in that order — and say so to the writer: this order carries no
editorial judgment and must not be followed as the page's order.
