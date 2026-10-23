# Reddit research: verifying a NYC apartment before you commit

## What we found
Across 20 threads (October 2025 to September 2026, mostly r/NYCapartments, plus r/AskNYC and r/columbia), renters keep describing the same gap: listings don't show what a place is really like, and the problems come out only at the tour, at move-in, or months later. Experienced New Yorkers do close that gap themselves, using HPD and 311 records, landlord lookups, and conversations with current tenants. But that knowledge is scattered and slow, and newcomers usually don't know it exists. Meanwhile bidding wars and "sign almost immediately" norms push people to commit before they can check anything. People who search remotely or from out of state carry the most risk, and they get the least sympathy when it goes wrong.

Counts below come from `quotes.jsonl` (82 verbatim quotes) and were computed with a script. "Threads" means the number of separate threads where we tagged a quote with that theme.

## Themes

### 1. Listings don't match reality (18 quotes, 5 threads)
- "The listings themselves are fiction: AI-generated photos are everywhere and not even subtle about it." r/NYCapartments, Mar 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1s2we9l/streeteasy_has_become_almost_completely_useless/))
- "ive been to 10 showings this week and none of them look like the photos it's crazzzzy" r/NYCapartments, Mar 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1s0qkkr/stop_ai_apartments/obwveju/))
- "pics had a full sized sectional couch that would easily imply a 12-15 foot wide room. On viewing it was barely 8 feet wide" r/NYCapartments, Mar 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1s0qkkr/stop_ai_apartments/oc1ijcw/))
- "I stupidly put in an application because I asked for a walk-through video and it looked great. I guess they’re AI-generating videos as well." r/NYCapartments, Mar 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1s0qkkr/stop_ai_apartments/)). The post scored 2,050, the highest in the corpus.
- "There's no way to know if an apartment has been rejected by 40 other people or just listed." r/NYCapartments, Mar 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1s2we9l/streeteasy_has_become_almost_completely_useless/))
- "We encountered so much bait-and-switching, completely unresponsive brokers, and naturally many FARE act violations along the way." r/NYCapartments, May 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1tjv5vb/my_apartment_search_experience/))
- Pattern: this appears in 5 separate threads, and the two posts at the center of it scored 2,050 and 812. It is the strongest and most recent signal in the corpus. It matches what Zaynah said in your interviews about AI-generated photos.

### 2. Problems surface only after you're in (11 quotes, 5 threads)
- "There’s so many potential issues you won’t necessarily see on a tour and those are the ones that sneak up on you and ruin your life." r/NYCapartments, Mar 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1rowe4d/what_are_the_biggest_red_flags_to_look_for_when/o9jorxj/))
- "There are zero windows in this unit and it gets unbearably hot and humid in the summer." r/NYCapartments, Aug 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1w05ds1/realized_im_living_in_an_illegal_basement_what_do/)). The poster had toured the unit, paid a broker fee, and only learned it was an illegal basement from a coworker.
- "The broker didn’t tell me the apt number in advance, so I couldn’t check whether the specific was affected." r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1snmp9x/dream_apartment_rent_stabilized_bedbug_history/))
- "they're still showing off unoccupied apartments priced under market to new tenants that have no idea what they're getting into." r/AskNYC, Jan 2026 ([link](https://www.reddit.com/r/AskNYC/comments/1qnk8lm/what_do_you_check_about_a_landlord_or_building/o1uc86i/))
- "noise from upstairs neighbors. But this is hard to test for during a tour." r/NYCapartments, Jan 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1q5i34z/nyc_apartment_rental_lessons_learned_the_hard_way/ny08iwl/))
- Pattern: this appears in 5 threads, covering pests, heat, noise, legality, and size. It mirrors Jude's experience with pests and AC in your interviews.

### 3. Experienced renters verify on their own, and it's fragmented (18 quotes, 5 threads)
- "HPD violations usually tell the real story way better than the listing does." r/AskNYC, Jan 2026 ([link](https://www.reddit.com/r/AskNYC/comments/1qnk8lm/what_do_you_check_about_a_landlord_or_building/o1ztp9c/))
- "For me it’s all about patterns not one off issues. I look at HPD violations, repeated 311 complaints and whether the landlord owns a bunch of other problem buildings under different LLCs." r/AskNYC, Jan 2026 ([link](https://www.reddit.com/r/AskNYC/comments/1qnk8lm/what_do_you_check_about_a_landlord_or_building/o1x4ksx/))
- "The best source of what it's like to live there are other tenants." r/AskNYC, Jan 2026 ([link](https://www.reddit.com/r/AskNYC/comments/1qnk8lm/what_do_you_check_about_a_landlord_or_building/o21dsu3/))
- "always ask if you can speak to a current tenant (or just hover outside the building after your tour til you see one)." r/NYCapartments, Mar 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1rowe4d/what_are_the_biggest_red_flags_to_look_for_when/o9jorxj/))
- "The city provides a ton of data on rental buildings but it’s scattered across dozens of different hard-to-read databases." r/NYCapartments, Jun 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1tyhs50/i_built_a_free_tool_for_renters_to_easily_spot/)). This is a builder's post, and it scored 1,090.
- "Checking rent stabilization is good to do, but takes weeks or a month to get info. It's not something you can realistically do before signing a lease" r/AskNYC, Jan 2026 ([link](https://www.reddit.com/r/AskNYC/comments/1qnk8lm/what_do_you_check_about_a_landlord_or_building/o1ubn9k/))
- Pattern: this appears in 5 threads. Tools that commenters name include HPD Online, 311, Who Owns What (JustFix), OpenIgloo, the bedbug registry, apartmentaudit.nyc, and StreetSmart. Public records exist, but the best signal (current tenants) has no channel.

### 4. Speed and bidding pressure (10 quotes, 6 threads)
- "It’s gotten to the point where I feel like if I don’t bid I will lose truly horrible that this normalized now." r/NYCapartments, May 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1t9lmoa/need_to_rant_about_losing_apartment_bidding_war/ol2yt7j/))
- "have all your documents ready, be proactive reaching out to new listings, be willing to sign almost immediately etc." r/NYCapartments, Sep 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1wlp7k2/moving_to_nyc_for_a_job_is_finding_an_apartment/pb0m79h/))
- "I’m also scared though if I don’t put it in the deposit he’s just gonna give the apartment to someone else" r/NYCapartments, Mar 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1rofkxp/about_to_put_down_a_deposit_for_an_apartment_the/))
- "The cycle of a rental info being poster, to you submitting your interest and documents and to signing the lease is very short, can just be a few days!" r/columbia, May 2026 ([link](https://www.reddit.com/r/columbia/comments/1szm6e9/grad_school_housing_advice_realistic_chances_of/ok3wajp/))
- Pattern: this appears in 6 threads, the widest spread of any theme. It is the reason verification gets skipped.

### 5. Hidden and illegal costs (8 quotes, 4 threads)
- "I had them and my electric bills were over $500 every month." r/NYCapartments, Sep 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1wac6ae/why_does_no_one_talk_about_wallmounted_ac_units/p8h6u9q/)). This refers to wall units that turned out to be the only heat.
- "how am I supposed to know the 750 is actually going to the super?" r/NYCapartments, Mar 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1rofkxp/about_to_put_down_a_deposit_for_an_apartment_the/))
- "I’m completely exhausted by the hidden financial traps of NYC apartment hunting." r/NYCapartments, May 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1tqgx3c/i_wrote_a_script_to_expose_hidden_coned_and/))
- Pattern: this appears in 4 threads. It matches the surprise $600 charge and AC costs from Jude's interview.

### 6. Newcomers are easy targets (8 quotes, 4 threads)
- "They knew I needed a place ASAP and that I was from Philly and didn't fully know the rules." r/NYCapartments, May 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1t9lmoa/need_to_rant_about_losing_apartment_bidding_war/ol3814z/))
- "Obviously since I’m new to the city maybe this is just a thing I don’t know about" r/NYCapartments, Mar 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1rofkxp/about_to_put_down_a_deposit_for_an_apartment_the/))
- "Brokers ghost me, apartments reject me, and I'm just so overwhelmed and confused." r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1selgra/deeply_overwhelmed_by_the_process_of_finding_an/))
- "If you even mention \"no income\" or \"guarantor\" in an initial contact, you are 99% getting ghosted." r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1selgra/deeply_overwhelmed_by_the_process_of_finding_an/oesp13k/))
- Pattern: this appears in 4 threads.

### 7. Remote or sight-unseen deals go wrong, and the crowd blames you (9 quotes, 2 threads tagged directly)
- "sent me videos of the place in the winter when the place was in a much better condition. I could tell because there was snow on the window. I did not think I had to confirm that it was still in good condition." r/NYCapartments, Oct 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1o1n4hp/do_not_sublet_on_facebook_in_nyc/))
- "My roommates are international and wanted to lock in a place before they started work in July, so we didn't get to see it in person beforehand." r/NYCapartments, Jul 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1upyc2j/signed_a_lease_before_viewing_in_person_got_a/))
- "Why in the world would you pay 2 grand for an apartment sight unseen?!?! I understand people are desperate but cmon man, yall can’t keep getting scammed like this!" r/NYCapartments, Oct 2025, score 1,207 ([link](https://www.reddit.com/r/NYCapartments/comments/1o1n4hp/do_not_sublet_on_facebook_in_nyc/nihmq33/))
- "Okay, transplant who didn’t bother going in person before handing over two grand" r/NYCapartments, Oct 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1o1n4hp/do_not_sublet_on_facebook_in_nyc/nihq2n5/))
- Pattern: two threads are directly about this. Related cases show up in 3 more: the walk-through video in the AI listings thread, the out-of-stater limited to 12 showings over 2 weekends, and the one-weekend job-mover. Treat this as a strong signal for your target user, but a smaller sample.

## For your personas
- **The remote mover on a clock.** This person is out of state or international, can visit once or twice, and has a fixed start date for a job or school. They see a limited number of units ("12 was the most I could manage", [link](https://www.reddit.com/r/NYCapartments/comments/1pzxari/what_i_learned_from_my_first_nyc_apartment_search/)). They rely on videos and photos that turn out to be misleading (Themes 1 and 7). Sometimes they sign sight unseen to satisfy roommates' deadlines (1upyc2j).
- **The rule-unaware newcomer.** This person doesn't know what's normal or legal: super "tips", good-faith deposits, months paid upfront (Theme 6, 1rofkxp, 1t9lmoa). Their questions tend to start with "is this normal?" They rely on a guarantor and get ghosted for it (1selgra).
- **The Columbia master's student.** They are low priority for university housing ("very very low chances for master's students", [link](https://www.reddit.com/r/columbia/comments/1szm6e9/grad_school_housing_advice_realistic_chances_of/ok3wajp/)). They are pushed into the off-campus market late, with no fallback plan. This matches Jackson's and Yung Yi's interviews.
- **The burned second-timer (contrast persona).** This person has been through the process once and now runs HPD, 311, and tenant checks themselves (Theme 3). They show what a "verified" decision looks like, and they are a likely early adopter or source of reviews.
- **What they've already tried:** StreetEasy, Facebook groups, Listings Project, Craigslist, brokers, and walk-through videos. For verification, they've used HPD, 311, Who Owns What, OpenIgloo, apartmentaudit.nyc, and talking to tenants in the hallway.

## For your brand position
- **Canonical language candidates:**
  - "look like the photos" ([link](https://www.reddit.com/r/NYCapartments/comments/1s0qkkr/stop_ai_apartments/obwveju/))
  - "the real story" ([link](https://www.reddit.com/r/AskNYC/comments/1qnk8lm/what_do_you_check_about_a_landlord_or_building/o1ztp9c/))
  - "red flags" ([link](https://www.reddit.com/r/NYCapartments/comments/1rowe4d/what_are_the_biggest_red_flags_to_look_for_when/))
  - "before signing that lease" ([link](https://www.reddit.com/r/NYCapartments/comments/1q5i34z/nyc_apartment_rental_lessons_learned_the_hard_way/))
  - "patterns not one off issues" ([link](https://www.reddit.com/r/AskNYC/comments/1qnk8lm/what_do_you_check_about_a_landlord_or_building/o1x4ksx/))
  - "talk to the previous tenant" ([link](https://www.reddit.com/r/AskNYC/comments/1qnk8lm/what_do_you_check_about_a_landlord_or_building/o1wscpb/))
  - "in one place" ([link](https://www.reddit.com/r/AskNYC/comments/1qnk8lm/what_do_you_check_about_a_landlord_or_building/o1uwnye/))
  - "hidden financial traps" ([link](https://www.reddit.com/r/NYCapartments/comments/1tqgx3c/i_wrote_a_script_to_expose_hidden_coned_and/))
  - "10-second vibe check" (a competitor's phrase, but users responded well; [link](https://www.reddit.com/r/NYCapartments/comments/1tyhs50/i_built_a_free_tool_for_renters_to_easily_spot/oq3jw6c/))
- **Language to avoid:**
  - "move-in ready" ([link](https://www.reddit.com/r/NYCapartments/comments/1s0qkkr/stop_ai_apartments/))
  - "off-market listings" ([link](https://www.reddit.com/r/NYCapartments/comments/1o1n4hp/do_not_sublet_on_facebook_in_nyc/))
  - "virtual doorman" and other inflated amenity labels ([link](https://www.reddit.com/r/NYCapartments/comments/1s2we9l/streeteasy_has_become_almost_completely_useless/))
  - Anything that sounds AI-generated. Users openly mock it: "holy ai generated" on a downvoted reply in 1upyc2j ([link](https://www.reddit.com/r/NYCapartments/comments/1upyc2j/signed_a_lease_before_viewing_in_person_got_a/ow62gtn/)), and "is this just a ChatGPT prompt" ([link](https://www.reddit.com/r/NYCapartments/comments/1tqgx3c/i_wrote_a_script_to_expose_hidden_coned_and/ooiji9x/)).
- **Objections:**
  - *Paraphrase: just see it in person.* This is the dominant community answer, with scores of 1,207 ([link](https://www.reddit.com/r/NYCapartments/comments/1o1n4hp/do_not_sublet_on_facebook_in_nyc/nihmq33/)) and 2,050 ([link](https://www.reddit.com/r/NYCapartments/comments/1s0qkkr/stop_ai_apartments/)). The pitch has to work for people who can't, or explain what touring still misses (Theme 2).
  - *Paraphrase: a broker already does this.* "This is when you NEED a broker... doing FaceTime tours" ([link](https://www.reddit.com/r/NYCapartments/comments/1o1n4hp/do_not_sublet_on_facebook_in_nyc/nihumak/)). On the other side, many threads distrust brokers.
  - *Paraphrase: just report it to StreetEasy.* "90% of them get corrected within a day or two" ([link](https://www.reddit.com/r/NYCapartments/comments/1s2we9l/streeteasy_has_become_almost_completely_useless/ocbc72g/)).
  - *Public data is incomplete or misleading.* "the complaints you see are the issues that were *reported*" ([link](https://www.reddit.com/r/NYCapartments/comments/1snmp9x/dream_apartment_rent_stabilized_bedbug_history/ogn5fm9/)).
  - *Accuracy.* "there were at least two inaccuracies" ([link](https://www.reddit.com/r/NYCapartments/comments/1tyhs50/i_built_a_free_tool_for_renters_to_easily_spot/oq6vhvp/)). One wrong fact kills trust.
  - *Privacy.* "it is bananas to give AI all of that information about yourself" ([link](https://www.reddit.com/r/NYCapartments/comments/1wlp7k2/moving_to_nyc_for_a_job_is_finding_an_apartment/pb2al7n/)).
  - *Free alternatives exist.* JustFix, OpenIgloo, apartmentaudit.nyc, and HPD Online are all free. You need a clear answer to why someone wouldn't just use those.

## Caveats
- **Possible promotion.** The update to the Facebook-sublet post praises a sublet platform ("Honestly Ohana saved my life", [link](https://www.reddit.com/r/NYCapartments/comments/1o1n4hp/do_not_sublet_on_facebook_in_nyc/)), and one AskNYC comment name-drops StreetSmart. Both read like possible astroturf. The ConEd-script post (1tqgx3c) is a self-promo, and commenters suspected it was a ChatGPT wrapper. Use those threads for the pain they describe, not as validation of the products.
- **Survivorship and loud minority.** r/NYCapartments regulars are people who made it through. The top replies to victims are harsh ("transplant who didn’t bother going in person"), which likely discourages the newcomers your product targets from posting at all.
- **Skew.** Reddit skews younger, US-based, and English-speaking. International students barely appear: r/internationalstudents returned 0 results, and the only direct mentions are second-hand (1t9lmoa, 1upyc2j). For that group, rely on your interviews, not this corpus.
- **Recency.** Everything is from October 2025 to September 2026, so the corpus is current. Several threads tie the problems to the FARE Act broker-fee change (2025). Comments also argue those problems existed "before fare act" ([link](https://www.reddit.com/r/NYCapartments/comments/1s2we9l/streeteasy_has_become_almost_completely_useless/ocbbkfh/)), so treat the causal link as contested.
- **Single-sub concentration.** 72 of 82 quotes come from r/NYCapartments.

## Coverage
- Subreddits: r/NYCapartments, r/AskNYC, r/columbia (search only: r/nyu; empty: r/internationalstudents)
- Date range: 2025-10 to 2026-09
- Threads: 20 read / 0 empty / 0 missing (plus 18 discovery searches: 17 read, 1 empty)
- Quotes in quotes.jsonl: 82 (counted by script)
- Suggested next pulls: an r/nyu or r/columbia sublet thread with comments, to get more student voice. Also search r/AskNYC for `international student apartment` to fill the international gap. Neither is required for the homework.
