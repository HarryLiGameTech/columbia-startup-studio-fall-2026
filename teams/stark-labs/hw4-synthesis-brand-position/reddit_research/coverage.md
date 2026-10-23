# Reddit corpus coverage

Reviewed locally on October 9, 2026. The human saved 33 named JSON files: 12 searches and 21 attempted thread saves. One thread save is a duplicate/mismatch, leaving **32 accepted files: 9 nonempty searches, 3 valid zero-result searches and 20 distinct comment-thread saves**. Thus there are 29 accepted nonempty files. Correcting R2-09 would give 33 accepted files and 30 nonempty files; do not count its current duplicate as an additional thread.

Round one contained 182 search appearances and 148 distinct post IDs; all 148 post bodies were screened. Round two contains 814 saved comment objects, of which 790 have nonempty, non-deleted/non-removed bodies. All saved bodies in these 20 files were reviewed. Reported Reddit comment totals are larger than many saved payloads, so these are partial snapshots, not complete-thread coverage. R2-15 explicitly contains 31 `more` placeholders.

The original R1-09 filename had an extra `.json` suffix; only the working-copy filename was normalized. Source hashes and original names are retained. The incorrect R2-09 is preserved outside the active corpus as a duplicate of R2-08.

## Search files

| Search | File | Results | Status |
|---|---|---:|---|
| [R1-01](https://www.reddit.com/r/web_design/search.json?q=client+website+content&restrict_sr=1&sort=top&t=year) | `r1-01-web_design.json` | 25 | saved and parsed |
| [R1-02](https://www.reddit.com/r/web_design/search.json?q=waiting+client+content&restrict_sr=1&sort=top&t=year) | `r1-02-web_design.json` | 19 | saved and parsed |
| [R1-03](https://www.reddit.com/r/web_design/search.json?q=content+questionnaire&restrict_sr=1&sort=top&t=year) | `r1-03-web_design.json` | 0 | saved; zero-result listing |
| [R1-04](https://www.reddit.com/r/freelance/search.json?q=website+client+content&restrict_sr=1&sort=top&t=year) | `r1-04-freelance.json` | 21 | saved and parsed |
| [R1-05](https://www.reddit.com/r/freelance/search.json?q=client+copy+images&restrict_sr=1&sort=top&t=year) | `r1-05-freelance.json` | 13 | saved and parsed |
| [R1-06](https://www.reddit.com/r/webdev/search.json?q=client+content+collection&restrict_sr=1&sort=top&t=year) | `r1-06-webdev.json` | 25 | saved and parsed |
| [R1-07](https://www.reddit.com/r/webdev/search.json?q=website+content+handoff&restrict_sr=1&sort=top&t=year) | `r1-07-webdev.json` | 25 | saved and parsed |
| [R1-08](https://www.reddit.com/r/smallbusiness/search.json?q=website+content+writing&restrict_sr=1&sort=top&t=year) | `r1-08-smallbusiness.json` | 25 | saved and parsed |
| [R1-09](https://www.reddit.com/r/smallbusiness/search.json?q=website+designer+content&restrict_sr=1&sort=top&t=year) | `r1-09-smallbusiness.json` | 25 | saved and parsed |
| [R1-10](https://www.reddit.com/r/web_design/search.json?q=content+snare&restrict_sr=1&sort=controversial&t=year) | `r1-10-web_design.json` | 0 | saved; zero-result listing |
| [R1-11](https://www.reddit.com/r/freelance/search.json?q=client+questionnaire&restrict_sr=1&sort=controversial&t=year) | `r1-11-freelance.json` | 0 | saved; zero-result listing |
| [R1-12](https://www.reddit.com/r/web_design/search.json?q=client+content&restrict_sr=1&sort=top&t=month) | `r1-12-web_design.json` | 4 | saved and parsed |

## Requested comment threads

| Request | Thread | Saved comment objects / readable bodies | Status |
|---|---|---:|---|
| R2-01 | [Regular client delays causing project backlog](https://www.reddit.com/r/freelance/comments/1o7f187/regular_client_delays_causing_project_backlog/) | 5 / 5 | read — saved portion |
| R2-02 | [How are you handling content creation for the sites you build?](https://www.reddit.com/r/web_design/comments/1qu33wf/how_are_you_handling_content_creation_for_the/) | 26 / 26 | read — saved portion |
| R2-03 | [How do you handle clients who prefer sending long, unstructured voice notes over written briefs?](https://www.reddit.com/r/freelance/comments/1uqoptb/how_do_you_handle_clients_who_prefer_sending_long/) | 25 / 21 | read — saved portion |
| R2-04 | [Our biggest bottleneck isn't the work, it's waiting for clients to do their part. Anyone else?](https://www.reddit.com/r/freelance/comments/1sci8yg/our_biggest_bottleneck_isnt_the_work_its_waiting/) | 17 / 16 | read — saved portion |
| R2-05 | [I cried on a client call today](https://www.reddit.com/r/freelance/comments/1wjvyxi/i_cried_on_a_client_call_today/) | 62 / 62 | read — saved portion |
| R2-06 | [How much would you charge for a custom perfume ecommerce website with this scope?](https://www.reddit.com/r/web_design/comments/1x1cxg5/how_much_would_you_charge_for_a_custom_perfume/) | 9 / 9 | read — saved portion |
| R2-07 | [Freelancers: How do you handle client website feedback efficiently?](https://www.reddit.com/r/freelance/comments/1p61x55/freelancers_how_do_you_handle_client_website/) | 2 / 2 | read — saved portion |
| R2-08 | [How do you handle “one small change” requests without killing your weekend?](https://www.reddit.com/r/webdev/comments/1qecnm4/how_do_you_handle_one_small_change_requests/) | 44 / 43 | read — saved portion |
| R2-09 | [Lost $2,300 to scope creep on one project. How do you prevent this?](https://www.reddit.com/r/freelance/comments/1ozc3zq/lost_2300_to_scope_creep_on_one_project_how_do/) | — | missing expected thread; saved file duplicates R2-08 |
| R2-10 | [[ADVICE] How are you sending site design files to clients?](https://www.reddit.com/r/web_design/comments/1tbzu56/advice_how_are_you_sending_site_design_files_to/) | 18 / 18 | read — saved portion |
| R2-11 | [What is important to include in website contracts?](https://www.reddit.com/r/web_design/comments/1tbbn27/what_is_important_to_include_in_website_contracts/) | 32 / 30 | read — saved portion |
| R2-12 | [My top 5 rules for long term client relationships (8 years freelancing)](https://www.reddit.com/r/freelance/comments/1v3j8w7/my_top_5_rules_for_long_term_client_relationships/) | 14 / 12 | read — saved portion |
| R2-13 | [What steps should I take to professionally redesign my website if I already have most of the content and branding finished?](https://www.reddit.com/r/web_design/comments/1wfwk38/what_steps_should_i_take_to_professionally/) | 33 / 33 | read — saved portion |
| R2-14 | [How do small businesses without a marketing person actually handle marketing?](https://www.reddit.com/r/smallbusiness/comments/1w5hlb9/how_do_small_businesses_without_a_marketing/) | 66 / 65 | read — saved portion |
| R2-15 | [I found out my mom is paying $400 a month for a static website and an email...](https://www.reddit.com/r/webdev/comments/1v5vhb3/i_found_out_my_mom_is_paying_400_a_month_for_a/) | 174 / 171 | read — saved portion |
| R2-16 | [Rant: Webflow SUCKS](https://www.reddit.com/r/webdev/comments/1tqkyfv/rant_webflow_sucks/) | 48 / 43 | read — saved portion |
| R2-17 | [Hard-coding vs WordPress for client sites: when does “full stack” actually make sense?](https://www.reddit.com/r/webdev/comments/1pta50j/hardcoding_vs_wordpress_for_client_sites_when/) | 33 / 33 | read — saved portion |
| R2-18 | [Webflow alternative for less tech-savvy clients?](https://www.reddit.com/r/web_design/comments/1q6d1vz/webflow_alternative_for_less_techsavvy_clients/) | 29 / 29 | read — saved portion |
| R2-19 | [Freelancers with small business clients - what's your stack?](https://www.reddit.com/r/webdev/comments/1tya16g/freelancers_with_small_business_clients_whats/) | 65 / 65 | read — saved portion |
| R2-20 | [Contractor permanently deleted content. What to do?](https://www.reddit.com/r/smallbusiness/comments/1qj7slu/contractor_permanently_deleted_content_what_to_do/) | 48 / 48 | read — saved portion |
| R2-21 | [Is anyone else getting tired of the “I built a website with AI, what do you think?” posts?](https://www.reddit.com/r/smallbusiness/comments/1vw5wad/is_anyone_else_getting_tired_of_the_i_built_a/) | 64 / 59 | read — saved portion |

## Independence and limits

The website-image-work narrative appears in multiple first-round crossposts (1wjvyxi, 1wjyvz2 and 1wjywu0); count one narrative. The clinic project appears as 1pta50j and 1pta8zs; count one project. R2-16 contains repeated same-author comment bodies (oohv9r0/oohrieq and ooj806q/ooj8dii); these are not independent observations. Comment scores are captured snapshots, not credibility guarantees. We did not check account histories or voting patterns, so promotion and coordination cannot be ruled out.

## Remaining manual correction

Save [R2-09, the intended scope-creep discussion](https://www.reddit.com/r/freelance/comments/1ozc3zq.json) as `r2-09.json`. No further automated Reddit access is used. The 20 reviewed threads support a bounded write-up; topical saturation is not claimed. Raw pages remain local and are excluded from the class package.
