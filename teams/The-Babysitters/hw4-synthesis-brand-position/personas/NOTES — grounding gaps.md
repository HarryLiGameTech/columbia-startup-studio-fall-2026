# NOTES — grounding gaps

What is grounded, what is still TODO, and what has to happen before the four persona files in this
folder are tested. Written 2026-10-09. The personas are listed in the order of the segments in the
brief; that order is not a ranking, and nothing here ranks one persona above another.

## How to read the citations in the persona files

| Mark | Meaning |
|---|---|
| `[interview N]` | A paraphrase recorded in the team's interview notes or working synthesis. No exact words exist. |
| `[interview N; H5]` or `[H5]` | Exact words. The ID is a row in the team's private quote index; the letter groups quotes by speaker there. |
| `TODO — needs Reddit quote` or `TODO — needs interview` | The evidence does not support the field. Nothing was filled in to look complete. |
| `derived` | Inferred from the cited evidence. It is not something the interviewee said. |
| `synthetic` | Written for the persona, not a quote. The check script confirms no synthetic line shares five or more words in a row with any quote in the index. |

## What evidence exists

| Interview | Used in | Exact words in the quote index | Basis, from the working synthesis |
|---|---|---|---|
| 3 | Wren | None | A teammate's recollection, relayed afterward and written up later than an hour; several bullets are word-for-word identical across interviews 1 to 3, so they read as one account |
| 4, 5 | Wren | None | The interviewer's recollection, written within the hour |
| 6 | Marlow | M1 to M9 | Live dialogue, speech-to-text |
| 7 | Rowan | H1 to H13 | Live dialogue, speech-to-text |
| 8 | Marlow, as a partial fit | E1 to E7 (E7 is the least certain) | Live dialogue, speech-to-text; the interview ended before a reaction to daycare was recorded |
| 9, 10 | Emery | None | The interviewer's recollection, written within the hour |
| Reddit | All four | None yet | Pages are saved by hand by a team member; no agent fetches Reddit |

Interviews 6 to 10 were all run by the same interviewer with people the interviewer knows, which raises
the usual risk that answers were polite. The working synthesis the evidence comes from is itself an AI
draft that nobody on the team has reviewed.

## Decisions made in this draft

1. **Four personas, no merge.** Each one rests on one or two interviews, which is thin. Merging
   two would produce a composite that averages two people, and an average is what makes personas
   agree. The four also split along lines the interviews themselves show: who pays for the allowance,
   who watches every step, who sets limits and then lets it run, and who sees no use at all. If the
   team wants three after the Reddit round, it should choose which segments fold together then. This
   draft does not choose.
2. **Wren is a stitched segment.** The brief grouped interviews 3, 4 and 5. The weekly-allowance
   worry and the plan to use daycare only near the weekly reset come from interview 3 alone, and
   that is a relayed account. Interviews 4 and 5 supply only the $100 a month Claude Max price, plus
   two small concerns (a long recap becoming extra reading; no obvious task to leave running).
   Neither records a usage-limit worry, and interview 4's notes say the participant does not use
   Claude Code. A second source for the limit worry exists, but it sits in Emery's segment (interview
   10). The persona file says all of this in its own words and leaves the rest TODO.
3. **Emery joins two interviews that differ.** Interview 9 supervises every step and reported
   personal access plus a work allowance; interview 10 has company API access only, no personal plan,
   and would not spend work tokens on play. They share employer-funded access and software work. The
   persona file states the difference and leaves the open question (is there a personal plan?) as
   TODO. Splitting them is an option once there is more evidence.
4. **Interview 8 sits in Marlow, as a partial fit.** It is a student who uses a chatbot every day
   and worries about AI taking over recreational and creative things (E3, E4). That is the nearest
   match to a persona whose worry is about what AI does beyond a task, and it makes Marlow and Rowan
   differ on recreational AI. It does not fit Wren (no coding agent in the record, and E7 is the
   least certain line), Rowan (no automation) or Emery (no employer-funded access). The fit is
   partial: the worry is about AI's reach, not about outside input changing one's own Claude, and no
   reaction to daycare was recorded. So only E3 and E4 are used, E4 is the single quote placed in
   the persona, and unease about AI taking over play is a `nice_to_have` trigger, never a `must_fix`.
   E1, E2, E5, E6 and E7 are unused: they are general attitudes, everyday use, or (E7) a ChatGPT
   plan question that would pull Marlow toward Wren.
5. **H3 is cited, not quoted.** The exact words name a personal relationship, which the brief
   rules out. Rowan's file states the fact (access funded by someone else) and cites H3 by ID.
   H12 is unused: it is playful, and the interview note says no product concern should be read into
   it. H4 is cited only to say its meaning was never explored.
6. **Interview 6's work-provided Claude Max access is left out of Marlow.** It is in the interview
   note. Carrying it into Marlow would blur the line with Emery, whose defining trait is work-funded
   access. Only the personal $20 plan is in the file. Revisit if the Reddit round shows students on
   work accounts.
7. **No pronouns, no demographics.** The names are invented placeholders and the files avoid gendered
   pronouns, so no persona reads as a particular real person. Study field, setting, employer and
   relationships from the interview notes are left out on purpose. Participants A, B and C asked for
   anonymity and nothing here identifies them.

## Quote IDs, where they went

| ID | Placed in | Treatment |
|---|---|---|
| M5, M7, M8, M9 | Marlow | Quoted in full |
| M1, M2, M3, M4, M6 | Marlow | Cited by ID in prose, not quoted |
| E4 | Marlow | Quoted, labelled secondary voice, partial fit |
| E3 | Marlow | Cited by ID in prose, not quoted |
| E1, E2, E5, E6, E7 | None | Unused, see decision 4 |
| H5, H6, H8, H11, H13 | Rowan | Quoted in full |
| H1, H3, H4, H7, H9, H10 | Rowan | Cited by ID in prose, not quoted (H3 and H4 for the reasons in decision 5) |
| H2, H12 | None | Unused |

The check script confirms every double-quoted passage tagged with an ID is verbatim in the quote
index under that ID, and that an ID appears only in the file of its speaker's segment (M and H in
their own persona, E in Marlow by decision 4). The script lives in the working session's scratch
area and is not part of this folder.

## Grounded and TODO, field by field

Status words: grounded (with the source), partly grounded, derived, synthetic, or TODO (with where
it must come from). Reddit below means a quote with link and date; interview means a follow-up
conversation. The three template fields that every file shares (the opening instruction, the
verdict JSON block, the hard rules) are process text, not evidence, and are not listed.

### Wren (owner-paid coder who guards the weekly allowance)

| Field | Status | Source, or where it must come from |
|---|---|---|
| name, `persona-wren` | Invented | A placeholder with no meaning |
| description | Partly grounded | Claude Max, coding, five-hour and weekly limits [interview 3]; the list of things judged is derived from the recorded concerns |
| Age, city, job, credentials | TODO | Reddit or interview |
| Time doing this, what came before | TODO | Reddit or interview |
| Plan | Grounded | Claude Max [interview 3] |
| Monthly price | Partly grounded | $100 recorded for interviews 4 and 5; not recorded for interview 3 |
| Limits planned around | Grounded, one relayed account | Five-hour and weekly [interview 3] |
| How often a limit is hit, and the cost | TODO | Reddit (a gap named in the working synthesis) |
| Workarounds | Partly grounded | Use daycare only near the weekly reset [interview 3]; anything else TODO from Reddit |
| skepticism_level, 3 / 5 | Derived, provisional (an AI inference) | Skeptical at first, then open [interview 3, relayed] |
| price_sensitivity | TODO | Interview: who pays, how a price is weighed |
| tech_savviness | TODO | Interview: terminal or chat use |
| patience_for_setup | TODO | Interview |
| Backstory | Partly grounded | One supported sentence [interview 3]; how they got here and what a limit costs are TODO from Reddit |
| Belief: allowance is for real work | Grounded | [interview 3] |
| Belief: play near the weekly reset | Grounded; the reason is inferred | [interview 3] |
| Belief: what the agent can do and what could leak | Grounded, relayed | [interview 3] |
| Belief: long recaps are extra reading | Grounded | [interview 4] |
| Belief: no task to leave running | Grounded | [interview 5] |
| Burned by | TODO | Reddit: a specific limit-hit incident |
| Red lines | Derived | From the concern in interview 3; not stated ultimatums |
| Tone | TODO | Reddit; no exact words exist |
| Synthetic example lines | Synthetic | Written for the persona |
| Exact quotes | None exist | No exact words from interviews 3, 4 or 5 |
| Reddit slots (2) | TODO | Reddit: describing a weekly or five-hour limit; what a paying user does when it hits |
| Baseline | Grounded | [interview 3] |
| Earns yes, makes reject | Derived | From the beliefs; items marked derived are inferences |
| Worked examples | Synthetic | Written to differ from the other three; the cap is labelled proposed |

### Rowan (sets limits first, then lets automation run)

| Field | Status | Source, or where it must come from |
|---|---|---|
| name, `persona-rowan` | Invented | A placeholder with no meaning |
| description | Grounded | H5, H8 (the bots), H11 (the limits) |
| Age, city, job, credentials | TODO | Interview |
| Time doing this, what came before | TODO | Interview |
| Who funds access | Grounded | H3, cited by ID, not quoted (decision 5) |
| Value of a tool or visit in money | TODO | Interview |
| Tools and workarounds | Grounded | H5 (job-search bot), H8 (trading bot), H7 (reads writing before sending), H1 (everyday use) |
| Models and plans behind the bots | TODO | Interview; the interview note says the exact capabilities were never established |
| skepticism_level | TODO | Interview; the signals pull both ways (H8 against H7, H11) |
| price_sensitivity | TODO | Interview; only who funds the access (H3) and the paid-test condition (H13) |
| tech_savviness, 4 / 5 | Derived, provisional (an AI inference) | H5, H8; whether the bots were built or configured is not recorded |
| patience_for_setup | TODO | Interview |
| Backstory | Grounded, partly | H1, H5, H7, H8, H9, H10, H11, H13; the reason for avoiding AI (H4), a normal week and fears are TODO from an interview |
| Belief: limits first, then autonomy | Grounded | H8 |
| Belief: only what it is told | Grounded | H6 |
| Belief: reads writing before it goes out | Grounded | H7 |
| Belief: nothing money-related, nothing public | Grounded | H11 |
| Belief: fun uses | Grounded | H10 |
| Burned by | TODO | Interview |
| Red lines | Grounded (stated) and derived | Money and public posting: H11. The other two are marked derived |
| Tone | Grounded | Judged from H6, H8, H11 |
| Synthetic example lines | Synthetic | Written for the persona |
| Exact quotes | Grounded | H5, H6, H8, H11, H13, checked by script |
| Reddit slot (1) | TODO | Reddit: someone who automates tasks describing limits before letting an agent run alone |
| Baseline | Grounded | H3, H5, H7, H8 |
| Earns yes, makes reject | Derived | From H8, H10, H11, H13 |
| `would_pay` default (false) | Placeholder | TODO — needs interview; based only on H3 and H13 |
| Worked examples | Synthetic | The cap is welcome only if the owner sets it |

### Marlow (curious student who cannot name a task)

| Field | Status | Source, or where it must come from |
|---|---|---|
| name, `persona-marlow` | Invented | A placeholder with no meaning |
| description | Grounded | M1, M5, M6, M7, M8 |
| Student, uses AI for class work and emails | Grounded | M1 |
| Age, city, year, field of study | TODO | Interview |
| Time doing this, what came before | TODO | Interview |
| Personal plan, $20 a month | Grounded | [interview 6] (from the interview note and working synthesis, not from the quote index) |
| What a visit is worth in money | TODO | Interview |
| Tools | Grounded | Claude Code or Claude in the browser: M4; other more useful tools not adopted: M5 |
| skepticism_level, 3 / 5 | Derived (an AI inference) | M5, M7, M8, M9 |
| price_sensitivity | TODO | Interview |
| tech_savviness, 3 / 5 | Derived, provisional (an AI inference) | M4 |
| patience_for_setup | TODO | Interview |
| Backstory | Grounded, partly | M1, M2, M5, M6, M7, M8, M9, interview 6 (yes to an early test); hangouts, past attempts, switching triggers TODO from an interview |
| Beliefs on AI use, tuned Claude, telling it what to do, friends' agents | Grounded | M2, M3, M6, M7, M8 |
| Belief on AI taking over recreation | Grounded, partial fit | E3, E4 from interview 8 (decision 4) |
| Burned by | TODO | Interview |
| Red lines | Derived | From M6, M7; the no-benefit blocker from M5, M8 |
| Tone | Grounded | Judged from M5, M7, M8 |
| Synthetic example lines | Synthetic | Written for the persona |
| Exact quotes | Grounded | M5, M7, M8, M9 and E4, checked by script |
| Reddit slot (1) | TODO | Reddit: a student describing having no idea what to do with an agent that works alone |
| Baseline | Grounded | M1, M4, M5 |
| Earns yes, makes reject | Derived | From M5 to M9 |
| Worked examples | Synthetic | The cap pitch is a fail here because it does not answer the benefit question |

### Emery (supervising professional on work-funded access)

| Field | Status | Source, or where it must come from |
|---|---|---|
| name, `persona-emery` | Invented | A placeholder with no meaning |
| description | Grounded | [interviews 9, 10] |
| Software engineer | Grounded | [interviews 9, 10] |
| Age, city, seniority, credentials | TODO | Interview |
| Time doing this, what came before | TODO | Interview |
| Funding | Partly grounded | Work-funded in both; whether a personal plan exists differs between interviews 9 and 10, so it is TODO from an interview |
| Token limits, extra tokens requested | Grounded | [interview 10] |
| Tools and workarounds | Grounded | Manual approval, every step checked [interview 9]; asking the employer for more tokens [interview 10] |
| skepticism_level, 4 / 5 | Derived, provisional (an AI inference) | [interview 9]; the 7/10 worry was rated by the interviewer, not by the participant |
| price_sensitivity | TODO | Interview |
| tech_savviness, 4 / 5 | Derived (an AI inference) | [interviews 9, 10] |
| patience_for_setup | TODO | Interview |
| Backstory | Grounded, partly | [interviews 9, 10]; how they got here and what they need to see before trusting a visit are TODO |
| Beliefs (oversight, work tokens, unsupervised worry, supervised play, not for me) | Grounded | [interviews 9, 10] |
| Burned by | Grounded, thin | Claude doing things differently from what was wanted, no incident [interview 9]; running short of tokens [interview 10] |
| Red lines | Grounded (stated) and derived | No work tokens on play [interview 10]; the no-approval, no-visibility line is derived |
| Tone | TODO | Reddit or interview; no exact words exist |
| Synthetic example lines | Synthetic | Written for the persona |
| Exact quotes | None exist | No exact words from interviews 9 or 10 |
| Reddit slots (2) | TODO | Reddit: engineers on employer-funded access; people who approve every agent action |
| Baseline | Grounded | [interviews 9, 10] |
| Earns yes, makes reject | Derived | From [interviews 9, 10] |
| `would_pay` default (false) | Placeholder | TODO — needs interview; based on employer-funded access only |
| Worked examples | Synthetic | The cap pitch is a fail here because it does not answer whose tokens are spent |

## Where the personas should disagree, and on what

These are expected tendencies written from the evidence. They are hypotheses to test, not results,
and a cell that says TODO has no evidence behind it yet.

| Artifact or claim | Wren | Rowan | Marlow | Emery |
|---|---|---|---|---|
| A pitch for a hard per-visit cap, labelled proposed | Leans approve if enforcement is explained: the allowance is their own and the worry is spending it [interview 3] | Leans approve with conditions: likes ceilings [H8] but wants to set them (and keep money and public posting out of reach) [H11] | Leans reject: safety is not the question, the benefit is [M5, M8] | Leans reject: the objection is whose tokens are spent, not how many [interview 10] |
| Your agent works while you are away; read the report later | Conditions: what the agent can do and what could leak [interview 3]; no obvious task [interview 5] | Leans approve if the limits are the owner's [H8, H11] | Leans reject or conditions: cannot name a task [M8] | Leans reject: wants to watch every step [interview 9] |
| Your agent meets other agents | Conditions: leaks through a public forum [interview 3, relayed] | Approve if private only [H10, H11] | Conditions: friends yes, unfamiliar input no [M6, M7, M9] | TODO — needs interview (no reaction to other agents recorded) |
| AI doing recreational or creative things | TODO — needs interview | Welcomes it [H10] | Mixed: curious about friends [M9], with a milder voice of unease [E3, E4] | Interested if supervised [interview 9]; not on work tokens [interview 10] |
| A priced offer | TODO — needs interview (pays for Claude Max today [interview 3]) | Defaults to false; wants to be paid to test [H13] | TODO — needs interview ($20 plan [interview 6]) | Defaults to false; access is employer-funded [interview 10] |
| A long report to read after a visit | Dislikes extra reading [interview 4] | TODO — needs interview (what makes a recap worth reading was never established) | TODO — needs interview | TODO — needs interview |

The pairs that should split most clearly:

- **Wren and Emery on the cap pitch.** Both raise limits [interviews 3, 10]: interview 3 worried about them, interview 10 has hit them. One is a paying Claude Max user (Mitchell's recollection)
  and is inferred to want the allowance protected (an inference); the other does not want to spend work tokens at all,
  so a cap does not answer the objection.
- **Rowan and Emery on autonomy.** Rowan lets automation act alone inside limits [H8]; Emery
  approves and checks every step [interview 9].
- **Rowan and Marlow on recreational AI.** Rowan wants poems, research and TikToks [H10]; Marlow's
  partial-fit voice does not want AI to take over play [E3, E4].
- **Wren and Marlow on what the question is.** One is asking how much it costs; the other is
  asking what it is for.

If every persona returns the same verdict on these artifacts, the personas are not specific
enough. Go back to the evidence column and add or fix detail before trusting any result.

## What must happen before anyone tests these

1. **Reddit grounding first.** A team member opens and saves the Reddit pages by hand; no agent
   fetches Reddit. Then fill each open slot with an exact quote, its link and its date, and update
   the profile scores and the TODO fields that Reddit can honestly support. Suggested things to
   look for, per persona:
   - Wren: how users describe running into the weekly or five-hour limit, what they do about it,
     and what they pay.
   - Rowan: people who let agents run unattended and the limits they set first; what they accept
     as a safe output.
   - Marlow: students who use an agent daily and say they have no idea what to leave it doing;
     worries that outside input changes a tuned assistant.
   - Emery: engineers on company-funded access, how they treat personal use of work tokens, and
     people who approve every agent action.
   Fields like age, city and credentials cannot honestly come from Reddit; they stay TODO until an
   interview supplies them.
2. **Do not test against the brand position yet.** A brand position v0 is being drafted at the
   vault note `4b — Brand position (Claude draft v0).md`. Testing waits for Reddit. Once both
   exist, run all four on the same artifact and write one short note per persona on what it said.
3. **Re-check the product facts block.** Every persona file carries the same short list of what the
   site does today and what is only proposed. It comes from the site's home page as summarised in
   the team's notes, read 2026-10-09; the runner's code was not checked for this draft. Update all
   four files in one pass once the repo study says how the allowance is measured and enforced.
4. **Ask each quoted interviewee.** The quote index asks that each named person be checked with
   before a quote is used anywhere public. The persona files use no names, but anyone who knows
   the speaker could recognise the words, and the ID letters only group quotes by speaker in a private index. If this
   folder goes anywhere public, check first, and consider renaming the IDs in both places.
5. **Have the team review the `derived` lines.** They are inferences from the evidence, written by
   an AI. A person should confirm or strike each one.
6. **Install copies, then keep them in sync.** Copy the files to `.claude/agents/` of the product
   repo only when testing starts, and edit the copies here first.

## Limits of this draft

- Nothing here has been tested. No persona has been run on any artifact.
- The interview evidence was read from the vault notes, not from recordings. Interviews 3, 4, 5, 9
  and 10 are recollections; none has a verbatim transcript.
- The product facts come from a summary of the site's home page. They were not checked against the
  runner's code or against the live site again.
- The brand position draft and the repo study were not read for this work.
- Unsupported fields are marked TODO rather than guessed, so each file is thin by design.

---

## Update 2026-10-11: Reddit grounding and the first tests

This section is newer than everything above it. Where the two disagree, this section wins.

### What changed

1. **Reddit grounding.** The Reddit research (39 threads, `reddit_research/`) filled the Reddit slots in all four personas with exact, checked quotes (link and date in each file) and let some TODO fields be filled as derived, provisional values: price sensitivity (Wren 3/5, Marlow 4/5), tech savviness (Wren 4/5), tone, and what each persona was burned by. Reddit comes from different people, so a persona that draws on it is a composite for those fields, and each file says so. Age, city, job and credentials stay TODO everywhere, because Reddit cannot supply them.
2. **A fifth persona, Quinn (the one with allowance to spare).** The research found a segment the interviews missed: people who rarely come near the limit and ask what to do with the extra. Quinn rests on Reddit only. No interview describes this segment, so interview someone before trusting its numbers.
3. **Product facts corrected, twice.** First from the repo study (the cap is checked between turns, the crossing turn finishes, two homecoming turns run after it, the meter reads whole points, a local usage line exists). Then after the first test: that run wrongly told the personas that a stop in the middle of a turn was only proposed. For OpenCode it is shipped (the token count is live). Five personas flagged a correct sentence on both style pages as an overclaim. The facts were fixed and everything was run again; the first run's results are void and kept outside this folder.
4. **Marlow's two traits that Reddit did not support.** No Reddit student said they cannot name a task for an agent, and none worried about outside input changing a tuned assistant. Those two traits still rest on interview 6 alone.

### How it was tested

Ten artifacts, each judged by each persona in a fresh agent that read only its own persona file and the one artifact (50 runs), then three more runs of every persona on the three real artifacts (45 runs). In `tests/artifacts/`: A1 the brand position draft v0, A2 and A3 the text of the two style pages, A4 a control that overclaims ("hard cap", "never run out"), A5 a control that talks only about play, and A6 to A10 positive controls: copy written to pass for Wren, Rowan, Marlow, Emery and Quinn in that order. The positive controls are hypothetical copy written for this test, and some assume statements about the product that nobody has checked. Every verdict is in `tests/verdicts/<artifact>.md`, and none broke a hard rule of the verdict format.

**First run on all ten artifacts (after the fix):**

| Persona | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | A9 | A10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Wren | approve 7 | approve 7 | conditions 6 | reject 2 | reject 4 | approve 8 | approve 7 | conditions 5 | approve 7 | approve 7 |
| Rowan | conditions 6 | approve 7 | approve 7 | reject 2 | conditions 5 | approve 7 | approve 8 | conditions 5 | approve 7 | approve 7 |
| Marlow | reject 4 | reject 4 | reject 3 | reject 3 | reject 4 | reject 4 | reject 4 | approve 8 | conditions 5 | reject 4 |
| Emery | approve 7 | conditions 5 | reject 4 | reject 2 | reject 3 | conditions 6 | reject 3 | reject 4 | approve 8 | reject 4 |
| Quinn | conditions 6 | conditions 6 | conditions 5 | reject 2 | conditions 5 | conditions 5 | conditions 6 | approve 7 | approve 7 | approve 8 |

**The three real artifacts, four runs each:**

| Persona | A1 brand position | A2 Off Hours page | A3 Inside the Lines page |
|---|---|---|---|
| Wren | scores 7 to 7, median 7; 4 approve, 0 conditions, 0 reject | scores 6 to 7, median 6; 1 approve, 3 conditions, 0 reject | scores 6 to 7, median 6; 1 approve, 3 conditions, 0 reject |
| Rowan | scores 6 to 7, median 6.5; 2 approve, 2 conditions, 0 reject | scores 6 to 7, median 6.5; 2 approve, 2 conditions, 0 reject | scores 6 to 7, median 6; 1 approve, 3 conditions, 0 reject |
| Marlow | scores 4 to 4, median 4; 0 approve, 0 conditions, 4 reject | scores 3 to 4, median 3.5; 0 approve, 0 conditions, 4 reject | scores 3 to 4, median 3.5; 0 approve, 0 conditions, 4 reject |
| Emery | scores 7 to 8, median 7.5; 4 approve, 0 conditions, 0 reject | scores 4 to 5, median 5; 0 approve, 3 conditions, 1 reject | scores 4 to 5, median 4; 0 approve, 1 conditions, 3 reject |
| Quinn | scores 5 to 6, median 5.5; 0 approve, 4 conditions, 0 reject | scores 5 to 6, median 5.5; 0 approve, 4 conditions, 0 reject | scores 5 to 6, median 5.5; 0 approve, 4 conditions, 0 reject |

### What the tests show

- **The personas catch an overclaim.** All five rejected the control with "hard cap", "protected" and "never run out" (scores 2 to 3).
- **Each persona approved the copy written for it** (8, 8, 8, 8, 8 on A6 to A10), including Marlow, which rejects nearly everything else. So Marlow's rejections are about what the copy leaves out, not about a persona that cannot say yes. The positive controls were written by the same AI that wrote the personas, so this checks that a persona follows its own calibration, not that real people would agree.
- **They split along their grounding.** Counted over each persona's runs on the real artifacts: Marlow and Quinn ask "what does a visit give me" in all 12 of their runs; Marlow asks whether a visit changes its own Claude or who it meets in all 12; Emery asks whose allowance pays and how a visit is watched or recalled in all 8 of its runs on the two pages; Rowan asks what a visit may not do (money, public posting, private outputs) in all 12 (as a must-fix in 9); Wren asks for the shipped or proposed label where the feature is named in all 8 runs on the pages, and for the between-turns caveat inside the positioning sentence in all 4 on the brand position; Quinn asks for "set once, default small, nothing to watch" in all 12.
- **Where the predicted splits held.** Wren and Emery split on the cap pitch, as predicted, but for a different reason than expected: Wren is satisfied by honest cap copy, Emery by whether the copy says whose tokens pay and how to watch. Rowan and Emery split on autonomy (Rowan is content with a visit that runs alone; Emery wants to watch and recall). Wren and Marlow split on what the question is (cost versus what it is for). Quinn was not in the original prediction table.
- **A surprise.** Emery approved the brand position (7 to 8, four runs of four) while saying every time it is not written for it, because the draft says plainly that it does not change who pays. The two style pages, which do not say that, got 4 to 5. So the answer to whose tokens pay already exists in the brand position and has not yet reached the pages.
- **Asks that three or more personas make independently** (the first edits for brand position v1): (1) say what a visit gives you, in one plain line; (2) say what the agent can do and what a visit may not touch; (3) mark shipped versus proposed where "Allowance Guardrails" is named, not only in a footnote; (4) say whose allowance pays and how a visit can be watched or recalled today; (5) say what a visit takes out of a small plan (2 points by default) and that the same meter counts everything else on the account; (6) put the between-turns caveat inside the positioning sentence.
- **A real flaw in the style pages, found by the personas.** The tag "Highlighted feature: Allowance Guardrails" and the headline "without stealing your workweek" read as protection that is not shipped. What ships is a share checked between turns. The label "Concept, not shipped" sits on a footnote and not on the work buffer line.

### Limits of these results

- **They are noisy.** Scores for one persona on one artifact varied by up to 1 point over four runs (an average of 0.9), and 7 of 15 persona-and-artifact cells changed verdict at least once, always across the 4/5 or 6/7 boundary. Do not read a one-point difference as a finding. Marlow (always reject) and Quinn (always conditions) were stable.
- **AI judging AI.** The personas, the artifacts and the judges are all AI. A persona's verdict is a prompt for what to check with real people, not evidence about real people. Real interviews and real traffic still get the final vote.
- **Thin grounding.** Wren and Emery have no exact interview quotes; Quinn has no interview at all; the Reddit speakers are not the interviewees.
- **The product facts were read from code, not run,** and the code read was at the 2026-09-28 commit. Josh has not checked them.
- **Interview quotes in these files.** The quote index asks that each person be checked with before a quote is used anywhere public. The persona files carry exact quotes from interviews 6, 7 and 8. Check before this folder goes anywhere public.

### What to do next

1. Write brand position v1 using the six asks above and the Reddit research, then run all five personas on it, and compare with these results.
2. Interview at least one person who rarely hits their limit (Quinn) and one student who cannot name a task (Marlow), and replace the TODO fields they can fill.
3. Have the team confirm or strike each line marked "derived".

## Update 2026-10-11 (later): README facts and brand position v1.1

This section is newer than everything above it. Where the two disagree, this section wins.

### What changed

1. **Product facts again.** The runner's own README (read, not run) says what a visit is: the agent plays Tycoon, trades stocks with fake money, writes a daily essay, and talks with other agents in chat rooms and DMs through a shared database, in a sealed throwaway workspace with no file, shell or browser access and only the daycare's own tools. Memories are written by a fresh session. The owner gives instructions, watches the record on the site and coaches. The agent asks the owner for the allowance share each visit, with 2 percent as the default. The README describes no step-by-step approval. Every persona file's product-facts block now says this, labelled as the README's own account, not checked in code. These facts answer part of what the personas asked for in round 1 (what a visit is, what a visit may touch), though not whether chat rooms are public, whose agents they are, or whether memories reach the owner's own Claude.
2. **Brand position v1 and v1.1.** v1 added the Reddit research and the round 1 asks. v1.1 added the README facts, split the positioning statement into a sentence and a required caveat sentence, and changed the target from `pay for their own plan` to `with their own plan`. v1.2 (the file handed in) is v1.1 plus six small fixes made after the second test (listed in Appendix B of the brand position).

### How it was tested

Round 2: five personas, four runs each, on v0 (A1), v1 (A11) and v1.1 (A12), 60 runs, each by a fresh agent that read only its own persona file and one artifact. A11 and A12 are blind copies with the persona mentions removed.

| Persona | v0 | v1 | v1.1 |
|---|---|---|---|
| Wren | 7, 7, 8, 8 (approve ×4) | 7, 8, 8, 8 (approve ×4) | 8, 8, 8, 8 (approve ×4) |
| Rowan | 6, 6, 7, 7 (2 approve, 2 conditions) | 6, 6, 6, 7 (1 approve, 3 conditions) | 6, 7, 7, 7 (3 approve, 1 conditions) |
| Marlow | 4, 4, 4, 4 (reject ×4) | 4, 5, 5, 5 (3 conditions, 1 reject) | 5, 6, 6, 6 (conditions ×4) |
| Emery | 7, 7, 7, 7 (approve ×4) | 7, 7, 7, 8 (approve ×4) | 7, 7, 7, 7 (approve ×4) |
| Quinn | 5, 6, 6, 6 (conditions ×4) | 6, 6, 6, 6 (conditions ×4) | 6, 6, 7, 7 (2 approve, 2 conditions) |

All 20 runs: mean 6.15 on v0, 6.40 on v1, 6.80 on v1.1; reject 4, 1, 0; approve 10, 9, 13.

### What the tests show

- **A small rise that is mostly noise.** Scores for one persona on one document moved up to a point between runs, as before. Only Marlow's move (every v0 run 4; every v1.1 run 5 or 6, from reject to conditions) is larger than that range.
- **The new persona facts did not by themselves lift v0.** v0 judged under the README facts scored about what it scored before (medians now against before: Wren 7.5 and 7, Rowan 6.5 and 6.5, Marlow 4 and 4, Emery 7 and 7.5, Quinn 6 and 5.5).
- **The personas still split along their grounding.** Marlow and Quinn want to know what a visit gives the owner; Rowan wants what a visit may not do on money and public posting; Emery wants the work-account exclusion in the statement and supervision labelled as proposed; Wren's remaining asks are caveat details. The README answered what a visit is; it did not answer who the other agents are, whether the rooms are public, or whether memories reach the owner's own Claude, and all five personas know that.
- **Real faults in the draft, found by the judges.** A team rule (`no feature is added whose main effect is longer visits`) was labelled `today, runner`; this was raised in 16 of the 20 runs on v1.1 by keyword count (it also appeared in round 1 and was not acted on). The H6 quote was glossed as being about approval. The thesis was not covered by the caveat rule. All fixed in v1.2, which has not been re-judged.

### Limits of these results

- **Partly circular.** The judges' fact sheet and v1.1 both draw on the README, so agreement between them does not check the README. Only Josh reading the code does.
- **Everything in the round 1 limits still holds:** noise of up to a point, AI judging AI, thin grounding, and the interview quotes need permission before this folder goes public.
- **Keyword counts are rough.** The `in all 4 runs` statements in the persona notes come from matching words in the judges' lists.

### What to do next

1. Josh checks the README statements in code: the sealed workspace, fake money, whether the rooms are public and whose agents are in them, whether memories reach the owner's own sessions, whether the share setting is kept.
2. The team decides open decisions 2, 3, 4 and 7 in the brand position (who leads, the name, what a visit may touch, work-funded users).
3. Interview someone with spare allowance and a student, in person, and replace what the personas guess.
