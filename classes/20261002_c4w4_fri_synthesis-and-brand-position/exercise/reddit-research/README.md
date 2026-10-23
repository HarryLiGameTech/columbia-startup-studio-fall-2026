# Reddit research agent

A Claude Code agent that helps your team hear real users in their own words before you build synthetic personas or write landing page copy.

## What it does

Your 10 interviews are a small sample of people you found and who were polite to you. Reddit has thousands of people describing the same problems, unprompted, to each other. This agent:

1. Suggests subreddits and searches for your problem space.
2. Gives you a list of Reddit links to save.
3. Reads the pages you saved and pulls out themes, with exact quotes and a link for every quote.
4. Writes a summary with sections for your personas and your brand position: words users actually use, words they mock, and the objections they raise.

## The one thing to know: you fetch, the agent reads

Reddit blocks bots and AI agents. If the agent tries to load Reddit itself, it fails every time. So the work is split:

- **The agent** writes a numbered list of Reddit links ending in `.json`.
- **You** open each link in your own browser and save the page into a folder called `reddit_corpus/raw/` in your project. (In Chrome or Firefox: open the link, then File > Save Page As, and keep the `.json` name.)
- **The agent** reads the files you saved and tells you what to fetch next.

Two or three rounds of 10 to 20 links is plenty for this class. Open the links at a normal pace. Opening dozens of tabs at once gets you rate limited, and the saved pages come back empty.

If a link shows an "access denied" page from your network (school Wi-Fi or a VPN), open the normal thread page first (the same link without `.json`), let it load, then try the `.json` link again. If that still fails, save the `old.reddit.com` version of the thread as HTML; the agent can read that too.

## Install it in Claude Code

1. In your team's project folder, make a folder called `.claude/agents/` if it isn't there.
2. Copy `reddit-researcher.md` into it: `.claude/agents/reddit-researcher.md`.
3. Copy `scripts/reddit_json_ingest.py` into your project too (for example, `scripts/reddit_json_ingest.py`). The agent runs it to clean up the pages you save. It needs only Python 3, no installs.
4. Start Claude Code in that folder and say: "Use the reddit-researcher agent to research [your problem space] for [your target user]."

Not using Claude Code? Give any model with file access the contents of `reddit-researcher.md` as its instructions. The fetch-and-save step is the same.

## How it feeds the rest of homework 4

- **Personas.** Use what the threads say about people's situations, constraints, and what they've already tried to ground your synthetic persona buckets.
- **Brand position.** Real phrases from users are candidates for canonical language. Words they mock go in language to avoid.
- **Copy.** Headlines that use words your users already say tend to land. Objections from the threads are your objection-handling section.

Reddit is not your audience, exactly. It skews younger, male, and technical, and the people in a subreddit are the ones who stayed. Treat it as a second source next to your interviews, not a replacement.

## What to hand in

Put these in `teams/your-team-name/hw4-synthesis-brand-position/reddit_research/`:

1. **The corpus list:** the threads you saved (the `urls_round*.md` files or `coverage.md`, with links).
2. **The agent's summary:** `reddit_research_summary.md`.
3. **3 to 5 quotes you used:** exact words, each with its link, and where you used it (a persona, your brand position's canonical language, or a line of copy). A short `quotes_used.md` is fine.

Don't hand in the raw saved pages. They're large and add nothing for the grader.

## Files in this folder

- `reddit-researcher.md`: the agent
- `scripts/reddit_json_ingest.py`: turns saved pages into clean files and suggests the next links to fetch
