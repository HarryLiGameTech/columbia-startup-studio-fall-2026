# AstraPath demand strategy

**Team Pola, 2026-11-11.** This plan covers the six weeks from now to Demo Day (Friday, December 18). The goal is 100 signups. It will change as we see which posts bring people in. For the product and pages, see the [MVP doc](../hw5-mvp-doc-and-pages/mvp_doc.md) and the [brand position](../hw4-synthesis-brand-position/brand_position.md).

## Traffic owners, by week

| Week | Class that week | Owners | Supporter |
|---|---|---|---|
| 1: Nov 9–15 | Class 10, Nov 13 | Isha Mitra, Sophia Hirao | Jiawen Li (Harry): promo video, bilibili |
| 2: Nov 16–22 | Class 11, Nov 20 | Isha Mitra, Sophia Hirao | Jiawen Li (Harry): promo video, bilibili |
| 3: Nov 23–29 | No class (Thanksgiving) | Isha Mitra, Sophia Hirao | |
| 4: Nov 30–Dec 6 | Class 12, Dec 4 | Isha Mitra, Sophia Hirao | |
| 5: Dec 7–13 | Class 13, Dec 11 | Isha Mitra, Sophia Hirao | |
| 6: Dec 14–18 | Demo Day, Dec 18 | Isha Mitra, Sophia Hirao | |

## Top communities

| Where | Who we reach | Estimated reach before Demo Day |
|---|---|---|
| bilibili | Chinese-speaking viewers, including students who study or will study abroad | 5,000 visitors to our pages (average case) to 20,000+ (best case), the team's estimate |
| TikTok | Students who follow Columbia accounts and campus hashtags | About 250 views per post on average, 1,000 at best (our guess for a new account) |
| Instagram | The same students, through Reels and Stories | About 250 views per post on average, 1,000 at best (our guess for a new account) |

**bilibili notes:**
- Jiawen has a relatively mature, transport-themed bilibili channel with 6,000+ subscribers.
- The promo video goes up during Jiawen's weeks (weeks 1–2) and points to the homepage.
- If the link in the video description isn't clickable, give a short address people can type. A Netlify redirect such as `astrapath-indoornav.netlify.app/bili` can add the UTMs.
- Google Analytics doesn't load in mainland China, so it will undercount bilibili viewers there. We count bilibili signups from the `utm_source` field our waitlist forms already save, not from Google Analytics.
- Our pages are in English only. We should check that they load quickly for viewers in China.

## Social posting schedule

We post about 1.5 times a week, 9 posts in total. Each video goes to both Instagram and TikTok. Captions on both apps aren't clickable, so each post's link goes in the bio (and in an Instagram Story link sticker). We change the bio link with every post. We also need to check that the TikTok account can show a bio link.

| # | Week | Post | Links to | Post links |
|---|---|---|---|---|
| 1 | 1 | Screen recording of a Northwest Corner route, from the front door to the room | Students page | Instagram: to add · TikTok: to add |
| 2 | 1 | Why a step-free route has to name the entrance and the elevator | Step-free page | Instagram: to add · TikTok: to add |
| 3 | 2 | Jiawen's promo video, vertical cut (the same week it goes up on bilibili) | Homepage | Instagram: to add · TikTok: to add |
| 4 | 3 | Finding the door visitors use and where to check in | Visitors page | Instagram: to add · TikTok: to add |
| 5 | 4 | First visits and new buildings: where the minutes go between the front door and the room | Students page | Instagram: to add · TikTok: to add |
| 6 | 4 | Teaser for blog post 2: find your spring classrooms before the first day | Blog post 2 | Instagram: to add · TikTok: to add |
| 7 | 5 | Asking AstraPath a question in any language | Homepage | Instagram: to add · TikTok: to add |
| 8 | 5 | How we map Northwest Corner by hand | Homepage | Instagram: to add · TikTok: to add |
| 9 | 6 | Demo Day | Homepage | Instagram: to add · TikTok: to add |

Thanksgiving week gets one post, because many students are away.

**UTMs.** Every link we post uses lowercase UTMs:

```
https://astrapath-indoornav.netlify.app/students/?utm_source=instagram&utm_medium=social&utm_campaign=pola_astrapath_nov2026&utm_content=post1
```

- `utm_source`: `instagram`, `tiktok`, `bilibili`, `blog`, or `email`
- `utm_medium`: `social` for posts, `video` for bilibili, `blog`, `email`
- `utm_campaign`: `pola_astrapath_nov2026` or `pola_astrapath_dec2026`, by the month of the post
- `utm_content`: `post1` to `post9`, `promo1` for the bilibili video, and `blog1` to `blog3`

**Rules for every post and email,** from the brand position: calm, not cheerful. No exclamation marks. No "get lost" jokes. Never "never be late again." Name the hallway, the door, or the room, never "go to floor four."

## Blog schedule

There are three posts, one every two weeks. They go on our own site at `/blog/`, which is best for search, and we cross-post them to Medium. Each post links to the landing page for its audience, and we promote each one in the next social post and the next newsletter. The article types come from the Class 6 slides (slide 45).

| Week | Type | Post | Links to |
|---|---|---|---|
| 2 | Founder journey | What 6 interviews taught us about finding a room in a building you don't know | Homepage |
| 4 | Tactical advice | Before spring semester: how to find your new classrooms before the first day | Students page |
| 6 | Solution explainer | How AstraPath gets you from the front door to the room (for Demo Day) | Homepage |

**More ideas, for later or to swap in:**
- **Problem-focused:** Why maps stop at the front door
- **Problem-focused:** Seven minutes inside Hamilton: where the time goes between classes
- **Founder journey:** Why we map buildings by hand, for now
- **Solution explainer:** Fastest, fewer changes, least effort: how AstraPath picks a route
- **Tactical advice:** Interviewing in a Midtown office tower: how to find the right door and where to check in
- **Tactical advice:** A step-free route through Northwest Corner, only once the entrance, elevator, and floors have been checked

## Email strategy

**Tool.** Netlify Forms collects our signups but can't send email. We will connect a free email tool that can send automatic emails, such as Brevo, Kit, or Mailchimp. Each page has its own waitlist form, so every contact comes in tagged with the role they signed up as.

**Segments:**

| Form | Segment | What they hear about first |
|---|---|---|
| `waitlist-home` | General | The app download link, new buildings |
| `waitlist-students` | Students | The app download link, new buildings |
| `waitlist-visitors` | Visitors | Visitor routes in buildings that have confirmed their access rules |
| `waitlist-step-free` | Step-free | Checked step-free routes |
| `waitlist-venues` | Venues | Venue plans. A founder emails each venue in person, with no automatic sequence. |

**By signup date (automatic, for every segment except venues):**
- **Day 0, welcome:** what AstraPath will do for their role, Jiawen's promo video, and their referral link from the thank-you page
- **Day 7:** reply to test a Northwest Corner route with us, or tell us which building they need next
- **Day 14:** a reminder to share their referral link

**Feature releases** go to the segment each feature is for, when it ships:
- the app download link to everyone
- checked step-free routes to the step-free segment
- visitor routes to visitors
- venue plans to venues

**Newsletter:** every two weeks to everyone, on Nov 20, Dec 4, and Dec 18 (Demo Day). Each one covers what we built, which building is next, and the latest blog post.

**By feature use:** these emails wait for the iPhone app. AstraPath has no accounts, so until then we can't see what anyone did in the app.

**Quiet, not naggy:** a person gets at most one email a week. If someone got a signup-date email that week, the newsletter waits.

## Napkin math

100 signups at a 1% signup rate takes about 10,000 visitors.

| Channel | Visitors, average | Visitors, best | Signups at 1%, average | Signups at 1%, best |
|---|---|---|---|---|
| bilibili promo video | 5,000 | 20,000 | 50 | 200 |
| Instagram + TikTok, 9 posts | 90 | 360 | 1 | 4 |
| Blog, 3 posts | 90 | 300 | 1 | 3 |
| **Total** | **5,180** | **20,660** | **52** | **207** |

How we got the numbers:
- **bilibili:** the team's estimate of visitors to our pages.
- **Instagram + TikTok:** 9 posts × 500 views per post across both apps (2,000 at best) × 2% of viewers clicking the bio link.
- **Blog:** about 30 visitors per post (100 at best), mostly from our own posts and emails.
- Referral signups from the thank-you page link aren't counted, so they're upside.

**What this tells us:** the best case clears 100, and the average case gets about half. Almost all of it rides on the bilibili video. Instagram and TikTok mostly keep people who already know us interested, rather than bringing new ones.

**When we check:** at the end of week 2, we compare bilibili signups (`utm_source=bilibili` in Netlify Forms) with the average-case pace. If we are behind, options include a second bilibili video in week 4, or three Instagram and TikTok posts a week. After every week, we update the Post links column and move effort to whatever brought signups.
