# CallIt: marketing specification and demand strategy

**Team:** ZeroOne. **Product:** CallIt, a private record of a group's predictions.
**Prepared:** 2026-10-17 by Aviv Pinto (marketing manager) with Emily Zhou (traffic owner).
**Due:** Friday 2026-10-23, 1:10 PM, with the working MVP (Class 6 slides, "Homework and what's next").

## How this file maps to the assignment

The class does not define a separate "marketing specification". The graded marketing deliverable is `demand_strategy.md`, with five required items (Class 6, "Homework: your demand strategy"). Sections 1 to 5 below follow those five items in the slide's order and wording. Sections 6 to 10 are the rest of the marketing specification the team asked for. To submit, Charles copies this file into the class folder as `demand_strategy.md` (folder name per the slides: `teams/zeroone/hw-mvp/`, which may change with the homework numbering). The evidence for published posts stays in [demand_strategy.md](../hw5-pages-demand-mvp/demand_strategy.md) (the HW5 record) and is linked, not repeated.

## 1. Your traffic owners, by name

| Owner | Responsibility |
| --- | --- |
| **Emily Zhou** | Owns the weekly traffic number: attributed waitlist signups by source and page. Reports it every Monday. |
| **Aviv Pinto** | Owns the plan and the posts: what goes out, where, when, and replies within 24 hours. |
| **Yuval Gerber** | Owns analytics and the pages: GA4, UTM capture, the `/admin` waitlist report, the welcome email. |

Every Monday, Emily and Aviv review the numbers with Yuval and pick one change for the week.

## 2. 2 or 3 communities, from your Reddit research

Our HW4 Reddit research list ([thread_list.md](../hw4-synthesis-brand-position/reddit_research/thread_list.md)) has 47 sources (searches and threads) across six subreddits, mostly r/SideProject (16) and r/FFCommish (13).

| Community | Why it fits | How we enter, within its rules |
| --- | --- | --- |
| **r/FFCommish** | League organizers there describe our exact problem: terms people remember differently, and no record of what was agreed. | Value first. Answer real league-management questions from experience. The rules forbid tool promotion, so no CallIt post and no link. |
| **r/SideProject** | The research found prediction-pool builders asking how to define results. Builders give direct product feedback. | Our two Reddit posts (r/SideProject and r/sideprojects) were removed by Reddit's filters on 2026-10-16. We asked the moderators for a review and post nothing more until it is answered. |
| **Columbia friend groups** (added after the research) | Warm reach with no promotion filter, and the audience our interviews support best: existing friend groups that already make calls. | Founder messages from our own accounts, in chats we belong to. Groups that say yes get a room invitation link to the live app. |

## 3. Your first 3 posts, each linking to a landing page with a UTM

Three posts are published, all from Emily's personal accounts. The published links, captions and link checks are in [demand_strategy.md](../hw5-pages-demand-mvp/demand_strategy.md), sections 4, 5 and 9.

| Post | Platform | Landing page | UTM link | Status |
| --- | --- | --- | --- | --- |
| P2 | Rednote | Friends | `https://call-it.app/for/friends?utm_source=rednote&utm_medium=post&utm_campaign=hw5_launch&utm_content=i_said_it` | Published |
| P3 | Instagram Reel (link in bio) | Sports | `https://call-it.app/for/sports?utm_source=instagram&utm_medium=bio&utm_campaign=hw5_launch&utm_content=knicks_spurs_reel` | Published 2026-10-16 |
| P4 | LinkedIn | Friends | `https://call-it.app/for/friends?utm_source=linkedin&utm_medium=post&utm_campaign=hw5_launch&utm_content=founder_post` | Published |

The next three posts (A1 to A3, week of 2026-10-19) are drafted in section 7.

## 4. One blog post, planned or published

**Drafted, not published.** The full draft is [docs/blog/season-calls.md](blog-draft.md) (696 words). Owner: Aviv drafts, Emily reviews. Target: published before the NBA opener on Tuesday 2026-10-20.

**Title:** Season-long calls: how to write a prediction your group can settle in April.
**Links to:** `https://call-it.app/for/agreements?utm_source=blog&utm_medium=owned&utm_campaign=launch&utm_content=season_calls`. This is the one landing page with no campaign traffic yet.

- **The problem:** a call made in October is judged months later. By then people remember different versions of it.
- **What to write down first:** the question, the choices, the closing time, and what counts, including the source for the result.
- **A worked example:** "Will the Knicks finish top four in the East?", with what counts defined as the final regular-season standings, and answers closing before the first game.

Emily's planned post ("Everyone says 'I called it.' What should a group prediction record keep?", linking to `/for/friends`) is the second blog idea. Its outline is in [demand_strategy.md](../hw5-pages-demand-mvp/demand_strategy.md), section 7.

## 5. Your welcome email, automated

**Status: merged on 2026-10-17, live after two server steps.** Yuval built it in [PR #7](https://github.com/Yuval-Gerber/CallIt/pull/7), approved by Elad. `waitlist-service/email.js` sends the copy below, word for word, through Resend. It goes out after the signup response, so it never blocks the signup. Each delivery is recorded per address, so the email never repeats, and failed sends are retried with backoff. It starts sending once Elad updates the hosted database schema and places the sending key on the server. A test signup with a fresh address then confirms delivery. Wording changes go through `waitlist-service/email.js`.

**Trigger:** a new waitlist signup on any landing page, sent once per email address.
**From:** CallIt, from the team's sending address. **Subject:** You're on the CallIt list.

> Hi,
>
> Thanks for joining the CallIt waitlist.
>
> CallIt keeps a record of your group's predictions. Make a call, everyone answers once, and after it closes, the group sees who called it.
>
> The app is open now. Want to try it with your group? Create a room and send your friends the invitation link: https://app.call-it.app
>
> No money in CallIt. Just the record.
>
> We're a student team at Columbia, and we read every reply. Tell us which call your group would make first.
>
> Aviv, Emily, Yuval, Elad and Charles

The waitlist signup records where the person came from. The email's app link has no UTM, because the app does not record UTMs yet.

## 6. Audience, positioning and the three landing pages

**Thesis:** Being right is better when your group remembers. **For** friends and communities who make predictions together, **CallIt** is a shared record. Each call has clear terms, one answer per person, and a result the group can revisit. Source: [brand_position.md](../hw4-synthesis-brand-position/brand_position.md).

| Page | Audience | What it promises |
| --- | --- | --- |
| [call-it.app/for/friends](https://call-it.app/for/friends) | Friends making everyday calls (who's late, who texts back first) | Remember who called it. |
| [call-it.app/for/sports](https://call-it.app/for/sports) | Friend groups that follow sports | Collect picks without copying chat messages. |
| [call-it.app/for/agreements](https://call-it.app/for/agreements) | Groups with calls that stay open for weeks | Keep the original agreement clear. |

The homepage is [call-it.app](https://call-it.app). Every page has one call to action, the waitlist signup.

## 7. Channels, the post calendar and the weekly loop

| Day | Post | Where | Page | UTM link |
| --- | --- | --- | --- | --- |
| Mon 10-19 | A1: founder post, the app is live | LinkedIn, Aviv | friends | `https://call-it.app/for/friends?utm_source=linkedin&utm_medium=post&utm_campaign=launch&utm_content=aviv_live` |
| Tue 10-20 (NBA opening night) | A2: season calls Reel | Instagram (and TikTok), Aviv, link in bio | sports | `https://call-it.app/for/sports?utm_source=instagram&utm_medium=bio&utm_campaign=launch&utm_content=season_calls` |
| Wed 10-21 to Fri 10-23 | A3: "try one call with us" | Two or three Columbia group chats | friends | `https://call-it.app/for/friends?utm_source=groupchat&utm_medium=dm&utm_campaign=launch&utm_content=try_one_call` |

The full post copy is in [docs/demand_strategy.md](weekly-plan.md), our weekly plan. All links use lower-case UTMs.

**Weekly loop:**
1. **Monday:** review the numbers and pick one change.
2. **Monday to Friday:** publish three posts and record each live link the same day.
3. **Within 24 hours of each post:** reply to real comments.
4. **Friday:** post a summary to the team.

## 8. The numbers we track and where they are read

| Number | Where it is read |
| --- | --- |
| Waitlist signups by source, medium and campaign | `/admin` on app.call-it.app (waitlist by source); `waitlist_attribution` table |
| Sessions and `sign_up` events by source and page | GA4 (property `G-HPKQ2CBQT7`): Realtime, and Acquisition, Traffic acquisition |
| Signups per session, per landing page | GA4, with `page` as a custom dimension |
| Rooms created from warm groups, and their members | The app's database, counted by Yuval on Monday |

Setup details are in [docs/ANALYTICS.md](analytics.md). Still open: marking `sign_up` as a key event in GA4. We set baselines at the first Monday review instead of inventing targets.

## 9. Budget

No paid spend. The only cost is the team's time. Paid ads come after the MVP presentations, per the Class 6 slides.

## 10. Rules for every post

- Founder posts from personal accounts, with the student team disclosed.
- Use the brand's words: call, prediction, group, who called it. No betting words.
- Say "No money in CallIt" when money comes up.
- Follow each community's rules. A removed post is recorded and never reposted as is.
- Show the product as it is today. Do not promise open decisions such as points or disputes.
