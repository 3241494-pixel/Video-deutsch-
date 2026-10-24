# Додає до готового index.html рядок українського перекладу під німецькими субтитрами + пише subtitles_uk.srt
import sys, json, html, os, shutil
from uk_translations import UK
V = sys.argv[1]; A = f"/mnt/project-files/tiktok-german/aspekte-b1plus/{V}"; W = f"/home/user/uk/{V}"
os.makedirs(f"{W}/proj", exist_ok=True)
TL = json.load(open(f"{A}/project/timeline.json")); SG = TL["segs"]; L = UK[V]; assert len(L) == len(SG)
src = open(f"{A}/project/index.html").read()
css = """  #ukcaps { position: absolute; left: 50px; right: 50px; top: 1712px; height: 190px; }
  .uk { position: absolute; left: 0; right: 0; top: 0; text-align: center; opacity: 0; }
  .uk span { display: inline-block; max-width: 980px; padding: 10px 28px; border-radius: 26px; background: rgba(255,255,255,.9);
    box-shadow: 0 6px 18px rgba(31,42,68,.08); color: #1971C2; font: 700 46px/1.22 "Inter Display", Inter, sans-serif; }
</style>"""
divs, js, srt = [], [], []
def ts(x): h, r = divmod(x, 3600); m, s = divmod(r, 60); return f"{int(h):02}:{int(m):02}:{int(s):02},{int(round((s % 1) * 1000)) % 1000:03}"
for i, (s, t) in enumerate(zip(SG, L)):
    if not t: continue
    st = s["start"] - .05
    en = s["end"] + (.2 if s["role"] == "pause" else .4)
    if i + 1 < len(SG): en = min(en, SG[i+1]["start"] - .08)
    divs.append(f'<div id="u{i}" class="uk"><span>{html.escape(t)}</span></div>')
    js.append(f'tl.fromTo("#u{i}",{{opacity:0,y:20}},{{opacity:1,y:0,duration:.2,ease:"power2.out"}},{st:.3f});')
    js.append(f'tl.to("#u{i}",{{opacity:0,duration:.15}},{en-.15:.3f});')
    srt.append(f"{len(srt)+1}\n{ts(st)} --> {ts(en)}\n{t}\n\n")
D = TL["duration"]
layer = f'  <div id="ukcaps" class="clip" data-start="0" data-duration="{round(D,2)}" data-track-index="3">\n' + "\n".join(divs) + "\n  </div>\n</div>\n<script>"
assert src.count("</style>") == 1 and src.count("</div>\n<script>") == 1 and src.count("tl.set({}, {}, D);") == 1
src = src.replace("</style>", css).replace("</div>\n<script>", layer).replace("tl.set({}, {}, D);", "\n".join(js) + "\n  tl.set({}, {}, D);")
open(f"{W}/proj/index.html", "w").write(src)
E = "/mnt/project-files/tiktok-german/aspekte-b1plus/engine"
for f in ["gsap.min.js", "hyperframes.json"]: shutil.copy(f"{E}/{f}", f"{W}/proj/")
json.dump({"id": V + "_uk", "name": V + "_uk", "createdAt": "2026-10-23T09:30:00.000Z"}, open(f"{W}/proj/meta.json", "w"))
open(f"{W}/subtitles_uk.srt", "w").write("".join(srt))
print(V, len(srt), "uk cues")
