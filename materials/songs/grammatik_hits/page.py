# Страница для Suno: вкладки по темам, три варианта в каждой, кнопки копирования Style и Lyrics
import html, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from songs import TOPICS
E = html.escape
tabs, panels = [], []
for i, t in enumerate(TOPICS):
    tabs.append(f'<button type="button" class="tab" role="tab" id="tab{t["no"]}" data-t="{t["no"]}" style="--c:{t["color"]}" aria-selected="{str(i==0).lower()}"><b>{t["no"]}</b> {E(t["title"])}</button>')
    cards = []
    for k, v in enumerate(t["vars"], 1):
        sid, lid = f's{t["no"]}{k}', f'l{t["no"]}{k}'
        cards.append(f'''<article class="card">
<header><span class="num">{t["no"]}.{k}</span><h3>{E(v["title"])}</h3></header>
<p class="plot">{E(v["plot"])}</p>
<p class="keys">{E(v["keys"])}</p>
<div class="field"><div class="fh"><b>Style</b><button type="button" class="copy" data-copy="{sid}">Копировать</button></div><pre id="{sid}">{E(v["style"])}</pre></div>
<div class="field"><div class="fh"><b>Lyrics</b><button type="button" class="copy" data-copy="{lid}">Копировать</button></div><pre id="{lid}" class="lyr">{E(v["lyrics"])}</pre></div>
</article>''')
    panels.append(f'''<section class="panel" id="p{t["no"]}" role="tabpanel" style="--c:{t["color"]}" {"" if i==0 else "hidden"}>
<div class="ph"><h2>{E(t["title"])}</h2><p><span class="pill">{E(t["gram"])}</span><span class="pill">{E(t["level"])}</span><span class="pill">{E(t["genre"])}</span></p></div>
<div class="grid">{"".join(cards)}</div></section>''')

page = f'''<title>Грамматика песнями: тексты Suno</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@600;700&family=Golos+Text:wght@400;600&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
/* Макет: вкладки тем сверху, три карточки варианта в ряд (на телефоне столбиком) */
:root {{ --bg:#f3f5f9; --surface:#fff; --ink:#161a2c; --muted:#5d6382; --line:#dde1ec; --soft:#eef1f7; --btn:#161a2c; --btn-ink:#fff;
  --display:"Unbounded","Arial Black",system-ui,sans-serif; --body:"Golos Text",system-ui,sans-serif; --mono:"JetBrains Mono",ui-monospace,Menlo,monospace; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#11131b; --surface:#1a1d29; --ink:#eceef7; --muted:#a2a7c3; --line:#2d3146; --soft:#232737; --btn:#eceef7; --btn-ink:#11131b; color-scheme:dark; }} }}
:root[data-theme="dark"] {{ --bg:#11131b; --surface:#1a1d29; --ink:#eceef7; --muted:#a2a7c3; --line:#2d3146; --soft:#232737; --btn:#eceef7; --btn-ink:#11131b; color-scheme:dark; }}
* {{ box-sizing:border-box; }}
body {{ background:var(--bg); color:var(--ink); font-family:var(--body); font-size:16px; line-height:1.5;
  padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); padding-block:28px 56px; }}
main {{ max-width:1180px; margin:0 auto; display:flex; flex-direction:column; gap:20px; }}
h1,h2,h3 {{ font-family:var(--display); margin:0; text-wrap:balance; line-height:1.2; }}
h1 {{ font-size:clamp(22px,5vw,32px); }} h2 {{ font-size:20px; color:var(--c); }} h3 {{ font-size:16px; }}
.lead {{ color:var(--muted); margin:8px 0 0; max-width:70ch; }}
.tabs {{ display:flex; flex-wrap:wrap; gap:8px; }}
.tab {{ font:600 14px var(--body); background:var(--surface); color:var(--ink); border:1px solid var(--line); border-radius:999px; padding:8px 14px; cursor:pointer; }}
.tab b {{ font-family:var(--display); color:var(--c); margin-right:4px; }}
.tab[aria-selected="true"] {{ background:var(--c); border-color:var(--c); color:#fff; }}
.tab[aria-selected="true"] b {{ color:#fff; }}
.ph {{ display:flex; flex-wrap:wrap; align-items:center; gap:10px 16px; }}
.ph p {{ margin:0; display:flex; flex-wrap:wrap; gap:6px; }}
.pill {{ font-size:13px; border:1px solid var(--c); color:var(--c); border-radius:999px; padding:2px 10px; }}
.panel {{ display:flex; flex-direction:column; gap:16px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:16px; }}
.card {{ background:var(--surface); border:1px solid var(--line); border-top:4px solid var(--c); border-radius:12px; padding:16px; display:flex; flex-direction:column; gap:12px; min-width:0; }}
.card header {{ display:flex; gap:10px; align-items:center; }}
.num {{ font-family:var(--display); font-size:13px; color:#fff; background:var(--c); border-radius:6px; padding:4px 8px; }}
.plot {{ margin:0; font-size:14px; }}
.keys {{ margin:0; font-family:var(--mono); font-size:12px; color:var(--c); background:var(--soft); border-radius:8px; padding:8px 10px; }}
.field {{ display:flex; flex-direction:column; gap:6px; min-width:0; }}
.fh {{ display:flex; justify-content:space-between; align-items:center; }}
.fh b {{ font-size:12px; color:var(--muted); letter-spacing:.06em; text-transform:uppercase; }}
pre {{ margin:0; font-family:var(--mono); font-size:12.5px; background:var(--soft); border-radius:8px; padding:10px; white-space:pre-wrap; overflow-wrap:anywhere; }}
pre.lyr {{ max-height:360px; overflow:auto; }}
.copy {{ font:600 13px var(--body); background:var(--btn); color:var(--btn-ink); border:0; border-radius:8px; padding:7px 12px; cursor:pointer; }}
button:focus-visible {{ outline:2px solid var(--c, var(--ink)); outline-offset:2px; }}
</style>
<main>
<div><h1>Грамматика песнями: 15 текстов для Suno</h1>
<p class="lead">5 тем, по 3 варианта. В вариантах одной темы разные сюжеты, слова и примеры. Строку Style вставляйте в поле Style, текст в поле Lyrics. В каждом стиле прописано чёткое и медленное произношение.</p></div>
<nav class="tabs" role="tablist">{"".join(tabs)}</nav>
{"".join(panels)}
</main>
<script>
const show = n => {{
  document.querySelectorAll(".tab").forEach(b => b.setAttribute("aria-selected", b.dataset.t == n));
  document.querySelectorAll(".panel").forEach(p => p.hidden = p.id != "p" + n);
  try {{ localStorage.setItem("tab", n); }} catch (e) {{}}
}};
document.querySelectorAll(".tab").forEach(b => b.addEventListener("click", () => show(b.dataset.t)));
const h = (location.hash.match(/^#t([1-5])$/) || [])[1];
let saved = null; try {{ saved = localStorage.getItem("tab"); }} catch (e) {{}}
if (h || saved) show(h || saved);
document.querySelectorAll("button[data-copy]").forEach(b => b.addEventListener("click", () => {{
  const el = document.getElementById(b.dataset.copy);
  const done = () => {{ b.textContent = "Скопировано"; setTimeout(() => b.textContent = "Копировать", 1500); }};
  const sel = () => {{ const r = document.createRange(); r.selectNodeContents(el); const s = getSelection(); s.removeAllRanges(); s.addRange(r); }};
  try {{ navigator.clipboard.writeText(el.textContent).then(done, sel); }} catch (e) {{ sel(); }}
}}));
</script>
'''
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "suno.html"), "w").write(page)
print(len(page))
