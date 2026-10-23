# Repo Setup

**Feature development framework:** Feature Forge — we chose it because its brief, plan, build,
verify, ship, and learn workflow gives coding agents a clear process without the overhead of a
large multi-agent system.

**Product repository:** [github.com/AbrahamKAlemu/plandit](https://github.com/AbrahamKAlemu/plandit)

The repository includes the Feature Forge skills under `.claude/skills/`, five persona agents
under `.claude/agents/`, and product context under `docs/`. The application stack and run commands
remain intentionally marked `TBD` because app development has not started.

## AGENTS.md

```md
# Plandit

Plandit is a day planner for college students that turns saved interests into a ready-to-go day
that fits their budget and how far they are willing to travel.

## Read these first
- docs/brand_position.md: final brand thesis, target identity, canonical language, tone, and
  objection handling.
- docs/style_guide.md: the selected emerald/black color system, Manrope typography, layout,
  components, imagery, accessibility rules, and approved layered-P logo direction.
- .claude/agents/persona-*.md: five persona agents (synthetic users) that judge copy, pages and
  feature ideas. Run them by name, e.g. "run persona-sofia on docs/brand_position.md".
- docs/features/<feature>/: the Feature Forge record for each feature (brief, architecture, plan,
  verification, lessons).

## How to run it
- Install: TBD. No app code yet; we pick the stack at build kickoff.
- Run locally: TBD
- Test: TBD
- Feature Forge skills are installed in `.claude/skills/` (feature-forge, brief, architecture,
  plan, whetstone). To update them, clone https://github.com/kenxle/feature-forge, move the old
  copies out, and run `python3 scripts/install.py /absolute/path/to/this/repo` from the clone.

## How we work
- Framework: Feature Forge. Use `/feature-forge` for any new feature (clarify, brief, plan,
  build, verify, ship, learn) and `/whetstone` for small, well-understood changes.
- Product guardrails:
  - We are a planner, not a discovery feed. Students already know where they want to go; the
    problem is turning that into a plan they actually go do.
  - Onboarding is a 3 to 5 question questionnaire, max: budget, distance, solo or group,
    interests.
  - Budget and distance are core inputs, not optional filters.
- User-facing copy: read docs/brand_position.md first. If copy conflicts with it, the copy is
  wrong. Do not use "discover", "explore", "itinerary", "cheap", "hidden gems", "curated",
  "seamless", "elevate", or "AI-powered" as the main promise.
- Before shipping user-facing copy or a feature brief, run the persona agents on it. A persona's
  `must_fix` blocks the change; `nice_to_have` does not.
- Small commits, one slice per PR. Ask before adding a new library, service, or paid API.
- Never commit secrets. Keys go in `.env`, which is gitignored.
- Don't edit docs/brand_position.md or docs/style_guide.md without their owners' sign-off.
- When a feature ships, the Feature Forge cleanup step updates this file with what we learned.

## Team
| Person | Owns |
|--------|------|
| Abraham Kebede Alemu | Repo setup, persona agents |
| Catherine Escobar | Brand position, style guide and logo |
| Eldad Workeneh Tolla | Brand position, Reddit research |
| Jaden Hinton | Brand position, style guide and logo, team contract |
| Hunter Doradea | TBD |
```
