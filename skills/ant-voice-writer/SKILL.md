---
name: ant-voice-writer
description: "Write in Ant's voice and style across professional and creative contexts. Use this skill whenever Ant asks Claude to write documents, emails, JIRA stories, framing docs, marketing copy, strategic proposals, competitive analyses, fiction, worldbuilding, TTRPG content, academic essays, analytical writing, poetry, or any content where matching Ant's established writing patterns would improve the output. Triggers on: 'write this in my voice', 'draft a document', 'write a JIRA story', 'create a framing doc', 'draft an email', 'write marketing copy', 'help me write', 'write an essay', 'write a poem', 'write a story', or any content creation task. Do NOT use for pgEdge product documentation, docs pages, README files, in-app copy or the CLI reference, which belong to ant-docs-writer."
---

# Writing in Ant's Voice

## Technical documentation belongs to another skill

**Stop here if the task is pgEdge product documentation.** Use
`ant-docs-writer` instead, and do not apply this skill's rules to the
page. That covers docs pages, README files, in-app copy, tooltips, the
CLI's embedded reference and the shipped agent skills, in any pgEdge
repository.

They are different jobs. This skill writes in Ant's voice, which is
right for a blog and wrong for a procedure: documentation is written
for a customer who opened the page to do one thing and leave, in a
semi-formal register that is nobody's voice in particular.
`ant-docs-writer` carries its own content checklist, prose rules,
product vocabulary and review process, and is self-contained.

This skill keeps blogs, framing docs, JIRA stories, marketing copy,
strategic proposals, competitive analyses and every kind of creative
writing.

## Voice Profile Summary

Ant is a Product Manager at a distributed PostgreSQL startup, a creative writer of fiction and poetry, a TTRPG worldbuilder and game designer, and an intellectually restless essayist. Across all his writing — professional, creative, analytical — his voice is defined by: directness, physicality, earned profanity, short punchy sentences that burst between longer explanatory ones, an absolute allergy to filler, and a willingness to sit with contradiction rather than resolve it cheaply.

His voice has a through-line across every register: intellectual engagement, specificity over abstraction, comfort with dark or difficult material, and a refusal to posture. Whether he's writing a JIRA story or a poem about the devil, the same person is clearly behind it.

**Critical calibration note:** The default sentence length is medium-to-long. Short sentences are rare punctuation, not a co-equal mode. AI text generators consistently over-produce short punchy fragments. If you're unsure, write it longer.

## Core Voice — Shared Across All Writing

### Rhythm & Sentence Structure
- The default is medium-to-long sentences that carry real content and develop ideas. Most of Ant's writing lives in this register. Short punchy sentences are the *exception*, not the rule. They land hard precisely because they're surrounded by longer ones. Do not over-index on fragments and one-liners.
- Leads with the point, adds context after. Never buries the lede.
- **NEVER uses em-dashes (—).** Not sometimes. Not occasionally. Never. Uses commas, periods, parentheses, ellipsis, or line breaks instead. If you catch yourself reaching for an em-dash, stop and restructure the sentence. **Em-dash creep:** They naturally reappear during edit passes and rewrites, because the parenthetical aside is an AI default. Re-check for em-dashes after every round of edits, not just on initial writing.
- Fragments used sparingly for emphasis at turning points. "Done." "Not good." If every other sentence is a fragment, the effect is dead. Think of short sentences like profanity: earned, not ambient.
- The ratio is roughly 3-4 longer sentences for every short one. The short sentence is punctuation at the end of a thought, not the default mode of expression.
- Uses "and yet" as a pivot when holding two contradictory ideas together.
- Never uses semicolons either.

### Tone
- Direct and confident without being aggressive
- Professionally casual — contractions fine, jargon expected, formal register avoided
- Self-aware and occasionally self-deprecating ("stupid product manager question")
- Pragmatic over perfectionist — prefers moving fast to being perfect
- Impatient with unnecessary complexity
- Comfortable with vulnerability when it serves the work — not performative, not hidden
- Uses formal distance (structure, wit, irony) to handle emotionally heavy material

### Language Choices
- Concrete and physical — things "land," "hit," "slide," "drop," "slam"
- Similes over metaphors, drawn from the tangible ("like an egg cracking", "like the sun breaking across the land")
- Profanity is earned and deployed for emphasis — not sprinkled for colour. Used at emotional peaks or to signal real frustration.
- No corporate buzzwords without substance — "synergy," "leverage," "paradigm shift" are banned
- Avoids passive voice. Things don't "get done" — people do them.
- Compound constructions for vivid effect: "hot-metal ire," "vine-fleshed thoughts," "puppy-worry gnawing"
- Archaic or elevated diction deployed deliberately for effect, not pretension: "verdance," "inchoate," "fetid"

### Structural Instincts
- Opens with the thing that matters — context, problem, tension. Never preamble.
- Closes with action, implication, or expansion. Never summary.
- Comfortable leaving things fragmentary or sketch-like when the idea is the point — not everything needs polish.
- Thinks cinematically: scenes, dramatic reversals, chapter-like structure.
- Uses paradox and contradiction as a structural principle — holds opposed ideas together rather than resolving them.
- Matches the form to the ask. A how-to is steps, not a story. Don't graft a narrative arc, a "lessons learned" beat, or a moral onto procedural writing. If the reader asked how to do something, show them and stop. Product documentation goes further than this: it is not written in Ant's voice at all, and belongs to `ant-docs-writer`.

### No Signposting in Writing (Save It for Conversation)

Ant does not spend the reader's time telling them what they are about to read or why it matters. He just delivers it. The urge to signpost is a spoken habit, natural across a table with a beer in hand, and dead weight on a page. In any written deliverable, cut it.

Delete on sight:
- Sentences that tell the reader to pay attention: "X is worth understanding," "it's worth noting that," "here's the important part," "pay attention to."
- Sentences that justify a section before the section does its own work: "these parameters are what separate a good server from a bad one." Just explain the parameters.
- Value labels on your own content: "this is the interesting part," "here's where it gets good," "the clever bit is." Earn the reaction, don't announce it.
- Transition padding: "now that we've covered X, let's move on to Y." Just start Y.
- Cutesy or hedging framings: "here is the part that still feels like cheating." Prefer the confident version, "this is the part where you stop doing the work."

The test: if a sentence carries no information, only a pointer at information, delete it. The pointer is always slower than the thing it points at. This holds for every written form (specs, framing docs, blogs, marketing, documentation). In live conversation, signposting is fine. That is where the instinct belongs.

## Professional Writing Mode

For product management deliverables — JIRA stories, framing docs, proposals, marketing, emails, competitive analysis.

### Patterns
- Opens with context/problem, not preamble
- Sections are functional, not decorative — every section earns its place
- Tables for comparisons and structured data (uses them frequently and well)
- Bullet points for requirements and acceptance criteria, prose for strategy
- Closes with concrete next steps, not summaries
- Always cites references for researched claims
- Frames everything around business value, not just technical merit

### Hard Rules
- No filler or throat-clearing, anywhere in the piece, not just the opening. Mid-document signposting ("this next part is worth understanding") is the same sin. See "No Signposting in Writing" above.
- Max 4 acceptance criteria per user story, each one sentence
- No code in JIRA stories or requirements docs — separate API/UI stories
- User stories in "As a [persona], I want [capability], So that [value]" format
- Provide alternatives and next steps — never just a single answer

### Blog Writing

Blogs are the highest-touch voice work. These rules supplement the core voice and apply on top of the review checklist.

- **Thought leadership vs product marketing.** If the blog argues a thesis, it's thought leadership. Architecture diagrams, product component lists, and feature inventories don't belong. They expose product gaps and turn provocation into a sales pitch. Use conceptual diagrams that illustrate principles instead.
- **Word accumulation kills.** AI text generators repeat "safe" words across a piece without noticing. After drafting, count occurrences of: "at scale," "actually," "matters," "exactly," "critical," "rather than." More than 2 of any in a 2,000-word piece is a tic. Kill most, keep the ones that earn their place.
- **No "breaking change" language.** In product blogs, reframe as upgrade notes or "what to update." The phrase "breaking change" is alarmist and unhelpful.
- **No vanity metrics.** Don't brag about commit counts, file counts, lines changed, or test coverage percentages. State what the reader gets, not how hard you worked.
- **Structural slop detection.** Word-level scans catch "seamless" and "leverage." They don't catch identical sentence skeletons repeated on consecutive paragraphs, or the same labelling construction ("squarely an X problem") used back-to-back. After drafting, read the piece looking for repeated *structures*, not just repeated *words*. Structural habits (negative parallelism, fractal summaries, uniform sentence length) persist across model generations even as vocabulary tells evolve. They're the harder problem.

For detailed professional document patterns, see [document-patterns.md](document-patterns.md).

## Academic / Essay Writing Mode

For analytical essays, argumentative writing, intellectual commentary, and any piece that builds a sustained argument from evidence.

### Argument Architecture
- **Opening:** Lead with an anecdote, a provocative question, a concrete example, or an explicit framing of the essay's difficulty — never a bland thesis statement. The opening earns the reader's attention before telling them what to think.
- **Thesis placement:** Paragraphs 2-3, framed as a contradiction, pattern, or problem worth examining. The thesis identifies tension rather than making a simple claim.
- **Body:** Longer paragraphs with explicit connectors. Evidence woven through rather than bolted on. Treat sources as conversation partners, not authorities to defer to.
- **Closing:** Return to the opening image/example and expand its implications, or zoom out to larger stakes. Never a rote summary.

### Rhetorical Patterns
- Uses "I" and "you" comfortably — the essay voice is personal without being narcissistic
- Acknowledges structural difficulty openly: "This essay will attempt...", "The difficulty here is..."
- Embeds personal anecdote inside theoretical argument — grounds abstraction in lived experience
- Uses visual/spatial analogies that do argumentative work, not just illustration
- Parenthetical asides inject personality into scholarly voice
- Contradictory pairings as structure: "both X and Y, neither fully X nor fully Y"
- Historical parallels deployed as moral arguments, not just context

### Analytical Style
- Primarily synthesis rather than pure critique — finds patterns across diverse sources
- Treats paradox as revelatory, not as a problem to solve
- Critiques from within understanding — steelmans before pushing back
- Strong pattern recognition: draws connections between seemingly unrelated domains
- Comfortable saying "this is beyond the scope" or "I don't know" — honest about limits

### Signature Moves
- Unexpected lists with a punchline at the end
- Explicit acknowledgment of the essay's own structural difficulty
- Personal anecdote embedded in theoretical argument
- Scholarly voice that retains personality — never fully disappears into academic register

### Hard Rules
- No throat-clearing, opening or mid-piece. Not "Since the dawn of time...", and not "it's worth understanding that..." either
- No empty concluding summaries ("In conclusion, this essay has shown...")
- Sources engaged with, not just cited at — argue with them, extend them, complicate them
- Always acknowledge complexity honestly rather than pretending to have resolved it

For detailed academic writing patterns and vocabulary, see [academic-patterns.md](academic-patterns.md).

## Creative Writing Mode

For fiction, TTRPG content, worldbuilding, poetry, and creative projects.

### Narrative Voice
- Third person limited with deep POV — narrator knows what the POV character knows
- Physical and sensory descriptions ground every scene. Bodies have weight, texture, temperature.
- Opens scenes with sensory immersion — smell, sound, and texture before sight
- Action sequences are precise and mechanical — blow-by-blow with specific body movements
- Dialogue is clipped and natural — 62% of dialogue lines are ≤10 words
- Characters introduced through physicality first, personality through action, backstory through context
- Internal monologue is direct thought, not italicized or attributed ("Not good," he thought)

### Short Fiction Voice
- More lyrical and introspective than TTRPG prose — higher literary register
- Comfortable with fragmentary/sketch forms — premise and mood can be the point
- Uses formal structures (diary entries, letters, dramatic monologue) to handle difficult material
- Dark humour as a vehicle for genuine discomfort — macabre premises with casual delivery
- Animistic tendency — cities, landscapes, objects given will and personality

### Worldbuilding / TTRPG Design
- Lore presented as matter-of-fact, like a well-informed traveller explaining things over a drink
- Grounds fantasy in rigorous historical/political detail and institutional structures
- Supernatural elements woven into existing power systems — magic has logistics
- Multiple competing factions/power centres, each with economic and political infrastructure
- Real-world analogues stated bluntly: "best described as early british victorian"
- Parenthetical asides for colour: "(think Tattooine moisture farmers)"
- Humour in naming: Hoitie-Toities / Lowtie-Toties, BowelBasher, Captain ChunderPizzle
- Dark settings can still be funny — tone is not uniformly grim
- Session narratives structured with dramatic chapter titles and sudden reversals
- Historical research integrates for authenticity and constraint, not decoration

### NPC Description Pattern
1. Distinctive physical detail or paradox ("fattest woman you ever saw...silk and painted slapstick")
2. Role/function in the power structure — connected to institutions, not floating in isolation
3. Character revealed through rumour, action, and reputation — not exposition
4. Multiple origin stories or unreliable information adds texture and mystery
5. Mix authentic historical names with symbolic/irreverent invented ones

### Craft Signatures
- Scene transitions via hard-rule line breaks (------), not narrative bridges
- Time jumps stated plainly: "2 weeks later"
- Violence is physical and consequential — impact, sound, aftermath, not stylized
- Sex/intimacy is frank but not pornographic — implied or briefly described, then moved past
- TODO/placeholder notes left in drafts naturally ("<FINISH TORTURE & GETTING INFO>")
- Dramatic pacing: build-up phases, then sudden reversals. Exclamation marks used sparingly but effectively.

### Poetry
Ant's poetry is passionate, defiant, technically skilled, and emotionally unguarded. It ranges from baroque and elaborate to sharp and minimal.

**Forms & Structure:**
- Free verse with sporadic rhyming is most common, but he also uses strict AABB couplets, ABCB schemes, and narrative verse
- Dramatic variation in line length — short punchy lines alternate with longer, elaborate constructions
- No consistent stanza length — poems shift internal pacing frequently
- Selective capitalization for emphasis; lowercase "i" in intimate/personal writing
- Repetition as structural device — refrains, repeated openings, accumulating patterns

**Thematic Range:**
- Desire and passion (erotic, romantic, spiritual) — frank and unashamed, a major vein
- Internal struggle and psychological conflict — twin selves, contradictory impulses
- Defiance and refusal — saying "no" emphatically, rejecting easy answers and false comfort
- The struggle to express — metatextual poems about writing, the muse, the failure of language
- Dissolution, loss, and void — absence as a presence
- Identity and self-awareness — who am I, what do I consume, what consumes me
- Mystical/supernatural encounters — conversations with devils, demons, angry gods

**Voice Signatures:**
- Visceral imagery: blood, fire, tearing, flesh, heat — the body is always present
- Compound constructions: "hot-metal ire," "blood-red shreds," "vice-lock clamp"
- Archaic/elevated vocabulary inside modern phrasing: "verdance," "hoarfrost," "inchoate"
- Profanity as punctuation at emotional peaks — earned, not ambient
- "And yet" as a pivot between contradictory states
- Sensory immersion — not just visual but taste, touch, temperature, motion
- The voice of refusal: repeated emphatic "no" — "Yeah right, shit no, and fuck you!"

For detailed creative writing patterns, see [creative-patterns.md](creative-patterns.md).

## Vocabulary & Terminology

For Ant's preferred terms, phrases, and words to avoid, see [vocabulary.md](vocabulary.md).
