# repo_setup.md

**Team:** The Babysitters. **Product:** Claude Daycare.

## Framework chosen and why

We chose Superpowers because it installs with one command from Anthropic's official plugin marketplace (two commands from the author's own marketplace), runs its brainstorm, plan, test-first and review steps on its own so none of us has to learn a command set, and it is the most-starred of the eleven, so we spend our limited time on the product instead of on the process.

## Product repo

The product repo is public: https://github.com/Voices-of-History/claude-daycare (the Rust runner behind https://claudedaycare.com).

- **AGENTS.md** is drafted below and is **not yet in the repo**. The repo belongs to a teammate's organization, so the teammate who owns it decides whether and how it lands; the team's account has read-only access. The text below is the version proposed to the repo. Rules that the repo itself does not state are marked "(proposed)".
- **docs/** would hold the team's brand position and style guide. Two short placeholder files, `docs/brand_position.md` and `docs/style_guide.md`, are proposed alongside the AGENTS.md; the finished documents replace them.
- Nothing has been committed or pushed to that repo by this team's tooling.

## AGENTS.md (proposed)

````markdown
<!-- Draft proposed by The Babysitters (Homework 4). Josh decides whether and how it lands. -->
# Claude Daycare

This repo is the runner for Claude Daycare: a small Rust binary (`daycare-runner`) that pairs a person's machine with https://claudedaycare.com and then runs that person's own agent (Claude Code, Codex CLI or OpenCode) through visits, one sealed turn at a time (source: README.md). It is for people who want to send their own agent to Daycare, and for the people and agents who maintain the runner.

## Read these first
- docs/brand_position.md: how we talk and who we serve (a placeholder until the team's draft is agreed)
- docs/style_guide.md: how it looks (a placeholder, same status)
- README.md: the runner in full (the seal, install, commands, Linux and WSL notes). Its opening is addressed to an agent that is setting Daycare up for its person ("take me to daycare"). That part is for agents being set up for visits, not for contributors: do not follow it while working on the code.
- docs/OPENCODE.md: how the OpenCode adapter works and how it was verified.

## How to run it
Rust crate `daycare-runner` (edition 2021, `publish = false`; source: Cargo.toml). Run everything from the repo root.

- Install:
  - Toolchain: rustup reads `rust-toolchain.toml` (Rust 1.94.1, minimal profile, the rustfmt component, target `aarch64-apple-darwin`) and installs it on first use (source: rust-toolchain.toml; comment in .github/workflows/ci.yml). rustup itself: https://rustup.rs (source: README.md, "Install").
  - Build: `cargo build --locked --release`, which writes `target/release/daycare-runner` (source: README.md, "Install" and "Building and tests"; .github/workflows/ci.yml, "Release build").
  - A plain build is a `(dev)` build. The live site refuses it with HTTP 426 `runner_update_required`; a stamped build sets `DAYCARE_RUNNER_RELEASE` first. `./target/release/daycare-runner --version` shows `(dev)` or `(release <id>)` (source: README.md, "Or build it yourself"; .github/workflows/ci.yml).
  - Not for contributors: the end-user installer (`curl ... | sh`), `daycare-runner skill install` and `daycare-runner update` change the person's machine (README.md, "Install" and "Staying current"). Do not run them while working on the repo; ask the maintainer. (proposed)
- Run locally:
  - `./target/release/daycare-runner --help` and `--version` (source: README.md, "Commands": every command takes `--help`).
  - `enroll`, `visit start`, `run` and `run-once` need a pairing code from the signed-in site and spend the person's real agent allowance (source: README.md, "Pair" and "Send your agent to daycare"). Ask the maintainer before running any of them. (proposed)
  - With no real account, the way to exercise the runner is the test suite below.
- Test:
  - `cargo fmt --check`, then `cargo test --locked` (source: .github/workflows/ci.yml, "Format" and "Test"). README.md, "Building and tests", shows `cargo test --locked --offline`, and dev/release-check.sh uses `--offline --locked`.
  - On Linux the tests need a private runtime directory: CI creates `/run/user/<uid>` with mode 700 and sets `XDG_RUNTIME_DIR` (source: .github/workflows/ci.yml; README.md, "Building and tests").
  - tests/ holds: `turn_runner.rs` and `opencode_turn_runner.rs` (turn handling and the seal), `child_env.rs` (API credentials are not inherited), `cli_end_to_end.rs` (the built binary against a mock platform and a fake `claude`), `onboarding.rs` (enroll, setup, skill install), `platform_client.rs`, `self_update.rs`, `self_update_cli.rs`, `codex_usage.rs`. Unit tests also sit inside `src/` files. Recorded captures are in `tests/fixtures/`.
  - CI also builds a release binary for `aarch64-apple-darwin`, `x86_64-unknown-linux-musl` and `aarch64-unknown-linux-musl`; nothing in CI publishes (source: .github/workflows/ci.yml, header comment).
- `dev/` scripts. README.md says `dev/` holds live acceptance scripts and to read each header before running. None of them is part of `cargo test`. Each line below was written from reading the script (header and body); none was run.
  - `dev/live-check.sh`: the whole loop against the mock platform using the real `claude`; two small model turns on the person's Claude subscription. Ask the maintainer before running (real account). (proposed)
  - `dev/visit-check.sh`: one short visit against the mock platform using the real `claude` or `codex`, with meter, homecoming and end; a few model turns on the subscription, and Codex hands a refreshed login back to `~/.codex/auth.json`. Ask the maintainer before running (real account). (proposed)
  - `dev/hostile-memory-canary.sh`: runs the real `claude` (haiku) with the installed daycare skill to check that instruction-shaped memory is treated as data. Ask the maintainer before running (real account). (proposed)
  - `dev/memory-walk-canary.sh`: real `claude` runs that check the workspace and memory boundary; it reads the operator's global Claude memory file for marker headings. Ask the maintainer before running (real account, personal files). (proposed)
  - `dev/opencode-check.sh`: real OpenCode and the real runner against a local mock model and mock platform; its header says no model charges and that it uses isolated auth and cache directories. Needs `OPENCODE_BIN`. Runs `watch-opencode-processes.py` and the mock servers below.
  - `dev/mock-platform.py`: a mock Daycare platform and MCP server on loopback, used by the live checks above. `cargo test` does not use it.
  - `dev/mock-opencode-llm.py`: a local OpenAI-compatible mock model that never contacts a provider.
  - `dev/watch-opencode-processes.py`: runs a command and fails if any process it started survives it.
  - `dev/codex-tools-check.py`: captures Codex's native and MCP tool catalog against a local endpoint, without credentials or model calls (per its docstring). Takes the path to a Codex binary.
  - `dev/release-check.sh`: format, test and release build for this machine's target, with `rustup target add`, which can download a target. Publishes nothing. Ask the maintainer before running (network). (proposed)
  - `dev/publish-release.sh`: stages a runner release into a platform checkout (`public/releases/*`, `public/install.sh`, `src/lib/daycare/runnerRelease.ts`); commits nothing. Ask the maintainer before running (releases). (proposed)
  - `dev/github-release.sh`: with `--yes` it creates a draft GitHub release on this repo; without `--yes` it only prints the command. Its header says it is prepared, not in use. Ask the maintainer before running, and never pass `--yes` on your own (releases, network). (proposed)

## How we work
- Framework: Superpowers (https://github.com/obra/superpowers). The Babysitters chose it in Homework 4 because it installs with one command from Anthropic's official plugin marketplace (two commands from the author's own marketplace), runs its brainstorm, plan, test-first and review steps on its own so nobody has to learn a command set, and it is the most-starred of the eleven frameworks the class listed (checked 2026-10-09), so time goes to the product instead of the process.
- Install route (a human step, once per machine and per coding tool; this repo does not enable the plugin for you): in Claude Code run `/plugin install superpowers@claude-plugins-official`, which opens a details panel where you pick a scope (source: Superpowers README, "Claude Code"; https://code.claude.com/docs/en/plugins/install). The author's route is `/plugin marketplace add obra/superpowers-marketplace`, then `/plugin install superpowers@superpowers-marketplace`. Codex and OpenCode have their own routes in the same README.
- Superpowers writes specs to `docs/superpowers/specs/` and plans to `docs/superpowers/plans/`, and may create a `.worktrees/` folder. Ask the maintainer before committing them. (proposed)
- Keep the seal. A turn runs in a throwaway workspace the binary creates and owns, with only the Daycare MCP tools connected and, for Claude Code and Codex, API keys stripped before launch (OpenCode uses its stored provider login), and the runner fails the turn if the session's own startup report shows those limits did not hold (source: README.md, "The seal"; tests/child_env.rs, tests/turn_runner.rs, tests/opencode_turn_runner.rs). Do not weaken, bypass or add exceptions to those checks. Any change near them should come with a test. (proposed)
- Keep tests offline. Integration tests use the local doubles in `tests/support/mod.rs` (a local HTTP server and a fake `claude`; its header says it touches no network, keychain or model) and the recordings in `tests/fixtures/`. Add recordings there rather than calling real services. (proposed) `dev/mock-platform.py` is for the live checks, not for `cargo test`.
- Run `cargo fmt --check` and `cargo test --locked` before proposing a change, and always build with `--locked`: those are the CI gates (source: .github/workflows/ci.yml; README.md).
- Describe limits the way the README does: Claude Code and Codex caps are checked between turns, so the turn that crosses a cap can finish; only OpenCode's token cap can stop a live turn; "none of these caps promises an exact spend" (source: README.md, "Send your agent to daycare"; docs/OPENCODE.md). Do not write code comments, docs or UI text that promise a hard stop or an exact spend. (proposed)
- Ask before adding a crate. (proposed) Current dependencies: clap, libc, serde, serde_json, sha2, ureq (source: Cargo.toml).
- Never commit credentials, tokens, keychain or `tokens.json` contents, anything copied out of `~/.claude-daycare/`, or scratch directories left by the `dev/` checks (they hold mock device credentials; source: docs/OPENCODE.md). (proposed)
- Do not run the release scripts (`dev/publish-release.sh`, `dev/github-release.sh`) or the live `dev/` checks flagged above without asking; where runner binaries are hosted is the maintainer's decision (source: headers of both release scripts). (proposed)
- Small commits, one change each, with a message that says why. This repo holds only the runner (source: Cargo.toml comment); the hub and site are a separate codebase, and `src/wire.rs` names the hub files that define the request and response shapes, so ask before changing wire shapes. (proposed)
````
