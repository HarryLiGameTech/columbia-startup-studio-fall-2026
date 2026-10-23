# Reddit Research Round 1 Discovery Searches

## Research Scope

**Problem space:** How international students research, compare, and apply to U.S. undergraduate colleges.

**Target users:** International high school students planning to apply to U.S. undergraduate programs, especially students who lack strong college counseling, are unsure of their academic position, or do not know where to begin.

**Questions for discovery:**

- How do students decide which colleges fit their academic profile, interests, budget, and location preferences?
- How do they classify schools as reach, target, or safety?
- Where do they look for requirements, tuition, scholarships, deadlines, majors, campus culture, and international-student support?
- Which sources do they distrust or consider outdated, incomplete, biased, or promotional?
- What makes the process confusing or overwhelming?
- Which tools, counselors, communities, spreadsheets, or other workarounds do they use?

## Manual Saving Instructions

Open each link manually in a logged-in browser at a normal pace. Do not open all links at once. Save each page into `reddit_corpus/raw/` using the suggested unique filename and keep the `.json` extension.

If a link is blocked, first open the corresponding normal subreddit search page without `.json`, let it load, and then try the `.json` link again. Do not use automated downloading.

## Prioritized Search Links

1. **International students discussing how to build a college list**  
   Save as: `round1_01_intltousa_college_list.json`  
   https://www.reddit.com/r/IntltoUSA/search.json?q=college%20list&restrict_sr=1&sort=top&t=year

2. **International students discussing reach, target, and safety schools**  
   Save as: `round1_02_intltousa_reach_target_safety.json`  
   https://www.reddit.com/r/IntltoUSA/search.json?q=reach%20target%20safety&restrict_sr=1&sort=top&t=year

3. **International students asking how to choose colleges or determine fit**  
   Save as: `round1_03_intltousa_choose_college_fit.json`  
   https://www.reddit.com/r/IntltoUSA/search.json?q=choose%20college%20fit&restrict_sr=1&sort=top&t=year

4. **International-student financial aid and scholarship concerns**  
   Save as: `round1_04_intltousa_financial_aid.json`  
   https://www.reddit.com/r/IntltoUSA/search.json?q=financial%20aid%20scholarship&restrict_sr=1&sort=top&t=year

5. **Experiences with counselors or lack of counseling**  
   Save as: `round1_05_intltousa_college_counselor.json`  
   https://www.reddit.com/r/IntltoUSA/search.json?q=college%20counselor&restrict_sr=1&sort=top&t=year

6. **Confusion or overwhelm during applications**  
   Save as: `round1_06_intltousa_application_overwhelmed.json`  
   https://www.reddit.com/r/IntltoUSA/search.json?q=application%20confused%20overwhelmed&restrict_sr=1&sort=top&t=year

7. **International-student college-list discussions in the broader application community**  
   Save as: `round1_07_a2c_international_college_list.json`  
   https://www.reddit.com/r/ApplyingToCollege/search.json?q=international%20student%20college%20list&restrict_sr=1&sort=top&t=year

8. **How applicants determine school fit**  
   Save as: `round1_08_a2c_choose_school_fit.json`  
   https://www.reddit.com/r/ApplyingToCollege/search.json?q=choose%20school%20fit&restrict_sr=1&sort=top&t=year

9. **Scattered college-research information and excessive searching**  
   Save as: `round1_09_a2c_college_research_websites.json`  
   https://www.reddit.com/r/ApplyingToCollege/search.json?q=college%20research%20websites%20information&restrict_sr=1&sort=top&t=year

10. **Reach, target, and safety classification discussions**  
    Save as: `round1_10_a2c_reach_target_safety.json`  
    https://www.reddit.com/r/ApplyingToCollege/search.json?q=reach%20target%20safety&restrict_sr=1&sort=top&t=year

11. **Financial aid for international applicants**  
    Save as: `round1_11_a2c_international_financial_aid.json`  
    https://www.reddit.com/r/ApplyingToCollege/search.json?q=international%20student%20financial%20aid&restrict_sr=1&sort=top&t=year

12. **Application-process confusion and overwhelm**  
    Save as: `round1_12_a2c_application_overwhelmed.json`  
    https://www.reddit.com/r/ApplyingToCollege/search.json?q=application%20process%20confused%20overwhelmed&restrict_sr=1&sort=top&t=year

13. **International applicants asking for profile evaluation**  
    Save as: `round1_13_chanceme_international_student.json`  
    https://www.reddit.com/r/chanceme/search.json?q=international%20student&restrict_sr=1&sort=top&t=year

14. **International applicants seeking realistic school lists**  
    Save as: `round1_14_chanceme_realistic_schools.json`  
    https://www.reddit.com/r/chanceme/search.json?q=international%20student%20realistic%20schools&restrict_sr=1&sort=top&t=year

15. **International students requesting school recommendations**  
    Save as: `round1_15_reversechanceme_international.json`  
    https://www.reddit.com/r/ReverseChanceMe/search.json?q=international%20student&restrict_sr=1&sort=top&t=year

16. **Applicants describing desired school fit**  
    Save as: `round1_16_reversechanceme_school_fit.json`  
    https://www.reddit.com/r/ReverseChanceMe/search.json?q=school%20fit&restrict_sr=1&sort=top&t=year

17. **Minority or disputed views about AI in college admissions**  
    Save as: `round1_17_a2c_ai_college_admissions_controversial.json`  
    https://www.reddit.com/r/ApplyingToCollege/search.json?q=AI%20college%20admissions&restrict_sr=1&sort=controversial&t=year

## After Saving

Confirm that the saved files contain JSON rather than an access-denied or rate-limit page. When all available pages are saved in `reddit_corpus/raw/`, report any links that failed and continue to local ingestion and Round 2 thread selection.
