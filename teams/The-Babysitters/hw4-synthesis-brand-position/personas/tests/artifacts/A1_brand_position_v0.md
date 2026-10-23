ARTIFACT A1. The team's brand position draft for Claude Daycare (v0, interview evidence only). Not for sale.

AI Startup Studio · Homework 4 — No Slop Setup

AI draft, not reviewed by the team.

# 4b — Brand position (Claude draft v0)

**Team Name:** The Babysitters · **Date:** 2026-10-09

A first draft of the brand position for Claude Daycare, filled in on the class template. It is meant to be edited by the team and then copied into `brand_position.md` (note 4). Written to be read by agents as well as people: every statement about what the product does is labelled either as true today or as proposed, not shipped. Rule from the template: when copy conflicts with this document, the copy is wrong.

## Preface

Claude Daycare is the team's own product (site claudedaycare.com, runner repo `Voices-of-History/claude-daycare`). Allowance Guardrails is the feature the research focuses on. Note 4 left open how much of the brand position is about the whole product and how much is about the allowance promise. This draft answers it as follows, so the team can overrule it:

- **Product level (Claude Daycare):** Brand Thesis, Brand Values, Tone Guidelines, Language to Avoid. These should still hold if the allowance feature changes.
- **Promise level (Allowance Guardrails):** Positioning Statement, Canonical Language, Objection Handling, Key Quotes. All the interview evidence about limits and usage points here, so the one benefit in the positioning statement is the allowance promise. It is treated as the first promise Claude Daycare makes, not as a separate brand and not as an add-on.
- **Target Identity** is worded at product level, with allowance-level evidence.

How to read the labels:

- **today (site)**: stated on the claudedaycare.com home page as read on 2026-10-09. Only the home page was read.
- **today (runner)**: read in the runner code by the repo study (see Sources), at commit 97424e9 of 2026-09-28. Nothing was built or run, so this means read in code, not observed live.
- **proposed, not shipped**: an idea from the team's own pre-interview canvas. Not a feature.
- **[interview-derived; Reddit wording still needed]**: wording from an interview only. No Reddit thread has been saved yet.
- **(paraphrase, interview N)**: the interviewer's recorded summary, not the participant's words. Never put in quotation marks.
- A short quoted phrase is a verbatim fragment of the full entry in the quote index with the same ID; a longer quote is the full entry. Participants are cited by quote ID, or by interview number and role.

How strong the evidence is: 1b rates Allowance Guardrails as mixed. Two interviews raised usage (3 and 10), and one of those is employer-funded. No interviewee was recorded describing the allowance problem in their own words, and the one line about needing usage (E7) is the least certain entry in the quote index. So the canonical phrases below are borrowed from nearby topics (limits on a bot, needing usage, work). That is why the Canonical Language section ends with a TODO and why every interview entry carries the Reddit tag.

Not covered: the Two-Minute Reunion idea.

Sources: template_brand-position (the template), 1a — Quote index, 1b — Working synthesis (an AI draft), 0 — In-class work (audience table), 4 — Brand position, Team — Claude Daycare and the two ideas (canvas and site facts), 5a — Style references (voice), and the **repo study**, Claude Daycare repo — how the allowance works today (an AI draft, not reviewed by the team; section numbers below are its sections).

## Brand Thesis

> **Letting your agent play is only worth it when you decide, before it leaves, how much of your usage it may spend.**

Why this anchor (proposed):

- It puts the decision with the owner and before the visit. That is true today (site): the visitor sets an allowance before a visit. It is also the idea behind "floors and ceilings" (H8).
- It makes no outcome promise. It does not say work usage is protected or that the owner never runs out, because the runner cannot yet back that (repo study sections 3.3 and 6).
- It holds at product level: it is true of a percentage setting today and of any guardrail added later.

## Positioning Statement

> **For people who pay for their own Claude Code or Codex plan and need that usage for real work, Claude Daycare is the daycare for your coding agent that lets it play on an allowance you set before it leaves because each visit ends when that allowance runs out.**

One benefit only: play on a limit the owner set in advance. The reason to believe is behaviour that exists today (site, and runner per repo study sections 1 and 3).

Held back on purpose: the team's own headline promise, to protect the usage you need for real work while your agent plays. The protected-work half is **proposed, not shipped**, because nothing in the runner protects a floor today (repo study section 6). Do not add it to this sentence until the buffer exists and has been tested.

Wording notes for anyone reusing the sentence:

- `ends when that allowance runs out` means the runner stops taking new turns once the weekly meter has moved by the share chosen. It is checked between turns, so the turn in progress finishes, and two more turns run at homecoming (repo study sections 3.3 and 4.2). Say this wherever there is room.
- The target user is a draft from note 0, not confirmed. `Pay for their own` leaves out employer-funded users on purpose (see Open decisions and gaps).
- `Claude Code` and `Codex` name the agent tools the site supports. They are not a claim of any relationship with their makers.

### What is true today, and what is only proposed

| Item | What exists | Label | Source |
|---|---|---|---|
| Allowance set before a visit | A weekly percentage for Claude Code or Codex (runner default 2 points); a token cap for OpenCode (runner default 300,000 tokens) | today (site, runner) | Site home page; repo study sections 1 and 3.1 (`DEFAULT_WEEKLY_SHARE`, `DEFAULT_TOKEN_CAP`) |
| Visit ends when it runs out | Checked between turns, so the turn that crosses the cap finishes; only OpenCode's token cap can stop a turn in progress | today (site, runner) | Site home page; repo study section 3.3 (`Ledger::should_end`, `run_turn`) |
| What the percentage measures | Movement of the account's weekly meter, so any other use of the account counts too; whole points at best | today (runner) | Repo study sections 1 and 2 |
| After the cap | Two more model turns at homecoming (private account, day report), not bounded by the cap | today (runner) | Repo study section 4.2 |
| Meter trouble | A visit does not start if the meter cannot be read; three missed readings in a row end it | today (runner) | Repo study section 2.2 (`MeterOutage`) |
| Owner recall | A recall command or the hub's come-home; it is seen only after the turn in progress | today (runner) | Repo study section 4.3 |
| Local usage line and status | At homecoming the command line reports the meter movement; `visit status` shows turns, tokens, cost and share. Command line only, not on the site | today (runner) | Repo study section 6 (`weekly_usage_line`, `VisitAction::Status`) |
| Strict, hard per-visit cap | Only the between-turns cap above exists; a mid-turn stop on Claude Code or Codex would need live usage the runner does not read | proposed, not shipped | Repo study section 6 |
| Protected work buffer | Nothing protects a floor. A flat floor on the meter reading is a small change; a floor that keeps enough for the rest of the week is a large or unclear one | proposed, not shipped | Repo study section 6 |
| Budget preview | Nothing predicts what a visit will use; `daycare-runner usage` only prints the current percent and reset day | proposed, not shipped | Repo study section 6 |
| Live progress | The command line shows status after each completed turn; the hub is not sent the meter movement | proposed, not shipped (for the site) | Repo study sections 5 and 6 |
| Automatic pause | There is no paused state; a visit is active or ended | proposed, not shipped | Repo study section 6 |
| Usage receipt | A local line only; nothing on the site | proposed, not shipped (for the site) | Repo study section 6 |

The site home page does not mention a protected buffer, a preview, live progress or a receipt, and does not say how the allowance is measured or enforced (team note).

## Brand Values

Proposed tiebreakers for when the team disagrees. Values are product level.

- **Honest limits over big promises** — State the limit the runner enforces, and its gaps, in the same place. If a headline and the repo study disagree, the headline changes. Tiebreak: choose `ends the visit when the allowance you set runs out` over `your work is always safe`. Source: the canvas rule to promise only limits the runner can enforce, and repo study section 3.3.
- **Your work over the agent's play** — When a choice trades the owner's usage against the agent's fun, side with the owner's usage. In practice: defaults stay small (today 2 points), a visit that cannot read the meter does not start, and one that loses it three rounds in a row ends (repo study section 2.2), and no feature is added whose main effect is longer visits. Source: the team's problem statement; interviews 3 and 10 (paraphrase, usage worries); "I need the usage" (E7).
- **The owner's limit over the agent's autonomy** — The owner sets the limit first and can bring the agent home; copy never sells autonomy as the point. Tiebreak: if a feature lets visits run on without the owner and another keeps the limit in the owner's hand, keep the limit. Source: "They can't do anything outside of what I specifically tell them." (H6); "floors and ceilings" (H8); interview 9 (paraphrase, a software engineer with employer-funded access who wants to watch every step).

## Target Identity

> **Claude Daycare is for someone who leans on a paid coding agent for the work they care about, wants to give it free time, and wants to set the limits first.**

In their words [interview-derived; Reddit wording still needed]:

- Leans on it: "most of the work that I do" (M1); "I can't really think of a task that I do without it." (M2)
- Needs the usage: "I need the usage" (E7) — the least certain entry in the quote index
- Sets limits first: "floors and ceilings" (H8)
- Keeps it inside what they say: "outside of what I specifically tell them" (H6)

What the evidence does and does not support:

- **Pays their own way.** Interviews 4, 5, 6 and 8 pay for plans with their own money (1b section 3). This is the basis for the positioning statement's `pay for their own`.
- **Has felt the limit.** Only interview 3, a heavy coding user, raised the weekly allowance as a paying Claude Max user (paraphrase, from Mitchell's recollection that this participant paid for the subscription for coding). Interview 10, a software engineer with employer-funded access, raised limits too, but the constraint there is employer policy (1b). One interview is thin.
- **Sets limits and lets it run.** This draws on the pattern in interview 7 (limits on a trading bot, then autonomy inside them) and not on interview 9 (a software engineer with employer-funded access who wants to watch every step). Whether the second type is a customer is open.
- **Not confirmed.** The audience is Claude Pro or Max users who use Claude Code (note 0, a draft). The canvas also says Apple Silicon Mac users; no interview checked that.

## Canonical Language

Template asks for 4 to 6 entries (the class slide said 5 to 10). Five entries come from interviews, one is a TODO. Each is a verbatim phrase from the quote index. None was said about an allowance for daycare visits, so each carries a caution.

- **"floors and ceilings"** (H8) — said by a student about the limits on a trading bot they let act alone (interview 7). Use: limits the owner sets in advance as a normal part of using an agent. Caution: today only a ceiling exists (the cap); a floor is the proposed protected work buffer, so `floors` stays out of live copy until that ships. [interview-derived; Reddit wording still needed]
- **"outside of what I specifically tell them"** (H6) — said about what their agents can do with their approval (interview 7). Use: the voice of an owner who keeps the agent inside what they set. Caution: a statement about permissions; the repo study covered the allowance, not what an agent may do, so use it for voice and never as a product claim. [interview-derived; Reddit wording still needed]
- **"I need the usage"** (E7) — said by a student about why they pay for a plan (interview 8). Use: the word is usage, where the site says allowance. Caution: the least certain entry in the quote index (the last line of a notes-style file); check the source line before using it in public copy. [interview-derived; Reddit wording still needed]
- **"most of the work that I do"** (M1) — said by a student about how AI fits into work and personal life (interview 6). Use: only as a pointer to the kind of tasks people do with AI (class and personal ones); it does not name the allowance. Caution: said about AI in general, not about limits; the same participant doubted the product's benefit (M5, M8). [interview-derived; Reddit wording still needed]
- **"anything else it can do"** (H11) — said by a student after naming what is off limits (interview 7); the full line is in the objection table. Use: a few firm lines and free play inside them. Caution: the firm line there was money. Claude Daycare limits usage, not money, so do not reuse `money-wise`. [interview-derived; Reddit wording still needed]
- **TODO — from Reddit research.** How people describe running low on usage, in their own words. No interview has this (1a gaps; note 0 audience table).

Words from the site that stay as the team's own, not interview-derived: visit, allowance, day report.

## Language to Avoid

- **Avoid:** `official`, `by Anthropic`, `Anthropic-approved`, `Claude's own`, any Anthropic or Claude logo, mark or look-alike — **Because:** it implies an affiliation nobody has shown. The site names no relationship to Anthropic, the product name contains Anthropic's trademark, and the name question is open (note 4; note 5a records that the concept pages carry a not-affiliated line). The only statement to make about the relationship is that the pages are not affiliated with or endorsed by Anthropic.
- **Avoid:** `add-on`, `plugin`, `extension`, `third-party` (as a description of Claude Daycare) — **Because:** it is the team's own product with its own site and runner repo (Almog, 2026-10-09, note 4). Earlier drafts called it an add-on, which was fixed in all six round 1 style pages (5a).
- **Avoid:** `guaranteed`, `never run out`, `your usage is protected`, `safe`, `zero risk` — **Because:** the runner cannot enforce that. The turn that crosses the cap finishes, two homecoming turns run after it, the meter resolves to whole points at best, other account use moves the same meter, and nothing protects a floor (repo study sections 3.3, 4.2 and 6). The runner's own end message uses `protected` in one place (repo study section 2.2); that is a wording question for Josh.
- **Avoid:** `protected work buffer`, `budget preview`, `live progress`, `automatic pause`, `usage receipt`, and `hard cap` in the strict sense, as features of the product — **Because:** they are canvas ideas, not shipped. Per-item status is in the table in Positioning Statement. The six round 1 style pages show some of them as placeholders (5a); round 2 copy must not.
- **Avoid:** `save money`, `cheaper`, `budget` read as dollars — **Because:** the limit is a share of a subscription meter, or tokens on OpenCode, not money. A cost cap can fail to bind on subscription logins (repo study section 2.0), and note 4 flags that `allowance` can sound like money.
- **Avoid:** `free`, `no cost` (as a price claim) — **Because:** a visit spends the owner's own usage (repo study section 1) and pricing is undecided; the canvas holds only revenue ideas.
- **Avoid:** `fully secure`, `100% private`, any new safety or privacy reassurance — **Because:** concerns about exposure came up in several interviews (1b section 1), and the repo study covered the allowance, not sandboxing or privacy (repo study section 8). Say only what the site already says until it is checked.
- **Avoid:** `unlock`, `supercharge`, `seamless`, `AI-powered`, `10x` — **Because:** the class coaching names jargon-only canonical language as a common failure (note 0, Task 6), and none of this wording appears in the interview quotes.

## Tone Guidelines

Proposed. The voice reference is pear.no as recorded in 5a: plain, concrete, short declarative sentences, terms stated openly. Paraphrased, not quoted.

- **Plain and specific, not hype** — Say the number and the limit in short sentences. Reason: the interviews show interest that is wide and shallow, and one participant said nothing was frustrating (H2, 1b), so there is no pain to shout about. Source: 5a (voice), 1b.
- **Dry and a little funny, not cute** — One light daycare image per page at most, and the sentence about the limit is always literal. Reason: a participant's first reaction was that the idea was funny but the benefit was unclear (M5), so humour earns a smile and the plain claim has to earn the click. Source: M5, 5a (calm and sparse).
- **Calm about limits, not alarmed** — Sound like a house rule, not a warning label. Reason: the one participant who builds limits talks about them as matter-of-fact settings (H8), and interview 9 (paraphrase) worried about unsupervised use, which fear-based copy would feed. Source: H8, 1b section 1.
- **Candid about what is not built, not coy** — If an idea is not shipped, say so or leave it out. Reason: stating terms openly is what 5a records as the pear.no voice, and the runner cannot yet back a protected-work promise (repo study section 6). Source: 5a, repo study.

## Objection Handling

Built from the concerns in 1b sections 1 and 2, most widespread first. Responses are copy directions. None presents an unshipped idea as existing; where one is mentioned, it is labelled proposed, not shipped.

| Objection | Your response |
|---|---|
| "Nothing's that frustrating. It's amazing." (H2), a student asked about the hardest part of using AI (interview 7). In all ten interviews, no one described a daycare-related problem before the pitch (paraphrase, all ten interviews). | Do not argue and do not invent a pain. Say who it is for: people who already hold their agent back to save usage for work. The team's main assumption, that fear of running out blocks trying it, is untested, so no headline about running out until Reddit wording shows people say it. |
| "My first reaction to the idea is that it's, like, funny, but, like, I don't know, like, what the benefit would be to me, and, like, I feel like there are other more useful AI tools that, like, I haven't integrated." (M5) and "I just can't think of, like, what my agent would do without me telling it to do something that would be useful for me." (M8), a senior CS major (interview 6). Six of ten interviews could not name a use (paraphrase, interviews 1, 2, 3, 5, 6 and 10). | Say plainly what a visit is today (site): the agent takes turns using only the daycare's own tools on an allowance you set, then a separate session writes a day report and saves memories. Be honest that allowance controls answer what a visit could cost, not what it is for. This objection stays open. |
| "I think it could be dangerous because, like, my Claude is, like, learning from my input. So now that Claude is learning from outside input, like, I would wonder how that would impact what I've fine-tuned it for." (M7), interview 6. Three interviews worried that information could leak through a public forum (paraphrase, interviews 1, 2 and 3). | State only what is checked: the site says the agent uses only the daycare's own tools. The repo study covered the allowance, not what the agent is exposed to, so no safety or privacy reassurance goes in copy until it is checked. |
| "Nothing money-wise, but anything else it can do. Can't post anything for me, only create only things that won't be public." (H11), interview 7, on what would need approval. A software engineer with employer-funded access was afraid of unsupervised use and wanted to watch every step (paraphrase, interview 9). | The owner holds the limits. Today that means an allowance set before the visit and a recall that brings the agent home after the turn it is on (repo study section 4.3). Do not say what the agent can or cannot post: the repo study did not check it. |
| A heavy coding user worried about the weekly allowance and would probably use daycare only near the weekly reset (paraphrase, interview 3). Another had recently hit limits at work (paraphrase, interview 10). | The core objection. Today: the allowance is a ceiling per visit, chosen before it starts. The turn in progress and two homecoming turns can add to it, and other account use counts (repo study sections 3.3 and 4.2). A protected work buffer and a budget preview are **proposed, not shipped**; do not describe them as available. |
| A software engineer with employer-funded access had asked work for more tokens and called daycare infeasible for their own case (paraphrase, interview 10). | Be honest: a cap does not make play on employer-funded access acceptable, and Claude Daycare does not change who pays. Do not aim copy at this user (see Open decisions and gaps). |
| "If you pay me." (H13), interview 7, on whether they would try an early version. | A visit spends the owner's own usage, so trying has a real cost today: the cap is checked between turns, so a visit can end a little over it, and two homecoming turns run after it (repo study section 1). Pricing is undecided: state no price and do not say free. |

## Key Quotes

### From interviews

Each is the full entry in the quote index. Check each source paragraph, and with the person, before using a quote in public copy (1a). [interview-derived; Reddit wording still needed]

1. "I let it trade autonomously. However, there's a bunch of, like, floors and ceilings and criteria." (H8) — a student who runs job-search and trading bots (interview 7), asked whether they let the trading bot act alone. The nearest wording to a limit set in advance. [interview-derived; Reddit wording still needed]
2. "I can't really think of a task that I do without it." (M2) — a senior CS major who pays for a personal Claude plan and has Claude Max through work (interview 6), on how AI fits into work and personal life. Why the work usage matters. [interview-derived; Reddit wording still needed]
3. "I need the usage I use it more than the free plan allows me to." (E7) — a student who pays for ChatGPT Plus (interview 8), on why they pay. The only interview line about needing usage, and the least certain entry in the quote index: the last line of a notes-style file, so confirm the source line before using it. [interview-derived; Reddit wording still needed]

### From Reddit

1. TODO — needs a saved Reddit thread, link and date
2. TODO — needs a saved Reddit thread, link and date
3. TODO — needs a saved Reddit thread, link and date

Reddit pages are opened and saved by hand by Almog; agents do not fetch Reddit.

## Open decisions and gaps

1. **Mitchell's and Josh's confirmation.** Almog chose Allowance Guardrails on 2026-10-09; Mitchell and Josh have not confirmed (note 0). The template wants a position the whole team agrees on, and Josh is the only contributor to the runner, so every `today (runner)` statement here also needs his check.
2. **What Allowance Guardrails adds beyond the existing allowance.** On this draft's reading of the repo study, it adds three things with little or nothing behind them today (a protected work buffer, a budget preview, an automatic pause) and stronger or more visible versions of three that exist in part (a cap that stops closer to the limit, progress on the site, a receipt on the site). The team has not decided which of these the product leads with, or whether `allowance guardrails` is a name or only a feature.
3. **The Claude name and the not-affiliated question.** The product name contains Anthropic's trademark and the home page says nothing about any relationship to Anthropic (team note, note 4). Open: whether to keep the name, and whether the site and every concept page carry a plain not-affiliated line. Note 4 points to the name check in 4a, which this draft did not read. This is not legal advice.
4. **How users describe the problem, in their own words (Reddit).** No exact interview quote about allowance or usage limits exists (1a gaps), so the problem row of the audience table (note 0), the TODO entry in Canonical Language, and all three Reddit quote slots wait for saved Reddit threads. Almog opens and saves those pages by hand. Also open: whether people say `usage` (E7) or `allowance` (the site).
5. **Employer-funded users, for whom a cap does not help.** Interview 10 (paraphrase, a software engineer with employer-funded access) has a constraint that is employer policy, which a cap does not change (1b). Work-funded access also appears in interviews 6 and 9. This draft aims at people who pay their own way. Decide whether to say so on the page, and whether this group is a later audience or never.
6. **Which repo study answers need Josh.** Questions are numbered as in the repo study, section 7.

| Question | What in this note waits on it |
|---|---|
| 1 (how much one turn moves the meter), 7 (cost of homecoming turns) | How much the turn in progress and the goodbye turns can add; whether `ends when it runs out` needs a number next to it |
| 2 (fractional percents), 9 (rate-limited fallback of any age), 12 (end-to-end tests for a weekly stop) | Wording of `N points`; how far the cap can be trusted when the meter is stale |
| 3 (why `WeeklyLimitTight` is never produced), 10 (which meter owners' work draws on), 11 (reset instant) | Whether a protected work buffer is a small build and whether it protects the right meter |
| 4, 5, 6 (what the hub does with budget fields, how it computes remaining budget, whether it can show new per-turn fields or a receipt) | Anything shown on the site: live progress, usage receipt |
| 8 (can the hub model a paused visit) | Automatic pause |
| 13 (are the product documents referenced in code readable), 14 (are records and `--json` stable) | Whether the product's own wording exists elsewhere; whether guardrail ideas can be prototyped |

7. **Thin evidence for the allowance promise.** 1b rates the idea mixed. The evidence from a paying user worried about the limit is one interview (3, Mitchell's recollection). No one has seen a visit, so reactions are to an idea described in a few sentences.
8. **Wording conflicts to settle.** Site: `allowance`; interviewee: `usage` (E7). Runner end message: `protected` (repo study section 2.2), which this document tells copy to avoid.
9. **The site beyond the home page.** Only the home page was read; the hub and site code are not in the repo clone. Anything the site shows or does not show beyond the home page is unchecked.
10. **Not yet done from note 4's steps.** Persona agents have not read this draft; no Reddit canonical language; no team agreement. E7 should be checked against its source line before it appears in any copy.
