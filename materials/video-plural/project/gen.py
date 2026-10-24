# Генерация index.html (HyperFrames) для ролика «Plural im Deutschen» из timeline.json и fw.words.json
import json, os, re, html
TL = json.load(open("timeline.json")); D = round(TL["duration"], 2)
S = {s["id"]: s for s in TL["scenes"]}
FW = json.load(open("fw.words.json"))["words"]

def norm(w): return re.sub(r"[^\wäöüß]", "", w.lower())

# Слова: текст из сценария, тайминги из faster-whisper (выравнивание внутри сцены)
def load_words():
    out = []
    for s in TL["scenes"]:
        ws = s["text"].split()
        cand = [w for w in FW if w["start"] >= s["start"] - 0.45 and w["start"] < s["end"] + 0.1]
        if len(cand) == len(ws):
            out += [{"word": w, "start": c["start"], "end": c["end"], "scene": s["id"]} for w, c in zip(ws, cand)]
            continue
        print("warn: word count mismatch in", s["id"], len(ws), len(cand))
        tot = sum(len(w) + 1 for w in ws); t = s["start"]; dur = s["end"] - s["start"]; j = 0
        for w in ws:
            m = next((c for c in cand[j:j + 4] if norm(c["word"]) == norm(w)), None)
            if m: j = cand.index(m) + 1; out.append({"word": w, "start": m["start"], "end": m["end"], "scene": s["id"]}); t = m["end"]; continue
            d = dur * (len(w) + 1) / tot; out.append({"word": w, "start": t, "end": t + d, "scene": s["id"]}); t += d
    return out
W = load_words()

# Последовательный поиск слов внутри сцены: seq("r1", "Tag", "Tage") -> [t1, t2]
def seq(scene, *words):
    ws = [w for w in W if w["scene"] == scene]; i = 0; res = []
    for target in words:
        while i < len(ws) and norm(ws[i]["word"]) != norm(target): i += 1
        if i == len(ws): raise SystemExit(f"нет слова {target} в {scene}")
        res.append(round(ws[i]["start"], 3)); i += 1
    return res

# Подсветка отличий формы множественного числа (умлаут и окончание)
def mark(sg, pl):
    out = ""
    for i, ch in enumerate(pl):
        same = i < len(sg) and sg[i] == ch
        out += html.escape(ch) if same else f'<b>{html.escape(ch)}</b>'
    return out

RULES = [
    ("r1", "-e", "#E8590C", "#FFF0E6", "♂ oft maskulin", "viele",
     [("der", "Tag", "Tage", "☀️"), ("der", "Hund", "Hunde", "🐕"), ("das", "Jahr", "Jahre", "📅")]),
    ("r2", "¨ + -e", "#D6336C", "#FFEEF3", "a o u → ä ö ü", "Aus",
     [("der", "Stuhl", "Stühle", "🪑"), ("die", "Hand", "Hände", "✋"), ("der", "Zug", "Züge", "🚆")]),
    ("r3", "-er", "#7048E8", "#F3F0FF", "⚪ oft neutral · mit Umlaut", "oft",
     [("das", "Kind", "Kinder", "🧒"), ("das", "Buch", "Bücher", "📘"), ("das", "Haus", "Häuser", "🏠")]),
    ("r4", "-n / -en", "#1C7ED6", "#E7F5FF", "♀ fast alle femininen", "Fast",
     [("die", "Lampe", "Lampen", "💡"), ("die", "Frau", "Frauen", "👩"), ("die", "Zeitung", "Zeitungen", "📰")]),
    ("r5", "-s", "#0CA678", "#E6FCF5", "🌍 Wörter aus anderen Sprachen", "meistens",
     [("das", "Auto", "Autos", "🚗"), ("das", "Handy", "Handys", "📱"), ("das", "Hotel", "Hotels", "🏨")]),
    ("r6", "—", "#495057", "#F1F3F5", "-er · -el · -en → oft gleich", "Nur",
     [("der", "Lehrer", "Lehrer", "👨‍🏫"), ("das", "Zimmer", "Zimmer", "🛏️"), ("der", "Apfel", "Äpfel", "🍎")]),
]
QUIZ = [("die", "Katze", "Katzen", "🐈"), ("der", "Baum", "Bäume", "🌳"), ("das", "Kino", "Kinos", "🎬"),
        ("das", "Glas", "Gläser", "🥛"), ("der", "Koffer", "Koffer", "🧳")]

H, J = [], []   # html сцен и js таймлайна
def js(s): J.append(s)
def t3(x): return f"{x:.3f}"

# --- Хук: 1 Tisch → 2 Tische ...
hk = S["hook"]; ht = seq("hook", "Tisch", "Tische", "Buch", "Bücher", "Auto", "Autos", "chaotisch", "Panik", "sechs")
pairs = [("Tisch", "Tische", "🪵"), ("Buch", "Bücher", "📘"), ("Auto", "Autos", "🚗")]
rows = "".join(f'<div class="hrow" id="hr{i}"><span class="em">{e}</span><span class="n">1</span>{sg}<span class="arr">→</span><span class="pl" id="hp{i}"><span class="n">2</span>{mark(sg, pl)}</span></div>' for i, (sg, pl, e) in enumerate(pairs))
H.append(f'''<div class="scene" id="sHook">
  <div id="hTitle">der <span>Plural</span></div>
  <div id="hRows">{rows}</div>
  <div id="hChaos">chaotisch?! 🤯</div>
  <div id="hSix"><span>6</span> Regeln</div>
</div>''')
js('tl.set("#sHook",{opacity:1},0);')
js(f'tl.fromTo("#hTitle",{{opacity:0,y:-60,scale:.8}},{{opacity:1,y:0,scale:1,duration:.5,ease:"back.out(2)"}},0.1);')
for i in range(3):
    js(f'tl.fromTo("#hr{i}",{{opacity:0,x:-120}},{{opacity:1,x:0,duration:.35,ease:"power3.out"}},{t3(ht[2*i]-.1)});')
    js(f'tl.fromTo("#hp{i}",{{opacity:0,scale:.5}},{{opacity:1,scale:1,duration:.35,ease:"back.out(3)"}},{t3(ht[2*i+1]-.05)});')
js(f'tl.fromTo("#hChaos",{{opacity:0,scale:.4,rotation:-12}},{{opacity:1,scale:1,rotation:-6,duration:.4,ease:"back.out(3)"}},{t3(ht[6]-.2)});')
js(f'tl.to("#hRows",{{x:12,duration:.05,repeat:7,yoyo:true}},{t3(ht[6])});')
js(f'tl.to(["#hRows","#hChaos"],{{opacity:.15,duration:.3}},{t3(ht[7]-.1)});')
js(f'tl.fromTo("#hSix",{{opacity:0,scale:.3}},{{opacity:1,scale:1,duration:.5,ease:"back.out(2.5)"}},{t3(ht[8]-.1)});')
js(f'tl.to("#sHook",{{opacity:0,y:-40,duration:.3}},{t3(hk["end"]+.4)});')

# --- Шесть правил
for k, (sid, end, col, soft, note, noteWord, ex) in enumerate(RULES):
    sc = S[sid]; n = k + 1
    words = []
    for a, sg, pl, e in ex: words += [sg, pl]
    tt = seq(sid, *words, noteWord)
    exr = "".join(f'''<div class="ex" id="{sid}e{i}"><span class="em">{e}</span>
      <div class="sg"><i>{a}</i> {sg}</div><span class="arr">→</span>
      <div class="pl" id="{sid}p{i}"><i>die</i> {mark(sg, pl) if sg != pl else pl}</div></div>''' for i, (a, sg, pl, e) in enumerate(ex))
    H.append(f'''<div class="scene rule" id="{sid}" style="--c:{col};--soft:{soft}">
  <div class="rhead"><div class="rnum">{n}</div><div class="rlab">Regel {n}</div><div class="rend" id="{sid}end">{end}</div></div>
  <div class="exs">{exr}</div>
  <div class="rnote" id="{sid}note">{html.escape(note)}</div>
</div>''')
    t0 = sc["start"] - 0.35
    js(f'tl.fromTo("#{sid}",{{opacity:0,y:80}},{{opacity:1,y:0,duration:.45,ease:"power3.out"}},{t3(t0)});')
    js(f'tl.fromTo("#{sid} .rnum",{{scale:0,rotation:-90}},{{scale:1,rotation:0,duration:.5,ease:"back.out(2.5)"}},{t3(t0+.1)});')
    js(f'tl.fromTo("#{sid}end",{{opacity:0,scale:2.2}},{{opacity:1,scale:1,duration:.45,ease:"back.out(2)"}},{t3(sc["start"]+.9)});')
    js(f'tl.to("#d{n}",{{backgroundColor:"{col}",scale:1.25,duration:.3}},{t3(t0)});')
    js(f'tl.to("#d{n}",{{scale:1,duration:.2}},{t3(t0+.35)});')
    for i in range(3):
        js(f'tl.fromTo("#{sid}e{i}",{{opacity:0,x:-140}},{{opacity:1,x:0,duration:.35,ease:"power3.out"}},{t3(tt[2*i]-.15)});')
        js(f'tl.fromTo("#{sid}p{i}",{{opacity:0,scale:.6,x:-30}},{{opacity:1,scale:1,x:0,duration:.35,ease:"back.out(2.5)"}},{t3(tt[2*i+1]-.08)});')
        js(f'tl.fromTo("#{sid}p{i} b",{{color:"#1F2A44"}},{{color:"{col}",duration:.25}},{t3(tt[2*i+1]+.15)});')
    js(f'tl.fromTo("#{sid}note",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.4,ease:"back.out(2)"}},{t3(tt[6]-.1)});')
    js(f'tl.to("#{sid}",{{opacity:0,x:-200,duration:.35,ease:"power2.in"}},{t3(sc["end"]+.45)});')

# --- Совет
tp = S["tip"]; tt = seq("tip", "Artikel", "Plural", "das", "die")
H.append('''<div class="scene" id="sTip">
  <div id="tipHead">💡 Mein Tipp</div>
  <div id="tipTxt">Lerne jedes Nomen mit <b>Artikel</b> + <b>Plural</b></div>
  <div id="card"><div class="cf">Buch</div><div class="cb"><i>das</i> Buch<br/><span><i>die</i> B<b>ü</b>ch<b>er</b></span></div></div>
</div>''')
js(f'tl.set("#sTip",{{opacity:1}},{t3(tp["start"]-.35)});')
js(f'tl.fromTo("#tipHead",{{opacity:0,y:-40}},{{opacity:1,y:0,duration:.4,ease:"back.out(2)"}},{t3(tp["start"]-.3)});')
js(f'tl.fromTo("#tipTxt",{{opacity:0}},{{opacity:1,duration:.4}},{t3(tt[0]-.3)});')
js(f'tl.fromTo("#card",{{opacity:0,y:80,rotation:-4}},{{opacity:1,y:0,rotation:0,duration:.45,ease:"back.out(2)"}},{t3(tt[1])});')
js(f'tl.to("#card .cf",{{rotationY:90,duration:.25,ease:"power2.in"}},{t3(tt[2]-.3)});')
js(f'tl.fromTo("#card .cb",{{rotationY:-90}},{{rotationY:0,duration:.3,ease:"power2.out"}},{t3(tt[2]-.05)});')
js(f'tl.to("#sTip",{{opacity:0,y:-60,duration:.35}},{t3(tp["end"]+.6)});')

# --- Тест
qi, qw, qp, qa = S["qintro"], S["qwords"], S["qpause"], S["qans"]
tw = seq("qwords", *[q[1] for q in QUIZ]); ta = seq("qans", *[q[2] for q in QUIZ])
qrows = "".join(f'''<div class="q" id="q{i}"><span class="qn">{i+1}</span><span class="em">{e}</span><div class="sg"><i>{a}</i> {sg}</div>
  <div class="ans"><span class="qm" id="qm{i}">?</span><span class="qa" id="qa{i}"><i>die</i> {mark(sg, pl) if sg != pl else pl}</span></div></div>''' for i, (a, sg, pl, e) in enumerate(QUIZ))
H.append(f'''<div class="scene" id="sQuiz">
  <div id="qHead"><span>TEST</span> 📝 Wie heißt der Plural?</div>
  <div id="qList">{qrows}</div>
  <div id="timer"><svg viewBox="0 0 200 200"><circle cx="100" cy="100" r="86" class="trk"/><circle id="ring" cx="100" cy="100" r="86" class="rng"/></svg>
    <div id="tnum">{"".join(f'<span id="tn{k}">{k}</span>' for k in range(5, 0, -1))}</div></div>
  <div id="pause">⏸ Pause drücken!</div>
</div>''')
js(f'tl.fromTo("#sQuiz",{{opacity:0}},{{opacity:1,duration:.3}},{t3(qi["start"]-.4)});')
js(f'tl.fromTo("#qHead",{{opacity:0,scale:.5}},{{opacity:1,scale:1,duration:.5,ease:"back.out(2.5)"}},{t3(qi["start"]-.3)});')
js(f'tl.to("#d1,#d2,#d3,#d4,#d5,#d6",{{scale:1.3,duration:.15,stagger:.06,yoyo:true,repeat:1}},{t3(qi["start"])});')
for i in range(5):
    js(f'tl.fromTo("#q{i}",{{opacity:0,y:50}},{{opacity:1,y:0,duration:.3,ease:"back.out(2)"}},{t3(tw[i]-.25)});')
# таймер: 5 секунд паузы между вопросами и ответами
p0 = qp["start"] - .1; p1 = qa["start"] - .2; step = (p1 - qp["end"]) / 5
js(f'tl.fromTo("#timer",{{opacity:0,scale:.5}},{{opacity:1,scale:1,duration:.35,ease:"back.out(2.5)"}},{t3(p0)});')
js(f'tl.fromTo("#pause",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.35,ease:"back.out(2)"}},{t3(p0+.1)});')
js(f'tl.to("#pause",{{scale:1.06,duration:.4,yoyo:true,repeat:{max(1, int((p1-p0)/.4)//2*2-1)},ease:"sine.inOut"}},{t3(p0+.5)});')
js(f'tl.fromTo("#ring",{{strokeDashoffset:0}},{{strokeDashoffset:540.4,duration:{t3(p1-qp["end"])},ease:"none"}},{t3(qp["end"])});')
for k in range(5):
    a = qp["end"] + k * step
    js(f'tl.fromTo("#tn{5-k}",{{opacity:0,scale:1.8}},{{opacity:1,scale:1,duration:.25,ease:"back.out(2)"}},{t3(a)});')
    js(f'tl.to("#tn{5-k}",{{opacity:0,duration:.12}},{t3(a+step-.12)});')
js(f'tl.to(["#timer","#pause"],{{opacity:0,scale:.6,duration:.25}},{t3(p1)});')
for i in range(5):
    js(f'tl.to("#qm{i}",{{opacity:0,scale:0,duration:.15}},{t3(ta[i]-.2)});')
    js(f'tl.fromTo("#qa{i}",{{opacity:0,scale:.5}},{{opacity:1,scale:1,duration:.3,ease:"back.out(3)"}},{t3(ta[i]-.1)});')
    js(f'tl.to("#q{i}",{{backgroundColor:"#EBFBEE",borderColor:"#2F9E44",duration:.25}},{t3(ta[i]-.1)});')
    js(f'tl.fromTo("#qa{i} b",{{color:"#1F2A44"}},{{color:"#2F9E44",duration:.25}},{t3(ta[i]+.1)});')

# --- CTA
ct = S["cta"]
H.append('''<div id="cta"><div class="t1">Wie viele hast du <b>richtig</b>? 🏆</div><div class="t2">Schreib deine Punkte in die Kommentare!</div>
  <div class="pts"><span>0/5</span><span>3/5</span><span>5/5 🔥</span></div></div><div id="arrow">👇</div>''')
js(f'tl.to("#qHead",{{opacity:0,duration:.3}},{t3(ct["start"]-.4)});')
js(f'tl.to("#qList",{{scale:.82,y:-150,transformOrigin:"50% 0%",duration:.5,ease:"power2.inOut"}},{t3(ct["start"]-.4)});')
js(f'tl.fromTo("#cta",{{opacity:0,y:120}},{{opacity:1,y:0,duration:.5,ease:"back.out(1.8)"}},{t3(ct["start"]-.2)});')
js(f'tl.fromTo("#cta .pts span",{{opacity:0,scale:.4}},{{opacity:1,scale:1,duration:.3,stagger:.15,ease:"back.out(3)"}},{t3(ct["start"]+.6)});')
js(f'tl.fromTo("#arrow",{{opacity:0}},{{opacity:1,duration:.3}},{t3(ct["start"]+1)});')
js(f'tl.to("#arrow",{{y:40,duration:.4,yoyo:true,repeat:5,ease:"sine.inOut"}},{t3(ct["start"]+1)});')

# --- Субтитры (караоке): реплики по 1–4 слова, рвём на знаках препинания; во время теста субтитры убираем, чтобы не мешали карточкам
cues, cur = [], []
for w in [x for x in W if x["scene"] not in ("qwords", "qans", "cta")]:
    if cur and cur[-1]["scene"] != w["scene"]: cues.append(cur); cur = []
    cur.append(w)
    if len(cur) >= 4 or w["word"][-1] in ".!?:,": cues.append(cur); cur = []
if cur: cues.append(cur)
cap_html = []
for i, c in enumerate(cues):
    spans = "".join(f'<span id="w{i}_{k}" class="w">{html.escape(x["word"])}</span> ' for k, x in enumerate(c))
    cap_html.append(f'<div id="c{i}" class="cue">{spans}</div>')
    st = c[0]["start"]; en = (cues[i+1][0]["start"] if i+1 < len(cues) and cues[i+1][0]["scene"] == c[0]["scene"] else c[-1]["end"] + 0.35)
    js(f'tl.fromTo("#c{i}",{{opacity:0,y:30,scale:.92}},{{opacity:1,y:0,scale:1,duration:.18,ease:"back.out(2)"}},{st:.3f});')
    js(f'tl.to("#c{i}",{{opacity:0,duration:.12}},{en-0.12:.3f});')
    for k, x in enumerate(c):
        js(f'tl.to("#w{i}_{k}",{{color:"#E8590C",scale:1.08,duration:.08}},{x["start"]:.3f});')
        js(f'tl.to("#w{i}_{k}",{{color:"#1F2A44",scale:1,duration:.1}},{max(x["end"], x["start"]+0.15):.3f});')

# SRT для загрузки в TikTok (весь текст, кроме пауз)
def ts(x): h, r = divmod(x, 3600); m, s = divmod(r, 60); return f"{int(h):02}:{int(m):02}:{int(s):02},{int(round((s % 1) * 1000)) % 1000:03}"
srt, cur = [], []
for w in W:
    if cur and cur[-1]["scene"] != w["scene"]: srt.append(cur); cur = []
    cur.append(w)
    if len(cur) >= 6 or w["word"][-1] in ".!?": srt.append(cur); cur = []
if cur: srt.append(cur)
open("subtitles_de.srt", "w").write("".join(f"{i}\n{ts(c[0]['start'])} --> {ts(c[-1]['end']+.2)}\n{' '.join(x['word'] for x in c)}\n\n" for i, c in enumerate(srt, 1)))

tpl = open("template.html").read()
tpl = tpl.replace("{{D}}", str(D)).replace("{{SCENES}}", "\n".join(H)).replace("{{CAPS}}", "\n".join(cap_html)).replace("{{JS}}", "\n".join(J))
os.makedirs("proj", exist_ok=True)
open("proj/index.html", "w").write(tpl); print("ok", D, len(cues), "cues")
