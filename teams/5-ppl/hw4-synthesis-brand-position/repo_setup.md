# UnlockDrill repo setup

**Team:** 5 PPL

**Framework selected for the proposed setup:** [OpenSpec](https://github.com/Fission-AI/OpenSpec), because explicit behavior scenarios help resolve prompt timing, skip, pause, and repeat-trigger behavior before implementation.

## Verified repository setup — October 17

**Product repo:** [Tommylilinfeng/unlockdrill](https://github.com/Tommylilinfeng/unlockdrill). Inspected commit `4597dd391ed123b949c890589c5bb37750d7bcab`.

- [AGENTS.md](https://github.com/Tommylilinfeng/unlockdrill/blob/4597dd391ed123b949c890589c5bb37750d7bcab/AGENTS.md) exists at the root.
- [Brand position](https://github.com/Tommylilinfeng/unlockdrill/blob/4597dd391ed123b949c890589c5bb37750d7bcab/docs/brand_position.md) and [style guide](https://github.com/Tommylilinfeng/unlockdrill/blob/4597dd391ed123b949c890589c5bb37750d7bcab/docs/style_guide.md) exist in `docs/`.
- Maya, Jordan, and Casey are installed in `.claude/agents/`. Companion PR #21 synchronizes the approved quote evidence and includes a review runbook.
- The React/TypeScript/Vite app, question validation script, and GitHub Pages workflow exist.
- OpenSpec was not initialized on the inspected main commit. [Companion PR #21](https://github.com/Tommylilinfeng/unlockdrill/pull/21) initializes version 1.14.3 with the spec-driven schema, project constraints, and Claude commands/skills.
- The inspected main AGENTS.md had a stale run section. Companion PR #21 corrects it; the copy below is the updated branch version.

## Actual commands

```bash
npm ci
npm run dev
npm run build
npm run lint
node scripts/validate-questions.mjs
```

Validation on the companion branch: `npm run build` passed; lint completed with four existing warnings in unchanged application files; all 25 questions passed validation. The validator needed a filesystem-URL conversion fix for paths containing spaces, included in that PR. Real-device Shortcuts testing remains open in [issue #3](https://github.com/Tommylilinfeng/unlockdrill/issues/3). The team's October 17 phone check concerns page/logo appearance and does not close that integration test.

## Feature acceptance scenarios

- An eligible app opening offers one reviewed question for a selected topic.
- Skip and pause remain visible; returning to the chosen app does not trigger a loop.
- A wrong answer receives a brief explanation without requiring correctness to exit.
- Frequency settings and offline/error exits behave consistently.
- Platform integration is verified on the actual target device before compatibility is advertised.

## Copy of AGENTS.md

````markdown
# UnlockDrill

## Product
UnlockDrill is an opt-in SAT practice shortcut. Offer one reviewed question at a student-selected app-opening moment. Prioritize a small start, useful feedback, and user control.

## Read first
Read docs/brand_position.md, docs/style_guide.md, relevant research, and the current feature specification. These describe proposed behavior; distinguish implemented features from plans.

## Evidence
Preserve interview IDs and exact quotations. Do not invent testimonials, score gains, persona facts, supported devices, or customer validation. Keep ErrorJournal and tutoring evidence separate from evidence for app-triggered practice.

## Feature workflow
Use the initialized OpenSpec workflow. Write the proposal, behavior scenarios, design, and task list; resolve platform uncertainty; implement a small change; verify the scenarios; document what changed and what remains uncertain.

## Product rules
Users choose the apps and timing. Keep skip and pause visible. Respect frequency limits. Avoid repeated-trigger loops. Never require a correct answer in the proposed default flow. Provide a safe exit on errors.

## Learning content
Use original or appropriately licensed questions. Check each answer and explanation. Do not imply official SAT endorsement. Do not equate attempts or streaks with score improvement.

## Design
Use the agreed tokens and logo assets. Maintain readable text, keyboard access, visible focus, labeled controls, and reduced-motion support. Do not add guilt-based copy or compulsory celebration.

## Data
Collect only data needed for the agreed feature and explain collection. Keep raw interview notes and participant identities out of public builds. Do not commit secrets.

## Run and verify
The app uses React, TypeScript, and Vite. Install with `npm ci`; start with `npm run dev`; type-check and build with `npm run build`; lint with `npm run lint`; validate question banks with `node scripts/validate-questions.mjs`. Optional services are configured through `.env.example`. Never commit `.env` or raw interview files. Report checks actually run and do not infer device behavior from a successful web build.

## Review and handoff
Test prompt eligibility, skip, pause, repeated opening, answer feedback, and error exit. Summarize behavior changes, checks actually run, and remaining limits in the pull request. Team members own final product and release decisions.
````

## Remaining setup

Review and merge companion PR #21 to land the prepared setup and evidence updates. All three installed-persona reviews completed on October 17 using Claude Code with Sonnet. Actual outputs and feedback decisions are in [the persona notes](personas/README.md), with reproducibility metadata in the companion PR. Real-device automation testing remains separate.
