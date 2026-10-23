#!/usr/bin/env python3
"""Claude Daycare logo set: rebuild the lockup, stacked and avatar SVGs.

Reads the mark (mark.svg, beside this script by default) and a font file, and
writes outlined (no <text>) SVGs:

    lockup.svg  lockup_on_ink.svg  lockup_mono_black.svg  lockup_mono_white.svg
    stacked.svg stacked_on_ink.svg  avatar.svg

Run it with the wordmark font (Hanken Grotesk, variable file, weight 700):

    python3 -m venv venv && venv/bin/pip install fonttools
    venv/bin/python3 build_logo_set.py --font "HankenGrotesk[wght].ttf"

To change the wordmark font, point --font at another .ttf/.otf (and --weight if
it is a variable font). Everything is measured from the font, so nothing else
needs editing. Only fonttools is needed; there is no other dependency.

Rules it applies (see LOGO_RULES.md):
  * Lockup: mark height = cap height. The mark's bottom edge sits on the
    baseline. The gap between the mark's right edge and the first letter's left
    edge is half the cap height. All measured on ink, not on font boxes.
  * Kerning: read from the font's GPOS 'kern' lookups (pair adjustments, formats
    1 and 2). Nothing else from GPOS or GSUB is applied. For "Claude Daycare" in
    Hanken Grotesk no GSUB feature that is on by default changes any glyph.
  * Stacked: mark 4 cap heights tall, centred over the name; the gap from the
    mark's bottom edge to the name's cap line is the mark's clear space (4 cells).
  * Margins: transparent files carry a one-cell margin (like mark.svg); the
    on-ink files carry the clear space (four cells) as their panel padding.
  * Avatar: the mark at 5/8 scale, centred on the ink square. Its farthest corner
    is 38.7 units from the centre of the 100-unit square, inside a circular crop
    and inside the 40-unit "maskable icon" safe circle. At 512 px a cell is
    exactly 20 px, so every edge lands on a whole pixel.
"""
import argparse
import math
import os
import re
import sys

try:
    from fontTools.pens.boundsPen import BoundsPen
    from fontTools.pens.svgPathPen import SVGPathPen
    from fontTools.pens.transformPen import TransformPen
    from fontTools.ttLib import TTFont
    from fontTools.varLib import instancer
except ImportError:
    sys.exit("fonttools is required: pip install fonttools (in a virtual environment)")

INK, NEAR_WHITE, BLACK, WHITE = "#1f1e1a", "#f7f6f2", "#000000", "#ffffff"
NAME = "Claude Daycare"

# Lattice of the mark: 16 cells of 6.25 units in a 100-unit box. The artwork
# spans cells 1 to 15, so its ink is 14 cells (87.5 units) tall and wide.
CELL = 6.25
LOCKUP_GAP_IN_CAPS = 0.5      # gap mark -> first letter, as a fraction of cap height
MARGIN_CELLS = 1              # margin of transparent files, in mark cells
CLEAR_CELLS = 4               # clear space (= panel padding of on-ink files), in cells
STACK_MARK_IN_CAPS = 4        # stacked: mark height as a multiple of cap height
AVATAR_SCALE = 0.625          # avatar: mark scale (5/8): a cell is 20 px at 512 px, so edges stay whole pixels
AVATAR_MAX_RADIUS = 40.0      # the farthest mark corner must stay within this distance of the centre

def num(v, digits=3):
    s = ("%.*f" % (digits, v)).rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s

# ---------------------------------------------------------------- the mark
def read_mark(path):
    """Return the mark as a list of closed polygons [(x, y), ...] (M, L, Z only)."""
    text = open(path, encoding="utf-8").read()
    d = re.search(r'\sd="([^"]+)"', text).group(1)
    if re.search(r"[A-Za-z]", re.sub(r"[MLZ]", "", d)):
        sys.exit("mark.svg: only M, L and Z path commands are supported")
    tok = re.findall(r"[MLZ]|-?\d+(?:\.\d+)?", d)
    polys, i = [], 0
    while i < len(tok):
        if tok[i] == "M":
            polys.append([(float(tok[i + 1]), float(tok[i + 2]))])
            i += 3
        elif tok[i] == "L":
            polys[-1].append((float(tok[i + 1]), float(tok[i + 2])))
            i += 3
        elif tok[i] == "Z":
            i += 1
        else:
            sys.exit("mark.svg: unexpected token %r" % tok[i])
    return polys

def mark_bbox(polys):
    xs = [p[0] for poly in polys for p in poly]
    ys = [p[1] for poly in polys for p in poly]
    return min(xs), min(ys), max(xs), max(ys)

def mark_path(polys, scale, tx, ty):
    """The mark's path data after x' = x*scale + tx, y' = y*scale + ty."""
    out = []
    for poly in polys:
        pts = ["%s %s" % (num(x * scale + tx, 5), num(y * scale + ty, 5)) for x, y in poly]
        out.append("M" + "L".join(pts) + "Z")
    return "".join(out)

# ------------------------------------------------------------ the wordmark
class Wordmark:
    def __init__(self, font_path, weight, text):
        font = TTFont(font_path)
        if "fvar" in font:
            font = instancer.instantiateVariableFont(font, {"wght": weight}, inplace=False)
        self.font, self.text = font, text
        self.gs = font.getGlyphSet()
        cmap = font.getBestCmap()
        try:
            self.names = [cmap[ord(c)] for c in text]
        except KeyError as e:
            sys.exit("font has no glyph for %r" % chr(e.args[0]))
        self.upem = font["head"].unitsPerEm
        h = cmap.get(ord("H"))   # cap height = top of the flat capital H
        self.cap = self.bounds(h)[3] if h else font["OS/2"].sCapHeight
        self.kerns = [self.kern(a, b) for a, b in zip(self.names, self.names[1:])]

    def bounds(self, name):
        bp = BoundsPen(self.gs)
        self.gs[name].draw(bp)
        return bp.bounds  # None for an empty glyph such as the space

    def kern(self, left, right):
        """Pair adjustment (font units) from GPOS 'kern' lookups, or 0."""
        if "GPOS" not in self.font:
            return 0
        gpos = self.font["GPOS"].table
        lookups = set()
        for fr in gpos.FeatureList.FeatureRecord:
            if fr.FeatureTag == "kern":
                lookups.update(fr.Feature.LookupListIndex)
        total = 0
        for li in sorted(lookups):
            for st in gpos.LookupList.Lookup[li].SubTable:
                st = getattr(st, "ExtSubTable", st)
                if not hasattr(st, "PairSet") and not hasattr(st, "Class1Record"):
                    continue  # not a pair-adjustment subtable
                if left not in st.Coverage.glyphs:
                    continue
                value = None
                if st.Format == 1:
                    ps = st.PairSet[st.Coverage.glyphs.index(left)]
                    for rec in ps.PairValueRecord:
                        if rec.SecondGlyph == right:
                            value = rec.Value1
                            break
                    else:
                        continue  # pair not listed here: try the next subtable
                elif st.Format == 2:
                    c1 = st.ClassDef1.classDefs.get(left, 0)
                    c2 = st.ClassDef2.classDefs.get(right, 0)
                    value = st.Class1Record[c1].Class2Record[c2].Value1
                total += getattr(value, "XAdvance", 0) or 0
                break  # first matching subtable of a lookup wins
        return total

    def positions(self):
        x, out = 0, []
        for i, n in enumerate(self.names):
            out.append(x)
            x += self.font["hmtx"][n][0] + (self.kerns[i] if i < len(self.kerns) else 0)
        return out

    def ink_x_min(self):
        return self.bounds(self.names[0])[0]

    def ink_box(self):
        """(xmin, ymin, xmax, ymax) of the ink in font units, y up, origin at the pen start."""
        xs0, xs1, ys0, ys1 = [], [], [], []
        for n, px in zip(self.names, self.positions()):
            b = self.bounds(n)
            if b:
                xs0.append(px + b[0]); xs1.append(px + b[2]); ys0.append(b[1]); ys1.append(b[3])
        return min(xs0), min(ys0), max(xs1), max(ys1)

    def paths(self, k, ox, oy):
        """One path d-string per visible glyph, scaled by k, y flipped, origin at (ox, oy)."""
        out = []
        for n, px in zip(self.names, self.positions()):
            if not self.bounds(n):
                continue
            pen = SVGPathPen(self.gs, ntos=num)
            self.gs[n].draw(TransformPen(pen, (k, 0, 0, -k, ox + k * px, oy)))
            out.append(pen.getCommands())
        return out

# ---------------------------------------------------------------- the SVGs
def svg(box, body, label):
    x, y, w, h = box
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s %s %s %s" role="img" '
            'aria-label="%s">%s</svg>\n' % (num(x), num(y), num(w), num(h), label, body))

def build_lockup(polys, wm):
    """Lockup in units where the cap height is 100. Returns (parts, ink box, cell)."""
    x0, y0, x1, y1 = mark_bbox(polys)
    m = 100.0 / (y1 - y0)                        # mark ink height -> cap height
    cell = CELL * m
    mark_w = (x1 - x0) * m
    k = 100.0 / wm.cap                           # font units -> lockup units
    gap = LOCKUP_GAP_IN_CAPS * 100.0
    ox = mark_w + gap - k * wm.ink_x_min()       # pen start of the first letter
    d_mark = mark_path(polys, m, -x0 * m, -y1 * m)   # bottom edge on y = 0 (baseline)
    glyphs = wm.paths(k, ox, 0)
    t = wm.ink_box()
    ink = (0.0, min(-100.0, -k * t[3]), ox + k * t[2], max(0.0, -k * t[1]))
    return d_mark, glyphs, ink, cell

def build_stacked(polys, wm):
    x0, y0, x1, y1 = mark_bbox(polys)
    m = STACK_MARK_IN_CAPS * 100.0 / (y1 - y0)
    cell = CELL * m
    k = 100.0 / wm.cap
    t = wm.ink_box()
    ox = -k * t[0]                               # name's left ink edge at x = 0
    name_w = k * (t[2] - t[0])
    mark_w = (x1 - x0) * m
    mark_left = (name_w - mark_w) / 2.0          # mark centred over the name's ink
    mark_bottom = -(100.0 + CLEAR_CELLS * cell)    # gap = the mark's clear space (4 cells)
    d_mark = mark_path(polys, m, mark_left - x0 * m, mark_bottom - y1 * m)
    glyphs = wm.paths(k, ox, 0)
    ink = (0.0, mark_bottom - (y1 - y0) * m, name_w, max(0.0, -k * t[1]))
    return d_mark, glyphs, ink, cell

def compose(d_mark, glyphs, ink, cell, colour, background, label):
    pad = (CLEAR_CELLS if background else MARGIN_CELLS) * cell   # panel padding or margin
    box = (ink[0] - pad, ink[1] - pad, ink[2] - ink[0] + 2 * pad, ink[3] - ink[1] + 2 * pad)
    body = ""
    if background:
        body += '<rect x="%s" y="%s" width="%s" height="%s" fill="%s"/>' % (
            num(box[0]), num(box[1]), num(box[2]), num(box[3]), background)
    body += '<g fill="%s"><path d="%s"/>' % (colour, d_mark)
    body += "".join('<path d="%s"/>' % g for g in glyphs) + "</g>"
    return svg(box, body, label)

def build_avatar(polys):
    x0, y0, x1, y1 = mark_bbox(polys)
    cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    s = AVATAR_SCALE
    far = s * max(math.hypot(x - cx, y - cy) for poly in polys for x, y in poly)
    if far > AVATAR_MAX_RADIUS:
        sys.exit("avatar: mark corner at %.2f units is outside the %.0f-unit safe circle" % (far, AVATAR_MAX_RADIUS))
    d = mark_path(polys, s, 50 - cx * s, 50 - cy * s)
    body = '<rect width="100" height="100" fill="%s"/><path fill="%s" d="%s"/>' % (INK, NEAR_WHITE, d)
    return svg((0, 0, 100, 100), body, NAME + " avatar"), s

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--font", required=True, help="path to the wordmark font (.ttf or .otf)")
    ap.add_argument("--weight", type=float, default=700, help="wght value if the font is variable (default 700)")
    ap.add_argument("--mark", default=os.path.join(here, "mark.svg"), help="path to mark.svg")
    ap.add_argument("--out", default=here, help="folder to write the SVGs into")
    ap.add_argument("--text", default=NAME, help="the name to set (default %r)" % NAME)
    a = ap.parse_args()

    polys = read_mark(a.mark)
    wm = Wordmark(a.font, a.weight, a.text)
    files = {}
    lock = build_lockup(polys, wm)
    files["lockup.svg"] = compose(*lock, INK, None, a.text)
    files["lockup_on_ink.svg"] = compose(*lock, NEAR_WHITE, INK, a.text)
    files["lockup_mono_black.svg"] = compose(*lock, BLACK, None, a.text)
    files["lockup_mono_white.svg"] = compose(*lock, WHITE, None, a.text)
    stack = build_stacked(polys, wm)
    files["stacked.svg"] = compose(*stack, INK, None, a.text)
    files["stacked_on_ink.svg"] = compose(*stack, NEAR_WHITE, INK, a.text)
    files["avatar.svg"], s = build_avatar(polys)

    os.makedirs(a.out, exist_ok=True)
    for name, content in files.items():
        with open(os.path.join(a.out, name), "w", encoding="utf-8") as fh:
            fh.write(content)
        print("wrote", name)
    print("cap height %s font units (upem %s); kerning applied to %d of %d pairs; avatar scale %.4f"
          % (num(wm.cap), wm.upem, sum(1 for v in wm.kerns if v), len(wm.kerns), s))

if __name__ == "__main__":
    main()
