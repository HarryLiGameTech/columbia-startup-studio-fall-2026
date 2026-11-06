---
read-when: A team is setting up or reading out its $100 ad test.
---

# Experiment Card Template

Fill this in **before** you spend a dollar. Commit it to your team folder, then launch. Don't edit sections 1 to 8 after launch. Section 9 is for the result.

The point of the card is that you decide what counts as a win before you see the data.

---

## 1. Question

One sentence, tied to a decision you'll make.

"Should we ______ ?"

## 2. Hypothesis

A claim with a number.

"At least ___% of visitors from [audience] who see [promise] will [sign up]."

## 3. The one variable

- **What we're testing:** (the promise, the audience, or the page)
- **Everything we hold fixed:** (page, offer, audience, budget, dates, placements)

## 4. Audience

One audience.

- **Platform and targeting:**
- **Why this audience:**

## 5. Setup

- **Platform:** Meta / Google Search / Reddit
- **The question this platform can answer:** (Meta: do visitors sign up? Google: do people search for this, and in what words? Reddit: does this community respond?)
- **Campaign objective:**
- **Budget:** $___ as a lifetime (total) budget
- **Start date:** ___ **End date:** ___ (7 days)
- **What counts as a signup:**
- **Where we read signups from:** (our database / GA4 / Amplitude / the ad dashboard)
- **Tracking check:** we clicked through our own ad link and saw the visit and the signup arrive. Yes / No
- **Expected clicks** (the platform's estimate): ___

## 6. The bar

Set these before launch.

- We read the result once, after the end date.
- **PASS** if signups are ___ or more.
- **FAIL** if signups are ___ or fewer.
- **UNCLEAR** if in between.
- **Our prediction:** ___ signups.

**Picking your numbers.** Find the row with your expected clicks. "Floor" is a signup rate that would mean the page isn't working; "good" is one that would mean it is. Each bar keeps the chance of a wrong call to about 1 in 20.

| Floor vs. good | Clicks | PASS at | FAIL at | UNCLEAR |
|---|---|---|---|---|
| 2% vs. 8% | 100 | 6 or more | 3 or fewer | 4 to 5 |
| 2% vs. 8% | 140 | 7 or more | 5 or fewer | 6 |
| 2% vs. 8% | 166 | 8 or more | 7 or fewer | none |
| 3% vs. 10% | 100 | 7 or more | 4 or fewer | 5 to 6 |
| 3% vs. 10% | 140 | 9 or more | 7 or fewer | 8 |
| 3% vs. 10% | 166 | 10 or more | 9 or fewer | none |

Pick a floor and a good rate that are far apart. With about 166 clicks, $100 can't settle whether your page converts 5% or 10%.

## 7. What we'll do

- **If PASS:**
- **If FAIL:** (low click rate means the hook or the audience is off; clicks but no signups means the page is off)
- **If UNCLEAR:** (default: don't spend more; decide from interviews and usability tests)

## 8. Stop rules

The only reasons to touch the ads mid-test: tracking is broken, the ad is disapproved, or spend is running over budget. Nothing else.

## 9. Result

Fill in after the end date.

- **Impressions:** ___ **Clicks:** ___ **Click rate:** ___%
- **Signups:** ___ **Signup rate:** ___%
- **Spend:** $___ **Cost per signup:** $___
- **Call:** PASS / FAIL / UNCLEAR
- **Did we do what section 7 said?**
