# Обкладинки TikTok (1080x1920) і YouTube (1280x720) для пісенних кліпів, світла тема
import subprocess, os
CH = "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell"
SONGS = {
 "ich_mache_weiter": dict(t1="Trennbare", t2="Verben", sub="als Song zum Mitsingen", n="60 Verben", song="Ich mache weiter",
   rows=[("Infinitiv", '<em class="o">auf</em>stehen'), ("Präsens", 'ich stehe <em class="o">auf</em>'), ("Perfekt", 'ich <em class="v">bin</em> <em class="o">auf</em><em class="g">ge</em>standen')]),
 "drei_formen": dict(t1="Starke", t2="Verben", sub="drei Formen zum Mitsingen", n="28 Verben", song="Drei Formen, sing sie laut",
   rows=[("Infinitiv", '<em class="o">gehen</em>'), ("Präteritum", '<em class="b">ging</em>'), ("Partizip II", '<em class="g"><u>ge</u>gangen</em>')]),
}
CSS = """
@font-face { font-family: "Inter Display"; font-weight: 800; src: local("Inter Display ExtraBold"); }
@font-face { font-family: "Inter Display"; font-weight: 900; src: local("Inter Display Black"); }
*{margin:0;padding:0;box-sizing:border-box} body{width:%dpx;height:%dpx;overflow:hidden;background:#FFF7EC;font-family:"Inter Display",Inter,sans-serif;color:#1F2A44;position:relative}
.blob{position:absolute;border-radius:50%%} em{font-style:normal} .o{color:#E8590C}.g{color:#0CA678}.b{color:#1C7ED6}.v{color:#7048E8}
u{text-decoration-thickness:.09em;text-underline-offset:.12em}
.chip{display:inline-block;padding:.35em .8em;border-radius:2em;background:#1F2A44;color:#fff;font-weight:800}
.chip b{color:#FFA94D}
.t1{font-weight:900;line-height:.95;letter-spacing:-.02em} .t2{color:#E8590C}
.sub{font-weight:800;color:#5C667D}
.row{background:#fff;border-radius:.6em;box-shadow:0 .25em .6em rgba(31,42,68,.12);border-left:.22em solid #FFA94D;padding:.3em .6em .35em}
.row:nth-child(2){border-left-color:#4DABF7}.row:nth-child(3){border-left-color:#63E6BE}
.row small{display:block;font:800 .32em Inter;letter-spacing:.08em;text-transform:uppercase;color:#868E96}
.row div{font-weight:900;white-space:nowrap}
.badges span{display:inline-block;padding:.3em .7em;border-radius:1.4em;background:#fff;font-weight:800;box-shadow:0 .15em .4em rgba(31,42,68,.08);margin-right:.4em}
.note{position:absolute;font-family:"Noto Color Emoji"}
"""
def tiktok(s):
    rows = "".join(f'<div class="row" style="margin-bottom:26px"><small>{a}</small><div>{b}</div></div>' for a, b in s["rows"])
    return f"""<style>{CSS % (1080,1920)}</style>
<div class="blob" style="left:-200px;top:120px;width:720px;height:720px;background:#FFE3C2"></div>
<div class="blob" style="left:620px;top:900px;width:640px;height:640px;background:#DBE4FF"></div>
<div class="blob" style="left:-160px;top:1450px;width:600px;height:600px;background:#D3F9D8"></div>
<div class="note" style="left:850px;top:1560px;font-size:130px;transform:rotate(14deg)">🎵</div>
<div style="position:absolute;left:70px;right:70px;top:150px">
 <div class="chip" style="font-size:44px">🎵 Song <b>· A2–B1</b></div>
 <div class="t1" style="font-size:190px;margin-top:50px">{s['t1']}<br><span class="t2">{s['t2']}</span></div>
 <div class="sub" style="font-size:62px;margin-top:30px">{s['sub']}</div>
 <div style="font-size:84px;margin-top:70px">{rows}</div>
 <div class="badges" style="font-size:44px;margin-top:40px"><span>🇺🇦 з перекладом</span><span>{s['n']}</span></div>
</div>
<div style="position:absolute;left:0;right:0;top:1640px;text-align:center"><span class="chip" style="font-size:64px;background:#E8590C">Sing mit! 🎤</span></div>"""
def youtube(s):
    rows = "".join(f'<div class="row" style="margin-bottom:16px"><small>{a}</small><div>{b}</div></div>' for a, b in s["rows"])
    return f"""<style>{CSS % (1280,720)}</style>
<div class="blob" style="left:-140px;top:-160px;width:560px;height:560px;background:#FFE3C2"></div>
<div class="blob" style="left:900px;top:380px;width:520px;height:520px;background:#DBE4FF"></div>
<div class="blob" style="left:420px;top:520px;width:360px;height:360px;background:#D3F9D8"></div>
<div style="position:absolute;left:56px;top:56px;width:640px">
 <div class="chip" style="font-size:28px">🎵 Song <b>· A2–B1</b></div>
 <div class="t1" style="font-size:100px;margin-top:28px">{s['t1']}<br><span class="t2">{s['t2']}</span></div>
 <div class="sub" style="font-size:38px;margin-top:18px">{s['sub']}</div>
 <div class="badges" style="font-size:28px;margin-top:30px"><span>🇺🇦 з перекладом</span><span>{s['n']}</span></div>
</div>
<div style="position:absolute;right:50px;top:120px;width:600px;font-size:52px">{rows}</div>
<div style="position:absolute;left:56px;bottom:56px"><span class="chip" style="font-size:36px;background:#E8590C">Sing mit! 🎤</span></div>"""
for k, s in SONGS.items():
    for kind, fn, w, h in (("tiktok", tiktok, 1080, 1920), ("youtube", youtube, 1280, 720)):
        p = f"/home/user/covers/{k}_{kind}.html"; open(p, "w").write("<!doctype html><meta charset=utf-8>" + fn(s))
        out = f"/home/user/covers/{k}_cover_{kind}.png"
        subprocess.run([CH, "--no-sandbox", "--hide-scrollbars", f"--window-size={w},{h}", f"--screenshot={out}", "file://" + p], capture_output=True)
        print(out, os.path.exists(out))
