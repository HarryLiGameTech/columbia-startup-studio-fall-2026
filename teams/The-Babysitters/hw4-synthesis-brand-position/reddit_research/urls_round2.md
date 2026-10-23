# Reddit research, round 2, batch A: threads to save in full

Picked on 2026-10-11 from the two search pages already in `reddit_corpus/raw/` (L01 is the "overnight" search in r/ClaudeCode; L02 is an r/ClaudeCode limits search, most likely link 2, "weekly limit"). The listings only hold each post's own text, so these threads still need their comments saved.

**How the picks were made, and what is not known.** I chose from titles, post text, score and comment count. I have not read any comments, so each "why" below is a guess about what the thread will hold, not a finding. The picks lean toward what Allowance Guardrails is about (protecting usage for real work while an agent runs unattended, surprise usage, wanting to see what happened). Two gaps to close in later batches: none of these was picked for arguing against the idea (the minority-view search, link 18, is meant to supply that), and I have not checked who the posters are, so if hobbyists and students matter, the r/vibecoding searches (links 13 and 14) are where they should show up.

**How to save each one.** Open the link in your own Chrome (logged in), wait for the text to load, press Cmd+A then Cmd+C. With the watcher running (`python3 -I scripts/watch_clipboard_reddit.py`) it files the page by itself. Or press Cmd+S and run `python3 -I scripts/collect_reddit_downloads.py` afterwards. Do not paste threads into chat: a big thread can be several megabytes.

Each link asks for up to 500 comments, sorted by top.

## A. Protecting the allowance vs unattended work
1. https://www.reddit.com/r/ClaudeCode/comments/1vw5muy/how_do_you_get_claude_to_code_overnight.json?sort=top&limit=500
   - How do you get Claude to code overnight? - 322 points, 178 comments, r/ClaudeCode, 1vw5muy
   - Why: The poster wants to code overnight but says their plan does not last the week if they do. Asks how others do it.
2. https://www.reddit.com/r/ClaudeCode/comments/1x1esxn/attention_heavy_ai_users.json?sort=top&limit=500
   - ATTENTION HEAVY AI USERS - 954 points, 323 comments, r/ClaudeCode, 1x1esxn
   - Why: An overnight run reportedly used a bit over half of the weekly usage in about a day. A runaway-usage story.
3. https://www.reddit.com/r/ClaudeCode/comments/1wo5eaw/is_this_a_new_feature_in_cc.json?sort=top&limit=500
   - Is this a new feature in CC? - 26 points, 28 comments, r/ClaudeCode, 1wo5eaw
   - Why: The poster hit the 5-hour limit, left the computer on, and found the work finished overnight. Surprise that it continued.

## B. Trust and safeguards for unattended runs
4. https://www.reddit.com/r/ClaudeCode/comments/1uxa0xw/5_months_running_a_oneman_saas_on_claude_code.json?sort=top&limit=500
   - 5 months running a one-man SaaS on Claude Code: what stuck and what I turned off - 107 points, 32 comments, r/ClaudeCode, 1uxa0xw
   - Why: Overnight sessions on scoped jobs, a ping when the agent needs the person, deploys held for the morning.
5. https://www.reddit.com/r/ClaudeCode/comments/1wjjqsv/claude_code_ran_a_backgrounded_command_that.json?sort=top&limit=500
   - Claude Code ran a backgrounded command that deleted my entire Windows user folder overnight - 166 points, 113 comments, r/ClaudeCode, 1wjjqsv
   - Why: A backgrounded command allegedly deleted a whole user folder overnight. The fear behind leaving agents alone.

## C. Seeing what the agent did or is doing
6. https://www.reddit.com/r/ClaudeCode/comments/1u3ffo4/i_never_know_if_my_overnight_claude_code_runs_are.json?sort=top&limit=500
   - I never know if my overnight Claude Code runs are stuck or just thinking, so I built a desk screen that shows  - 31 points, 25 comments, r/ClaudeCode, 1u3ffo4
   - Why: Cannot tell if an overnight run is stuck or thinking, so built a desk screen. Wants a glance, not logs.
7. https://www.reddit.com/r/ClaudeCode/comments/1takxpl/clawdmeter_a_small_esp32_usage_limit_monitor.json?sort=top&limit=500
   - Clawdmeter - a small ESP32 usage limit monitor (source code in description) - 2087 points, 114 comments, r/ClaudeCode, 1takxpl
   - Why: A small hardware usage-limit monitor. Evidence that people build their own meters.

## D. Limit anxiety and constantly checking
8. https://www.reddit.com/r/ClaudeCode/comments/1uv6ns4/dear_anthropic_this_has_to_stop.json?sort=top&limit=500
   - Dear Anthropic, This Has to STOP. - 2732 points, 558 comments, r/ClaudeCode, 1uv6ns4
   - Why: A long complaint that the limits and credits make using the service a constant source of stress.
9. https://www.reddit.com/r/ClaudeCode/comments/1wqagzu/claude_added_graceful_stopping_point_in_new_update.json?sort=top&limit=500
   - Claude added graceful stopping point in new update - 2614 points, 105 comments, r/ClaudeCode, 1wqagzu
   - Why: Praise for a new 'graceful stopping point' feature, said to help in the middle of an important task. The screenshot is not in the saved data, so what it stops at (the limit?) is a guess; the comments should say.

## E. Not knowing what the allowance really is
10. https://www.reddit.com/r/ClaudeCode/comments/1s7ilti/what_does_20x_usage_actually_mean_i_measured_it.json?sort=top&limit=500
   - what does "20x usage" actually mean? i measured it. $363 per 5 hours. - 128 points, 59 comments, r/ClaudeCode, 1s7ilti
   - Why: Someone measured what '20x usage' means in dollars per window. Shows people cannot see the number.
11. https://www.reddit.com/r/ClaudeCode/comments/1w38v98/claude_max_20x_only_applies_to_the_5hour_window.json?sort=top&limit=500
   - Claude Max “20x” only applies to the 5-hour window. Weekly usage on the $200 plan is 2x the $100 plan - 1775 points, 224 comments, r/ClaudeCode, 1w38v98
   - Why: Claims Max 20x applies to the 5-hour window but weekly usage is only about 2x the cheaper plan.

## F. Surprise cost and usage jumps
12. https://www.reddit.com/r/ClaudeCode/comments/1uxzjry/hit_my_limit_yesterday_caved_and_bought_50_credit.json?sort=top&limit=500
   - Hit my limit yesterday, caved and bought $50 credit, and no joke, Fable spent the entire $50 on the first prom - 921 points, 494 comments, r/ClaudeCode, 1uxzjry
   - Why: Bought $50 of credit and says one prompt spent all of it without finishing.
13. https://www.reddit.com/r/ClaudeCode/comments/1wurd3e/mmmkay_i_didnt_believe_others_at_first_but.json?sort=top&limit=500
   - Mmmkay. I didn't believe others at first, but something is suddenly off with Opus 5.5 - 1147 points, 531 comments, r/ClaudeCode, 1wurd3e
   - Why: Reports that the model's behavior and token use changed suddenly, with usage going from about 70% to 90% in an hour.

## Not picked yet, and why

- Humor and meme posts with no text (for example 1u1jphj, 5,476 points) were skipped: there is no allowance content to quote, though the comments may hold some.
- Showcase posts for tools (Codeman, Night Watch) were skipped for now; they are people selling a tool, which is a different kind of evidence than someone describing their own problem.
- 1t5hs98 ("Doubled Rate Limits", 824 comments) is a candidate for the dissent side if the minority-view search is thin.
