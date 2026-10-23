# Demand Strategy — Restroom Ready

**Team:** Five Girls

**Date:** October 16, 2026

**Traffic owner:** Zheli Chen

**Campaign:** `hw5`

## Goal and audience

We want people who spend time out in NYC to visit a restroom information page and join the waitlist for updates. Our first audience is students, residents, and visitors walking between places. We are testing three reasons to care: usable conditions, entry rules and the route inside, and knowing the source and age of a report.

Each landing page offers email signup and a public sample demo. The full finder remains behind team access during development. Waitlist signup measures interest in updates; it does not establish that someone used a restroom.

Our seven-day target is **50 campaign sessions and five distinct waitlist emails** across Facebook, X, and the blog. These are planning targets, not results. This sprint uses organic outreach, with no paid ads.

## Communities and distribution

Our [HW4 Reddit research](../hw4-synthesis-brand-position/reddit_research/research_summary.md) covered two communities:

- **[r/AskNYC](https://www.reddit.com/r/AskNYC/):** informs the questions and language around finding a restroom. Its rules prohibit promotion and solicitation.
- **[r/nyc](https://www.reddit.com/r/nyc/):** informs the citywide problem and public-restroom context. Its [posting rules](https://www.reddit.com/r/nyc/wiki/sidebarrules/) restrict market-research requests, and a [moderator notice](https://www.reddit.com/r/nyc/comments/1uhgzrw/removed/) specifically mentions generic restroom-finder apps.

Reddit submissions were filtered, so the active distribution plan uses the **New York&People Facebook group**, **X**, and **Medium**. Filtered Reddit posts are not counted as live outreach. Zheli publishes and follows up on all three placements, maintains the tagged links, and checks campaign sessions and signups after 24 hours and seven days.

The Facebook group is a place to introduce the project to people interested in New York. The X post gives a short product introduction with a direct waitlist link. The Medium article explains the design decisions behind the product. We will use actual visits and responses to judge whether these audiences include people who need the app.

## First three posts

| Placement | Message and audience | Landing-page link | Publication record |
| --- | --- | --- | --- |
| New York&People Facebook group | Introduce Restroom Ready to the group's readers and invite waitlist signup. | The actual published link still needs to be recorded. | Zheli reports posting on October 16. The post permalink is still needed. |
| [X introduction](https://x.com/88boiwe0n/status/2111142704390496429) | A short introduction for prospective NYC users: entry rules, stairs, cleanliness ratings, and dated reports. | [Entry and route](https://nyc.imfinethanku.me/entry-route/?utm_source=x&utm_medium=organic_social&utm_campaign=hw5&utm_content=entry_route_x_launch) | Published as @88boiwe0n on October 16 at 1:10 PM EDT. The post page and its tagged destination were checked. |
| [Medium: Building Restroom Ready: Making a restroom pin useful](https://medium.com/@zc2856/building-restroom-ready-making-a-restroom-pin-useful-f690320d261e) | Explain the product to readers interested in the NYC restroom problem and how we are approaching it. | [Conditions](https://nyc.imfinethanku.me/conditions/?utm_source=blog&utm_medium=organic_content&utm_campaign=hw5&utm_content=restroom_checklist) | Published October 16 by Zheli, account @zc2856. Publication confirmation was observed. |

The X post reads:

> We're building Restroom Ready, a NYC bathroom finder with entry rules, stairs, cleanliness ratings, and dated reports.
>
> Join the waitlist for updates:

The tagged entry-and-route link follows that text. The post describes a product in development and makes waitlist signup the primary invitation.

For Facebook, we still need the permalink and the link that was actually posted. If updating that post, use [this dated-reports destination](https://nyc.imfinethanku.me/dated-reports/?utm_source=facebook&utm_medium=organic_social&utm_campaign=hw5&utm_content=new_york_people). We will not attribute earlier untagged visits to that campaign.

All UTM keys and values are lowercase. X uses `utm_source=x`, `utm_medium=organic_social`, and `utm_content=entry_route_x_launch`; the blog uses `utm_source=blog`, `utm_medium=organic_content`, and `utm_content=restroom_checklist`. All use `utm_campaign=hw5`. Names, emails, and other personal information do not go into campaign parameters.

## Blog

Zheli published [Building Restroom Ready: Making a restroom pin useful](https://medium.com/@zc2856/building-restroom-ready-making-a-restroom-pin-useful-f690320d261e) on October 16. The article explains why entry rules, the route inside, and conditions need separate fields; what update and verification dates establish; and how private and public passcode reports coexist. It also explains the sample-data boundary of the public demo and ends with a link to the conditions page.

## Measurement and follow-up

Google Analytics **`G-YJG2N05KY9`** tracks the homepage, three benefit pages, demo, privacy, thank-you, and the finder after team access is granted, on the team domain. Successful waitlist signup emits the **`generate_lead`** key event. Opening the thank-you URL directly does not create a lead. Demo actions are simulated and do not establish real restroom use.

After 24 hours and seven days, Zheli records campaign sessions by source and content, landing pages, and successful signup events. Distinct stored emails determine unique leads; repeated successful submissions can produce additional Analytics events. Team verification visits are kept separate from customer demand.

| Signal | Next action |
| --- | --- |
| Platform activity but few attributed sessions | Check link availability and UTM parameters. |
| Sessions but few signups | Review the page's promise, CTA, and readers' questions. |
| Interest in missing entry or route facts | Collect a manageable set of genuine dated observations. |
| Few ratings or many unknowns | Keep missing information visible rather than inventing reports. |

The channels and messages differ, so their results are directional rather than a controlled A/B test. Campaign sessions and signup results have not yet been recorded. X and Medium have publication links; the remaining publication documentation is the Facebook permalink and actual landing-page destination.
