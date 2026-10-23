# Reddit research: student subleasing and renting in NYC

**Team:** Aditya · **Problem space:** one transparent, honest place to rent and sublease, replacing the scatter across Facebook groups and Marketplace, Craigslist, Listings Project, Airbnb, and StreetEasy · **Target user:** college students (starting with Columbia and NYC) who need a short-term sublet or room, or who want to sublet their own place

## What we found

People don't say the hard part is *finding* listings. They say it's *telling which ones are real*. That came up in 10 separate threads across all six subreddits, and it's the strongest finding. Close behind are three connected problems: people can't see a place before they have to pay; they're asked to pay in ways that offer no protection (Zelle, wire, money orders); and real listers either never answer or get flooded with replies. Students and interns get hit hardest, because they are out of town, need exact dates, and need 3 to 4 month terms that leasing offices won't offer. The corpus covers r/NYCapartments, r/Scams, r/AskNYC, r/nyu, r/columbia, and r/college, mostly from 2025 to 2026 (62 of 68 quotes). Theme counts come from `quotes.jsonl` (see Coverage).

## Themes

### 1. "Which ones are real": telling real listings from scams
- {q0}
- {q1}
- {q2}
- {q8}
- {q9}
- {q5}
- {q6}
- {q10}
- {q11}
- Shows up in 10 separate threads across r/NYCapartments, r/Scams, r/AskNYC, r/nyu, r/columbia, and r/college, which makes it the strongest pattern in the corpus. It matches 4 of our 5 housing interviews (Ruby, Emma, Marcus, Jasmine).

### 2. You can't see it before you pay
- {q12}
- {q14}
- {q15}
- {q18}
- {q16}
- {q17}
- Shows up in 5 threads. Community advice is firm: see it in person or don't rent. The people asking can't do that, because they're out-of-town students and interns or their parents. The advice and the need contradict each other, and our product sits in that gap.

### 3. Paying with no protection
- {q22}
- {q20}
- {q21}
- {q23}
- {q24}
- {q25}
- Shows up in 3 threads. Note the exchange in the fake-manager thread: one person says a money order is a red flag, and the next asks "why? how should you pay?" People know what's unsafe but don't know what safe looks like.

### 4. Nobody answers, or everyone answers
- {q26}
- {q27}
- {q28}
- {q30}
- {q31}
- {q32}
- Shows up in 4 threads. This is a two-sided problem. Seekers get ghosted while listers are buried in messages. It matches Marcus from our interviews ("half of them never answered").

### 5. The search is scattered across too many places
- {q33}
- {q34}
- {q35}
- {q36}
- Shows up in 3 threads. One poster already built an aggregator for this exact problem (see Objections). Being scattered is real but secondary: a top reply to that same post says the real problem is trust, not finding listings.

### 6. Trust comes from people you know
- {q37}
- {q38}
- {q40}
- {q41}
- {q42}
- {q43}
- Shows up in 5 threads. People trust school-gated groups, word of mouth, and mutual friends. When those are missing ("no mutual friends… not much of a digital footprint"), people don't know how to verify someone. This matches Jasmine and Tina from our interviews.

### 7. Is the sublet even allowed?
- {q44}
- {q45}
- {q46}
- {q47}
- Shows up in 3 threads. Calling the building to confirm the tenant exists is what exposed the scam in the internship thread. "Is this person actually the tenant, and allowed to sublet?" is a check people already do by hand.

### 8. Subletters need honest people too
- {q48}
- {q49}
- {q50}
- {q51}
- Shows up in 2 threads (a smaller pattern). The supply side worries about squatters and unreliable subletters, and some say outright that they'd prefer students.

### 9. Students need exact dates and short terms
- {q52}
- {q53}
- {q54}
- {q55}
- {q56}
- Shows up in 3 threads. Short terms (summer, internship, a semester, before student housing opens) are where students both save the most and take the most risk.

## For your personas

- **Out-of-town intern or incoming grad student.** Never been to NYC, needs about 3 months, can't tour in person, and knows they're "a prime target for scams" (theme 2: {q12}). They've tried the university portal and Facebook groups. They worry deals are "suspiciously good." Often a parent is involved in the search (two threads are posted by parents: [1rndpst](https://www.reddit.com/r/Scams/comments/1rndpst/how_to_protect_against_rental_scams_for_remote/), [1vk68ol](https://www.reddit.com/r/Scams/comments/1vk68ol/us_nyc_sublet_too_good_to_be_true/)).
- **Current student who needs a short sublet in NYC.** Already in the city and messaging lots of listers, but gets ghosted and is surrounded by scams (theme 1: {q3}). Has tried Ohana, Craigslist, Airbnb, and Facebook groups. Wants a summer or semester room near campus and the right dates with a friend (theme 9: {q52}).
- **Parent helping a student.** Pays or co-pays, reads Reddit, and checks with the landlord. They're nervous because they can't see the place (theme 2: {q14}).
- **Student or young renter subletting out their own room.** Wants a reliable, respectful subletter, preferably a student, and is overwhelmed by replies (themes 4 and 8: {q50}, {q31}).

## For your brand position

**Canonical language candidates** (words users actually use):
- "which ones are real" ({q0})
- "legit" ({q8})
- "sus" / "sketch" ({q62}; {q9})
- "sight unseen" ({q16})
- "red flag" ({q23})
- "zero protections" ({q21})
- "a full time job" ({q33})
- "mutual friends" ({q41})
- "allowed to rent the room out" ({q46})
- "reliable, honest sub letter" ({q48})

**Language to avoid** (words users mock or distrust):
- "refundable deposit" framing: {q63}
- Sob stories and over-reassurance: {q64}
- "Too good to be true" excitement and urgency: {q67}
- Calling a few days' stay a "sublet": {q65}
- Calling an Airbnb-style service something else: {q66}
- Leading with "virtual tour" as proof: {q17}

**Objections** (reasons people give for not trying a solution):
- "Another aggregator": {q57}
- "Airbnb already protects me": {q58}; {q59}
- "Verification by ID means nothing": {q60}
- "Aggregated data isn't accurate": {q61}
- "Facebook-sourced listings are sus even inside a good tool": {q62}
- "Just don't rent sight unseen": {q16}

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
