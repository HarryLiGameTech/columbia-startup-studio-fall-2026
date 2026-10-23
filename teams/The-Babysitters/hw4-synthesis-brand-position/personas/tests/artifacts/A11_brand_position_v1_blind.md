ARTIFACT A11. The team's brand position draft for Claude Daycare (v1). Not for sale.

# Brand Position: Claude Daycare (v1)

**Team Name:** The Babysitters · **Date:** 2026-10-11

AI draft, not reviewed by the team. Mitchell and Josh have not seen it, and Josh has not checked the statements about the runner.

**Purpose:** This is an internal document. It captures the brand's thesis, identity and canonical language so that everything the team builds speaks with one voice: landing page, copy, features, pitch. It is meant to be read by agents as well as people. Rule from the template: when copy conflicts with this document, the copy is wrong.

Claude Daycare is the team's own product (site claudedaycare.com, runner repo `Voices-of-History/claude-daycare`). Allowance Guardrails is the feature the research focuses on.

**How to read the labels.** Every statement about what the product does is labelled one of these:

- **today (site):** stated on the claudedaycare.com home page as read on 2026-10-09. Only the home page was read.
- **today (runner):** read in the runner's code at commit 97424e9 of 2026-09-28. Nothing was built or run, so this means read in code, not seen working.
- **proposed, not shipped:** an idea from the team's own canvas. Not a feature. Copy must not describe it as available.
- A quotation mark means exact words from an interview (ID in brackets) or a saved Reddit comment (with its link).

**What this version changes from v0.** v0 was written from the ten interviews alone. v1 adds the Reddit research (39 threads, 6,970 comments, January to October 2026) and a first round of testing. Nothing the evidence did not support was added, and anything that needs Josh is an open decision at the end, not a claim.

---

## Brand Thesis

> **Your agent can have a day of its own, as long as you set the limit before it leaves.**

Why this anchor (proposed):

- It names what the owner gets (a day of its own for the agent, with a day report when it comes home, today (site)) and who decides the limit (the owner, before the visit, today (site and runner)). v0's thesis named only the limit.
- It makes no outcome promise. It does not say work usage is protected or that the owner never runs out, because the runner cannot back that yet (see the table in the appendix).
- It holds at product level: it is true of a percentage setting today and of any guardrail added later.

---

## Positioning Statement

> **For people who pay for their own Claude Code or Codex plan, Claude Daycare is the daycare for your coding agent that sends it on a visit with a share of your weekly usage you choose before it leaves, and gives you a day report when it comes home, because each visit ends once that share is spent: the share is checked between turns, so a visit can end a little over it.**

Short form, for headlines only:

> **Send your agent on a visit with a share of your weekly usage you choose before it leaves.**

**Rule for the short form.** Wherever it appears, the next sentence must say the rest: *The share is checked between turns, so a visit can end a little over it, and two more turns run after it ends.* It is a rule of this document that the caveat travels with the sentence.

What changed from v0: the target no longer says "need that usage for real work"; the benefit now includes the day report; the between-turns caveat is inside the sentence.

One benefit on the limit side only: play on a limit the owner set in advance. The reason to believe is behaviour that exists today (site, and runner). Held back on purpose: the team's own headline promise, to protect the usage you need for real work while your agent plays. The protected-work half is **proposed, not shipped**, because nothing in the runner protects a floor today. Do not add it to this sentence until the buffer exists and has been tested.

Wording notes for anyone reusing the sentence:

- `ends once that share is spent` means the runner stops taking new turns once the weekly meter has moved by the share chosen. The turn in progress finishes on Claude Code and Codex, and two more turns run at homecoming (today, runner). On OpenCode the allowance is a token cap that is counted live and can stop a turn in progress, but it is not exact (today, runner).
- `a share of your weekly usage` is measured as how far the account's weekly meter moves, so anything else done on the account in that time counts too, and the meter reads whole percentage points at best (today, runner). The runner's default share is 2 points; a visit with no setting gets it.
- `for people who pay for their own plan` leaves out employer-funded users on purpose (see open decision 7).
- `Claude Code` and `Codex` name the agent tools the site supports. They are not a claim of any relationship with their makers.

---

## Brand Values

Tiebreakers for when the team disagrees. Values are product level.

- **Honest limits over big promises** — State the limit the runner enforces, and its gaps, in the same place. If a headline and the code disagree, the headline changes. Tiebreak: choose `ends once the share you set is spent` over `your work is always safe`. Evidence: people ask for a plain gauge and for the plan to be written plainly. "show a multiplier gauge in usage" ([r/ClaudeCode, Mar 2026](https://www.reddit.com/r/ClaudeCode/comments/1s4idyz/update_on_session_limits/ocnc8tg/)); "written plainly in the docs" ([r/ClaudeCode, Aug 2026](https://www.reddit.com/r/ClaudeCode/comments/1w38v98/claude_max_20x_only_applies_to_the_5hour_window/p6yex19/)).
- **Your work over the agent's play** — When a choice trades the owner's usage against the agent's fun, side with the owner's usage. In practice: the default share stays small (2 points), a visit that cannot read the meter does not start, one that loses it three rounds in a row ends, and no feature is added whose main effect is longer visits (today, runner). Evidence: owners already leave headroom by hand: "leave headroom for the rest of the day" ([r/ClaudeCode, Jul 2026](https://www.reddit.com/r/ClaudeCode/comments/1uv6ns4/dear_anthropic_this_has_to_stop/ox9bacd/)).
- **The owner's limit over the agent's autonomy** — The owner sets the limit first and can bring the agent home; copy never sells autonomy as the point. Tiebreak: if a feature lets visits run on without the owner and another keeps the limit in the owner's hand, keep the limit. Evidence: "They can't do anything outside of what I specifically tell them." (H6) and "I let it trade autonomously. However, there's a bunch of, like, floors and ceilings and criteria." (H8).

---

## Target Identity

> **Claude Daycare is for someone who pays for their own coding agent, wants to give it a day of its own, and wants to set the limit first.**

In their words:

- Paces the week by hand: "a day's worth of my weekly allowance per day" ([r/ClaudeAI, Sep 2026](https://www.reddit.com/r/ClaudeAI/comments/1why2zx/a_lot_of_talk_about_reduced_weekly_limits_but_a/pa8dpqd/))
- Leaves headroom: "leave headroom for the rest of the day" ([r/ClaudeCode, Jul 2026](https://www.reddit.com/r/ClaudeCode/comments/1uv6ns4/dear_anthropic_this_has_to_stop/ox9bacd/))
- Sets limits first: "I let it trade autonomously. However, there's a bunch of, like, floors and ceilings and criteria." (H8)
- Keeps it inside what they say: "They can't do anything outside of what I specifically tell them." (H6)

What the evidence does and does not support:

- **Pays their own way.** Interviews 4, 5, 6 and 8 pay for plans with their own money, and the Reddit voices who pace their week are on their own plans.
- **Protects the allowance by hand.** Found in 32 of 39 Reddit threads (research summary, theme 2), almost always as a personal workaround: pacing, shorter chats, a script, a custom meter. That is evidence of a need, and also of a competitor: many people solve it themselves.
- **A second audience the position does not yet speak to: people with allowance to spare.** Reddit shows them clearly ("I upgraded to the 20x plan because the 5x wasn't enough, but most weeks I end up only using like 50-70% of my usage before it resets." ([r/ClaudeAI, Aug 2026](https://www.reddit.com/r/ClaudeAI/comments/1vfoq73/max_20x_user_here_only_burning_through_5070_of_my/))). Their replies when someone asks what to do with the extra are mostly useful backlog jobs, not play. This position does not make them the target, because its reason to believe (a share you set) speaks to people who think about the limit. Decision 2 below.
- **Not confirmed.** The audience is Claude Pro or Max users who use Claude Code (a draft). The canvas also says Apple Silicon Mac users; no interview checked that.

---

## Canonical Language

Words people use, with the link. Plain words first: from a count over all 7,009 texts in the saved threads, people say "limit" in over 1,000 and "usage" in over 800, and "allowance" in 25 (14 threads).

- **weekly allowance** — as in "a day's worth of my weekly allowance per day" ([r/ClaudeAI, Sep 2026](https://www.reddit.com/r/ClaudeAI/comments/1why2zx/a_lot_of_talk_about_reduced_weekly_limits_but_a/pa8dpqd/)). Use: the site's word is understood and people do say it; it is less common than "limit" or "usage", so pair it with one of them the first time it appears.
- **pace myself** — "I have to pace myself to reach 90%+ usage by reset time" ([r/ClaudeCode, Aug 2026](https://www.reddit.com/r/ClaudeCode/comments/1w38v98/claude_max_20x_only_applies_to_the_5hour_window/p6ydoq2/)). Use: how owners already treat the week; it fits a share you set before the visit.
- **headroom** — "leave headroom for the rest of the day" ([r/ClaudeCode, Jul 2026](https://www.reddit.com/r/ClaudeCode/comments/1uv6ns4/dear_anthropic_this_has_to_stop/ox9bacd/)). Use: the word for what the owner keeps for work. Caution: a protected buffer is proposed, not shipped, so say `headroom` only about the owner's own habit or the default share, never as a product promise.
- **budget cap** — "Loops until failure, budget cap, or Ctrl-C" ([r/ClaudeCode, Apr 2026](https://www.reddit.com/r/ClaudeCode/comments/1svxcb7/pattern_im_using_to_keep_claude_code_productive/)). Use: the plain name for a limit set in advance. Caution: the author is promoting their own repo; use the words, not the source.
- **handoff doc** — "have it write a handoff doc" ([r/ClaudeCode, Sep 2026](https://www.reddit.com/r/ClaudeCode/comments/1wjhkef/rate_limits_are_so_bad_right_now_open_source/paiqfye/)). Use: what people already ask an agent to write before a limit; close in spirit to the day report. Caution: the day report is written after the visit ends, not before.
- **floors and ceilings** — "I let it trade autonomously. However, there's a bunch of, like, floors and ceilings and criteria." (H8, interview 7). Use: limits set in advance as a normal part of using an agent. Caution: today only a ceiling exists; a floor is the proposed work buffer, so `floors` stays out of live copy until that ships.

Words from the site that stay as the team's own: visit, allowance, day report, homecoming.

---

## Language to Avoid

- **Avoid:** `official`, `by Anthropic`, `Anthropic-approved`, `Claude's own`, any Anthropic or Claude logo, mark or look-alike — **Because:** it implies an affiliation nobody has shown. The site names no relationship to Anthropic, the product name contains Anthropic's trademark, and the name question is open. The only statement to make about the relationship is that the pages are not affiliated with or endorsed by Anthropic.
- **Avoid:** `add-on`, `plugin`, `extension`, `third-party` (as a description of Claude Daycare) — **Because:** it is the team's own product with its own site and runner repo.
- **Avoid:** `guaranteed`, `never run out`, `your usage is protected`, `safe`, `zero risk`, `stops instantly`, `hard cap` in the strict sense — **Because:** the runner cannot enforce that. On Claude Code and Codex the turn that crosses the cap finishes, two homecoming turns run after it, the meter resolves to whole points at best, other account use moves the same meter, and nothing protects a floor (today, runner). The runner's own end message uses `protected` in one place; that is a wording question for Josh.
- **Avoid:** `protected work buffer`, `budget preview`, `live progress`, `automatic pause`, `usage receipt` as features of the product — **Because:** they are canvas ideas, not shipped (table in the appendix). The command line does print a usage line and a progress line today, but nothing like that is on the site.
- **Avoid:** `20x`, `10x`, any multiple, and `unlimited` — **Because:** people call a multiplier label a lie when it does not scale the way it reads: "The 20x plan with or without boosted limits is a blatant lie" ([r/ClaudeCode, Aug 2026](https://www.reddit.com/r/ClaudeCode/comments/1w3lw7f/just_cancelled_my_claude_code_bullshit_20x_plan/)).
- **Avoid:** `guardrails` as the name of what ships, and `graceful`, `checkpoint`, `pause` for how a visit ends — **Because:** people use `guardrails` for safety rules on an agent (for example "agentic needs boring OS-level guardrails: max process count, browser launch caps, and a kill switch" ([r/ClaudeCode, Oct 2026](https://www.reddit.com/r/ClaudeCode/comments/1x1esxn/attention_heavy_ai_users/petyigy/))), not for a usage limit, so a reader may expect safety rules; and the runner does not checkpoint or pause, it finishes the turn in progress and then ends the visit. See open decision 3.
- **Avoid:** `set once`, `always on`, `automatic` (about the allowance) — **Because:** a default share exists, but nobody has checked whether the setting persists between visits. Ask Josh before copy says it.
- **Avoid:** `save money`, `cheaper`, `budget` read as dollars — **Because:** the limit is a share of a subscription meter, or tokens on OpenCode, not money. A cost cap can fail to bind on subscription logins (today, runner).
- **Avoid:** `free`, `no cost` as a price claim — **Because:** a visit spends the owner's own usage, and pricing is undecided.
- **Avoid:** `fully secure`, `100% private`, `can't post anything`, any new safety or privacy reassurance — **Because:** what the agent can do and what could leave a visit has not been checked (open decision 4).
- **Avoid:** `unlock`, `supercharge`, `seamless`, `AI-powered`, `10x`, `token maxing` — **Because:** jargon and hype are what people mock; `token maxing` is an insult in these threads. "I'm convinced a lot of this is due to token maxing. I use the max 20x plan and pretty much never hit limits. They keep changing things, I never hit limits." ([r/ClaudeCode, Jul 2026](https://www.reddit.com/r/ClaudeCode/comments/1uv6ns4/dear_anthropic_this_has_to_stop/oxacdqr/))

---

## Tone Guidelines

- **Plain and specific, not hype** — Say the number and the limit in short sentences, and give the number before the metaphor. Reason: a reply with 922 points under the announcement of a limit change asked for a gauge, not a promise. "Please be transparent about it: show a multiplier gauge in usage. That would be the right thing to do." ([r/ClaudeCode, Mar 2026](https://www.reddit.com/r/ClaudeCode/comments/1s4idyz/update_on_session_limits/ocnc8tg/))
- **Dry and a little funny, not cute** — One light daycare image per page at most, and the sentence about the limit is always literal.
- **Calm about limits, not alarmed** — Sound like a house rule, not a warning label, and do not assume the reader is always about to run out. Reason: a large group says they never hit the limit, and for them fear-led copy fixes a problem they do not have. "I never get close to my limit. Ever. I just chatted for 2 hours and I'm at 9% usage." ([r/ClaudeAI, Apr 2026](https://www.reddit.com/r/ClaudeAI/comments/1sepqzw/you_accidentally_say_hello_to_claude_and_it/oeterfb/))
- **Candid about what is not built, not coy** — If an idea is not shipped, say so next to the name, not in a footnote.

---

## Objection Handling

What skeptics said, in the interviews and on Reddit, and how copy should answer. Responses are copy directions. None presents an unshipped idea as existing; where one is mentioned, it is labelled proposed, not shipped.

| Objection | Your response |
|---|---|
| **I never hit the limit.** "I never get close to my limit. Ever. I just chatted for 2 hours and I'm at 9% usage." ([r/ClaudeAI, Apr 2026](https://www.reddit.com/r/ClaudeAI/comments/1sepqzw/you_accidentally_say_hello_to_claude_and_it/oeterfb/)) (a search matched 86 texts across 20 threads; reading a sample, about 6 in 10 were people who really do not hit the limit, so roughly 50; the largest group of pushback) | Do not argue. For this reader the pitch is not protection; it is what a visit gives (a day report and saved memories, today (site)) at a small default share (2 points). Say who it is for: people who pay for their own plan and want to give their agent a day of its own. Do not write copy as if the reader is always short. The honest edge for them is the heavy week: say the share is checked between turns and a visit can end a little over. |
| **It's a flat rate and I don't track it.** "no, it's a flat rate subscription. i pay it and use it for what i want out of it, and then i don't worry about it." ([r/ClaudeCode, Jun 2026](https://www.reddit.com/r/ClaudeCode/comments/1u9e0rz/does_anyone_else_feel_robbed_when_they_dont_max/osmh8rx/)) | Do not ask them to track anything. Say what a visit takes (a share of the weekly meter, 2 points by default) and that a usage line is printed in the command line when it ends (today (runner); not on the site). Whether a setting persists between visits is open (decision 5), so do not say `set once`. |
| **Downgrade instead.** "Just so you're aware the 5x plan is 50% of the 20x so you may want to simply downgrade." ([r/ClaudeAI, Aug 2026](https://www.reddit.com/r/ClaudeAI/comments/1vfoq73/max_20x_user_here_only_burning_through_5070_of_my/p1qulk5/)) (advice to someone using half of a Max 20x plan) | Be honest: if you never use your plan, a cheaper plan may be the right answer, and Claude Daycare does not push anyone to upgrade. It is for people who keep their plan and want to put some of it to a visit. |
| **I wouldn't trust it with the last of my usage.** "I typically end the week with like 10% usage, give or take on either end. Could I possibly squeeze some more usage? Sure. Do I trust that it wouldn't run out? No." ([r/ClaudeAI, Sep 2026](https://www.reddit.com/r/ClaudeAI/comments/1wkqszd/asked_claude_to_waste_my_remaining_usage_before/pat0jzf/)) (this comment was voted down to -19, so a minority view in that thread) | That is why the default share is small and the edges are stated: checked between turns, whole points at best, other account use counts. The protected work buffer and the budget preview are **proposed, not shipped**; do not promise a floor. |
| **What's the benefit to me?** "My first reaction to the idea is that it's, like, funny, but, like, I don't know, like, what the benefit would be to me, and, like, I feel like there are other more useful AI tools that, like, I haven't integrated." (M5), a student, interview 6. Six of ten interviews could not name a use; "I just can't think of, like, what my agent would do without me telling it to do something that would be useful for me." (M8). | Say plainly what a visit is today (site): the agent takes turns using only the daycare's own tools on an allowance you set, then writes a day report and saves memories. The evidence that people want this is thin: "fun" uses of leftover allowance came up in only 3 of 39 Reddit threads, and people with spare allowance mostly list useful jobs. This objection stays open (decision 2). |
| **Could it change my own Claude, or who does it meet?** "I think it could be dangerous because, like, my Claude is, like, learning from my input. So now that Claude is learning from outside input, like, I would wonder how that would impact what I've fine-tuned it for." (M7), interview 6 | Not checked. Nothing in the runner study says whether anything from a visit can reach the owner's own Claude sessions. Until Josh answers (decision 4), say only what the site says: the agent uses only the daycare's own tools. No safety reassurance. |
| **What can it do? Can it spend money or post publicly?** "Nothing money-wise, but anything else it can do. Can't post anything for me, only create only things that won't be public." (H11), interview 7 | Not checked. The owner holds the limits: today that means an allowance set before the visit and a recall that brings the agent home after the turn it is on. Do not say what the agent can or cannot post until Josh has checked. |
| **Is this my work account?** "Actually it's our company account so never used for other stuff than claude code. Company work" ([r/ClaudeCode, Mar 2026](https://www.reddit.com/r/ClaudeCode/comments/1s392ep/in_13_minutes_100_usage_happened_yesterday_too/oceczhi/)) (a Reddit voice on a company account), and an engineer with employer-funded access called daycare infeasible for their case (paraphrase, interview 10) | A cap does not change who pays. Say plainly: a visit spends the owner's own allowance on the owner's own plan, and it is not meant for company or work-funded accounts (decision 7). Say what the owner can do today: recall a visit at any time, read a usage line in the command line and a day report. Live viewing and step-by-step approval are **proposed, not shipped**. |
| **Unattended work only creates review work.** "I'm not sure it would be 2x more productive. In the morning you will have A LOT of code to either review or trust blindly that it fits your expectations." ([r/ClaudeCode, Aug 2026](https://www.reddit.com/r/ClaudeCode/comments/1vw5muy/how_do_you_get_claude_to_code_overnight/p5e9186/)) | A visit is not coding work to review: what comes back is a day report and saved memories (today (site)). Check with Josh that nothing else comes back before copy says so. |
| **Is it even allowed?** "just curious how u use claude outside of claude env, is it legal according to their tos?" ([r/ClaudeCode, Aug 2026](https://www.reddit.com/r/ClaudeCode/comments/1vsyn8t/what_i_learned_running_25_claude_code_and_codex/p4x8oce/)) (words like terms of service, ban or violate appear in 15 texts across 10 threads, not each one checked) | Open and not for copy to answer. Whether running a coding agent on a subscription through a tool like Daycare is within the provider's terms is not answered by anything read. Do not claim it is. Check before launch. This is not legal advice. |
| **If you pay me.** "If you pay me." (H13), interview 7, on whether they would try an early version | A visit spends the owner's own usage, so trying has a real cost today: a share of the weekly meter, checked between turns, with two homecoming turns after it. Pricing is undecided: state no price and do not say free. |

---

## Key Quotes

### From interviews

Each is the full entry in the team's quote index. Check each source paragraph, and with the person, before using a quote in public copy.

1. "I let it trade autonomously. However, there's a bunch of, like, floors and ceilings and criteria." (H8) — a student who runs job-search and trading bots (interview 7), asked whether they let the trading bot act alone. The nearest wording to a limit set in advance.
2. "They can't do anything outside of what I specifically tell them." (H6) — the same student, on what their agents can do with approval. The voice of an owner who keeps the agent inside what they set.
3. "My first reaction to the idea is that it's, like, funny, but, like, I don't know, like, what the benefit would be to me, and, like, I feel like there are other more useful AI tools that, like, I haven't integrated." (M5) — a student (interview 6), first reaction to the idea. The objection the copy must answer.

### From Reddit

1. "Please be transparent about it: show a multiplier gauge in usage. That would be the right thing to do." ([r/ClaudeCode, Mar 2026](https://www.reddit.com/r/ClaudeCode/comments/1s4idyz/update_on_session_limits/ocnc8tg/)) — a reply to the announcement of a limit change (March 2026, 922 points). The tone to match: a plain gauge, not a promise.
2. "What helped wasn't Anthropic changing anything, it was me treating compute like payroll instead of tap water. Before any big run I make it estimate the size first, split the work into waves, and leave headroom for the rest of the day. Haven't burned a day since." ([r/ClaudeCode, Jul 2026](https://www.reddit.com/r/ClaudeCode/comments/1uv6ns4/dear_anthropic_this_has_to_stop/ox9bacd/)) — an owner who sizes a run, splits it into waves and leaves headroom. The behaviour the position builds on.
3. "I'm not super strict with myself, but I also try to use only a day's worth of my weekly allowance per day (ie: ~14% of my weekly limit per day)." ([r/ClaudeAI, Sep 2026](https://www.reddit.com/r/ClaudeAI/comments/1why2zx/a_lot_of_talk_about_reduced_weekly_limits_but_a/pa8dpqd/)) — an owner pacing the week by percent. Shows "weekly allowance" in use.
4. "Predictable limits, graceful checkpointing before cutoff, and reliable adherence to persistent instructions would make a huge difference. Right now, the usage anxiety is becoming part of the job." ([r/ClaudeCode, Jul 2026](https://www.reddit.com/r/ClaudeCode/comments/1uv6ns4/dear_anthropic_this_has_to_stop/oxakc8i/)) — what people ask for. The line "usage anxiety is becoming part of the job" is the problem in their words; the copy must not claim the cure.
5. "I upgraded to the 20x plan because the 5x wasn't enough, but most weeks I end up only using like 50-70% of my usage before it resets." ([r/ClaudeAI, Aug 2026](https://www.reddit.com/r/ClaudeAI/comments/1vfoq73/max_20x_user_here_only_burning_through_5070_of_my/)) — the person with allowance to spare. The audience the position does not yet speak to.

Reddit pages are opened and saved by hand by Almog; agents do not fetch Reddit. The quotes were checked by script against the saved comments. Full evidence: the research summary and `quotes_used.md`.

---

## Appendix A. What is true today, and what is only proposed

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

## Appendix B. Open decisions and gaps

1. **Mitchell's and Josh's confirmation.** Almog chose Allowance Guardrails on 2026-10-09; Mitchell and Josh have not confirmed. Josh is the only contributor to the runner, so every `today (runner)` statement needs his check.
2. **Which audience leads, and whether "play" is the frame.** This draft aims at people who pay their own way and think about their limit. The Reddit research shows a second group with allowance to spare, who want to know what a visit gives them and whose replies, when one of them asked what to do with the extra, are mostly useful jobs (scheduled agents, captioning a photo library, organising old drives), not play. If the team wants that group, the benefit has to change, and the word "play" may have to share the stage with a job.
3. **The name.** "Allowance Guardrails" names a feature whose protective half is proposed. Two readings of the word "guardrails" are in the evidence (safety rules vs a usage limit). Options: keep the name for the proposed set only and call what ships "the allowance"; or rename. The style pages currently tag the shipped cap as "Highlighted feature: Allowance Guardrails".
4. **What a visit can and cannot do, and whether anything reaches the owner's own Claude.** Not checked by the runner study. Questions for Josh: what can the daycare's own tools touch; can anything from a visit (saved memories, the day report) reach the owner's own sessions; can a visit spend money or post anywhere public.
5. **Does the allowance setting persist?** The runner has a default share; whether a chosen value persists between visits is not known.
6. **Is it allowed by the provider's terms?** Reddit voices asked and nothing read answers it. Not for copy to settle; check before launch. This is not legal advice.
7. **Employer-funded users.** A cap does not make play on a work account acceptable and Claude Daycare does not change who pays. This draft aims at people on their own plan. Decide whether to say so on the page, and whether work-funded users are a later audience or never.
8. **How far a visit can go over.** The size of one turn is not recorded anywhere in the runner, so `a little over` cannot be given a number. Josh's own visit records could answer it (repo study question 1).
9. **The Claude name and the not-affiliated question.** The product name contains Anthropic's trademark and the home page says nothing about any relationship. Open: whether to keep the name, and whether every page carries a plain not-affiliated line. This is not legal advice.
10. **Strength of the evidence.** The Reddit research supports that people protect their allowance by hand (32 of 39 threads) and that leftover allowance exists (18). It also shows strong pushback: about 50 texts across 20 threads say they never hit the limit, and one of the higher-scored replies (16 points) to someone with spare usage is to downgrade, though the top reply in that thread (21 points) is to run scheduled agents and several others list useful jobs. The interview evidence for the allowance promise is one paying user plus one employer-funded engineer. Real people still get the final vote.
11. **Permission for interview quotes.** The quote index asks that each person be checked with before a quote is used anywhere public.
12. **The site beyond the home page.** Only the home page was read; the hub and site code are not in the repo clone.

## Sources

The team's quote index and working synthesis of the ten interviews; the Reddit research (`reddit_research_summary.md`, `quotes_used.md`, `coverage.md`); and the team's read of the runner's code (the repo study, an internal AI draft, section numbers refer to it). The class template is `template_brand-position.md`.

*This document is the foundation for landing page copy and synthetic testing. When copy conflicts with this document, the copy is wrong.*
