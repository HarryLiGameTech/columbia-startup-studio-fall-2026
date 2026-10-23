# CallIt MVP

## What we are building

CallIt is for friend groups that want a shared record of who predicted what and who called it. A manager creates a private group and shares an invitation. Members join, answer a call before its closing time, and return to see the recorded result.

Each call has 2 to 6 answer choices, a closing time, and a clear condition for the result. Members answer once. After closing, the manager checks the result and records it. The group can revisit the terms, answers, and result without searching old messages.

## MVP features

- Private groups with invitations and manager/member roles.
- Calls with clear terms, 2 to 6 choices, a closing time, and an optional result source.
- One answer per member, hidden from other members until closing.
- Manager-recorded results and a record of who answered correctly.
- Comments and a history of resolved calls.

## What comes later

- Points and broader scoring.
- A process for reviewing disputed results.
- Public groups, automated reminders, reactions, and a mobile app.
- More ways to change or correct a call after publication.

## Cut and manual steps

The pilot does not include points, dispute voting, public groups, automated reminders, payment processing, or a native mobile app. Published terms and submitted answers stay fixed. A call with incorrect terms must be cancelled and posted again.

For an initial pilot, a group manager checks the agreed result source and enters the outcome manually. The group can use its existing chat for reminders and feedback. These steps let the team learn from real groups before building more automation.

## Stack, services, and cost

- **Application:** Next.js with Supabase authentication and Postgres.
- **Marketing pages:** Vite with a shared Node.js waitlist service and Google Analytics.
- **Coding agent:** Codex and Claude Code.
- **Hosting:** DigitalOcean with Caddy and HTTPS.
- **Current cost estimate:** DigitalOcean is listed at USD 6 per month. The domain purchase was USD 8.20. Supabase, Resend, Google Analytics, GitHub, and Pexels are on free plans or have no cost recorded. Prices and free-plan limits can change. Founder time is not included.

## Roles

| Owner | Responsibility |
|---|---|
| Yuval Gerber | Application, landing pages, database integration, hosting, and analytics. |
| Elad Tisch | Product decisions, presentation, and demo. |
| Aviv Pinto | Marketing, product identity, and interface design with Yuval. |
| Zhangcheng (Charles) | Integration, requirements checks, homework submission, and project budget. |
| Shiyu Zhou (Emily) | Weekly traffic, communities, posts, and pilot feedback. |

## How we will know it works

Measure account creations and whether members answer a call, return for its result, and start another call. The pilot will show whether groups use the shared record more than once. The course assignment does not set a numeric pass threshold.

## Risks and open questions

- A small pilot may not show whether groups will keep using CallIt.
- Managers must agree on the result source and meaning of each call before members answer.
- The team must decide how to handle disputed results and later changes to terms.
- Analytics and a final walkthrough should be checked on the live experience before the pilot.

## References

- [Class 5 slides](https://github.com/kenxle/columbia-startup-studio-fall-2026/blob/main/classes/20261009_c5w5_fri_demand-gen-and-landing-pages/class-5-slides.pdf): MVP scope, document requirements, and demo.
- [Brand position](https://github.com/Yuval-Gerber/CallIt/blob/codex/recover-landing-pages/landing-pages/docs/brand_position.md): audience, core promise, and value to test.
- [Product rules](https://github.com/Yuval-Gerber/CallIt/blob/codex/recover-landing-pages/web-app/docs/product-rules.md): current behavior and future decisions.
