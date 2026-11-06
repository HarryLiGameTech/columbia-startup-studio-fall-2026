# Weekly update: November 6, 2026

## What we built last week and why
After the Oct 23 midterm we slowed down for a week, so most of this happened in the last few days.
- Fixed bugs on the staging MVP that would have blocked people mid-flow [list the main ones, e.g. favorites not updating], so usability testers can get through search, saving, and booking.
- Wrote a usability test script (docs/usability/test_script.md in the Gable repo) with tasks that end at our aha moment: describing what you want and getting a short list of sublets that fit.
- Opened the staging site to the public so testers can reach it without a Vercel login.
- Started "List your room": Columbia students post their sublet and our team verifies it by hand before it goes live. Why: every listing in Gable is still sample data, so no one can get real value yet. Real, verified supply is our biggest gap.

## What we're building this week and why
- Run 3–5 usability sessions with students outside our team, then fix the biggest problems they hit. Why: we've only watched ourselves use Gable.
- Finish "List your room" and get our first 5–10 real sublets from our network. Why: real listings turn Gable from a demo into something useful, and they're our path to real users.
- Automate the welcome email that still sends by hand. Why: it's the first touch after someone signs up.

## Current user count
[N] waitlist signups (Supabase `signups`, excluding our own test rows). 0 real listings so far.

## Biggest blocker
Supply. We don't have real sublets yet, and we've decided not to scrape sites that prohibit it, so listings have to come from students posting them directly.