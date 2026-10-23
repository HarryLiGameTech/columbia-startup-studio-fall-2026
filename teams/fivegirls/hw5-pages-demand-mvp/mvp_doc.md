# MVP — Restroom Ready

**Team:** Five Girls

**Date:** October 16, 2026

**Public demo:** [nyc.imfinethanku.me/demo](https://nyc.imfinethanku.me/demo/)

**Team finder:** [nyc.imfinethanku.me/find](https://nyc.imfinethanku.me/find/) — shared access passcode required

**Development repository:** [imnotmomo/nyc-restroom](https://github.com/imnotmomo/nyc-restroom)

**Demo:** October 23, 2026, 1:10 PM; five minutes.

## Problem and first user

Someone spending the day in an unfamiliar NYC neighborhood needs a restroom they can reasonably try. A nearby location is only the start. Entry restrictions, the route inside, old information, and missing details can change the decision.

Our first users are NYC students and residents walking between places. The product is a phone-friendly web app so someone can open a shared link immediately. This submission's MVP is the existing web app; a native iOS app is outside this sprint.

## Core flow

1. Open **Try the demo** from a public marketing page. Explore the sample without an account. The real directory is available separately through the team's access gate.
2. In the unlocked finder, search for a place, pan/zoom the map, or choose **Locate me** to request browser location. The list starts in Name A–Z order. Distance sorting becomes available after location is shared; there is no default starting point. Without permission, search, the list, and map still work.
3. Compare nearby listings in the list or on the map. At a wide zoom, numbered clusters group locations; individual places appear as the user zooms in.
4. Open a listing. Read the source, data date, published details, available ratings, and separate entry, route, and condition fields. Missing facts remain “Not reported.”
5. Open walking directions in an external map. This is the end of the main lookup flow.

The finder access gate and Google Sign-in serve separate purposes. After unlocking the finder, browsing does not require a Google account. Google Sign-in is required to save a place, keep a private visit note, rate cleanliness, submit or verify a passcode, or log a missing restroom. Public demo actions simulate these interactions without signing in. Email signup on a marketing page is a separate way to ask for updates.

## What is already built

| Area | Current behavior | Boundary |
| --- | --- | --- |
| Public demo | One Target Herald Square example with local viewing, filters, saves, ratings, notes, new-place logging, and passcode checks. | Sample restroom facts and actions are labeled. No Google account, Firebase writes, or persistent changes; reload resets the examples. The street address supplies context, not proof of the sample restroom details. |
| Team finder access | The real directory requires a shared server-checked passcode before its page loads. | This gate is separate from Google accounts and does not make the underlying public city data confidential. Its secret is not included in submission files or public links. |
| Directory | 1,064 distinct locations imported from all 1,066 source rows, with two exact duplicates merged. | Citywide source snapshot, not every restroom in NYC. The city data-update date is June 27, 2025; retrieval was October 15, 2026 in New York. Neither date is a team inspection. |
| Search and map | Search, list selection, compact pins, clusters, location request, name/distance sorting, and external walking directions. | Distance is straight-line from the shared location, not a measured walking time. No distance is shown before location is shared. Browser permission and map/network availability still apply. |
| Filters | **ALL**, **Public**, **Clean (4★+)**, **Accessible**, and **Saved**. | Public does not guarantee unrestricted or free entry. Clean requires ratings averaging at least four stars and excludes unrated places. In the real directory, Accessible matches the city's facility label; it does not certify the route or stall. Saved requires Google Sign-in in the real finder and uses local sample state in the demo. |
| Google accounts | Firebase Google Sign-in and restored account state in the real finder. | Browsing after the page access gate does not require sign-in. Account writes have emulator checks; a real team-account sign-in remains a rehearsal check. The public demo has no account UI. |
| Public ratings | Read an average/count without Google Sign-in. Signed-in users can drag or tap directly across the stars to choose 1–5 in 0.5 steps, then submit, update, or remove their rating. | One current vote per account and place. An empty summary is not a review, and a rating does not establish today's condition. Demo ratings stay local. |
| Saved places and notes | Save places and keep account-owned visit notes in Firestore. | Notes remain private; they are not public condition reports. |
| Log a restroom | Signed-in users can search an address or request nearby address suggestions. Selecting one fills the public address and pin together; manual corrections remain available. The form includes category, entry/route observations, code requirement, and an optional code with its own visibility. | The form starts with no chosen pin. Browser location helps find candidate addresses; it is not automatically the restroom's location. Contributions are visitor reports, separate from city data. Only the latest 1,000 submissions load; location editing and moderation tools remain future work. |
| Restroom passcodes | Show public reports and the signed-in user's own private code, with separate last-updated and last-verified times. Codes default to Only me, which also saves the place. Only the submitter can edit a report or change its visibility. | Reports can disagree and remain separate. Verification is a visitor's report of successful use of that code version, not a guarantee. Editing the code clears its prior verification. Demo public 3434 and owned private 3535 are separate sample reports. |
| Marketing and signup | Homepage plus conditions, entry/route, and dated-reports pages; durable email signup, a thank-you page, and automated Cloudflare confirmation receipts for new signups. | A primary-site test receipt was received. Delivery can be delayed or fail, and repeated/historical signups do not resend. Joining the waitlist does not create a Google account. Marketing examples remain illustrative. |
| Analytics | GA4 on eight approved routes on the team domain: the homepage, three benefit pages, demo, privacy, thank-you, and finder after access is granted. Successful signup emits `generate_lead`. | Demo actions are not tracked. The event counts successful submissions, including repeat addresses; database records determine unique emails. Setup checks are not demand. No emails, account IDs, notes, passcodes, search text, or precise coordinates go to Analytics. |

## What we are cutting

We are freezing the working lookup flow for this demo. These features are outside the October 23 scope:

- A native iOS app or App Store release.
- Booking, payments, subscriptions, or paid promotion.
- Live occupancy, queues, guaranteed opening hours, or automated cleanliness verification.
- Turn-by-turn navigation inside our site, indoor routing, or certified wheelchair accessibility.
- A new external review feed, automated venue scraping, or automatic policy updates.
- Public free-text discussions, photo uploads, push notifications, and a moderation dashboard.
- A complete system for conflicting per-field reports. The marketing pages describe that direction; the current finder does not yet resolve every disagreement automatically.

If a rehearsal exposes a failure in browsing, permissions, data loading, sign-in, or saving, that repair takes priority over adding features.

## Manual and simulated parts

**Source refresh:** the city directory is a bundled snapshot refreshed by a script and reviewed before deployment. It is not a live city feed. The team has not inspected all listings or verified their current hours and conditions.

**Entry and condition details:** official fields stay separate from optional visitor submissions. We need actual visitors to contribute missing observations. We will not fill gaps with guessed rules, generated reviews, or invented ratings.

**Public demo:** Target's street address is sourced, but its example ratings, entry/route attributes, codes 3434 and 3535, and verification timestamps are simulated. Adding a sample place, rating, saving, or verifying a code changes only the current page's memory. Reloading resets it. The real finder uses the city snapshot and Firestore, with its page access gate kept separate.

**Map provider:** the default finder and public demo use Leaflet with OpenStreetMap tiles. A MapKit JS adapter exists for the finder, but Apple authorization and rendering have not been verified. Activating it requires a genuine domain-restricted Apple token and a rebuild. Browser location cannot bypass Safari or operating-system permission settings.

**Marketing examples and imagery:** example listing values explain the proposed experience and stay labeled as examples. Website photography supplies context; it is not evidence that the pictured restroom is currently usable.

**Outreach and updates:** this week's acquisition plan is a New York&People Facebook group post, the [published X introduction](https://x.com/88boiwe0n/status/2111142704390496429), and the [published Medium article](https://medium.com/@zc2856/building-restroom-ready-making-a-restroom-pin-useful-f690320d261e). Zheli owns all three. The social posts invite prospective NYC users to join the waitlist. The X post was published October 16 at 1:10 PM EDT and contains a tagged entry-and-route link. Zheli reports the Facebook post is published; its permalink and actual landing-page link still need to be recorded in [the demand strategy](demand_strategy.md). Reddit submissions were filtered and do not count as live outreach. The team publishes, replies, and records actual outcomes manually. New waitlist signups automatically queue a transactional receipt; later product updates and any campaign emails are separate work.

## Stack and development process

| Part | Choice |
| --- | --- |
| Frontend | Next.js, React, TypeScript, and CSS; static export with client-side finder components. |
| Map and address lookup | Leaflet/OpenStreetMap; optional finder MapKit JS adapter pending Apple authorization. Browser Geolocation for explicit requests; NYC Planning GeoSearch for selected address and nearby suggestions. |
| Accounts and data | Existing Firebase project **`nye-restroom`**, registered as a web app. Firebase Authentication for Google Sign-in; Cloud Firestore for private saves/notes, ratings, visitor-submitted locations, and private/opt-in public passcode reports. Security rules separate public reads from account-owned writes. |
| Waitlist and email | `/api/waitlist`; persistent SQLite on the VPS, separate from Firestore accounts. Cloudflare Email Sending sends fixed receipts from a durable outbox. Signup deduplication, bounded retries, rate limits, and server-only credentials protect this flow. |
| Hosting | [Team domain](https://nyc.imfinethanku.me/) on the team's VPS using Caddy HTTPS and a nonroot Node service. |
| Analytics | Google Analytics **`G-YJG2N05KY9`**, manual sanitized pageviews, lowercase UTM attribution, and confirmed-signup `generate_lead`. |
| Coding agent | Codex, with separate planning, implementation, and independent review responsibilities. Relevant Firebase skills guide backend changes. |
| Feature process | Brief → plan → independent review → build → verify → ship → record lessons, documented in [the product process](https://github.com/imnotmomo/nyc-restroom/blob/main/docs/feature_development.md). |

For changes, record the user problem, observable acceptance criteria, owned files, review findings, actual checks, and delivery status in `docs/features/`. Use the repository's supported type check, tests, and production build. Rehearse relevant phone/browser flows; use disposable emulators for write tests rather than manufacturing public reports. Confirm the deployed result before calling it shipped.

## Responsibilities through the demo

This is the proposed working allocation for the remaining sprint, not a claim about who authored previous code.

| Teammate | Responsibility | Deliverable |
| --- | --- | --- |
| **Zheli Chen** | Facebook and X outreach, blog publication, engineering integration, hosting, Firebase, and Analytics. | Placement permalinks and accurate availability records, a published blog URL, a stable deployed build, verified core flow, and an accurate measurement export for the demo. |
| **Ciarrah Wang** | Blog fact checks and mobile lookup rehearsal. | Reviewed conditions language, a checked landing-page-to-demo flow, and recorded usability problems. |
| **Ziying Zhou** | Listing/source clarity and outreach copy review. | Review of entry/route wording, source dates, and unknowns, plus notes on relevant reader feedback. |
| **Siqi Jiang** | Demo testing and backup preparation. | Recorded device/browser problems, a checked demo rehearsal, and backup screenshots. |
| **Zhenni Yue** | Blog editorial review, user flow rehearsal, and demo narration. | Editorial notes, a five-minute script, and a short list of observed usability problems. |

## Five-minute demo

| Time | Show |
| --- | --- |
| **0:00–0:35** | The problem and the four live marketing pages. State that each tests a different benefit. |
| **0:35–1:55** | Open the public demo. Identify the Target sample, drag across the stars, try filters and saving, and compare the public code with the owned private code. Show that only the owner can edit visibility and that reload resets sample actions. |
| **1:55–3:10** | Switch to the real finder with team access prepared. Search, zoom a cluster, explain source/date/unknowns, and open directions. With an authorized team Google account, show private saves and the nearby-address/code options in Log a restroom. Do not create fictional public places, ratings, or code checks; submit only a real observation with approval. |
| **3:10–4:15** | Show actual outreach posts if published, their UTM destinations, and observed Analytics results. If traffic is small or absent, say so. Do not present setup traffic as adoption. |
| **4:15–5:00** | State the data limits, the next missing evidence, and the one improvement we would prioritize from real feedback. |

Before October 23, rehearse public demo/reset, finder unlock/lock, Google Sign-in with a real team account, location allowed and denied on a phone, external directions, private save/readback, and public-report loading after unlocking. Check nearby address selection and owner-only passcode controls without manufacturing venue observations. Keep screenshots ready for a network interruption and label them as a backup. A saved screenshot does not establish that an unfinished interaction works.

## Evidence and next decision

The product repository contains the current [city snapshot and provenance](https://github.com/imnotmomo/nyc-restroom/tree/main/data/nyc-restrooms), [Analytics release evidence](https://github.com/imnotmomo/nyc-restroom/blob/main/docs/features/google-analytics.md), [public demo and finder access checks](https://github.com/imnotmomo/nyc-restroom/blob/main/docs/features/protected-finder-demo.md), [direct-star rating checks](https://github.com/imnotmomo/nyc-restroom/blob/main/docs/features/star-drag.md), [new-location checks](https://github.com/imnotmomo/nyc-restroom/blob/main/docs/features/log-restroom.md), [passcode checks](https://github.com/imnotmomo/nyc-restroom/blob/main/docs/features/restroom-passcodes.md), and [confirmation email checks](https://github.com/imnotmomo/nyc-restroom/blob/main/docs/features/waitlist-confirmations.md). These describe implementation verification, not customer demand.

For the next decision, we will compare actual channel sessions, distinct waitlist emails, and concrete questions from readers. If people care most about a missing entry or route detail, the next slice should collect and display that detail for a manageable set of real places.
