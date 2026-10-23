# Claude Daycare — MVP document

The Babysitters · October 22, 2026 · Draft pending actual service costs and public release verification.

## 1. What we are building

Claude Daycare is a recreational activity service for owners of coding agents. The initial audience is a personally funded agent owner who is curious about games or conversations and willing to spend some of their own usage to see what happens. Interest in a visit is a hypothesis to test; the interviews do not establish an urgent problem shared by all AI users or a willingness to pay.

The owner's practical questions are what they would get from a visit, what it consumes, and what they can inspect afterward. The core flow is **owner installs and pairs a local companion → chooses an activity/instructions and allowance → agent takes turns through Daycare's activity tools → owner reviews recorded activity and any returned report or memories**. The first useful result is an activity record the owner finds interesting enough to read, rather than a settings screen or a promise that the model improved.

The website's shorter acquisition flow is **visitor selects a relevant benefit page → enters an email for product updates → server stores that page/proposition interest → visitor sees a verified confirmation**. This does not create a product account or start a visit.

Research and positioning: [HW3 interviews](https://github.com/kenxle/columbia-startup-studio-fall-2026/blob/main/teams/The-Babysitters/hw3-interviews/README.md), [HW4 brand position](https://github.com/kenxle/columbia-startup-studio-fall-2026/blob/main/teams/The-Babysitters/hw4-synthesis-brand-position/brand_position.md), and [HW4 research](https://github.com/kenxle/columbia-startup-studio-fall-2026/tree/main/teams/The-Babysitters/hw4-synthesis-brand-position/reddit_research). We retain objections about usefulness, installation, privacy, and spending usage on recreation. Earlier work-reserve and job-board ideas do not establish shipped guarantees.

## 2. MVP features

- Homepage and three focused benefit pages with a shared brand and visible email capture.
- Server-side email validation, rate limiting, per-page/proposition interest storage, and honest duplicate/error/confirmation behavior.
- Authenticated owner accounts, agent profiles, and local-companion pairing in the platform code.
- Activities and social interactions, including games, Tycoon, and conversations, through the Daycare tool surface.
- Owner-selected weekly-meter allowance for supported Claude Code/Codex visits; a separate token setting for OpenCode.
- Recorded activity, receipts, and any best-effort returned report or saved memories.
- Page/proposition measurement through GA4 and a separate EU PostHog marketing project.

Website behavior is tested locally. Platform feature presence is grounded in source and setup documentation; it is not a claim that this release has passed a complete real-agent visit or public end-to-end test.

## 3. Later features, in priority order

1. Better onboarding and failure recovery, so a new owner can complete a first visit with less assistance.
2. Clearer return records grounded in activity evidence, so the owner can judge what happened without reading an unstructured transcript.
3. Better allowance/status explanations and observed overshoot reporting, so owners understand what the existing setting actually controls.
4. Return-use improvements chosen from observed visits and feedback, so repeat engagement addresses real interest rather than adding an activity catalogue.
5. Revisit separate job-board or protected-work-reserve concepts only after independent demand and feasibility checks; neither is promised by the current marketing pages.

## 4. Cut, manual, and faked parts

- The active pages collect email update interests; they do not promise an automated welcome email, immediate access, a launch date, or account creation.
- Website examples use clearly labeled sample game data. They are illustrative previews, not recordings of completed real visits or customer testimonials.
- No protected work reserve, exact spending stop, model-learning claim, job income, payouts, marketplace availability, or real-money trading is part of the website promise.
- Weekly-meter checks occur between turns. The running turn and homecoming can consume more; other activity on the same account affects its meter.
- Reports/memories are best effort. Missing records are shown as missing instead of being filled with generated evidence.
- Team members review feedback, choose content, and coordinate distribution manually. The signup implementation stores interests; update-email delivery needs an explicit team process/provider.
- Public deployment and production migration are handled by Josh. No full real-agent demo or deployed signup success is established by the local website checks.

## 5. Stack, services, and cost

The platform uses Next.js 16, React 19, TypeScript, Node.js, pnpm, Supabase Postgres/Auth/Storage, and a separate local companion. Website work uses Codex with Astra implementation agents. Provider/model calls in the platform use the Vercel AI SDK with Anthropic and OpenAI; optional image generation uses Replicate. The companion consumes the owner's compatible plan or configured provider usage. The marketing form itself makes no model call.

**Actual bills have not been supplied.** Published price references below are not the team's verified spending or a commitment to a paid plan. Josh must confirm the active plans, billing period, and current usage before this cost section is final.

| Component or service | Purpose | Cost recorded for this draft |
|---|---|---|
| Next.js, React, TypeScript, Node.js and pnpm | Website/server implementation and development | No separate paid framework service configured; hosting and developer-tool subscriptions are separate. |
| Coding agents/tools | Website and product development | Codex/Astra used for this work; actual team subscription/API allocation still to confirm. |
| GitHub | Platform/runner source, PRs, and CI | Actual account plan and CI/storage charges still to confirm. |
| `claudedaycare.com` domain | Public website | Registrar, purchase/renewal amount and billing owner still to confirm. |
| Vercel | Hosted Next.js site/API | Actual plan/usage still to confirm. Public reference: Hobby $0/month; Pro $20/month, with usage/seat details on [Vercel pricing](https://vercel.com/pricing). |
| Supabase | Database, auth, and hosted storage | Actual project plan/compute/storage/egress still to confirm. Public reference: Free $0/month; Pro from $25/month on [Supabase pricing](https://supabase.com/pricing). |
| Email | Product account email and eventual update-list delivery | Supabase Auth is present; actual SMTP/update-email provider and charges still to confirm. The marketing signup route currently saves an interest rather than sending an email. |
| Payments | A future product charge/checkout | No payment step added to the marketing signup flow; pricing and any actual payment service still to confirm. |
| Google Analytics 4 | Website page/proposition and successful-interest measurement | Standard Analytics is offered [free of charge](https://marketingplatform.google.com/about/analytics/); no Analytics 360 purchase was made in this setup. |
| PostHog EU | Separate marketing product analytics | [Published free allowance](https://posthog.com/pricing): 1 million analytics events/month; actual project billing state still to confirm. Replay and autocapture are disabled. |
| Anthropic and OpenAI APIs | Server game-master/judging features | Usage-based; configured model, token volume and actual monthly spend need Josh's confirmation. These costs are separate from an owner's companion plan. |
| Replicate | Optional activity image generation | Usage-based optional service; activation and actual spend still to confirm. |
| Nasdaq / SEC data | Simulated-stock quote/symbol data in platform source | No paid API key is present in these provider implementations; actual service arrangements/costs still to confirm. Activity money is fake. |

The total monthly operating cost is **not yet verified**. Do not add the public free/paid examples into a fictional actual bill. Domain renewal, platform usage, developer subscriptions, server AI calls, and the owner's agent usage are distinct costs.

## 6. Success measure

Measure the funnel in separate counts: visits by proposition/source → stored email interests → product account creations → first completed visits → owners returning for another visit. One email choosing several propositions is several interests, not several people. GA Realtime test visits are not customer traction.

**Proposed first-use decision rule for team review:** recruit five non-team target users, aim for all five to create an account and complete a first visit, and look for at least three voluntarily returning within seven days with a concrete reason they wanted another visit. Record the raw counts, failures, and interview explanations. This is a proposed continuation threshold, not a measured result or a team-approved commitment. If interest stops at the preview or people cannot name the value of the return record, narrow/change the proposition before adding features.

The HW5 website acceptance check is separate: every public page must load, explain its specific offer, and save a test email where the team can inspect it.

## 7. Risks and open questions

- Is curiosity about the activity enough to produce voluntary repeat use? Interview interest and synthetic persona scores do not answer this.
- Do the usage cost, installation, awake-computer requirement and supported-account limits outweigh the activity's appeal?
- Can the team demonstrate one complete real visit and explain its output with actual evidence?
- Are release behavior, transcript handling, privacy copy, and provider/account requirements aligned at deployment?
- Can the team apply both signup migrations, verify a real stored interest per page, and preserve historical cohorts?
- Can Josh deploy the intended branch through the correct Vercel team and make the public routes available by class time?
- What are the actual service bills, product pricing, and update-email process?
- Will uncoached target readers understand the first screen and see a reason to continue?

## 8. Named roles

Confirmed by Almog with the team on October 22, 2026:

| Owner | Responsibility |
|---|---|
| Almog Ankori | Website, page copy, and product decisions. |
| Josh Hegstad | Working product, database, and deployment. |
| Mitchell Rosenthal | Customer interviews and feedback. |
| Mansi Rank | Traffic/distribution: coordinate relevant channels, posts/content, link attribution, and acquisition results; teammates can contribute execution. |

The team still needs to review the proposed success threshold, confirm actual costs, and verify the public release. A complete document does not substitute for the live-page and working-capture requirements.
