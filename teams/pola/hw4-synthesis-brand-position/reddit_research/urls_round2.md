# Reddit research — Round 2

Round 1 showed that bare "lost" queries mostly return lost-and-found items, emotional "feeling lost" posts, or (on huge subs) sort=top megathreads — see `coverage.md`. Round 2 therefore leans on the handful of genuinely on-topic threads Round 1 did surface (all comment counts, so **thread URLs** first), plus **refined search URLs** that drop bare "lost" in favor of more specific phrasing, building nicknames, and a couple of new venues (hospitals, airport gates).

## Thread URLs (fetch these first — ranked by relevance, then comment count)

1. https://www.reddit.com/r/UofT/comments/10qithd.json
   — "Got lost wandering around campus" (score 513, 22 comments). Most direct hit from Round 1: a literal getting-lost-on-campus post.

2. https://www.reddit.com/r/mildlyinfuriating/comments/1uxfar3.json
   — "Too many people ask if this is the office" (487, **277 comments**). Cross-domain (office, not campus) but huge comment thread specifically about confusing building/door signage — likely rich in "why isn't this labeled better" voice for the signage-trust theme.

3. https://www.reddit.com/r/UofT/comments/4m28gv.json
   — "Why isn't there a system of underground tunnels beneath U of T" (71, 33 comments). About unpredictable travel time between buildings and wanting a better way to get across a big campus — adjacent to the "sometimes 6 min, sometimes 12 min" theme.

4. https://www.reddit.com/r/UofT/comments/1soqb6v.json
   — "id like to apologize to the person i gave the absolute worst directions to" (92, 14 comments). Wrong-directions / trust-in-directions story, told from the direction-giver's side — useful for the "if it's wrong once, I stop trusting it" theme.

5. https://www.reddit.com/r/UofT/comments/xpda1i.json
   — "What door do we use to access the G.S.U. Pub? One sign says... the other seems to reference the first door" (11, 12 comments). Direct, literal entrance-signage confusion.

6. https://www.reddit.com/r/UofT/comments/8hhbp7.json
   — "To all those a little lost" — referenced by a Round-1 result ("To all those a little scared...") as the original post it follows up on. Not yet in the corpus; title suggests it may be directly about campus disorientation. Worth confirming.

7. https://www.reddit.com/r/UofT/comments/t58ppq.json
   — "Which UofT buildings have elevators and accessible entrances?" (5, 3 comments). Low volume but directly hits the accessibility/mobility-limited-user angle (secondary user segment).

8. https://www.reddit.com/r/UofT/comments/d09ad5.json
   — "Hey first years: GET LOST!" (147, 24 comments). Lower priority: an advice post encouraging first-years to explore campus on purpose, not a pain-point account, but may have comments describing real disorientation during that exploration.

## Refined search URLs (new phrasing — avoids bare "lost")

9. https://www.reddit.com/r/columbia/search.json?q=%22wrong%20building%22&restrict_sr=1&sort=top&t=all
   — Columbia, exact-phrase "wrong building."

10. https://www.reddit.com/r/columbia/search.json?q=%22wrong%20hallway%22&restrict_sr=1&sort=top&t=all
    — Columbia, exact-phrase "wrong hallway" (closest wording to Maya's own account).

11. https://www.reddit.com/r/barnard/search.json?q=%22wrong%20building%22&restrict_sr=1&sort=top&t=all
    — Barnard, refined retry of missing #4.

12. https://www.reddit.com/r/barnard/search.json?q=%22which%20floor%22&restrict_sr=1&sort=top&t=all
    — Barnard, refined retry of missing #5 (different angle: floor-level confusion).

13. https://www.reddit.com/r/BostonU/search.json?q=%22wrong%20building%22&restrict_sr=1&sort=top&t=all
    — BU, exact-phrase retry (Round 1's "lost in building" was swamped by lost-and-found posts).

14. https://www.reddit.com/r/UofT/search.json?q=%22Sidney%20Smith%22%20maze&restrict_sr=1&sort=top&t=all
    — UofT, targeted at a specific known building: Sidney Smith Hall has a longstanding student reputation as a maze. A guess, but a well-targeted one.

15. https://www.reddit.com/r/UofT/search.json?q=Robarts%20maze&restrict_sr=1&sort=top&t=all
    — UofT, same logic for Robarts Library, also known among students for a confusing layout.

16. https://www.reddit.com/r/CollegeRant/search.json?q=%22wrong%20building%22&restrict_sr=1&sort=top&t=year
    — CollegeRant, refined (Round 1's "lost on campus"/"classroom" queries there were 0/25 and 0/2 on-topic).

17. https://www.reddit.com/r/AskCollege/search.json?q=%22first%20week%22%20lost&restrict_sr=1&sort=top&t=year
    — AskCollege, refined retry of missing #12.

18. https://www.reddit.com/r/GoogleMaps/search.json?q=indoor%20navigation&restrict_sr=1&sort=top&t=all
    — GoogleMaps, refined retry of missing #18 (dropped the exact "does not work indoors" phrase, which may have been too narrow for a small sub).

19. https://www.reddit.com/r/nursing/search.json?q=%22patients%20get%20lost%22&restrict_sr=1&sort=top&t=year
    — New venue: hospital wayfinding from staff's point of view (matches the "large complex venue" secondary segment — hospitals). Unproven sub for this topic, worth one try.

20. https://www.reddit.com/r/travel/search.json?q=%22wrong%20gate%22&restrict_sr=1&sort=top&t=year
    — Refined airport angle (Round 1's "lost in the airport" was 0/25 on-topic; "wrong gate" targets the same missed-flight-from-confusion story more precisely).

## Notes

- Thread URLs 1–8 are the full-subreddit-path form per the never-fetch contract (`https://www.reddit.com/r/<sub>/comments/<post-id>.json`), not the bare `/comments/<id>.json` form.
- `r/nursing` (#19) is a new, unverified-for-this-topic subreddit — flagged as a guess, same caveat as `r/GoogleMaps`.
- If #6 (`8hhbp7`) turns out to be off-topic or empty, that's useful information too — it tells us the "scared"/"lost" UofT post series is more about social anxiety than physical navigation.

Please open each link in your browser, save the page (File > Save Page As, or select all and paste into a file) into `reddit_corpus/raw/` with a `.json` name, and tell me when you're done.

**File naming convention:** `r2_<2-digit-index>_<subreddit>_<short-topic>.json`, matching the numbers above, e.g.:
- `r2_01_uoft_got-lost-wandering-campus.json`
- `r2_09_columbia_wrong-building.json`
- `r2_19_nursing_patients-get-lost.json`

## Round 2 additions (#21–24)

Added after several Round 2 searches came back dead (0-byte saves for #9 and #20; most exact-phrase searches unsaved or returning nothing). Each ID below was taken from a post already present in the saved corpus, and its text was checked for on-topic content before listing.

21. https://www.reddit.com/r/UofT/comments/3kfgle.json
    — "Hey First Years: GET LOST!" (21 comments, 2015-09). Original of thread #8: advice to walk your routes before classes start; mentions dead ends and a building shortcut that "shaves 3 minutes off of your walk".

22. https://www.reddit.com/r/UofT/comments/klylv.json
    — "Suggestion for first year students: GET LOST!" (30 comments, 2011-09). Same author's earlier version, with a different comment section. Old: date-tag any quotes.

23. https://www.reddit.com/r/BostonU/comments/1f7w0n3.json
    — "30 Signs You're A Freshman (or a transfer student) at BU" (39 comments, 2024-09). Recent first-year experience; includes "You lost your wallet while looking for your classes on the first day."

24. https://www.reddit.com/r/GoogleMaps/comments/8qkx62.json
    — "Is the accuracy of Google Indoor Maps bad?" (2 comments, 2018-06). Small, but the only thread directly on indoor-map accuracy, the strongest trust theme from the interviews.

Spare if one of these is dead: https://www.reddit.com/r/UofT/comments/jr7tpn.json — "Help! I've Been Following Robarts' Directional Arrows for Four Hours!" (3 comments, 2020-11), a satire piece about the library's one-way arrows.
