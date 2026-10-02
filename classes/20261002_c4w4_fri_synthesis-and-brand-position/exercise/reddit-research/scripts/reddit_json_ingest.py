#!/usr/bin/env python3
"""reddit_json_ingest.py — Normalize saved Reddit .json payloads and emit next-pull candidates.

Part of the manual-collection workflow for the reddit-researcher agent.
You save Reddit .json payloads by hand into reddit_corpus/raw/; this script:
  1. Normalizes each payload into a standard shape.
  2. Computes ranked drilldown_candidates — high-signal .json URLs for you to fetch next.

Usage:
    reddit_json_ingest.py [--raw DIR] [--out DIR] [--corpus DIR] [FILE ...]

Handles two Reddit payload shapes:
  - Post+comments: top-level JSON array [Listing(t3), Listing(t1...)]
  - Listing: single Listing object of t3 items

stdlib only: json, argparse, os, re, datetime, sys
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# Slug helpers
# ---------------------------------------------------------------------------

def permalink_to_slug(permalink: str) -> str:
    """Convert a Reddit permalink to a filesystem-safe slug.

    /r/running/comments/abc123/some_title/ -> r_running__comments__abc123__some_title
    """
    # Strip leading/trailing slashes, replace / with __, sanitize
    s = permalink.strip("/")
    s = s.replace("/", "__")
    # Remove characters that are unsafe on most filesystems
    s = re.sub(r"[^\w\-]", "_", s)
    # Collapse multiple underscores
    s = re.sub(r"_+", "_", s)
    return s.strip("_")


def epoch_to_iso(ts) -> str:
    """Convert a Unix epoch (int or float) to ISO 8601 UTC string."""
    try:
        dt = datetime.fromtimestamp(float(ts), tz=timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except (TypeError, ValueError, OSError):
        return ""


def full_url(permalink: str) -> str:
    """Return the canonical https://www.reddit.com URL for a permalink."""
    p = permalink.strip()
    if p.startswith("http"):
        return p
    return "https://www.reddit.com" + (p if p.startswith("/") else "/" + p)


_POSTID_RE = re.compile(r"/comments/([a-z0-9]+)", re.I)
_SUB_RE = re.compile(r"/r/([A-Za-z0-9_]+)/comments/")


def drilldown_url(permalink: str) -> str:
    """Return a compact .json drilldown URL for a reddit permalink.

    Use the full-subreddit-path form `https://www.reddit.com/r/<sub>/comments/<post-id>.json`.
    School and company networks often block the bare `/comments/<post-id>.json`
    form while letting the full path through. The browser still saves each
    payload as a unique `<post-id>.json` file. Falls back to the bare form only
    when the permalink has no subreddit, and to the full permalink form for
    non-standard links."""
    m = _POSTID_RE.search(permalink)
    if m:
        sub = _SUB_RE.search(permalink)
        if sub:
            return "https://www.reddit.com/r/" + sub.group(1) + "/comments/" + m.group(1) + ".json"
        return "https://www.reddit.com/comments/" + m.group(1) + ".json"
    base = full_url(permalink).rstrip("/")
    if not base.endswith(".json"):
        base += "/.json"
    return base


# ---------------------------------------------------------------------------
# Reddit permalink / redd.it extraction from text
# ---------------------------------------------------------------------------

# Matches /r/<sub>/comments/<id>/<slug>/ and variants
_REDDIT_PERMALINK_RE = re.compile(
    r"(?:https?://(?:www\.)?reddit\.com)?(/r/[A-Za-z0-9_]+/comments/[A-Za-z0-9]+(?:/[^\s\"')>]*)?)"
)
# Matches redd.it/<id> short links
_REDDITIT_RE = re.compile(r"https?://redd\.it/([A-Za-z0-9]+)")


def extract_reddit_refs(text: str) -> list:
    """Extract Reddit thread permalinks mentioned in free text."""
    if not text:
        return []
    found = []
    for m in _REDDIT_PERMALINK_RE.finditer(text):
        pl = m.group(1).rstrip(")")
        # Normalise to end with /
        if not pl.endswith("/"):
            pl += "/"
        found.append(pl)
    for m in _REDDITIT_RE.finditer(text):
        # redd.it short links — we don't know subreddit, emit the short URL as-is
        found.append("https://redd.it/" + m.group(1))
    return found


# ---------------------------------------------------------------------------
# Comment tree walker
# ---------------------------------------------------------------------------

def walk_comments(children, depth=0, post_permalink="") -> tuple:
    """Recursively walk a Reddit comment Listing children list.

    Returns:
        (comments: list[dict], more_parents: list[str])
        more_parents: permalinks of comments whose subtrees were truncated (kind=='more')
    """
    comments = []
    more_parents = []

    for child in children:
        kind = child.get("kind", "")
        data = child.get("data", {})

        if kind == "more":
            # Truncated subtree — the parent's permalink is the drilldown point.
            # We record post_permalink as the anchor since we don't have the
            # parent comment's permalink at this level; callers may pass it via
            # the parent comment's permalink when recursing.
            if post_permalink:
                more_parents.append(post_permalink)
            continue

        if kind != "t1":
            continue

        cid = data.get("id", "")
        c_permalink = data.get("permalink", "")
        author = data.get("author", "[deleted]")
        created_utc = data.get("created_utc", 0)
        score = data.get("score", 0)
        body = data.get("body", "")

        comment = {
            "id": cid,
            "author": author,
            "created_iso": epoch_to_iso(created_utc),
            "score": score,
            "depth": depth,
            "body": body,
            "permalink": c_permalink,
        }
        comments.append(comment)

        # Recurse into replies
        replies = data.get("replies", "")
        if replies and isinstance(replies, dict):
            reply_data = replies.get("data", {})
            reply_children = reply_data.get("children", [])
            sub_comments, sub_more = walk_comments(
                reply_children, depth=depth + 1, post_permalink=c_permalink
            )
            comments.extend(sub_comments)
            more_parents.extend(sub_more)

            # Check for 'more' nodes directly in reply children
            for rc in reply_children:
                if rc.get("kind") == "more":
                    # The parent comment's permalink is the drilldown anchor
                    more_parents.append(c_permalink)
                    break

    return comments, more_parents


# ---------------------------------------------------------------------------
# Normalize a single t3 (post) data dict
# ---------------------------------------------------------------------------

def normalize_post(post_data: dict, comment_listing=None) -> dict:
    """Produce the normalized post shape from a t3 data dict + optional comment Listing."""
    permalink = post_data.get("permalink", "")
    url = post_data.get("url", full_url(permalink))
    subreddit = post_data.get("subreddit", "")
    title = post_data.get("title", "")
    author = post_data.get("author", "[deleted]")
    created_utc = post_data.get("created_utc", 0)
    score = post_data.get("score", 0)
    num_comments = post_data.get("num_comments", 0)
    selftext = post_data.get("selftext", "")
    crosspost_list = post_data.get("crosspost_parent_list", [])

    # Walk comments
    comments = []
    raw_more_parents = []
    if comment_listing:
        children = comment_listing.get("data", {}).get("children", [])
        comments, raw_more_parents = walk_comments(children, depth=0, post_permalink=permalink)

    # --- Drilldown candidates ---
    candidates = []
    seen_urls = set()

    def add_candidate(pl):
        if not pl:
            return
        u = drilldown_url(pl)
        if u not in seen_urls:
            seen_urls.add(u)
            candidates.append(u)

    # (a) truncated 'more' subtrees
    for pl in raw_more_parents:
        add_candidate(pl)

    # (b) crosspost parents
    for cp in crosspost_list:
        cp_pl = cp.get("permalink", "")
        if cp_pl:
            add_candidate(cp_pl)

    # (c) reddit links in selftext and comment bodies
    all_text = selftext
    for c in comments:
        all_text += "\n" + c.get("body", "")

    for ref_pl in extract_reddit_refs(all_text):
        if ref_pl.startswith("https://redd.it/"):
            # Short URL — emit as-is with .json suffix
            u = ref_pl.rstrip("/") + "/.json"
        else:
            u = drilldown_url(ref_pl)
        if u not in seen_urls:
            seen_urls.add(u)
            candidates.append(u)

    return {
        "permalink": permalink,
        "url": url,
        "subreddit": subreddit,
        "title": title,
        "author": author,
        "created_iso": epoch_to_iso(created_utc),
        "score": score,
        "num_comments": num_comments,
        "selftext": selftext,
        "comments": comments,
        "drilldown_candidates": candidates,
    }


# ---------------------------------------------------------------------------
# Payload parsing — two shapes
# ---------------------------------------------------------------------------

def parse_payload(raw: object) -> list:
    """Return a list of (post_data, comment_listing_or_None) tuples from a raw payload.

    Handles:
      - Post+comments: top-level list [Listing(t3), Listing(t1...)]
      - Listing: single Listing object of t3 items
    """
    results = []

    if isinstance(raw, list) and len(raw) >= 1:
        # Post+comments shape: [Listing(t3), Listing(t1...)]
        post_listing = raw[0]
        comment_listing = raw[1] if len(raw) >= 2 else None

        post_children = post_listing.get("data", {}).get("children", [])
        for child in post_children:
            if child.get("kind") == "t3":
                results.append((child.get("data", {}), comment_listing))

    elif isinstance(raw, dict) and raw.get("kind") == "Listing":
        # Plain listing of t3 posts (subreddit .json)
        children = raw.get("data", {}).get("children", [])
        for child in children:
            if child.get("kind") == "t3":
                results.append((child.get("data", {}), None))

    return results


# ---------------------------------------------------------------------------
# Corpus scanning — what slugs are already normalized
# ---------------------------------------------------------------------------

def load_existing_slugs(corpus_dir: str) -> set:
    """Return set of drilldown .json URLs already represented in the corpus."""
    existing = set()
    if not os.path.isdir(corpus_dir):
        return existing
    for fname in os.listdir(corpus_dir):
        if not fname.endswith(".json"):
            continue
        fpath = os.path.join(corpus_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                doc = json.load(f)
            pl = doc.get("permalink", "")
            if pl:
                existing.add(drilldown_url(pl))
        except (json.JSONDecodeError, OSError):
            pass
    return existing


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Normalize saved Reddit .json payloads and emit next-pull candidates."
    )
    parser.add_argument(
        "--raw",
        default="./reddit_corpus/raw",
        help="Directory of saved raw .json files (default: ./reddit_corpus/raw)",
    )
    parser.add_argument(
        "--out",
        default="./reddit_corpus/normalized",
        help="Output directory for normalized .json files (default: ./reddit_corpus/normalized)",
    )
    parser.add_argument(
        "--corpus",
        default=None,
        help="Corpus dir to dedup drilldown candidates against (default: same as --out)",
    )
    parser.add_argument(
        "files",
        nargs="*",
        metavar="FILE",
        help="Explicit .json files to ingest (in addition to --raw dir)",
    )
    args = parser.parse_args()

    corpus_dir = args.corpus if args.corpus else args.out

    # Collect input files
    input_files = list(args.files)
    if os.path.isdir(args.raw):
        for fname in sorted(os.listdir(args.raw)):
            if fname.endswith(".json"):
                fpath = os.path.join(args.raw, fname)
                if fpath not in input_files:
                    input_files.append(fpath)

    if not input_files:
        print(f"No .json files found in {args.raw!r} and no FILE args given. Nothing to do.")
        sys.exit(0)

    # Load existing corpus to dedup candidates
    existing_urls = load_existing_slugs(corpus_dir)

    # Ensure output dir exists
    os.makedirs(args.out, exist_ok=True)

    ingested_slugs = []
    all_candidates = []  # (drilldown_url, source_slug)

    for fpath in input_files:
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                raw = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"  [SKIP] {fpath}: {e}", file=sys.stderr)
            continue

        post_tuples = parse_payload(raw)
        if not post_tuples:
            print(f"  [SKIP] {fpath}: no t3 posts found in payload")
            continue

        for post_data, comment_listing in post_tuples:
            permalink = post_data.get("permalink", "")
            if not permalink:
                print(f"  [SKIP] a post in {fpath}: no permalink")
                continue

            slug = permalink_to_slug(permalink)
            out_path = os.path.join(args.out, slug + ".json")

            normalized = normalize_post(post_data, comment_listing)
            normalized["drilldown_candidates"] = [
                u for u in normalized["drilldown_candidates"]
                if u not in existing_urls
            ]

            # Never let a comment-less pull (e.g. a subreddit/search listing,
            # which only carries post metadata) clobber an existing normalized
            # file that already has a fuller comment tree (e.g. from an
            # individual thread .json save). Processing order is filesystem-
            # sort order, not fetch-intent order, so a search.json can sort
            # after the real thread pull and silently zero out its comments.
            if os.path.exists(out_path):
                try:
                    with open(out_path, "r", encoding="utf-8") as ef:
                        existing_doc = json.load(ef)
                    if len(existing_doc.get("comments", [])) > len(normalized["comments"]):
                        print(
                            f"  [SKIP-WRITE] {slug}: existing normalized file has "
                            f"{len(existing_doc.get('comments', []))} comments, "
                            f"{fpath} would only contribute {len(normalized['comments'])}; keeping existing"
                        )
                        ingested_slugs.append(slug)
                        existing_urls.add(drilldown_url(permalink))
                        continue
                except (json.JSONDecodeError, OSError):
                    pass

            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(normalized, f, indent=2, ensure_ascii=False)

            ingested_slugs.append(slug)

            # Add to existing_urls so subsequent posts in this run don't re-suggest
            existing_urls.add(drilldown_url(permalink))

            for u in normalized["drilldown_candidates"]:
                all_candidates.append((u, slug))

    # --- Output ---
    print()
    print("=== Ingested ===")
    for slug in ingested_slugs:
        print(f"  {slug}")

    # Dedup candidates across all ingested posts (preserve first-seen order)
    seen_out = set()
    ranked = []
    for u, source_slug in all_candidates:
        if u not in seen_out and u not in existing_urls:
            seen_out.add(u)
            ranked.append((u, source_slug))

    print()
    print("=== Suggested next .json URLs ===")
    if ranked:
        for u, source_slug in ranked:
            print(f"  {u}")
            print(f"    (from: {source_slug})")
    else:
        print("  (none — corpus is saturated for this batch)")
    print()


if __name__ == "__main__":
    main()
