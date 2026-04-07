# Voice Feedback Guide

How to extract voice skill improvements from user feedback during the blog creation process.

## Selecting Passages for Feedback

Choose 3-5 passages that are most likely to reveal voice preferences. Prioritize:

### High-Value Targets

1. **Opening sentences** — How someone opens a piece is deeply personal. The draft's opening may be competent but not *them*. Ask.

2. **Technical explanations** — There's a huge range of ways to explain the same technical concept. Some people lead with the code, some lead with the analogy, some lead with the problem it solves. The user's preference here is a strong voice signal.

3. **Transitions** — The connective tissue between sections. These are often where AI-generated writing is most visible and where the user's natural voice is most distinctive.

4. **Opinion statements** — Any sentence where the blog takes a position. The strength of the claim, the degree of hedging, the word choices around conviction are all voice markers.

5. **Closing/takeaway** — How someone wraps up reveals their instinct about what matters. Do they end on action? On a question? On implication?

### Low-Value Targets (Skip These)

- Pure factual statements ("PostgreSQL 16 was released in September 2023")
- Code blocks (these are what they are)
- Structural elements (headers, bullet point formatting)
- Passages where you're confident the voice is right

## Asking for Feedback

Frame each request as a rewrite invitation, not a yes/no approval. The goal is to get the user to actually write, not just evaluate.

### Good Framing

> Here's how I wrote the opening:
>
> "Most teams don't think about distributed databases until their single-node PostgreSQL instance starts buckling under cross-region latency. By then, they're deep into an architecture that wasn't designed for it."
>
> How would you open this? Write it however feels natural. If this already sounds like you, just say so.

### Bad Framing

> "Is this opening okay?" — Gets a yes/no, not a voice sample
> "Rate this passage 1-5" — Gives you a number, not language
> "What would you change?" — Too vague; often gets "it's fine"

### Encouraging Authentic Responses

Some users will try to "help" by writing in a polished, formal way that isn't their actual voice. If a rewrite feels over-edited or stiff, gently push:

> "That's helpful. Now imagine you're explaining this to a colleague over coffee. How would you actually say it?"

## Extracting Patterns from Feedback

When the user rewrites a passage, analyze the delta between your version and theirs along these dimensions:

### Sentence Structure

| Signal | What It Means | Voice Skill Update |
|--------|--------------|-------------------|
| User shortened your sentences | They prefer tighter prose in this context | Note the context where brevity is preferred |
| User combined your sentences | They prefer flowing, connected prose | Note the context where longer sentences work |
| User broke your long sentence into fragments | They use fragments more than the skill suggests | Adjust the short/long ratio guidance |
| User added a parenthetical aside | They think in asides | Add parenthetical usage as a pattern |

### Word Choice

| Signal | What It Means | Voice Skill Update |
|--------|--------------|-------------------|
| User replaced a formal word with a casual one | The formal register was too high | Add the word swap to vocabulary preferences |
| User replaced a generic verb with a physical one | They want more concrete language | Reinforce the physicality patterns |
| User replaced your word with a domain-specific term | They have preferred terminology | Add to the preferred terms list |
| User added profanity or informal language | The tone can be more casual than the skill currently allows for blogs | Note the context where casual tone is permitted |

### Structural Choices

| Signal | What It Means | Voice Skill Update |
|--------|--------------|-------------------|
| User rewrote to lead with a question | They like rhetorical questions as openers | Add to structural patterns |
| User rewrote to lead with an example | They prefer concrete-first over abstract-first | Reinforce the "open with what matters" pattern |
| User added a "and yet" or similar pivot | The skill's pivot phrases are confirmed | No change needed (confirmation is useful data) |
| User removed hedging language | The skill's directness guidance is understated | Strengthen the "be direct" guidance |

### Confirmed Patterns

When a user says "this is fine" or doesn't change a passage, that's also data. It means the skill correctly predicted their voice for that type of content. Track what worked so you don't accidentally remove good patterns in future updates.

## Applying Updates to the Voice Skill

### Rules for Voice Skill Updates

1. **Require pattern confirmation.** A single word swap is not enough to update the skill. Look for patterns: the same type of change appearing 2+ times, or a single change that's strong and unambiguous (like "never start a blog with a question" after the user rewrote away from that structure).

2. **Be conservative with additions.** The voice skill should grow slowly. Adding too much from a single blog session risks overfitting to one piece of content. If you're not sure a pattern is generalizable, note it in a comment rather than adding it as a rule.

3. **Never remove existing patterns based on one session.** If the user's feedback contradicts something in the current voice skill, flag the tension rather than resolving it. Example: "The voice skill says to avoid short sentences, but in this blog the user chose several. This might be blog-specific or it might indicate the ratio guidance needs adjustment. Flagging for review."

4. **Organize by context.** If a pattern is specific to blog writing (vs. all professional writing), put it in a blog-specific section. The voice skill should capture context-dependent patterns, not just universal rules.

5. **Preserve the user's words.** When adding examples to the voice skill, use the user's actual rewrites as the examples. Their phrasing is the ground truth.

### Update Format

When presenting voice skill updates to the user, structure them as:

> **What I noticed:**
> In 3 out of 4 feedback passages, you replaced abstract descriptions with specific technical examples. For instance, you changed "efficient replication" to "replicating a 50GB table in under 3 minutes."
>
> **Proposed skill update:**
> Add to Professional Writing → Blog subsection: "When making capability claims, always anchor them in specific, quantified examples. Not 'fast replication' but 'replicates a 50GB table in under 3 minutes.'"
>
> **Should I add this?**

Let the user approve each update before applying it.
