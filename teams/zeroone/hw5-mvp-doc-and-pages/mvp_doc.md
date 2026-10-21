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

The build plan for the October 23 MVP divides the work into five parts. Each owner takes their part through implementation, tests, and fixes, then works with Charles to verify the complete flow.

| Owner | MVP build responsibility | Delivery check |
|---|---|---|
| Yuval Gerber | Calls and results: create and publish a call, enforce the closing time, accept one answer per member, record the result, and show who called it. | A call runs from creation to the correct-answer scoreboard; late and duplicate answers are rejected. |
| Elad Tisch | Accounts and infrastructure: signup, sign-in, confirmation email, database permissions, hosted migrations, DNS, and deployment support. | Members can create accounts and sign in; private data stays protected; hosted configuration supports the pilot. |
| Aviv Pinto | Groups and invitations: create a private group, share and accept invitations, manage membership and roles, and handle leaving or removing a member. | Two accounts can join the same group; manager permissions and access after departure work correctly. |
| Zhangcheng Kang (Charles) | Integration and release verification: connect the account, group, and call flows; run the complete user journey; coordinate fixes; prepare demo data and the five-minute MVP demo. | The deployed app completes signup, joining, answering, result recording, and scoreboard updates in one verified walkthrough. |
| Shiyu Zhou (Emily) | Traffic and pilot operations: recruit a friend group, help members join, run manual reminders, collect feedback, and review visits and signups with Yuval. | A pilot group completes a call; feedback records whether members return for the result and want another call. |

Each owner can use AI agents for implementation, tests, and documentation. The owner reviews the output and verifies their delivery check. One coordinator handles Git changes in each shared checkout.

## Delivery and verification

HW5 defines the MVP. The working MVP and five-minute demo are due for HW6 on October 23, 2026, at 1:10 PM America/New_York. Use a call with a short closing time so the demo can show the result and scoreboard.

The code is present. On October 16, Elad reported that all five backend migrations were applied and hosted rollback checks passed. The full signed-in production walkthrough and confirmation email delivery remain open in the team records. Verify signup, invitation acceptance, answering, result recording, and scoreboard updates before claiming the pilot is ready.

## References

- [Class 5 slides](https://github.com/et2921/CallIt/blob/90e6cfd/homework/hw-5/ref/class-5-slides.pdf), pages 40 and 89-91: MVP scope, document requirements, and demo deadline.
- [HW4 brand position](https://github.com/et2921/CallIt/blob/90e6cfd/homework/hw-4/brand_position.md): audience, core promise, and value to test.
- [Current product rules](https://github.com/et2921/CallIt/blob/90e6cfd/web-app/docs/product-rules.md): implemented rules and deferred features.
