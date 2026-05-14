#!/usr/bin/env python3
"""
Generate SVG placeholder assets for the public demo portfolio.

Reads a manifest of (path, label, kind) tuples and writes a labeled SVG
to each path. `kind` controls the glyph in the corner (image / video / demo).
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

PALETTES = {
    "p1":  ("#e9b5a0", "#d97757"),  # warm
    "p2":  ("#cdd6c4", "#7f9670"),  # sage
    "p3":  ("#d9c6e4", "#8d6db0"),  # plum
    "p4":  ("#f1d59a", "#c89546"),  # amber
    "p5":  ("#c9d8e8", "#5e84a8"),  # blue
    "p6":  ("#e5cdb7", "#a07d59"),  # tan
    "p7":  ("#f0c4c4", "#b96a6a"),  # rose
    "p9":  ("#cfe1d4", "#658a72"),  # mint
    "p10": ("#c5d8db", "#5a8189"),  # teal
    "p11": ("#dcd1ea", "#7d6bb0"),  # lavender
    "p12": ("#e6dcc8", "#9b8868"),  # sand
}

PROJECT_NAMES = {
    "p1":  "Pulse Survey",
    "p2":  "Feedback Graph",
    "p3":  "Insights Surface",
    "p4":  "Theme Sequencer",
    "p5":  "This Portfolio",
    "p6":  "Pulse Dashboard",
    "p7":  "Onboarding Redesign",
    "p9":  "Weekend Builds",
    "p10": "Forge Docs",
    "p11": "Weekly Streaks",
    "p12": "Mason System",
}


def xml_escape(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg(project_id: str, caption: str, kind: str = "image", w: int = 1600, h: int = 1000) -> str:
    base, accent = PALETTES.get(project_id, ("#e0dccf", "#8a857e"))
    name = xml_escape(PROJECT_NAMES.get(project_id, "Placeholder"))
    kind_label = {"image": "Image", "video": "Video", "demo": "Interactive demo"}.get(kind, "Asset")
    caption = xml_escape(caption)

    glyph = {
        "image": '<circle cx="46" cy="46" r="10" fill="currentColor" opacity=".55"/><path d="M14 78 L36 50 L52 64 L70 42 L86 78 Z" fill="currentColor" opacity=".55"/>',
        "video": '<path d="M38 28 L72 50 L38 72 Z" fill="currentColor" opacity=".75"/>',
        "demo":  '<rect x="14" y="22" width="72" height="48" rx="6" fill="none" stroke="currentColor" stroke-width="3" opacity=".7"/><path d="M30 80 L50 80 L48 70 L32 70 Z" fill="currentColor" opacity=".7"/><circle cx="68" cy="46" r="4" fill="currentColor"/>',
    }[kind]

    caption_short = caption if len(caption) <= 64 else caption[:61] + "…"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{base}"/>
      <stop offset="1" stop-color="{accent}"/>
    </linearGradient>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#1a1a1a" opacity=".10"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#g)"/>
  <rect width="100%" height="100%" fill="url(#dots)"/>
  <g transform="translate({w//2 - 320}, {h//2 - 140})" fill="#1a1a1a">
    <text x="0" y="0" font-family="Inter, system-ui, sans-serif" font-size="22" font-weight="500" letter-spacing="3" opacity=".55">{kind_label.upper()} · {project_id.upper()}</text>
    <text x="0" y="80" font-family="'Source Serif 4', Georgia, serif" font-size="68" font-weight="600">{name}</text>
    <text x="0" y="140" font-family="Inter, system-ui, sans-serif" font-size="26" opacity=".7">{caption_short}</text>
    <text x="0" y="220" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="18" opacity=".5">sample · public demo</text>
  </g>
  <g transform="translate(60, 60)" color="#1a1a1a">{glyph}</g>
</svg>
'''


# (path under assets/, caption, kind)
MANIFEST = [
    ("p1/teacher-portal.svg", "Pulse Survey, embedded in-product", "video"),

    ("p2/suggested.svg", "Feedback graph overview", "image"),
    ("p2/knowledge-gaps.svg", "What unstructured feedback hides", "image"),
    ("p2/snippet-example.svg", "A structured feedback node", "image"),

    ("p3/hub.svg", "Insights Surface cover", "video"),
    ("p3/knowledge-hub-demo-2.svg", "Themes adapt to product area", "demo"),
    ("p3/context-and-assetes-gallery.svg", "Themed feed by signal", "image"),
    ("p3/context-and-assetes-tag.svg", "Themes drillable to quotes", "image"),
    ("p3/context-popover-demo.svg", "One-tap export to Linear", "demo"),
    ("p3/knowledge-hub-demo.svg", "Customer-facing changelog", "demo"),

    ("p4/sequences.svg", "Theme Sequencer cover", "video"),
    ("p4/training-center-topics.svg", "Tag feedback, watch suggestions update", "demo"),
    ("p4/training-center-demo.svg", "Manual tagging UI", "demo"),
    ("p4/training-center-brief.svg", "Theme drift visualization", "demo"),
    ("p4/training-center-improve.svg", "Confidence-scored suggestions", "demo"),
    ("p4/training-center-sequences.svg", "Theme history, traced", "demo"),
    ("p4/training-center-cot.svg", "Single feedback's theme trace", "demo"),

    ("p5/this-portfolio.svg", "Portfolio cover", "video"),
    ("p5/portfolio-home.svg", "Portfolio home", "image"),
    ("p5/prompt-to-portfolio-demo.svg", "Prompt to portfolio", "demo"),

    ("p6/dashboard.svg", "Portfolio health dashboard", "image"),
    ("p6/insights-home.svg", "Pulse Dashboard home", "image"),
    ("p6/scorecard.svg", "Per-account health card", "image"),
    ("p6/classification-states.svg", "Three account states", "image"),
    ("p6/enrichment-query.svg", "Natural-language query", "image"),
    ("p6/tracker-board.svg", "CS watchlist", "image"),

    ("p7/home-before-after.svg", "Onboarding, before/after", "image"),
    ("p7/activity-redesign.svg", "Step 2 — one habit, one tap", "image"),
    ("p7/payment-flow.svg", "Day-seven review prompt", "image"),
    ("p7/autopay-flow.svg", "Adding a second habit in-app", "image"),

    ("p9/personal-page.svg", "Profile with weekend builds", "image"),
    ("p9/quiz-show.svg", "Changelog page template", "video"),
    ("p9/invitation.svg", "Waitlist landing template", "video"),
    ("p9/scroll-site.svg", "SaaS pricing template", "video"),

    ("p10/care-app.svg", "Forge Docs cover", "video"),
    ("p10/care-demo.svg", "Search-first docs", "demo"),
    ("p10/exercise-demo.svg", "Copy-friendly code blocks", "demo"),
    ("p10/dashboard.svg", "Author dashboard", "image"),
    ("p10/protocol-builder.svg", "Live preview alongside markdown", "demo"),
    ("p10/unit-builder.svg", "Add a framework variant", "demo"),

    ("p11/card-app.svg", "Weekly Streaks cover", "video"),
    ("p11/activation-demo.svg", "Five-of-seven counts", "demo"),
    ("p11/popovers-demo.svg", "Reactivation prompt", "demo"),

    ("p12/home.svg", "Tessera product surface", "image"),
    ("p12/trackers-demo.svg", "Watchlists", "demo"),
    ("p12/scorecards-demo.svg", "Scorecards", "demo"),
    ("p12/snippets-demo.svg", "Themes", "demo"),
    ("p12/notices-demo.svg", "Notices", "demo"),
    ("p12/dashboard.svg", "Pulse dashboard", "video"),

]


def main():
    written = 0
    for rel, caption, kind in MANIFEST:
        project_id = rel.split("/", 1)[0]
        out = ASSETS / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(svg(project_id, caption, kind))
        written += 1

    # Identity placeholders (portrait, og image)
    portrait = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="pg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#e9b5a0"/>
      <stop offset="1" stop-color="#d97757"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="#f5f3ee"/>
  <circle cx="200" cy="200" r="190" fill="url(#pg)"/>
  <circle cx="200" cy="160" r="60" fill="#fbf9f4"/>
  <path d="M90 320 C 90 240, 310 240, 310 320 L 310 400 L 90 400 Z" fill="#fbf9f4"/>
  <text x="200" y="380" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="22" fill="#1a1a1a" opacity=".7">Riley Quinn</text>
</svg>
'''
    (ASSETS / "portrait.svg").write_text(portrait)

    og = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630">
  <defs>
    <linearGradient id="og" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f5f3ee"/>
      <stop offset="1" stop-color="#e9b5a0"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#og)"/>
  <text x="80" y="280" font-family="'Source Serif 4', Georgia, serif" font-size="74" font-weight="600" fill="#1a1a1a">Riley Quinn</text>
  <text x="80" y="350" font-family="Inter, system-ui, sans-serif" font-size="32" fill="#4a4744">Senior Product Designer · 10 yrs · Lisbon</text>
  <text x="80" y="400" font-family="Inter, system-ui, sans-serif" font-size="22" fill="#8a857e">Selected work 2017–2026 · public demo portfolio</text>
</svg>
'''
    (ASSETS / "og.svg").write_text(og)

    print(f"Wrote {written + 2} SVG placeholders")


if __name__ == "__main__":
    main()
