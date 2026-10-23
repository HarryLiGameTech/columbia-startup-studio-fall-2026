# UnlockDrill Reddit research

**Team:** 5 PPL\
**Prepared:** October 17, 2026\
**Status:** Corpus verified; research and proposed applications ready for team review.

## What we found

The manually saved corpus contains **30 distinct threads**, with **617 non-deleted/non-removed comment bodies** (including 1 AutoModerator comment excluded from interpretation). It includes 15 r/Sat threads, 9 r/GetStudying threads, 5 r/digitalminimalism threads, and 1 r/productivity thread. Students describe difficulty starting, breaks that expand into scrolling, and uncertainty about whether practice is helping. Broader discussions reveal a tension between restrictions that are too easy to bypass and restrictions people abandon, as well as the practical need to remain reachable. The evidence supports testing a small, useful practice action; it does not establish demand, retention, willingness to pay, or score gains for UnlockDrill.

## Collection and analysis method

The team manually saved 10 Reddit search JSON pages and 30 thread JSON pages through its browser. Searches used `sort=top&t=year`; 232 result entries represented 225 distinct candidate posts. The agent selected threads for relevance to initiation, attention, study quality, fatigue, and contrasting experiences, then read the local post and comment text. No Reddit pages were fetched automatically. This is purposive research, not a representative or exhaustive sample.

Files were parsed locally, checked by embedded post ID rather than filename, and normalized into one JSON file per thread. A mislabeled duplicate of `1rndkot` initially occupied the `1oktpuh` filename; the team re-saved the correct thread, which was verified before this report. All 30 expected IDs are now present once. Search-reported comment totals may differ from saved bodies; this report counts only text actually in the local files.

Post dates span **2025-10-30 to 2026-10-07**; all saved post/comment timestamps span **2025-10-30 to 2026-10-13** (UTC dates). Image-only evidence and external links were not treated as read evidence. Deleted/removed text, automated moderation, jokes, and product pitches were not treated as independent support for product demand. Named-product recommendations are potential promotional material even when they sound personal.

Every excerpt in [quotes.jsonl](quotes.jsonl) was checked as an exact contiguous substring of its source post or comment. Wording, spelling, and punctuation are preserved. Theme counts below are computed from that **curated evidence ledger**, count a thread once per theme, and are minimum documented support—not exhaustive coding, percentages of users, or estimates of market prevalence. Advice, self-reported experience, and our product interpretation remain distinct.

## Themes

### 1. Starting and returning to study can be difficult even when students care

> The hardest part is starting again. Every time I try to study, it feels overwhelming because I know how much I’ve missed.

[Q01: r/Sat, 2026-04, post](https://www.reddit.com/r/Sat/comments/1srrdgp/trying_to_study_for_the_sat_after_a_really_rough/)

> I learned the hard way that I couldn’t tell when 10 minutes turned into 20 umm or even an hour of scrolling, lol.

[Q02: r/GetStudying, 2026-04, post](https://www.reddit.com/r/GetStudying/comments/1serr7p/what_do_you_guys_do_in_study_breaks/)

Documented in **4 separate threads**: Q01, Q02, Q07, Q08. The SAT example concerns returning after a difficult period; the other examples concern broader studying and university work. They should not be collapsed into a single cause. Q07 reports continued avoidance after removing distractions, while Q08 says short sessions and quiz apps did not solve the problem.

**Implication to test:** Make the first action concrete and small, but compare it with alternatives and allow people to decline. A short task is a hypothesis, not a universal solution.

### 2. Useful friction and intolerable restriction are different

> All of it is fake. If I can override it, I will.

[Q09: r/digitalminimalism, 2026-01, post](https://www.reddit.com/r/digitalminimalism/comments/1qh3vzb/i_dont_trust_myself_around_my_phone_anymore/)

> And I'd last maybe 3 days before I'd undo everything in frustration.

[Q04: r/digitalminimalism, 2026-02, post](https://www.reddit.com/r/digitalminimalism/comments/1r2qgd5/the_thing_that_finally_clicked_about_my_phone/)

Documented in **5 separate threads**: Q04, Q09, Q10, Q11, Q18. These are broader phone-use or study contexts, not direct SAT demand. Some accounts favor physically moving the phone; others report deleting restrictive apps or repeatedly bypassing limits. In the physical-blocker thread, some commenters report satisfaction, while creators also promote their products. We do not treat those endorsements as independent validation.

**Implication to test:** Track skipping, disabling, and continued voluntary use. Offer adjustable timing and compare against simply putting the phone away; do not assume stronger blocking is always better.

### 3. People may need phone access while trying to avoid scrolling

> Also, I have to be on call all day, so I can't turn off my phone completely.

[Q03: r/GetStudying, 2026-04, post](https://www.reddit.com/r/GetStudying/comments/1sjwdg0/any_tips_on_how_to_break_a_phone_addiction_its/)

Documented in **3 separate threads**: Q03, Q12, Q13. The contexts include being on call, work scheduling, and required work apps. Q13 is from a named-product recommendation thread and carries a promotional caveat. A commenter in the newly corrected thread also objects that removing electronics does not work when studying is online; this is additional context, not included in the ledger count.

**Implication to test:** Preserve essential access and explain exactly which apps or moments are affected. This supports investigating control and exceptions; it does not prove the right skip frequency for SAT students.

### 4. More questions or more time are not the same as better learning

> Measure progress by whether those same mistakes are disappearing, not by hours studied or the number of full tests completed.

[Q05: r/Sat, 2026-07, comment](https://www.reddit.com/r/Sat/comments/1v9yhkb/how_much_can_i_realistically_improve_a_1300_in_30/p0nc21u/)

> I mean the point of my post was asking how to study smarter not necessarily harder 😭

[Q06: r/Sat, 2026-06, comment](https://www.reddit.com/r/Sat/comments/1tzu7bl/how_does_one_study_smart_for_the_sat_to_reach_a/oqdnr7u/)

Documented in **3 separate SAT threads**: Q05, Q06, Q14. Q05 is commenter advice, Q06 is the original poster clarifying the question, and Q14 is a personal account of memorizing mistakes rather than understanding them. The evidence is about perceived learning quality, not independently measured gains. Another SAT post reports remembering questions after completing the bank twice: [Stuck at 650 RW, aiming for 750+ in 3 months. I've already finished the Question Bank twic](https://www.reddit.com/r/Sat/comments/1urcl3b/stuck_at_650_rw_aiming_for_750_in_3_months_ive/).

**Implication to test:** Pair a relevant question with a concise explanation and a later similar question. Assess understanding rather than treating streaks or completion counts as proof of learning. Do not automatically expand into a full error-journal product.

### 5. Fatigue is a separate constraint, not just a distraction problem

> My school ends at roughly 4pm, and after that I'll just be tired which I can't even concentrate to solve math problems.

[Q15: r/GetStudying, 2026-10, post](https://www.reddit.com/r/GetStudying/comments/1wuvezc/how_do_i_study_while_being_tired/)

Documented in **3 separate general-study threads**: Q15, Q16, Q17. These describe after-school tiredness, poor sleep, or fatigue when attempting study. Comments suggest many responses, including rest, schedule changes, and short sessions; they are user suggestions, not medical or scientific findings.

**Implication to test:** Let students pause and choose timing. Avoid guilt-based messaging or implying every break should become more studying.

## Contradictions and limits to preserve

- **Remove the phone versus preserve necessary access:** Q10 describes success with leaving the phone elsewhere; Q03 and Q12 describe why complete separation is difficult.
- **Small tasks versus persistent avoidance:** A smaller start may help some people, but Q07 and Q08 explicitly challenge a universal short-task solution.
- **Stricter limits versus sustained use:** Q09 and Q18 criticize bypassable limits; Q04 and Q11 report abandoning restrictions. These may describe different people, situations, or tolerances.
- **Quantity versus quality:** In the SAT discussion behind Q06, advice to study eight hours provokes pushback. Another thread debates whether all practice tests must be used before an attempt: [How I got a 1510 (790 math!) without spending money and with not a lot of time.](https://www.reddit.com/r/Sat/comments/1pue5k9/how_i_got_a_1510_790_math_without_spending_money/). Do not resolve these disagreements into a single prescribed duration.
- **Phone distraction versus other barriers:** [What am I doing wrong? practice scores 1340–1460 but got 1240 on the real SAT](https://www.reddit.com/r/Sat/comments/1sj42i3/what_am_i_doing_wrong_practice_scores_13401460/) includes test anxiety, while [final SAT in 2 weeks... need a prep schedule](https://www.reddit.com/r/Sat/comments/1wzkdp9/final_sat_in_2_weeks_need_a_prep_schedule/) concerns a device constraint. Neither should be counted as proof that app-opening prompts solve the user's problem.

## For your personas

These are proposed refinements of existing composites, not new validated customer segments. No demographic details, budgets, or diagnoses should be invented from these posts.

### Maya — tired starter

Use Q01 and Q02: the first step can feel overwhelming, and a short break can expand into scrolling. Test whether the page explains one achievable action without shaming the student. The general-study break account does not establish Maya's age or SAT status. Quote sources: [Q01: r/Sat, 2026-04, post](https://www.reddit.com/r/Sat/comments/1srrdgp/trying_to_study_for_the_sat_after_a_really_rough/); [Q02: r/GetStudying, 2026-04, post](https://www.reddit.com/r/GetStudying/comments/1serr7p/what_do_you_guys_do_in_study_breaks/).

### Jordan — blocker skeptic

Use Q03 and Q04: remaining reachable matters, and excessive restriction can cause abandonment. Ask whether the mechanism and controls are clear and whether it sounds like another blocker to disable. Quote sources: [Q03: r/GetStudying, 2026-04, post](https://www.reddit.com/r/GetStudying/comments/1sjwdg0/any_tips_on_how_to_break_a_phone_addiction_its/); [Q04: r/digitalminimalism, 2026-02, post](https://www.reddit.com/r/digitalminimalism/comments/1r2qgd5/the_thing_that_finally_clicked_about_my_phone/).

### Casey — purposeful reviewer

Use Q05 and Q06: meaningful practice matters more than accumulating hours or questions. Ask whether the question is relevant, the explanation useful, and the end of the activity clear. Q05 is advice, not evidence Casey personally achieved a result. Quote sources: [Q05: r/Sat, 2026-07, comment](https://www.reddit.com/r/Sat/comments/1v9yhkb/how_much_can_i_realistically_improve_a_1300_in_30/p0nc21u/); [Q06: r/Sat, 2026-06, comment](https://www.reddit.com/r/Sat/comments/1tzu7bl/how_does_one_study_smart_for_the_sat_to_reach_a/oqdnr7u/).

## For your brand position

The five brand-source selections are **Q01–Q05**; see [selected_quotes.md](selected_quotes.md) for exact text, provenance, and destination mapping.

- **Problem language:** “starting again” (Q01) and “an hour of scrolling” (Q02) can inform empathetic problem copy. Keep these contexts distinct.
- **Control language:** Q03 supports explaining essential access; Q04 motivates explaining adjustable timing and pause. The wording “skip and pause” remains product language, not a Reddit quote.
- **Learning language:** Q05 supports describing relevant practice and useful feedback rather than promising score gains.
- **Original copy to test:** “One SAT question. A small start, on your terms.” This is newly written copy, not a quotation or validated claim.
- **Language to avoid:** guaranteed score increases, “cures phone addiction,” or claims that students simply lack discipline. The SAT poster behind Q06 explicitly resists advice to study harder; Q07 and Q08 show why a simplistic discipline message can miss the problem.
- **Objections to answer:** Why would I keep this enabled? Can I use my phone when I need it? Is this question helping me learn? Why is this better for me than putting the phone away?

## Caveats

Only half the threads are from r/Sat; subreddit membership does not verify anyone's age, exam plans, location, or identity. Search terms intentionally favor distraction and study difficulties, and top/year sorting favors visible discussions. Comments within a thread are not independent interviews. Accounts may be mistaken, promotional, exaggerated, or AI-written; no external verification of identities or outcomes was performed. Reddit claims about dopamine, ADHD, test scoring, and commercial tools are not adopted as established facts. This corpus contains no direct test of UnlockDrill, and no prevalence, retention, revenue, or learning-outcome estimate is warranted.

## Coverage and handoff

- **30 / 30 expected distinct threads verified**, all with usable comments; 0 missing; 0 duplicate post IDs.
- **10 discovery search files** retained separately from the thread count.
- **617 non-deleted/non-removed comment bodies**, including 1 AutoModerator bodies; greetings and other low-information comments are included in the inventory count but not treated as findings.
- **18 exact excerpts** in [quotes.jsonl](quotes.jsonl); theme counts in [theme_counts.json](theme_counts.json).
- Full thread list, filenames, and per-thread counts: [coverage.md](coverage.md).
- Raw pages remain in `../reddit_corpus/raw/`; normalized copies in `../reddit_corpus/normalized/`.

The class README requests the corpus list, summary, and selected quotes rather than raw pages in the class repository. Retain the full raw corpus and supply it separately if the TA requests access. This report replaces the scope of the earlier five-link scan; its old R1–R5 quotes should not be treated as verified by this new corpus. The team approved the selected quotes on October 17, and they are integrated into [brand_position.md](../brand_position.md) and the [persona files](../personas/README.md). Fresh installed-agent tests remain outstanding.
