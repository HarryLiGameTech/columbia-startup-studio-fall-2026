# Reddit research — Round 3 (optional, minimal)

**Status: skipped by the team.** The corpus already had 31 saved files; none of the links below were fetched.

Per the instructions for this round: no new guessed searches (round 2's guessed searches mostly came back dead — see `coverage.md`), only post IDs that already appear in the saved data. I checked the ingest script's "Suggested next .json URLs" output and did a regex scan of every normalized post/comment body in the corpus for `reddit.com/r/.../comments/...` links. That turned up two kinds of leads:

- A large pile of dead ends: `r/AskReddit` megathread remnants (people linking to other giant unrelated AskReddit threads from inside the 2014/2016 "best of" megathreads we already read), a UofT "toilet paper" joke thread, a UofT professor-email meme thread, a `r/GoogleMaps` fuel-efficient-routing idea, and a crosspost-bot notice duplicating a thread we already have. None of these are plausibly about indoor wayfinding — I did not include them.
- Exactly one genuinely promising lead, plus one weak one, both linked from the BU "Incoming Student Guide" post we already have (`r_BostonU_comments_1mtml9c`).

Given that only one strong candidate turned up — not enough to justify a full round, and consistent with round 2's lesson that most derived leads are dead ends — this is a short, optional list rather than a full round 3. Fetch it only if you want one more data point; skipping it entirely is reasonable too.

1. https://www.reddit.com/r/BostonU/comments/1677git.json
   — "The biggest adjustment for an incoming BU student" — linked from the Incoming Student Guide. "Biggest adjustment" threads on college subs often surface wayfinding/orientation complaints among the top answers (homesickness, workload, etc. are also likely). Medium priority — the only real lead from this pass.

2. https://www.reddit.com/r/BostonU/comments/1lihmnf.json
   — "Incoming student course registration is tomorrow" — also linked from the same guide. Title suggests this is about registration mechanics, not navigation. Low priority / likely off-topic — include only for completeness.

**File naming convention:** `r3_01_bostonu_biggest-adjustment.json`, `r3_02_bostonu_registration-tomorrow.json`.

Please open each link in your browser, save the page (File > Save Page As, or select all and paste into a file) into `reddit_corpus/raw/` with a `.json` name, and tell me when you're done — or tell me to skip this round and move straight to finalizing the write-up.
