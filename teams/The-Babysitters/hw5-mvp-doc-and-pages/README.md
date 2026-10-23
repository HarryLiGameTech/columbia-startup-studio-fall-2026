# The Babysitters — HW5: Claude Daycare

Submitted October 23, 2026.

**Release status:** the redesigned homepage and three benefit pages are deployed; all four URLs below returned HTTP 200 signed out on October 23, 2026.

## Pages, audiences, and propositions

All four pages offer **Get Daycare updates**: an email interest list, not an account creation, access entitlement, or visit. A successful save leads to a receipt-verified thank-you page.

| Page | Public URL | Specific reader | Benefit being tested |
|---|---|---|---|
| Homepage | https://claudedaycare.com/ | A coding-agent owner encountering Daycare for the first time | Understand a recreational visit and inspect the activity record that comes back. |
| Spare usage | https://claudedaycare.com/for/spare-usage | A personally funded coding-agent owner with usage they are willing to spend on an experiment | Explore games and conversations for curiosity, using their own plan. Leaving usage unused is also an option. |
| Visit records | https://claudedaycare.com/for/see-what-happened | An agent owner who wants to inspect an activity afterward rather than trust its narrative alone | Read the account alongside supporting activity and any returned report or memories, including explicit missing-data states. |
| Usage controls | https://claudedaycare.com/for/set-the-limit | An agent owner who wants to choose how much usage to offer before trying a visit | Understand allowance setup, what the meter measures, and between-turn stopping and homecoming limits. |

These are research-informed message hypotheses, not validated customer segments. The retired `/for/post-a-job` concept does not count toward the three active landing pages.

## Product and supporting work

- [MVP document](mvp_doc.md).
- [Website and platform repository](https://github.com/hegstadjosh/claude-daycare-platform) — private; instructor access may need to be granted by its owner.
- [Public local-companion source](https://github.com/Voices-of-History/claude-daycare).
- [HW3 interviews](https://github.com/kenxle/columbia-startup-studio-fall-2026/blob/main/teams/The-Babysitters/hw3-interviews/README.md).
- [HW4 brand position](https://github.com/kenxle/columbia-startup-studio-fall-2026/blob/main/teams/The-Babysitters/hw4-synthesis-brand-position/brand_position.md) and [style guide](https://github.com/kenxle/columbia-startup-studio-fall-2026/blob/main/teams/The-Babysitters/hw4-synthesis-brand-position/style_guide.md).

The redesign keeps the selected Capped bars lockup, sentence-case copy, restrained imagery, and Lucide controls. It introduces a coordinated paper/cobalt treatment with Newsreader and IBM Plex Sans. This is a redesign revision of the two previously unselected dark style directions, not a claim that the old guide already prescribed these colors. Product illustrations visibly use sample data; no customer testimonial or completed visit is invented.

## HW5 completion checks

- [x] Implement one homepage and three distinct current-product benefit pages.
- [x] Give each page a clearly explained email-update action.
- [x] Apply the selected logo and a consistent visual system across the pages.
- [x] Verify layouts at desktop, 390px, and 320px and check invalid/save-error/direct-thanks behavior locally.
- [x] Prepare the eight-section MVP document and this page/audience/URL index.
- [ ] Confirm actual service costs in the MVP document with Josh.
- [x] Complete real database save/readback checks for all four local forms: each stored the expected source/proposition; a duplicate controls submission preserved one row. All 19 signup pgTAP assertions passed in an isolated local Supabase stack.
- [x] Merge and deploy the intended release.
- [ ] Verify all four public URLs, each saved test signup, duplicate handling, and truthful confirmation after deployment.
- [ ] Confirm the purchased-domain ownership/renewal details with Josh.
- [x] Open the team HW5 PR in the class repository.

HW5 uses one team PR as the submission. Its live assignment page does not require an additional CourseWorks submission. A PR in the product repository is implementation work; it does not substitute for the class-repository hand-in.
