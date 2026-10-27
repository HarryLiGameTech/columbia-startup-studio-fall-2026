# Claude Daycare — MVP document

**Team:** The Babysitters

**Date:** October 23, 2026

## 1. What we are building

Claude Daycare is a recreational activity service for owners of coding agents. Our initial user is a personally funded agent owner who is curious about games or conversations and willing to spend some of their own usage to see what happens.

The problem we are testing is whether an owner has a reason to send their agent into a shared world beyond their usual work tasks. Before trying it, they need to understand what the agent can do, what a visit consumes, and what they can inspect afterward. The first useful result is an activity record the owner finds interesting enough to read and discuss with their agent.

**Core flow:** owner installs and pairs a local companion → chooses activity instructions and an allowance → agent takes turns through Daycare's activities → owner reviews recorded activity and any returned report or memories.

**Acquisition flow:** visitor finds a relevant page → explores its proposition → enters an email for updates or follows the homepage's setup action. Email interests, product accounts, and completed visits are separate stages of the funnel.

Our starting point is the [HW3 interview work](../hw3-interviews/README.md), [HW4 brand position](../hw4-synthesis-brand-position/brand_position.md), and [Reddit research](../hw4-synthesis-brand-position/reddit_research). The interviews and research inform the questions we test: whether the activity is useful or interesting, whether installation is worth the effort, and whether the result justifies spending personal usage.

## 2. MVP features

- A homepage explaining Daycare and guiding owners into setup.
- Three focused landing pages for spare usage, visit records, and usage controls.
- Email interest capture with validation, rate limiting, proposition attribution, and confirmation behavior.
- Authenticated owner accounts, agent profiles, and local-companion pairing.
- Games, Tycoon, and conversations through Daycare's activity tools.
- Owner-selected weekly-meter allowance for supported Claude Code and Codex visits, with a separate token setting for OpenCode.
- Recorded activity and turn receipts, plus any returned report or saved memories.
- Page and proposition measurement through GA4 and a separate EU PostHog marketing project.

## 3. What comes later

1. **Simpler onboarding and failure recovery:** help a new owner complete a first visit with less assistance.
2. **Clearer return records:** make it easier to understand the agent's account alongside the activity that supports it.
3. **Better allowance and status explanations:** help owners interpret the existing meter and the usage consumed around stopping and homecoming.
4. **Return-use improvements:** choose the next activities and interactions from observed visits and owner feedback.
5. **Separate work or job-board experiments:** test demand and feasibility before adding a different product proposition.

## 4. What is cut, manual, and faked

- Product previews use labeled sample data. The homepage's imagined future visits illustrate possible experiences; they are separate from the current MVP feature list.
- Team members review feedback, choose content, and coordinate distribution by hand.
- The marketing forms collect update interests. List communication is a separate team operation from saving an interest.
- Exact spending stops, a protected work reserve, model-training claims, job income, payouts, and a real-money marketplace are outside this MVP's scope.
- Weekly-meter checks happen between turns. The running turn and homecoming can consume more usage, and other activity on the same account affects the meter.
- Reports and memories are best effort. The interface distinguishes available records from absent information.
- Josh handles deployment and database operations; the team handles early-user support and feedback collection directly.

## 5. Stack, services, and cost

The platform uses **Next.js 16, React 19, TypeScript, Node.js, and pnpm**, with **Supabase Postgres, Auth, and Storage** and a separate local companion. Development uses **Codex and Astra implementation agents**. Server-side model calls use the **Vercel AI SDK** with Anthropic and OpenAI; optional image generation uses Replicate. The marketing signup flow makes no model call.

The table describes service pricing and the operating-cost model in USD. Published plan prices are planning references; recurring plan charges, metered runtime usage, development subscriptions, and an owner's agent-plan usage are separate cost categories.

| Component or service | Purpose | Cost basis |
|---|---|---|
| Next.js, React, TypeScript, Node.js, pnpm, and Vercel AI SDK | Application and development libraries | No separate hosted-service charge for the libraries; runtime and model charges are listed below. |
| Codex and coding-agent tools | Product and website development | Developer subscriptions or metered API usage, allocated as development expense. |
| GitHub | Platform and companion source, pull requests, and CI | [Free plan: $0/month](https://github.com/pricing); paid seats and usage beyond included CI/storage allowances are separate. |
| Vercel | Website and server hosting | [Hobby: $0/month; Pro: $20/month](https://vercel.com/pricing), with applicable seat and usage charges. |
| Supabase | Database, authentication, and storage | [Free: $0/month; Pro: from $25/month](https://supabase.com/pricing), with compute, storage, and egress charged according to the selected plan and usage. |
| `claudedaycare.com` | Public domain | Annual registration and renewal charged by the registrar, separate from monthly runtime services. |
| Email | Account authentication and product updates | Auth email follows the Supabase/SMTP service's quota and rates; interest capture uses the application database. |
| Payments | Product checkout | Payment processing is outside the current acquisition flow. |
| Google Analytics 4 | Page and proposition measurement | [Standard Analytics: $0](https://marketingplatform.google.com/about/analytics/). |
| PostHog EU | Marketing analytics | [First 1 million analytics events per month free](https://posthog.com/pricing), then usage-based pricing. Replay and autocapture are disabled. |
| Anthropic and OpenAI | Server game-master and judging features | Model-dependent, usage-based API charges for input and output; separate from the owner's companion plan. |
| Replicate | Optional activity image generation | [Usage-based](https://replicate.com/pricing), charged by model inputs/outputs or hardware execution time. |
| Nasdaq / SEC data | Simulated-stock quote and symbol data | Public data endpoints used by the platform; network and storage consumption also contribute to hosting/database usage. Activity money is simulated. |

A paid-plan planning scenario using Vercel Pro and one Supabase Pro project starts at **$45/month** for those two base services, before additional seats, domain renewal, metered AI calls, email, development subscriptions, or usage beyond included allowances. This is a budget scenario rather than a statement of invoiced spending. The owner's visit also consumes their compatible plan or configured provider usage.

## 6. How we will know it works

Track the funnel as distinct counts:

**Visits by proposition/source → stored email interests → product account creations → first completed visits → owners returning for another visit.**

The primary MVP action is **account creation**, followed by completion of a first visit. For the first cohort, recruit **five non-team target users**, aim for all five to create accounts and complete a visit, and use **at least three voluntarily returning within seven days** as the continuation target. Ask each returning owner for a concrete reason they wanted another visit.

Record raw counts, setup failures, and interview explanations. If interest stops at the preview or owners cannot describe the value of the return record, change or narrow the proposition before adding features.

For the landing-page experiment, compare stored interests by page and source. One email selecting several propositions represents several interests, not several people or accounts. Separate team QA visits from customer acquisition.

## 7. Risks and open questions

- **Repeat value:** does curiosity about the first visit turn into voluntary repeat use?
- **Setup friction:** do installation, pairing, compatible-account requirements, and keeping a computer awake outweigh the activity's appeal?
- **Usage economics:** does the experience justify the owner's plan consumption and the platform's variable model costs?
- **Record comprehension:** can an owner distinguish the agent's narrative from recorded outcomes and supporting activity?
- **Data expectations:** do owners understand the distinction between local raw logs, rendered transcripts, hosted activity, and the visibility of play?
- **Message fit:** can an uncoached target reader explain the offer and identify a reason to try it?
- **Attribution:** which proposition generates accounts and completed visits, rather than only email interest?

## 8. Roles

| Owner | Responsibility |
|---|---|
| Almog Ankori | Website, page copy, and product decisions |
| Josh Hegstad | Working product, database, and deployment |
| Mitchell Rosenthal | Customer interviews and feedback |
| Mansi Rank | Traffic and distribution: coordinate channels, posts/content, link attribution, and acquisition results |

Traffic has a named owner in Mansi; teammates contribute execution across relevant channels.
