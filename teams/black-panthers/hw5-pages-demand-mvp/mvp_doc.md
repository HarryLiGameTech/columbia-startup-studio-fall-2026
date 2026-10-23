# Plandit MVP

## Core flow: user, action, value

**User:** A college student who has saved places from TikTok, Instagram, screenshots, links, or group chats but has not turned them into an outing.

**Action:** The student adds 3-5 saved places, confirms their budget, available time, starting point, travel mode, and maximum distance, then asks Plandit to make a plan.

**Value:** Plandit returns a ready-to-go day with an ordered route, arrival times, estimated costs, and travel time between stops. The student can use the plan alone or share it with friends.

The MVP proves one thing: **Plandit can turn a small set of places a student already wants to visit into a sensible one-day plan that respects real constraints.**

## MVP flow

1. The student pastes links to 3-5 social media posts or manually adds places.
2. Plandit extracts or confirms each place's name, address, coordinates, category, estimated cost, and expected duration.
3. The places are saved to the student's list.
4. The student provides budget, start time, available time, travel mode, start location, and maximum travel distance or time.
5. Plandit selects and orders a subset of places that fits those constraints.
6. The app shows the plan on a map and in a list with times, costs, and travel legs.
7. The student can open stop details and share the plan.

A successful MVP demo completes this flow in under 30 seconds and produces a plan a teammate would realistically use.

## In scope

- Add a place from a TikTok or Instagram link
- Manual place entry when link extraction fails
- Saved-place list
- Place deduplication
- Budget, time, location, distance, and travel-mode constraints
- Selection and ordering of 3-5 stops
- Map and list views of the plan
- Timing, cost, and travel estimates
- Clear errors when a link or place cannot be processed
- A shareable plan

## Cut from the MVP

- A discovery feed or recommendation marketplace
- Support for every social platform
- Automatic processing of every video's audio and on-screen text
- Native payments, reservations, ticketing, or purchases
- Real-time friend voting, chat, or collaborative editing
- Public profiles, followers, or a social network
- Complex rewards or referral payouts
- Multi-day trips and vacation planning
- Perfect real-time opening hours, prices, or crowd levels
- Personalized machine-learning recommendations

## Faked or Wizard of Oz

- The demo uses a set of pre-tested links so a social platform change cannot break the presentation.
- If metadata extraction fails, the user can confirm or manually enter the place.
- A teammate may review low-confidence extracted places before they enter the demo database.
- Estimated price, visit duration, and opening hours may come from seeded data rather than a live provider.
- Seeded NYC places let planning work before the extraction pipeline is complete.
- Straight-line distance and average travel speed can substitute for a maps API when routing is unavailable.

These fallbacks must be visible as estimates or manual confirmation; they should not silently appear to be live data.

## Stack

| Layer | MVP choice |
|---|---|
| App framework | iOS-oriented mobile prototype using SwiftUI patterns and MapKit for the map and route experience |
| Landing site | Static HTML, CSS, and JavaScript |
| Data | Hosted Postgres, with tables for users, saved videos, places, saved places, plans, and plan stops |
| Email capture | Formspree |
| Analytics | Google Analytics 4 |
| Hosting | Vercel for the public landing site; hosted database/service for MVP data |
| Agent-assisted workflow | Feature Forge with Claude Code, plus GitHub Copilot CLI for repository and implementation support |

The database is the contract between extraction and planning. Place records include confidence so uncertain results can be confirmed rather than guessed.

## Roles

| Owner | Responsibility |
|---|---|
| Jaden Hinton | Video/link metadata extraction, place resolution, and app/web UI integration |
| Abraham Alemu | Database schema, hosted data service, seed data, and shared data contract |
| Eldad Tolla | Constraint-based place selection, route ordering, scheduling, and planner tests |
| Catherine Escobar | Brand and demand strategy, community messaging, landing-page copy, and traffic |
| Hunter Doradea | Demand execution, campus and social distribution, partnerships, and traffic reporting |

Hunter Doradea and Catherine Escobar jointly own traffic. Schema changes must be shared with the team before integration.

## Build order

1. Finalize the database schema and seed approximately 20 real NYC places.
2. Build extraction and planning in parallel against the shared schema.
3. Connect one pasted link through extraction, storage, and planning.
4. Replace prototype screen data with live database results.
5. Run the complete demo twice and keep pre-tested links as a backup.

## Acceptance criteria

- At least 5 of 8 test links return a correct place or a clear manual-confirmation state.
- Given the seeded places and sample constraints, the planner returns a valid plan in under 3 seconds.
- Total cost, total duration, and travel legs remain within the user's constraints.
- The plan appears on a map and in an ordered list.
- Tests cover budget, time window, travel limit, required stops, too few places, and no valid plan.
- Failures produce a clear message and do not create incorrect place or plan records.

