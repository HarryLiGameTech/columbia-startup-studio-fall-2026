# Coverage

## Round 1 (search URLs, from urls_round1.md)

Each line: result count returned / how many of those results were actually on-topic (indoor wayfinding, confusing buildings/entrances, unpredictable indoor travel time, signage/maps-indoors trust, big-venue getting lost — not "lost item" or "feeling emotionally lost") after reading title + selftext.

1. `r/columbia` "cannot find classroom" — **read**, 3 results, 0 on-topic (Love Letter to Columbia, Prezbo emails).
2. `r/columbia` "late to class lost" — **read**, 25 results, 0 on-topic. "Lost in the crowd" looked promising but is about feeling academically overwhelmed, not navigation. Rest is campus-politics/advice/academic-struggle posts.
3. `r/columbia` "which entrance" — **read**, 3 results, 0 on-topic (Hamilton Hall occupation statement — political, not wayfinding; party-scene question; sublet listing).
4. `r/barnard` "lost in building" — **missing** (never saved).
5. `r/barnard` "late for class" — **missing** (never saved).
6. `r/BostonU` "lost in building" — **read**, 25 results, 0 on-topic. Reddit matched "lost" almost entirely as **lost-and-found physical items** (lost ID, lost hydroflask, lost AirPods, etc.), not people getting lost.
7. `r/BostonU` "elevator late class" — **read**, 25 results, 0 on-topic at the time, **revised to 1 on-topic** after a round-2 keyword sweep (see Round 2 summary below): the "Incoming Student Guide" post in this result set has a line telling incoming students to walk their schedule in advance to avoid first-day classroom stress.
8. `r/UofT` "lost on campus" — **read**, 25 results, **2 on-topic**: "Got lost wandering around campus" (score 513, 22 comments); "Why isn't there a system of underground tunnels beneath U of T" (71, 33 comments — travel-time-between-buildings complaint). 3 more are tangential ("Hey first years: GET LOST!" reposts — advice to explore campus on purpose, not a pain-point account, but may contain relevant comments).
9. `r/UofT` "which entrance" — **read**, 25 results, **3 on-topic**: "id like to apologize to the person i gave the absolute worst directions to" (92, 14 comments — wrong-directions/trust theme); "What door do we use to access the G.S.U. Pub? One sign says... the other... seems to reference the first door" (11, 12 comments — direct entrance-signage confusion); "Which UofT buildings have elevators and accessible entrances?" (5, 3 comments — accessibility/entrance). 1 tangential: "To all those a little scared..." references an earlier post "To all those a little lost" (id `8hhbp7`) not yet in the corpus — flagged for round 2.
10. `r/CollegeRant` "lost on campus" — **read**, 23 results, 0 on-topic ("lost" used only in the emotional/academic-struggle sense: dropping out, failing classes, loneliness).
11. `r/CollegeRant` "cannot find my classroom" — **read**, 2 results, 0 on-topic.
12. `r/AskCollege` "first day lost campus" — **missing** (never saved).
13. `r/IKEA` "lost in the store" — **read**, 16 results, 0 on-topic. Matched almost entirely on "lost [furniture] parts/screws," not getting lost while shopping.
14. `r/mildlyinfuriating` "lost in parking garage" — **read**, 25 results, 0 on-topic. Matched "parking garage" generally; all results are neighbor/HOA parking disputes, not GPS/wayfinding-in-a-garage stories.
15. `r/mildlyinfuriating` "confusing building signage" — **read**, 13 results, **1 on-topic (cross-domain, tangential)**: "Too many people ask if this is the office" (487, 277 comments — door/signage confusion at a building entrance, large comment thread). 1 weak/borderline: "Confusing Bin Labels" at a university building (23, 20 comments) — about trash labeling, not wayfinding; excluded.
16. `r/travel` "lost in the airport" — **read**, 25 results, 0 on-topic. All trip reports and lost-luggage/lost-passport stories; none about getting lost finding a gate/exit.
17. `r/AskReddit` "worst time you got lost in a building" — **read**, 25 results, 0 on-topic. Entirely dominated by r/AskReddit's own all-time megathreads (best-of-year winners, mod announcements, unrelated viral AskReddit posts) — the broad query + `sort=top&t=all` on a huge sub surfaced sub-level virality, not the search topic.
18. `r/GoogleMaps` "does not work indoors" — **missing** (never saved).

**Summary:** 14/18 search URLs fetched, 4 missing (#4, #5, #12, #18). Of ~285 total search results read, only ~6 were clearly on-topic (all in `r/UofT`) plus 1 strong cross-domain tangential result (`r/mildlyinfuriating`). Root cause: "lost" is dominated on Reddit by (a) lost-and-found physical items, (b) "feeling lost" emotionally/academically, and (c) sub-level megathreads at `sort=top&t=all`. Round 2 drops bare "lost" queries in favor of more specific phrases ("wrong building," "wrong hallway," building-specific nicknames, etc.) — see `urls_round2.md`.

Normalized corpus: all 14 raw files parsed successfully by `reddit_json_ingest.py` into `reddit_corpus/normalized/` (255 unique post records; these are search-listing records with post metadata only, no comments, since search.json does not return comments — comments will come from the round 2 thread `.json` pulls).

## Round 2 (threads + searches, from urls_round2.md plus #21-24 added when forwarding to the human)

Every comment in each thread below was read. "On-topic" = contributed at least one quote to `quotes.jsonl`.

1. `r/UofT` 10qithd "Got lost wandering around campus" — **read**, 22 comments, **0 on-topic**. The title is misleading: the whole thread is an inside joke about the Rotman business building/students, not a literal getting-lost account.
2. `r/mildlyinfuriating` 1uxfar3 "Too many people ask if this is the office" — **read**, 196 comments (listing metadata says 277; the gap is deleted/removed comments and un-expanded "more" nodes), **5 on-topic quotes**. Cross-domain (an auto-repair-shop office door, not a campus building) but directly about entrance/signage confusion and the embarrassment of asking.
3. `r/UofT` 4m28gv "Why isn't there a system of underground tunnels beneath U of T" — **read**, 33 comments, **2 on-topic quotes**. The post itself is a satirical "let's build it ourselves" rant; most comments are jokes, but it contains a genuine complaint about weather/travel-time variance and one real data point about tunnel-connected buildings at UTSC.
4. `r/UofT` 1soqb6v "worst directions I gave" — **read**, 13 comments, **3 on-topic quotes**. Direct wrong-directions/trust story, plus a strong parallel anecdote (a grandma misdirected inside an airport terminal) and a reply confirming the confusion is repeated ("I did this this semester too").
5. `r/UofT` xpda1i "which door GSU Pub" — **read**, 14 comments, **1 on-topic quote**. Literal entrance-signage confusion, compounded by posted hours not matching reality.
6. `r/UofT` 8hhbp7 "To all those a little lost..." — **read**, 39 comments, **0 on-topic**. Confirmed: this is "lost" in the emotional/academic sense (a GPA/mental-health advice post about surviving first year), not physical navigation.
7. `r/UofT` t58ppq "Which UofT buildings have elevators and accessible entrances?" — **read**, 4 comments, **1 on-topic quote** (from the post itself). The comments are just a link to a resource site, no further personal account.
8. `r/UofT` d09ad5 "Hey first years: GET LOST! (2019 repost)" — **read**, 23 comments, **4 on-topic quotes**: campus-shortcut complexity, tunnels mattering in winter, and a counter-finding that a plain campus map is "good enough" for some students.
9. `r/columbia` "wrong building" search — **empty** (0 bytes, page failed to load).
10. `r/columbia` "wrong hallway" search — **missing** (never saved).
11. `r/barnard` "wrong building" search (retry) — **missing** (never saved).
12. `r/barnard` "which floor" search (retry) — **missing** (never saved).
13. `r/BostonU` "wrong building" search — **read**, 1 result, **0 on-topic**. The one hit ("Misdelivered mail: Jubaida M?") matched because a package was left at the wrong building — not a person getting lost.
14. `r/UofT` "Sidney Smith maze" search — **missing** (never saved).
15. `r/UofT` "Robarts maze" search — **read**, 1 result, **1 on-topic**: "Help! I've Been Following Robarts' Directional Arrows for Four Hours!" — a satirical post linking to an external satire site (boundarynews.com), 0 comments. Treated as evidence that "Robarts is a maze" is a widespread enough campus joke to be satirized, not as a literal personal account — flagged accordingly in quotes.jsonl's theme notes.
16. `r/CollegeRant` "wrong building" search — **missing** (never saved).
17. `r/AskCollege` "first week lost" search (retry) — **missing** (never saved).
18. `r/GoogleMaps` "indoor navigation" search — **read**, 3 results: `8qkx62` (on-topic, see #24), `1h5eyur` "How to create Indoor Maps?" (tangential — a building administrator, not a navigating user, asking how to build indoor maps; still corroborates the underlying problem), `mgftk8` (off-topic — about Google's fuel-efficient driving routes, matched the search only incidentally).
19. `r/nursing` "patients get lost" search — **missing** (never saved).
20. `r/travel` "wrong gate" search — **empty** (0 bytes, page failed to load).
21. `r/UofT` 3kfgle "Hey First Years: GET LOST! (2015 original)" — **read**, 22 comments, **2 on-topic quotes**: a multi-hour self-navigated detour through steam tunnels, and a mention of a building directory/kiosk (digital, Kinect-operated).
22. `r/UofT` klylv "Suggestion for first year students: GET LOST! (2011 original)" — **read**, 34 comments, **3 on-topic quotes**: time pressure undercutting the "get lost on purpose" advice, "maps/streetview can't see inside buildings," and GPS apps being an unreliable substitute for learned routes.
23. `r/BostonU` 1f7w0n3 "30 Signs You're a Freshman at BU (2024)" — **read**, 39 comments, **1 on-topic quote** (from the post's numbered list: losing a wallet while looking for class on the first day). The comment thread itself is entirely BU-slang trivia (pronunciation of "CAS," building nicknames), no further wayfinding content.
24. `r/GoogleMaps` 8qkx62 "Is the accuracy of Google Indoor Maps bad? (2018)" — **read**, 2 comments, **1 on-topic quote** (from the post; an informal accuracy poll, not a personal story — one reply says accuracy is "a few steps off").

**Round 2 summary:** 17 of 24 URLs produced content (12 full threads + 3 search files with results); 2 came back empty (network-side failures, not Reddit blocks); 7 were never saved, all guessed searches on subreddits/phrasings that round 1 had already shown were low-yield (barnard, AskCollege, CollegeRant, nursing, and the "Sidney Smith maze" guess) — consistent with round 2's broader finding that guessed searches are much lower-yield than following an on-topic thread's own comments. Of 12 full comment threads read end-to-end, 10 contributed at least one quote; the UofT "Rotman meme" thread and the "To all those a little lost" mental-health thread contributed none despite promising titles.

**Keyword re-sweep of the full normalized corpus (255 search-listing posts from both rounds):** before finalizing quotes.jsonl, ran a local regex sweep (wrong building/floor/entrance/door, elevator, wheelchair/accessible, maze, tunnel, indoor map, signage, parking garage, "lost on the first day," etc.) across every normalized selftext and comment body to check for on-topic posts missed during the manual round-1/round-2 read. This surfaced exactly one addition: the BU "Incoming Student Guide" post (`r_BostonU_comments_1mtml9c`, found via search URL #7, "elevator late class") advises incoming students to walk their class schedule in advance "to prevent stress on the first day(s)" — added to quotes.jsonl under `first_week_fades`. Everything else the sweep flagged was either already in quotes.jsonl or a false positive (e.g. a Columbia "general advice" post that mentions elevators only in the context of holding doors open).
