# Обложки серии: TikTok 1080x1920 и YouTube 1280x720 -> ../EP_ID/EP_ID_cover_tiktok.png / _cover_youtube.png
# python covers.py [EP_ID ...]   (без аргументов — все серии)
import sys, os, html, subprocess, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import series as S
CH = glob.glob('/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell')[0]

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = "file:///home/user/artikel/assets"
ART = {"der": ("#1C6FD6", "#EAF2FF", "#CFE0FA"), "die": ("#E0313F", "#FFF0F1", "#FAD3D7"), "das": ("#1E9E52", "#EBF8F0", "#C9EBD6")}
FONTS = f'''@font-face{{font-family:Nunito;font-weight:900;src:url({A}/fontsource-nunito-5.2.7/files/nunito-latin-900-normal.woff2);unicode-range:U+0000-024F,U+2000-206F}}
@font-face{{font-family:Nunito;font-weight:900;src:url({A}/fontsource-nunito-5.2.7/files/nunito-cyrillic-900-normal.woff2);unicode-range:U+0400-04FF}}
@font-face{{font-family:Unbounded;font-weight:800;src:url({A}/fontsource-unbounded-5.2.8/files/unbounded-latin-800-normal.woff2)}}
.em{{font-family:"Noto Color Emoji"}}'''

def page(e, W, H):
    C, BG, BG2 = ART[e["art"]]
    ends = [b["show"] for b in e["blocks"]]
    ics = [b["words"][0][1] for b in e["blocks"]]
    v = H > W
    pills = "".join(f'<span class="p" style="transform:rotate({(-1) ** k * (2 + k % 3)}deg)">{html.escape(x)}</span>' for k, x in enumerate(ends))
    icons = "".join(f'<span class="em ic" style="left:{(k * 211 + 40) % (W - 150)}px;top:{(k * 337 + (1150 if v else 420)) % (H - 160) if not v else 1200 + (k % 3) * 170}px;transform:rotate({(-1) ** k * 12}deg)">{i}</span>' for k, i in enumerate(ics))
    css = f'''{FONTS}*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;overflow:hidden;position:relative;font-family:Nunito;color:#232A3D;background:radial-gradient(circle at 25% 15%,#fff,{BG} 45%,{BG2})}}
.chip{{position:absolute;padding:.25em .8em;border-radius:2em;background:#fff;font:900 {44 if v else 30}px Nunito;box-shadow:0 6px 16px rgba(35,42,61,.1)}}
.art{{position:absolute;padding:0 .4em .06em;border-radius:.35em;background:{C};color:#fff;font:800 {260 if v else 170}px Unbounded;box-shadow:0 .05em 0 rgba(0,0,0,.15)}}
.imm{{position:absolute;font:800 {96 if v else 64}px Unbounded;color:#232A3D}}
.ps{{position:absolute;display:flex;flex-wrap:wrap;gap:{22 if v else 14}px}}
.p{{display:inline-block;padding:.05em .45em .12em;border-radius:.45em;background:#fff;color:{C};font:800 {84 if v else (60 if len(ends) <= 4 else 50)}px Unbounded;white-space:nowrap;box-shadow:0 8px 20px rgba(35,42,61,.12)}}
.ic{{position:absolute;font-size:{120 if v else 84}px}}
.uk{{position:absolute;font:900 {48 if v else 30}px Nunito;color:#2B63C6}}'''
    if v:
        body = f'''<div class="chip" style="left:60px;top:70px"><span class="em">🎵</span> Deutsch mit Musik</div>
<div class="chip" style="right:60px;top:70px">Folge {e["no"]}/5</div>
<div class="imm" style="left:0;right:0;top:250px;text-align:center">IMMER</div>
<div style="position:absolute;left:0;right:0;top:390px;text-align:center"><span class="art" style="position:static;display:inline-block">{e["art"]}</span></div>
<div class="ps" style="left:70px;right:70px;top:760px;justify-content:center">{pills}</div>
<div class="uk" style="left:0;right:0;top:1700px;text-align:center">🇺🇦 з перекладом українською</div>
<div style="position:absolute;left:0;right:0;top:1790px;text-align:center"><span class="chip" style="position:static;display:inline-block;background:{C};color:#fff">Sing mit! <span class="em">🎤</span></span></div>'''
        body += "".join(f'<span class="em ic" style="left:{x}px;top:{y}px;transform:rotate({r}deg)">{i}</span>' for i, (x, y, r) in zip(ics, [(110, 1330, -12), (460, 1420, 8), (800, 1320, -6), (280, 1560, 10), (640, 1560, -10), (880, 1520, 6)]))
    else:
        body = f'''<div class="chip" style="left:50px;top:40px"><span class="em">🎵</span> Deutsch mit Musik · Folge {e["no"]}/5</div>
<div class="imm" style="left:60px;top:150px">IMMER</div>
<span class="art" style="left:50px;top:240px">{e["art"]}</span>
<div class="ps" style="left:620px;right:40px;top:110px">{pills}</div>
<div class="uk" style="left:60px;top:520px;width:560px">Artikel lernen mit Endungen<br>🇺🇦 з перекладом</div>
<div class="chip" style="left:60px;top:635px;background:{C};color:#fff">Sing mit! <span class="em">🎤</span></div>'''
        body += "".join(f'<span class="em ic" style="left:{x}px;top:{y}px;transform:rotate({r}deg)">{i}</span>' for i, (x, y, r) in zip(ics, [(760, 600, -12), (900, 610, 8), (1040, 600, -6), (1170, 600, 10)]))
    return f'<!doctype html><meta charset=utf-8><style>{css}</style>{body}'

def main(ids):
    for e in S.EPISODES:
        if ids and e["id"] not in ids: continue
        d = f"{ROOT}/{e['id']}"; os.makedirs(d, exist_ok=True)
        for name, W, H in (("tiktok", 1080, 1920), ("youtube", 1280, 720)):
            hp = f"/home/user/artikel/cover_{e['id']}_{name}.html"; open(hp, "w").write(page(e, W, H))
            out = f"/home/user/artikel/{e['id']}_cover_{name}.png"
            subprocess.run([CH, "--no-sandbox", "--hide-scrollbars", "--allow-file-access-from-files", f"--window-size={W},{H}", "--virtual-time-budget=2000", f"--screenshot={out}", "file://" + hp], capture_output=True)
            subprocess.run(["cp", out, f"{d}/{e['id']}_cover_{name}.png"])
    print("ok")

main(sys.argv[1:])
