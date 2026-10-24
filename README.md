# Видео Deutsch

Личная апка для публикации обучающих видео по немецкому: ролики, названия, теги и описания для TikTok, YouTube и Instagram, кнопки скачивания и копирования, отметки «опубликовано».

- `index.html`, `app.js`, `style.css`: сама апка (GitHub Pages).
- `data/videos.json`: каталог (собирается `tools/build.py`).
- `data/published.json`: отметки «опубликовано», апка пишет их сюда через GitHub API.
- `videos/`: mp4. `materials/`: сценарии, тексты песен, проекты видео, субтитры, обложки.
- Новый ролик: добавить запись в `tools/catalog.py`, запустить `python3 tools/build.py`, закоммитить.
