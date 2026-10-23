# ClientReady Reddit research round 1

**Status:** All 12 searches were manually saved and parsed: 9 nonempty, 3 zero-result listings. All 148 unique post bodies were screened locally. See `urls_round2.md` for selected comment-thread pages, which are not yet saved.

**Problem:** People assembling small websites receive long documents, images and uneven contributions, and must decide what belongs on each page. Investigate this separately from nonresponse, approval/version changes, and self-authored copy.

**Target:** Builders who collect and organize material from other people. Student cases are our starting evidence; freelance and small-studio applicability remains unverified.

## Save these manually

Log into Reddit in your own browser. Open links individually at a normal pace. Save the displayed JSON using File → Save Page As, with the unique filename shown. Do not use an automated downloader or bulk-open links. If rate limited, wait ten minutes before resuming.

Save folder: `/Users/ansonhe/Documents/Codex/2026-10-02/homework-3-interviews-due-friday-by/outputs/clientready-product/reddit_corpus/raw`

1. [r/web_design — client website content](https://www.reddit.com/r/web_design/search.json?q=client+website+content&restrict_sr=1&sort=top&t=year) — save as `r1-01-web_design.json`
2. [r/web_design — waiting client content](https://www.reddit.com/r/web_design/search.json?q=waiting+client+content&restrict_sr=1&sort=top&t=year) — save as `r1-02-web_design.json`
3. [r/web_design — content questionnaire](https://www.reddit.com/r/web_design/search.json?q=content+questionnaire&restrict_sr=1&sort=top&t=year) — save as `r1-03-web_design.json`
4. [r/freelance — website client content](https://www.reddit.com/r/freelance/search.json?q=website+client+content&restrict_sr=1&sort=top&t=year) — save as `r1-04-freelance.json`
5. [r/freelance — client copy images](https://www.reddit.com/r/freelance/search.json?q=client+copy+images&restrict_sr=1&sort=top&t=year) — save as `r1-05-freelance.json`
6. [r/webdev — client content collection](https://www.reddit.com/r/webdev/search.json?q=client+content+collection&restrict_sr=1&sort=top&t=year) — save as `r1-06-webdev.json`
7. [r/webdev — website content handoff](https://www.reddit.com/r/webdev/search.json?q=website+content+handoff&restrict_sr=1&sort=top&t=year) — save as `r1-07-webdev.json`
8. [r/smallbusiness — website content writing](https://www.reddit.com/r/smallbusiness/search.json?q=website+content+writing&restrict_sr=1&sort=top&t=year) — save as `r1-08-smallbusiness.json`
9. [r/smallbusiness — website designer content](https://www.reddit.com/r/smallbusiness/search.json?q=website+designer+content&restrict_sr=1&sort=top&t=year) — save as `r1-09-smallbusiness.json`
10. [r/web_design — content snare](https://www.reddit.com/r/web_design/search.json?q=content+snare&restrict_sr=1&sort=controversial&t=year) — save as `r1-10-web_design.json`
11. [r/freelance — client questionnaire](https://www.reddit.com/r/freelance/search.json?q=client+questionnaire&restrict_sr=1&sort=controversial&t=year) — save as `r1-11-freelance.json`
12. [r/web_design — client content](https://www.reddit.com/r/web_design/search.json?q=client+content&restrict_sr=1&sort=top&t=month) — save as `r1-12-web_design.json`

## Next round

After the human saves these searches, run the installed local ingest script and inspect the candidates. Select approximately 18–28 relevant threads with comments, emit their full `/r/<subreddit>/comments/<id>.json` links, and have the human save them. Aim for 30–100 valid saved files overall; search-result files alone are not enough. Count distinct threads, not duplicate saves. Do not fabricate thread IDs or presume a search result contains comments.

If JSON is blocked, try the normal page manually first, then JSON again. A manually saved old.reddit.com HTML thread is an allowed fallback. Never count an access-denied or empty response as research.

The class submission includes coverage, summaries and selected quotes; raw pages stay in the local product repository and are excluded from Git.
