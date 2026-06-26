# Professional Document Patterns

## JIRA Stories

### Structure
1. Title: Verb-first, specific ("Deploy MCP Server to pgEdge Cloud", not "MCP Server Work")
2. Description: Context paragraph (2-3 sentences), then requirements
3. User Story: "As a [persona], I want [capability], So that [value]"
4. Acceptance Criteria: Max 4, each one sentence, testable
5. Notes/Dependencies: Only if blocking

### Example Voice
> As a pgEdge Cloud customer, I want to deploy an MCP Server alongside my database cluster, So that I can enable agentic AI applications to interact with my data without managing additional infrastructure.

### Rules
- Separate API and UI stories — don't combine them
- No code snippets in stories
- Non-prescriptive on implementation — state the "what," not the "how"
- Dependencies called out explicitly with JIRA links

## Framing Documents

### Structure
1. Context / Problem Statement (1-2 paragraphs)
2. Proposed Approach (with options if applicable)
3. Key Decisions Required (table or bullet format)
4. Scope / Out of Scope
5. Open Questions
6. Next Steps (specific, assigned, time-bound)

### Voice Pattern
Opens with urgency — why this matters now. Example: "pgEdge Cloud currently only supports BYOA/BYOC deployment models. To reach our subscription revenue targets for H2, we need a multi-tenant hosting option available by Q3."

### Rules
- Tables for option comparison (always include a "Recommendation" column)
- "Open Questions" section is critical — surfaces unknowns early
- Non-prescriptive: "I do not want to get prescriptive about how this is implemented"

## Strategic Proposals

### Structure
1. Executive Summary (3-4 sentences max)
2. Market Context (competitive landscape, with specific competitor data)
3. Proposed Strategy
4. Financial Impact (numbers, not hand-waving)
5. Risks and Mitigations
6. Timeline and Next Steps

### Voice Pattern
Data-heavy, reference-rich, recommendation-clear. Always includes competitor pricing or positioning data. Example: "CockroachDB charges $0.50/vCPU-hour for their Dedicated tier. Our current pricing at $125/vCPU/month is competitive but needs volume discount tiers to win enterprise deals."

## Marketing Copy

### Structure
- Headline: Benefit-first, specific
- Body: Problem → Solution → Differentiator → CTA
- Always includes 3-5 specific technical capabilities
- Competitor-aware without being combative

### Voice Pattern
Professional but not stuffy. States capabilities plainly. Example: "pgEdge Distributed Postgres gives you multi-master replication across regions with automatic conflict resolution. No application changes required."

### Rules
- No superlatives without evidence ("best," "fastest," "most advanced" need proof)
- Technical accuracy is non-negotiable — marketing never overpromises
- Include specific PostgreSQL version numbers and extension names

## Technical Documentation

### Voice Pattern
Direct, scannable, example-driven. Assumes reader is technical. Example: "The Spock extension handles multi-master replication. Install it with `spock install` and configure replication sets using the pgEdge CLI."

### Rules
- Code examples for every configuration step
- Prerequisites listed upfront
- Expected outputs shown for verification
- Troubleshooting section for common failures
- A how-to is procedure, not narrative. No moral, no "what I learned," no story arc grafted on. If a sample or personal dataset is used to demonstrate, keep it as flavour at the edges (intro, payoff) and out of the steps.
- Keep the reader's use-case central. Don't thread your own schema, table names, or row counts through every command. The reader came for the procedure with their own data, not for yours.
- Genericise the reader-facing parts. Use placeholders (`<your-db>`, `<your-table>`) over hardcoded personal names, profiles, or account IDs.
- Prose is not wrapped to a fixed column. Only code blocks wrap. Don't hard-break paragraphs at 79/80 characters in something meant to be read as a document. That is a code-file habit, not a writing one.

## Competitive Analysis

### Structure
1. Competitor overview (1 paragraph each)
2. Comparison table (features, pricing, deployment models)
3. Strengths/weaknesses matrix
4. Positioning recommendations

### Voice Pattern
Factual and specific — never dismissive of competitors. "CockroachDB has excellent Kubernetes integration. We should note this gap in our enterprise positioning." Always includes specific pricing data and technical differentiators.

## Emails & Messages

### Voice Pattern
- Short. Gets to the point in the first line.
- Requests are specific and time-bound
- Closes with a clear ask, not an open question
- Uses "Thanks" not "Thank you for your time and consideration"

### Example
> Hey [name] — quick question on the subscription pricing model. Do we have unit costs for a 4-vCPU managed Postgres instance on AWS us-east-1? Need it for the tier pricing deck by Friday. Thanks
