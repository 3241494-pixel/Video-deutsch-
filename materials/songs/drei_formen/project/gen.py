# Генерує proj/index.html: караоке-кліп «Drei Formen, sing sie laut» (сильні дієслова, 3 форми; світла тема, 1080x1920)
import json, html, re, sys
sys.path.insert(0, "/home/user/song2")
from uk import UK, SECTIONS

L = json.load(open("/home/user/song2/lines.json"))
assert len(L) == len(UK)
D = float(sys.argv[1])
SEIN = {"bin", "sind", "ist", "bist", "seid"}
HABEN = {"habe", "haben", "hat", "hab", "hast", "habt"}
def norm(w): return re.sub(r"[^a-zäöüß]", "", w.lower())
def split_tok(tok):
    m = re.match(r"^([^\wäöüÄÖÜß]*)([\wäöüÄÖÜß']+)([^\wäöüÄÖÜß]*)$", tok)
    return m.groups() if m else ("", tok, "")

def part_html(w):
    # Partizip II: «ge» окремим відтінком
    low = w.lower()
    i = low.find("ge") if low.startswith("ge") or "ge" in low[:6] else -1
    if low.startswith("ge"): return f'<em class="pp"><u>{w[:2]}</u>{w[2:]}</em>'
    return f'<em class="pp">{w}</em>'

def forms_of(k):
    # три форми з рядка «Gehen — ging — gegangen,» або «Gehen, ging, gegangen!»
    t = L[k]["text"]
    parts = [norm(p) for p in re.split(r"\s*—\s*|,\s*", t) if norm(p)]
    return parts if len(parts) == 3 else None

def kind(c):
    a = L[2*c]["text"]
    if " — " in a and forms_of(2*c) and len(a.split(" — ")) == 3: return "forms"
    if forms_of(2*c) and a.count(",") >= 2 and len(a.split()) == 3: return "chant"
    return "text"

def word_html(tok, k, forms):
    a, w, z = split_tok(tok); low = w.lower()
    if forms and low == forms[0]: core = f'<em class="inf">{w}</em>'
    elif forms and low == forms[1]: core = f'<em class="prt">{w}</em>'
    elif forms and (low == forms[2] or (len(low) > len(forms[2]) and low.endswith(forms[2]))):
        core = part_html(w) if low == forms[2] else f'{w[:len(w)-len(forms[2])]}{part_html(w[len(w)-len(forms[2]):])}'
    elif forms and low in SEIN: core = f'<em class="s">{w}</em>'
    elif forms and low in HABEN: core = f'<em class="h">{w}</em>'
    else: core = html.escape(w)
    return a + core + z

def spans(k, forms, rowsplit=False):
    # слова рядка k з таймінгами; rowsplit=True ділить по «—» на рядки
    toks = L[k]["text"].split(); ti = 0; rows = [[]]
    for t in toks:
        if t == "—":
            if rowsplit: rows.append([])
            else: rows[-1].append((html.escape("—"), None))
            continue
        rows[-1].append((word_html(t, k, forms), L[k]["t"][ti])); ti += 1
    assert ti == len(L[k]["t"]), k
    return rows

NC = len(L) // 2
sec_of = lambda line: max(i for i, s in enumerate(SECTIONS) if s[0] <= line)
start = [L[2*c]["start"] for c in range(NC)]; end = [L[2*c+1]["end"] for c in range(NC)]
show, hide = [], []
for c in range(NC):
    nxt = start[c+1] if c + 1 < NC else D
    show.append(max(0, start[c] - .35) if c else 0)
    hide.append(min(nxt - .3, end[c] + 1.4) if nxt - end[c] > 3 else nxt - .3)

cards, js, rows = [], [], []
wid = 0
def word_js(sid, t):
    js.append(f'tl.to("#{sid}",{{opacity:1,duration:.14,ease:"power1.out"}},{t[0]:.3f});')
    js.append(f'tl.fromTo("#{sid}",{{y:0}},{{y:-10,duration:.12,yoyo:true,repeat:1,ease:"sine.out"}},{t[0]:.3f});')
def line_html(ws, pre):
    global wid
    out = []
    for h, t in ws:
        if t is None: out.append(f'<span class="w dash">{h}</span>'); continue
        wid += 1; sid = f"w{wid}"; word_js(sid, t); out.append(f'<span class="w" id="{sid}">{h}</span>')
    return " ".join(out)

for c in range(NC):
    a, b = 2*c, 2*c+1; kd = kind(c); f = forms_of(a)
    if kd == "forms":
        ra = spans(a, f, rowsplit=True); ukp = UK[a].split(" — ")
        inner = ""
        for r, (lb, ws) in enumerate(zip(["Infinitiv", "Präteritum", "Partizip II"], ra)):
            inner += f'<div class="drow" id="d{c}_{r}"><div class="lab">{lb}</div><div class="de fit">{line_html(ws, "")}</div><div class="ru">{html.escape(ukp[r])}</div></div>'
            t0 = ws[0][1][0]
            js.append(f'tl.fromTo("#d{c}_{r}",{{x:-40,opacity:0}},{{x:0,opacity:1,duration:.25,ease:"power2.out"}},{show[c] if r == 0 else max(show[c], t0-.3):.3f});')
        wb = spans(b, f)[0]
        aux = next((x for x in L[b]["text"].split() if norm(x) in SEIN | HABEN), "")
        tag = ('<span class="aux s">sein</span>' if norm(aux) in SEIN else '<span class="aux h">haben</span>') if aux else ""
        inner += f'<div class="drow ex" id="d{c}_3"><div class="lab">Beispiel · Perfekt {tag}</div><div class="ex fit">{line_html(wb, "")}</div><div class="ru">{html.escape(UK[b])}</div></div>'
        js.append(f'tl.fromTo("#d{c}_3",{{y:30,opacity:0}},{{y:0,opacity:1,duration:.3,ease:"power2.out"}},{max(show[c], L[b]["start"]-.35):.3f});')
        cards.append(f'<div class="card drill" id="c{c}">{inner}</div>')
        rows.append((sec_of(a), f'<div class="lrow" id="r{c}"><span class="lde"><em class="inf">{f[0]}</em> <span class="ar">·</span> <em class="prt">{f[1]}</em> <span class="ar">·</span> {part_html(f[2])}</span><span class="lu">{html.escape(ukp[0])}</span></div>'))
    else:
        inner = ""
        for k in (a, b):
            ws = spans(k, forms_of(k) if kd == "chant" or forms_of(k) else None)[0]
            inner += f'<div class="big fit">{line_html(ws, "")}</div><div class="uk">{html.escape(UK[k])}</div>'
        cards.append(f'<div class="card line" id="c{c}">{inner}</div>')
        de = re.sub(r"[,!.]$", "", L[a]["text"])
        rows.append((sec_of(a), f'<div class="lrow" id="r{c}"><span class="lde">{" ".join(word_html(t, a, forms_of(a)) for t in de.split())}</span><span class="lu">{html.escape(re.sub(r"[,!.]$", "", UK[a]))}</span></div>'))
    js.append(f'tl.fromTo("#c{c}",{{opacity:0,y:50,scale:.96}},{{opacity:1,y:0,scale:1,duration:.3,ease:"back.out(1.6)"}},{show[c]:.3f});')
    js.append(f'tl.to("#c{c}",{{opacity:0,y:-30,duration:.22,ease:"power2.in"}},{hide[c]-.22:.3f});')
    js.append(f'tl.fromTo("#r{c}",{{opacity:0,x:-30}},{{opacity:1,x:0,duration:.3,ease:"power2.out"}},{min(end[c]+.1, hide[c]):.3f});')

# секції: плашка зверху + список унизу
lists, pills = [], []
for g, (l0, de, uk) in enumerate(SECTIONS):
    cs = [c for c in range(NC) if sec_of(2*c) == g]
    st = show[cs[0]]; en = hide[cs[-1]] if g + 1 < len(SECTIONS) else D
    lists.append(f'<div class="list" id="g{g}"><div class="lhead">In diesem Teil · <span>у цій частині</span></div>' + "".join(r for gg, r in rows if gg == g) + "</div>")
    pills.append(f'<div class="pill" id="p{g}"><b>{html.escape(de)}</b> · {html.escape(uk)}</div>')
    js.append(f'tl.fromTo(["#g{g}","#p{g}"],{{opacity:0,y:30}},{{opacity:1,y:0,duration:.35,ease:"power2.out"}},{st:.3f});')
    js.append(f'tl.to(["#g{g}","#p{g}"],{{opacity:0,duration:.25}},{en-.25:.3f});')

# паузи без співу
fills = []
for c in range(NC):
    nxt = start[c+1] if c + 1 < NC else D
    if nxt - end[c] > 3:
        a_, b_ = hide[c], (nxt - .35 if c + 1 < NC else D)
        txt = ('🎧', 'Hör zu und sing mit!', 'Слухай і співай разом!') if c + 1 < NC else ('🔁', 'Noch einmal hören!', 'Послухай ще раз і повтори!')
        fills.append(f'<div class="fill" id="f{c}"><div class="fe em">{txt[0]}</div><div class="ft">{txt[1]}</div><div class="fu">{txt[2]}</div></div>')
        js.append(f'tl.fromTo("#f{c}",{{opacity:0,scale:.9}},{{opacity:1,scale:1,duration:.35,ease:"back.out(1.7)"}},{a_:.3f});')
        js.append(f'tl.fromTo("#f{c} .fe",{{rotation:-12}},{{rotation:12,duration:.5,yoyo:true,repeat:{max(1, int((b_-a_)/.5)-1)},ease:"sine.inOut"}},{a_:.3f});')
        if c + 1 < NC: js.append(f'tl.to("#f{c}",{{opacity:0,duration:.25}},{b_-.25:.3f});')

tpl = open(__import__('os').environ.get('TPL', '/home/user/song2/template.html')).read()
out = (tpl.replace("{{D}}", f"{D}").replace("{{CARDS}}", "\n".join(cards + fills)).replace("{{LISTS}}", "\n".join(lists))
       .replace("{{PILLS}}", "\n".join(pills)).replace("{{JS}}", "\n  ".join(js)))
open(__import__('os').environ.get('OUT', '/home/user/song2/proj/index.html'), "w").write(out)
json.dump({"id": "drei_formen", "name": "drei_formen", "createdAt": "2026-10-23T16:30:00.000Z"}, open(__import__('os').path.dirname(__import__('os').environ.get('OUT', '/home/user/song2/proj/index.html')) + '/meta.json', "w"))
print("ok", NC, "cards", len(SECTIONS), "sections", len(js), "tweens")
