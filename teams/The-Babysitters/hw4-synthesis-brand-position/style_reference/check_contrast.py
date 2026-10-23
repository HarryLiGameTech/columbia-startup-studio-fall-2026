#!/usr/bin/env python3
"""

WCAG 2.x contrast check for style round 3. Python 3 standard library only.

How it works
  1. Reads the colour tokens from the :root block of each page, so the numbers follow the files.
  2. Checks the text, UI and decoration colour pairs listed in PAGES below, with a note on where each is used.
  3. Backdrop glows (Off Hours only) are composited the way a browser does it (sRGB, alpha over the ground)
     and the text that sits on a glow is checked against that composite. The glow is blurred on the page,
     so its real peak is lower than the composite used here: these are worst cases.
  4. GUIDE_ONLY lists colours that the draft style guide names but the pages do not use yet (the error colour).
  5. Fails (exit status 1) if any pair is under its threshold or if a :root colour is not used in any pair.

Contrast ratio = (L1 + 0.05) / (L2 + 0.05), where L is WCAG relative luminance:
  each sRGB channel c/255 is linearised (c <= 0.03928: c/12.92, else ((c + 0.055)/1.055)^2.4),
  then L = 0.2126 R + 0.7152 G + 0.0722 B.

Roles and thresholds
  body   text under 24px regular or 18.66px bold          4.5:1
  large  text at 24px regular or 18.66px bold, or more    3.0:1
  ui     non-text marks that carry meaning (WCAG 1.4.11)  3.0:1
  decor  purely decorative (hairlines, backdrop, stripes) listed, no threshold

Run:    python3 -I check_contrast.py
Table:  python3 -I check_contrast.py --markdown
"""
import math
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
THRESHOLD = {"body": 4.5, "large": 3.0, "ui": 3.0, "decor": None}

# ---------------------------------------------------------------- colour maths
def hex_to_rgb(value):
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "#%02X%02X%02X" % tuple(int(round(c)) for c in rgb)

def luminance(rgb):
    def lin(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def ratio(rgb_a, rgb_b):
    la, lb = luminance(rgb_a), luminance(rgb_b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

def floor2(x):
    """Show two decimals without rounding up, so a displayed value never hides a fail."""
    return math.floor(x * 100) / 100

# ---------------------------------------------------------------- token reading
def read_tokens(path):
    text = path.read_text(encoding="utf-8")
    root = re.search(r":root\s*\{(.*?)\n\}", text, re.S)
    if not root:
        raise SystemExit("no :root block in %s" % path.name)
    tokens = {}
    for name, value in re.findall(r"--([a-z0-9-]+):\s*(#[0-9A-Fa-f]{6})\s*;", root.group(1)):
        tokens[name] = value.upper()
    return tokens

def resolve(spec, tokens, used):
    """spec is a token name, a literal #RRGGBB, or ("mix", fg_spec, alpha, bg_spec)."""
    if isinstance(spec, tuple):
        _, fg_spec, alpha, bg_spec = spec
        fg_rgb, fg_label = resolve(fg_spec, tokens, used)
        bg_rgb, bg_label = resolve(bg_spec, tokens, used)
        out = tuple(f * alpha + b * (1 - alpha) for f, b in zip(fg_rgb, bg_rgb))
        return out, "%s at %d%% over %s = %s" % (fg_label.split(" ")[0], round(alpha * 100), bg_label.split(" ")[0], rgb_to_hex(out))
    if spec.startswith("#"):
        return hex_to_rgb(spec), spec.upper()
    if spec not in tokens:
        raise SystemExit("token --%s is not defined in :root" % spec)
    used.add(spec)
    return hex_to_rgb(tokens[spec]), "--%s %s" % (spec, tokens[spec])

def mix(fg, alpha, bg):
    return ("mix", fg, alpha, bg)

# ---------------------------------------------------------------- the pairs
# (foreground, background, role, where it is used)
PAGES = {}

_glow = mix("glow", 0.5, "ground")      # horizon glow behind the subline, buttons and 'works with' line
_moon = mix("accent", 0.12, "ground")   # moon glow behind the headline and feature label
PAGES["off-hours-r3.html"] = [
    ("ink", "ground", "large", "Headline (h1, 48-132px); drawing heading (28-40px)"),
    ("ink", "ground", "body", "Wordmark, header link, key names, labels inside the drawing"),
    ("ink-faint", "ground", "body", "Feature label, drawing label, scale numbers, key text, caption"),
    ("ink", _moon, "large", "Headline where the moon glow sits behind it"),
    ("ink-faint", _moon, "body", "Feature label near the moon glow"),
    ("ink", _glow, "body", "Subline and secondary button label over the horizon glow"),
    ("ink-faint", _glow, "body", "'Works with' line over the horizon glow"),
    ("accent", _glow, "body", "Secondary button label on hover, over the horizon glow"),
    ("ground", "ink", "body", "Primary button label"),
    ("ground", "accent", "body", "Primary button label on hover, skip-link label"),
    ("accent", "ground", "body", "'Concept, not shipped' tag text and border"),
    ("ink", "ground-2", "large", "Section heading (h2, 36-64px), step headings (24px)"),
    ("ink", "ground-2", "body", "Footer link"),
    ("ink-faint", "ground-2", "body", "Section label, step text, footer text"),
    ("accent", "ground-2", "large", "Step numerals (52px)"),
    ("ink", "ground", "ui", "Drawing: work line, guardrail rails and posts, cap line, checks, 'over' bracket"),
    ("ink-faint", "ground", "ui", "Drawing: scale ticks, zoom window, leader lines, detail frame; square nodes"),
    ("accent", "ground", "ui", "Drawing: turn blocks, homecoming outlines, visit bar; focus ring"),
    ("dots", "ground", "ui", "Drawing: dotted unused stretch"),
    ("ink", _glow, "ui", "Secondary button border over the horizon glow"),
    ("accent", _glow, "ui", "Focus ring over the horizon glow"),
    ("ground", "ink", "ui", "Primary button arrow and its divider"),
    ("accent", "ground-2", "ui", "Focus ring on the steps band and footer"),
    ("ink-faint", "ground-2", "ui", "Square nodes on the steps band and footer"),
    ("line", "ground", "decor", "1px frame hairlines"),
    ("line", "ground-2", "decor", "1px frame hairlines and step dividers on the steps band"),
    ("glow", "ground", "decor", "Backdrop: horizon glow against the ground"),
]

PAGES["inside-the-lines-r3.html"] = [
    ("ink", "ground", "large", "Headline (h1, 32-72px)"),
    ("ink", "ground", "body", "Wordmark, header link, subline, drawing heading, legend names, secondary button label"),
    ("ink-faint", "ground", "body", "Feature label, rail label, drawing label, 'works with' line, legend text, caption"),
    ("accent", "ground", "body", "'Concept, not shipped' tag text and border; secondary button label on hover"),
    ("accent-ink", "accent", "body", "Primary button label, skip-link label"),
    ("accent-ink", "ink", "body", "Primary button label on hover"),
    ("ink", "ground-2", "large", "Section heading (h2, 28-44px)"),
    ("ink", "ground-2", "body", "Step headings (20px), step numbers, footer link"),
    ("ink-faint", "ground-2", "body", "Section label, step text, rail label, footer text"),
    ("ink", "field", "ui", "Field: boundary, turn lines, check dots, allowance line, buffer edge"),
    ("ink", "stripe", "ui", "Same marks over a mowing stripe"),
    ("ink-faint", "field", "ui", "Field: hatching in the work buffer"),
    ("ink-faint", "stripe", "ui", "Hatching over a mowing stripe"),
    ("accent", "field", "ui", "Field: homecoming lines, hollow dot, home marker"),
    ("accent", "stripe", "ui", "Homecoming marks over a mowing stripe"),
    ("accent-ink", "accent", "ui", "House icon in the home marker; primary button arrow and divider"),
    ("ink", "ground", "ui", "Legend swatches; secondary button border"),
    ("accent", "ground", "ui", "Legend homecoming swatch; focus ring on the main ground"),
    ("ink", "ground-2", "ui", "Step number squares"),
    ("accent", "ground-2", "ui", "Focus ring on the steps band and footer"),
    ("ink-faint", "ground", "decor", "Square nodes and rail ticks"),
    ("line", "ground", "decor", "1px frame lines and rail border"),
    ("line", "ground-2", "decor", "1px frame lines and step cell borders on the steps band"),
    ("field", "ground", "decor", "Field against the page (the 2px boundary line carries the shape)"),
    ("stripe", "field", "decor", "Mowing stripes against the field"),
]

PAGES["index.html"] = [
    ("ink", "bg", "large", "Heading (h1, 30-44px)"),
    ("ink", "bg", "body", "Wordmark"),
    ("ink-2", "bg", "body", "Intro, note, footer text"),
    ("bg", "ink", "body", "Skip-link label"),
    ("ink", "card", "body", "Card text"),
    ("ink-2", "card", "body", "Card descriptions and 'refined from' labels"),
    ("link", "card", "body", "Direction names (links)"),
    ("link", "bg", "body", "NOTES.md and style guide links"),
    ("ink", "bg", "ui", "Concept tag border; focus ring"),
    ("rule", "card", "ui", "Card border"),
    ("rule", "bg", "ui", "Footer rule, swatch borders"),
]

# Colours the draft style guide names that no page uses yet. Literal hex values, checked against both grounds.
GUIDE_ONLY = [
    ("#FF9B8F", "#0E1647", "body", "Error text on the Off Hours ground (style guide token 'error')"),
    ("#FF9B8F", "#090F34", "body", "Error text on the Off Hours band"),
    ("#FF9B8F", "#0B1F0F", "body", "Error text on the Inside the Lines ground"),
    ("#FF9B8F", "#0E2813", "body", "Error text on the Inside the Lines band"),
]

# ---------------------------------------------------------------- run
def evaluate(pairs, tokens, used):
    rows, failures = [], 0
    for fg, bg, role, where in pairs:
        fg_rgb, fg_label = resolve(fg, tokens, used)
        bg_rgb, bg_label = resolve(bg, tokens, used)
        r = ratio(fg_rgb, bg_rgb)
        need = THRESHOLD[role]
        if need is None:
            verdict = "decor, no threshold"
        elif r >= need:
            verdict = "pass"
        else:
            verdict = "FAIL"
            failures += 1
        rows.append((fg_label, bg_label, where, role, r, need, verdict))
    return rows, failures

def main():
    markdown = "--markdown" in sys.argv[1:]
    results = {}
    total_fail = total_unused = total_pairs = 0
    for name, pairs in PAGES.items():
        tokens = read_tokens(HERE / name)
        used = set()
        rows, failures = evaluate(pairs, tokens, used)
        unused = sorted(set(tokens) - used)
        results[name] = (rows, failures, unused)
    rows, failures = evaluate(GUIDE_ONLY, {}, set())
    results["style guide only (not on a page yet)"] = (rows, failures, [])
    for name, (rows, failures, unused) in results.items():
        total_fail += failures
        total_unused += len(unused)
        total_pairs += len(rows)
        if markdown:
            print("\n#### %s\n" % name)
            print("| Foreground | Background | Where | Role | Ratio | Needs | Result |")
            print("|---|---|---|---|---|---|---|")
            for fg, bg, where, role, r, need, verdict in rows:
                need_s = "none" if need is None else "%.1f:1" % need
                print("| %s | %s | %s | %s | %.2f:1 | %s | %s |" % (fg, bg, where, role, floor2(r), need_s, verdict))
        else:
            print("\n== %s ==" % name)
            for fg, bg, where, role, r, need, verdict in rows:
                need_s = "-" if need is None else "%.1f:1" % need
                print("  %-5s %6.2f:1 (needs %-6s) %-20s  %s on %s  [%s]" % (role, floor2(r), need_s, verdict, fg, bg, where))
        if unused:
            print("  UNUSED TOKENS (no pair lists them): %s" % ", ".join("--" + u for u in unused))
    print("\nPairs checked: %d" % total_pairs)
    print("Pairs under their threshold: %d" % total_fail)
    print("Tokens not used in any pair: %d" % total_unused)
    return 1 if (total_fail or total_unused) else 0

if __name__ == "__main__":
    sys.exit(main())
