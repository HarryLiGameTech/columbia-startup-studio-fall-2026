# Reddit research, round 2: threads

Picked from the 13 round-1 searches: relevant to student subletting, trust, and search pain, then ranked by comment count. The ingest script's own suggestions were off-topic (security cameras, Canadian law), so they are not used.

Save each into `reddit_corpus/raw/` with the name shown (Downloads is fine; Claude moves them).

| # | Theme | Save as | URL | Thread |
|---|---|---|---|---|
| 1 | Students | `t_columbia_1cpwev9.json` | https://www.reddit.com/r/columbia/comments/1cpwev9.json | Incoming Grad Student - is Off-Campus Housing Marketplace Reliable? |
| 2 | Students | `t_nyu_1onrwz9.json` | https://www.reddit.com/r/nyu/comments/1onrwz9.json | where do nyu students find housing/post sublets |
| 3 | Students | `t_columbia_1r5zu9i.json` | https://www.reddit.com/r/columbia/comments/1r5zu9i.json | housing question! PLZ HELP |
| 4 | Students | `t_columbia_1k1ntg6.json` | https://www.reddit.com/r/columbia/comments/1k1ntg6.json | When to start looking for off-campus housing? |
| 5 | Students | `t_nyu_1q1be9k.json` | https://www.reddit.com/r/nyu/comments/1q1be9k.json | NYU Apartment vs Airbnb |
| 6 | Students | `t_scams_1rndpst.json` | https://www.reddit.com/r/Scams/comments/1rndpst.json | How to protect against rental scams for remote internship? |
| 7 | Competitor idea | `t_nycapartments_1o4bou1.json` | https://www.reddit.com/r/NYCapartments/comments/1o4bou1.json | Rental and sublet aggregator (someone built a version of our idea) |
| 8 | Sublet trust | `t_scams_1vk68ol.json` | https://www.reddit.com/r/Scams/comments/1vk68ol.json | [US] NYC Sublet - Too Good to be True? |
| 9 | Sublet trust | `t_scams_1vm1uc3.json` | https://www.reddit.com/r/Scams/comments/1vm1uc3.json | Is this a sublet scam? |
| 10 | Sublet trust | `t_nycapartments_1wrcqru.json` | https://www.reddit.com/r/NYCapartments/comments/1wrcqru.json | Does this Manhattan sublet sound legit or should we be worried? |
| 11 | Sublet trust | `t_nycapartments_1pjtbcb.json` | https://www.reddit.com/r/NYCapartments/comments/1pjtbcb.json | I think I was scammed by a fake apartment manager in NYC |
| 12 | Sublet trust | `t_scams_1qhaawg.json` | https://www.reddit.com/r/Scams/comments/1qhaawg.json | [US] Housing application scam |
| 13 | Sublet trust | `t_renters_1wmukcf.json` | https://www.reddit.com/r/Renters/comments/1wmukcf.json | [NY] I found photos of the inside of my apartment on a real estate listing |
| 14 | Search pain | `t_nycapartments_1synk84.json` | https://www.reddit.com/r/NYCapartments/comments/1synk84.json | how i found my nyc apartment in may 2026 post-FARE act |
| 15 | Search pain | `t_asknyc_1vnjm4d.json` | https://www.reddit.com/r/AskNYC/comments/1vnjm4d.json | Best way to go about finding a sublet these days? |
| 16 | Search pain | `t_nycapartments_1sjxv1c.json` | https://www.reddit.com/r/NYCapartments/comments/1sjxv1c.json | Looking for a 1bed-1bath. Why the hell is it so difficult. |
| 17 | Search pain | `t_nycapartments_1u7ufvs.json` | https://www.reddit.com/r/NYCapartments/comments/1u7ufvs.json | How do people actually find apartments in Harlem? We keep getting ignored |
| 18 | Subletter side | `t_asknyc_1r5gvmn.json` | https://www.reddit.com/r/AskNYC/comments/1r5gvmn.json | Anyone who've successfully sublet out their own rental apartments? |
| 19 | Subletter side | `t_nycapartments_1ow4lyn.json` | https://www.reddit.com/r/NYCapartments/comments/1ow4lyn.json | Subletting my room in LES STARTING DEC/JAN |
| 20 | Subletter side | `t_asknyc_1vaad6h.json` | https://www.reddit.com/r/AskNYC/comments/1vaad6h.json | Why do people sublet their apartment for 5 days? |

**Redo from round 1** (came back empty or duplicated):

21. `nycapts_fake_listing.json`: https://www.reddit.com/r/NYCapartments/search.json?q=fake+listing&restrict_sr=1&sort=top&t=year&limit=50
22. `nycapts_roommate.json`: https://www.reddit.com/r/NYCapartments/search.json?q=finding+a+roommate&restrict_sr=1&sort=top&t=year&limit=50

Please open each link in your browser, save the page (File > Save Page As, or select all and paste into a file) into `reddit_corpus/raw/` with a `.json` name, and tell me when you're done.
