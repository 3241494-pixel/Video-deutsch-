# Склейка озвучки сцен с паузами -> voice.wav + timeline.json
import json, numpy as np, soundfile as sf
scenes = json.load(open("script.json"))
lead = 1.2  # тишина в начале, пока появляется хук
gaps = {"hook":0.7,"intro":0.8,"t1":0.9,"sitz":0.8,"platz":0.8,"komm":0.8,"aus":1.0,"grammar":1.0,"twist":1.6,"reveal":0.9,"cta":2.5}
out, t, sr0, tl = [], lead, None, []
for s in scenes:
    a, sr = sf.read(f"audio/{s['id']}.wav", dtype="float32"); sr0 = sr0 or sr
    if not out: out.append(np.zeros(int(lead*sr), np.float32))
    out.append(a); d = len(a)/sr
    tl.append({"id": s["id"], "start": round(t,3), "end": round(t+d,3), "text": s["text"]})
    out.append(np.zeros(int(gaps[s["id"]]*sr), np.float32)); t += d + gaps[s["id"]]
sf.write("voice.wav", np.concatenate(out), sr0)
json.dump({"duration": round(t,3), "scenes": tl}, open("timeline.json","w"), ensure_ascii=False, indent=1)
print(round(t,2))
