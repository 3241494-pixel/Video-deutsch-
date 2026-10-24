# Генерує дитячий кліп «Hallo, ABC!» (HyperFrames): python gen.py v|h  -> proj/index.html або proj_h/index.html
import json, html, re, sys, math, os, shutil
sys.path.insert(0, "/home/user/abc")
from uk import UK, WORDS, NAMES
from chars import C

MODE = sys.argv[1] if len(sys.argv) > 1 else "v"
D = 144.0
L = json.load(open("/home/user/abc/lines.json")); assert len(L) == len(UK)
PAL = ["#FF6B6B", "#FF922B", "#FAB005", "#51CF66", "#20C997", "#339AF0", "#5C7CFA", "#845EF7", "#F06595"]
ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
col = lambda ch: PAL[(ALPHA.index(ch) if ch in ALPHA else "ÄÖÜß".index(ch) + 3) % len(PAL)]
def norm(w): return re.sub(r"[^a-zäöüß]", "", w.lower())

if MODE == "v":
    W, H, OUT = 1080, 1920, "/home/user/abc/proj"
    P = dict(tile=(340, 190, 400), lname=(770, 230), char=(170, 630, 740), word=1300, caps=(40, 1530, 62, 42),
             grid=(65, 230, 6, 140, 22, 96), gsun=(350, 1050, 380), title=(0, 260, 170), isun=(200, 700, 680), btile=(70, 560, 210, 40))
    CSS = """  #chip { top: 70px; left: 60px; } #legend { left: 60px; top: 1785px; } #bar { left: 60px; right: 60px; top: 1870px; }
  .caps { left: 40px; right: 40px; top: 1530px; height: 250px; }
  #hill1 { top: 1480px; height: 800px; } #hill2 { top: 1580px; height: 700px; }"""
else:
    W, H, OUT = 1920, 1080, "/home/user/abc/proj_h"
    P = dict(tile=(200, 130, 330), lname=(570, 190), char=(1120, 80, 700), word=(80, 940, 530), caps=(100, 835, 54, 36),
             grid=(90, 150, 9, 120, 18, 84), gsun=(1440, 140, 420), title=(80, 230, 150), isun=(1180, 90, 640), btile=(250, 260, 260, 50))
    CSS = """  #chip { top: 36px; left: 60px; } #legend { right: 60px; top: 36px; } #bar { left: 60px; right: 60px; top: 1050px; height: 12px; }
  .caps { left: 100px; right: 100px; top: 835px; height: 200px; } .word { text-align: left; }
  #hill1 { top: 820px; height: 600px; width: 60%; } #hill2 { top: 880px; height: 500px; width: 60%; }"""

def svg(key, cls=""):
    return f'<svg viewBox="0 0 400 400" class="{cls}">{C[key]}</svg>'

# сцени: групи рядків
scenes = []
i = 0
while i < len(L):
    t = L[i]["text"]
    if t.startswith("A, B, C"): scenes.append(("chorus", list(range(i, i + 4)))); i += 4; continue
    if i <= 1: scenes.append(("intro", [0, 1])); i = 2; continue
    if i >= len(L) - 2: scenes.append(("outro", [len(L) - 2, len(L) - 1])); break
    if t.startswith("Und noch vier"): scenes.append(("bridge", [i])); i += 1; continue
    scenes.append(("letter", [i])); i += 1
starts = [L[ks[0]]["start"] for _, ks in scenes]
show = [0 if n == 0 else starts[n] - .3 for n in range(len(scenes))]
hide = [show[n + 1] if n + 1 < len(scenes) else D for n in range(len(scenes))]

js, html_sc = [], []
def J(s): js.append(s)
def idle(sel, a, b):
    # м'яке похитування персонажа протягом сцени
    n = max(1, int((b - a) / .6))
    J(f'tl.fromTo("{sel}",{{rotation:-4}},{{rotation:4,duration:.6,yoyo:true,repeat:{n},ease:"sine.inOut",transformOrigin:"50% 90%"}},{a:.3f});')
def parts(sel, a, b):
    n = max(1, int((b - a) / .25))
    J(f'tl.fromTo("{sel} .wing",{{scaleY:1}},{{scaleY:.7,duration:.12,yoyo:true,repeat:{n*2},transformOrigin:"50% 100%"}},{a:.3f});')
    J(f'tl.fromTo("{sel} .rays",{{rotation:0}},{{rotation:30,duration:{b-a:.2f},ease:"none",transformOrigin:"200px 200px"}},{a:.3f});')
    J(f'tl.fromTo("{sel} .flame",{{scaleY:1}},{{scaleY:1.35,duration:.1,yoyo:true,repeat:{n*2},transformOrigin:"200px 300px"}},{a:.3f});')
    J(f'tl.fromTo("{sel} .yo",{{y:0}},{{y:60,duration:.3,yoyo:true,repeat:{n},ease:"sine.inOut"}},{a:.3f});')
    J(f'tl.fromTo("{sel} .hand",{{rotation:0}},{{rotation:360,duration:{b-a:.2f},ease:"none",transformOrigin:"200px 210px"}},{a:.3f});')
    J(f'tl.fromTo("{sel} .spout",{{scale:.6,opacity:.4}},{{scale:1.1,opacity:1,duration:.3,yoyo:true,repeat:{n},transformOrigin:"200px 90px"}},{a:.3f});')
    J(f'tl.fromTo("{sel} .tent",{{skewX:-6}},{{skewX:6,duration:.35,yoyo:true,repeat:{n},ease:"sine.inOut",transformOrigin:"200px 230px"}},{a:.3f});')
    J(f'tl.fromTo("{sel} .stick",{{rotation:-12}},{{rotation:12,duration:.15,yoyo:true,repeat:{n*2},transformOrigin:"300px 40px"}},{a:.3f});')
    J(f'tl.fromTo("{sel} .tail",{{rotation:-8}},{{rotation:8,duration:.3,yoyo:true,repeat:{n},transformOrigin:"300px 300px"}},{a:.3f});')
    J(f'tl.fromTo("{sel} .glow",{{opacity:.3}},{{opacity:.9,duration:.3,yoyo:true,repeat:{n}}},{a:.3f});')
    J(f'tl.fromTo("{sel} .mane",{{rotation:-6}},{{rotation:6,duration:.3,yoyo:true,repeat:{n},transformOrigin:"200px 205px"}},{a:.3f});')
    J(f'tl.fromTo("{sel} .flap",{{rotation:0}},{{rotation:-25,duration:.2,yoyo:true,repeat:{n},transformOrigin:"100px 210px"}},{a:.3f});')
    # моргання
    J(f'tl.to("{sel} .eye",{{scaleY:.1,duration:.07,yoyo:true,repeat:1,transformOrigin:"50% 50%"}},{a + (b-a)*.6:.3f});')

def tile_html(id_, ch, x, y, s, extra=""):
    low = ch.lower() if ch != "ß" else ""
    inner = f'{ch}<small>{low}</small>' if low and low != ch else ch
    return f'<div class="tile" id="{id_}" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;font-size:{s*.62:.0f}px;background:{col(ch)}{extra}">{inner}</div>'

def sparks(id_, cx, cy, t):
    out = []
    for k in range(10):
        a = k * math.pi / 5; c = PAL[k % len(PAL)]
        out.append(f'<div class="spark" id="{id_}s{k}" style="left:{cx-13}px;top:{cy-13}px;background:{c}"></div>')
        J(f'tl.fromTo("#{id_}s{k}",{{x:0,y:0,opacity:1,scale:1}},{{x:{170*math.cos(a):.0f},y:{170*math.sin(a):.0f},opacity:0,scale:.3,duration:.7,ease:"power2.out",immediateRender:false}},{t:.3f});')
    return "".join(out)

for n, (kind, ks) in enumerate(scenes):
    a, b = show[n], hide[n]; sid = f"sc{n}"; body = ""
    if kind == "letter":
        l = L[ks[0]]; ch = next((c for c in l["text"][:6] if c in "ÄÖÜß"), l["text"][0])  # літера лише з початку рядка (у «Spaß» теж є ß)
        art, word, key, ukw = WORDS[ch]
        tx, ty, ts = P["tile"]; cx, cy, cs = P["char"]
        body += tile_html(f"{sid}t", ch, tx, ty, ts)
        body += f'<div class="lname" id="{sid}n" style="left:{P["lname"][0]}px;top:{P["lname"][1]}px">sprich: <span>{NAMES[ch]}</span></div>'
        body += f'<div class="char" id="{sid}c" style="left:{cx}px;top:{cy}px;width:{cs}px;height:{cs}px">{svg(key)}</div>'
        if MODE == "v": wst = f"left:0;right:0;top:{P['word']}px"
        else: wst = f"left:{P['word'][0]}px;width:{P['word'][1]}px;top:{P['word'][2]}px"
        body += f'<div class="word" id="{sid}w" style="{wst}"><div class="de"><span class="{art}">{art}</span> {html.escape(word)}</div><div class="uk">{ukw}</div></div>'
        # час слова: перший токен, що збігається зі словом
        toks = [norm(x) for x in l["text"].split() if norm(x)]
        wt = next((l["t"][j][0] for j, x in enumerate(toks) if x == norm(word) or x == norm(word).replace("jojo", "jojo")), a + .9)
        body += sparks(sid, (cx + cs / 2) if MODE == "v" else (cx + cs / 2), cy + cs * .45, wt)
        J(f'tl.fromTo("#{sid}t",{{scale:0,rotation:-25}},{{scale:1,rotation:0,duration:.45,ease:"back.out(2.2)"}},{a:.3f});')
        J(f'tl.fromTo("#{sid}n",{{opacity:0,x:40}},{{opacity:1,x:0,duration:.3}},{a+.2:.3f});')
        for j, x in enumerate(toks):
            if x == norm(ch) and j < 4 and l["t"][j][0] > a + .3:
                J(f'tl.fromTo("#{sid}t",{{y:0}},{{y:-40,duration:.13,yoyo:true,repeat:1,ease:"power1.out"}},{l["t"][j][0]:.3f});')
        J(f'tl.fromTo("#{sid}c",{{scale:0,y:120}},{{scale:1,y:0,duration:.5,ease:"back.out(1.8)"}},{a+.15:.3f});')
        idle(f"#{sid}c svg", a + .7, b); parts(f"#{sid}c", a, b)
        J(f'tl.fromTo("#{sid}w",{{opacity:0,scale:.6}},{{opacity:1,scale:1,duration:.35,ease:"back.out(2)"}},{max(a+.3, wt-.1):.3f});')
    elif kind == "chorus":
        gx, gy, cols, s, gap, fs = P["grid"]
        cells = "".join(f'<div class="gt" id="{sid}g{c}" style="width:{s}px;height:{s}px;font-size:{fs}px">{c}</div>' for c in ALPHA)
        body += f'<div class="grid" id="{sid}grid" style="left:{gx}px;top:{gy}px;grid-template-columns:repeat({cols},{s}px);gap:{gap}px">{cells}</div>'
        sx, sy, ss = P["gsun"]
        body += f'<div class="char" id="{sid}c" style="left:{sx}px;top:{sy}px;width:{ss}px;height:{ss}px">{svg("sonne")}</div>'
        J(f'tl.fromTo("#{sid} .gt",{{scale:0}},{{scale:1,duration:.3,stagger:.015,ease:"back.out(2)"}},{a:.3f});')
        J(f'tl.fromTo("#{sid}c",{{scale:0}},{{scale:1,duration:.5,ease:"back.out(1.8)"}},{a+.2:.3f});')
        idle(f"#{sid}c svg", a + .7, b); parts(f"#{sid}c", a, b)
        for k in ks:
            l = L[k]
            for j, x in enumerate(l["text"].replace("—", " ").split()):
                pass
            toks = [x for x in l["text"].split() if norm(x)]
            for x, t in zip(toks, l["t"]):
                c = re.sub(r"[^A-Z]", "", x)
                if len(c) == 1 and c in ALPHA:
                    J(f'tl.to("#{sid}g{c}",{{backgroundColor:"{col(c)}",color:"#fff",duration:.1}},{t[0]:.3f});')
                    J(f'tl.fromTo("#{sid}g{c}",{{scale:1}},{{scale:1.25,duration:.12,yoyo:true,repeat:1,ease:"power1.out"}},{t[0]:.3f});')
                elif norm(x) == "juchhe":
                    J(f'tl.fromTo("#{sid} .gt",{{y:0}},{{y:-30,duration:.15,yoyo:true,repeat:1,stagger:.02}},{t[0]:.3f});')
    elif kind in ("intro", "outro"):
        tx, ty, tf = P["title"]
        txt = '<b>Hallo,</b><br><i>A</i><u>B</u><b>C</b>!' if kind == "intro" else '<b>Tschüss!</b><br><i>Bis</i> <u>morgen!</u>'
        tst = f"left:0;right:0;top:{ty}px;font-size:{tf}px" if MODE == "v" else f"left:{tx}px;width:1000px;top:{ty}px;font-size:{tf}px"
        body += f'<div class="title" id="{sid}h" style="{tst}">{txt}</div>'
        sx, sy, ss = P["isun"]
        body += f'<div class="char" id="{sid}c" style="left:{sx}px;top:{sy}px;width:{ss}px;height:{ss}px">{svg("sonne")}</div>'
        J(f'tl.fromTo("#{sid}h",{{scale:0,rotation:-10}},{{scale:1,rotation:0,duration:.6,ease:"back.out(2)"}},{a+.1:.3f});')
        J(f'tl.fromTo("#{sid}h",{{y:0}},{{y:-20,duration:.5,yoyo:true,repeat:{max(1,int((b-a)/.5)-2)},ease:"sine.inOut"}},{a+.7:.3f});')
        J(f'tl.fromTo("#{sid}c",{{scale:0,y:200}},{{scale:1,y:0,duration:.7,ease:"back.out(1.6)"}},{a+.3:.3f});')
        idle(f"#{sid}c svg", a + 1, b); parts(f"#{sid}c", a, b)
    elif kind == "bridge":
        bx, by, bs, bg = P["btile"]
        for j, ch in enumerate("ÄÖÜß"):
            body += tile_html(f"{sid}t{j}", ch, bx + j * (bs + bg), by, bs)
            J(f'tl.fromTo("#{sid}t{j}",{{scale:0,rotation:-30}},{{scale:1,rotation:0,duration:.4,ease:"back.out(2.2)"}},{a + .25 + j*.35:.3f});')
    html_sc.append(f'<div class="scene" id="{sid}">{body}</div>')
    J(f'tl.set("#{sid}",{{opacity:1}},{a:.3f}); tl.set("#{sid}",{{opacity:0}},{b:.3f});')

# караоке внизу
caps = []
cx_, cy_, cf, cu = P["caps"]
for k, l in enumerate(L):
    toks = l["text"].split(); ti = 0; ws = []
    for t in toks:
        if not norm(t): ws.append(f'<span class="w" style="color:#CED4DA">{html.escape(t)}</span>'); continue
        wid = f"k{k}_{ti}"; st = l["t"][ti][0]; ti += 1
        m = re.match(r"^([A-ZÄÖÜß])[,!]?$", t)
        cl = col(m.group(1)) if m else "#3B2F2F"
        ws.append(f'<span class="w" id="{wid}">{html.escape(t)}</span>')
        J(f'tl.to("#{wid}",{{color:"{cl}",duration:.08}},{st:.3f});')
        J(f'tl.fromTo("#{wid}",{{y:0}},{{y:-12,duration:.1,yoyo:true,repeat:1}},{st:.3f});')
    u = f'<div class="u" style="font-size:{cu}px">{html.escape(UK[k])}</div>' if UK[k] else ""
    caps.append(f'<div class="cue" id="q{k}"><div class="ln" style="font-size:{cf}px">{" ".join(ws)}</div>{u}</div>')
    a = 0 if k == 0 else L[k]["start"] - .25
    b = L[k+1]["start"] - .25 if k + 1 < len(L) else D - .5
    b = min(b, L[k]["end"] + 2.5)
    J(f'tl.fromTo("#q{k}",{{opacity:0,y:20}},{{opacity:1,y:0,duration:.18}},{a:.3f}); tl.to("#q{k}",{{opacity:0,duration:.12}},{b-.12:.3f});')

# фон: хмари, пагорби, квіти
bg = []
for j, (x, y, w) in enumerate([(80, 420, 220), (700, 300, 260), (380, 900, 180), (1500, 200, 240), (1300, 560, 200)]):
    if MODE == "v" and x > 1000: x = x - 900
    bg.append(f'<div class="cloud" id="cl{j}" style="left:{x}px;top:{y if MODE == "v" else y*.55:.0f}px;width:{w}px;height:{w*.38:.0f}px"></div>')
    J(f'tl.fromTo("#cl{j}",{{x:0}},{{x:{160 if j % 2 else -160},duration:D,ease:"sine.inOut"}},0);')
bg.append('<div id="hill1"></div><div id="hill2"></div>')
fl = [(60, 1700), (930, 1650), (500, 1820)] if MODE == "v" else [(1780, 940), (40, 960), (900, 1000)]
for j, (x, y) in enumerate(fl):
    bg.append(f'<div class="flower" id="fl{j}" style="left:{x}px;top:{y}px;font-size:70px">🌼</div>')
    J(f'tl.fromTo("#fl{j}",{{rotation:-10}},{{rotation:10,duration:.9,yoyo:true,repeat:Math.max(0,Math.floor(D/.9)-1),ease:"sine.inOut"}},0);')

tpl = open("/home/user/abc/template.html").read()
out = (tpl.replace("{{RES}}", "portrait" if MODE == "v" else "landscape").replace("{{W}}", str(W)).replace("{{H}}", str(H))
       .replace("{{D}}", str(D)).replace("{{CSS}}", CSS).replace("{{BG}}", "\n".join(bg))
       .replace("{{SCENES}}", "\n".join(html_sc)).replace("{{CAPS}}", "\n".join(caps)).replace("{{JS}}", "\n  ".join(js)))
os.makedirs(OUT, exist_ok=True)
for f in ["gsap.min.js", "hyperframes.json", "fredoka-latin-600-normal.woff2", "fredoka-latin-700-normal.woff2"]:
    if not os.path.exists(f"{OUT}/{f}"): shutil.copy(f"/home/user/abc/proj/{f}", OUT)
open(f"{OUT}/index.html", "w").write(out)
json.dump({"id": "abc_" + MODE, "name": "abc_" + MODE, "createdAt": "2026-10-23T18:10:00.000Z"}, open(f"{OUT}/meta.json", "w"))
print("ok", MODE, len(scenes), "scenes", len(js), "tweens")
