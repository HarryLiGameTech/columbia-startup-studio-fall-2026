# Reddit research, round 1: discovery URLs

## What this round is for

We are testing the "Claude Daycare" idea: letting a coding agent do autonomous side activities while the user protects the Claude Pro or Max usage they need for real work. This round is discovery only. It should show how people describe hitting usage limits, how they budget or protect usage, what they do (and fear) when agents run unattended, what surprises them about cost, whether they read agent logs or summaries, and whether anyone runs agents just for fun.

Answers used for the three opening questions (the human was not asked, these were supplied in the task):
1. Problem space: Claude Code users on a limited subscription want autonomous side activities but worry about spending usage they need for real work.
2. Target user: Claude Pro or Max subscribers who rely on Claude Code for coursework, freelance work, side projects or a job, and who watch their usage limit.
3. Known subreddits: none.

## Subreddits chosen

Caveat: I may not touch Reddit, so I could not verify that any of these exist, are active, or allow search in the way I expect. They are chosen from general knowledge of large, well-known communities. If a link returns nothing, the subreddit name or its activity is the first thing to check.

- r/ClaudeAI: the main general community for Claude; the most likely place for plan, limit and pricing complaints and comparisons.
- r/ClaudeCode: a community focused on Claude Code itself; the most likely place for unattended runs, overnight agents, subagents and usage-burn stories.
- r/vibecoding: a large community of people building with AI agents, many of them hobbyists, students and side-project builders; good for fun uses and for how non-professionals handle limits.
- r/ChatGPTCoding: a large AI-coding community that compares tools; useful for how people talk about Claude Code limits next to alternatives.
- r/cursor: a large community for another agentic coding tool; useful for how people talk about usage caps and agent cost outside the Claude world, as a contrast.

## URLs to open (ranked by likely relevance)

1. https://www.reddit.com/r/ClaudeCode/search.json?q=budget%20usage%20limit&restrict_sr=1&sort=top&t=year - how people ration or protect their allowance for important work
2. https://www.reddit.com/r/ClaudeCode/search.json?q=weekly%20limit&restrict_sr=1&sort=top&t=year - the weekly limit: how it feels, what people do about it
3. https://www.reddit.com/r/ClaudeCode/search.json?q=session%20limit&restrict_sr=1&sort=top&t=year - hitting the session limit mid-task and the workarounds people use
4. https://www.reddit.com/r/ClaudeAI/search.json?q=claude%20code%20usage%20limit&restrict_sr=1&sort=top&t=year - the broader Claude audience on Claude Code limits, plan comparisons
5. https://www.reddit.com/r/ClaudeCode/search.json?q=overnight&restrict_sr=1&sort=top&t=year - people running agents overnight: what for, and what went right or wrong
6. https://www.reddit.com/r/ClaudeCode/search.json?q=unattended&restrict_sr=1&sort=top&t=year - unattended or autonomous runs and the safeguards people mention
7. https://www.reddit.com/r/ClaudeAI/search.json?q=dangerously%20skip%20permissions&restrict_sr=1&sort=top&t=year - safety attitudes toward letting the agent act without approval (sandboxes, fears, horror stories)
8. https://www.reddit.com/r/ClaudeCode/search.json?q=burned%20through%20usage&restrict_sr=1&sort=top&t=month - recent surprise usage drain from agent runs
9. https://www.reddit.com/r/ClaudeAI/search.json?q=unexpected%20usage&restrict_sr=1&sort=top&t=year - surprise or hidden usage and cost, and how people found out
10. https://www.reddit.com/r/ClaudeCode/search.json?q=subagents%20usage&restrict_sr=1&sort=top&t=year - whether subagents and parallel agents eat the allowance faster than expected
11. https://www.reddit.com/r/ClaudeCode/search.json?q=agent%20logs&restrict_sr=1&sort=top&t=year - whether people read agent logs, and how they track what the agent did
12. https://www.reddit.com/r/ClaudeAI/search.json?q=summary%20of%20what%20claude%20did&restrict_sr=1&sort=top&t=year - appetite for summaries or reports of agent work, and what format people want
13. https://www.reddit.com/r/vibecoding/search.json?q=claude%20usage%20limit&restrict_sr=1&sort=top&t=year - how hobbyists and students cope with Claude limits
14. https://www.reddit.com/r/vibecoding/search.json?q=agent%20overnight&restrict_sr=1&sort=top&t=year - fun or experimental unattended agent runs among hobbyists
15. https://www.reddit.com/r/ChatGPTCoding/search.json?q=claude%20code%20limits&restrict_sr=1&sort=top&t=year - cross-tool view: do limits push people to other tools
16. https://www.reddit.com/r/cursor/search.json?q=usage%20limits%20agent&restrict_sr=1&sort=top&t=year - contrast: how another agent tool's users talk about caps and surprise cost
17. https://www.reddit.com/r/ClaudeCode/search.json?q=side%20project%20for%20fun&restrict_sr=1&sort=top&t=year - hobbyist and playful uses of a coding agent
18. https://www.reddit.com/r/ClaudeAI/search.json?q=weekly%20limit&restrict_sr=1&sort=controversial&t=year - minority and voted-down views on limits (people who say limits are fine, or that complaining is overblown)

## How to open them

Open the links one at a time at a normal pace, while logged in to Reddit, and do not open them all in a burst. If a page comes back empty or says "too many requests", wait 10 minutes and try again.

Please open each link in your browser, save the page (File > Save Page As, or select all and paste into a file) into `reddit_corpus/raw/` with a `.json` name, and tell me when you're done.
