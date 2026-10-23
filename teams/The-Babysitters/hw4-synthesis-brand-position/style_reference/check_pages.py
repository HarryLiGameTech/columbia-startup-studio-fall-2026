#!/usr/bin/env python3
"""

Structure and copy check for the style round 3 pages. Python 3 standard library only; reads files, changes nothing.

For each page it checks:
  - well-formed: every non-void element is closed, in order, and nothing is closed that was not open
  - no duplicate id; every href="#x", aria-labelledby and local file link resolves
  - lang, charset, viewport and title present; exactly one h1; no skipped heading level
  - no <script>, no <img> or other raster image, no stylesheet or resource other than Google Fonts
  - at most two font families requested
  - a :focus-visible rule, a prefers-reduced-motion: reduce rule, 44px minimum on the skip link, nav links and buttons
  - the footer disclaimer, and on the two direction pages: the three steps, "checked between turns",
    "Concept, not shipped", "Numbers are illustrative." exactly once
  - none of a list of overclaiming, ranking or filler phrases, and no emoji or asterisk-like glyph in the text

Run: python3 -I check_pages.py
"""
import html.parser
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
DIRECTION_PAGES = ["off-hours-r3.html", "inside-the-lines-r3.html"]
ALL_PAGES = DIRECTION_PAGES + ["index.html"]

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
FOOTER = "Concept sketch for The Babysitters (Columbia COMS W4995, Fall 2026). Not affiliated with or endorsed by Anthropic."
STEP_TITLES = ["Set the allowance", "Send your agent", "Read what happened"]

# Phrases that would break the honest-claims rule, rank the directions, or call the product something it is not.
BANNED = [
    r"stops? exactly", r"exactly at the cap", r"hard stop", r"hard cap", r"guarantee", r"never run out",
    r"never goes over", r"never over", r"your usage is protected", r"100%\s*safe", r"zero risk", r"pauses itself",
    r"add-on", r"third-party", r"plugin", r"official", r"(?<!endorsed )by anthropic", r"anthropic-approved",
    r"recommended", r"front-runner", r"winner", r"our pick", r"the best", r"preferred",
    r"lorem", r"ipsum", r"supercharge", r"seamless", r"unlock", r"ai-powered", r"10x",
]
# Glyphs that read as stars, sparkles or asterisks, plus emoji ranges.
BAD_GLYPHS = set("*✱✲✳✴✵✶✷✸✹✺✻✼✽✾✿❀❁❂❃❄❅❆❇❈❉❊❋★☆⁂⁎⁕٭")

class Parser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors, self.ids, self.hrefs, self.labelledby = [], [], [], [], []
        self.headings, self.tags, self.links, self.text = [], [], [], []
        self.in_style = False
        self.style = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append(tag)
        if "id" in a:
            self.ids.append(a["id"])
        if "href" in a:
            self.hrefs.append((tag, a["href"], a.get("rel")))
        if "src" in a:
            self.links.append(a["src"])
        if "aria-labelledby" in a:
            self.labelledby.extend(a["aria-labelledby"].split())
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))
        if tag == "style":
            self.in_style = True
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_startendtag(self, tag, attrs):
        # <path/> and friends inside SVG: open and closed at once
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag == "style":
            self.in_style = False
        if tag in VOID:
            self.errors.append("closing tag for void element </%s> at %s" % (tag, self.getpos()))
            return
        if not self.stack:
            self.errors.append("</%s> with nothing open at %s" % (tag, self.getpos()))
            return
        top, pos = self.stack.pop()
        if top != tag:
            self.errors.append("</%s> at %s closes <%s> opened at %s" % (tag, self.getpos(), top, pos))

    def handle_data(self, data):
        if self.in_style:
            self.style.append(data)
        else:
            self.text.append(data)

def check(name):
    path = HERE / name
    raw = path.read_text(encoding="utf-8")
    p = Parser()
    p.feed(raw)
    p.close()
    fails = list(p.errors)
    if p.stack:
        fails.append("unclosed elements: %s" % ", ".join("<%s> at %s" % t for t in p.stack))
    dup = sorted({i for i in p.ids if p.ids.count(i) > 1})
    if dup:
        fails.append("duplicate ids: %s" % dup)
    for tag, href, rel in p.hrefs:
        if href.startswith("#"):
            if href[1:] not in p.ids:
                fails.append("anchor %s does not resolve" % href)
        elif href.startswith("http"):
            if not href.startswith(("https://fonts.googleapis.com", "https://fonts.gstatic.com")):
                fails.append("outside link or resource: %s" % href)
        else:
            if not (path.parent / href).resolve().exists():
                fails.append("local link %s does not exist" % href)
    for ref in p.labelledby:
        if ref not in p.ids:
            fails.append("aria-labelledby %s does not resolve" % ref)
    if p.links:
        fails.append("src attributes found (images or scripts): %s" % p.links)
    for bad in ("script", "img", "picture", "video", "iframe", "object", "embed"):
        if bad in p.tags:
            fails.append("<%s> present" % bad)
    if re.search(r"url\((?!\"?data:image/svg\+xml)", "".join(p.style)):
        fails.append("a CSS url() that is not an inline SVG")
    if not re.search(r'<html lang="en">', raw):
        fails.append("no lang on <html>")
    for needle in ('<meta charset="utf-8">', 'name="viewport"', "<title>"):
        if needle not in raw:
            fails.append("missing %s" % needle)
    if p.headings.count(1) != 1:
        fails.append("h1 count is %d" % p.headings.count(1))
    prev = 0
    for level in p.headings:
        if level > prev + 1:
            fails.append("heading level jumps from h%d to h%d" % (prev, level))
        prev = level
    families = re.findall(r"family=([A-Za-z+]+)", raw)
    if len(set(families)) > 2:
        fails.append("more than two font families: %s" % families)
    css = "".join(p.style)
    if ":focus-visible" not in css:
        fails.append("no :focus-visible rule")
    if name in DIRECTION_PAGES and "prefers-reduced-motion: reduce" not in css:
        fails.append("no reduced-motion rule")
    for cls in (".skip", ".navlink", ".btn ", ".dir", ".links a"):
        block = re.search(re.escape(cls.strip()) + r"\s*\{([^}]*)\}", css)
        if block and "min-height" in block.group(1):
            m = re.search(r"min-height:\s*([\d.]+)(px|rem)", block.group(1))
            px = float(m.group(1)) * (16 if m.group(2) == "rem" else 1)
            if px < 44:
                fails.append("%s min-height %.0fpx under 44px" % (cls, px))
    text = re.sub(r"\s+", " ", " ".join(p.text))
    if FOOTER not in text:
        fails.append("footer disclaimer missing")
    if name in DIRECTION_PAGES:
        for title in STEP_TITLES + ["How it works in three steps"]:
            if text.count(title) < 1:
                fails.append("missing '%s'" % title)
        for needle in ("checked between turns", "Concept, not shipped", "not bounded by"):
            if needle not in text:
                fails.append("missing '%s'" % needle)
        if text.count("Numbers are illustrative.") != 1:
            fails.append("'Numbers are illustrative.' appears %d times" % text.count("Numbers are illustrative."))
    low = text.lower()
    for pat in BANNED:
        if re.search(pat, low):
            fails.append("banned phrase /%s/ in page text" % pat)
    for ch in set(text):
        if ch in BAD_GLYPHS or unicodedata.category(ch) == "So" or ord(ch) >= 0x1F000:
            fails.append("glyph %r (U+%04X) in page text" % (ch, ord(ch)))
    return fails

def main():
    total = 0
    for name in ALL_PAGES:
        fails = check(name)
        total += len(fails)
        print("%s  %s" % ("PASS" if not fails else "FAIL", name))
        for f in fails:
            print("      " + f)
    print("\nProblems found: %d" % total)
    return 1 if total else 0

if __name__ == "__main__":
    sys.exit(main())
