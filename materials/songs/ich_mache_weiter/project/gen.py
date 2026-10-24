# Генерує proj/index.html: караоке-кліп на пісню «Ich mache weiter» (світла тема, 1080x1920)
import json, html, re, sys
sys.path.insert(0, "/home/user/song")
from uk import UK, SECTIONS_UK

D = 300.86
L = json.load(open("/home/user/song/lines.json"))
assert len(L) == len(UK)
PREF = sorted("hinaus herein zurück weiter vorbei fern nach weg mit los auf aus ein zu an ab um vor rein raus".split(), key=len, reverse=True)
SEP = set(PREF)
DRILL = {"Intro", "Final Chorus", "Outro"} | {s for s in SECTIONS_UK if s.startswith("Verse")}
SEC_DE = {"Intro": "Am Morgen", "Chorus": "Refrain", "Final Chorus": "Finale", "Outro": "Outro"}
def sec_de(s): return SEC_DE.get(s, s.split("— ")[-1])
def norm(w): return re.sub(r"[^a-zäöüß]", "", w.lower())

def split_pref(w, part=False):
    # Віддільний префікс (помаранчевий) + «ge» (зелений) у словах типу aufgewacht
    low = w.lower()
    for p in PREF:
        if low.startswith(p) and len(low) - len(p) >= 3:
            head, rest = w[:len(p)], w[len(p):]
            ge = ""
            if part and rest.lower().startswith("ge") and not rest.lower().startswith("gen"):
                ge, rest = rest[:2], rest[2:]
            out = f'<em class="p">{head}</em>'
            if ge: out += f'<em class="g">{ge}</em>'
            return out + rest
    return w

def word_html(tok, prev, nxt):
    m = re.match(r"^([^\wäöüÄÖÜß]*)([\wäöüÄÖÜß']+)([^\wäöüÄÖÜß]*)$", tok)
    if not m: return html.escape(tok)
    a, w, z = m.groups(); low = w.lower(); pl = norm(prev or ""); nl = norm(nxt or "")
    if low == "bin": core = f'<em class="s">{w}</em>'
    elif low == "habe": core = f'<em class="h">{w}</em>'
    elif low in ("mich", "sich"): core = f'<em class="r">{w}</em>'
    elif pl in ("bin", "habe", "mich"): core = split_pref(w, part=True)
    elif low in SEP and pl not in ("ich", "du", "wir", "") and nl != "haus": core = f'<em class="p">{w}</em>'
    elif w[0].isupper() and low.endswith("en") and low not in ("ich",): core = split_pref(w)
    else: core = w
    return a + core + z

def kind(k):
    l = L[k]; parts = l["text"].split(" — ")
    if l["sec"] in DRILL and len(parts) >= 2: return "drill"
    return "line"

def labels(k):
    l = L[k]; n = len(l["text"].split(" — "))
    if n == 3: return ["Infinitiv", "Präsens", "Perfekt"]
    if l["sec"] == "Outro": return ["Präsens", "Perfekt"]
    return ["Infinitiv", "Präsens"]

# групи для списку внизу: секція, а фінал розбитий на дві частини
groups, cur = [], []
for k, l in enumerate(L):
    if cur and (l["sec"] != L[cur[-1]]["sec"] or k == 69):
        groups.append(cur); cur = []
    cur.append(k)
groups.append(cur)
gid = {k: g for g, ks in enumerate(groups) for k in ks}

# моменти показу/приховування карток
show, hide = [], []
for k, l in enumerate(L):
    nxt = L[k+1]["start"] if k + 1 < len(L) else D
    show.append(max(0, l["start"] - .3) if k else 0)
    hide.append(min(nxt - .3, l["end"] + 1.4) if nxt - l["end"] > 3 else nxt - .3)

cards, js, rows, pills = [], [], [], []
for k, l in enumerate(L):
    toks = l["text"].split(); ti = 0; times = l["t"]
    rws = [[]]
    for i, t in enumerate(toks):
        if t == "—": rws.append([]); continue
        prev = toks[i-1] if i and toks[i-1] != "—" else ""
        nxt = toks[i+1] if i + 1 < len(toks) else ""
        rws[-1].append((word_html(t, prev, nxt), times[ti])); ti += 1
    assert ti == len(times), k
    ukp = UK[k].split(" — ")
    if kind(k) == "drill":
        lab = labels(k); assert len(lab) == len(rws), k
        inner = ""
        for r, (lb, ws) in enumerate(zip(lab, rws)):
            aux = ""
            if lb == "Perfekt":
                aux = '<span class="aux s">sein</span>' if any(norm(re.sub("<.*?>", "", h)) == "bin" for h, _ in ws) else '<span class="aux h">haben</span>'
            wsh = " ".join(f'<span class="w" id="w{k}_{r}_{j}">{h}</span>' for j, (h, _) in enumerate(ws))
            u = f'<div class="ru">{html.escape(ukp[r])}</div>' if len(ukp) == len(rws) else ""
            inner += f'<div class="drow" id="d{k}_{r}"><div class="lab">{lb}{aux}</div><div class="de fit">{wsh}</div>{u}</div>'
        if len(ukp) != len(rws): inner += f'<div class="uk">{html.escape(UK[k])}</div>'
        cards.append(f'<div class="card drill" id="c{k}">{inner}</div>')
    else:
        ws = [x for r in rws for x in r]
        wsh = " ".join(f'<span class="w" id="w{k}_0_{j}">{h}</span>' for j, (h, _) in enumerate(ws))
        cards.append(f'<div class="card line" id="c{k}"><div class="big fit">{wsh}</div><div class="uk">{html.escape(UK[k])}</div></div>')
        rws = [ws]
    # анімація картки
    js.append(f'tl.fromTo("#c{k}",{{opacity:0,y:50,scale:.96}},{{opacity:1,y:0,scale:1,duration:.3,ease:"back.out(1.6)"}},{show[k]:.3f});')
    js.append(f'tl.to("#c{k}",{{opacity:0,y:-30,duration:.22,ease:"power2.in"}},{hide[k]-.22:.3f});')
    if kind(k) == "drill":
        for r, ws in enumerate(rws):
            js.append(f'tl.fromTo("#d{k}_{r}",{{x:-40,opacity:0}},{{x:0,opacity:1,duration:.25,ease:"power2.out"}},{max(show[k], ws[0][1][0]-.35) if r else show[k]:.3f});')
    for r, ws in enumerate(rws):
        for j, (_, t) in enumerate(ws):
            js.append(f'tl.to("#w{k}_{r}_{j}",{{opacity:1,scale:1,color:"#1F2A44",duration:.14,ease:"power1.out"}},{t[0]:.3f});')
            js.append(f'tl.fromTo("#w{k}_{r}_{j}",{{y:0}},{{y:-10,duration:.12,yoyo:true,repeat:1,ease:"sine.out"}},{t[0]:.3f});')
    # рядок у списку внизу
    if kind(k) == "drill":
        de = re.sub("<.*?>", "", " ".join(h for h, _ in rws[0])).lower() if labels(k)[0] == "Infinitiv" else re.sub("<.*?>", "", " ".join(h for h, _ in rws[0]))
        last = rws[-1]
        if labels(k)[-1] == "Perfekt":
            perf = " ".join(h for h, _ in last if norm(re.sub("<.*?>", "", h)) != "ich")
            de_h = f'{split_pref(de.split()[-1]) if de.split()[0] != "sich" else "sich " + split_pref(de.split()[-1])} <span class="ar">→</span> {perf}' if labels(k)[0] == "Infinitiv" else f'{" ".join(h for h, _ in rws[0])} <span class="ar">→</span> {perf}'
        else:
            de_h = f'{split_pref(de)} <span class="ar">→</span> {" ".join(h for h, _ in last)}'
        u = ukp[0]
    else:
        de_h = " ".join(h for h, _ in rws[0]); u = ""
    rows.append((gid[k], f'<div class="lrow" id="r{k}"><span class="lde">{de_h}</span><span class="lu">{html.escape(u)}</span></div>'))
    js.append(f'tl.fromTo("#r{k}",{{opacity:0,x:-30}},{{opacity:1,x:0,duration:.3,ease:"power2.out"}},{min(l["end"]+.1, hide[k]):.3f});')

# групи-списки й плашки секцій
lists = []
for g, ks in enumerate(groups):
    s = L[ks[0]]["sec"]; st = show[ks[0]]; en = hide[ks[-1]] if g + 1 < len(groups) else D
    lists.append(f'<div class="list" id="g{g}"><div class="lhead">In diesem Teil · <span>у цій частині</span></div>' + "".join(r for gg, r in rows if gg == g) + "</div>")
    pills.append(f'<div class="pill" id="p{g}"><b>{html.escape(sec_de(s))}</b> · {html.escape(SECTIONS_UK[s])}</div>')
    js.append(f'tl.fromTo(["#g{g}","#p{g}"],{{opacity:0,y:30}},{{opacity:1,y:0,duration:.35,ease:"power2.out"}},{st:.3f});')
    js.append(f'tl.to(["#g{g}","#p{g}"],{{opacity:0,duration:.25}},{en-.25:.3f});')

# паузи без співу
fills = []
for k in range(len(L)):
    nxt = L[k+1]["start"] if k + 1 < len(L) else D
    if nxt - L[k]["end"] > 3:
        a, b = hide[k], (nxt - .35 if k + 1 < len(L) else D)
        fid = f"f{k}"
        txt = ('🎧', 'Hör zu und sing mit!', 'Слухай і співай разом!') if k + 1 < len(L) else ('🔁', 'Noch einmal hören!', 'Послухай ще раз і повтори!')
        fills.append(f'<div class="fill" id="{fid}"><div class="fe em">{txt[0]}</div><div class="ft">{txt[1]}</div><div class="fu">{txt[2]}</div></div>')
        js.append(f'tl.fromTo("#{fid}",{{opacity:0,scale:.9}},{{opacity:1,scale:1,duration:.35,ease:"back.out(1.7)"}},{a:.3f});')
        js.append(f'tl.fromTo("#{fid} .fe",{{rotation:-12}},{{rotation:12,duration:.5,yoyo:true,repeat:{max(1, int((b-a)/.5)-1)},ease:"sine.inOut"}},{a:.3f});')
        if k + 1 < len(L): js.append(f'tl.to("#{fid}",{{opacity:0,duration:.25}},{b-.25:.3f});')

tpl = open(__import__('os').environ.get('TPL', '/home/user/song/template.html')).read()
out = (tpl.replace("{{D}}", f"{D}").replace("{{CARDS}}", "\n".join(cards + fills)).replace("{{LISTS}}", "\n".join(lists))
       .replace("{{PILLS}}", "\n".join(pills)).replace("{{JS}}", "\n  ".join(js)))
open(__import__('os').environ.get('OUT', '/home/user/song/proj/index.html'), "w").write(out)
json.dump({"id": "ich_mache_weiter", "name": "ich_mache_weiter", "createdAt": "2026-10-23T13:30:00.000Z"}, open(__import__('os').path.dirname(__import__('os').environ.get('OUT', '/home/user/song/proj/index.html')) + '/meta.json', "w"))
print("ok", len(cards), "cards", len(groups), "groups", len(js), "tweens")
