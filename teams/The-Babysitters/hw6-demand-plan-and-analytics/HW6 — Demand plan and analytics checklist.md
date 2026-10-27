# Homework 6 — Demand Plan and Analytics

## Deadline and submission

**Due 2026-10-23 at 13:10 America/New_York.** CourseWorks lists 0 points and no Canvas submission.

Open **one pull request per team** to [the class repository](https://github.com/kenxle/columbia-startup-studio-fall-2026), putting the document in `teams/The-Babysitters/hw6-demand-plan-and-analytics/demand_strategy.md`. The current assignment says the PR itself is the submission; nothing is submitted on CourseWorks.

## Part 1 — semester demand strategy

- [ ] Name one or two traffic owners **for every remaining week**. Ownership may rotate.
- [ ] Identify target communities on Reddit, Facebook, or other forums and estimate how many relevant people may see posts.
- [ ] Set a social posting schedule and add a link to each post.
- [ ] Set a blog schedule through the end of the semester, brainstorm topics, and assign some to particular weeks.
- [ ] Define the email strategy: newsletters, feature releases, and/or lifecycle messages triggered by signup timing or feature use.
- [ ] Estimate traffic and signups using a **signup rate of 1% or less**. Show how the plan could reach 100 signups during the remaining semester.

The strategy can evolve as results arrive. At 1% conversion, 100 signups needs about 10,000 visitors; lower conversion requires more. This is arithmetic for planning, not a measured product result.

Class 6 slide 45's four article types: problem-focused, founder journey, solution explainer, and tactical advice. The slides also encourage first posts, a planned or published blog post, and automated welcome email; distinguish that guidance from the explicit document requirements.

## Part 2 — Google Analytics on every page

- [x] Create a Google Analytics account and property with the correct name, timezone, and currency — Claude Daycare Marketing, New York, USD; configured October 22.
- [x] Add a Web data stream — Claude Daycare website; public measurement ID `G-FHERCC17DW`.
- [ ] Install the Google tag through direct tagging, Tag Manager, or the website builder.
- [ ] Verify the tag is on the homepage and **every landing page**.
- [ ] Send successful signups to a thank-you page, fire a signup event there, and mark it a **key event** in GA.
- [ ] Put lowercase UTMs on every posted link, distinguishing source, medium, campaign, and post. UTM values are case-sensitive.
- [ ] Verify visits/events in GA Realtime; normal reports can take 24–48 hours.
- [ ] Save the PR URL and evidence of verification. Neither was checked in this course-material review.

The instructor says agents will inspect public pages for analytics tags.

## Optional learning and source conflict

**Analytics Academy 101 and 102 are explicitly optional and not part of HW 6** on the current assignment page. Class 6 slides 67, 70, and 72 say to start the courses and include a note; the assignment-specific optional label is the clearest current requirement.

Older schedules called HW 6 the working MVP. **The current HW 6 is Demand Plan and Analytics; the working product is required for the separate October 23 midterm.** Class 6 slide 72's combined folder/Canvas-link instruction conflicts with the separate numbered folders and PR-only instructions on the live assignment pages.

## My work and submission

Initial course-material review did not verify the demand strategy, analytics, or team PR. The following later October 22 update supersedes the analytics-setup part of that status.

GA4 is configured with `sign_up` as the key event and event-scoped page/proposition dimensions. The manual tag runs on all four local acquisition pages; collection returned HTTP 204 and the routes appeared in GA Realtime. A controlled lowercase UTM campaign was verified with clean page location and an empty referrer. A separate EU PostHog project received collection requests with HTTP 200. Its dashboard visibility and real server conversions remain unverified. Setup details and evidence are in [the implementation handoff](https://drive.google.com/file/d/1AWqRfouBqm4M8LpdXen8zWuSh5fTb70x/view?usp=drivesdk). No server secret or project token is stored in this note.

The implementation counts server `sign_up` only after a new interest row is inserted, followed by receipt-verified thank-you confirmation. A direct thank-you URL cannot count as a signup. Local browser capture/readback passed on all four forms using fixture addresses, with Chrome DNT respected; this did not establish conversion delivery in vendor reports. Public tags, public capture, deployed conversions, real campaign links, the demand-strategy document, and the HW6 class PR remain open.

Almog confirmed Mansi as traffic/distribution owner. The broader proposal assigns her the demand-plan document, evidence coordination, and HW6 class PR, using the analytics work already completed. See [the team delivery plan](https://drive.google.com/file/d/1zh4ckdIVsiBurY24ZI9Fi1UKTJQFJR6q/view?usp=drivesdk). No class-repository HW6 PR was found during the October 22 GitHub check; none was created here.


---
Source snapshot: School/Columbia/AI Startup Studio/Assignments/Homework 6 — Demand Plan and Analytics.md · copied 2026-10-22. The vault source is unchanged.
