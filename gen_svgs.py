import random, sys, os
from xml.sax.saxutils import escape

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
random.seed(18)

G = "#00FF41"
FONT = "'Fira Code','JetBrains Mono','SF Mono',Menlo,Consolas,'Courier New',monospace"

# ---------------------------------------------------------------- banner
W, H = 1000, 280
chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノ$#@%&*<>/\\{}[]"
cols = []
step = 20
for i, x in enumerate(range(6, W, step)):
    n = random.randint(10, 18)
    s = "".join(random.choice(chars) for _ in range(n))
    dur = random.uniform(3.5, 9)
    delay = -random.uniform(0, dur)
    op = random.uniform(0.25, 0.75)
    spans = []
    for j, c in enumerate(s):
        y = j * 18
        fill = "#CCFFDD" if j == n - 1 else G
        o = 1 if j == n - 1 else round(0.15 + 0.85 * j / n, 2)
        spans.append(f'<text x="{x}" y="{y}" fill="{fill}" fill-opacity="{o}">{escape(c)}</text>')
    cols.append(
        f'<g class="col" style="animation-duration:{dur:.2f}s;animation-delay:{delay:.2f}s;opacity:{op:.2f}">'
        + "".join(spans) + "</g>")

banner = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .rain text {{ font: 15px {FONT}; }}
  .col {{ animation-name: fall; animation-iteration-count: infinite; animation-timing-function: linear; }}
  @keyframes fall {{ from {{ transform: translateY(-340px); }} to {{ transform: translateY({H + 20}px); }} }}
  .title {{ font: 700 72px {FONT}; letter-spacing: 6px; }}
  .sub {{ font: 500 18px {FONT}; letter-spacing: 3px; }}
  .g1 {{ animation: g1 3s infinite steps(1); }}
  .g2 {{ animation: g2 3s infinite steps(1); }}
  .main {{ animation: flick 6s infinite; }}
  @keyframes g1 {{ 0%,86%,100% {{ transform: translate(0,0); opacity:0 }} 87% {{ transform: translate(-6px,2px); opacity:.9 }} 90% {{ transform: translate(5px,-2px); opacity:.9 }} 93% {{ transform: translate(-3px,0); opacity:.9 }} 96% {{ opacity:0 }} }}
  @keyframes g2 {{ 0%,86%,100% {{ transform: translate(0,0); opacity:0 }} 87% {{ transform: translate(6px,-2px); opacity:.9 }} 90% {{ transform: translate(-5px,2px); opacity:.9 }} 93% {{ transform: translate(3px,1px); opacity:.9 }} 96% {{ opacity:0 }} }}
  @keyframes flick {{ 0%,40%,44%,100% {{ opacity:1 }} 42% {{ opacity:.4 }} }}
  .scan {{ animation: scan 4s linear infinite; }}
  @keyframes scan {{ from {{ transform: translateY(-40px) }} to {{ transform: translateY({H}px) }} }}
  .cur {{ animation: blink 1s steps(1) infinite; }}
  @keyframes blink {{ 50% {{ fill-opacity: 0 }} }}
</style>
<defs>
  <pattern id="lines" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="2" fill="#000" fill-opacity=".35"/></pattern>
  <radialGradient id="vig" cx="50%" cy="50%" r="70%"><stop offset="55%" stop-color="#000" stop-opacity="0"/><stop offset="100%" stop-color="#000" stop-opacity=".9"/></radialGradient>
  <linearGradient id="beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{G}" stop-opacity="0"/><stop offset="1" stop-color="{G}" stop-opacity=".12"/></linearGradient>
  <filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <clipPath id="r"><rect width="{W}" height="{H}" rx="14"/></clipPath>
</defs>
<g clip-path="url(#r)">
  <rect width="{W}" height="{H}" fill="#020a04"/>
  <g class="rain">{"".join(cols)}</g>
  <rect x="200" y="70" width="600" height="140" fill="#020a04" fill-opacity=".72" rx="6"/>
  <g text-anchor="middle">
    <text class="title g1" x="{W/2}" y="152" fill="#ff0055">CORONATI-18</text>
    <text class="title g2" x="{W/2}" y="152" fill="#00e5ff">CORONATI-18</text>
    <text class="title main" x="{W/2}" y="152" fill="{G}" filter="url(#glow)">CORONATI-18</text>
    <text class="sub" x="{W/2}" y="190" fill="#9dffb8">// low-level &amp; curious · C · Python<tspan class="cur" fill="{G}">_</tspan></text>
  </g>
  <rect class="scan" width="{W}" height="40" fill="url(#beam)"/>
  <rect width="{W}" height="{H}" fill="url(#lines)"/>
  <rect width="{W}" height="{H}" fill="url(#vig)"/>
</g>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="none" stroke="{G}" stroke-opacity=".5" stroke-width="2"/>
</svg>'''
open(os.path.join(OUT, "banner.svg"), "w").write(banner)

# ---------------------------------------------------------------- terminal / neofetch
TW = 1000
ghost = [
    "       ▄▄██████▄▄       ",
    "     ▄████████████▄     ",
    "    ██▀▀▀████▀▀▀████    ",
    "    █  ▄▄ ██  ▄▄ ███    ",
    "    █  ██ ██  ██ ███    ",
    "    ██▄▄▄████▄▄▄████    ",
    "    ████████████████    ",
    "    ████████████████    ",
    "    ██▀ ▀██▀▀██▀ ▀██    ",
    "    ▀     ▀  ▀     ▀    ",
]
info = [
    ("coronati-18", "@github", None),
    ("─" * 22, None, None),
    ("User", "coronati-18", "k"),
    ("Location", "Europe 🌍", "k"),
    ("Kernel", "brain v18.0-caffeinated", "k"),
    ("Shell", "zsh · vim · gcc", "k"),
    ("Languages", "C · Python · Java", "k"),
    ("Focus", "algorithms · memory mgmt", "k"),
    ("Uptime", "since the first segfault", "k"),
    ("Motto", "malloc() it. free() it.", "k"),
]

LH = 24
top = 50
y0 = top + 46
parts = []
t = 0.3
# prompt line 1 typed
cmd1 = "neofetch --hacker"
parts.append(f'<text x="28" y="{y0}" class="p">coronati-18@github<tspan fill="#c9d1d9">:</tspan><tspan fill="#58a6ff">~</tspan><tspan fill="#c9d1d9">$ </tspan></text>')
cx = 28 + 9.6 * len("coronati-18@github:~$ ")
parts.append(f'<g><text x="{cx:.1f}" y="{y0}" class="c">{cmd1}</text>'
             f'<rect x="{cx-1:.1f}" y="{y0-17}" width="{9.6*len(cmd1)+4:.1f}" height="24" fill="#0d1117" class="type" style="--w:{9.6*len(cmd1)+4:.1f}px;animation-delay:{t}s;animation-duration:{len(cmd1)*0.06:.2f}s;animation-timing-function:steps({len(cmd1)})"/></g>')
t += len(cmd1) * 0.06 + 0.4

body_y = y0 + 38
GRID = [
    "....XXXXXX....",
    "..XXXXXXXXXX..",
    ".XXXXXXXXXXXX.",
    ".XWWXXXXWWXXX.",
    "XWWWWXXWWWWXXX",
    "XWWPPXXWWPPXXX",
    "XWWPPXXWWPPXXX",
    "XXWWXXXXWWXXXX",
    "XXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX",
    "XX.XXX..XXX.XX",
    "X...XX..XX...X",
]
px = 16
gx, gy = 70, body_y - 14
cells = []
for r, row in enumerate(GRID):
    for c, ch in enumerate(row):
        if ch == ".": continue
        col = {"X": G, "W": "#e6fff0", "P": "#0d1117"}[ch]
        cells.append(f'<rect x="{c*px}" y="{r*px}" width="{px}" height="{px}" fill="{col}"/>')
parts.append(f'<g class="fade" style="animation-delay:{t:.2f}s"><g transform="translate({gx},{gy})"><g class="float" filter="url(#gl)">{"".join(cells)}</g></g></g>')
t += 0.3
ix = 360
for i, (a, b, kind) in enumerate(info):
    y = body_y + i * LH
    d = t + i * 0.18
    if kind == "k":
        parts.append(f'<text x="{ix}" y="{y}" class="fade" style="animation-delay:{d:.2f}s"><tspan class="k">{escape(a)}</tspan><tspan fill="#c9d1d9">: {escape(b)}</tspan></text>')
    elif b:
        parts.append(f'<text x="{ix}" y="{y}" class="fade k b" style="animation-delay:{d:.2f}s">{escape(a)}<tspan fill="#c9d1d9">{escape(b)}</tspan></text>')
    else:
        parts.append(f'<text x="{ix}" y="{y}" class="fade" fill="#3a3f47" style="animation-delay:{d:.2f}s">{escape(a)}</text>')
t += len(info) * 0.18
# color blocks
cy = body_y + len(info) * LH - 6
colors = ["#000000", "#ff0055", G, "#ffd700", "#58a6ff", "#bc8cff", "#00e5ff", "#c9d1d9"]
for i, c in enumerate(colors):
    parts.append(f'<rect x="{ix + i*30}" y="{cy}" width="30" height="18" fill="{c}" class="fade" style="animation-delay:{t:.2f}s"/>')
t += 0.6

# line 2: exploit progress
y2 = cy + 62
cmd2 = "./hack --target=future"
parts.append(f'<text x="28" y="{y2}" class="p fade" style="animation-delay:{t:.2f}s">coronati-18@github<tspan fill="#c9d1d9">:</tspan><tspan fill="#58a6ff">~</tspan><tspan fill="#c9d1d9">$ </tspan></text>')
t += 0.2
parts.append(f'<g class="fade" style="animation-delay:{t:.2f}s;animation-duration:.01s"><text x="{cx:.1f}" y="{y2}" class="c">{cmd2}</text>'
             f'<rect x="{cx-1:.1f}" y="{y2-17}" width="{9.6*len(cmd2)+4:.1f}" height="24" fill="#0d1117" class="type" style="--w:{9.6*len(cmd2)+4:.1f}px;animation-delay:{t:.2f}s;animation-duration:{len(cmd2)*0.06:.2f}s;animation-timing-function:steps({len(cmd2)})"/></g>')
t += len(cmd2) * 0.06 + 0.4
y3 = y2 + LH + 4
parts.append(f'<text x="28" y="{y3}" class="fade dim" style="animation-delay:{t:.2f}s">[*] bypassing sleep schedule ............ <tspan fill="{G}">OK</tspan></text>')
t += 0.5
parts.append(f'<text x="28" y="{y3+LH}" class="fade dim" style="animation-delay:{t:.2f}s">[*] injecting coffee into /dev/brain ..... <tspan fill="{G}">OK</tspan></text>')
t += 0.5
y5 = y3 + 2 * LH
barw = 400
parts.append(f'<text x="28" y="{y5}" class="fade dim" style="animation-delay:{t:.2f}s">[*] compiling skills</text>')
parts.append(f'<rect x="260" y="{y5-14}" width="{barw}" height="16" fill="none" stroke="{G}" stroke-opacity=".6" class="fade" style="animation-delay:{t:.2f}s"/>')
parts.append(f'<rect x="262" y="{y5-12}" width="{barw-4}" height="12" fill="{G}" class="bar" style="animation-delay:{t:.2f}s"/>')
parts.append(f'<text x="{260+barw+14}" y="{y5}" fill="{G}" class="fade" style="animation-delay:{t+2.6:.2f}s">100% · ACCESS GRANTED</text>')
t += 3.0
y6 = y5 + LH + 10
parts.append(f'<text x="28" y="{y6}" class="p fade" style="animation-delay:{t:.2f}s">coronati-18@github<tspan fill="#c9d1d9">:</tspan><tspan fill="#58a6ff">~</tspan><tspan fill="#c9d1d9">$ </tspan></text>')
parts.append(f'<rect x="{cx:.1f}" y="{y6-16}" width="10" height="20" fill="{G}" class="fade cur" style="animation-delay:{t:.2f}s,0s"/>')

TH = y6 + 30
term = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{TW}" height="{TH}" viewBox="0 0 {TW} {TH}">
<style>
  text {{ font: 16px {FONT}; fill: #c9d1d9; }}
  .p {{ fill: {G}; font-weight: 700; }}
  .c {{ fill: #ffffff; }}
  .k {{ fill: {G}; font-weight: 700; }}
  .b {{ font-weight: 700; }}
  .dim {{ fill: #8b949e; }}
  .ghost {{ fill: {G}; font-size: 17px; }}
  .fade {{ opacity: 0; animation: show .3s ease forwards; }}
  @keyframes show {{ to {{ opacity: 1; }} }}
  .type {{ transform-box: fill-box; transform-origin: right; animation-name: type; animation-fill-mode: both; }}
  @keyframes type {{ from {{ transform: scaleX(1); }} to {{ transform: scaleX(0); }} }}
  .bar {{ transform-box: fill-box; transform-origin: left; transform: scaleX(0); animation: bar 2.6s cubic-bezier(.6,.1,.3,1) forwards; }}
  @keyframes bar {{ 0% {{ transform: scaleX(0) }} 30% {{ transform: scaleX(.35) }} 55% {{ transform: scaleX(.42) }} 100% {{ transform: scaleX(1) }} }}
  .float {{ animation: float 2.4s ease-in-out infinite; }}
  @keyframes float {{ 50% {{ transform: translateY(-8px); }} }}
  .cur {{ animation: show .1s forwards, blink 1s steps(1) infinite; }}
  @keyframes blink {{ 50% {{ fill-opacity: 0; }} }}
</style>
<defs><filter id="gl" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
<rect x="1" y="1" width="{TW-2}" height="{TH-2}" rx="12" fill="#0d1117" stroke="{G}" stroke-opacity=".45" stroke-width="2"/>
<path d="M1 13a12 12 0 0 1 12-12h{TW-26}a12 12 0 0 1 12 12v27H1z" fill="#161b22"/>
<line x1="1" y1="40" x2="{TW-1}" y2="40" stroke="{G}" stroke-opacity=".25"/>
<circle cx="26" cy="21" r="7" fill="#ff5f56"/><circle cx="50" cy="21" r="7" fill="#ffbd2e"/><circle cx="74" cy="21" r="7" fill="#27c93f"/>
<text x="{TW/2}" y="26" text-anchor="middle" style="font-size:14px;fill:#8b949e">coronati-18@github: ~ — zsh — 120×40</text>
{"".join(parts)}
</svg>'''
open(os.path.join(OUT, "terminal.svg"), "w").write(term)
print("ok", TH)
