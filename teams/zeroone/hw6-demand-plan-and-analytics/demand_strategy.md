# CallIt: marketing specification and demand strategy

**Team:** ZeroOne. **Product:** CallIt, a private record of a group's predictions.
**Prepared:** 2026-10-17 by Aviv Pinto (marketing manager) with Emily Zhou (traffic owner).
**Due:** Friday 2026-10-23, 1:10 PM New York time, for HW6: Demand Plan and Analytics.

## How this file maps to the assignment

The class does not define a separate "marketing specification". The graded marketing deliverable is `demand_strategy.md`, with five required items (Class 6, "Homework: your demand strategy"). Sections 1 to 5 below follow those five items in the slide's order and wording. Sections 6 to 10 are the rest of the marketing specification the team asked for. To submit, Zhangcheng (Charles) copies this file as `demand_strategy.md` into `teams/zeroone/hw6-demand-plan-and-analytics/` and opens the team pull request. The pull request is the submission. Source: the current assignment text supplied by Zhangcheng (Charles) on October 21, 2026. The evidence for published posts stays in [HW5 submission evidence](https://github.com/kenxle/columbia-startup-studio-fall-2026/pull/48) (the HW5 record) and is linked, not repeated.

The October 23 Courseworks instructions require a semester-wide plan to drive 100 signups. This document now includes a weekly schedule and a planning model below. Reach figures are estimates for planning. They are not measured audience sizes or confirmed commitments.

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

Planning reach assumptions for the remaining semester: Columbia group chats, 20–100 readers per relevant chat; founder social posts, 100–500 views per post; r/FFCommish contributions, 50–300 readers per useful thread. These are rough ranges for planning only. We have not collected member counts, platform analytics, or permission to promote in the forums. Count observed reach from each platform where available, and use tagged landing-page sessions as the visit measure.

## 3. Your first 3 posts, each linking to a landing page with a UTM

Three posts are published, all from Emily's personal accounts. The published links, captions and link checks are in [HW5 submission evidence](https://github.com/kenxle/columbia-startup-studio-fall-2026/pull/48), sections 4, 5 and 9.

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

Emily's planned post ("Everyone says 'I called it.' What should a group prediction record keep?", linking to `/for/friends`) is the second blog idea. Its outline is in [HW5 submission evidence](https://github.com/kenxle/columbia-startup-studio-fall-2026/pull/48), section 7.

## 5. Your welcome email, automated

**Status: live.** The welcome email sends after a new signup. Delivery is asynchronous. Provider acceptance does not establish recipient inbox placement.

Yuval built the automation in [PR #7](https://github.com/Yuval-Gerber/CallIt/pull/7), approved by Elad. `waitlist-service/email.js` sends the copy below through Resend after the signup response. Delivery state is recorded per address, and failed sends are retried with backoff. Copy changes go through that source file. Evidence: Yuval's October 23 database/server read-back on the team Bulletin Board.

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
> Aviv, Emily, Yuval, Elad and Zhangcheng (Charles)

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

The original first-week calendar below preserves the posts and tagged links already documented. The semester schedule follows it.

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

### Semester schedule and reach estimate

The plan covers the eight remaining weeks from October 26 through December 18. The target is 100 additional waitlist signups. At a 1% signup rate, this needs 10,000 visits, or 1,250 visits per week. The signup rate is a planning ceiling, not a measured conversion rate. Current evidence is too small to calculate a reliable rate.

| Week | Traffic owner | Planned activity | Planning reach assumption | Visit target |
| --- | --- | --- | ---: | ---: |
| Oct 26–Nov 1 | Emily, with Aviv | One founder social post; one warm group-chat invitation; answer relevant organizer questions without promotion in r/FFCommish. | 1,500 people | 1,250 |
| Nov 2–8 | Emily, with Aviv | One social post with a real product clip; one group-chat invitation; one community contribution. | 1,500 people | 1,250 |
| Nov 9–15 | Emily, with Aviv | Publish one problem-focused blog article; one social post linking to it; one group-chat invitation. | 1,500 people | 1,250 |
| Nov 16–22 | Emily, with Aviv | One tactical social post; invite a second warm group to try a real call; one community contribution. | 1,500 people | 1,250 |
| Nov 23–29 | Emily, with Aviv | One founder-journey post tied to a real product lesson; light holiday-week group outreach. | 1,500 people | 1,250 |
| Nov 30–Dec 6 | Emily, with Aviv | Publish one solution explainer; one social post; invite one group to use a call during the week. | 1,500 people | 1,250 |
| Dec 7–13 | Emily, with Aviv | One user-problem post; one social post; share the explainer with relevant warm groups. | 1,500 people | 1,250 |
| Dec 14–18 | Emily, with Aviv | One semester learning post and final warm outreach; report results before Demo Day. | 1,500 people | 1,250 |

**Estimate method:** the 1,500 weekly reach is a working assumption for combined personal social reach, warm group messages, and community reading. Platform follower counts and group sizes have not been collected. Replace this estimate with observed reach and unique landing-page sessions each Monday. Do not add overlapping channel reach as unique visitors without deduplication.

**Back-of-napkin result:** 8 × 1,250 = 10,000 visits. At the maximum planning rate of 1%, this yields 100 signups. If the actual rate is lower, the plan needs more traffic or more weeks. The current 11 real signups are the starting snapshot, not a conversion rate; the 212 design views include tests and cannot be used as the denominator.

### Blog schedule

Use the four article types from Class 6 slide 45. Emily reviews; Aviv drafts and publishes. Each article links to the matching audience page with lowercase UTMs.

| Target week | Type | Working title | Destination |
| --- | --- | --- | --- |
| Nov 9–15 | Problem-focused | Why friend groups remember the same prediction differently | `/for/friends` |
| Nov 23–29 | Founder journey | What our first user interviews changed about CallIt | `/for/agreements` |
| Nov 30–Dec 6 | Solution explainer | How a group can keep a prediction and its result together | `/for/agreements` |
| Dec 7–13 | Tactical advice | A short guide to writing a prediction with clear terms | `/for/sports` |

These are proposed dates. Emily and Aviv must confirm capacity and the publishing destination. The NBA season-calls draft remains a supporting article idea.

### Email lifecycle

- **New waitlist signup:** send the existing welcome email once per address. Yuval reported three sends accepted by Resend since activation. Provider acceptance does not prove inbox placement.
- **Product update:** Aviv and Emily prepare a short newsletter only when there is a real product change or a useful pilot result. The team has not approved a newsletter cadence.
- **Pilot invitation:** invite a group that agrees to try the product. Emily tracks the invitation and responses. Do not send automated activity emails; notifications are not part of the current product.
- **After a pilot call closes:** the manager records the result in the app. The team asks participants for feedback through the group's agreed channel.

Confirm email consent, owner capacity, and any newsletter schedule before sending new campaign email.

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
