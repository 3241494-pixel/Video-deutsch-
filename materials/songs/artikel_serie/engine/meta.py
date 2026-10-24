# Названия с тегами (TikTok и YouTube) и описание YouTube для каждой серии -> ../EP_ID/meta.md
# Таймкоды берутся из ../EP_ID/lines.json, если выравнивание уже сделано
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import series as S

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UK_ART = {"der": "чоловічий рід", "die": "жіночий рід", "das": "середній рід"}

def mmss(t): return f"{int(t // 60)}:{int(t % 60):02d}"

def build(e):
    art = e["art"]; ends = [b["show"] for b in e["blocks"]]
    ends_s = " ".join(ends)
    tt = f"Immer {art.upper()}! {ends_s} 🎵 Folge {e['no']}/5 #deutschlernen #learngerman #artikel #derdiedas #німецькамова #deutschmitmusik"
    yt = f"Immer {art.upper()}! {', '.join(ends)} | Artikel-Song {e['no']}/5 #deutschlernen #derdiedas #shorts"
    if len(yt) > 100:
        yt = f"Immer {art.upper()}! {' '.join(ends)} | Artikel {e['no']}/5 #deutschlernen #derdiedas"
    yt_h = yt.replace(" #shorts", "")
    # описание YouTube: ключевые слова в первых строках, список слов с переводом, таймкоды, хэштеги
    lines = []
    lines.append(f"Der, die oder das? Hör aufs Ende! In diesem Lied lernst du: Nomen mit {', '.join(ends)} sind {'immer' if all(b['a'].startswith('Immer') for b in e['blocks']) else 'fast immer'} {art.upper()}.")
    lines.append(f"Німецькі артиклі легко: слова із закінченнями {', '.join(ends)} — це {art} ({UK_ART[art]}). Пісня з перекладом українською, співай разом і запам'ятовуй.")
    lines.append("")
    lp = f"{ROOT}/{e['id']}/lines.json"
    if os.path.exists(lp):
        L = json.load(open(lp))
        lines.append("Таймкоди:")
        lines.append("0:00 Intro: der, die, das")
        for i, b in enumerate(e["blocks"]):
            lines.append(f"{mmss(L[2 + 5 * i]['start'])} {b['show']} — {b['a']}")
        lines.append(f"{mmss(L[2 + 5 * len(e['blocks'])]['start'])} Wiederholung + Ausnahmen")
        lines.append("")
    lines.append("Wörter im Lied / Слова в пісні:")
    for b in e["blocks"]:
        lines.append(f"{b['show']}: " + ", ".join(f"{art} {w} ({uk})" for w, _, uk in b["words"]))
    if e["exceptions"]:
        lines.append("")
        lines.append("Ausnahmen / Винятки: " + ", ".join(e["exceptions"]))
    lines.append("")
    lines.append("Serie «Der, die, das mit Musik»: 5 Lieder über Artikel und Endungen (A1–B1). Abonniere, damit du keine Folge verpasst!")
    lines.append("")
    lines.append(f"#deutschlernen #derdiedas #artikel #germangrammar #learngerman #німецькамова #німецька #deutschmitmusik #{art}")
    return tt, yt, yt_h, "\n".join(lines)

for e in S.EPISODES:
    tt, yt, yt_h, desc = build(e)
    d = f"{ROOT}/{e['id']}"; os.makedirs(d, exist_ok=True)
    open(f"{d}/meta.md", "w").write(f"# {e['no']}. {e['title']}\n\n## TikTok: название с тегами\n```\n{tt}\n```\n\n## YouTube Shorts (вертикаль): название с тегами ({len(yt)} симв.)\n```\n{yt}\n```\n\n## YouTube (16:9): название с тегами ({len(yt_h)} симв.)\n```\n{yt_h}\n```\n\n## YouTube: описание\n```\n{desc}\n```\n")
    print(e["id"], len(yt), len(yt_h))
