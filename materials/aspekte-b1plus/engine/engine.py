# Генератор грамматических роликов (HyperFrames): spec -> озвучка по фразам с паузами -> тайминги слов -> index.html
# Использование: python engine.py spec_name   (spec_name.py лежит рядом и задаёт BLOCKS, CTA, TITLE)
import sys, os, re, json, html, importlib, subprocess
import numpy as np, soundfile as sf

NAME = sys.argv[1]; STEP = sys.argv[2] if len(sys.argv) > 2 else "all"
SPEC = importlib.import_module(NAME)
W_DIR = f"/home/user/gv/{NAME}"; os.makedirs(f"{W_DIR}/seg", exist_ok=True); os.makedirs(f"{W_DIR}/proj", exist_ok=True)
# темп можно переопределить в спецификации (видео 6+ медленнее: SPEED 0.75, паузы длиннее)
SPEED = getattr(SPEC, "SPEED", 0.85)
GAP_SEG = getattr(SPEC, "GAP_SEG", 0.75)        # пауза между фразами
GAP_BLOCK = getattr(SPEC, "GAP_BLOCK", 1.8)     # пауза между блоками
GAP_DOTS = 0.6                                  # пауза на месте «…» внутри фразы (пропуск в тесте)
LEAD = 0.8
TIMER = getattr(SPEC, "TIMER", 5)               # секунд на ответы в тесте (можно задать в блоке "timer")
def timer_of(bi): return SPEC.BLOCKS[bi].get("timer", TIMER) if bi < len(SPEC.BLOCKS) else TIMER

# --- 1. Список фраз в порядке озвучки
def segments():
    out = []
    for bi, b in enumerate(SPEC.BLOCKS):
        if b["kind"] == "quiz":
            parts = [("intro", s) for s in b["intro"]] + [("q", s) for s in b["q_say"]] + [("pause", b.get("pause_say", "Drück auf Pause und denk nach!"))] + [("a", s) for s in b["a_say"]]
        else:
            parts = [("seg", s) for s in b["segs"]]
        for k, (role, s) in enumerate(parts):
            out.append({"block": bi, "role": role, "k": k, "text": s})
    out.append({"block": len(SPEC.BLOCKS), "role": "cta", "k": 0, "text": SPEC.CTA["say"]})
    return out
SEGS = segments()

def tts():
    import sherpa_onnx
    d = "/home/user/models/vits-piper-de_DE-thorsten-high/"
    tts = sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
        vits=sherpa_onnx.OfflineTtsVitsModelConfig(model=d + "de_DE-thorsten-high.onnx", tokens=d + "tokens.txt", data_dir=d + "espeak-ng-data"), num_threads=4)))
    sr0, audio, t = None, [], LEAD
    for i, s in enumerate(SEGS):
        # «…» = настоящая пауза: синтезируем части отдельно и вставляем тишину
        parts, a = [p.strip() for p in s["text"].split("…") if p.strip()], []
        for pi, p in enumerate(parts):
            r = tts.generate(p, sid=0, speed=SPEED); sr0 = r.sample_rate; a.append(np.array(r.samples, np.float32))
            if pi < len(parts) - 1: a.append(np.zeros(int(GAP_DOTS * sr0), np.float32))
        a = np.concatenate(a)
        if i == 0: audio.append(np.zeros(int(LEAD * sr0), np.float32))
        s["start"] = round(t, 3); s["end"] = round(t + len(a) / sr0, 3); audio.append(a); t = s["end"]
        nxt = SEGS[i + 1] if i + 1 < len(SEGS) else None
        gap = 2.2 if nxt is None else (timer_of(s["block"]) + 0.7 if s["role"] == "pause" else (GAP_BLOCK if nxt["block"] != s["block"] else GAP_SEG))
        audio.append(np.zeros(int(gap * sr0), np.float32)); t += gap
    sf.write(f"{W_DIR}/voice.wav", np.concatenate(audio), sr0)
    json.dump({"duration": round(t, 3), "segs": SEGS}, open(f"{W_DIR}/timeline.json", "w"), ensure_ascii=False, indent=1)
    print("voice", round(t, 1), "s")

def whisper():
    os.environ.setdefault("HF_HOME", "/home/user/models/hf")
    from faster_whisper import WhisperModel
    m = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=os.cpu_count())
    prompt = " ".join(s["text"] for s in SEGS)[:800]
    segs, _ = m.transcribe(f"{W_DIR}/voice.wav", language="de", word_timestamps=True, vad_filter=True, initial_prompt=prompt)
    words = [{"word": w.word.strip(), "start": round(float(w.start), 3), "end": round(float(w.end), 3)} for s in segs for w in s.words if w.word.strip()]
    json.dump({"words": words}, open(f"{W_DIR}/fw.words.json", "w"), ensure_ascii=False, indent=1)
    print("whisper", len(words), "words")

# --- 2. Слова сценария с таймингами (текст из сценария, время из Whisper, внутри границ фразы)
def norm(w): return re.sub(r"[^\wäöüß]", "", w.lower())
def load_words(TL, FW):
    out = []
    for si, s in enumerate(TL["segs"]):
        ws = s["text"].split()
        cand = [w for w in FW if w["start"] >= s["start"] - 0.3 and w["start"] < s["end"] + 0.05]
        if len(cand) == len(ws):
            out += [{"word": w, "start": max(c["start"], s["start"]), "end": c["end"], "seg": si} for w, c in zip(ws, cand)]; continue
        # выравнивание difflib: совпавшие слова берут время Whisper, остальные интерполируются между соседями
        import difflib
        sm = difflib.SequenceMatcher(a=[norm(w) for w in ws], b=[norm(c["word"]) for c in cand], autojunk=False)
        st = [None] * len(ws); en = [None] * len(ws)
        for a0, b0, n in sm.get_matching_blocks():
            for q in range(n): st[a0+q] = max(cand[b0+q]["start"], s["start"]); en[a0+q] = min(cand[b0+q]["end"], s["end"] + .1)
        i = 0
        while i < len(ws):
            if st[i] is not None: i += 1; continue
            j2 = i
            while j2 < len(ws) and st[j2] is None: j2 += 1
            lo = en[i-1] if i > 0 else s["start"]; hi = st[j2] if j2 < len(ws) else s["end"]
            tot = sum(len(ws[q]) + 1 for q in range(i, j2)); t = lo
            for q in range(i, j2):
                d = max(hi - lo, .1 * (j2 - i)) * (len(ws[q]) + 1) / tot; st[q] = t; en[q] = t + d; t += d
            i = j2
        out += [{"word": w, "start": st[q], "end": en[q], "seg": si} for q, w in enumerate(ws)]
    return out

def build():
    TL = json.load(open(f"{W_DIR}/timeline.json")); FW = json.load(open(f"{W_DIR}/fw.words.json"))["words"]
    D = round(TL["duration"], 2); SG = TL["segs"]; W = load_words(TL, FW)
    def segof(bi, role, k):
        hits = [i for i, s in enumerate(SG) if s["block"] == bi and (role is None or s["role"] == role)]
        return hits[k]
    def at(bi, spec, role=None):
        # spec: номер фразы в блоке или (номер, слово)
        k, word = (spec, None) if isinstance(spec, int) else spec
        si = segof(bi, role, k) if role else [i for i, s in enumerate(SG) if s["block"] == bi][k]
        if word:
            hit = next((w for w in W if w["seg"] == si and norm(w["word"]) == norm(word)), None)
            if hit: return round(hit["start"], 3)
            print("warn: no word", word, "in", SG[si]["text"])
        return SG[si]["start"]
    H, J = [], []
    js = J.append
    def t3(x): return f"{x:.3f}"
    nrules = sum(1 for b in SPEC.BLOCKS if b.get("num"))
    dots = "".join(f'<div class="dot" id="d{i+1}"></div>' for i in range(nrules))
    starts = [min(s["start"] for s in SG if s["block"] == bi) for bi in range(len(SPEC.BLOCKS) + 1)]
    for bi, b in enumerate(SPEC.BLOCKS):
        bid = f"k{bi}"; col = b.get("color", "#E8590C"); soft = b.get("soft", "#FFF0E6")
        t0 = starts[bi] - 0.5; t1 = starts[bi + 1] - 0.55
        if b["kind"] == "quiz":
            qs = "".join(f'''<div class="qrow" id="{bid}q{i}"><div class="qq"><span class="qn">{i+1}</span><span class="em">{q.get("em","")}</span><span>{q["q"]}</span></div>
              <div class="qa"><span class="qm" id="{bid}m{i}">?</span><span class="qans" id="{bid}a{i}">{q["a"]}</span></div></div>''' for i, q in enumerate(b["items"]))
            T = timer_of(bi); many = " many" if len(b["items"]) >= 5 else ""
            H.append(f'''<div class="scene{many}" id="{bid}" style="--c:{col};--soft:{soft}">
  <div class="qhead"><span>TEST</span> {b["title"]}</div><div class="qlist">{qs}</div>
  <div class="timer" id="{bid}timer"><svg viewBox="0 0 200 200"><circle cx="100" cy="100" r="86" class="trk"/><circle id="{bid}ring" cx="100" cy="100" r="86" class="rng"/></svg>
    <div class="tnum">{"".join(f'<span id="{bid}tn{k}">{k}</span>' for k in range(T, 0, -1))}</div></div>
  <div class="pause" id="{bid}pause">⏸ Pause drücken!</div>
</div>''')
            js(f'tl.fromTo("#{bid}",{{opacity:0}},{{opacity:1,duration:.35}},{t3(t0)});')
            js(f'tl.fromTo("#{bid} .qhead",{{opacity:0,scale:.5}},{{opacity:1,scale:1,duration:.5,ease:"back.out(2.5)"}},{t3(t0+.1)});')
            for i in range(len(b["items"])):
                js(f'tl.fromTo("#{bid}q{i}",{{opacity:0,y:50}},{{opacity:1,y:0,duration:.35,ease:"back.out(2)"}},{t3(at(bi, i, "q")-.2)});')
            # таймер стоит в зоне субтитров: появляется после фразы «Drück auf Pause», когда субтитр уже ушёл
            ps = SG[segof(bi, "pause", 0)]; p0 = ps["end"] + .3; p1 = SG[segof(bi, "a", 0)]["start"] - .25; step = (p1 - p0) / T
            js(f'tl.fromTo("#{bid}timer",{{opacity:0,scale:.5}},{{opacity:1,scale:1,duration:.35,ease:"back.out(2.5)"}},{t3(p0-.15)});')
            js(f'tl.fromTo("#{bid}pause",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.35,ease:"back.out(2)"}},{t3(p0-.1)});')
            js(f'tl.fromTo("#{bid}ring",{{strokeDashoffset:0}},{{strokeDashoffset:540.4,duration:{t3(p1-p0)},ease:"none"}},{t3(p0)});')
            for k in range(T):
                a = p0 + k * step
                js(f'tl.fromTo("#{bid}tn{T-k}",{{opacity:0,scale:1.8}},{{opacity:1,scale:1,duration:.25,ease:"back.out(2)"}},{t3(a)});')
                js(f'tl.to("#{bid}tn{T-k}",{{opacity:0,duration:.12}},{t3(a+step-.12)});')
            js(f'tl.to(["#{bid}timer","#{bid}pause"],{{opacity:0,scale:.6,duration:.25}},{t3(p1)});')
            for i in range(len(b["items"])):
                ta = at(bi, i, "a")
                js(f'tl.to("#{bid}m{i}",{{opacity:0,scale:0,duration:.15}},{t3(ta-.2)});')
                js(f'tl.fromTo("#{bid}a{i}",{{opacity:0,scale:.6}},{{opacity:1,scale:1,duration:.3,ease:"back.out(3)"}},{t3(ta-.1)});')
                js(f'tl.to("#{bid}q{i}",{{backgroundColor:"#EBFBEE",borderColor:"#2F9E44",duration:.25}},{t3(ta-.1)});')
            if bi < len(SPEC.BLOCKS) - 1:   # не последний тест: уходит, как обычная сцена
                js(f'tl.to("#{bid}",{{opacity:0,x:-160,duration:.35,ease:"power2.in"}},{t3(t1)});'); continue
            # последний тест остаётся на экране над CTA, сжимается вверх
            sc, dy = (.62, -60) if many else (.8, -140)
            js(f'tl.to("#{bid} .qhead",{{opacity:0,duration:.3}},{t3(t1)});')
            js(f'tl.to("#{bid} .qlist",{{scale:{sc},y:{dy},transformOrigin:"50% 0%",duration:.5,ease:"power2.inOut"}},{t3(t1)});')
            continue
        head = ""
        if b.get("title"): head = f'<div class="btitle">{b["title"]}</div>'
        if b.get("num"): head = f'<div class="rhead"><div class="rnum">{b["num"]}</div><div class="rlab">{b["label"]}</div></div>'
        elif b.get("label"): head += f'<div class="rhead"><div class="rlab">{b["label"]}</div></div>'
        if b.get("badge"): head += f'<div class="badge" id="{bid}badge">{b["badge"]}</div>'
        rows = ""
        for i, r in enumerate(b.get("rows", [])):
            em = f'<span class="em">{r["em"]}</span>' if r.get("em") else ""
            if "r" in r:
                qa = " qa" if r.get("cls") == "qa" else ""
                rows += f'<div class="row pair{qa}" id="{bid}r{i}">{em}<span class="l">{r["l"]}</span><span class="arr">→</span><span class="r" id="{bid}rr{i}">{r["r"]}</span></div>'
            else:
                rows += f'<div class="row {r.get("cls","line")}" id="{bid}r{i}">{em}<span class="l">{r["l"]}</span></div>'
        tb = b.get("table")
        if tb:
            rows += '<div class="tbl"><div class="trow th"><div></div>' + "".join(f"<div>{h}</div>" for h in tb["cols"]) + "</div>"
            rows += "".join(f'<div class="trow" id="{bid}t{i}">' + "".join(f"<div>{x}</div>" for x in tr) + "</div>" for i, tr in enumerate(tb["rows"])) + "</div>"
        notes = "".join(f'<div class="note" id="{bid}n{i}">{n["html"]}</div>' for i, n in enumerate(b.get("notes", [])))
        H.append(f'<div class="scene" id="{bid}" style="--c:{col};--soft:{soft}">{head}<div class="rows">{rows}</div><div class="notes">{notes}</div></div>')
        js(f'tl.fromTo("#{bid}",{{opacity:0,y:70}},{{opacity:1,y:0,duration:.45,ease:"power3.out"}},{t3(t0)});')
        if b.get("title"): js(f'tl.fromTo("#{bid} .btitle",{{opacity:0,scale:.7}},{{opacity:1,scale:1,duration:.5,ease:"back.out(2)"}},{t3(t0+.05)});')
        if b.get("num"):
            js(f'tl.fromTo("#{bid} .rnum",{{scale:0,rotation:-90}},{{scale:1,rotation:0,duration:.5,ease:"back.out(2.5)"}},{t3(t0+.1)});')
            js(f'tl.to("#d{b["num"]}",{{backgroundColor:"{col}",scale:1.3,duration:.3}},{t3(t0)});'); js(f'tl.to("#d{b["num"]}",{{scale:1,duration:.2}},{t3(t0+.35)});')
        if b.get("badge"): js(f'tl.fromTo("#{bid}badge",{{opacity:0,scale:1.8}},{{opacity:1,scale:1,duration:.45,ease:"back.out(2)"}},{t3(at(bi, b.get("badge_at", 0))+.3)});')
        for i, r in enumerate(b.get("rows", [])):
            ta = at(bi, r.get("at", 0))
            js(f'tl.fromTo("#{bid}r{i}",{{opacity:0,x:-120}},{{opacity:1,x:0,duration:.4,ease:"power3.out"}},{t3(ta-.15)});')
            if "r" in r:
                js(f'tl.fromTo("#{bid}rr{i}",{{opacity:0,scale:.6}},{{opacity:1,scale:1,duration:.35,ease:"back.out(2.5)"}},{t3(at(bi, r.get("rat", r.get("at", 0)))-.05)});')
        if tb:
            js(f'tl.fromTo("#{bid} .th",{{opacity:0,y:-30}},{{opacity:1,y:0,duration:.35}},{t3(t0+.2)});')
            for i, a_ in enumerate(tb["at"]):
                js(f'tl.fromTo("#{bid}t{i}",{{opacity:0,x:-120}},{{opacity:1,x:0,duration:.4,ease:"power3.out"}},{t3(at(bi, a_)-.15)});')
        for i, n in enumerate(b.get("notes", [])):
            js(f'tl.fromTo("#{bid}n{i}",{{opacity:0,y:30,scale:.9}},{{opacity:1,y:0,scale:1,duration:.4,ease:"back.out(2)"}},{t3(at(bi, n.get("at", 0))-.1)});')
        js(f'tl.to("#{bid}",{{opacity:0,x:-160,duration:.35,ease:"power2.in"}},{t3(t1)});')
    # CTA
    tc = starts[-1]
    chips = "".join(f"<span>{c}</span>" for c in SPEC.CTA.get("chips", []))
    H.append(f'<div id="cta"><div class="t1">{SPEC.CTA["t1"]}</div><div class="t2">{SPEC.CTA["t2"]}</div><div class="pts">{chips}</div></div><div id="arrow">👇</div>')
    js(f'tl.fromTo("#cta",{{opacity:0,y:120}},{{opacity:1,y:0,duration:.5,ease:"back.out(1.8)"}},{t3(tc-.3)});')
    if chips: js(f'tl.fromTo("#cta .pts span",{{opacity:0,scale:.4}},{{opacity:1,scale:1,duration:.3,stagger:.15,ease:"back.out(3)"}},{t3(tc+.6)});')
    js(f'tl.fromTo("#arrow",{{opacity:0}},{{opacity:1,duration:.3}},{t3(tc+1)});')
    js(f'tl.to("#arrow",{{y:40,duration:.45,yoyo:true,repeat:5,ease:"sine.inOut"}},{t3(tc+1)});')
    # караоке-субтитры (кроме CTA)
    cues, cur = [], []
    for w in [x for x in W if SG[x["seg"]]["role"] != "cta"]:
        if cur and cur[-1]["seg"] != w["seg"]: cues.append(cur); cur = []
        cur.append(w)
        if len(cur) >= 4 or w["word"][-1] in ".!?:,": cues.append(cur); cur = []
    if cur: cues.append(cur)
    caps = []
    for i, c in enumerate(cues):
        caps.append(f'<div id="c{i}" class="cue">' + "".join(f'<span id="w{i}_{k}" class="w">{html.escape(x["word"])}</span> ' for k, x in enumerate(c)) + "</div>")
        st = c[0]["start"]; en = cues[i+1][0]["start"] if i + 1 < len(cues) and cues[i+1][0]["seg"] == c[0]["seg"] else c[-1]["end"] + 0.4
        js(f'tl.fromTo("#c{i}",{{opacity:0,y:30,scale:.92}},{{opacity:1,y:0,scale:1,duration:.18,ease:"back.out(2)"}},{st:.3f});')
        js(f'tl.to("#c{i}",{{opacity:0,duration:.12}},{en-.12:.3f});')
        for k, x in enumerate(c):
            js(f'tl.to("#w{i}_{k}",{{color:"#E8590C",scale:1.08,duration:.08}},{x["start"]:.3f});')
            js(f'tl.to("#w{i}_{k}",{{color:"#1F2A44",scale:1,duration:.1}},{max(x["end"], x["start"]+.18):.3f});')
    # SRT
    def ts(x): h, r = divmod(x, 3600); m, s = divmod(r, 60); return f"{int(h):02}:{int(m):02}:{int(s):02},{int(round((s % 1) * 1000)) % 1000:03}"
    srt = [[w for w in W if w["seg"] == i] for i in range(len(SG))]
    open(f"{W_DIR}/subtitles_de.srt", "w").write("".join(f"{i}\n{ts(c[0]['start'])} --> {ts(c[-1]['end']+.3)}\n{' '.join(x['word'] for x in c)}\n\n" for i, c in enumerate(srt, 1) if c))
    tpl = open("/home/user/gv/template.html").read()
    tpl = (tpl.replace("{{D}}", str(D)).replace("{{CHIP}}", SPEC.CHIP).replace("{{DOTS}}", dots)
              .replace("{{SCENES}}", "\n".join(H)).replace("{{CAPS}}", "\n".join(caps)).replace("{{JS}}", "\n".join(J)))
    open(f"{W_DIR}/proj/index.html", "w").write(tpl)
    for f in ["gsap.min.js", "hyperframes.json"]: subprocess.run(["cp", f"/home/user/gv/{f}", f"{W_DIR}/proj/"])
    json.dump({"id": NAME, "name": NAME, "createdAt": "2026-10-17T15:30:00.000Z"}, open(f"{W_DIR}/proj/meta.json", "w"))
    print("built", D, "s,", len(cues), "cues")

if STEP in ("all", "tts"): tts()
if STEP in ("all", "whisper"): whisper()
if STEP in ("all", "build"): build()
