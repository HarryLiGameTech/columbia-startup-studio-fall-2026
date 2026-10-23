# Reddit research: student subleasing and renting in NYC

**Team:** Aditya · **Problem space:** one transparent, honest place to rent and sublease, replacing the scatter across Facebook groups and Marketplace, Craigslist, Listings Project, Airbnb, and StreetEasy · **Target user:** college students (starting with Columbia and NYC) who need a short-term sublet or room, or who want to sublet their own place

## What we found

People don't say the hard part is *finding* listings. They say it's *telling which ones are real*. That came up in 10 separate threads across all six subreddits, and it's the strongest finding. Close behind are three connected problems: people can't see a place before they have to pay; they're asked to pay in ways that offer no protection (Zelle, wire, money orders); and real listers either never answer or get flooded with replies. Students and interns get hit hardest, because they are out of town, need exact dates, and need 3 to 4 month terms that leasing offices won't offer. The corpus covers r/NYCapartments, r/Scams, r/AskNYC, r/nyu, r/columbia, and r/college, mostly from 2025 to 2026 (62 of 68 quotes). Theme counts come from `quotes.jsonl` (see Coverage).

## Themes

### 1. "Which ones are real": telling real listings from scams
- "the hardest part of subletting in nyc was never finding listings, it's figuring out which ones are real" r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1o4bou1/_/oe8t3vv/))
- "half the photos are stolen from streeteasy and the person wants you to wire a deposit before you even see the place" r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1o4bou1/_/oe8t3vv/))
- "why are 95% of facebook group housing posts scams" r/nyu, May 2025 ([link](https://www.reddit.com/r/nyu/comments/1kmxk6o/why_are_95_of_facebook_group_housing_posts_scams/))
- "Are these all legit? They all look newly renovated and clean. Or just like craiglist, are there scams at OCHA?" r/columbia, May 2021 ([link](https://www.reddit.com/r/columbia/comments/nl3sok/is_off_campus_housing_portal_ocha_legit/))
- "The FB groups are a it sketch" r/college, Mar 2024 ([link](https://www.reddit.com/r/college/comments/1beb8hf/internship_housing/))
- "I also beg everyone to stay off Facebook marketplace and craigslist because there’s a 1% chance you find anything real." r/NYCapartments, Dec 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1pjtbcb/_/ntgsz53/))
- "Doubly true for shit on Craigslist - that’s scammer central now." r/Scams, Aug 2026 ([link](https://www.reddit.com/r/Scams/comments/1vk68ol/_/p2r2mlk/))
- "this one didn’t seem clear to me until I had engaged with “her” for quite a while" r/Scams, Mar 2026 ([link](https://www.reddit.com/r/Scams/comments/1rndpst/_/o98f00r/))
- "A good trick i found for checking for scams has been a simple reverse image search" r/NYCapartments, May 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1synk84/_/ok6mv08/))
- Shows up in 10 separate threads across r/NYCapartments, r/Scams, r/AskNYC, r/nyu, r/columbia, and r/college, which makes it the strongest pattern in the corpus. It matches 4 of our 5 housing interviews (Ruby, Emma, Marcus, Jasmine).

### 2. You can't see it before you pay
- "have never been to NYC before; as such, I fear I am a prime target for scams" r/columbia, May 2024 ([link](https://www.reddit.com/r/columbia/comments/1cpwev9/incoming_grad_student_is_offcampus_housing/))
- "It is too far away to just swing by for a visit." r/Scams, Mar 2026 ([link](https://www.reddit.com/r/Scams/comments/1rndpst/how_to_protect_against_rental_scams_for_remote/))
- "my question is how do you arrange that over the internet without being at risk of being scammed?" r/Scams, Mar 2026 ([link](https://www.reddit.com/r/Scams/comments/1rndpst/_/o9646h6/))
- "I got lit up by people saying I shouldn’t sign anything even if there was a video tour offered and that I have to do it in person." r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1synk84/_/oixhxmw/))
- "Never rent a place in New York sight unseen, period." r/Scams, Aug 2026 ([link](https://www.reddit.com/r/Scams/comments/1vk68ol/_/p2r228e/))
- "Virtual tour = scam." r/Scams, Aug 2026 ([link](https://www.reddit.com/r/Scams/comments/1vm1uc3/_/p360ouk/))
- Shows up in 5 threads. Community advice is firm: see it in person or don't rent. The people asking can't do that, because they're out-of-town students and interns or their parents. The advice and the need contradict each other, and our product sits in that gap.

### 3. Paying with no protection
- "He told me I was approved, made me sign a lease, and asked for a USPS money order for the deposit." r/NYCapartments, Dec 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1pjtbcb/i_think_i_was_scammed_by_a_fake_apartment_manager/))
- "Zelle is only for people you are already face to face with." r/Scams, Aug 2026 ([link](https://www.reddit.com/r/Scams/comments/1vk68ol/_/p2r7cbr/))
- "Triply true for Zelle, which has zero protections." r/Scams, Aug 2026 ([link](https://www.reddit.com/r/Scams/comments/1vk68ol/_/p2r3sko/))
- "A money order for the deposit is a huge red flag" r/NYCapartments, Dec 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1pjtbcb/_/ntl26bo/))
- "why? how should you pay?" r/NYCapartments, Dec 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1pjtbcb/_/ntl7b3e/))
- "I would use a payment app that gives you the ability to send the money as a purchase as opposed to as a gift." r/Scams, Mar 2026 ([link](https://www.reddit.com/r/Scams/comments/1rndpst/_/o965cql/))
- Shows up in 3 threads. Note the exchange in the fake-manager thread: one person says a money order is a red flag, and the next asks "why? how should you pay?" People know what's unsafe but don't know what safe looks like.

### 4. Nobody answers, or everyone answers
- "For any long, legitimate sublets, or for actual rentals, it's impossible to get a reply." r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1synk84/_/oiwwd74/))
- "Tried out listings project but no one returns my emails." r/AskNYC, Aug 2026 ([link](https://www.reddit.com/r/AskNYC/comments/1vnjm4d/best_way_to_go_about_finding_a_sublet_these_days/))
- "In many cases nobody responds at all." r/NYCapartments, Jun 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1u7ufvs/how_do_people_actually_find_apartments_in_harlem/))
- "the few people I’ve reached out to haven’t responded" r/nyu, May 2025 ([link](https://www.reddit.com/r/nyu/comments/1kmxk6o/why_are_95_of_facebook_group_housing_posts_scams/))
- "I listed my own room last week and I got over 40 replies." r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1synk84/_/oixfqfa/))
- "She said she listed on fb marketplace also but was bombarded by messages" r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1synk84/_/oj0fsu0/))
- Shows up in 4 threads. This is a two-sided problem. Seekers get ghosted while listers are buried in messages. It matches Marcus from our interviews ("half of them never answered").

### 5. The search is scattered across too many places
- "It really is a full time job trying to find a place in NYC." r/NYCapartments, Oct 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1o4bou1/rental_and_sublet_aggregator/))
- "The fact you can't filter through this pages was annoying." r/NYCapartments, Oct 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1o4bou1/rental_and_sublet_aggregator/))
- "even more spammy than craigslist and difficult to sort the posts by date posted" r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1synk84/how_i_found_my_nyc_apartment_in_may_2026_postfare/))
- "Where do students usually post short term leases for 4/8-month terms? is there some kind of discord server?" r/nyu, Nov 2025 ([link](https://www.reddit.com/r/nyu/comments/1onrwz9/where_do_nyu_students_find_housingpost_sublets/))
- Shows up in 3 threads. One poster already built an aggregator for this exact problem (see Objections). Being scattered is real but secondary: a top reply to that same post says the real problem is trust, not finding listings.

### 6. Trust comes from people you know
- "they require your uni to join the group" r/columbia, May 2024 ([link](https://www.reddit.com/r/columbia/comments/1cpwev9/_/l3nugjb/))
- "word of mouth - i posted on IG a bunch just asking people if they knew of anything opening up." r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1synk84/how_i_found_my_nyc_apartment_in_may_2026_postfare/))
- "That's how wide you have to network haha" r/NYCapartments, Jun 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1u7ufvs/_/os4sdce/))
- "Maybe if you have mutual friends on Facebook?" r/NYCapartments, Sep 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1wrcqru/_/pcbgvv2/))
- "We also don’t have any mutual friends, so there isn’t really much of a digital footprint for me to verify." r/NYCapartments, Sep 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1wrcqru/_/pck58kd/))
- "My sister's friend's little sister works for a startup at USF that does student subleasing." r/college, Mar 2024 ([link](https://www.reddit.com/r/college/comments/1beb8hf/internship_housing/))
- Shows up in 5 threads. People trust school-gated groups, word of mouth, and mutual friends. When those are missing ("no mutual friends… not much of a digital footprint"), people don't know how to verify someone. This matches Jasmine and Tina from our interviews.

### 7. Is the sublet even allowed?
- "We plan to confirm with the landlord organization that she’s a renter there & her permission to sublease." r/Scams, Mar 2026 ([link](https://www.reddit.com/r/Scams/comments/1rndpst/how_to_protect_against_rental_scams_for_remote/))
- "they said they have no tenant by that name and that the apartment number she gave me doesn’t exist in the building" r/Scams, Mar 2026 ([link](https://www.reddit.com/r/Scams/comments/1rndpst/_/o97rcxu/))
- "my bigger concern is whether she’s actually allowed to rent the room out in the first place" r/NYCapartments, Sep 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1wrcqru/_/pck0v34/))
- "as soon as he leased the unit, he began posing as the "owner" and was subleasing the unit out" r/NYCapartments, Dec 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1pjtbcb/_/nti53va/))
- Shows up in 3 threads. Calling the building to confirm the tenant exists is what exposed the scam in the internship thread. "Is this person actually the tenant, and allowed to sublet?" is a check people already do by hand.

### 8. Subletters need honest people too
- "worried about finding a reliable, honest sub letter for my rent stabilized apartment" r/AskNYC, Mar 2026 ([link](https://www.reddit.com/r/AskNYC/comments/1r5gvmn/_/odeuqif/))
- "The only risk of this is the subletter becoming a squatter and refusing to leave once u come back" r/AskNYC, Feb 2026 ([link](https://www.reddit.com/r/AskNYC/comments/1r5gvmn/_/o5m9eoq/))
- "(Preferably college students / 20 somethings)" r/NYCapartments, Nov 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1ow4lyn/subletting_my_room_in_les_starting_decjan/))
- "I was wondering if I should’ve even bothered trying Reddit!" r/NYCapartments, Nov 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1ow4lyn/_/nonjd9k/))
- Shows up in 2 threads (a smaller pattern). The supply side worries about squatters and unreliable subletters, and some say outright that they'd prefer students.

### 9. Students need exact dates and short terms
- "The only thing i’m worried about with subletting is that i won’t be able to get the right dates and/or my roommate won’t be able to live with me" r/nyu, Jan 2026 ([link](https://www.reddit.com/r/nyu/comments/1q1be9k/_/nx4ts04/))
- "She’s only going to be there for 3 months and can’t afford to spend her summer in a hotel." r/Scams, Mar 2026 ([link](https://www.reddit.com/r/Scams/comments/1rndpst/_/o95yc6j/))
- "it’s basically impossible to lease a furnished apartment for only 3 months from a leasing company, it needs to be a sublet from a longer term renter." r/Scams, Mar 2026 ([link](https://www.reddit.com/r/Scams/comments/1rndpst/how_to_protect_against_rental_scams_for_remote/))
- "need to find a place to sublet for a few months before moving into student housing" r/Scams, Aug 2026 ([link](https://www.reddit.com/r/Scams/comments/1vm1uc3/is_this_a_sublet_scam/))
- "you can 1000% sublet a room for half that" r/nyu, Jan 2026 ([link](https://www.reddit.com/r/nyu/comments/1q1be9k/_/nx4bx4y/))
- Shows up in 3 threads. Short terms (summer, internship, a semester, before student housing opens) are where students both save the most and take the most risk.

## For your personas

- **Out-of-town intern or incoming grad student.** Never been to NYC, needs about 3 months, can't tour in person, and knows they're "a prime target for scams" (theme 2: "have never been to NYC before; as such, I fear I am a prime target for scams" r/columbia, May 2024 ([link](https://www.reddit.com/r/columbia/comments/1cpwev9/incoming_grad_student_is_offcampus_housing/))). They've tried the university portal and Facebook groups. They worry deals are "suspiciously good." Often a parent is involved in the search (two threads are posted by parents: [1rndpst](https://www.reddit.com/r/Scams/comments/1rndpst/how_to_protect_against_rental_scams_for_remote/), [1vk68ol](https://www.reddit.com/r/Scams/comments/1vk68ol/us_nyc_sublet_too_good_to_be_true/)).
- **Current student who needs a short sublet in NYC.** Already in the city and messaging lots of listers, but gets ghosted and is surrounded by scams (theme 1: "facebook groups: it’s been almost entirely scammers, and only one person has even replied back to me." r/nyu, May 2025 ([link](https://www.reddit.com/r/nyu/comments/1kmxk6o/why_are_95_of_facebook_group_housing_posts_scams/))). Has tried Ohana, Craigslist, Airbnb, and Facebook groups. Wants a summer or semester room near campus and the right dates with a friend (theme 9: "The only thing i’m worried about with subletting is that i won’t be able to get the right dates and/or my roommate won’t be able to live with me" r/nyu, Jan 2026 ([link](https://www.reddit.com/r/nyu/comments/1q1be9k/_/nx4ts04/))).
- **Parent helping a student.** Pays or co-pays, reads Reddit, and checks with the landlord. They're nervous because they can't see the place (theme 2: "It is too far away to just swing by for a visit." r/Scams, Mar 2026 ([link](https://www.reddit.com/r/Scams/comments/1rndpst/how_to_protect_against_rental_scams_for_remote/))).
- **Student or young renter subletting out their own room.** Wants a reliable, respectful subletter, preferably a student, and is overwhelmed by replies (themes 4 and 8: "(Preferably college students / 20 somethings)" r/NYCapartments, Nov 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1ow4lyn/subletting_my_room_in_les_starting_decjan/)), "I listed my own room last week and I got over 40 replies." r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1synk84/_/oixfqfa/))).

## For your brand position

**Canonical language candidates** (words users actually use):
- "which ones are real" ("the hardest part of subletting in nyc was never finding listings, it's figuring out which ones are real" r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1o4bou1/_/oe8t3vv/)))
- "legit" ("Are these all legit? They all look newly renovated and clean. Or just like craiglist, are there scams at OCHA?" r/columbia, May 2021 ([link](https://www.reddit.com/r/columbia/comments/nl3sok/is_off_campus_housing_portal_ocha_legit/)))
- "sus" / "sketch" ("and the fb posts but i personally find them sus" r/NYCapartments, Oct 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1o4bou1/_/pek5k6n/)); "The FB groups are a it sketch" r/college, Mar 2024 ([link](https://www.reddit.com/r/college/comments/1beb8hf/internship_housing/)))
- "sight unseen" ("Never rent a place in New York sight unseen, period." r/Scams, Aug 2026 ([link](https://www.reddit.com/r/Scams/comments/1vk68ol/_/p2r228e/)))
- "red flag" ("A money order for the deposit is a huge red flag" r/NYCapartments, Dec 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1pjtbcb/_/ntl26bo/)))
- "zero protections" ("Triply true for Zelle, which has zero protections." r/Scams, Aug 2026 ([link](https://www.reddit.com/r/Scams/comments/1vk68ol/_/p2r3sko/)))
- "a full time job" ("It really is a full time job trying to find a place in NYC." r/NYCapartments, Oct 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1o4bou1/rental_and_sublet_aggregator/)))
- "mutual friends" ("Maybe if you have mutual friends on Facebook?" r/NYCapartments, Sep 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1wrcqru/_/pcbgvv2/)))
- "allowed to rent the room out" ("my bigger concern is whether she’s actually allowed to rent the room out in the first place" r/NYCapartments, Sep 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1wrcqru/_/pck0v34/)))
- "reliable, honest sub letter" ("worried about finding a reliable, honest sub letter for my rent stabilized apartment" r/AskNYC, Mar 2026 ([link](https://www.reddit.com/r/AskNYC/comments/1r5gvmn/_/odeuqif/)))

**Language to avoid** (words users mock or distrust):
- "refundable deposit" framing: "Refundable "If you decide to cancel", so what the heck is the deposit for lol..." r/Scams, Aug 2026 ([link](https://www.reddit.com/r/Scams/comments/1vm1uc3/_/p369a1h/))
- Sob stories and over-reassurance: "The sob story about the wife, offered up totally unprompted, is another red flag." r/Scams, Aug 2026 ([link](https://www.reddit.com/r/Scams/comments/1vm1uc3/_/p360a0s/))
- "Too good to be true" excitement and urgency: "They want people to get excited over the opportunity so they'll send money without thinking it through" r/Scams, Aug 2026 ([link](https://www.reddit.com/r/Scams/comments/1vk68ol/_/p2rwe46/))
- Calling a few days' stay a "sublet": "five days is not a sublet…just pay your rent!" r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1synk84/_/oj4uobg/))
- Calling an Airbnb-style service something else: "They even have a "World Cup Rentals" section that is basically Airbnb by another name." r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1synk84/_/oiwwd74/))
- Leading with "virtual tour" as proof: "Virtual tour = scam." r/Scams, Aug 2026 ([link](https://www.reddit.com/r/Scams/comments/1vm1uc3/_/p360ouk/))

**Objections** (reasons people give for not trying a solution):
- "Another aggregator": "We get a new one every year." r/NYCapartments, Oct 2025 ([link](https://www.reddit.com/r/NYCapartments/comments/1o4bou1/_/nj17hmc/))
- "Airbnb already protects me": "Keep all messaging and payment on Airbnb, and if something goes wrong they'll find her another place to stay and pay for it." r/Scams, Mar 2026 ([link](https://www.reddit.com/r/Scams/comments/1rndpst/_/o96uewo/)); "If you want some measure of security and a contract, pay for a real Airbnb." r/NYCapartments, Sep 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1wrcqru/_/pcejerq/))
- "Verification by ID means nothing": "There is no way you can validate any ID. So what’s the point in receiving a copy of someone’s ID?" r/Scams, Aug 2026 ([link](https://www.reddit.com/r/Scams/comments/1vm1uc3/_/p36kg4s/))
- "Aggregated data isn't accurate": "I wouldn't trust it. Its not very accurate." r/NYCapartments, Apr 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1synk84/_/oizk4hv/))
- "Facebook-sourced listings are sus even inside a good tool": "and the fb posts but i personally find them sus" r/NYCapartments, Oct 2026 ([link](https://www.reddit.com/r/NYCapartments/comments/1o4bou1/_/pek5k6n/))
- "Just don't rent sight unseen": "Never rent a place in New York sight unseen, period." r/Scams, Aug 2026 ([link](https://www.reddit.com/r/Scams/comments/1vk68ol/_/p2r228e/))

## Caveats

- **Who uses Reddit.** Reddit skews younger, male, and technical. It's a fair match for students, but our Columbia-specific voice is thin. r/columbia mostly contributed older posts (2021 and 2024); most of the student voice comes from r/nyu, r/college, and NYC-wide subs.
- **Selection bias toward scams.** We searched r/Scams and terms like "scam" and "fake listing" on purpose, so this corpus over-represents bad experiences. People who found a sublet easily through a friend (like Tina in our interviews) rarely post.
- **Several posts aren't from NYC students.** Some threads are from parents, travelers, or students elsewhere (UCSD, an MIT intern in SF). We used them because the problem is the same, not because the person matches our target user exactly.
- **Low-score comments.** Several quotes have scores of 1 to 5. They are real but weren't widely upvoted. Higher-signal quotes (score 20+) are in themes 1 to 3.
- **One competitor-builder voice.** The aggregator thread's original poster is promoting their own tool, so we quote replies to it rather than treating the post as user sentiment.

## Coverage

- **Subreddits:** r/NYCapartments, r/Scams, r/AskNYC, r/nyu, r/columbia, r/college. r/Renters was searched but contributed no quotes (mostly non-NYC landlord disputes).
- **Date range of quotes:** May 2021 to October 2026 (62 of 68 from 2025 to 2026).
- **Threads:** 15 read / 0 empty / 5 missing (lower priority, skipped). Plus 15 searches read. 30 files and 437 comments in total. See `coverage.md`.
- **Quotes in quotes.jsonl:** 68, all verbatim and checked against the saved pages by `scripts/build_quotes.py`.
- **Suggested next pulls:** r/columbia threads 1r5zu9i and 1k1ntg6, for more Columbia-specific voice, and r/Renters 1wmukcf (real apartment photos reused in a fake listing).
