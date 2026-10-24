#!/usr/bin/env python3
# Сборка репозитория из общих файлов проекта:
#   videos/<группа>/<id>.mp4, materials/<путь как в tiktok-german>/..., data/videos.json
# Запуск: python3 tools/build.py [/mnt/project-files/tiktok-german]
# data/published.json (отметки) не трогаем, если он уже есть: его ведёт апка.
import json, os, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(sys.argv[1] if len(sys.argv) > 1 else "/mnt/project-files/tiktok-german")
sys.path.insert(0, str(ROOT / "tools"))
import catalog  # noqa: E402

SKIP_DIRS = {"__pycache__", ".hyperframes", "node_modules"}


def probe(path):
    # Длительность и размер кадра через ffprobe
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height:format=duration", "-of", "json", str(path)],
                         capture_output=True, text=True, check=True).stdout
    d = json.loads(out)
    s = d["streams"][0]
    return float(d["format"]["duration"]), s["width"], s["height"]


def copy_file(rel):
    # Копирует один файл материалов; wav сжимаем в mp3, чтобы репозиторий не раздувался
    src = SRC / rel
    if src.suffix == ".wav":
        dst = ROOT / "materials" / Path(rel).with_suffix(".mp3")
        if not dst.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-b:a", "192k", str(dst)], check=True)
    else:
        dst = ROOT / "materials" / rel
        if not dst.exists() or dst.stat().st_size != src.stat().st_size:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
    return {"path": str(dst.relative_to(ROOT)), "size": dst.stat().st_size}


def copy_material(rel):
    src = SRC / rel
    if src.is_dir():
        files = []
        for p in sorted(src.rglob("*")):
            if p.is_file() and not (set(p.relative_to(src).parts) & SKIP_DIRS) and p.suffix != ".mp4":
                files.append(copy_file(str(p.relative_to(SRC))))
        return {"name": rel + "/", "dir": True, "files": files}
    f = copy_file(rel)
    return {"name": Path(f["path"]).name, "dir": False, "files": [f]}


def meta_blocks(rel):
    # meta.md эпизода серии: 1 TikTok, 2 Shorts, 3 YouTube 16:9, 4 описание
    return re.findall(r"```\n(.*?)\n```", (SRC / rel).read_text(), re.S)


def split_tags(text):
    i = text.find(" #")
    return (text[:i].strip(), text[i:].strip()) if i > 0 else (text, "")


def main():
    videos = []
    for v in catalog.VIDEOS:
        src = SRC / v["src"]
        dur, w, h = probe(src)
        vertical = h > w
        dst = ROOT / "videos" / v["group"] / f"{v['id']}.mp4"
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.exists() or dst.stat().st_size != src.stat().st_size:
            shutil.copy2(src, dst)

        if "meta_md" in v:
            tt, shorts, yt, desc = meta_blocks(v["meta_md"])[:4]
            v = {**v, "tiktok": tt if vertical else None, "yt_title": shorts if vertical else yt, "yt_desc": desc}

        posts = {}
        if vertical and v.get("tiktok"):
            title, tags = split_tags(v["tiktok"])
            posts["tiktok"] = {"text": v["tiktok"]}
            posts["instagram"] = {"text": f"{title}\n\n{v['about']}\n\n{tags}"}
        posts["youtube"] = {"title": v["yt_title"], "description": v["yt_desc"],
                            "kind": "Shorts" if vertical else "Видео 16:9"}

        covers = {k: copy_file(p)["path"] for k, p in (v.get("cover") or {}).items()}
        materials = [copy_material(m) for m in v.get("materials", [])]

        videos.append({
            "id": v["id"], "group": v["group"], "title": v["title"], "level": v["level"], "topic": v["topic"],
            "about": v["about"], "file": str(dst.relative_to(ROOT)), "size": dst.stat().st_size,
            "duration": round(dur, 1), "width": w, "height": h, "vertical": vertical,
            "covers": covers, "posts": posts, "materials": materials,
        })
        print(f"{v['id']:28} {dur:6.1f}s {w}x{h}")

    drafts = [copy_material(d) for d in catalog.DRAFTS]
    data = {"groups": catalog.GROUPS, "videos": videos, "drafts": drafts}
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / "videos.json").write_text(json.dumps(data, ensure_ascii=False, indent=1))
    pub = ROOT / "data" / "published.json"
    if not pub.exists():
        pub.write_text(json.dumps({v["id"]: {} for v in videos}, ensure_ascii=False, indent=1))
    print(len(videos), "videos")


if __name__ == "__main__":
    main()
