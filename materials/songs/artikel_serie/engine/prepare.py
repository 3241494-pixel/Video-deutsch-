# Подготовка песни из Suno к монтажу: python prepare.py EP_ID путь/к/песне.(mp3|m4a|wav)
# 1) wav 44.1k; 2) вокал отдельно (audio-separator UVR-MDX-NET-Voc_FT); 3) faster-whisper по вокалу (слова со временем);
# 4) привязка слов текста серии к распознанным (difflib) + интерполяция; 5) биты (librosa)
# результат: ../EP_ID/song.wav, lines.json, beats.json
import sys, os, json, re, difflib, subprocess, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import series as S

EP_ID, SRC = sys.argv[1], sys.argv[2]
E = next(e for e in S.EPISODES if e["id"] == EP_ID)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = f"{ROOT}/{EP_ID}"; WORK = f"/home/user/artikel/prep_{EP_ID}"; os.makedirs(WORK, exist_ok=True)
def norm(w): return re.sub(r"[^a-zäöüß]", "", w.lower())

wav = f"{WORK}/song.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC, "-ar", "44100", "-ac", "2", wav], check=True)
voc = glob.glob(f"{WORK}/*(Vocals)*.*")
if not voc:
    subprocess.run(["audio-separator", wav, "-m", "UVR-MDX-NET-Voc_FT.onnx", "--output_dir", WORK, "--model_file_dir", "/home/user/artikel/models"], check=True)
    voc = glob.glob(f"{WORK}/*(Vocals)*.*")
vw = f"{WORK}/vw.json"
if not os.path.exists(vw):
    from faster_whisper import WhisperModel
    m = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(voc[0], language="de", word_timestamps=True, vad_filter=False)
    json.dump([{"word": w.word, "start": w.start, "end": w.end} for s in segs for w in s.words], open(vw, "w"), ensure_ascii=False)

# привязка текста
lines = [{"text": l} for l in S.lyrics(E).splitlines() if l.strip() and not l.startswith("[")]
for L in lines: L["words"] = [t for t in L["text"].split() if norm(t)]
LW = [(i, norm(t)) for i, L in enumerate(lines) for t in L["words"]]
R = json.load(open(vw)); RN = [norm(w["word"]) for w in R]
sm = difflib.SequenceMatcher(None, [x[1] for x in LW], RN, autojunk=False)
T = [None] * len(LW)
for tag, a1, a2, b1, b2 in sm.get_opcodes():
    if tag == "equal" or (tag == "replace" and a2 - a1 == b2 - b1):
        for k in range(a2 - a1): T[a1 + k] = [R[b1 + k]["start"], R[b1 + k]["end"]]
matched = sum(t is not None for t in T)
i = 0
while i < len(T):  # интерполяция пропусков
    if T[i] is None:
        j = i
        while j < len(T) and T[j] is None: j += 1
        s = T[i - 1][1] if i else 0.0; e = T[j][0] if j < len(T) else s + .5 * (j - i)
        step = (e - s) / (j - i)
        for k in range(i, j): T[k] = [round(s + step * (k - i), 3), round(s + step * (k - i + 1), 3)]
        i = j
    else: i += 1
for (li, _), t in zip(LW, T): lines[li].setdefault("t", []).append(t)
for L in lines:
    t = L["t"]
    for k in range(len(t)): t[k][1] = min(t[k][1], t[k][0] + 1.2)
    L["start"], L["end"] = t[0][0], t[-1][1]
    del L["words"]

import librosa
y, sr = librosa.load(wav, sr=22050, mono=True)
dur = round(len(y) / sr, 2)
tempo, bt = librosa.beat.beat_track(y=y, sr=sr, start_bpm=90)
beats = [round(float(x), 3) for x in librosa.frames_to_time(bt, sr=sr)]
os.makedirs(D, exist_ok=True)
subprocess.run(["cp", wav, f"{D}/song.wav"])
json.dump(lines, open(f"{D}/lines.json", "w"), ensure_ascii=False, indent=0)
json.dump({"beats": beats, "duration": dur, "tempo": float(tempo[0] if hasattr(tempo, "__len__") else tempo)}, open(f"{D}/beats.json", "w"))
print(f"matched {matched}/{len(LW)}  duration {dur}s  tempo {float(tempo[0] if hasattr(tempo, '__len__') else tempo):.1f}")
for k, L in enumerate(lines): print(k, round(L["start"], 1), round(L["end"], 1), L["text"][:60])
