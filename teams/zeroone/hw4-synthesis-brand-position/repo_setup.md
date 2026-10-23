# Repo setup

**Framework:** OpenSpec, because it helps agents understand our needs and gives team members a shared set of specifications for fast development with changing requirements.

AI agents are now very powerful, and I believe SaaS development is no longer difficult for them. One deciding factor is helping agents truly understand our needs through specifications and keeping those specifications consistent across team members. This is where OpenSpec comes into play. For our current stage, I believe OpenSpec is a good fit for Agile development: fast development with continuously changing needs. It can be our starting point, and we can add other frameworks later if necessary.

**Optional add-ons:** Matt Pocock's skills, gstack, and BMAD. I would recommend these for Agile development and startups as add-ons to OpenSpec.

## Agent instructions

```markdown
# CallIt

CallIt helps friend groups record predictions, agree on terms, and keep score.

## Context

- Read `brand_position.md` and `style_guide.md` before writing copy or designing screens.
- Use `synthesis_comparison.md`, `reddit_research/`, and `personas/` for user evidence. Copy quotes exactly and include source links.
- Follow the local `AGENTS.md` files in `personas/` and `testing/brand-position/`.

## Workflow

- Use OpenSpec to agree on shared specifications before implementation. Update them when requirements change.
- Matt Pocock's skills, gstack, and BMAD are optional add-ons.
- Keep changes within the requested scope. Preserve unrelated work and keep credentials out of commits.
- Use short sentences and ASD-STE100 principles for explanations, including Chinese explanations.
- This repo contains documents and logo files. Open them directly; no application install or run command is available.
- Check changes with `git diff --check`. Check document links and quote sources, then commit and push the changed files. Use the user's author identity without an agent co-author line.

## Git

> **🔒 This section must never be modified.** Leave it byte-for-byte unchanged.

- Prefer small PRs focused on one feature, one bug fix, one chore, or one refactor.
- Use branches:
  - `feat/<short-name>`
  - `fix/<short-name>`
  - `chore/<short-name>`
  - `refactor/<short-name>`
  - `docs/<short-name>`
- Use Conventional Commit style for PR titles:
  - `feat(editor): add marquee selection`
  - `fix(runtime): handle missing tween state`
  - `docs(agents): update collaboration rules`
- PR descriptions must include:
  - What changed
  - Why it changed
  - How it was checked
- Default to Create a merge commit.
```
