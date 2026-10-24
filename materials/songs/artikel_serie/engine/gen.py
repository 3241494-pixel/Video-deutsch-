# Генератор анимированного клипа серии «Артикли по окончаниям» (HyperFrames + GSAP)
# python gen.py EP_ID v|h [--fake]
#   читает ../EP_ID/lines.json (выравнивание текста по вокалу) и ../EP_ID/beats.json (биты песни);
#   --fake строит тайминги без песни (88 BPM) — для проверки анимации до получения трека
# результат: /home/user/artikel/EP_ID_v|h/index.html
import json, html, sys, os, shutil, math, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import series as S

EP_ID, MODE = sys.argv[1], sys.argv[2]
FAKE = "--fake" in sys.argv
E = next(e for e in S.EPISODES if e["id"] == EP_ID)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = "/home/user/artikel"
ASSETS = f"{WORK}/assets"
OUT = f"{WORK}/{EP_ID}_{MODE}"

# цвета артиклей (как в прошлых клипах: der синий, die красный, das зелёный)
ART = {"der": ("#1C6FD6", "#EAF2FF", "#CFE0FA"), "die": ("#E0313F", "#FFF0F1", "#FAD3D7"), "das": ("#1E9E52", "#EBF8F0", "#C9EBD6")}
C, BG, BG2 = ART[E["art"]]
INK, MUTED, UKC = "#232A3D", "#6B7390", "#2B63C6"

def norm(w): return re.sub(r"[^a-zäöüß]", "", w.lower())

# ---------- тайминги ----------
LYR = [l for l in S.lyrics(E).splitlines() if l.strip() and not l.startswith("[")]
if FAKE:
    beat = 60 / 88
    L, t = [], 2.0
    for k, text in enumerate(LYR):
        toks = [x for x in text.split() if norm(x)]
        ts = []
        for x in toks:
            d = beat * (0.5 if norm(x) in ("der", "die", "das") else 1.0)
            ts.append([round(t, 3), round(t + d * .9, 3)]); t += d
        L.append({"text": text, "t": ts, "start": ts[0][0], "end": ts[-1][1]}); t += beat * 2
    D = round(t + 8, 2)
    BEATS = [round(2.0 + i * beat, 3) for i in range(int((D - 2) / beat))]
else:
    L = json.load(open(f"{ROOT}/{EP_ID}/lines.json"))
    meta = json.load(open(f"{ROOT}/{EP_ID}/beats.json"))
    BEATS, D = meta["beats"], meta["duration"]
assert [x["text"] for x in L] == LYR, "lines.json не совпадает с текстом серии"

# раскладка строк: 2 строки интро, по 5 строк на блок, 2 строки финала
NB = len(E["blocks"])
blk_lines = [list(range(2 + 5 * i, 7 + 5 * i)) for i in range(NB)]
outro = [2 + 5 * NB, 3 + 5 * NB]

def tok_times(k):
    """[(токен, start)] для строки k, только словесные токены"""
    toks = [x for x in L[k]["text"].split() if norm(x)]
    return [(x, L[k]["t"][j][0]) for j, x in enumerate(toks)]

# ---------- геометрия ----------
if MODE == "v":
    W, H = 1080, 1920
    G = dict(hdr_x=60, hdr_w=960, q_y=180, pill_y=270, stamp_y=540, uk_y=450, list_x=60, list_y=790, row_h=160, cols=1, col_w=960,
             word_fs=76, uk_fs=38, icon=124, pill_fs=150, stamp_fs=104, q_fs=58)
else:
    W, H = 1920, 1080
    G = dict(hdr_x=90, hdr_w=700, q_y=180, pill_y=260, stamp_y=560, uk_y=450, list_x=850, list_y=150, row_h=270, cols=2, col_w=490,
             word_fs=60, uk_fs=32, icon=100, pill_fs=150, stamp_fs=78, q_fs=52)

js, scenes = [], []
def J(s): js.append(s)

def emoji(e, size, cls="ic"):
    return f'<span class="{cls}" style="font-size:{size}px">{e}</span>'

# ---------- интро ----------
def intro_scene():
    a, b = 0.0, L[blk_lines[0][0]]["start"] - .6
    tt = tok_times(0) + tok_times(1)
    body = '<div class="intro">'
    body += '<div class="ddd">' + "".join(f'<span id="i_{w}" class="big" style="color:{ART[w][0]}">{w.capitalize()}</span>' for w in ("der", "die", "das")) + '</div>'
    body += '<div class="iq" id="i_q">wer weiß das? <span class="emo">🤔</span></div>'
    body += f'<div class="hint" id="i_h"><span class="hw">die Woh<b style="color:{ART["die"][0]}">nung</b></span><span class="arrow" id="i_ar">⬆</span><div class="ht">Hör aufs Ende!</div></div>'
    body += '<div class="iuk" id="i_uk">Дивись на закінчення слова!</div>'
    body += '</div>'
    times = {}
    for x, t in tt: times.setdefault(norm(x), t)
    for w in ("der", "die", "das"):
        t = times.get(w, a + .5)
        J(f'tl.fromTo("#i_{w}",{{y:-260,opacity:0,rotation:-12}},{{y:0,opacity:1,rotation:0,duration:.5,ease:"bounce.out"}},{max(0, t - .25):.3f});')
    J(f'tl.fromTo("#i_q",{{scale:0}},{{scale:1,duration:.4,ease:"back.out(2.5)"}},{times.get("wer", a + 2):.3f});')
    J(f'tl.fromTo("#i_q .emo",{{rotation:-15}},{{rotation:15,duration:.3,yoyo:true,repeat:5}},{times.get("wer", a + 2):.3f});')
    th = times.get("hör", a + 4)
    J(f'tl.fromTo("#i_h",{{opacity:0,y:80}},{{opacity:1,y:0,duration:.45,ease:"back.out(2)"}},{th - .1:.3f});')
    J(f'tl.fromTo("#i_h b",{{scale:1}},{{scale:1.35,duration:.25,yoyo:true,repeat:5,ease:"power1.inOut",transformOrigin:"50% 80%"}},{times.get("ende", th + 1):.3f});')
    J(f'tl.fromTo("#i_ar",{{y:0}},{{y:-30,duration:.25,yoyo:true,repeat:7}},{times.get("ende", th + 1):.3f});')
    J(f'tl.fromTo("#i_uk",{{opacity:0}},{{opacity:1,duration:.3}},{th + .3:.3f});')
    return a, b, body

# ---------- блок окончания ----------
def block_scene(i):
    bl = E["blocks"][i]; ks = blk_lines[i]
    a = L[ks[0]]["start"] - .6
    b = L[blk_lines[i + 1][0]]["start"] - .6 if i + 1 < NB else L[outro[0]]["start"] - .6
    sid = f"b{i}"
    q_toks = tok_times(ks[0]); a_toks = tok_times(ks[1])
    # вопрос: слова появляются по мере пения (без самого окончания — оно в пилюле)
    qwords = [x for x, _ in q_toks]
    sung_end = {norm(p) for p in re.split(r"[„“ ]+", bl["sing"]) if norm(p)}
    qh = []
    for j, (x, t) in enumerate(q_toks):
        if bl["sing"] != "Verb" and norm(x) in sung_end or (norm(x) == "oder" and len(sung_end) > 1) or (bl["sing"] == "ie" and norm(x) in ("wie", "energie")):
            continue
        qh.append(f'<span class="qw" id="{sid}q{j}">{html.escape(x.strip("„“?,"))}</span>')
        J(f'tl.fromTo("#{sid}q{j}",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.2}},{t - .05:.3f});')
    pill_t = next((t for x, t in q_toks if norm(x) in sung_end), q_toks[-1][1])
    if qh: qh[-1] = qh[-1].replace("</span>", "?</span>")
    body = f'<div class="q" style="left:{G["hdr_x"]}px;width:{G["hdr_w"]}px;top:{G["q_y"]}px;font-size:{G["q_fs"]}px">{" ".join(qh)}</div>'
    body += f'<div class="pillw" style="left:{G["hdr_x"]}px;width:{G["hdr_w"]}px;top:{G["pill_y"]}px"><span class="pill" id="{sid}p" style="font-size:{min(G["pill_fs"], G["hdr_w"] * .92 / (len(bl["show"]) * .74 + .9)):.0f}px">{html.escape(bl["show"])}</span></div>'
    uk_q = {"Endet ein Wort auf": "Слово закінчується на", "Beginnt ein Wort mit": "Слово починається з", "Wird ein Verb zum Nomen": "Дієслово стає іменником"}[bl["q"]]
    uk_a = {"Immer": "завжди", "Fast": "майже завжди", "Meistens": "здебільшого"}[bl["a"].split()[0]]
    body += f'<div class="quk" id="{sid}u" style="left:{G["hdr_x"]}px;width:{G["hdr_w"]}px;top:{G["uk_y"] + (40 if MODE == "v" else 30)}px">{uk_q}{" " + html.escape(bl["show"]) if bl["q"] != "Wird ein Verb zum Nomen" else ""}? → {uk_a} <b>{E["art"]}</b></div>'
    body += f'<div class="stampw" style="left:{G["hdr_x"]}px;width:{G["hdr_w"]}px;top:{G["stamp_y"] + (40 if MODE == "v" else 30)}px"><span class="stamp" id="{sid}s" style="font-size:{min(G["stamp_fs"], G["hdr_w"] * .82 / (len(bl["a"]) * .8 + .8)):.0f}px">{html.escape(bl["a"].upper())}</span></div>'
    # искры вокруг печати
    for k in range(12):
        ang = k * math.pi / 6
        body += f'<span class="spark" id="{sid}k{k}" style="left:{G["hdr_x"] + G["hdr_w"] / 2:.0f}px;top:{G["stamp_y"] + 100:.0f}px"></span>'
    J(f'tl.fromTo("#{sid}p",{{scale:0,rotation:-20}},{{scale:1,rotation:0,duration:.5,ease:"back.out(2.6)"}},{pill_t - .1:.3f});')
    J(f'tl.fromTo("#{sid}u",{{opacity:0}},{{opacity:1,duration:.3}},{pill_t + .2:.3f});')
    st = a_toks[0][1]
    J(f'tl.fromTo("#{sid}s",{{scale:3,opacity:0,rotation:-25}},{{scale:1,opacity:1,rotation:-6,duration:.28,ease:"power4.in"}},{st - .28:.3f});')
    J(f'tl.fromTo(".stage",{{x:0}},{{x:14,duration:.05,yoyo:true,repeat:5}},{st:.3f});')
    for k in range(12):
        ang = k * math.pi / 6
        J(f'tl.fromTo("#{sid}k{k}",{{x:0,y:0,opacity:1,scale:1}},{{x:{260 * math.cos(ang):.0f},y:{140 * math.sin(ang):.0f},opacity:0,scale:.2,duration:.7,ease:"power2.out",immediateRender:false}},{st:.3f});')
    # слова
    wt = tok_times(ks[2]) + tok_times(ks[3])
    nouns = [(x, t) for x, t in wt if norm(x) not in ("der", "die", "das")]
    arts = [t for x, t in wt if norm(x) in ("der", "die", "das")]
    rows = []
    for j, (w, ic, uk) in enumerate(bl["words"]):
        t_art = arts[j] if j < len(arts) else nouns[j][1] - .3
        t_n = nouns[j][1] if j < len(nouns) else t_art + .3
        stem, end = split_word(w, bl)
        col, row = (j % G["cols"], j // G["cols"]) if G["cols"] == 1 else (j // 3, j % 3)
        x = G["list_x"] + col * (G["col_w"] + 40); y = G["list_y"] + row * G["row_h"]
        rid = f"{sid}r{j}"
        stem_html = f'<span class="st">{html.escape(stem)}</span><span class="en" id="{rid}e">{html.escape(end)}</span>' if MODE == "v" or True else ""
        if end and not stem:  # окончание в начале слова (Ge-)
            stem_html = f'<span class="en" id="{rid}e">{html.escape(end)}</span><span class="st">{html.escape(w[len(end):])}</span>'
        rows.append(f'''<div class="row" id="{rid}" style="left:{x}px;top:{y}px;width:{G["col_w"]}px;height:{G["row_h"] - 16}px">
  <div class="icb" id="{rid}i" style="width:{G["icon"]}px;height:{G["icon"]}px">{emoji(ic, int(G["icon"] * .66))}</div>
  <div class="txt"><div class="wt" style="font-size:{G["word_fs"]}px"><span class="ar" id="{rid}a">{E["art"]}</span> {stem_html}</div><div class="wuk" style="font-size:{G["uk_fs"]}px">{html.escape(uk)}</div></div>
</div>''')
        J(f'tl.fromTo("#{rid}",{{opacity:0,x:{160 if MODE == "v" else 120}}},{{opacity:1,x:0,duration:.3,ease:"power3.out"}},{t_art - .15:.3f});')
        J(f'tl.fromTo("#{rid}i",{{scale:0,rotation:-40}},{{scale:1,rotation:0,duration:.45,ease:"back.out(3)"}},{t_art - .05:.3f});')
        J(f'tl.fromTo("#{rid}a",{{scale:1.6}},{{scale:1,duration:.3,ease:"back.out(2)"}},{t_art:.3f});')
        J(f'tl.fromTo("#{rid}e",{{y:-140,opacity:0,scale:2.2}},{{y:0,opacity:1,scale:1,duration:.38,ease:"back.out(1.7)"}},{t_n + .05:.3f});')
        J(f'tl.fromTo("#{rid}",{{backgroundColor:"rgba(255,255,255,0)"}},{{backgroundColor:"rgba(255,255,255,0.95)",duration:.15}},{t_art - .1:.3f});')
        nxt = arts[j + 1] if j + 1 < len(arts) else t_n + 1.2
        J(f'tl.to("#{rid}",{{backgroundColor:"rgba(255,255,255,0.55)",duration:.2}},{nxt - .1:.3f});')
    body += "".join(rows)
    # итоговая строка блока: окончания вспыхивают по очереди, печать снова
    rt = tok_times(ks[4])
    r0 = rt[0][1]
    J(f'tl.fromTo("#{sid} .en",{{scale:1}},{{scale:1.3,duration:.16,yoyo:true,repeat:1,stagger:.12,ease:"power1.out"}},{r0:.3f});')
    J(f'tl.fromTo("#{sid} .icb",{{y:0}},{{y:-22,duration:.16,yoyo:true,repeat:1,stagger:.12}},{r0:.3f});')
    J(f'tl.fromTo("#{sid}p",{{rotation:0}},{{rotation:6,duration:.12,yoyo:true,repeat:3}},{r0:.3f});')
    J(f'tl.fromTo("#{sid}s",{{scale:1}},{{scale:1.18,duration:.15,yoyo:true,repeat:1}},{rt[-1][1] - .2:.3f});')
    # покачивание иконок по битам внутри блока
    for bt in BEATS:
        if a + 1 < bt < b - .3:
            J(f'tl.fromTo("#{sid} .icb .ic",{{scale:1}},{{scale:1.12,duration:.1,yoyo:true,repeat:1,ease:"power1.out"}},{bt:.3f});')
    return a, b, body

def split_word(w, bl):
    """делит слово на основу и выделяемое окончание"""
    show = bl["show"]
    if show.startswith("Ge-"):
        return "", "Ge"
    if show.startswith("Verb"):
        return w[:-2], w[-2:]
    for e in sorted((p.strip(" -/") for p in show.split("/")), key=len, reverse=True):
        if e and w.lower().endswith(e):
            return w[:-len(e)], w[-len(e):]
    return w, ""

# ---------- финал: сетка окончаний + исключения ----------
def outro_scene():
    a = L[outro[0]]["start"] - .6; b = D
    tiles = "".join(f'<div class="tile" id="o_t{i}"><span style="font-size:{70 if len(bl["show"]) <= 7 else 48}px;white-space:nowrap">{html.escape(bl["show"])}</span><small>{" · ".join(html.escape(w[0]) for w in bl["words"][:3])}</small></div>' for i, bl in enumerate(E["blocks"]))
    body = f'<div class="ohd" id="o_h"><span class="art" style="background:{C}">{E["art"]}</span></div>'
    gc = (2 if MODE == "v" else (NB if NB <= 4 else 3))
    body += f'<div class="ogrid" id="o_g" style="grid-template-columns:repeat({gc},1fr)">{tiles}</div>'
    body += '<div class="ofin" id="o_f">jetzt weißt du das! <span class="emo">🎉</span></div>'
    if E["exceptions"]:
        body += '<div class="oexc" id="o_x"><b>Ausnahmen · винятки:</b> ' + " ".join(f'<span class="xc">{html.escape(x)}</span>' for x in E["exceptions"]) + '</div>'
    body += '<div class="octa" id="o_s"><span class="emo">💾</span> Speichern &amp; wiederholen! · Збережи й повторюй!</div>'
    J(f'tl.fromTo("#o_s",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.4}},{a + 2:.3f});')
    J(f'tl.fromTo("#o_h",{{scale:0}},{{scale:1,duration:.5,ease:"back.out(2.4)"}},{a + .2:.3f});')
    J(f'tl.fromTo("#o_g .tile",{{opacity:0,scale:.5}},{{opacity:.35,scale:1,duration:.3,stagger:.06}},{a + .1:.3f});')
    rt = tok_times(outro[0])
    # каждое пропетое окончание зажигает свою плитку
    ti = 0
    for x, t in rt:
        if ti < len(E["blocks"]) and norm(x) in {norm(p) for p in re.split(r"[ /\-→]+", E["blocks"][ti]["show"])} | {norm(E["blocks"][ti]["sing"].split("“")[0])}:
            J(f'tl.to("#o_t{ti}",{{opacity:1,backgroundColor:"{C}",color:"#fff",duration:.12}},{t:.3f});')
            J(f'tl.fromTo("#o_t{ti}",{{scale:1}},{{scale:1.15,duration:.14,yoyo:true,repeat:1}},{t:.3f});')
            ti += 1
    t_end = rt[-1][1]
    J(f'tl.to("#o_g .tile",{{opacity:1,backgroundColor:"{C}",color:"#fff",duration:.2}},{t_end:.3f});')
    ft = tok_times(outro[1])
    J(f'tl.fromTo("#o_f",{{scale:0,rotation:-8}},{{scale:1,rotation:0,duration:.5,ease:"back.out(2.4)"}},{ft[0][1]:.3f});')
    for k in range(24):
        cx = W * (.1 + .8 * ((k * 37) % 24) / 24)
        body += f'<span class="conf" id="o_c{k}" style="left:{cx:.0f}px;background:{["#FFC93C", C, "#5BC0EB", "#9BC53D", "#FF7AA2"][k % 5]}"></span>'
        J(f'tl.fromTo("#o_c{k}",{{y:-60,rotation:0,opacity:1}},{{y:{H + 80},rotation:{(k % 7) * 90 + 180},duration:{2.6 + (k % 5) * .35:.2f},ease:"power1.in",immediateRender:false}},{ft[0][1] + (k % 6) * .12:.3f});')
    if E["exceptions"]:
        J(f'tl.fromTo("#o_x",{{opacity:0,y:60}},{{opacity:1,y:0,duration:.5}},{ft[-1][1] + .4:.3f});')
    return a, b, body

parts = [intro_scene()] + [block_scene(i) for i in range(NB)] + [outro_scene()]
for n, (a, b, body) in enumerate(parts):
    sid = f"sc{n}"
    scenes.append(f'<div class="scene" id="{sid}">{body}</div>')
    J(f'tl.set("#{sid}",{{opacity:1}},{a:.3f});')
    if n:  # переход: сцена въезжает снизу, фон вспыхивает цветом артикля
        J(f'tl.fromTo("#{sid}",{{y:{H * .35:.0f},rotationX:-25}},{{y:0,rotationX:0,duration:.45,ease:"power3.out",immediateRender:false}},{a:.3f});')
        J(f'tl.fromTo("#flash",{{opacity:.45}},{{opacity:0,duration:.5,immediateRender:false}},{a:.3f});')
    if n + 1 < len(parts):
        J(f'tl.to("#{sid}",{{y:{-H * .3:.0f},opacity:0,duration:.35,ease:"power2.in"}},{b - .35:.3f});')
    # индикатор блока
    if 1 <= n <= NB:
        J(f'tl.to("#dot{n - 1}",{{backgroundColor:"{C}",scale:1.3,duration:.2}},{a:.3f}); tl.to("#dot{n - 1}",{{scale:1,duration:.2}},{b:.3f});')

# ---------- фон: плавающие окончания + пульс по битам ----------
bgh = []
ends = [bl["show"] for bl in E["blocks"]]
for k in range(10):
    x = (k * 263) % (W - 300); y = (k * 389) % (H - 200); fs = 90 + (k * 23) % 90
    bgh.append(f'<div class="fl" id="fl{k}" style="left:{x}px;top:{y}px;font-size:{fs}px">{html.escape(ends[k % len(ends)])}</div>')
    J(f'tl.fromTo("#fl{k}",{{x:0,y:0,rotation:{-8 + k % 5 * 4}}},{{x:{(-1) ** k * 140},y:{-120 - (k % 3) * 60},rotation:{8 - k % 5 * 4},duration:D,ease:"sine.inOut"}},0);')
for bt in BEATS:
    J(f'tl.fromTo("#pulse",{{scale:.85,opacity:.5}},{{scale:1.25,opacity:0,duration:.55,ease:"power2.out",immediateRender:false}},{bt:.3f});')
dots = "".join(f'<span class="dot" id="dot{i}"></span>' for i in range(NB))

CSS_MODE = ("""
  .intro .ddd { top: 330px; } .intro .iq { top: 640px; } .intro .hint { top: 900px; } .intro .iuk { top: 1330px; }
  .ohd { top: 150px; } .ogrid { left: 60px; right: 60px; top: 430px; } .ofin { top: 1260px; } .oexc { left: 60px; right: 60px; top: 1450px; }
  #pulse { left: 140px; top: 1660px; width: 800px; height: 800px; }
""" if MODE == "v" else """
  .intro .ddd { top: 150px; } .intro .iq { top: 420px; } .intro .hint { top: 600px; } .intro .iuk { top: 930px; }
  .ohd { top: 50px; } .ohd .art { font-size: 120px !important; } .ogrid { left: 120px; right: 120px; top: 250px; } .ofin { top: 745px; font-size: 80px !important; } .oexc { left: 160px; right: 160px; top: 860px; line-height: 1.6 !important; }
  #pulse { left: -150px; top: 600px; width: 900px; height: 900px; }
""")

TPL = f'''<!doctype html>
<html lang="de" data-resolution="{"portrait" if MODE == "v" else "landscape"}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width={W}, height={H}" />
<script src="gsap.min.js"></script>
<style>
  @font-face {{ font-family: "Nunito"; font-weight: 900; src: url("nunito-latin-900-normal.woff2") format("woff2"); unicode-range: U+0000-024F, U+2000-206F, U+2190-21FF; }}
  @font-face {{ font-family: "Nunito"; font-weight: 900; src: url("nunito-cyrillic-900-normal.woff2") format("woff2"); unicode-range: U+0400-04FF; }}
  @font-face {{ font-family: "Nunito"; font-weight: 800; src: url("nunito-latin-800-normal.woff2") format("woff2"); unicode-range: U+0000-024F, U+2000-206F, U+2190-21FF; }}
  @font-face {{ font-family: "Nunito"; font-weight: 800; src: url("nunito-cyrillic-800-normal.woff2") format("woff2"); unicode-range: U+0400-04FF; }}
  @font-face {{ font-family: "Unbounded"; font-weight: 800; src: url("unbounded-latin-800-normal.woff2") format("woff2"); unicode-range: U+0000-024F, U+2000-206F; }}
  @font-face {{ font-family: "Unbounded"; font-weight: 800; src: url("unbounded-cyrillic-800-normal.woff2") format("woff2"); unicode-range: U+0400-04FF; }}
  @font-face {{ font-family: "Noto Color Emoji"; src: local("Noto Color Emoji"), local("NotoColorEmoji"); }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: {BG}; }}
  #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; font-family: Nunito, "Noto Color Emoji", sans-serif; color: {INK};
    background: radial-gradient(circle at 20% 10%, #fff 0%, {BG} 45%, {BG2} 100%); }}
  .layer {{ position: absolute; inset: 0; }}
  .fl {{ position: absolute; font: 800 100px Unbounded; color: {C}; opacity: .07; white-space: nowrap; }}
  #pulse {{ position: absolute; border-radius: 50%; border: 10px solid {C}; opacity: 0; }}
  #flash {{ position: absolute; inset: 0; background: {C}; opacity: 0; }}
  .stage {{ position: absolute; inset: 0; perspective: 1600px; }}
  .scene {{ position: absolute; inset: 0; opacity: 0; transform-origin: 50% 0; }}
  .em, .emo, .ic {{ font-family: "Noto Color Emoji"; font-weight: 400; }}
  #top {{ position: absolute; left: 50px; right: 50px; top: 50px; display: flex; justify-content: space-between; align-items: center; }}
  .chip {{ padding: 12px 28px; border-radius: 40px; background: #fff; font: 900 38px Nunito; box-shadow: 0 6px 18px rgba(35,42,61,.08); }}
  .chip .d1 {{ color: {ART["der"][0]}; }} .chip .d2 {{ color: {ART["die"][0]}; }} .chip .d3 {{ color: {ART["das"][0]}; }}
  #dots {{ display: flex; gap: 14px; }} .dot {{ width: 22px; height: 22px; border-radius: 50%; background: rgba(35,42,61,.15); }}
  .q, .pillw, .stampw, .quk {{ position: absolute; text-align: center; }}
  .q {{ font-weight: 900; color: {INK}; }} .qw {{ display: inline-block; margin: 0 .12em; }}
  .pill {{ display: inline-block; white-space: nowrap; padding: .02em .45em .1em; border-radius: .5em; background: {C}; color: #fff; font: 800 1em Unbounded; box-shadow: 0 .08em 0 rgba(0,0,0,.15), 0 .15em .4em rgba(35,42,61,.18); }}
  .quk {{ font: 800 {40 if MODE == 'v' else 30}px Nunito; white-space: nowrap; color: {UKC}; }} .quk b {{ color: {C}; }}
  .stamp {{ display: inline-block; white-space: nowrap; padding: .08em .4em; border: .09em solid {C}; border-radius: .25em; color: {C}; font: 800 1em Unbounded; background: rgba(255,255,255,.85); letter-spacing: .02em; }}
  .spark {{ position: absolute; width: 26px; height: 26px; border-radius: 50%; background: {C}; opacity: 0; }}
  .row {{ position: absolute; display: flex; align-items: center; gap: 28px; padding: 0 22px; border-radius: 34px; opacity: 0; }}
  .icb {{ flex: none; display: flex; align-items: center; justify-content: center; border-radius: 30px; background: #fff; box-shadow: 0 6px 0 rgba(35,42,61,.06), 0 10px 22px rgba(35,42,61,.1); }}
  .txt {{ min-width: 0; flex: 1; }}
  .wt {{ font-weight: 900; white-space: nowrap; line-height: 1.1; }}
  .wt .ar {{ display: inline-block; color: {C}; }} .wt .en {{ display: inline-block; color: {C}; text-decoration: underline; text-decoration-thickness: .08em; text-underline-offset: .12em; }}
  .wuk {{ margin-top: 4px; font-weight: 800; color: {UKC}; }}
  .intro .ddd, .intro .iq, .intro .hint, .intro .iuk, .ohd, .ofin {{ position: absolute; left: 0; right: 0; text-align: center; }}
  .intro .ddd {{ white-space: nowrap; }} .intro .big {{ display: inline-block; margin: 0 .12em; font: 800 {124 if MODE == "v" else 170}px Unbounded; }}
  .intro .iq {{ font: 900 100px Nunito; }}
  .intro .hw {{ display: inline-block; padding: 10px 40px; border-radius: 40px; background: #fff; font: 900 120px Nunito; box-shadow: 0 10px 30px rgba(35,42,61,.12); }}
  .intro .hw b {{ display: inline-block; }}
  .intro .arrow {{ display: block; font: 900 90px Nunito; color: {ART["die"][0]}; margin-left: 330px; }}
  .intro .ht {{ font: 800 76px Unbounded; margin-top: 10px; }}
  .intro .iuk {{ font: 800 50px Nunito; color: {UKC}; }}
  .ohd .art {{ display: inline-block; padding: 0 .5em .08em; border-radius: .4em; color: #fff; font: 800 170px Unbounded; }}
  .ogrid {{ position: absolute; display: grid; gap: 26px; }}
  .tile {{ display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; padding: 26px 10px; border-radius: 30px; background: #fff; color: {C}; box-shadow: 0 8px 22px rgba(35,42,61,.1); }}
  .tile span {{ font: 800 70px Unbounded; }} .tile small {{ font: 900 30px Nunito; opacity: .9; text-align: center; }}
  .ofin {{ font: 900 96px Nunito; }}
  .oexc {{ position: absolute; text-align: center; font: 800 38px Nunito; color: {MUTED}; line-height: 1.9; }}
  .oexc b {{ color: {INK}; }} .xc {{ display: inline-block; margin: 0 6px; padding: 0 18px; border-radius: 24px; background: #fff; color: {INK}; }}
  .octa {{ position: absolute; left: 0; right: 0; text-align: center; font: 900 {36 if MODE == 'v' else 36}px Nunito; white-space: nowrap; color: {INK}; top: {1700 if MODE == 'v' else 985}px; }}
  .conf {{ position: absolute; top: 0; width: 22px; height: 34px; border-radius: 6px; opacity: 0; }}
  #bar {{ position: absolute; left: 50px; right: 50px; bottom: 34px; height: 14px; border-radius: 7px; background: rgba(255,255,255,.8); overflow: hidden; }}
  #barf {{ width: 100%; height: 100%; background: {C}; transform-origin: 0 50%; }}
{CSS_MODE}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{D}" data-width="{W}" data-height="{H}">
  <div id="bg" class="layer clip" data-start="0" data-duration="{D}" data-track-index="0">
    {"".join(bgh)}
    <div id="pulse"></div>
  </div>
  <div id="ui" class="layer clip" data-start="0" data-duration="{D}" data-track-index="1">
    <div class="stage">
{chr(10).join(scenes)}
    </div>
    <div id="top"><div class="chip"><span class="em">🎵</span> <span class="d1">der</span> · <span class="d2">die</span> · <span class="d3">das</span> · Folge {E["no"]}</div><div id="dots">{dots}</div></div>
    <div id="bar"><div id="barf"></div></div>
    <div id="flash"></div>
  </div>
</div>
<script>
  // подгонка длинных слов под ширину строки
  document.querySelectorAll(".wt").forEach(el => {{
    const max = el.parentElement.clientWidth; let fs = parseFloat(getComputedStyle(el).fontSize);
    while (el.scrollWidth > max && fs > 30) {{ fs -= 2; el.style.fontSize = fs + "px"; }}
  }});
  const tl = gsap.timeline({{ paused: true }});
  const D = {D};
  tl.fromTo("#barf", {{ scaleX: 0 }}, {{ scaleX: 1, duration: D, ease: "none" }}, 0);
  {chr(10).join("  " + s for s in js)}
  tl.set({{}}, {{}}, D);
  window.__timelines["main"] = tl;
</script>
</body>
</html>
'''

os.makedirs(OUT, exist_ok=True)
for src, dst in [("gsap-3.14.2/dist/gsap.min.js", "gsap.min.js")] + [
        (f"fontsource-{f.split('-')[0]}-{'5.2.7' if f.startswith('nunito') else '5.2.8'}/files/{f}", f) for f in
        ["nunito-latin-900-normal.woff2", "nunito-cyrillic-900-normal.woff2", "nunito-latin-800-normal.woff2", "nunito-cyrillic-800-normal.woff2",
         "unbounded-latin-800-normal.woff2", "unbounded-cyrillic-800-normal.woff2"]]:
    if not os.path.exists(f"{OUT}/{dst}"): shutil.copy(f"{ASSETS}/{src}", f"{OUT}/{dst}")
open(f"{OUT}/index.html", "w").write(TPL)
shutil.copy(os.path.join(ROOT, "..", "..", "aspekte-b1plus", "engine", "hyperframes.json"), f"{OUT}/hyperframes.json")
json.dump({"id": f"{EP_ID}_{MODE}", "name": f"{EP_ID}_{MODE}", "createdAt": "2026-10-24T08:00:00.000Z"}, open(f"{OUT}/meta.json", "w"))
print("ok", EP_ID, MODE, "D", D, "scenes", len(parts), "tweens", len(js))
