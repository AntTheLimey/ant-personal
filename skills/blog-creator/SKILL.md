---
name: blog-creator
description: "End-to-end blog creation workflow: topic exploration, guided questioning, Obsidian vault research, voice-matched drafting, automated review, user feedback for voice skill improvement, and final polish. Use this skill whenever the user wants to write a blog post, draft a blog, create blog content, write a technical blog, write a company blog, brainstorm a blog topic, or mentions 'blog' in the context of content creation. Also triggers on: 'write a post about', 'draft an article about', 'I want to blog about', 'help me write about [topic] for the website', 'create content for the blog', or any request that involves researching a topic and producing a publishable written piece. Use this even for partial blog tasks like 'help me outline a blog post' or 'review my blog draft'."
---

# Blog Creator

A multi-phase workflow for creating high-quality, voice-matched blog posts informed by the user's own knowledge base. This skill researches the user's Obsidian vault for relevant source material, drafts in the user's authentic voice, performs rigorous self-review, and uses feedback to improve both the blog and the user's Voice Skill over time.

## Overview of Phases

The workflow has nine phases. Move through them in order, but be responsive to the user jumping ahead or going back. The phases are:

1. **Topic & Direction** — Opinionated editorial guidance to shape the blog
2. **Research** — Semantic search of the Obsidian vault + local project files + git history
3. **Outline & Length** — Propose structure and confirm scope
4. **Draft** — Write the blog in the user's voice
5. **First Review** — Automated quality review
6. **Image Placement** — Suggest where to place images, memes, diagrams
7. **Feedback Loop** — Cherry-picked passages for user rewrite + voice learning
8. **Second Review & Polish** — Post-edit quality pass
9. **Finalize** — Deliver the blog and an updated Voice Skill package

---

## Phase 1: Topic & Direction

The user provides a topic. Your job is not to collect requirements like a form. You are an opinionated editor. Present specific angles and push the user toward the most interesting one.

### How to Ask

Use AskUserQuestion with 3-4 questions. The critical difference from a generic questionnaire: **you suggest specific angles and let the user react, rather than asking open-ended questions.** Most writers know what they don't want better than what they do want. Give them something to push back against.

**Present 2-3 angles with opinions.** Don't just list options neutrally. Lead with the one you think is strongest and say why. Example:

> I'd suggest taking the "here's what I learned building this" angle rather than a feature walkthrough. Your narrative blogs (like the MM-Ready origin story) consistently perform because they're honest about mistakes and surprises. The feature walkthrough is safer but less distinctive. Thoughts?

**Ask about the reader's takeaway, not the reader's demographic.** "What should someone remember 24 hours later?" is more useful than "who is the audience?" The audience question matters, but it's secondary to the takeaway.

**Probe for the emotional core.** Every good blog has a moment of genuine feeling: surprise, frustration, pride, uncertainty. Ask what that moment is for this topic. If the user doesn't have one yet, that's a signal the angle might need work.

**Confirm the direction with a 3-4 sentence synthesis** before moving on. The synthesis should capture: the angle, the takeaway, the tone, and the emotional core.

---

## Phase 2: Research

Research the user's Obsidian vault, local project files, and git history for material that can inform the blog.

### Obsidian Vault Research

Search the vault using `mcp__obsidian-mcp-tools__search_vault_smart`. **Do not use folder filters.** The vault's folder structure may not match what you'd expect. Let the semantic search work across the entire vault.

Run 3-5 searches with different query formulations:

1. **Direct topic search** — The blog topic as a query
2. **Technical concept search** — Key technical terms, product names, or features
3. **Adjacent concept search** — Related ideas for depth or unexpected connections
4. **Previous blog search** — Search for the user's existing blog posts. This serves two purposes: (a) avoid repeating phrases, angles, or examples they've already used, and (b) learn from what worked in their previous writing. Search queries like "blog post", "[topic] blog", or the blog title if known.

For each search, set `filter.limit` to 10. No folder filters.

When results come back, read the most promising files using `mcp__obsidian-mcp-tools__get_vault_file` to extract:

- Specific technical details, architecture decisions, or code patterns
- Previously published language and positioning (to stay consistent)
- Unique insights or internal knowledge that would make the blog distinctive
- Code snippets that could be adapted as examples
- **Phrases and patterns to avoid repeating** from previous blogs

### Local File & Git History Research

If the blog topic involves a specific project or codebase:

1. **Read project files** — READMEs, docs, examples, configuration files for accurate technical details
2. **Check git history** — Run `git log --oneline -20` and `git log --all --oneline --grep="keyword"` in relevant repos to understand recent changes, deliberate removals, and terminology shifts. If the user has been actively revising a project, the git history reveals what they're intentionally moving toward or away from. This is critical for avoiding terminology the user is deliberately phasing out.
3. **Check for deliberate avoidances** — If you see a term being removed in recent commits (e.g., replacing "Docker Swarm" with just "Docker" or "container orchestration"), treat that as a strong signal to avoid that term in the blog.

### Research Synthesis

Present a brief research summary to the user:

- "Here's what I found that's relevant" (2-3 key findings)
- "Here's something interesting I didn't expect" (if applicable)
- "I noticed you've been [removing/replacing X] in recent revisions of [project], so I'll avoid [X] in the blog" (if applicable)
- "I found these previous blog posts covering related ground: [list]. I'll make sure not to repeat their angles or signature phrases." (if applicable)
- "I couldn't find vault material on X, so I'll work from general knowledge for that section" (flag gaps)

Confirm the user is happy with the research base before proceeding.

---

## Phase 3: Outline & Length

Based on the creative direction and research, propose a blog structure.

### Adaptive Length

Determine the appropriate length from the topic complexity and research depth:

- **Short (800-1200 words):** Focused opinion pieces, single-concept explainers, announcements
- **Medium (1200-2000 words):** Technical tutorials, competitive positioning, narrative pieces
- **Long (2000-3000 words):** Deep dives, multi-section technical guides, thought leadership

State your recommendation and reasoning. Example: "This is a technical walkthrough with code examples, so I'd target ~1800 words. The code blocks add visual length without adding reading time, so it'll feel shorter than it is."

### Outline Format

Present the outline as a sequence of sections with one-sentence descriptions of what each section does narratively. Not just topic labels. Example:

> 1. **Open with the problem** — Most developers discover they need distributed Postgres after they've already built on single-node. Start there.
> 2. **Introduce Spock as the answer** — Not as a feature list, but as the thing that lets you keep your existing schema and just... replicate it.
> 3. **Walk through the setup** — Concrete steps, real CLI commands, actual output.
> 4. **Show conflict resolution** — This is where distributed gets interesting. Use the e-commerce cart example from the docs.
> 5. **Close with what's next** — Where to go from here, link to docs, mention Cloud option.

### Context Check

For any technology, tool, or concept mentioned in the outline that isn't universally known by the target audience, flag it and plan a brief "what is it" explanation. Not a paragraph, just a sentence. Example: if the blog mentions Codespaces and the audience includes developers who might not use GitHub, plan for a one-liner like "GitHub Codespaces gives you a full dev environment in your browser, with a generous free tier of compute hours."

Confirm the outline and length with the user before drafting.

---

## Phase 4: Draft

### Voice Loading

Before writing, read the user's Voice Skill. Check for an `ant-voice-writer` skill (or similar voice skill) in the available skills list. If found, read the full SKILL.md and any referenced pattern files. The voice skill is the authority on how the user writes. Follow it closely.

Key voice principles to internalize (these are drawn from the ant-voice-writer skill, but always defer to whatever the current voice skill actually says):

- Lead with the point. Never bury the lede.
- Medium-to-long sentences are the default. Short punchy sentences are the exception, used for emphasis.
- No em-dashes. Ever. Use commas, periods, parentheses, or restructure.
- No semicolons.
- Concrete, physical language. Things "land," "hit," "slide."
- Profanity is earned and rare in professional writing.
- No corporate buzzwords without substance.
- Open with what matters. Close with action or implication, never summary.
- Active voice. People do things. Things don't "get done."

### Drafting Approach

Write the full blog in a single pass, following the confirmed outline. As you write:

- Weave in specific details from the vault research. If you found code snippets, architecture details, or product specifics, use them. The whole point of the research phase was to ground this blog in real material.
- Include code examples where appropriate. Make sure they are accurate and runnable. If you're pulling from vault source code, verify the syntax and API calls are current.
- Write transitions that carry the reader forward. Each section should end with a reason to keep reading.
- Match the confirmed tone. If the direction was "practical how-to with a conversational wrapper," don't drift into marketing speak halfway through.
- **One-liner context for unfamiliar tools/concepts** — Where the outline flagged a context check, include it naturally in the prose. Don't break flow for a definition. Weave it in.
- **Show the work, not just the result** — If the blog is about something the user built or created, don't just describe what it does. Include some of the "how we built it" and "what went into it" perspective. Readers of technical blogs are often interested in the engineering and design decisions behind a product, not just its capabilities. What tradeoffs were made? What was harder than expected? What did the team learn? This is what separates a blog from a product page.

Save the draft as a markdown file in the output directory.

---

## Phase 5: First Review

After drafting, perform a thorough self-review. Read the entire blog as a critical editor. Check every item on the review checklist.

For the full review checklist, see [references/review-checklist.md](references/review-checklist.md).

### The Review Checklist (Summary)

**AI Slop Detection:**
- Scan for phrases that sound generated rather than written. Common tells: "In today's rapidly evolving landscape", "It's worth noting that", "Let's dive in", "At the end of the day", "This is where X shines", "Without further ado". Remove or rewrite all of them.
- Watch for the pattern of stating something and then immediately restating it in different words. Humans don't do this. Cut the restatement.
- Check for excessive hedging: "perhaps", "it could be argued", "one might say". The user's voice is direct. Be direct.

**Performative Writing Filter:**
- Scan for sentences that describe the writer's physical actions or emotional reactions in a way that feels staged rather than authentic. "I sat back in my chair." "I couldn't believe what I was seeing." "A grin spread across my face." These are writing-about-writing. If a sentence describes the author's body language or internal state in a way that serves the narrative framing more than the actual story, cut it or replace it with something that advances the point.

**Cross-Blog Phrase Repetition:**
- If the research phase found previous blog posts by the user, scan the current draft for distinctive phrases that appeared in those posts. A phrase that was fresh and effective once becomes a verbal tic when it shows up in every post. Examples: "hits different", "and yet", specific metaphors or analogies. The first use was great. The second use is a crutch. Find a different way to say it.

**Em-dash Check:**
- Search the entire draft for the em-dash character. If any exist, the review fails. Replace every instance.

**One-Sentence Paragraph Check:**
- Scan for one-sentence paragraphs, especially short ones. One-sentence paragraphs are a powerful rhetorical device when used sparingly (once, maybe twice in a blog post). If there are more than two, the effect is dead. Merge short standalone sentences into adjacent paragraphs, or expand them into full paragraphs with supporting context. The user's writing rhythm is medium-to-long paragraphs with strategic single-sentence breaks, not a string of fragments.

**Sentence Rhythm Check (this is where AI writing most commonly fails):**
- Count all sentences under 10 words. If more than 20% of the blog's sentences are short, the review fails. The user's natural rhythm is medium-to-long sentences as the base. Short sentences are rare punctuation, not default mode.
- Flag any sequence of 2+ consecutive short sentences, including across paragraph breaks.
- Kill "No X. No Y. Just Z." and similar parallel fragment triplets on sight. These are AI writing tics, not human prose.
- Also flag sequences of 5+ long sentences with no variation. The rhythm needs breaks, but breaks should be one well-placed short sentence, not a cascade of fragments.

**Technical Accuracy:**
- Verify every code snippet compiles/runs conceptually. Check function names, API calls, CLI commands against what you found in the vault research.
- Verify product names, version numbers, and feature descriptions match current pgEdge terminology.
- If the blog references specific behaviour, make sure it's accurate. Don't invent capabilities.
- **Cross-reference with git history** — If the research phase found deliberate terminology changes in recent commits, make sure the blog uses the current terminology, not the old one.

**Readability:**
- Read each paragraph aloud in your head. Does it flow? Does it sound like something a human would say at a conference talk?
- Flag any paragraph longer than 6 sentences. Consider breaking it up.
- Check that the opening earns the reader's attention in the first two sentences.
- Check that the closing drives action or provokes thought, not summary.

**Authorial Intent (for existing draft reviews):**
- Before changing the tone or emphasis of any passage, ask: what was the author trying to say here? Read for the intent behind the words, not just the words themselves. If a passage describes a personal experience, preserve the author's framing of that experience. Don't reinterpret their motivations. For example, if the author frames a learning experience as "a forcing function for something I already intended to do," do not rewrite it to sound like they were unfamiliar with their own product. The author knows their own story better than you do.

**Voice Consistency:**
- Does this sound like the same person throughout? Watch for register shifts mid-piece.
- Are there any corporate buzzwords that slipped through?
- Is the language concrete and physical, or has it drifted into abstraction?

Apply all fixes from the review directly to the draft. Do not present a list of issues. Fix them. Then note what you changed in a brief summary for the user.

---

## Phase 6: Image Placement

Blog posts benefit from visual breaks. The user's narrative-style blogs in particular use images (especially meme GIFs from nerd culture) to punctuate moments of humor, irony, or dramatic reversal.

### How to Suggest Images

Read through the finalized-so-far draft and identify 3-6 natural image placement points. For each one, provide:

1. **Where it goes** — The exact sentence or paragraph break where the image should appear
2. **What kind of image** — One of: meme/GIF, diagram, screenshot, code output
3. **What it should convey** — A description of the tone and subject matter to search for
4. **Suggested search terms** — Specific enough to find something good

### Image Placement Patterns

The user's published blogs (e.g., "MM-Ready: An Origin Story") follow a specific image strategy. Two types of images serve two different functions:

**Meme GIFs — Punctuate Emotional Beats**
These go at narrative turning points, never as decoration. The pattern:

- **After a triumphant reveal** — "By the time the team came back from lunch, I had a working scanner." → [IT'S ALIVE! Frankenstein meme]. The meme amplifies the pride/surprise.
- **After a gut-punch moment** — "I'd built the right tool for the wrong workflow." → [facepalm meme]. The meme lets the reader sit with the embarrassment alongside the author.
- **After a moment of horrified realization** — "Then I showed it to Customer Success." → [WHAT'D YOU DO?!? reaction]. The meme signals "this is about to go sideways."
- **After dry self-deprecation** — Where the author is clearly laughing at themselves. The meme is the visual punchline.

The memes should come from nerd culture the author actually watches: Red Dwarf, Blackadder, sci-fi/fantasy, classic internet culture. Not generic stock-photo humor.

**Code/Terminal Screenshots — Punctuate Technical Proof**
These go where the blog makes a technical claim and needs to show, not tell:

- After describing what a tool does, show the actual output
- After explaining a setup process, show the terminal result
- After claiming something works, show it working

**General Rhythm:**
In a 2000-word narrative blog, aim for 4-6 images total. Roughly one every 300-400 words. Alternate between meme and technical as the blog alternates between narrative and proof. Never stack two images back-to-back without substantial prose between them.

### Format

Present image suggestions as markers in the draft:

```
<!-- IMAGE SUGGESTION: [meme/GIF] After "There was just one tiny problem."
Tone: comedic understatement for an impending disaster
Search: "excellent plan sir" Red Dwarf Kryten, OR Baldrick "cunning plan" Blackadder, OR similar "overconfident plan goes wrong" reaction GIF
-->
```

The user will source and place the actual images. Your job is to identify the moments and suggest the right tone.

---

## Phase 7: Feedback Loop

This phase serves two purposes: improving the current blog and improving the user's Voice Skill for future use.

### How It Works

Select 3-5 passages from the blog that you are least confident about voice-wise. These should be sentences or short paragraphs where:

- The phrasing feels generic or could have been written by anyone
- You had to make a judgment call about tone or word choice
- The technical explanation might not match how the user would actually explain it
- The transition or opening felt forced

For each passage, present it to the user and ask: **"How would you say this, in your own words?"**

Use AskUserQuestion for this, but frame each one as an open-ended rewrite request. For example:

> Here's a sentence from the draft:
> "Spock handles conflict resolution automatically, which means you don't need to write custom logic for most common scenarios."
>
> How would you say this? Feel free to rewrite it entirely, tweak a few words, or tell me it's fine as-is.

### Processing Feedback

When the user rewrites a passage:

1. **Apply it to the blog** — Use their version (or a blend if theirs needs light editing for flow).
2. **Extract voice patterns** — Note what they changed. Did they make it shorter? More concrete? Add a specific example? Change the sentence structure? These patterns become voice skill updates.
3. **Log the learning** — Keep a running list of voice observations for Phase 9.

If the user says a passage is fine, that's useful data too. It means the skill got that voice pattern right.

For detailed guidance on extracting voice patterns from feedback, see [references/voice-feedback-guide.md](references/voice-feedback-guide.md).

---

## Phase 8: Second Review & Polish

After incorporating feedback, do another full pass using the same review checklist from Phase 5. This time, pay special attention to:

- **Seams** — Places where the user's rewritten passages meet your original draft. Make sure the transitions are smooth and the voice is consistent across the boundary.
- **New issues** — Sometimes editing one paragraph creates problems in adjacent ones. Check flow around every edit.
- **Final em-dash sweep** — Run one more check. These sneak back in during editing.
- **One-sentence paragraph recheck** — Make sure edits didn't create new orphaned short paragraphs.
- **Factual consistency** — Make sure edits didn't introduce contradictions with other parts of the blog.

Apply all fixes. The blog should now be in final-draft quality.

---

## Phase 9: Finalize

### Deliver the Blog

Save the final blog as a markdown file. The filename should be descriptive: `blog-[topic-slug].md` (e.g., `blog-pgedge-mcp-server-setup.md`).

Present it to the user with a brief note on:
- Final word count
- Summary of research sources used (vault files referenced)
- Summary of voice feedback incorporated
- Image placement suggestions (if any)

### Update the Voice Skill

Based on the voice feedback collected in Phase 7, prepare updates to the user's Voice Skill:

1. **Copy the existing voice skill to a temporary working location.** The installed skill may be read-only. Copy the full skill directory (SKILL.md + all reference files) to `/tmp/ant-voice-writer/`.

2. **Apply voice learnings.** Review each piece of feedback from Phase 7 and determine what, if anything, should be added to the voice skill. Types of updates:

   - **New vocabulary preferences** — If the user consistently chose specific words over alternatives, add them to vocabulary.md
   - **New sentence patterns** — If the user restructured sentences in a consistent way, document the pattern
   - **New avoidances** — If the user rewrote away from certain phrasings, add them to the "words to avoid" lists
   - **Tone adjustments** — If the user's rewrites revealed a tone preference not captured in the skill, note it
   - **Blog-specific patterns** — If patterns emerged that are specific to blog writing (vs. other professional writing), add a blog-writing subsection if one doesn't exist

   Be conservative. Only add patterns that showed up in multiple feedback instances or that represent a clear, strong preference. A single word swap is not a pattern. Three similar rewrites that all add concrete examples where the draft was abstract is a pattern.

3. **Package the updated skill.** Use the skill-creator packaging script:
   ```bash
   python -m scripts.package_skill /tmp/ant-voice-writer/
   ```
   from the skill-creator directory.

4. **Present the package to the user** with a summary of what changed and why. Let them decide whether to install it.

---

## Edge Cases

### User provides an existing draft
If the user already has a draft they want improved, skip Phases 1-3. Start with a **deep read** of the draft to understand the author's intent, narrative arc, and emotional core. Then do a research pass (Phase 2) focused on: (a) verifying technical claims, (b) checking git history for deliberate terminology changes, and (c) finding previous blog posts to avoid phrase repetition. Then proceed to Phase 5 (First Review) onward.

The most important thing when working with an existing draft: **respect the author's intent.** Read for what they're trying to say, not just what they said. Do not reframe their experiences or motivations. If they describe something as "a forcing function for something I intended to do," that's a deliberate narrative choice. Don't change it to "I didn't know my own product."

### User only wants an outline
Stop after Phase 3. Deliver the outline and research summary. Offer to continue to drafting when they're ready.

### User wants to skip feedback
Respect it. Move from Phase 6 directly to Phase 8, and skip the Voice Skill update in Phase 9. The blog will still be good; you just won't improve the voice skill this round.

### No Voice Skill found
If there's no voice skill available, write in a professional, direct tone. During the feedback phase, note that you're collecting voice data that could be used to create a voice skill in the future. Offer to create one from the feedback collected.

### No Obsidian vault access
If the Obsidian MCP tools are unavailable, skip the vault search portion of Phase 2. Use web search and the user's local files as research sources instead. Flag this limitation to the user.
