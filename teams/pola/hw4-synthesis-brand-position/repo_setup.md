# Repo setup

**Framework: [OpenSpec](https://github.com/Fission-AI/OpenSpec).** Our engine already works spec-first (proposals in `docs/roadmap/`, finished designs in `docs/implemented-design/`), and OpenSpec is the lightweight, brownfield-friendly spec framework that formalizes that loop for all three coding agents we already use: Claude Code, Codex, and GitHub Copilot.

## Product repos (both public)

| Repo | What it is | Stack |
|---|---|---|
| [HarryLiGameTech/indoor-topo-navi](https://github.com/HarryLiGameTech/indoor-topo-navi) | **TopoNavi**, the routing engine. Buildings are described in TopoScript (floors, doors, transports, access rules), compiled into navigation graphs, and served as routes through a REST API. | Scala 3, Java, ANTLR, Spring Boot 3.2; JDK 20, Gradle 8.4 wrapper; Apache-2.0 |
| [HarryLiGameTech/toponavi-mcp-server](https://github.com/HarryLiGameTech/toponavi-mcp-server) | The **MCP server** that lets an AI agent answer navigation questions by calling the engine's REST API. | TypeScript, MCP TypeScript SDK, Zod, Jest; Node.js 20+ |

---

## Step 1: Pick a feature development framework

We compared the frameworks from the homework table against how the team already works.

| Framework | Fit for us | Verdict |
|---|---|---|
| **OpenSpec** | Spec-driven, built "for brownfield not just greenfield," adopted incrementally ("You write specs only for what you're about to change"). It generates integrations for Claude Code (`.claude/`), Codex (`.agents/skills/`), and GitHub Copilot (`.github/`), the three agents that already appear in our history. Its flow (`propose` → `apply` → `archive`) is the flow our `docs/roadmap/` → `docs/implemented-design/` folders were improvising. | **Chosen** |
| GitHub Spec Kit | Also spec-driven, with a fuller spec → plan → tasks pipeline. OpenSpec's own comparison calls it "Thorough but heavyweight. Rigid phase gates, lots of Markdown, Python setup." Too much ceremony for a five-person team on a class timeline, and an extra toolchain (Python) on top of the JDK and Node we already need. | Not chosen |
| Superpowers | A strong method for how a single agent session works (brainstorm, plan, test-first, review); some of us already use it in Claude Code. But it shapes the session, not the repo: it doesn't give the team one shared, living spec of what the engine does. It can run inside the OpenSpec loop rather than replace it. | Complements OpenSpec for individual sessions |

**Why the existing workflow points to OpenSpec:**
- **We already write the spec first.** `docs/roadmap/runtime-exclusions-cli.md` says "Status: Planned; not implemented" before any code exists. `docs/roadmap/traversal-preference-spec.md` is "Finalized" and records the implementation status.
- **Our two-folder convention already drifts.** `docs/implemented-design/uncertain-access-spec.md` lives in the "implemented" folder but says "Status: Draft." OpenSpec keeps in-flight changes (`openspec/changes/`) separate from the accepted spec (`openspec/specs/`), and archiving is an explicit step, so status and location can't disagree.
- **Agents already ship our code:**
  - The MCP server was bootstrapped by GitHub Copilot's coding agent (PR #1, `copilot/setup-mcp-server`).
  - Several later PRs in both repos came from `codex/...` branches.
  - The engine repo has a `.claude/` folder.

  A framework tied to one agent would leave two of the three out.

## Step 2: Create the product repo

We kept the two existing repos rather than starting fresh. The engine repo predates this class (created September 2025), and it already implements what our brand position promises:

| Brand position promise | Where it already exists in the engine |
|---|---|
| **Your route, not the map's:** access rights decide the route | TopoScript `root` parameters such as `haveStaffCard`, `haveManagementCard`, and `haveRoomKey` compile a graph specific to each user (`readme.md`, Example maps). Elevator dispatch rules by origin and destination: `docs/implemented-design/management-domain-ride-policy-spec.md` (Status: Implemented). |
| **Step-free and mobility-aware routes** | `MinimizePhysicalDemands` is a native routing objective (`docs/http-api.md`). |
| **Honest, not confident:** say which part is unchecked | Draft spec for routes that are restricted but may be usable ("A door says 'Card Access', but is sometimes open"): `docs/implemented-design/uncertain-access-spec.md`. The MCP elevator tool must tell users the information is "for reference" and that local access policies may apply. |
| **Exact over approximate** | Routes return structured waypoints, route tags, and required actions (MCP server README). |

**Why two repos, not one:**
- **Different toolchains.** The engine is JDK/Gradle and the MCP server is Node, and they release separately.
- **A thin, explicit boundary.** The MCP server only talks to the engine through the versioned REST API (`/api/v1`, contract in `docs/endpoint-design.md`). An agent working in either repo needs one toolchain and one contract, not the whole system.

## Step 3: Write AGENTS.md

One `AGENTS.md` at the root of each repo, from `resources/template_agents-md.md`. Copies are in the appendices below.

- **Codex and GitHub Copilot** read `AGENTS.md` directly.
- **Claude Code** gets a one-line `CLAUDE.md` containing `@AGENTS.md`, so all three agents read the same rules.

## Step 4: Add docs/ with the brand position and style guide

- **What we add:** `docs/brand_position.md` and `docs/style_guide.md` in both repos, the paths the template's "Read these first" section expects.
- **The engine repo:** it already has a `docs/` folder for engine documentation.
- **The MCP server:** it gets `docs/` for the first time. It's where the brand position matters most, because its tool descriptions and results are read by an agent and often repeated word for word to a user.
- **Source of truth:** the hw4 copies in this folder; update both repos together when they change.

## Agent-readiness cleanup

Small fixes so an agent walking into either repo isn't misled:

| Repo | Fix | Why |
|---|---|---|
| engine | Stop tracking `bootrun.log`, `bootrun_local.log`, `.idea/`, and `.claude/settings.local.json` (`git rm --cached`) | They are already in `.gitignore` but were committed before the rule existed; logs and personal IDE settings are noise to an agent. |
| engine | Narrow `.gitignore`'s `.claude` rule to `.claude/settings.local.json` | The blanket rule would also hide OpenSpec's shared Claude Code skills and commands. |
| MCP server | Stop tracking `.DS_Store`; keep `package-lock.json` and delete `pnpm-lock.yaml` | Two lockfiles leave an agent guessing which package manager to use. The README and scripts use npm. |
| MCP server | Update the README's "Project structure" section | It lists only `src/index.ts`; the server now has separate navigation, discovery, elevator, and name-resolution modules, most with their own tests. |
| MCP server | Add a license (team decision; the engine is Apache-2.0) | No license means no one may legally reuse the code. |

## Adopting OpenSpec

1. Install the CLI (Node.js 20.19.0 or higher): `npm install -g @fission-ai/openspec@latest`.
2. Run `openspec init` in each repo and select Claude Code, Codex, and GitHub Copilot. This adds `openspec/` and each tool's integration files.
3. New behavior changes start with `/opsx:propose` (Claude Code, Copilot) or the matching `$openspec-*` skill (Codex), then `/opsx:apply`, then `/opsx:archive` after merge.
4. Existing specs move over incrementally, as OpenSpec recommends for existing codebases. A `docs/roadmap/` proposal becomes an `openspec/changes/` change when work on it starts, and a `docs/implemented-design/` spec becomes part of `openspec/specs/` the next time a change touches it. We don't rewrite them all up front.

## Setup changes

| Change | engine PR | MCP server PR |
|---|---|---|
| `AGENTS.md` + `CLAUDE.md` | pending | pending |
| `docs/brand_position.md`, `docs/style_guide.md` | pending | pending |
| `openspec init` (Claude Code, Codex, Copilot) | pending | pending |
| Agent-readiness cleanup | pending | pending |

---

## Appendix A: AGENTS.md for indoor-topo-navi

````markdown
# TopoNavi

TopoNavi is the indoor routing engine behind AstraPath: it compiles TopoScript building descriptions (floors, doors, transports, access rules) into navigation graphs and serves room-to-room routes through a REST API, for people who need to reach a specific room in a building they don't know.

## Read these first
- docs/brand_position.md: how we talk and who we serve
- docs/style_guide.md: how it looks
- docs/endpoint-design.md and docs/http-api.md: the REST contract. The MCP server (HarryLiGameTech/toponavi-mcp-server) depends on it.
- docs/topo-script-reference/: the TopoScript language reference (published to GitHub Pages)
- openspec/: accepted specs (openspec/specs/) and in-flight changes (openspec/changes/)

## Repo map
| Path | What lives there |
|---|---|
| toponavi-core/ | Graphs, transport models, and route planning (Scala 3) |
| toponavi-dsl/ | TopoScript parser, compiler, and navigation API (Scala, ANTLR) |
| toponavi-web/ | Spring Boot REST service, authentication, and map management (Java) |
| examples/ | Four sample buildings (indigoBJ, nbc4, swfc, trent). They contain legacy syntax and may not compile; use the synthetic projects in the compiler tests for reproducible cases. |
| docs/roadmap/, docs/implemented-design/ | Design specs written before OpenSpec. They move into openspec/ when a change next touches them. |

## How to run it
- Requirements: JDK 20 (tested with 20.0.2). The Gradle 8.4 wrapper is included. Run every command from the repository root.
- Install / build: `./gradlew assemble`
- Run locally: `SPRING_PROFILES_ACTIVE=local ./gradlew :toponavi-web:bootRun`. The `local` profile (application-local.yml) uses an in-memory H2 database and the maps in examples/. The API is under http://localhost:8080/api/v1; the health check is /api/v1/health.
- Run in Docker: `docker network create toponavi-agent-net` once, then `docker compose up --build`.
- Test (fast, known-good subset): `./gradlew :toponavi-dsl:test --tests CompilationValidationTest --tests RootConstraintTest --tests CompilationIsolationTest`
- Test (full): `./gradlew test --continue`. It has known failures, listed in docs/arithmetic-validation-findings.md. Report any new failure; never change a test's expected result to make it pass.
- Benchmarks (opt-in): `./gradlew :toponavi-dsl:transportBenchmark --args='--profile smoke'`
- After editing docs/topo-script-reference/: `node docs/topo-script-reference/tools/build-search-index.mjs`

## How we work
- Framework: OpenSpec. A behavior change starts as a proposal in openspec/changes/ (`/opsx:propose` in Claude Code and Copilot, the matching `$openspec-*` skill in Codex), is built with `/opsx:apply`, and is archived with `/opsx:archive` after merge. Typos, dependency bumps, and test-only fixes don't need a proposal.
- Keep changes focused, follow the surrounding code style, and add a regression test for every behavior change.
- Keep access control and preference separate. Access rules (`requires`, root parameters such as `haveStaffCard`) are compile-time permissions. Preferences (tags, `banTags`, `minimizeTag`) apply at navigation time. Never encode a preference as a permission; see docs/roadmap/traversal-preference-spec.md.
- Don't change the REST contract (`/api/v1`, docs/endpoint-design.md) without a spec change, and say so in the PR: the MCP server depends on it.
- Never claim in code, docs, or API output that a route is step-free or permitted unless the map data says so. Accessibility depends on the supplied map data and policies.
- Never commit secrets: .env, *.pem, GitHub App keys, JWT secrets. Add new settings to .env.example with an empty value.
- Ask before adding a library or a Gradle module.
- Commit messages use Conventional Commits with the module as scope: `feat(dsl): ...`, `fix(core): ...`, `refactor(web): ...`, `docs(...): ...`.
````

## Appendix B: AGENTS.md for toponavi-mcp-server

````markdown
# toponavi-mcp-server

The Model Context Protocol (MCP) server that lets AI agents answer indoor navigation questions for AstraPath users, by calling the TopoNavi engine's REST API.

## Read these first
- docs/brand_position.md: how we talk and who we serve. Tool descriptions and tool results are read by an agent and often repeated to a user, so they follow its tone and language rules.
- docs/style_guide.md: how it looks
- The engine's REST contract: docs/endpoint-design.md and docs/http-api.md in HarryLiGameTech/indoor-topo-navi
- openspec/: accepted specs (openspec/specs/) and in-flight changes (openspec/changes/)

## Repo map
- src/index.ts: server entry point and tool registrations
- src/navigation.ts, src/filtered-query.ts, src/elevator-query.ts: the route, discovery, and elevator tools
- src/place-resolution.ts, src/building-resolution.ts: fuzzy, alias, and Chinese name resolution
- src/building-catalog.ts: the building inventory, read from `GET /api/v1/buildings` at startup
- src/backend-api.ts: the HTTP client for the engine
- Tests sit next to the code they cover (`*.test.ts`). src/backend-api.ts and src/index.ts don't have their own test files yet.

## How to run it
- Requirements: Node.js 20 or higher, and npm (package-lock.json is the lockfile).
- Install: `npm install`
- Configure: `TOPONAVI_API_BASE_URL` (engine URL), `TOPONAVI_API_TOKEN` (platform JWT), `TOPONAVI_API_TIMEOUT_MS` (default 60000, enough for a cold SWFC compile).
- Start the engine first: the server reads the building inventory at startup and exits with a catalog error if the engine is unreachable.
- Run in development: `npm run dev` (stdio transport)
- Build and run: `npm run build`, then `npm start`
- Test: `npm test`

## How we work
- Framework: OpenSpec, the same as the engine. A behavior change starts as a proposal in openspec/changes/ (`/opsx:propose`, or the matching `$openspec-*` skill in Codex), is built with `/opsx:apply`, and is archived with `/opsx:archive` after merge.
- Keep this server a thin adapter. Fuzzy interpretation stays here; routing and canonical predicates run in the engine.
- Every tool has explicit Zod input and output schemas. Add or change a tool together with its test.
- When the engine's contract changes, update src/backend-api.ts and the affected tool tests in the same PR, and link the engine PR.
- Don't guess. Keep returning `needs_interpretation` below 50% confidence, and never invent a building, node, or elevator.
- User-facing wording follows docs/brand_position.md: name the hallway, door, and floor; say which part is unchecked; never promise "you'll never get lost." Elevator answers keep the notice that the information is for reference and local access policies may apply.
- Never commit tokens, and never put secrets in tool output.
- Ask before adding a dependency.
- Commit messages use Conventional Commits: `feat: ...`, `fix: ...`, `refactor: ...`, `chore: ...`.
````
