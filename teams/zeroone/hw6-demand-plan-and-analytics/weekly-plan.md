# CallIt demand strategy (living plan)

**Owners:** Aviv (`@Aviv`, marketing manager: the plan and the posts) and Emily (`@Emily`, owns the weekly traffic number).
**Started:** 2026-10-17. **Covers:** the week of Monday 2026-10-19 to Sunday 2026-10-25, then rolls forward each Monday.
**Status:** plan and post drafts. Nothing in this document has been published yet. Rows move from "draft" to "published" only with a live link.

This file is the weekly operating plan. The HW5 submission, with the first five posts, their captions and their verified links, stays in [homework/hw-5/demand_strategy.md](https://github.com/Yuval-Gerber/CallIt/blob/codex/charles-delivery-checklist/homework/hw-5/demand_strategy.md). This plan builds on it and does not repeat it.

The class-ready version, structured as the graded `demand_strategy.md` with the welcome email and the full marketing specification, is [homework/hw-5/marketing_spec.md](https://github.com/Yuval-Gerber/CallIt/blob/codex/charles-delivery-checklist/homework/hw-5/marketing_spec.md).

## What week one taught us

| Observation (from the HW5 record) | What we change |
| --- | --- |
| Both Reddit posts were removed by Reddit's filters within minutes (new account, promotional link). | No more cold promotional posts on Reddit. Reddit becomes a place to contribute without links until the account has history. |
| The three posts that stayed up were on personal accounts with real followers (Rednote, Instagram, LinkedIn). | Week two uses warm reach first: our own networks, group chats and personal accounts. |
| The strongest hook in every post was the moment everyone "called it" after the fact. | Keep that hook. Lead with one concrete scene, then the four steps, then one question. |
| `/for/agreements` has had no campaign link yet. | The blog post points there, so all three audience pages get tested. |
| The app is now live on app.call-it.app with real rooms, answers, results and the settle-up ledger. | Posts can show the real product instead of a concept. **Decided by Yuval (2026-10-17, PR #3):** posts keep pointing at the waitlist pages, because only they record UTM attribution and GA4 today. A warm friend group gets a room invitation link instead: one of us creates the room and sends its link, and we count the room's members. |

## 1. Who owns traffic every week

| Job | Owner | When |
| --- | --- | --- |
| The weekly number: attributed waitlist signups by source and page | Emily | Reported every Monday |
| The plan, the posts, replies to comments within 24 hours | Aviv | Posts Monday to Friday; this file updated every Monday |
| Monday review of the numbers on `/admin` (waitlist by source) and GA4 | Emily and Aviv, with Yuval | Every Monday; first one 2026-10-19 |
| Analytics setup (`sign_up` key event, `page` custom dimension) | Yuval | Open per [docs/ANALYTICS.md](https://github.com/Yuval-Gerber/CallIt/blob/codex/charles-delivery-checklist/docs/ANALYTICS.md) |

**The number we track:** attributed waitlist signups per week, split by `utm_source` and landing page. Supporting numbers: sessions per source, and signups per session per page. We set the baseline at the first Monday review instead of inventing a target now.

## 2. Communities for week two

| Community | Why | How we enter | Page |
| --- | --- | --- | --- |
| **Columbia friend groups** (our own group chats, class group chats where sharing is welcome, Instagram followers) | Warm reach, no promotion filters, and the exact audience the research supports best: existing friend groups that already make calls. | A short personal message asking groups to try one real call. Members of the team post from their own accounts. | `/for/friends` |
| **Friends who follow the NBA together** | The start of the NBA season is a natural moment for season-long calls ("Who makes the playoffs?") and game-night calls. Sports was the clearest scenario in week one. | One short video on Instagram (and TikTok if Aviv has an account), framed around opening week. Confirm the opening date before posting. | `/for/sports` |
| **r/FFCommish** (from the HW4 research: 14 of the threads) | Organizers there talk about the exact problem: terms people remember differently and records nobody keeps. | Value first, no links: answer two or three real league-management questions from experience this week. Rules forbid tool promotion, so no CallIt post and no UTM link here. | none |

r/SideProject and r/sideprojects are paused until the moderator review from week one is answered.

## 3. Three posts this week (Aviv)

All links use lower-case UTMs. `utm_campaign=launch` follows the format on the board; `utm_content` tells posts apart. Each row is a **draft** until it has a published link.

| ID | Day | Where | Page | Tagged link | Status |
| --- | --- | --- | --- | --- | --- |
| A1 | Mon 10-19 | LinkedIn, Aviv's account | friends | `https://call-it.app/for/friends?utm_source=linkedin&utm_medium=post&utm_campaign=launch&utm_content=aviv_live` | draft |
| A2 | NBA opening week | Instagram Reel (and TikTok), Aviv's account; link in bio | sports | `https://call-it.app/for/sports?utm_source=instagram&utm_medium=bio&utm_campaign=launch&utm_content=season_calls` | draft |
| A3 | Wed 10-21 to Fri 10-23 | Two or three Columbia group chats, one message each | friends | `https://call-it.app/for/friends?utm_source=groupchat&utm_medium=dm&utm_campaign=launch&utm_content=try_one_call` | draft |

For TikTok, reuse A2 with `utm_source=tiktok`.

### A1. LinkedIn (draft)

> Last week my friends argued for ten minutes about a prediction from August. Nobody disputed the result. They disputed what we had agreed to.
>
> I just joined the team building CallIt, a private record of your group's predictions. It is live now, and we are running our own group's calls on it:
>
> - Make a call: a question, a closing time and one line on what counts.
> - Everyone answers once. Answers lock.
> - After it closes, the group's manager records the result.
> - The group sees who called it.
>
> No money in CallIt. Just the record.
>
> If your group keeps arguing about who said what, I would love for you to try it and tell me what is missing.
>
> https://call-it.app/for/friends?utm_source=linkedin&utm_medium=post&utm_campaign=launch&utm_content=aviv_live

Before posting, Aviv replaces the opening line with a true story of his own. Do not post an invented anecdote.

### A2. Instagram Reel (draft)

**Video, about 15 seconds:** a phone screen recording of the live app. Make a call "Will the Knicks make the playoffs?", three friends answer, the answers lock. End card: "Lock it in now. Settle it in April." with the CallIt logo.

**Caption:**

> Everyone has a take on opening night. By April nobody remembers theirs.
>
> CallIt keeps your group's season calls on record. One answer each, locked, and the group sees who called it.
>
> Preview and early access: link in bio.
>
> #CallIt #NBA #Knicks #GroupChat #StudentStartup

Set the bio link to the A2 URL before posting and check that it keeps all four UTMs.

### A3. Group chat message (draft)

> Hey all, a few of us are building CallIt for our startup class: a shared record of your group's predictions (who's late, who wins the game, who texts back first). Would you try one real call with us this week? Takes a minute: https://call-it.app/for/friends?utm_source=groupchat&utm_medium=dm&utm_campaign=launch&utm_content=try_one_call

Send it only in chats where you are a member and where sharing a project is normal. One message per chat, no follow-up spam.

For a close friend group that says yes, skip the waitlist: create a room on app.call-it.app, post their first call, and send the room's invitation link. Record the room and its member count in this file on Monday.

## 4. One blog post we can write now

**Title:** Season-long calls: how to write a prediction your group can settle in April
**Links to:** `/for/agreements` with `https://call-it.app/for/agreements?utm_source=blog&utm_medium=owned&utm_campaign=launch&utm_content=season_calls`
**Owner:** Aviv drafts; Emily reviews. This is a second idea next to Emily's planned post in the HW5 document, aimed at the page that has no traffic yet.

- **The problem:** a call made in October is judged months later, and by then people remember different versions of it. Use the opening-week example.
- **The four things to write down first:** the question, the choices, the closing time, and what counts (including the source for the result).
- **A worked example:** "Will the Knicks finish top four in the East?", with what counts defined ("final regular-season standings on NBA.com") and answers closing before the first game. Then what happens in April: the manager records the result, and the group sees who called it.

## 5. Weekly loop

1. **Monday:** review last week's numbers with Yuval (`/admin` and GA4). Emily posts the number on the board. Aviv updates this file: what worked, the next three posts, one experiment.
2. **Monday to Friday:** publish the three posts. Record each live link in section 3 the same day.
3. **Within 24 hours of each post:** reply to genuine comments. Note feature requests in this file.
4. **Friday:** a one-line board row with what was published and anything that went wrong.

## Rules for every post

- Use the brand's words: call, prediction, group, manager, who called it. Never betting words: no "bet", "odds", "payout", "stake", "wager", "cash out", "win money".
- Say "No money in CallIt" when money comes up. Settling up happens outside the app.
- Disclose that we are a student team. Show the product as it is today and do not promise features that are open in [web-app/docs/product-rules.md](https://github.com/Yuval-Gerber/CallIt/blob/codex/charles-delivery-checklist/web-app/docs/product-rules.md) (points, disputes, reactions, public groups).
- Follow each community's rules. If a post is removed, record it and do not repost the same thing.

## Open items

- **OPEN (Aviv):** a true opening story for A1, and the NBA opening date for A2.
- **OPEN (Emily):** first Monday number on 2026-10-19; check whether the week-one Reddit moderator review was answered.
