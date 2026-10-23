# HW5 — Restroom Ready

**Team:** Five Girls

**Date:** October 16, 2026

**Product:** [Restroom Ready](https://nyc.imfinethanku.me/)

**Development repository:** [imnotmomo/nyc-restroom](https://github.com/imnotmomo/nyc-restroom)

Restroom Ready helps people choose a restroom in NYC before making the trip. The public website includes four marketing pages, an email signup flow, and an interactive demo with one sample location. The full finder requires team access during development and uses a dated city dataset, with separate community ratings and visitor-submitted locations. It does not establish current availability or complete NYC coverage.

## Public pages

| Page | URL | Purpose |
| --- | --- | --- |
| Homepage | [nyc.imfinethanku.me](https://nyc.imfinethanku.me/) | Introduce the product and collect emails. |
| Conditions | [Conditions](https://nyc.imfinethanku.me/conditions/) | Test interest in knowing usable basics before walking over. |
| Entry and route | [Entry and route](https://nyc.imfinethanku.me/entry-route/) | Test interest in permission, floors, stairs, and the route inside. |
| Dated reports | [Dated reports](https://nyc.imfinethanku.me/dated-reports/) | Test interest in sources, dates, and visible unknowns. |
| Interactive demo | [Try the demo](https://nyc.imfinethanku.me/demo/) | Try one sample location, filters, ratings, saves, additions, and passcode visibility without an account. Changes are simulated and reset on reload. |
| Thank-you | [Thank-you](https://nyc.imfinethanku.me/thank-you/) | Confirm a successful email signup. Opening this URL alone does not count as a signup. |
| Privacy | [Privacy](https://nyc.imfinethanku.me/privacy/) | Explain waitlist, account, contribution, and Analytics data. |

The full [finder](https://nyc.imfinethanku.me/find/) is a separate team-access page. Its shared access gate is separate from Google Sign-in for account-owned contributions.

## Submission files

- [Demand strategy](demand_strategy.md): audiences, named owners, campaign links, Facebook and X outreach, the published blog, and measurement.
- [MVP document](mvp_doc.md): core flow, shipped scope, cuts, manual work, stack, responsibilities, and the October 23 demo.

## Analytics and learning

Google Analytics measurement ID **`G-YJG2N05KY9`** is connected to the seven public routes above and the full finder after team access is granted, on the team domain. Actual page visits were observed in Realtime. Successful waitlist submissions trigger **`generate_lead`**, configured as a key event. That event counts completed successful submissions; distinct stored email records are needed to count unique leads. Demo page visits are tracked, but simulated demo actions do not send action events. Test visits used to verify the setup are not customer demand.

Pageviews use approved routes and lowercase UTM labels. Emails, Firebase account IDs, private notes, search text, and precise coordinates are excluded. Automatic outbound and form tracking is disabled. The product repository records the [actual setup and verification](https://github.com/imnotmomo/nyc-restroom/blob/main/docs/features/google-analytics.md).

**Analytics Academy:** enrolled in Google's current [Google Analytics Certification (2026) learning path](https://skillshop.docebosaas.com/learn/courses/18609/google-analytics-certification-2026). The older standalone 101 and 102 links supplied by Google's Help page returned “Access denied” after sign-in. The current path contains the matching introductory sections:

- **101 topic:** Get Started Using Google Analytics (GA). Its first activity, “Understand Google Analytics and Its Role in Business Growth,” was opened and Skillshop confirmed it was started on October 16.
- **102 topic:** Manage GA Data and Learn to read reports. Its first activity, “Navigate Your Google Analytics Account,” was opened in the training player on October 16.

These are course starts, not course completion or certification.

## Remaining submission steps

Real credited NYC photographs have been added to all four marketing pages; sources, photograph dates, and CC BY 4.0 credits are visible.

The current three-placement plan is the New York&People Facebook group, the published X post, and the published Medium article. Record the Facebook permalink and actual landing-page link to finish documenting the three placements. The Reddit research communities remain documented in the demand strategy, together with the observed submission outcomes and the change in distribution. Submit one team PR with this folder, then paste its link into Courseworks. The working MVP and five-minute in-class demo are due October 23 at 1:10 PM.
