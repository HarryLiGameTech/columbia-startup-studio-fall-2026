# Reddit collection — Round 1: discovery searches

**Status:** Links prepared; no pages collected or verified yet.

Scope: SAT students’ experiences starting practice, phone distraction, and attempts to manage it. Broader communities provide secondary context, not direct SAT audience evidence.

Save destination: `reddit_corpus/raw/`

## Save manually

1. Log into Reddit in your own browser.
2. Open one link at a time, at a normal pace.
3. Check that the page contains JSON data, not a login, blocked, or rate-limit page.
4. Choose File → Save Page As (Command-S on Mac). Keep the `.json` extension and use the filename below.
5. Save to the destination above. In the macOS save dialog, Command-Shift-G lets you paste the folder path.
6. If saving the displayed JSON does not work, copy the complete JSON text into a plain-text file with the same `.json` filename. Do not save rich text.
7. If rate limited, wait 10 minutes before resuming. Do not automate opening or downloading links.

These are discovery search files, not the 30 distinct thread files we will collect next. Empty results and blocked pages must not be counted as usable evidence.

## First batch

1. [r/Sat: phone distraction](https://www.reddit.com/r/Sat/search.json?q=phone+distraction&restrict_sr=1&sort=top&t=year) — save as `search_01_sat_phone.json`

2. [r/Sat: procrastination](https://www.reddit.com/r/Sat/search.json?q=procrastination&restrict_sr=1&sort=top&t=year) — save as `search_02_sat_procrastination.json`

3. [r/Sat: start studying](https://www.reddit.com/r/Sat/search.json?q=start+studying&restrict_sr=1&sort=top&t=year) — save as `search_03_sat_start.json`

4. [r/Sat: study routine](https://www.reddit.com/r/Sat/search.json?q=study+routine&restrict_sr=1&sort=top&t=year) — save as `search_04_sat_routine.json`

5. [r/GetStudying: phone](https://www.reddit.com/r/GetStudying/search.json?q=phone&restrict_sr=1&sort=top&t=year) — save as `search_05_getstudying_phone.json`

6. [r/GetStudying: too tired](https://www.reddit.com/r/GetStudying/search.json?q=too+tired&restrict_sr=1&sort=top&t=year) — save as `search_06_getstudying_tired.json`

7. [r/GetStudying: short sessions](https://www.reddit.com/r/GetStudying/search.json?q=short+sessions&restrict_sr=1&sort=top&t=year) — save as `search_07_getstudying_short.json`

8. [r/digitalminimalism: app blockers](https://www.reddit.com/r/digitalminimalism/search.json?q=app+blockers&restrict_sr=1&sort=top&t=year) — save as `search_08_digitalminimalism_blockers.json`

9. [r/digitalminimalism: screen time](https://www.reddit.com/r/digitalminimalism/search.json?q=screen+time&restrict_sr=1&sort=top&t=year) — save as `search_09_digitalminimalism_screentime.json`

10. [r/productivity: blocking apps studying](https://www.reddit.com/r/productivity/search.json?q=blocking+apps+studying&restrict_sr=1&sort=top&t=year) — save as `search_10_productivity_blockers.json`

## After saving

Tell the assistant which files are saved. It will inspect the local files, report missing or invalid pages, and select relevant thread URLs with comments for the next round. No thread URLs will be invented from the search terms.

Keep all raw files locally. The class README asks for the corpus list, summary, and selected quotes rather than raw pages in the class repository; retain the raw files so they can be supplied if the TA requests access.

Class instructions: https://github.com/kenxle/columbia-startup-studio-fall-2026/blob/main/classes/20261002_c4w4_fri_synthesis-and-brand-position/exercise/reddit-research/README.md
