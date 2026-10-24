# Обкладинки для дитячого кліпу «Hallo, ABC!»: TikTok 1080x1920 і YouTube 1280x720 з власними персонажами
import sys, subprocess
sys.path.insert(0, "/home/user/abc"); from chars import C
CH = "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell"
F = "file:///home/user/abc/proj/"
def svg(k, x, y, s, r=0): return f'<svg viewBox="0 0 400 400" style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;transform:rotate({r}deg);overflow:visible">{C[k]}</svg>'
def tile(ch, x, y, s, c, r): return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;border-radius:{s*.22}px;background:{c};color:#fff;font:700 {s*.68:.0f}px Fredoka;display:flex;align-items:center;justify-content:center;transform:rotate({r}deg);box-shadow:0 {s*.06:.0f}px 0 rgba(0,0,0,.15);border:{s*.045:.0f}px solid rgba(255,255,255,.7)">{ch}</div>'
HEAD = f'''<!doctype html><meta charset=utf-8><style>@font-face{{font-family:Fredoka;font-weight:700;src:url({F}fredoka-latin-700-normal.woff2)}}
@font-face{{font-family:"Inter Display";font-weight:800;src:local("Inter Display ExtraBold")}}
*{{margin:0;padding:0}} body{{width:WWpx;height:HHpx;overflow:hidden;position:relative;background:linear-gradient(#CFEFFF,#EAF8FF 60%,#FFF9EC)}}
.h{{position:absolute;border-radius:50% 50% 0 0}} .chip{{position:absolute;padding:.3em .9em;border-radius:2em;background:#fff;font:700 1em Fredoka;box-shadow:0 .15em .4em rgba(59,47,47,.1)}}
.t{{position:absolute;font:700 1em Fredoka;color:#3B2F2F;line-height:1}}</style>'''
tt = HEAD.replace("WW","1080").replace("HH","1920") + '<div class="h" style="left:-100px;top:1450px;width:800px;height:800px;background:#B2F2BB"></div><div class="h" style="left:450px;top:1550px;width:800px;height:700px;background:#8CE99A"></div>'
tt += tile("A", 110, 230, 260, "#FF6B6B", -8) + tile("B", 410, 200, 260, "#FF922B", 4) + tile("C", 710, 240, 260, "#339AF0", 9)
tt += '<div class="t" style="left:0;right:0;top:580px;text-align:center;font-size:150px"><span style="color:#FF6B6B">Hallo,</span> <span style="color:#51CF66">ABC!</span></div>'
tt += '<div class="t" style="left:0;right:0;top:770px;text-align:center;font-size:62px;color:#5C667D">Das deutsche Alphabet</div>'
tt += svg("apfel", 60, 950, 380, -8) + svg("biene", 620, 900, 400, 8) + svg("zebra", 330, 1210, 430, 0)
tt += '<div class="chip" style="left:60px;top:70px;font-size:44px">🎵 Kinderlied</div><div class="chip" style="right:60px;top:70px;font-size:44px;font-family:\'Inter Display\';color:#1971C2">🇺🇦 з перекладом</div>'
tt += '<div style="position:absolute;left:0;right:0;top:1700px;text-align:center"><span class="chip" style="position:static;display:inline-block;font-size:64px;background:#FF6B6B;color:#fff">Sing mit! 🎤</span></div>'
yt = HEAD.replace("WW","1280").replace("HH","720") + '<div class="h" style="left:-100px;top:560px;width:700px;height:500px;background:#B2F2BB"></div><div class="h" style="left:650px;top:600px;width:800px;height:400px;background:#8CE99A"></div>'
yt += tile("A", 60, 70, 160, "#FF6B6B", -8) + tile("B", 245, 60, 160, "#FF922B", 4) + tile("C", 430, 75, 160, "#339AF0", 9)
yt += '<div class="t" style="left:60px;top:285px;font-size:112px"><span style="color:#FF6B6B">Hallo,</span> <span style="color:#51CF66">ABC!</span></div>'
yt += '<div class="t" style="left:64px;top:415px;font-size:44px;color:#5C667D">Das deutsche Alphabet für Kinder</div>'
yt += '<div class="chip" style="left:60px;top:500px;font-size:30px;font-family:\'Inter Display\';color:#1971C2">🇺🇦 з перекладом</div><div class="chip" style="left:360px;top:500px;font-size:30px">🎵 Kinderlied</div>'
yt += svg("apfel", 700, 40, 300, -8) + svg("biene", 960, 60, 300, 8) + svg("zebra", 820, 330, 360, 0)
for name, html, w, h in (("tiktok", tt, 1080, 1920), ("youtube", yt, 1280, 720)):
    p = f"/home/user/abc/cover_{name}.html"; open(p, "w").write(html)
    subprocess.run([CH, "--no-sandbox", "--hide-scrollbars", f"--window-size={w},{h}", f"--screenshot=/home/user/abc/hallo_abc_cover_{name}.png", "file://" + p], capture_output=True)
print("ok")
