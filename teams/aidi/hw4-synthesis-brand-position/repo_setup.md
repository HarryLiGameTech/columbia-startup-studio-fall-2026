# Repository Setup

## Feature development framework

We chose **Feature Forge** because its brief → plan → build → verify → ship → learn lifecycle gives our three-person team a clear, lightweight process for building and validating Aplovia's MVP without adding the complexity of a larger multi-agent framework.

## Product repository

The product repository is a private repository named `aplovia`, hosted at [github.com/EdisonHon/aplovia](https://github.com/EdisonHon/aplovia).

## Confirmed technology decisions

- Primary language and server framework: Python with Django
- Page rendering and interaction: Django Templates with HTMX
- Interface: semantic HTML, the project's custom CSS design tokens, and limited vanilla JavaScript
- Database: PostgreSQL
- Testing: pytest, pytest-django, and Playwright
- Phase 1 exclusions: no React or Tailwind CSS unless a later feature demonstrates a clear need
- File storage: local `media/` storage during development, with private S3-compatible object storage for deployed user documents; uploaded files are never committed to Git
- Reminders: in-app reminder time and deadline status in Phase 1; email delivery and Celery/Redis background jobs are deferred until they are justified by user testing
- Deployment target: Render, using its Django web-service workflow and managed PostgreSQL; the team accepts free-tier cold starts in exchange for minimizing cost
- Deployment configuration: keep a reproducible `render.yaml` in the repository and connect Render to the private GitHub repository
- Runtime and dependency tools: Python 3.12, Django 5.2 LTS, pip with `requirements.txt`, psycopg 3, Gunicorn, and WhiteNoise

## AGENTS.md

The following file will live at the top of the `aplovia` product repository:

````markdown
# Aplovia

Aplovia is a bilingual web application that helps international high school students applying as first-year students to U.S. colleges identify and understand reach, match, and safety schools and manage their application process themselves.

## Read these first

- `docs/brand_position.md`: who we serve, what problem we solve, and the language we use
- `docs/style_guide.md`: visual system, interface rules, accessibility floors, and logo usage

## How to run it

### Requirements

- Python 3.12
- PostgreSQL
- A local `.env` created from `.env.example`; never commit secrets

### Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
python manage.py migrate
```

On macOS or Linux, activate the environment with `source .venv/bin/activate` instead.

### Run locally

```powershell
python manage.py runserver
```

### Test

```powershell
python manage.py check
pytest
```

## Technology

- Python 3.12 and Django 5.2 LTS
- Django Templates, HTMX, semantic HTML, custom CSS, and limited vanilla JavaScript
- PostgreSQL through psycopg 3
- pytest, pytest-django, and Playwright
- Gunicorn and WhiteNoise on Render
- Local `media/` storage in development and private S3-compatible object storage for deployed user documents

Do not add React, Tailwind CSS, Celery, Redis, or another major framework or service without team approval and a demonstrated Phase 1 need.

## How we work

- **Framework:** Feature Forge — brief → plan → build → verify → ship → learn.
- Start each non-trivial feature with a short brief defining the user, problem, scope, acceptance criteria, and explicit non-goals.
- Obtain team agreement on the plan before implementation. Keep changes small enough to review and verify.
- Add or update tests with behavior changes. Before calling work complete, run relevant tests and manually check the affected English and Chinese interfaces at desktop and iPad widths.
- Record what shipped, verification evidence, and important lessons so the next feature can reuse them.
- Ask before adding a dependency, changing the data model beyond the approved feature, introducing an external service, or expanding Phase 1 scope.

## Product and data rules

- The Phase 1 audience is international high school students applying as first-year students to U.S. undergraduate programs.
- Present reach, match, and safety as explained estimates, never guarantees of admission.
- Keep source URLs and last-checked dates with school information. Do not present unverified AI output as fact.
- AI assistance is optional and closed by default. Never read or send a student's document or personal information to an AI service unless the student explicitly selects it for that action.
- Preserve student control: recommend and explain, but do not make application decisions for the student.
- Update English and Chinese interface copy together. Do not automatically translate or rewrite a student's application materials.
- Store secrets only in environment variables. Keep `.env`, uploaded documents, and local `media/` files out of Git.
- Use Django migrations for schema changes; never modify a shared or production database manually.

## Interface rules

- Follow `docs/style_guide.md`; use the Midnight Navy design tokens and supplied Aplovia logo assets.
- Prioritize the student's next deadline-driven action. Keep the interface professional, trustworthy, clear, and calm.
- Maintain keyboard access, visible focus states, sufficient contrast, explicit text labels, and minimum 44px pointer targets.
- The left navigation and optional right AI drawer open independently. The AI drawer never opens automatically.
- Avoid decorative imagery, gradients, generic AI symbols, and ranking-first school presentations.
````
