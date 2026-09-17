# In-app copy

Loaded when the page itself is in-app copy: tooltips, help icons,
confirm dialogs, empty states.

Tooltips, help icons, confirm dialogs and empty states are
documentation too, written to a tighter budget.

- Define the thing it sits on in plain words and stop. One sentence
  is the norm, two is the ceiling.
- If the label already says it, write nothing. "None" is a valid
  answer. The test is whether the text adds something the label and
  value do not.
- No timing or transition claims. The status change is the signal. A
  docs page may state a duration where the reader needs one to act;
  in-app copy never does.
- A failed state names the one action available, nothing about
  bookkeeping.
- A confirm dialog states the action and the one consequence the user
  must know, not the timing or the internal mechanics.
- When one sentence is not enough, keep the one sentence and link to
  the page that owns the detail.
- Buttons carry no hover tooltip; the explanation sits in a help icon
  beside the control. An icon-only button keeps its short
  accessible-name hover label, which is not an explanation.
