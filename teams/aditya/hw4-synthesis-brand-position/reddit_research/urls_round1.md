# Reddit research, round 1: discovery searches

**Problem space:** Renting and subleasing is scattered across Facebook Marketplace, Airbnb, Craigslist, StreetEasy, school groups, and group chats. Listings are often inaccurate, scammy, or unanswered. We want one transparent, honest place to rent and sublease.

**Target user:** College students (starting with Columbia/NYC) who need a short-term sublease or a room, or who want to sublet their own place, especially without a trusted personal lead.

**Subreddits:** r/NYCapartments, r/columbia, r/nyu, r/college, r/Renters, r/Scams, r/AskNYC

Ranked by relevance. Save each page into `reddit_corpus/raw/` with the file name shown.

| # | Save as | URL |
|---|---|---|
| 1 | `nycapts_sublet_scam.json` | https://www.reddit.com/r/NYCapartments/search.json?q=sublet+scam&restrict_sr=1&sort=top&t=year&limit=50 |
| 2 | `nycapts_sublet_student.json` | https://www.reddit.com/r/NYCapartments/search.json?q=sublet+student&restrict_sr=1&sort=top&t=year&limit=50 |
| 3 | `columbia_sublet.json` | https://www.reddit.com/r/columbia/search.json?q=sublet&restrict_sr=1&sort=top&t=all&limit=50 |
| 4 | `columbia_housing.json` | https://www.reddit.com/r/columbia/search.json?q=off+campus+housing&restrict_sr=1&sort=top&t=all&limit=50 |
| 5 | `nycapts_fb_marketplace.json` | https://www.reddit.com/r/NYCapartments/search.json?q=facebook+marketplace&restrict_sr=1&sort=top&t=year&limit=50 |
| 6 | `nycapts_fake_listing.json` | https://www.reddit.com/r/NYCapartments/search.json?q=fake+listing&restrict_sr=1&sort=top&t=year&limit=50 |
| 7 | `nyu_sublet.json` | https://www.reddit.com/r/nyu/search.json?q=sublet&restrict_sr=1&sort=top&t=all&limit=50 |
| 8 | `college_sublease.json` | https://www.reddit.com/r/college/search.json?q=sublease&restrict_sr=1&sort=top&t=all&limit=50 |
| 9 | `scams_sublet.json` | https://www.reddit.com/r/Scams/search.json?q=sublet&restrict_sr=1&sort=top&t=year&limit=50 |
| 10 | `scams_rental_marketplace.json` | https://www.reddit.com/r/Scams/search.json?q=rental+facebook+marketplace&restrict_sr=1&sort=top&t=year&limit=50 |
| 11 | `renters_sublet.json` | https://www.reddit.com/r/Renters/search.json?q=sublet&restrict_sr=1&sort=top&t=year&limit=50 |
| 12 | `renters_listing_photos.json` | https://www.reddit.com/r/Renters/search.json?q=listing+photos+misleading&restrict_sr=1&sort=top&t=all&limit=50 |
| 13 | `askny_sublet.json` | https://www.reddit.com/r/AskNYC/search.json?q=sublet&restrict_sr=1&sort=top&t=year&limit=50 |
| 14 | `nycapts_roommate.json` | https://www.reddit.com/r/NYCapartments/search.json?q=finding+a+roommate&restrict_sr=1&sort=top&t=year&limit=50 |
| 15 | `nycapts_subletting_my_room.json` | https://www.reddit.com/r/NYCapartments/search.json?q=subletting+my+room&restrict_sr=1&sort=top&t=year&limit=50 |

Please open each link in your browser, save the page (File > Save Page As, or select all and paste into a file) into `reddit_corpus/raw/` with a `.json` name, and tell me when you're done.
