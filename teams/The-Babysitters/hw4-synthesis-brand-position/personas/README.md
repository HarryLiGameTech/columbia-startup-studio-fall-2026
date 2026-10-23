# Persona agents v1 for Claude Daycare

Five synthetic judge personas for Claude Daycare, one per user segment that the ten interviews and
the Reddit research pointed to, and the one verdict format they all return. They are grounded in
the ten interviews and in Reddit comments from 39 saved threads (see `reddit_research/`). Every
field the evidence does not support is still marked `TODO — needs interview`. Read
`NOTES — grounding gaps.md` for what is grounded, what is still TODO, and the test results.

Claude Daycare is the team's own product (site: claudedaycare.com). The personas judge copy, pages
and feature ideas for it, in particular the focus feature chosen on 2026-10-09, Allowance
Guardrails (protect the usage you need for real work while your agent plays). Every persona file
carries the same short list of what the product does today and what is only proposed, read from the
site, from the runner's code and (since 2026-10-11) from the runner's own README, so a persona never treats an idea as shipped. The README parts (what a visit is, a sealed workspace, fake money) are the README's own account and have not been checked against code.

## The personas

| Persona | Segment | Evidence | File |
|---|---|---|---|
| Wren | Owner-paid coder who guards the weekly allowance | interviews 3, 4, 5 (no exact quotes); Reddit voices who pace their week and leave headroom | `persona-wren.md` |
| Rowan | Sets limits first, then lets automation run | interview 7 (H5, H6, H8, H11, H13); Reddit voices who set limits before running agents unattended | `persona-rowan.md` |
| Marlow | Curious student who cannot name a use and worries about outside input | interview 6 (M5, M7, M8, M9) and, as a partial fit, interview 8 (E4); Reddit student voices on cost | `persona-marlow.md` |
| Emery | Supervising professional on work-funded access | interviews 9, 10 (paraphrase only); Reddit voices on work accounts and approvals | `persona-emery.md` |
| Quinn | The one with allowance to spare, who rarely comes near the limit | Reddit only; no interview describes this segment | `persona-quinn.md` |

Quote IDs (M, H, E plus a number) are rows in the team's quote index note. Interviewees are cited
by interview number and quote ID only. Reddit comments are cited as `[Reddit thread/comment]`, with
the link in the Voices section of the file and in `reddit_research/quotes_used.md`; Reddit voices
are different people, so where a file draws on several of them it says so. The first names are
invented placeholders with no meaning; no persona is a real person.

## The shared verdict format

Every persona returns exactly one JSON object and nothing else. This block shows the format only;
it is not a real verdict.

```json
{
  "persona": "persona-wren",
  "artifact": "draft description of a paid planning tier",
  "verdict": "approve_with_conditions",
  "score": 6,
  "headline": "One sentence that sums up the judgment.",
  "must_fix": ["Only things that would make this persona stop using it or refuse to pay."],
  "nice_to_have": ["Preferences and polish. Never blocks sign-off."],
  "in_character_reaction": "Two to four sentences in the persona's voice.",
  "would_flip_me": "The smallest change that moves the verdict up one band.",
  "would_pay": false
}
```

| Field | Type | Meaning and rule |
|---|---|---|
| `persona` | string | The agent's name. It must equal the file name without `.md`, for example `persona-wren`. |
| `artifact` | string | A short label for what was judged. |
| `verdict` | string | One of `approve`, `approve_with_conditions`, `reject`. It must match the score band. |
| `score` | integer | 1 to 10, whole numbers only. |
| `headline` | string | One sentence that sums up the judgment. |
| `must_fix` | list of strings | Only things that would make this persona stop using the product or refuse to pay. Empty if and only if the verdict is `approve`. |
| `nice_to_have` | list of strings | Preferences and polish. Never blocks sign-off. May be empty. |
| `in_character_reaction` | string | Two to four sentences in the persona's own voice. |
| `would_flip_me` | string | The smallest change that moves the verdict up one band. Required, and not empty, on every `reject`; give it on `approve_with_conditions` too. On `approve` it is an empty string. |
| `would_pay` | `true`, `false` or `"n/a"` | Whether this persona would pay for what the artifact offers. `"n/a"` when the artifact is not for sale. |

### Hard rules

1. Score bands: 7 to 10 is `approve`, 5 to 6 is `approve_with_conditions`, 1 to 4 is `reject`.
   The verdict must match its band. A 6 labelled `approve` is a broken verdict.
2. `must_fix` is empty if and only if the verdict is `approve`. A conditions or reject verdict with
   an empty `must_fix` is broken, and so is an approve with anything in it.
3. Every `reject` includes a non-empty `would_flip_me`.
4. `would_pay` is `"n/a"` when the artifact is not for sale (a logo, a style page, a brand
   statement). Use `true` or `false` only when the artifact asks for money or describes a priced
   offer.
5. Return only the JSON object. No text before or after it.
6. Nitpicks go in `nice_to_have`. `must_fix` is for things that would actually make the persona
   stop using it or refuse to pay.

## How to run a persona

1. This folder is the source of truth. Later, copy the persona files you want into the `.claude/agents/`
   folder of the product repo. The class repo ignores `.claude/`, so files left only there would
   not be committed; the copies in `personas/` are what gets handed in. Keep the two in sync by
   editing here and copying over.
2. In Claude Code, ask for one persona by name and hand it one artifact, inline or as a file path.
   For example: use the persona-wren agent to judge `docs/brand_position.md`. Say whether the
   artifact is for sale, so `would_pay` can be answered honestly.
3. Each agent only has Read, Grep and Glob. It can read the files you point it to. It cannot use the
   product, browse, or run anything.
4. Save each returned JSON object next to the artifact it judged, then write one short note per
   persona on what it said.
5. Run every persona on the same artifact, so the verdicts can be compared.

## How to read the results

- **Ignore the praise.** Read `must_fix` and `would_flip_me` first. Those are the dealbreakers and
  the smallest changes that would move a verdict.
- **Look for disagreements.** Two personas that split on the same artifact point to two audiences,
  or to a claim that works for one segment and fails another. `NOTES — grounding gaps.md` lists
  where each pair is expected to split.
- **If every persona agrees, they are not specific enough.** Treat that as a bug in the personas,
  not as good news, and go back to the evidence.
- **Known failure modes:** answers that are too nice, personas that give suspiciously similar
  feedback, no ability to use the product, and a stereotype of a group in place of the group's own
  view. Grounding in real quotes is what partly fixes the last two.
- **A persona is not a user.** Its verdict is a prompt for what to check with real people. Real
  traffic and real interviews still get the final vote. A persona judging an AI-written draft is
  not evidence about the draft.
- **Loop:** build the personas, draft, ask each persona, revise, ask again.

## House rules for editing these files

- A quotation mark means exact words. Put a quote in only if it appears verbatim in the team's
  quote index (with its ID) or in a saved Reddit comment (with its link), and only in the persona
  whose segment the speaker belongs to. The Reddit quotes in these files were put in by script from
  `reddit_research/quotes.jsonl`, which checks each one against the saved comment.
- Never turn a paraphrase into a quote. Interviews 1 to 5, 9 and 10 have no exact quotes.
- If the evidence does not support a field (age, city, job, income, numbers, tools, a score),
  write `TODO — needs Reddit quote` or `TODO — needs interview`. Do not fill it with something
  plausible.
- Say whether an Allowance Guardrails idea is proposed or shipped. Today's behaviour comes from the
  site and the runner, not from the team's canvas.
- No real names, no school or employer names, no personal relationships, nothing that could identify
  an interviewee, and no Reddit usernames.

## Grounding status

Version 1, 2026-10-11. Grounded in the ten interviews and in Reddit comments from 39 saved threads.
Reddit evidence is a composite of different people, not one person's
life, so it fills voice, money, tools and what people were burned by. It cannot honestly fill age,
city, job or credentials, which stay TODO until an interview supplies them.

| Persona | Exact interview quotes | Reddit quotes in the file | Main gap |
|---|---|---|---|
| Wren | none exist | 4 | The limit concern comes from one relayed interview; age, job, setup patience and how often a limit is hit are TODO |
| Rowan | 5 (H5, H6, H8, H11, H13) | 2 (plus others cited inline) | One interviewee; money, skepticism and background are TODO |
| Marlow | 4 from interview 6, 1 from interview 8 | 3 | One interviewee for the core. No Reddit student said they cannot name a task, and none worried about outside input, so those two traits rest on interview 6 alone |
| Emery | none exist | 4 | Two interviews that differ on whether a personal plan exists; Reddit voices split the same way; no exact interview words |
| Quinn | none: no interview | 5 (plus others cited inline) | Reddit only. This segment was found in the research, not the interviews, and needs at least one interview before its numbers are trusted |

The order above is the order of the segments, not a ranking. The full list of grounded and TODO
fields per persona, where the personas should disagree, and the test results are in
`NOTES — grounding gaps.md`.
