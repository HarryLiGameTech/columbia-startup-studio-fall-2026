# Reddit research — Round 1: discovery search URLs

Topic: indoor wayfinding in unfamiliar/large buildings (primary user: college students moving between unfamiliar campus buildings under time pressure; secondary: people in large complex venues — malls, hospitals, airports, parking garages — including those coordinating pickups or accompanying mobility-limited family).

These are **search URLs only** (no thread permalinks exist yet). Ranked by expected signal: direct campus-wayfinding hits first, then entrance/time-pressure variants, then the big-venue analogs (mall/parking garage/airport) that map to the secondary user segment, then broad/meme discovery threads likely to surface cross-domain anecdotes.

Campus subs (`r/columbia`, `r/barnard`, `r/BostonU`, `r/UofT`) are run with `t=all` instead of `t=year` — these are small-to-medium, topic-specific subs where "getting lost in a building" is a rare-enough post type that a single year's window would likely return nothing. The large general subs (`r/CollegeRant`, `r/AskCollege`, `r/IKEA`, `r/mildlyinfuriating`, `r/travel`, `r/AskReddit`) keep `t=year` for the community's lasting view, since they have enough volume that a year window should still surface top posts; `r/GoogleMaps` is set to `t=all` since it's a smaller, lower-traffic sub.

1. https://www.reddit.com/r/columbia/search.json?q=cannot%20find%20classroom&restrict_sr=1&sort=top&t=all
   — Columbia-specific, directly matches the Hamilton-Hall "wrong hallway, backtracked, 4 min late" story from the team's interviews.

2. https://www.reddit.com/r/columbia/search.json?q=late%20to%20class%20lost&restrict_sr=1&sort=top&t=all
   — Columbia, time-pressure + lost framing together.

3. https://www.reddit.com/r/columbia/search.json?q=which%20entrance&restrict_sr=1&sort=top&t=all
   — Columbia, entrance/door confusion (echoes the "map says there's a door but it's locked" trust problem).

4. https://www.reddit.com/r/barnard/search.json?q=lost%20in%20building&restrict_sr=1&sort=top&t=all
   — Barnard, general lost-in-building search (one interviewee was a Barnard senior).

5. https://www.reddit.com/r/barnard/search.json?q=late%20for%20class&restrict_sr=1&sort=top&t=all
   — Barnard, time-pressure framing.

6. https://www.reddit.com/r/BostonU/search.json?q=lost%20in%20building&restrict_sr=1&sort=top&t=all
   — Boston University, general lost-in-building search (one interviewee, Steve, is a BU sophomore).

7. https://www.reddit.com/r/BostonU/search.json?q=elevator%20late%20class&restrict_sr=1&sort=top&t=all
   — BU, unpredictable indoor travel time (elevator/crowded hallway variance, echoes Tristan's "six minutes vs. twelve minutes" quote).

8. https://www.reddit.com/r/UofT/search.json?q=lost%20on%20campus&restrict_sr=1&sort=top&t=all
   — University of Toronto, chosen as a "big complex campus known for confusing buildings" sub (tunnel system, Sidney Smith building maze jokes are a known UofT meme) — not from the team's materials, a reasoned guess.

9. https://www.reddit.com/r/UofT/search.json?q=which%20entrance&restrict_sr=1&sort=top&t=all
   — UofT, entrance confusion variant.

10. https://www.reddit.com/r/CollegeRant/search.json?q=lost%20on%20campus&restrict_sr=1&sort=top&t=year
    — General college venting sub, larger/more active than any single-school sub; good for volume on the lost/late pattern.

11. https://www.reddit.com/r/CollegeRant/search.json?q=cannot%20find%20my%20classroom&restrict_sr=1&sort=top&t=year
    — Same sub, direct classroom-finding phrasing.

12. https://www.reddit.com/r/AskCollege/search.json?q=first%20day%20lost%20campus&restrict_sr=1&sort=top&t=year
    — General college Q&A sub, targets the first-week/first-day-of-classes framing called out as a key time-pressure moment.

13. https://www.reddit.com/r/IKEA/search.json?q=lost%20in%20the%20store&restrict_sr=1&sort=top&t=year
    — Mall/big-single-building analog to the secondary user segment; getting lost inside an IKEA is a well-known recurring complaint/joke, good proxy for "guessing game" indoor navigation in a huge complex building.

14. https://www.reddit.com/r/mildlyinfuriating/search.json?q=lost%20in%20parking%20garage&restrict_sr=1&sort=top&t=year
    — General gripe sub, targets the "GPS/CarPlay loses signal in underground parking garage" sub-problem.

15. https://www.reddit.com/r/mildlyinfuriating/search.json?q=confusing%20building%20signage&restrict_sr=1&sort=top&t=year
    — Same sub, targets the signage/wayfinding-trust theme across any building type (not campus-specific).

16. https://www.reddit.com/r/travel/search.json?q=lost%20in%20the%20airport&restrict_sr=1&sort=top&t=year
    — Big-venue analog: airport wayfinding/missed-gate stories, parallel to the mall-pickup scenario in the team's interviews.

17. https://www.reddit.com/r/AskReddit/search.json?q=worst%20time%20you%20got%20lost%20in%20a%20building&restrict_sr=1&sort=top&t=all
    — Broad discovery query on a huge general sub; "what's your worst getting-lost story" style threads tend to pull in cross-domain anecdotes (campus, mall, hospital, airport, office) in one place with lots of upvoted replies.

18. https://www.reddit.com/r/GoogleMaps/search.json?q=does%20not%20work%20indoors&restrict_sr=1&sort=top&t=all
    — Targets the maps-accuracy/trust theme directly ("Google Maps stops being useful once you're inside") from the people most likely to describe it precisely.

## Notes on subreddit confidence

- High confidence these exist and are active: r/columbia, r/barnard, r/CollegeRant, r/IKEA, r/mildlyinfuriating, r/travel, r/AskReddit, r/UofT.
- Less certain: **r/BostonU** (name may differ slightly, e.g. a less common variant — worth confirming it loads before relying on it), **r/AskCollege** (smaller/less active than r/CollegeRant, results may be thin), **r/GoogleMaps** (likely a small, low-traffic sub — included because it's the most direct match for the maps-accuracy theme, but may return little).
- None of these (besides columbia/barnard/BostonU) came from the team's materials — they are reasoned guesses per the playbook (lively, specific communities; big-campus subs known for confusing buildings; communities where indoor navigation / malls / airports / signage frustration naturally come up).

## File naming convention

Save each page into `reddit_corpus/raw/` using this pattern, so files map back to the numbered list above:

```
r1_<2-digit-index>_<subreddit>_<short-topic>.json
```

Examples:
- `r1_01_columbia_cant-find-classroom.json`
- `r1_08_uoft_lost-on-campus.json`
- `r1_17_askreddit_worst-lost-story.json`

Please open each link in your browser, save the page (File > Save Page As, or select all and paste into a file) into `reddit_corpus/raw/` with a `.json` name, and tell me when you're done.
