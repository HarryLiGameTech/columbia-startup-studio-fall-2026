# CallIt MVP

## Core flow: user, action, value

CallIt is for existing friend groups that want a shared record of who predicted what and who called it. The core promise is: "Being right is better when your group remembers."

1. A manager creates a private group and shares its invitation link.
2. Members create an account or sign in and join the group.
3. The manager posts a call with 2-6 answer options, a closing time, and a clear winning condition.
4. Each member answers once before closing. The terms and answers stay fixed.
5. After closing, the manager checks the outcome and records the result.
6. Members return to see the result and the group's correct-answer scoreboard.

The value is one shared record of the terms, answers, and result. Members can revisit the outcome without reconstructing earlier chat messages. The pilot will test whether members answer, return for the result, and want to make another call.

## Cut: what we are not building

The core pilot uses private groups, fixed calls, one answer per member, manager-recorded results, and a correct-answer scoreboard. It excludes a points economy, dispute voting, public groups, reactions, automated reminders, payment processing, and a native mobile app. The manager's recorded result is final in this version. A call with incorrect terms must be cancelled and posted again.

The current app also has optional room token values and a settlement ledger. Members settle outside CallIt through Venmo, Apple Cash, or in person. CallIt records amounts and payment status; it does not transfer money. These features are outside the core pilot demonstration.

## Faked: our Wizard of Oz parts

For the first pilot, the team will recruit a group and help members join. The manager will check the agreed result source and enter the outcome manually. The team will use the group's existing chat for reminders and feedback rather than build an automated notification system. These are planned manual steps; pilot results are not yet established.

## Stack: framework, agent, and hosting

- **Application:** Next.js with Supabase authentication and Postgres. Database access rules protect private group data.
- **Marketing pages:** Vite, with a shared Node.js waitlist service and Google Analytics.
- **Coding agents:** Codex and Claude Code, coordinated through a custom Git-based multi-agent workflow. Shared instructions, a bulletin board, and a sync agent support handoffs and regular synchronization.
- **Hosting:** A DigitalOcean server runs the application and marketing pages behind Caddy with HTTPS. The server deploys from the team's GitHub base branch.

## Roles: who builds what, who owns traffic

Current ownership follows the team's October 17 role decision.

| Owner | Responsibility |
| --- | --- |
| Yuval Gerber | Development: app, landing pages, database integration, hosting and analytics. |
| Elad Tisch | Product decisions, presentation and live demo rehearsal. |
| Aviv Pinto | Marketing with Emily, coin identity and UI design with Yuval. |
| Zhangcheng Kang (Charles) | Integration, requirements checks, homework submission and project budget. |
| Shiyu Zhou (Emily) | Weekly traffic, communities, publication evidence and pilot feedback. |

## Delivery and verification

HW5 defines the MVP. The midterm MVP presentation is on October 23, 2026, at 1:10 PM America/New_York. HW6 is Demand Plan and Analytics. Use a call with a short closing time so the demo can show the result and scoreboard.

The code is present. On October 16, Elad reported that all five backend migrations were applied and hosted rollback checks passed. Yuval reported an older deployed walkthrough passing 13/13 checks on October 17. The final interface change (team PR #22) and a timed rehearsal of that deployed revision remain pending as of October 21. Verify signup, invitation acceptance, answering, result recording, and scoreboard updates on the final build before claiming pilot readiness. The rubric allows 7.5 minutes for presenting and 7.5 minutes for questions; every member presents.

## References

- [Class 5 slides](https://github.com/kenxle/columbia-startup-studio-fall-2026/blob/main/classes/20261009_c5w5_fri_demand-gen-and-landing-pages/class-5-slides.pdf), pages 40 and 89-91: MVP scope, document requirements, and demo deadline.
- [HW4 brand position](../hw4-synthesis-brand-position/brand_position.md): audience, core promise, and value to test.
