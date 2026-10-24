# Страница серии для скачивания: видео, обложки, названия с тегами, описания YouTube, фильтры и отметки
# python page.py OUT_DIR  -> OUT_DIR/index.html (+ копирует mp4/png, которые уже отрендерены)
import sys, os, json, html, shutil, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import series as S
import importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
spec = importlib.util.spec_from_file_location("meta", os.path.join(os.path.dirname(os.path.abspath(__file__)), "meta.py"))
# meta.py при импорте перезаписывает meta.md — это безопасно и даёт свежие таймкоды
meta = importlib.util.module_from_spec(spec); spec.loader.exec_module(meta)

ARTC = {"der": "var(--der)", "die": "var(--die)", "das": "var(--das)"}
def esc(s): return html.escape(s, quote=True)
def dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout.strip()
    t = float(r or 0); return f"{int(t // 60)}:{int(t % 60):02d}"

def copy_btn(label, text, big=False):
    return f'''<div class="row"><span class="lbl">{label}</span><button type="button" class="cp" data-copy="{esc(text)}">Копировать</button></div>
<{"pre" if big else "p"} class="{"descr" if big else "ttl"}">{esc(text)}</{"pre" if big else "p"}>'''

cards = []
for e in S.EPISODES:
    tt, yt, yt_h, desc = meta.build(e)
    d = f"{ROOT}/{e['id']}"
    ends = " ".join(b["show"] for b in e["blocks"])
    for fmt in ("v", "h"):
        mp4 = f"{e['id']}.mp4" if fmt == "v" else f"{e['id']}_youtube.mp4"
        cov = f"{e['id']}_cover_{'tiktok' if fmt == 'v' else 'youtube'}.png"
        if not os.path.exists(f"{d}/{mp4}"): continue
        # страница принимает файлы до 15 МБ: перекодируем с CRF 21 (для анимации визуально без потерь), звук без изменений
        if not os.path.exists(f"{OUT}/{mp4}") or os.path.getsize(f"{OUT}/{mp4}") > 15_000_000:
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{d}/{mp4}", "-c:v", "libx264", "-preset", "slow", "-crf", "21",
                            "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-c:a", "copy", f"{OUT}/{mp4}"], check=True)
        shutil.copy(f"{d}/{cov}", OUT)
        kinds = "downloaded,tiktok,youtube" if fmt == "v" else "downloaded,youtube"
        post = (copy_btn("TikTok: название с тегами", tt) + copy_btn("YouTube Shorts: название с тегами", yt)) if fmt == "v" else \
               (copy_btn("YouTube: название с тегами", yt_h) + '<details><summary>Описание YouTube</summary>' + copy_btn("Описание", desc, True) + '</details>')
        cards.append(f'''<article class="item {'wide' if fmt == 'h' else ''}" data-fmt="{fmt}" data-ep="{e['no']}" data-kinds="{kinds}" style="--c:{ARTC[e['art']]}">
  <video src="{mp4}" controls playsinline preload="metadata" poster="{cov}"></video>
  <div class="head"><span class="badge">{e['art']}</span><div><h2>{e['no']}. {esc(e['title'])}</h2><p class="ends">{esc(ends)}</p></div></div>
  <div class="meta"><span>{dur(f"{d}/{mp4}")}</span><span>{'TikTok 1080×1920' if fmt == 'v' else 'YouTube 1920×1080'}</span><span>🇺🇦 переклад</span></div>
  <button type="button" class="dl" data-file="{mp4}">Скачать MP4</button>
  <div class="marks"></div>
  <div class="post">{post}</div>
  <div class="cover"><img src="{cov}" alt="Обложка {'TikTok' if fmt == 'v' else 'YouTube'}" loading="lazy"><button type="button" class="dl alt" data-file="{cov}">Скачать обложку PNG</button></div>
</article>''')

PAGE = '''<title>Артикли: видео серии</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@700;800&family=Nunito:wght@600;800;900&display=swap">
<style>
/* Сетка карточек: вертикальные ролики по 3 в ряд, горизонтальные по 2; на телефоне одна колонка */
:root {
  --bg: #f4f6fa; --card: #ffffff; --fg: #1f2537; --muted: #5f6680; --line: #e0e4ee; --chip: #eef1f7;
  --der: #1c6fd6; --die: #e0313f; --das: #1e9e52; --ok: #1f8a4c; --ok-bg: #e3f5ea; --btn: #1f2537; --btn-fg: #fff;
  --display: "Unbounded", "Arial Black", system-ui, sans-serif; --body: "Nunito", system-ui, -apple-system, sans-serif;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #12141b; --card: #1b1e28; --fg: #eceef6; --muted: #a3a9be; --line: #2c3142; --chip: #252a38;
  --der: #6fa2ff; --die: #ff6f7c; --das: #52d18b; --ok: #5fd08f; --ok-bg: #173325; --btn: #eceef6; --btn-fg: #12141b; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #12141b; --card: #1b1e28; --fg: #eceef6; --muted: #a3a9be; --line: #2c3142; --chip: #252a38;
  --der: #6fa2ff; --die: #ff6f7c; --das: #52d18b; --ok: #5fd08f; --ok-bg: #173325; --btn: #eceef6; --btn-fg: #12141b; color-scheme: dark }
* { box-sizing: border-box; }
body { background: var(--bg); color: var(--fg); font-family: var(--body); font-size: 15px; line-height: 1.5; }
.wrap { max-width: 1100px; margin: 0 auto; padding-block: 32px 56px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
h1 { font-family: var(--display); font-weight: 800; font-size: clamp(26px, 5vw, 38px); margin: 0 0 6px; text-wrap: balance; }
h1 .d1 { color: var(--der); } h1 .d2 { color: var(--die); } h1 .d3 { color: var(--das); }
.lead { color: var(--muted); margin: 0 0 18px; max-width: 64ch; }
.bar { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin: 0 0 14px; }
.note { color: var(--muted); font-size: 13px; font-variant-numeric: tabular-nums; }
.filter { font: 800 13px var(--body); color: var(--fg); background: var(--card); border: 1px solid var(--line); border-radius: 99px; padding: 5px 13px; cursor: pointer; }
.filter[aria-pressed="true"] { background: var(--fg); color: var(--bg); border-color: var(--fg); }
.sep { width: 1px; height: 22px; background: var(--line); margin: 0 4px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 22px; margin-top: 22px; }
.item { background: var(--card); border: 1px solid var(--line); border-top: 4px solid var(--c); border-radius: 16px; padding: 16px; display: flex; flex-direction: column; gap: 12px; min-width: 0; }
.item.wide { grid-column: span 2; }
@media (max-width: 700px) { .item.wide { grid-column: auto; } }
.item.done { box-shadow: 0 0 0 2px var(--ok) inset; }
video { width: 100%; aspect-ratio: 9 / 16; border-radius: 10px; background: #000; display: block; }
.item.wide video { aspect-ratio: 16 / 9; }
.head { display: flex; gap: 10px; align-items: center; }
.head > div { min-width: 0; }
.badge { font: 800 14px var(--display); color: #fff; background: var(--c); border-radius: 8px; padding: 5px 9px; }
h2 { font-family: var(--display); font-weight: 700; font-size: 17px; margin: 0; }
.ends { margin: 0; color: var(--c); font-weight: 800; font-size: 13px; }
.meta { display: flex; flex-wrap: wrap; gap: 6px; }
.meta span { background: var(--chip); font-size: 12px; font-weight: 800; padding: 2px 9px; border-radius: 99px; font-variant-numeric: tabular-nums; }
.dl { font: 800 15px var(--body); color: var(--btn-fg); background: var(--btn); border: 0; border-radius: 12px; padding: 10px 16px; cursor: pointer; }
.dl.alt { background: var(--chip); color: var(--fg); font-size: 13px; padding: 8px 12px; }
.dl:disabled { opacity: .6; cursor: progress; }
.dl:focus-visible, .filter:focus-visible, .mark:focus-visible, .cp:focus-visible, summary:focus-visible { outline: 2px solid var(--c, var(--der)); outline-offset: 2px; }
.marks { display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 6px; }
.mark { font: 800 13px var(--body); color: var(--muted); background: transparent; border: 1.5px dashed var(--line); border-radius: 10px; padding: 6px 4px; cursor: pointer; display: flex; flex-direction: column; align-items: center; line-height: 1.25; }
.mark small { font-size: 11px; font-weight: 600; font-variant-numeric: tabular-nums; }
.mark[aria-pressed="true"] { color: var(--ok); background: var(--ok-bg); border: 1.5px solid var(--ok); }
.mark:disabled { cursor: default; opacity: .55; }
.post { border-top: 1px dashed var(--line); padding-top: 10px; display: flex; flex-direction: column; gap: 4px; min-width: 0; }
.row { display: flex; align-items: center; justify-content: space-between; gap: 8px; }
.lbl { font-size: 12px; font-weight: 800; color: var(--muted); text-transform: uppercase; letter-spacing: .04em; }
.ttl { margin: 0 0 6px; overflow-wrap: anywhere; font-weight: 800; }
.descr { margin: 0; white-space: pre-wrap; overflow-wrap: anywhere; font: 600 13px/1.45 var(--body); color: var(--muted); background: var(--chip); border-radius: 8px; padding: 10px; max-height: 260px; overflow: auto; }
.cp { font: 800 12px var(--body); color: var(--fg); background: var(--chip); border: 1px solid var(--line); border-radius: 99px; padding: 4px 11px; cursor: pointer; flex: none; }
details summary { cursor: pointer; font-weight: 800; font-size: 14px; margin: 4px 0; }
.cover { display: flex; flex-direction: column; gap: 8px; }
.cover img { border-radius: 10px; border: 1px solid var(--line); max-height: 220px; object-fit: contain; align-self: flex-start; }
.item[hidden] { display: none; }
.empty { color: var(--muted); padding: 30px 0; }
</style>
<div class="wrap">
  <h1>Серия <span class="d1">der</span> · <span class="d2">die</span> · <span class="d3">das</span>: артикли по окончаниям</h1>
  <p class="lead">Пять анимированных песен-клипов. У каждой серии вертикальное видео для TikTok и Shorts, горизонтальное для YouTube, обложки, названия с тегами и описание для YouTube. Отметки «Скачано», «TikTok» и «YouTube» сохраняются и видны на всех устройствах.</p>
  <div class="bar">
    <button type="button" class="dl" id="zipV">Скачать все TikTok-видео</button>
    <button type="button" class="dl alt" id="zipH">Скачать все YouTube-видео</button>
    <span class="note" id="zipNote"></span>
  </div>
  <div class="bar">
    <span class="note">Формат:</span>
    <button type="button" class="filter" data-group="fmt" data-val="all" aria-pressed="true">Все</button>
    <button type="button" class="filter" data-group="fmt" data-val="v">TikTok / Shorts</button>
    <button type="button" class="filter" data-group="fmt" data-val="h">YouTube 16:9</button>
    <span class="sep"></span>
    <span class="note">Серия:</span>
    <button type="button" class="filter" data-group="ep" data-val="all" aria-pressed="true">Все</button>
    EPBTNS
  </div>
  <div class="bar">
    <span class="note">Показать:</span>
    <button type="button" class="filter" data-group="st" data-val="all" aria-pressed="true">Все</button>
    <button type="button" class="filter" data-group="st" data-val="downloaded">Не скачано</button>
    <button type="button" class="filter" data-group="st" data-val="tiktok">Не в TikTok</button>
    <button type="button" class="filter" data-group="st" data-val="youtube">Не на YouTube</button>
    <span class="note" id="stats">Отметки загружаются…</span>
  </div>
  <div class="grid" id="grid">
CARDS
  </div>
  <p class="empty" id="empty" hidden>Под эти фильтры ничего не подходит.</p>
</div>
<script>
// Копирование: если буфер недоступен, выделяем текст рядом с кнопкой
document.addEventListener("click", async e => {
  const b = e.target.closest("button.cp"); if (!b) return;
  try { await navigator.clipboard.writeText(b.dataset.copy); b.textContent = "Скопировано ✓"; }
  catch { const p = b.parentElement.nextElementSibling; const r = document.createRange(); r.selectNodeContents(p);
    const s = getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = "Выделено, нажми Ctrl+C"; }
  setTimeout(() => { b.textContent = "Копировать"; }, 2000);
});

const items = [...document.querySelectorAll("article.item")];
const fileOf = a => a.querySelector("video").getAttribute("src");
const mb = n => (n / 1048576).toFixed(1).replace(".", ",") + " МБ";
const dlP = window.claude ? claude.use("downloads") : Promise.resolve(null);
let downloads = null;
dlP.then(d => { downloads = d; if (!d) document.querySelectorAll(".dl").forEach(b => { b.disabled = true; b.title = "Скачивание недоступно в этом окне"; }); });

items.forEach(a => {
  const b = a.querySelector("button.dl[data-file$='.mp4']");
  fetch(fileOf(a), { method: "HEAD" }).then(r => { const n = +r.headers.get("content-length"); if (n) b.textContent = "Скачать MP4 · " + mb(n); b.dataset.label = b.textContent; }).catch(() => {});
});
async function getBlob(f) { const r = await fetch(f); if (!r.ok) throw new Error("HTTP " + r.status); return r.blob(); }
function errText(e) {
  const c = e && e.code;
  if (c === "declined") return "Отменено";
  if (c === "rate_limited") return "Подожди и нажми ещё раз";
  return "Не получилось, попробуй ещё раз";
}
async function save(filename, data) { if (!downloads) throw { code: "unavailable" }; return downloads.save({ filename, data }); }

document.addEventListener("click", async e => {
  const b = e.target.closest("button.dl[data-file]"); if (!b || b.disabled) return;
  const label = b.dataset.label || b.textContent; b.disabled = true; b.textContent = "Готовлю файл…";
  try { await save(b.dataset.file, await getBlob(b.dataset.file)); b.textContent = "Сохранено ✓"; if (/\\.mp4$/.test(b.dataset.file)) markDownloaded([b.dataset.file]); }
  catch (err) { b.textContent = errText(err); }
  setTimeout(() => { b.textContent = label; b.disabled = false; }, 2500);
});

// ZIP без сжатия: mp4 уже сжат, архив собирается в браузере
const CRC = (() => { const t = new Uint32Array(256); for (let i = 0; i < 256; i++) { let c = i; for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; t[i] = c >>> 0; } return t; })();
function crc32(u8) { let c = 0xFFFFFFFF; for (let i = 0; i < u8.length; i++) c = CRC[(c ^ u8[i]) & 255] ^ (c >>> 8); return (c ^ 0xFFFFFFFF) >>> 0; }
function makeZip(entries) {
  const enc = new TextEncoder(), parts = [], central = []; let offset = 0;
  for (const { name, data } of entries) {
    const n = enc.encode(name), crc = crc32(data), size = data.length;
    const h = new DataView(new ArrayBuffer(30));
    h.setUint32(0, 0x04034b50, true); h.setUint16(4, 20, true); h.setUint16(6, 0x0800, true); h.setUint32(10, 0x00210000, true);
    h.setUint32(14, crc, true); h.setUint32(18, size, true); h.setUint32(22, size, true); h.setUint16(26, n.length, true);
    parts.push(h.buffer, n, data);
    const c = new DataView(new ArrayBuffer(46));
    c.setUint32(0, 0x02014b50, true); c.setUint16(4, 20, true); c.setUint16(6, 20, true); c.setUint16(8, 0x0800, true);
    c.setUint32(12, 0x00210000, true); c.setUint32(16, crc, true); c.setUint32(20, size, true); c.setUint32(24, size, true);
    c.setUint16(28, n.length, true); c.setUint32(42, offset, true);
    central.push(c.buffer, n); offset += 30 + n.length + size;
  }
  const cd = central.reduce((s, p) => s + p.byteLength, 0), end = new DataView(new ArrayBuffer(22));
  end.setUint32(0, 0x06054b50, true); end.setUint16(8, entries.length, true); end.setUint16(10, entries.length, true);
  end.setUint32(12, cd, true); end.setUint32(16, offset, true);
  return new Blob([...parts, ...central, end.buffer], { type: "application/zip" });
}
async function zipAll(btn, fmt, name) {
  if (btn.disabled) return;
  const label = btn.textContent, note = document.getElementById("zipNote"); btn.disabled = true;
  const sel = items.filter(a => a.dataset.fmt === fmt);
  try {
    const entries = [];
    for (let i = 0; i < sel.length; i++) {
      btn.textContent = "Загружаю " + (i + 1) + " из " + sel.length + "…";
      const f = fileOf(sel[i]); entries.push({ name: f, data: new Uint8Array(await (await getBlob(f)).arrayBuffer()) });
      const cov = sel[i].querySelector(".cover button").dataset.file;
      entries.push({ name: cov, data: new Uint8Array(await (await getBlob(cov)).arrayBuffer()) });
    }
    btn.textContent = "Собираю архив…"; const zip = makeZip(entries); note.textContent = "Архив " + mb(zip.size);
    await save(name, zip); btn.textContent = "Сохранено ✓"; markDownloaded(sel.map(fileOf));
  } catch (err) { btn.textContent = errText(err); }
  setTimeout(() => { btn.textContent = label; btn.disabled = false; }, 3000);
}
document.getElementById("zipV").addEventListener("click", e => zipAll(e.currentTarget, "v", "artikel-serie-tiktok.zip"));
document.getElementById("zipH").addEventListener("click", e => zipAll(e.currentTarget, "h", "artikel-serie-youtube.zip"));

// Отметки в общей базе: marks/<файл> = {downloaded, tiktok, youtube} (дата ISO или null)
const NAMES = { downloaded: "Скачано", tiktok: "TikTok", youtube: "YouTube" };
const marks = {}; let dbRef = null; const F = { fmt: "all", ep: "all", st: "all" };
const fmtDate = iso => new Date(iso).toLocaleDateString("ru-RU", { day: "numeric", month: "short" });
items.forEach(a => {
  a.querySelector(".marks").innerHTML = a.dataset.kinds.split(",").map(k =>
    `<button type="button" class="mark" data-kind="${k}" data-file="${fileOf(a)}" aria-pressed="false" disabled>${NAMES[k]}<small>—</small></button>`).join("");
});
function render() {
  let dl = 0, tt = 0, yt = 0, shown = 0;
  const nV = items.filter(a => a.dataset.fmt === "v").length;
  items.forEach(a => {
    const f = fileOf(a), m = marks[f] || {}, kinds = a.dataset.kinds.split(",");
    a.querySelectorAll(".mark").forEach(b => {
      const on = !!m[b.dataset.kind]; b.setAttribute("aria-pressed", on); b.disabled = !dbRef;
      b.querySelector("small").textContent = on ? "✓ " + fmtDate(m[b.dataset.kind]) : "нет";
    });
    if (m.downloaded) dl++; if (m.tiktok) tt++; if (m.youtube) yt++;
    a.classList.toggle("done", kinds.filter(k => k !== "downloaded").every(k => m[k]));
    const hide = (F.fmt !== "all" && a.dataset.fmt !== F.fmt) || (F.ep !== "all" && a.dataset.ep !== F.ep) ||
      (F.st !== "all" && (!kinds.includes(F.st) || !!m[F.st]));
    a.hidden = hide; if (!hide) shown++;
  });
  document.getElementById("empty").hidden = shown > 0;
  document.getElementById("stats").textContent = dbRef
    ? `Скачано ${dl} из ${items.length} · TikTok ${tt} из ${nV} · YouTube ${yt} из ${items.length}`
    : "Отметки недоступны в этом окне";
}
async function saveMark(file, patch) {
  if (!dbRef) return;
  const prev = marks[file] || {}, next = { downloaded: null, tiktok: null, youtube: null, ...prev, ...patch };
  marks[file] = next; render();
  try { await dbRef.doc(file).set(next); }
  catch { marks[file] = prev; render(); document.getElementById("stats").textContent = "Не удалось сохранить отметку, попробуй ещё раз"; }
}
function markDownloaded(files) { const now = new Date().toISOString(); files.forEach(f => { if (!(marks[f] || {}).downloaded) saveMark(f, { downloaded: now }); }); }
document.addEventListener("click", e => {
  const b = e.target.closest("button.mark");
  if (b && !b.disabled) { const on = b.getAttribute("aria-pressed") === "true"; saveMark(b.dataset.file, { [b.dataset.kind]: on ? null : new Date().toISOString() }); return; }
  const f = e.target.closest("button.filter");
  if (f) { F[f.dataset.group] = f.dataset.val;
    document.querySelectorAll(`button.filter[data-group="${f.dataset.group}"]`).forEach(x => x.setAttribute("aria-pressed", x === f)); render(); }
});
render();
(window.claude ? claude.use("db") : Promise.resolve(null)).then(db => {
  if (!db) { render(); return; }
  dbRef = db.collection("marks");
  dbRef.onSnapshot(snap => { Object.keys(marks).forEach(k => delete marks[k]); snap.docs.forEach(d => { marks[d.id] = d.data(); }); render(); },
    () => { dbRef = null; render(); });
  render();
});
</script>
'''
epbtns = "".join(f'<button type="button" class="filter" data-group="ep" data-val="{e["no"]}">{e["no"]} · {e["art"]}</button>' for e in S.EPISODES)
open(f"{OUT}/index.html", "w").write(PAGE.replace("EPBTNS", epbtns).replace("CARDS", "\n".join(cards)))
print("ok", len(cards), "cards")
