# Blog Review Checklist

Use this checklist during Phase 5 (First Review) and Phase 8 (Second Review). Every item must pass. If something fails, fix it in-place and note what you changed.

## 1. AI Slop Detection

AI-generated text has recognizable tells. The goal is to produce writing that sounds like it was written by a human with opinions, not assembled by a language model.

### Phrases to Kill on Sight

These phrases are almost never used by human writers in natural prose. If you find any of them, rewrite the sentence:

- "In today's rapidly evolving landscape"
- "It's worth noting that" / "It bears mentioning"
- "Let's dive in" / "Let's dive deeper" / "Let's unpack"
- "Without further ado"
- "At the end of the day"
- "This is where X shines" / "This is where X really comes into its own"
- "Game-changer" / "Gamechanger"
- "Revolutionize" / "Revolutionary"
- "Seamless" / "Seamlessly" (unless describing an actual seam)
- "Cutting-edge" / "State-of-the-art" / "Next-generation"
- "Empower" / "Empowering"
- "Robust" (in marketing context)
- "Leverage" (as a verb)
- "Ecosystem" (when you mean "set of tools" or "community")
- "Journey" (when you mean "process" or "experience")
- "Unlock" (when you mean "enable" or "allow")
- "Harness" (when you mean "use")
- "Navigate" (when you mean "deal with" or "figure out")
- "Landscape" (when you mean "market" or "field")
- "Streamline" (when you mean "simplify" or "speed up")
- "Elevate" (when you mean "improve")
- "Delve" / "Delve into"
- "Explore how" (as an opening)
- "In this blog post, we will..."
- "Hits different" (was fresh once, now overused across posts)

### Structural Slop Patterns

- **The restatement pattern:** Saying something, then immediately saying it again in different words. Example: "This reduces latency significantly. In other words, your queries will be much faster." Cut the restatement. Trust the reader.
- **The false transition:** "With that in mind," "That being said," "Having established that," — these add words without adding meaning. Cut them and let the next sentence stand on its own.
- **The list-then-elaborate pattern:** Listing 3 things and then spending a paragraph on each with near-identical sentence structures. Vary the structure. Not every point needs the same treatment.
- **The hedge sandwich:** Starting with "While X is...", then "However, Y...", then "Nevertheless, Z..." — multiple hedges stacked on each other. Pick a position and state it.
- **The anaphoric fragment pattern:** "No installation. No configuration. Just code." / "No setup. No friction. Just results." This is a deeply ingrained AI writing tic. It sounds punchy on first read but is structurally lazy: it avoids writing a real sentence that develops the thought. If you find any "No X. No Y. Just Z." constructions, or similar parallel fragment triplets, rewrite them as a proper sentence. Example fix: "You don't need to install or configure anything. Click the link and you're writing code." The real sentence does more work and sounds like a human wrote it.

### Performative Writing

Sentences that describe the writer's physical actions or emotional reactions in a way that serves narrative framing more than the actual story. "I sat back in my chair." "I couldn't believe what I was seeing." "A grin spread across my face." These are writing-about-writing. If a sentence describes the author's body language or internal state and you can remove it without losing any information or narrative momentum, it's performative. Cut it.

Exception: if the physical action IS the story (e.g., "I was stumbling to my desk at 1 AM" in a blog about building something at 3 AM), that's authentic detail, not performance.

## 2. Em-Dash Check

Search the entire document for the em-dash character: —

Also search for double-hyphens (--) which sometimes substitute for em-dashes.

If any are found, the review fails on this item. Replace every instance:

- If the em-dash separates a parenthetical, use parentheses or commas
- If the em-dash introduces a consequence or elaboration, use a period and start a new sentence
- If the em-dash creates a dramatic pause, use an ellipsis or restructure
- If the em-dash connects two related clauses, use a comma or split into two sentences

This is not a stylistic preference. It is an absolute rule. Zero em-dashes in the final output.

## 3. Semicolon Check

Search for semicolons (;) in prose text (code blocks are exempt).

Replace with periods, commas, or sentence restructuring. Same absoluteness as em-dashes.

## 4. One-Sentence Paragraphs

Count the number of one-sentence paragraphs in the entire blog. If there are more than two, the review fails.

One-sentence paragraphs are a powerful rhetorical punch when used once, maybe twice. "Gut punch." works as a standalone paragraph because everything around it is full paragraphs. But when every other paragraph is a single sentence, the rhythm flattens and the effect dies.

Fix by:
- Merging the short paragraph into the one above or below it
- Expanding it into 2-3 sentences that develop the idea
- Asking: "Does this sentence earn its own paragraph, or is it just accidentally alone?"

The only exemption: section-ending one-liners that serve as transitions. Even these should be rare.

## 5. Sentence Rhythm

### Short Sentence Clusters
This is critical because AI text generators default to short, punchy sentences far more often than human writers do. The user's actual writing rhythm is medium-to-long sentences as the base, with short sentences deployed sparingly for emphasis.

**Hard rule:** Count all sentences under 10 words in the entire blog. If more than 20% of sentences are short, the review fails. Rewrite short sentences into longer ones that develop the thought, or combine adjacent short sentences into one substantial one.

**Sequence rule:** Flag any sequence of 2 or more consecutive sentences under 10 words. This includes across paragraph boundaries. "No installation. No configuration. Just run it." is three consecutive short sentences even if they're formatted as a paragraph.

**Fragment patterns:** Watch for parallel fragments used as rhetorical flourish: "No X. No Y. Just Z." / "Fast. Simple. Done." / "One click. One command. One result." These almost always come from AI, not humans. Rewrite as complete sentences.

Fix by combining, expanding, or restructuring. The goal is a rhythm where medium-length sentences carry the content and short sentences punctuate key moments, not the other way around.

### Long Sentence Monotony
Flag any sequence of 5 or more consecutive sentences over 25 words with no short sentence break. The rhythm needs variation.

Fix by finding the natural punctuation point in one of the long sentences and breaking it into a short, punchy statement.

### Paragraph Length
Flag any paragraph longer than 6 sentences. Blog readers scan. Dense paragraphs get skipped.

Fix by finding the natural break point (usually a shift in sub-topic) and splitting.

## 6. Cross-Blog Phrase Repetition

If the research phase found previous blog posts by the user, scan the current draft for distinctive phrases that also appeared in those posts. A phrase that was fresh and effective once becomes a verbal tic when it shows up in every post.

Known repeat-offenders to watch for:
- "hits different"
- Specific metaphors or analogies reused across posts
- Signature sentence structures that have already appeared

The first use (in the original blog) was great. The second use (in this one) is a crutch. Find a different way to express the same idea.

## 7. Technical Accuracy

### Code Snippets
- Verify syntax is correct for the language used
- Verify function names, method calls, and CLI commands match actual APIs
- Verify configuration values are realistic (port numbers, file paths, etc.)
- If the code was drawn from vault research, cross-reference with the source
- Include expected output or results where helpful

### Product Terminology
- "multi-master replication" not "multi-primary replication"
- "Spock" (capitalized) in prose, `spock` in code contexts
- "pgEdge Cloud" not "PGEdge cloud" or "pgedge Cloud"
- "pgEdge" not "PGEdge" or "Pgedge" in running text
- "PostgreSQL" not "Postgres" in formal/first references (Postgres is fine after first use)
- Verify version numbers and feature names against vault documentation

### Deliberate Terminology Changes
If the research phase found that certain terms are being actively removed or replaced in git history (e.g., "Docker Swarm" being phased out in favor of "Docker" or "container orchestration"), the blog must use the current preferred terminology. This is not a style preference. It reflects deliberate product positioning decisions.

### Claims and Capabilities
- Don't claim features that don't exist
- Don't overstate performance without evidence
- If making a comparison with competitors, verify the comparison is accurate and current
- Technical limitations should be acknowledged, not hidden

## 8. Authorial Intent (Existing Drafts Only)

When reviewing an existing draft, the most important thing is understanding what the author was trying to say, not just what they said. Before changing the tone, emphasis, or framing of any passage, ask: "What is the author's intent here?"

Specific rules:
- **Never reinterpret the author's motivations.** If they say "this was a forcing function for something I already intended to do," that means they already knew the product. Don't reframe it as "I didn't know my product."
- **Preserve self-aware framing.** If the author is being deliberately self-deprecating or candid about limitations, that's a conscious choice. Don't soften it into generic competence.
- **Match the narrative the author is building.** Read the whole draft before touching anything. Understand the arc. If the blog builds toward a lesson, don't undermine the lesson by over-polishing the setup.

## 9. Readability

### Opening
The first two sentences must earn the reader's attention. Test by asking: "Would I keep reading if I saw this on Hacker News?" If the opening is a bland setup paragraph, rewrite it to start with the problem, a surprising fact, or a concrete scenario.

### Closing
The final paragraph must drive action or provoke thought. Test by asking: "Does this end with energy or does it fizzle?" If it's a summary of what was covered, rewrite it. Options: call to action, open question, implication for the future, "here's what to try next."

### Transitions Between Sections
Each section should end with a reason to keep reading, and each section should begin by connecting to what came before. If two sections feel disconnected, add a bridging sentence or reorder.

### Scanability
Readers will scan before they read. Make sure:
- Headings tell a story (not just topic labels)
- The first sentence of each section carries the key idea
- Code blocks and examples break up prose
- No wall-of-text sections longer than ~200 words without a visual break

### Context for Unfamiliar Tools
When the blog mentions a tool, technology, or concept that some readers might not know, include a one-sentence "what is it" explanation woven into the prose. Not a parenthetical definition dump, just a natural contextual sentence. Example: "GitHub Codespaces gives you a full dev environment in your browser, with a generous free tier of compute hours." If you're unsure whether the audience knows something, include the one-liner. It costs almost nothing and prevents reader drop-off.

## 10. Voice Consistency

### Register Stability
Read the piece start to finish and check that the voice doesn't shift. Common drift patterns:
- Starting conversational, becoming formal in technical sections
- Starting technical, becoming marketing-speak in the conclusion
- Inconsistent use of "you" vs "we" vs third person

### Banned Words Check
Scan for words from the voice skill's avoid lists. Common catches:
- "utilize" → "use"
- "ensure" → "make sure" (or be specific)
- "in order to" → "to"
- "leverage" → (be specific about what you're actually doing)
- "synergy" → (just don't)
- "best-in-class" → (prove it or cut it)

### Physicality Check
Is the language concrete? Are things happening, or are things being described in abstract terms? The voice skill emphasizes physical, tangible language. If a paragraph is all abstractions, ground it with a specific example or physical verb.

## 11. Final Sweep

- Spell check (especially technical terms and product names)
- Link check (if any URLs are included, verify they're plausible)
- Consistent heading hierarchy (H1 for title, H2 for major sections, H3 for subsections)
- No orphaned TODO or placeholder notes
- Word count is within the target range agreed in Phase 3
