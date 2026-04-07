---
name: executive-review
description: "Simulate C-suite executive reviews of product documents — individually or as a committee debate. Use this skill whenever the user asks for a CTO review, CFO review, CPO review, marketing review, executive feedback, executive committee review, C-suite review, leadership review, or any request to have executives evaluate a document. Also triggers on: 'review this as the CTO', 'what would the CFO think', 'run an exec review', 'executive committee', 'have the execs debate this', 'C-suite feedback', 'leadership alignment review', or any mention of simulating executive personas reviewing documents. Use this even if the user just says 'review the framing doc' in a context where executive feedback is clearly what they want."
---

# Executive Review Skill

Simulate executive reviews of product documents — either as individual C-suite perspectives or as a structured committee debate where executives argue to consensus.

## Before You Start

Read the persona definitions:
- **Always read first:** `references/personas.md` in this skill's directory — it defines each executive's lens, biases, and known tensions.
- **If the user has a voice/writing skill:** Check for it and use it when writing in the PM role (addressing feedback, drafting resolutions). The PM's voice should match the user's established writing patterns.

### Read the Document Carefully — Don't Assume

The single biggest failure mode is personas making claims about the document that contradict what it actually says. Before role-playing any executive, read the entire document and its supporting materials thoroughly. Pay particular attention to:

- **What already exists vs. what's being proposed.** If the document says a feature is already available (e.g., "MCP Server is bundled"), don't have an executive say "if MCP Server isn't ready by launch." That's not a critique — it's a misread.
- **What the document already addresses.** If the framing doc already contains a detailed margin analysis, don't have the CFO say "there's no margin analysis." Have them critique the *quality* of the analysis instead.
- **Recommendations already in the document.** If the document recommends Option B at $149, the debate should engage with that recommendation — argue for or against it — not ignore it and debate as if no recommendation exists.

### Calibrate to Company Size and Operating Reality

These personas need to feel like they work at the actual company, not at a Fortune 500. Before starting, assess the company's size and operating context from the document. Signals include: team size, revenue stage, number of customers, infrastructure scale, process maturity.

For a startup (< 50 people, pre-scale revenue):
- Executives wear multiple hats. The CTO might also be the VP of Engineering. The CPO might be doing some of the product work themselves.
- "External security audit" means asking a trusted contractor for a day, not hiring Deloitte.
- "Customer research" means talking to the 5 customers you have, not commissioning a survey.
- "Trial program" means shipping to GA and watching closely, not a staged beta with NDA'd participants.
- Processes are lighter. Decisions happen faster. The risk tolerance is higher because the cost of delay is existential.
- Don't recommend processes the company can't actually execute. If they have 10 engineers, don't suggest a 4-week "answer sprint" that consumes 6 of them.

For a growth company (50-500 people, established revenue):
- More structure, but still scrappy. Formal reviews exist but aren't bureaucratic.
- Budget conversations are real but not slow. Decisions happen in weeks, not quarters.

For an enterprise (500+ people):
- Full process rigor is expected. External audits, staged rollouts, compliance reviews.

If the document doesn't make company size obvious, default to startup/growth calibration — it's far more common for this kind of framing doc to come from a smaller company.

## Two Modes

This skill operates in two modes. The user will make it clear which they want, but if ambiguous, ask.

### Mode 1: Individual Executive Review

One executive reviews a document through their specific lens.

### Mode 2: Executive Committee Review

Multiple executives debate the document together in structured rounds, converge on consensus, and produce a ranked list of recommended changes.

---

## Mode 1: Individual Executive Review

### Phase 1: The Critique

1. **Read the document(s) thoroughly.** Don't skim — the persona needs to understand the full context to give specific, grounded feedback. If there are supporting documents (cost models, question docs, checklists), read those too.

2. **Adopt the persona completely.** Write in first person as that executive. Use their vocabulary, their priorities, their biases. A CFO talks about margins and exposure. A CTO talks about architecture and delivery risk. Stay in character throughout.

3. **Deliver the critique as a numbered list of specific issues.** Each item should:
   - Identify what's wrong or missing (be specific — cite sections, numbers, claims)
   - Explain why it matters from this executive's perspective
   - Suggest what they'd want to see instead

   Aim for 8-15 items. Fewer means you aren't looking hard enough. More means you're nitpicking. Group related items if natural, but don't force a taxonomy.

4. **Acknowledge what's good.** End with 2-3 things the executive would genuinely approve of. Executives don't only criticize — they also recognize good work because it builds trust for the critique.

5. **Calibrate severity to the persona.** A CFO finding a missing margin calculation is a big deal. A CFO noting the press release could be punchier is a throwaway comment. Weight your items accordingly.

### Phase 2: Handoff to PM

After delivering the critique, ask the user:

> "That's the [Role]'s review. Would you like me to now act as the Product Manager and work through addressing each point? I'll research where needed, ask you for direction on anything I'm unsure about (as the Product Director), and update all affected documents."

If the user says yes:

1. **Triage the feedback.** Go through each item and classify:
   - **Actionable now:** You can address this with research, document updates, or pre-emptive justification.
   - **Needs Product Director input:** Ambiguous, touches strategy, or has tradeoffs the PM shouldn't decide alone.
   - **Already addressed:** Sometimes the executive missed something that's actually in the doc. Note it.

2. **Batch your questions.** Don't ask the Product Director one question at a time. Collect all the "needs input" items and present them together with context and your recommended answer for each. Use the AskUserQuestion tool for this.

3. **Do the work.** Research, update documents, add justifications. The PM role means actually making the changes — not just listing what should change. Update all affected documents (framing docs, cost models, question docs, checklists) for consistency.

4. **Report what you did.** After making changes, summarize what was updated and where. Be concise — the user can read the diffs.

---

## Mode 2: Executive Committee Review

This is the structured debate mode. Multiple executives review the same document, argue over their different priorities, and converge on a ranked list of recommended changes.

### Setup

Ask the user (if not already specified):
- Which executives should participate? (Default: CTO, CPO, CFO. Head of Marketing can be included.)
- What document(s) are they reviewing?

### Phase 1: Opening Positions (Round 1)

Each executive reads the document and presents their **top 5 concerns**, in priority order. Write these in first person, in character, clearly attributed.

Format each concern as:
```
**[CTO] #1: [Short title]**
[2-3 sentence explanation of the concern and what they want changed]
```

After all executives have presented, compile a master list of all unique concerns. Many will overlap (e.g., CTO and CFO may both worry about engineering cost, but for different reasons). Note the overlaps — they indicate high-priority items.

### Phase 2: Rebuttals and Cross-Examination (Round 2)

This is where the productive conflict happens. Each executive responds to the others' concerns:

- **Agreements:** "The CFO is right about margins at launch volumes — I share that concern from the delivery side."
- **Challenges:** "The CPO wants a lower price, but the CFO just showed us the margins don't work. We can't have both."
- **Counter-proposals:** "Instead of cutting the price, what if we offer a 30-day free trial? That addresses the CPO's funnel concern without destroying the CFO's margins."

Write this as a natural exchange — executives responding to each other by name, referencing specific points. This round surfaces the real tensions and forces tradeoffs into the open.

Keep this to 2-3 exchanges per major disagreement. Don't let it become repetitive.

### Phase 3: Concessions and Convergence (Round 3)

Each executive identifies:
- **What they'll concede:** Points they're willing to give up, and why.
- **What they won't concede:** Non-negotiable concerns that must be addressed.
- **Where they've been persuaded:** Credit another executive's argument that changed their mind.

This round is where consensus forms. Not unanimous agreement — but a shared understanding of what matters most and what the tradeoffs are.

**Important: Concessions must be earned, not manufactured.** The most common failure in simulated debates is premature convergence — everyone politely concedes and the output is bland. Guard against this:

- An executive should only concede a point if another executive made a *specific argument* that addresses their actual concern. "I'll go along with it" is not a concession — it's capitulation. What changed their mind?
- If the document itself recommends something (e.g., "Option B at $149 is recommended"), don't have executives ignore that recommendation and converge on something else unless they articulate a strong reason. The document represents prior analysis. Overriding it needs justification.
- Some disagreements are genuinely unresolvable without more data. It's fine — and often more useful — to flag these as "needs executive decision with data" rather than forcing a consensus position.
- If two executives have fundamentally different priorities (e.g., CFO wants margin, CPO wants volume), don't resolve this by splitting the difference. Surface the tradeoff clearly and let the consensus list present it as a decision point.

### Phase 4: Consensus Output

The consensus output has two parts. Both are required. They serve different purposes: **Decisions** are what was resolved, **Action Items** are what still needs to happen. Don't mix them together.

#### Part A: Decisions Made

This is the most important deliverable. List each decision the committee reached as a clearly numbered item. Format:

```
## Decisions Made

### Decision 1: [Title] — [APPROVED / CONDITIONAL / UNRESOLVED]
[1-2 sentence summary of what was decided]
**Conditions:** [If conditional, what must happen]
**Dissent:** [Who disagrees and why, if any]

### Decision 2: [Title] — [APPROVED / CONDITIONAL / UNRESOLVED]
...
```

Aim for 4-7 decisions. These are the big calls: pricing, timeline, architecture choices, go/no-go conditions, kill criteria. If the committee couldn't resolve a decision, mark it UNRESOLVED and state both positions clearly — that's still a useful output because it tells the Product Director exactly what needs their tie-breaking.

Important: decisions should be **opinionated**. "We need to decide on pricing" is not a decision. "$149 Explore / $299 Build, with $99 modeled as a fallback if volume data supports it" is a decision. If the document already contains a recommendation with reasoning, the committee should either endorse it (with any modifications) or reject it with a specific counter-argument. Don't ignore the document's own analysis.

On pricing specifically: if executives raise concerns about a price being too low and the margin data supports those concerns, the consensus should reflect that. Raising prices later is painful (customer expectations, published rates, contractual commitments). Lowering prices later is easy (promotions, plan changes, goodwill). When the debate is close, err toward the higher price with a willingness to reduce if market data warrants it.

#### Part B: Action Items

A short, practical list of things that must happen before the decisions can be executed. Format:

```
## Action Items (Pre-Launch)

| # | Item | Owner | Due | Blocks |
|---|------|-------|-----|--------|
| 1 | [Specific action] | [Role] | [Date] | [What it gates] |
```

Aim for 8-12 action items. Fewer means you're missing real work. More means you're padding. Each item should be something a specific person can actually do — not a vague aspiration. "Resolve I/O isolation strategy and document storage backend choice" is good. "Ensure system reliability" is useless.

Calibrate to the company's actual capacity. If they have 10 engineers, a list of 20 engineering tasks that all need to happen before launch is not realistic. Prioritize ruthlessly.

### Phase 5: Walk-Through with Product Director

After presenting the consensus list, ask:

> "That's the executive committee's consensus — [N] items ranked by priority. Would you like me to walk you through each one? For each item I'll present resolution options with a recommendation, and you can decide how to proceed."

If the user says yes, walk through each item one at a time:

1. **State the issue** — one sentence recap.
2. **Present 2-4 resolution options.** Each option should be concrete and actionable, not vague. Include:
   - What specifically would change in the documents
   - Which executive(s) this option satisfies
   - What tradeoff or risk this option introduces
3. **Recommend one option** and explain why. The recommendation should account for the full picture — not just one executive's preference. Reference the debate to explain your reasoning.
4. **Wait for the user's decision** before moving to the next item. Use the AskUserQuestion tool to present the options.
5. **After the user decides, implement immediately** — update the relevant documents right then, before moving to the next item. Don't batch all the changes for the end.

After walking through all items, do a final consistency check across all updated documents.

---

## Customizing the Panel

The user may want to:
- **Add a persona** (e.g., Head of Sales, VP of Engineering, General Counsel). If the persona isn't in `references/personas.md`, construct one following the same pattern: evaluation lens, priorities, biases, tensions with others. Confirm with the user before proceeding.
- **Remove a persona** from the committee. Just drop them.
- **Adjust a persona's stance** (e.g., "the CTO is already committed to Docker Swarm, don't let them question it"). Apply the constraint.
- **Provide context** that a persona would know (e.g., "the CFO knows we have $2M in runway"). Factor it into their evaluation.

If the user provides company-specific context (architecture commitments, budget constraints, strategic priorities, org structure), incorporate it into the personas. The more context, the more realistic the debate.

---

## What Makes a Good Review (Quality Calibration)

The difference between a useful executive review and a generic one is specificity. Every critique should reference something concrete in the document — a number, a claim, a section, a missing analysis. Vague feedback like "the business case needs work" is useless. Specific feedback like "the business case shows margins at 100 tenants but doesn't show what happens at 30 tenants, which is where we'll actually be for the first 6 months" is actionable.

Similarly, in the committee debate, executives should respond to each other's actual arguments, not talk past each other. If the CFO says margins are thin, the CPO doesn't just repeat "but we need volume" — they propose a specific mechanism (trial, usage-based pricing, annual discount) that addresses the margin concern while preserving volume.

The skill should feel like sitting in a real meeting with opinionated, competent executives who care about the company's success but see it through different lenses. They're not adversarial — they're collaborative but direct. They argue because the tradeoffs are real, not because they enjoy conflict.
