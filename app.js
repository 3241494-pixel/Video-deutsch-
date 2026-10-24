// Видео Deutsch: каталог роликов, тексты для соцсетей и отметки «опубликовано» в GitHub
"use strict";

// Репозиторий: на GitHub Pages определяем по адресу, иначе берём основной
const REPO = (() => {
  const m = location.hostname.match(/^([^.]+)\.github\.io$/i);
  const seg = location.pathname.split("/").filter(Boolean)[0];
  return m && seg ? { owner: m[1], name: decodeURIComponent(seg) } : { owner: "3241494-pixel", name: "Video-deutsch-" };
})();
const BRANCH = "main";
const MARKS_PATH = "data/published.json";
const API = `https://api.github.com/repos/${REPO.owner}/${REPO.name}/contents/${MARKS_PATH}`;
const GH_TREE = `https://github.com/${REPO.owner}/${REPO.name}/tree/${BRANCH}/`;

// Сети: где и что публикуем
const NETS = {
  tiktok: { name: "TikTok", upload: "https://www.tiktok.com/tiktokstudio/upload", limit: 4000 },
  youtube: { name: "YouTube", upload: "https://studio.youtube.com/", limit: 5000 },
  instagram: { name: "Instagram", upload: "https://www.instagram.com/", limit: 2200 },
};

const $ = (s, el = document) => el.querySelector(s);
const store = {
  get(k) { try { return localStorage.getItem(k); } catch { return null; } },
  set(k, v) { try { v == null ? localStorage.removeItem(k) : localStorage.setItem(k, v); } catch {} },
};

let catalog = null;          // data/videos.json
let marks = {};              // id -> {tiktok, youtube, instagram: ISO-дата}
let marksSha = null;         // sha файла отметок для записи через API
let token = store.get("gh_token");
let filter = { group: store.get("f_group") || "all", todo: new Set(), q: "" };
const tabsState = {};        // id -> активная вкладка

// ---------- утилиты ----------
const fmtDur = s => `${Math.floor(s / 60)}:${String(Math.round(s % 60)).padStart(2, "0")}`;
const fmtMB = n => (n / 1048576).toFixed(1).replace(".", ",") + " МБ";
const fmtSize = n => n > 1048576 ? fmtMB(n) : Math.max(1, Math.round(n / 1024)) + " КБ";
const fmtDate = iso => new Date(iso).toLocaleDateString("ru-RU", { day: "numeric", month: "short" });
const netsOf = v => v.vertical ? ["tiktok", "youtube", "instagram"] : ["youtube"];
const enc = s => btoa(String.fromCharCode(...new TextEncoder().encode(s)));
const dec = b => new TextDecoder().decode(Uint8Array.from(atob(b.replace(/\s/g, "")), c => c.charCodeAt(0)));
const fileUrl = p => p.split("/").map(encodeURIComponent).join("/");

function toast(text) {
  const t = document.createElement("div"); t.className = "toast"; t.textContent = text;
  document.body.append(t); setTimeout(() => t.remove(), 2600);
}
function el(tag, attrs = {}, ...kids) {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === "class") e.className = v; else if (k === "text") e.textContent = v;
    else if (k.startsWith("on")) e.addEventListener(k.slice(2), v); else if (v != null) e.setAttribute(k, v);
  }
  kids.flat().forEach(k => k != null && e.append(k));
  return e;
}
async function copyText(btn, text) {
  try { await navigator.clipboard.writeText(text); btn.textContent = "Скопировано ✓"; }
  catch {
    const pre = btn.closest(".field")?.querySelector("pre");
    if (pre) { const r = document.createRange(); r.selectNodeContents(pre); const s = getSelection(); s.removeAllRanges(); s.addRange(r); }
    btn.textContent = "Выделено, Ctrl+C";
  }
  setTimeout(() => { btn.textContent = "Копировать"; }, 1800);
}

// ---------- GitHub ----------
function setSync(state, text) {
  $("#syncDot").className = "dot" + (state === "on" ? " on" : state === "err" ? " err" : "");
  $("#syncText").textContent = text;
}
async function ghGet() {
  const r = await fetch(`${API}?ref=${BRANCH}&t=${Date.now()}`, {
    headers: { Authorization: `Bearer ${token}`, Accept: "application/vnd.github+json" }, cache: "no-store" });
  if (r.status === 401) throw new Error("Токен не подходит (401). Создай новый.");
  if (r.status === 404) throw new Error("Нет доступа к репозиторию: проверь, что токен выдан на " + REPO.name);
  if (!r.ok) throw new Error("GitHub ответил " + r.status);
  const j = await r.json();
  return { data: JSON.parse(dec(j.content)), sha: j.sha };
}
async function ghPut(data, sha, message) {
  const r = await fetch(API, {
    method: "PUT",
    headers: { Authorization: `Bearer ${token}`, Accept: "application/vnd.github+json", "Content-Type": "application/json" },
    body: JSON.stringify({ message, branch: BRANCH, sha, content: enc(JSON.stringify(data, null, 1) + "\n") }),
  });
  if (r.status === 409 || r.status === 422) return null;    // файл успели изменить: перечитаем
  if (r.status === 403) throw new Error("У токена нет права записи (Contents: Read and write).");
  if (!r.ok) throw new Error("GitHub ответил " + r.status);
  return (await r.json()).content.sha;
}

async function loadMarks() {
  if (token) {
    try { const { data, sha } = await ghGet(); marks = data; marksSha = sha; setSync("on", "Сохраняется в GitHub"); return; }
    catch (e) { setSync("err", "Ошибка GitHub"); $("#tokenNote").textContent = e.message; }
  } else setSync("", "Только просмотр");
  try { marks = await (await fetch(MARKS_PATH + "?t=" + Date.now(), { cache: "no-store" })).json(); } catch { marks = {}; }
}

// Записи идут по одной: каждая перечитывает свежий файл при конфликте
let queue = Promise.resolve();
function saveMark(id, net, on) {
  const apply = d => { d[id] = { ...(d[id] || {}) }; if (on) d[id][net] = new Date().toISOString(); else delete d[id][net]; return d; };
  apply(marks); render();
  if (!token) { toast("Чтобы сохранять, добавь токен GitHub (кнопка вверху)"); openSettings(true); return; }
  const v = catalog.videos.find(x => x.id === id);
  const msg = `${on ? "Опубликовано" : "Снята отметка"}: ${v ? v.title : id} → ${NETS[net].name}`;
  queue = queue.then(async () => {
    setSync("on", "Сохраняю…");
    for (let i = 0; i < 3; i++) {
      if (marksSha == null) { const g = await ghGet(); marksSha = g.sha; marks = apply(g.data); }
      const sha = await ghPut(marks, marksSha, msg);
      if (sha) { marksSha = sha; setSync("on", "Сохранено в GitHub"); return; }
      const g = await ghGet(); marksSha = g.sha; marks = apply(g.data);
    }
    throw new Error("Не удалось записать после трёх попыток");
  }).catch(e => { setSync("err", "Не сохранено"); toast(e.message); }).finally(render);
}

// ---------- отрисовка ----------
function summary() {
  const vs = catalog.videos, c = { tiktok: [0, 0], youtube: [0, 0], instagram: [0, 0] };
  vs.forEach(v => netsOf(v).forEach(n => { c[n][1]++; if (marks[v.id]?.[n]) c[n][0]++; }));
  $("#summary").textContent = `${vs.length} роликов · TikTok ${c.tiktok[0]}/${c.tiktok[1]} · YouTube ${c.youtube[0]}/${c.youtube[1]} · Instagram ${c.instagram[0]}/${c.instagram[1]}`;
}

function groupChips() {
  const box = $("#groupChips"); box.textContent = "";
  const mk = (id, title, n) => el("button", { type: "button", class: "chip", "aria-pressed": String(filter.group === id),
    onclick: () => { filter.group = id; store.set("f_group", id); render(); } }, title + " ", el("small", { text: String(n) }));
  box.append(mk("all", "Все", catalog.videos.length));
  catalog.groups.forEach(g => box.append(mk(g.id, g.title, catalog.videos.filter(v => v.group === g.id).length)));
}

function visible(v) {
  if (filter.group !== "all" && v.group !== filter.group) return false;
  if (filter.todo.size && ![...filter.todo].some(n => netsOf(v).includes(n) && !marks[v.id]?.[n])) return false;
  if (filter.q) {
    const hay = [v.id, v.title, v.about, v.topic, JSON.stringify(v.posts)].join(" ").toLowerCase();
    if (!filter.q.toLowerCase().split(/\s+/).every(w => hay.includes(w))) return false;
  }
  return true;
}

function field(label, text, limit) {
  const btn = el("button", { type: "button", class: "copy", text: "Копировать", onclick: e => copyText(e.currentTarget, text) });
  const n = [...text].length;
  return el("div", { class: "field" },
    el("div", { class: "field-h" }, el("span", {}, label + " ", limit ? el("small", { class: n > limit ? "over" : "", text: `${n}/${limit}` }) : null), btn),
    el("pre", { text }));
}

function panelFor(v, net) {
  const p = v.posts[net], out = [];
  if (net === "youtube") {
    out.push(field(`Название (${p.kind})`, p.title, 100), field("Описание", p.description, 5000));
  } else {
    out.push(field(net === "tiktok" ? "Подпись с тегами" : "Подпись для Reels", p.text, NETS[net].limit));
  }
  const cover = net === "youtube" ? v.covers.youtube : v.covers.tiktok;
  if (cover) out.push(el("div", { class: "covers" },
    el("a", { href: fileUrl(cover), download: "", title: "Скачать обложку" }, el("img", { src: fileUrl(cover), alt: "Обложка", loading: "lazy" }), "Скачать обложку PNG")));
  const on = !!marks[v.id]?.[net];
  out.push(el("div", { class: "panel-actions" },
    el("a", { class: "ghost", href: NETS[net].upload, target: "_blank", rel: "noopener", text: `Открыть ${NETS[net].name} ↗` }),
    el("span", { class: "note", text: on ? `Опубликовано ${fmtDate(marks[v.id][net])}` : "Ещё не опубликовано" })));
  return out;
}

function materials(v) {
  const box = [];
  v.materials.forEach(m => {
    const item = el("div", { class: "mat" });
    if (m.dir) {
      const total = m.files.reduce((s, f) => s + f.size, 0);
      item.append(el("b", { text: m.name }), " ", el("span", { class: "size", text: `${m.files.length} файлов · ${fmtSize(total)} · ` }),
        el("a", { href: GH_TREE + "materials/" + fileUrl(m.name), target: "_blank", rel: "noopener", text: "папка на GitHub ↗" }),
        el("ul", {}, m.files.map(f => el("li", {}, el("a", { href: fileUrl(f.path), target: "_blank", rel: "noopener", text: f.path.replace("materials/" + m.name, "") }), " ", el("span", { class: "size", text: fmtSize(f.size) })))));
    } else {
      const f = m.files[0];
      item.append(el("a", { href: fileUrl(f.path), target: "_blank", rel: "noopener" }, el("b", { text: m.name })), " ", el("span", { class: "size", text: fmtSize(f.size) }));
    }
    box.push(item);
  });
  return box;
}

function card(v) {
  const c = $("#cardTpl").content.firstElementChild.cloneNode(true);
  const nets = netsOf(v);
  c.id = v.id;
  if (!v.vertical) c.classList.add("wide");
  if (nets.every(n => marks[v.id]?.[n])) c.classList.add("done");
  const video = $("video", c);
  video.src = fileUrl(v.file) + "#t=0.5";
  video.preload = "metadata";
  if (v.covers.tiktok && v.vertical) video.poster = fileUrl(v.covers.tiktok);
  else if (v.covers.youtube && !v.vertical) video.poster = fileUrl(v.covers.youtube);
  $("h3", c).textContent = v.title;
  $(".meta", c).append(...[fmtDur(v.duration), v.vertical ? "9:16" : "16:9", v.level, v.topic, fmtMB(v.size)].map(t => el("span", { text: t })));
  $(".about", c).textContent = v.about;
  const dl = $(".dl", c); dl.href = fileUrl(v.file); dl.setAttribute("download", v.id + ".mp4");
  dl.textContent = `Скачать MP4 · ${fmtMB(v.size)}`;

  $(".marks", c).append(...nets.map(n => {
    const on = !!marks[v.id]?.[n];
    return el("button", { type: "button", class: "mark", "aria-pressed": String(on),
      title: on ? "Снять отметку" : "Отметить как опубликованное",
      onclick: () => saveMark(v.id, n, !on) },
      (on ? "✓ " : "") + NETS[n].name + " ", el("small", { text: on ? fmtDate(marks[v.id][n]) : "нет" }));
  }));

  const active = tabsState[v.id] && nets.includes(tabsState[v.id]) ? tabsState[v.id] : nets[0];
  $(".tabs", c).append(...nets.map(n => el("button", { type: "button", role: "tab", class: "tab", "aria-selected": String(n === active),
    onclick: () => { tabsState[v.id] = n; c.replaceWith(card(v)); } },
    NETS[n].name + (n === "youtube" ? (v.vertical ? " Shorts" : "") : n === "instagram" ? " Reels" : ""),
    marks[v.id]?.[n] ? el("span", { class: "ok", text: " ✓" }) : null)));
  $(".panel", c).append(...panelFor(v, active));
  $(".mats-in", c).append(...materials(v));
  $(".mats summary", c).textContent = `Материалы для создания (${v.materials.reduce((s, m) => s + m.files.length, 0)} файлов)`;
  return c;
}

function render() {
  if (!catalog) return;
  summary(); groupChips();
  document.querySelectorAll("[data-todo]").forEach(b => b.setAttribute("aria-pressed", String(filter.todo.has(b.dataset.todo))));
  const list = $("#list"), open = new Set([...list.querySelectorAll("details[open]")].map(d => d.closest(".card")?.id));
  list.textContent = "";
  let shown = 0;
  catalog.groups.forEach(g => {
    const vs = catalog.videos.filter(v => v.group === g.id && visible(v));
    if (!vs.length) return;
    shown += vs.length;
    list.append(el("section", { class: "group" }, el("h2", { text: g.title }), el("p", { text: g.note })));
    vs.forEach(v => { const c = card(v); if (open.has(v.id)) $("details", c).open = true; list.append(c); });
  });
  if (!shown) list.append(el("p", { class: "empty", text: "Под эти фильтры ничего не подходит." }));
  if (catalog.drafts?.length && filter.group === "all" && !filter.todo.size && !filter.q) {
    list.append(el("section", { class: "group" }, el("h2", { text: "Заготовки без видео" }),
      el("p", { text: "Тексты песен для Suno и темы будущих роликов." })),
      el("div", { class: "drafts" }, materials({ materials: catalog.drafts })));
  }
}

// ---------- настройки ----------
function openSettings(force) {
  const s = $("#settings"), show = force === true ? true : s.hidden;
  s.hidden = !show; $("#openSettings").setAttribute("aria-expanded", String(show));
  if (show) $("#token").focus();
}
$("#openSettings").addEventListener("click", () => openSettings());
$("#repoName2").textContent = REPO.name;
$("#tokenForm").addEventListener("submit", async e => {
  e.preventDefault();
  const t = $("#token").value.trim(); if (!t) return;
  token = t; store.set("gh_token", t); $("#token").value = "";
  $("#tokenNote").textContent = "Проверяю токен…";
  await loadMarks(); render();
  if (marksSha) { $("#tokenNote").textContent = "Готово: отметки читаются и сохраняются прямо в репозиторий."; openSettings(false); $("#settings").hidden = true; }
});
$("#forget").addEventListener("click", async () => {
  token = null; marksSha = null; store.set("gh_token", null);
  $("#tokenNote").textContent = "Токен удалён из этого браузера.";
  await loadMarks(); render();
});
document.querySelectorAll("[data-todo]").forEach(b => b.addEventListener("click", () => {
  filter.todo.has(b.dataset.todo) ? filter.todo.delete(b.dataset.todo) : filter.todo.add(b.dataset.todo); render();
}));
let qTimer; $("#q").addEventListener("input", e => { clearTimeout(qTimer); qTimer = setTimeout(() => { filter.q = e.target.value.trim(); render(); }, 200); });

// ---------- старт ----------
(async () => {
  try { catalog = await (await fetch("data/videos.json", { cache: "no-cache" })).json(); }
  catch { $("#summary").textContent = "Не удалось загрузить data/videos.json"; return; }
  if (filter.group !== "all" && !catalog.groups.some(g => g.id === filter.group)) filter.group = "all";
  await loadMarks();
  render();
  if (location.hash.length > 1) document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView();
})();
