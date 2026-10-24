# Генерация index.html (HyperFrames) из timeline.json и words.json
import json, os, re, html
TL = json.load(open("timeline.json")); D = round(TL["duration"], 2)
S = {s["id"]: s for s in TL["scenes"]}

# Слова: из faster-whisper (words.json), иначе оценка пропорционально длине слова
def est_words():
    out = []
    for s in TL["scenes"]:
        ws = s["text"].split(); tot = sum(len(w)+1 for w in ws); t = s["start"]; dur = s["end"]-s["start"]
        for w in ws:
            d = dur*(len(w)+1)/tot; out.append({"word": w, "start": t, "end": t+d, "scene": s["id"]}); t += d
    return out
def norm(w): return re.sub(r"[^\wäöüß]", "", w.lower())
def load_words():
    if not os.path.exists("words.json"): return est_words()
    fw = json.load(open("words.json"))["words"]
    # текст берём из сценария, тайминги из Whisper: выравниваем по сцене
    out = []
    for s in TL["scenes"]:
        ws = s["text"].split()
        cand = [w for w in fw if w["start"] >= s["start"]-0.55 and w["start"] < s["end"]+0.2 and w["end"]-w["start"] > 0.01]
        if len(cand) == len(ws):
            for w, c in zip(ws, cand): out.append({"word": w, "start": c["start"], "end": c["end"], "scene": s["id"]})
        else:
            # разное число слов: оценка, но с точными границами сцены
            tot = sum(len(w)+1 for w in ws); t = s["start"]; dur = s["end"]-s["start"]
            j = 0
            for w in ws:
                m = next((c for c in cand[j:] if norm(c["word"]) == norm(w)), None)
                if m: j = cand.index(m)+1; out.append({"word": w, "start": m["start"], "end": m["end"], "scene": s["id"]}); t = m["end"]; continue
                d = dur*(len(w)+1)/tot; out.append({"word": w, "start": t, "end": t+d, "scene": s["id"]}); t += d
            print("warn: word count mismatch in", s["id"], len(ws), len(cand))
    return out
W = load_words()
def wt(scene, word, nth=0):
    hits = [w for w in W if w["scene"] == scene and norm(w["word"]) == norm(word)]
    return round(hits[nth]["start"], 3) if len(hits) > nth else S[scene]["start"]

# Субтитры: реплики по 1–4 слова, рвём на знаках препинания
cues, cur = [], []
for w in [x for x in W if x["scene"] != "cta"]:
    if cur and cur[-1]["scene"] != w["scene"]: cues.append(cur); cur = []
    cur.append(w)
    if len(cur) >= 4 or w["word"][-1] in ".!?:,": cues.append(cur); cur = []
if cur: cues.append(cur)

cap_html, cap_js = [], []
for i, c in enumerate(cues):
    spans = "".join(f'<span id="w{i}_{k}" class="w">{html.escape(x["word"])}</span> ' for k, x in enumerate(c))
    cap_html.append(f'<div id="c{i}" class="cue">{spans}</div>')
    st = c[0]["start"]; en = (cues[i+1][0]["start"] if i+1 < len(cues) and cues[i+1][0]["scene"] == c[0]["scene"] else c[-1]["end"]+0.35)
    cap_js.append(f'tl.fromTo("#c{i}",{{opacity:0,y:30,scale:.92}},{{opacity:1,y:0,scale:1,duration:.18,ease:"back.out(2)"}},{st:.3f});')
    cap_js.append(f'tl.to("#c{i}",{{opacity:0,duration:.12}},{en-0.12:.3f});')
    for k, x in enumerate(c):
        cap_js.append(f'tl.to("#w{i}_{k}",{{color:"#E8590C",scale:1.08,duration:.08}},{x["start"]:.3f});')
        cap_js.append(f'tl.to("#w{i}_{k}",{{color:"#1F2A44",scale:1,duration:.1}},{max(x["end"], x["start"]+0.15):.3f});')

def t(x): return f"{x:.3f}"
g = {k: t(v) for k, v in {
  "hook": S["hook"]["start"], "intro": S["intro"]["start"], "t1": S["t1"]["start"],
  "sit": wt("t1","Sit!"), "t1away": wt("t1","bewegt"),
  "sitzW": wt("sitz","Sitz!"), "sitzDo": wt("sitz","setzt"), "sitzMean": wt("sitz","bedeutet:"),
  "platzW": wt("platz","Platz!"), "platzDo": wt("platz","legt"), "platzMean": wt("platz","heißt:"),
  "kommW": wt("komm","Komm"), "kommDo": wt("komm","steht"),
  "ausToy": S["aus"]["start"], "ausW": wt("aus","Aus!"), "ausBrav": wt("aus","Braver"),
  "gram": S["grammar"]["start"], "gramPol": wt("grammar","höflicher:"), "gramBruno": wt("grammar","Aber"),
  "twist": S["twist"]["start"], "flu": wt("twist","flüstere"), "leck": wt("twist","Willst"),
  "rev": S["reveal"]["start"]-0.9, "revSay": S["reveal"]["start"], "jede": wt("reveal","jeder"),
  "cta": S["cta"]["start"], "end": D}.items()}
tpl = open("template.html").read()
for k, v in g.items(): tpl = tpl.replace("{{"+k+"}}", v)
tpl = tpl.replace("{{D}}", str(D)).replace("{{CAPS}}", "\n".join(cap_html)).replace("{{CAPJS}}", "\n".join(cap_js))
open("proj/index.html", "w").write(tpl); print("ok", D, len(cues), "cues")
