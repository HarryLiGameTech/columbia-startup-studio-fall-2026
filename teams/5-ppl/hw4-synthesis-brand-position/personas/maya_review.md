# Maya: installed-agent brand-position review

**Date:** October 17, 2026. **Tool:** Claude Code, installed `persona-maya`, model alias `sonnet`, read-only tools.

**Result:** Initial and revised-copy runs both approved (8/10), with no must-fix items. Scores describe synthetic persona judgments, not human feedback or customer validation.

**Feedback decisions:** Adopted a separate, explicit Skip/Pause clarification and explained the Shortcuts setup requirement plus a sample-question path without setup. Deferred setup-time estimates until measured. Visual examples and default frequency are product-design follow-ups; this review does not establish their implementation.

**Actual outputs:** [Initial](runs/2026-10-17/maya-raw.txt), [revised copy](runs/2026-10-17/maya-final-raw.txt), and [tested document / reproduction metadata](runs/2026-10-17/README.md).

## Revised-copy response

```json
{
  "verdict": "approve",
  "score": 8,
  "understanding": "The document frames UnlockDrill as an opt-in, low-effort practice shortcut: one short question, visible skip/pause/frequency controls, and an explicit setup clarification that app-opening prompts need a Shortcuts automation but a sample question can be tried without that setup. This matches my situation of wanting one easy action and the ability to skip or pause when I need my phone for something real, and it does not promise an unskippable or every-opening interruption.",
  "must_fix": [],
  "nice_to_have": [
    "State up front roughly how long the Shortcuts setup takes, since 'set up an automation' still sounds like a task even if optional.",
    "Show the skip/pause buttons in the landing-page mockup copy itself (not just described) so it's visually obvious before I commit to anything.",
    "Clarify whether frequency controls default to something low out of the box, since I'd want that decided for me on day one rather than configured."
  ],
  "evidence": [
    "I03",
    "I07",
    "Q01",
    "Q02"
  ]
}
```

## Earlier review — historical record


**Recorded version:** October 9 initial-copy simulation. This is preserved history; it does not test the October 17 evidence update.

**Method:** AI-authored role simulation of the initial message “Turn phone time into SAT practice,” based on the cited interview and Reddit evidence. This was not an independently installed-agent execution or human feedback. The scores are synthetic calibration, not survey measurements.

```json
{
  "verdict": "revise",
  "score": 6,
  "understanding": "A question before opening a selected app.",
  "must_fix": [
    "Tell me how often prompts appear and whether I can skip."
  ],
  "nice_to_have": [
    "Show a short question example."
  ],
  "evidence": [
    "I03",
    "I07",
    "R1-Q1",
    "R2-Q1"
  ]
}
```

**Revision:** The current brand position names one question, chosen apps/timing, skip and pause, and topic-relevant feedback. The October 17 installed-agent runs below supersede this pending status.
