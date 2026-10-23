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

## MVP features

- Private groups with invitation links and manager/member roles.
- Calls with 2–6 answers, a closing time, written terms, and an optional result source.
- One answer per member, with picks hidden from other members until closing.
- Manager-recorded results after closing, followed by a record of who called it.
- Comments and a group history for resolved calls.

## What comes later

The following items remain open or outside the core pilot. Product order requires Elad's decision.

- Points and a broader scoring system, after the team decides how points work.
- Dispute voting, after the team decides who votes, the threshold, quorum, ties, and timing.
- Agreement-based changes to posted terms; until decided, cancel and repost instead.
- Public groups; groups remain private in the current version.
- Reactions beyond comments, and self-service account deletion and retention controls.
- Automated reminders and a native mobile application.

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

### Services and current cost evidence

- DigitalOcean hosting: USD 6 per month in the current plan. The actual invoice is pending.
- Domain: USD 8.20 purchase reported for `call-it.app`; renewal cost is pending.
- Supabase, Resend, GA4, GitHub, and Pexels: free plans or no cost reported. Check current quotas before onboarding a pilot.
- The service plan and known spend are tracked in [the project budget](https://github.com/Yuval-Gerber/CallIt/blob/codex/recover-landing-pages/docs/BUDGET.md). Founder time is not priced.

## Roles: who builds what, who owns traffic

The build plan for the October 23 MVP divides the work into five parts. Each owner takes their part through implementation, tests, and fixes, then works with Zhangcheng (Charles) to verify the complete flow.

| Owner | MVP build responsibility | Delivery check |
|---|---|---|
| Yuval Gerber | Calls and results: create and publish a call, enforce the closing time, accept one answer per member, record the result, and show who called it. | A call runs from creation to the correct-answer scoreboard; late and duplicate answers are rejected. |
| Elad Tisch | Accounts and infrastructure: signup, sign-in, confirmation email, database permissions, hosted migrations, DNS, and deployment support. | Members can create accounts and sign in; private data stays protected; hosted configuration supports the pilot. |
| Aviv Pinto | Groups and invitations: create a private group, share and accept invitations, manage membership and roles, and handle leaving or removing a member. | Two accounts can join the same group; manager permissions and access after departure work correctly. |
| Zhangcheng (Charles) | Integration and release verification: connect the account, group, and call flows; run the complete user journey; coordinate fixes; prepare demo data and the five-minute MVP demo. | The deployed app completes signup, joining, answering, result recording, and scoreboard updates in one verified walkthrough. |
| Shiyu Zhou (Emily) | Traffic and pilot operations: recruit a friend group, help members join, run manual reminders, collect feedback, and review visits and signups with Yuval. | A pilot group completes a call; feedback records whether members return for the result and want another call. |
## How we will know it works

Track account creations for recruited pilot groups, then check whether members answer a call, return for its result, and start another call. The course assignment and product rules do not set a pass threshold. Elad must set the threshold before the pilot results are used to decide whether to continue.

## Risks and open questions

- Small pilot groups may not show whether members will keep using the app.
- Managers record results by hand. They must agree on the source and the meaning of each call before members answer.
- The account-creation target for continuing the pilot is open and needs Elad's decision.
- The course expects analytics and a working public experience. GA4 key-event status and a final signed-in browser walkthrough still need evidence.
- Current service invoices, quotas, and the domain's renewal cost need owner read-backs.

## Delivery and verification

HW5 defines the MVP. The midterm MVP presentation is on October 23, 2026, at 1:10 PM America/New_York. HW6 is Demand Plan and Analytics. Use a call with a short closing time so the demo can show the result and scoreboard.

The code is present. On October 16, Elad reported that all five backend migrations were applied and hosted rollback checks passed. Yuval reported an older deployed walkthrough passing 13/13 checks on October 17. The final interface change (team PR #22) and a timed rehearsal of that deployed revision remain pending as of October 21. Verify signup, invitation acceptance, answering, result recording, and scoreboard updates on the final build before claiming pilot readiness. The rubric allows 7.5 minutes for presenting and 7.5 minutes for questions; every member presents.

## References

- [Class 5 slides](https://github.com/kenxle/columbia-startup-studio-fall-2026/blob/main/classes/20261009_c5w5_fri_demand-gen-and-landing-pages/class-5-slides.pdf), pages 40 and 89-91: MVP scope, document requirements, and demo deadline.
- [HW4 brand position](https://github.com/Yuval-Gerber/CallIt/blob/codex/recover-landing-pages/homework/hw-4/brand_position.md): audience, core promise, and value to test.
- [Current product rules](https://github.com/Yuval-Gerber/CallIt/blob/codex/recover-landing-pages/web-app/docs/product-rules.md): implemented rules and deferred features.
