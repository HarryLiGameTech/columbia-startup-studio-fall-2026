# Weekly Update: AstraPath (Team Pola), November 13, 2026

## Accountability: what we did

This is our first weekly update, so there's no earlier plan to compare against.

### Tech (build)

- **Harry (Jiawen Li)** worked on our routing engine, TopoNavi:
  - A refactor that moves the existing GitHub sign-in service out of the engine.
  - Perception-aware semantics and guidance algorithms.
  - Custom elevator waiting-time calculation, using algorithms our mappers contributed.
- **Hailey (Yining Ma)** developed the web frontend for our app.
- We put the Google tag in the `<head>` of all six pages on our site and connected our Google Analytics ID. Before, a script added the tag after the page loaded, so it didn't show in the page source.

### Marketing (grow, analyze)

- **Sophia Hirao** did customer outreach and talked with 2 departments at our school. Both were interested and gave us useful insights.
- **Isha Mitra** set up our TikTok and Instagram accounts and is publishing promo videos, with help from Harry.
- We wrote our [demand strategy](hw6-demand-plan-and-analytics/demand_strategy.md) through Demo Day, with traffic owners for every week.
- We set up Google Analytics 4 with `sign_up` as a key event, and confirmed page views and a signup in Realtime on November 11.

### Product (build, research)

- **Hailey and Harry** built more demos for business customers: hospital workflow, elevator operation, and warehouse operation optimization models.
- **Oleh Goumain** mapped 2 more buildings at Barnard College.
- We ran 3 usability sessions (homework 7), one with a stranger, and all 3 testers reached the aha moment. Search was the weakest step: "Northwest Corner 502" returned a route to a water fountain. Step-free wasn't seen as part of the route on screen. See our [usability synthesis](hw7-usability-testing/usability_synthesis.md).

### Fundraising

- The week before, we applied to Y Combinator and a16z. We think both are unlikely to come through.

## Planning: what we're doing next

### Product and tech (build)

- **Barnard:** finish mapping the Barnard buildings, now that we have their floor plans.
- **iOS app:** develop the AstraPath iOS app.
- **Landmark demos:** add demos of well-known buildings, such as Shanghai World Financial Center (SWFC).
- Start the three changes from our usability synthesis:
  1. Search returns the exact room you asked for, or says it can't. It never shows a route to a different place.
  2. A step-free switch on the route card. Each elevator is named with the floors it stops at.
  3. Long "keep going straight" steps end at a landmark you can see.

  **Why:** these are the steps where our testers got stuck or lost confidence. The first two come right before the aha moment, and the third right after it.

### Marketing (grow, analyze)

- Harry publishes the promo video on bilibili, and Isha posts a vertical cut on Instagram and TikTok. Our first blog post (founder journey: what 6 interviews taught us) goes up in the week of November 16.  
  **Why:** bilibili carries almost all of our signup estimate (about 50 signups in the average case), so the video comes first.
- At the end of week 2 (November 22), compare bilibili signups (`utm_source=bilibili` in Netlify Forms) with the average-case pace in our demand strategy.  
  **Why:** it tells us whether we need a second video or more posts.

### Fundraising

- Apply to PearX. This time the application will say more about how we'll make money.

### Research

- None this week.

## Issues

- None this week.
