# Homework 4 — Repo setup

**Framework selected: Feature Forge**, because its brief → plan → build → verify → ship → learn process keeps user evidence and implementation decisions together, with a short route for small changes suitable for our two-person team.

## Product repository

Product: **ClientReady**. A separate local Git repository is prepared in the deliverable bundle as `clientready-product/`. It has not been published, so there is no public product repository URL. The application itself is not built yet; this week establishes the context and workflow for next week's work.

The repository contains:

- Root `AGENTS.md`, based on the course template.
- `docs/brand_position.md` and `docs/style_guide.md` for coding-agent context.
- A project-specific Feature Forge workflow and an 11-framework comparison.
- The provided Reddit researcher in `.claude/agents/reddit-researcher.md` and its local Python ingest script.
- A repository-local Codex research skill in `.agents/skills/reddit-research/SKILL.md`.
- Instructions for testing persona definitions in isolated agent reviews.
- An internal static preview navigator, a local link/asset checker, and a `.gitignore` excluding secrets and the raw Reddit corpus.

Feature Forge is selected as a process and documented in our own project workflow. Its full upstream plugin and installer have **not** been installed. None of the other frameworks was installed for this comparison. Course-provided research files are retained unchanged with a source notice. No global agent settings were changed.

## Run and verification

From the product repository root:

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory .
python3 scripts/check_repo.py
```

The first command serves an internal local navigator at `http://127.0.0.1:8000/`; it is not an application server. Python 3.10+ is sufficient, with no third-party runtime dependency for the scaffold or Reddit normalizer. The checker does not contact live Reddit or any external website.

Setup validation performed on October 9, 2026:

- The supplied Reddit normalizer ran successfully against an isolated, synthetic parser fixture and retained its comment text and source path. The fixture was deleted and never entered the research corpus.
- The reference checker accepted a complete temporary scaffold and detected an intentionally broken local link.
- The asset checker detected a malformed SVG fixture.
- The repository-local research skill's required frontmatter and relative course-agent reference were checked directly. The bundled skill validator could not run because its PyYAML dependency is absent from available Python runtimes.
- A local HTTP serving check was attempted, but the execution environment denied binding a localhost socket. The preview command is provided; live serving was not verified in this environment.
- The integrated product checker passed after final assembly. Checked 11 required files, 264 local references, and 41 assets. PASS: setup files and checked local references/assets are present and valid. Six actual persona response objects across two rounds passed their output-contract checks, and six distinct persona interview quotations matched the supplied Chinese notes. The latest personas additionally use six verified Reddit context excerpts. See `validation_report.json` for the packaged verification record.

The current local corpus contains 32 accepted saves; the research summary documents 20 reviewed comment snapshots and one missing expected thread caused by a duplicate save. Human Reddit collection and any incomplete research items remain separate from repository setup.

## Framework comparison

Reviewed October 9, 2026. This is a lightweight comparison of the 11 assigned frameworks' current primary READMEs, not an installation benchmark. Features and setup can change; the course table's October 2 update dates are not reused as current verification.

| Framework | What its README emphasizes | Fit for this project |
|---|---|---|
| [Feature Forge](https://github.com/kenxle/feature-forge/blob/main/README.md) | A connected feature record, brief, architecture, slices, verification, learning, and a short route for small changes. | **Selected.** The sequence is easy to explain in a two-person team, and the record can carry interview evidence into later implementation. |
| [gstack](https://github.com/garrytan/gstack/blob/main/README.md) | Specialized planning, design, review, browser QA, and release tools; setup includes runtime and browser components. | Valuable once there is an app to inspect; broader tooling than this documentation and static-preview stage needs. |
| [Superpowers](https://github.com/obra/superpowers/blob/main/README.md) | Clarify a design, plan, test-first implementation, subagent development, and review. | Strong alternative for implementation discipline. Feature Forge's connected product record matches the immediate course work more directly. |
| [pstack mirror](https://github.com/backnotprop/pstack/blob/main/README.md) | Modular engineering skills and playbooks emphasizing rigorous, verifiable work. The current mirror identifies Cursor as upstream. | Useful individual practices, but choosing and learning a larger playbook set is not necessary for our first small experiment. |
| [GitHub Spec Kit](https://github.com/github/spec-kit/blob/main/README.md) | Structured specifications, plans, tasks, implementation, and convergence; additional assessment and bug routes. | Good when the scope is settled and feature specs need to scale. More setup than required for the current scaffold. |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec/blob/main/README.md) | Iterative artifact-guided changes, requirements and scenarios, implementation, then archiving. | Close alternative. We favor Feature Forge's explicit research-to-brief and learning connection for now. |
| [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md) | Agile AI development with explicit decisions, durable context, and specialized product, architecture, UX, and testing views. | Capable of small and large work. Our team can start with fewer workflow choices and revisit if coordination grows. |
| [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin/blob/main/README.md) | Brainstorm, plan, work, simplify, review, and save lessons that inform later changes. | Strong runner-up because retained learning matters. We can adopt the lesson-recording habit within Feature Forge. |
| [Agent OS](https://github.com/buildermethods/agent-os/blob/main/README.md) | Extract, deploy, and index codebase standards; shape better specifications. | More valuable after real implementation establishes patterns worth extracting. |
| [SuperClaude](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/master/README.md) | Commands, specialized agents, modes, and optional MCP integrations layered on Claude Code. | The team uses Codex, so a process that travels through ordinary project files is simpler at this stage. |
| [Ruflo](https://github.com/ruvnet/ruflo/blob/main/README.md) | Multi-agent orchestration, memory, MCP, routing, and a console around coding agents. | More orchestration than a two-person, pre-application project presently needs. |

## Choice and limits

Use **Feature Forge** as the feature development process. Keep the upstream framework's useful sequence and evidence discipline, with a compact record for small tasks. No full framework plugin has been installed, no global configuration has been changed, and no claim is made that the other 10 frameworks were tested in execution.

The local adaptation is in `docs/development-workflow.md` in the product repository. When application coding begins, decide whether to install the upstream skills and verify them in the team's actual tool. That installer is separate from selecting and documenting the process for Homework 4.



## Copy of AGENTS.md

```markdown
# ClientReady

ClientReady helps people building small websites turn scattered text and images into content organized by page.

## Read these first
- `docs/brand_position.md`: audience, problem, evidence, and language.
- `docs/style_guide.md`: visual direction, type, colors, and logo rules.
- `docs/development-workflow.md`: our Feature Forge workflow and feature records.
- `docs/agent-setup.md`: how to use the research agent and persona files.

## How to run it
- Install: Git and Python 3.10+; the current setup has no third-party runtime packages.
- Run locally from the repository root: `python3 -m http.server 8000 --bind 127.0.0.1 --directory .`, then open `http://127.0.0.1:8000/`.
- Check local references and assets: `python3 scripts/check_repo.py`.
- Normalize human-saved Reddit files: `python3 scripts/reddit_json_ingest.py --raw reddit_corpus/raw --out reddit_corpus/normalized --corpus reddit_corpus/normalized`.
- This is a research and design setup repository. The local page is an internal navigator. There is no application server, database, account system, deployment, or app test suite yet. Add real run and test commands when those components exist.

## How we work
- Framework: Feature Forge. Write a brief, explore architecture when needed, plan small slices, build, verify, ship within the team's authorization, and record lessons. Use the short route for small, understood changes.
- One feature record in `docs/features/` connects the user problem, evidence, acceptance criteria, decisions, checks, and remaining questions.
- Use a focused branch and small reviewable changes. Preserve unrelated teammate work. Record actual checks and their results; an unrun check is not a pass.
- Preserve the source and meaning of research. Distinguish exact Chinese notes, English translations, AI interpretations, and hypothetical persona reactions. Never invent quotations, interviews, adoption, or payment evidence.
- The current interviews are a small student sample. Do not describe them as proof of agency demand or willingness to pay.
- For the course Reddit task, the human opens and saves all live Reddit pages. Agents only suggest URLs and read local files. Do not use browser automation, network scripts, or search tools to fetch Reddit content.
- Use the documented brand language and visual tokens. Keep prototype screens clearly distinguished from available product behavior. Do not add fake testimonials, customers, metrics, pricing, or working signup claims.
- Keep changes proportional to the task. Explain a new dependency or service before adding it. Do not silently introduce paid services, tracking, or uploads of participant data.
- Review changed screens at narrow and wide widths, with keyboard navigation. Check local links and asset loading. Add behavior tests when actual behavior is introduced.
- Do not commit credentials, `.env` files, identifiable interview records, or the raw Reddit corpus. Preserve third-party notices.
```
