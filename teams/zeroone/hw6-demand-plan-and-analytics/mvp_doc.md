# CallIt MVP

## Product and core flow

CallIt is for friend groups that want a shared record of who predicted what and who called it. A manager creates a private group and shares an invitation. Members join, answer a call before it closes, and return to see the recorded result.

Each call has 2 to 6 answer choices, a closing time, and a clear condition for the result. Members answer once. The manager checks the result and records it after closing. The group can revisit the terms, answers, and result.

## Current features

- Private groups with invitations and manager/member roles.
- Calls with written terms, 2 to 6 choices, a closing time, and an optional result source.
- One answer per member, hidden from other members until closing.
- Manager-recorded results, comments, and a history of resolved calls.

## Later features

Points, a process for reviewing disputed results, public groups, automated reminders, reactions, and a native mobile app are outside the current core pilot.

## Manual steps

For an initial pilot, the manager checks the agreed result source and enters the outcome manually. The group can use its existing chat for reminders and feedback.

## Stack and cost

- **Application:** Next.js with Supabase authentication and Postgres.
- **Marketing pages:** Vite with a shared Node.js waitlist service and Google Analytics.
- **Coding agents:** Codex and Claude Code.
- **Hosting:** DigitalOcean with Caddy and HTTPS.

## Roles

| Owner | Responsibility |
|---|---|
| Yuval Gerber | Application, landing pages, database integration, hosting, and analytics. |
| Elad Tisch | Product decisions, presentation, and demo. |
| Aviv Pinto | Marketing, product identity, and interface design with Yuval. |
| Zhangcheng (Charles) | Integration, requirements checks, homework submission, and project budget. |
| Shiyu Zhou (Emily) | Weekly traffic, communities, posts, and pilot feedback. |

## Success measure

Measure account creations and whether members answer a call, return for its result, and start another call. The course assignment does not define a numeric pass threshold.

## Risks

Small pilot groups may not show whether groups will keep using CallIt. Managers must agree on the result source and meaning of each call before members answer. The team will use pilot feedback to guide future product decisions.
