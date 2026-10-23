# First traffic report: October 12 to October 22, 2026

Prepared by Yuval (analytics) for Emily (traffic owner), October 22, 2026. Times are America/New_York. Numbers come from our own waitlist and app databases, read on October 22 at about 22:15. GA4 visitor and session numbers are not in this draft yet; they are marked **Pending data from Yuval**.

## Summary

The waitlist has **11 real signups** in its first eleven days. Most arrived in the first week, around the HW5 launch posts. Instagram is the only tagged channel with more than one signup. App accounts are still almost all team test accounts. The app is available at https://app.call-it.app.

## Actual results

| Measure | Week of Oct 12 | Week of Oct 19 (to Oct 22) | Total |
|---|---|---|---|
| Real waitlist signups | 9 | 2 | 11 |
| Team test signups (excluded) | 11 | 0 | 11 |

Real waitlist signups by source:

| Source | Medium | Campaign | Signups |
|---|---|---|---|
| instagram | bio | hw5_launch | 3 |
| linkedin | post | hw5_launch | 1 |
| direct or untagged | | | 7 |

The source of the seven untagged signups is unknown.

Group type chosen at signup, where given: sports 3, friends 1.

App accounts at app.call-it.app are counted separately from the waitlist: 8 accounts, 6 confirmed, 7 of them team test accounts.

## Visitors and conversion

| Measure | Value |
|---|---|
| Landing-design views in our own table, Oct 12 to 22 | 212 (tests included; home-page views not in this table; not usable as a conversion denominator) |
| GA4 users, sessions and views per page | **Pending data from Yuval** |
| GA4 sessions per source and medium | **Pending data from Yuval** |
| `sign_up` marked as a GA4 key event | **Pending confirmation from Yuval** |

Yuval reported a live browser check on October 22: GA4 loads on all four pages (`/`, `/for/friends`, `/for/sports`, `/for/agreements`), and the thank-you page sends `sign_up` once per saved signup.

## What this tells us

- **Tagged links work.** Every tagged post that produced a signup is attributable to its source and campaign.
- **Untagged sharing hides the source.** Seven of eleven signups came without a tag. From now on, every link anyone shares should carry UTM tags, even in a direct message (`utm_medium=dm`).
- **The sample is too small for a rate.** Eleven signups don't support a conversion rate yet. The forecast keeps the 1%-or-lower planning assumption until GA4 visitor counts are in.

## Next report

Due October 29, covering October 23 to 29. Inputs are the same three database reports plus the GA4 Traffic acquisition export, so the conversion rate can be stated per source.
