#!/usr/bin/env python3
"""Fill {qN} placeholders in summary_template.md with quotes from quotes.jsonl (line N),
so every quote in the summary is the verified verbatim text with its link."""
import json, os, re
from datetime import datetime
HERE = os.path.dirname(os.path.abspath(__file__))
Q = [json.loads(l) for l in open(os.path.join(HERE, "..", "quotes.jsonl"))]
def fmt(i):
    r = Q[i]
    when = datetime.strptime(r["date"], "%Y-%m").strftime("%b %Y")
    return f"\"{r['quote']}\" {r['subreddit']}, {when} ([link]({r['permalink']}))"
src = open(os.path.join(HERE, "summary_template.md")).read()
out = re.sub(r"\{q(\d+)\}", lambda m: fmt(int(m.group(1))), src)
open(os.path.join(HERE, "..", "reddit_research_summary.md"), "w").write(out)
print("rendered", len(re.findall(r"\{q\d+\}", src)), "quotes")
