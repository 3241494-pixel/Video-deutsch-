# Розпізнавання вокалу з таймінгами слів (без VAD, без підказки)
import os, json, sys
os.environ.setdefault("HF_HOME", "/home/user/models/hf")
from faster_whisper import WhisperModel
m = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=os.cpu_count())
segs, info = m.transcribe(sys.argv[1], language="de", word_timestamps=True, vad_filter=False, condition_on_previous_text=False, beam_size=5)
words = [{"word": w.word.strip(), "start": round(float(w.start), 3), "end": round(float(w.end), 3), "prob": round(float(w.probability), 3)} for s in segs for w in s.words if w.word.strip()]
json.dump(words, open(sys.argv[2], "w"), ensure_ascii=False, indent=0)
print(len(words))
