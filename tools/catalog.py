# Каталог всех роликов: тексты для соцсетей и список материалов.
# Единый источник для data/videos.json (собирает tools/build.py).
# Новый ролик = новая запись в VIDEOS (+ при необходимости новая группа в GROUPS).

GROUPS = [
    {"id": "start", "title": "Первые ролики", "note": "Сюжетный ролик и первый грамматический разбор, 1080×1920."},
    {"id": "aspekte", "title": "Грамматика по Aspekte neu B1+",
     "note": "Серия по учебнику Aspekte neu B1 plus (Teil 1), по порядку глав. В конце каждого ролика тест с таймером."},
    {"id": "aspekte_uk", "title": "Aspekte с украинскими субтитрами",
     "note": "Ролики 1–6 серии Aspekte: немецкий голос и субтитры, под ними украинский перевод."},
    {"id": "artikel", "title": "Серия der · die · das",
     "note": "5 песен про артикли по окончаниям: вертикаль для TikTok/Shorts/Reels и 16:9 для YouTube."},
    {"id": "songs", "title": "Песни для изучения",
     "note": "Клипы на учебные песни Suno: караоке, немецкий текст и украинский перевод."},
]

# Общие хвосты описаний
ASPEKTE_DE = "Aus der Serie «Grammatik mit Aspekte neu B1+». Am Ende: Test mit Timer – wie viele hast du richtig? Schreib dein Ergebnis in die Kommentare!"
ASPEKTE_RU = "Серия «Грамматика по Aspekte neu B1+». В конце тест с таймером: напиши в комментариях свой результат!"
ASPEKTE_UK = "Серія «Граматика за Aspekte neu B1+». Німецька озвучка, німецькі субтитри та переклад українською. Наприкінці тест із таймером!"
UK_TAGS = "#німецькамова #вивчаюнімецьку #deutschlernen #grammatik #deutschb1 #learngerman"

# Ролики. Поля:
#   id       — имя файла без .mp4 (оно же ключ отметок в data/published.json)
#   src      — путь к mp4 в общих файлах проекта (tiktok-german/...)
#   group, title (как в апке), level, topic, about (по-русски, что в ролике)
#   tiktok   — название + теги одной строкой (подпись к посту)
#   yt_title — название YouTube (≤100 символов, теги можно внутри)
#   yt_desc  — описание YouTube
#   cover    — обложки {tiktok, youtube} (пути в общих файлах), если есть
#   materials — файлы и папки для создания (пути в общих файлах)
VIDEOS = []


def add(**v):
    VIDEOS.append(v)


# ---------- Первые ролики ----------
add(id="bruno_nur_deutsch", src="first-video/bruno_nur_deutsch.mp4", group="start",
    title="Bruno versteht nur Deutsch", level="A2–B1", topic="императив, Sie",
    about="Собака «понимает только немецкий»: пять команд-императивов, вежливая форма с Sie и слово das Leckerli.",
    tiktok="Versteht mein Hund nur Deutsch? 🐕🇩🇪 Sitz, Platz, Aus! #deutschlernen #learngerman #deutsch #hund #germanforbeginners #немецкийязык",
    yt_title="Versteht mein Hund nur Deutsch? 🐕 Sitz, Platz, Aus! #deutschlernen #shorts",
    yt_desc="Sitz! Platz! Komm her! Aus! Bruno versteht nur Deutsch – oder? Fünf Imperative für Hunde und die höfliche Form mit Sie: «Könnten Sie sich bitte setzen?»\n"
            "Собака понимает только немецкий? Пять команд в повелительном наклонении, вежливая форма с Sie и слово das Leckerli. Уровень A2–B1.\n\n"
            "Welches Wort soll Bruno als Nächstes lernen? Schreib es in die Kommentare!\n\n"
            "#deutschlernen #learngerman #imperativ #hund #deutscha2 #немецкийязык",
    materials=["first-video/README.md", "first-video/subtitles_de.srt", "first-video/project", "first-video/audio"])

add(id="plural_deutsch", src="video-plural/plural_deutsch.mp4", group="start",
    title="Plural im Deutschen", level="A2–B1", topic="6 правил + тест",
    about="Шесть правил множественного числа (-e, умлаут, -er, -n/-en, -s, без окончания) и тест из пяти слов с таймером.",
    tiktok="Plural im Deutschen: 6 Regeln + Test 🇩🇪 Wie viele hast du richtig? #deutschlernen #learngerman #grammatik #deutscha2 #germangrammar #немецкийязык",
    yt_title="Plural im Deutschen: 6 Regeln + Test 🇩🇪 #deutschlernen #grammatik #shorts",
    yt_desc="Tisch – Tische, Buch – Bücher, Auto – Autos: Ist der Plural im Deutschen chaotisch? Nein! Sechs Regeln: -e, Umlaut + -e, -er, -n/-en, -s und ohne Endung. Am Ende: Test mit 5 Wörtern.\n"
            "Множественное число в немецком: 6 правил и тест с таймером. Уровень A2–B1.\n\n"
            "#deutschlernen #learngerman #plural #grammatik #deutscha2 #немецкийязык",
    materials=["video-plural/README.md", "video-plural/subtitles_de.srt", "video-plural/project", "video-plural/audio"])

# ---------- Aspekte ----------
ASPEKTE = [
    ("v1_perfekt", "1. Perfekt oder Präteritum?", "Kapitel 1", "4 правила + тест",
     "Устная речь и письма в Perfekt, газеты и романы в Präteritum, war/hatte/wollte почти всегда в Präteritum, образование Präteritum.",
     "Perfekt oder Präteritum? 🤔 So sagst du es richtig + Test",
     "#deutschlernen #grammatik #perfekt #präteritum #deutschb1 #немецкийязык",
     "Wann sagt man «ich habe gemacht» und wann «ich machte»? Mündlich und in Mails: Perfekt. Zeitung und Roman: Präteritum. Und war, hatte, wollte fast immer im Präteritum.",
     "Коли Perfekt, а коли Präteritum: усне мовлення, газети, war/hatte/wollte."),
    ("v2_partizip", "2. Partizip II", "Kapitel 1", "5 типов + тест",
     "ge-…-t и ge-…-en, отделяемые (aufgehört), неотделяемые и -ieren без ge, смешанные глаголы (gekannt, gebracht, gedacht, gewusst).",
     "Partizip II: ge- oder kein ge-? 🤯 5 Regeln + Test",
     "#deutschlernen #grammatik #partizip #deutscha2 #learngerman #немецкийязык",
     "gemacht, gefahren, aufgehört, verstanden, studiert: fünf Regeln für das Partizip II – mit ge-, ohne ge- und die gemischten Verben gekannt, gebracht, gedacht, gewusst.",
     "Partizip II: з ge- і без ge-, відокремлювані та змішані дієслова."),
    ("v3_plusquam", "3. Plusquamperfekt + nachdem", "Kapitel 1", "примеры + тест",
     "«Прошлое в прошлом»: история про Matthias из учебника, hatte/war + Partizip II, предложения с nachdem и тест «Was ist vorher passiert?».",
     "Plusquamperfekt in 90 Sekunden ⏪ Mit nachdem + Test",
     "#deutschlernen #grammatik #plusquamperfekt #deutschb1 #learngerman #немецкийязык",
     "Die Vergangenheit in der Vergangenheit: hatte/war + Partizip II und Sätze mit nachdem. Was ist vorher passiert?",
     "Plusquamperfekt: минуле в минулому, hatte/war + Partizip II і речення з nachdem."),
    ("v4_kasus", "4. Welcher Kasus?", "Kapitel 1", "6 моделей + тест",
     "Глагол определяет падеж: Nominativ, Akkusativ, Dativ, Dativ + Akkusativ и глаголы с предлогом. Падежи выделены цветом.",
     "Dativ oder Akkusativ? Das Verb entscheidet! ⚖️ + Test",
     "#deutschlernen #dativ #akkusativ #grammatik #deutschb1 #немецкийязык",
     "Das Verb entscheidet den Kasus: Nominativ, Akkusativ, Dativ, Dativ + Akkusativ und Verben mit Präposition – mit Farben erklärt.",
     "Дієслово визначає відмінок: Nominativ, Akkusativ, Dativ і дієслова з прийменником."),
    ("v5_reihenfolge", "5. Wer kommt zuerst?", "Kapitel 1", "3 правила + тест",
     "Порядок объектов: два существительных (сначала Dativ), местоимение + существительное (местоимение впереди), два местоимения (сначала Akkusativ).",
     "Ich gebe ihn ihm 🤯 Dativ oder Akkusativ zuerst? + Test",
     "#deutschlernen #grammatik #dativ #akkusativ #deutschb1 #немецкийязык",
     "Ich gebe dem Mann den Ball. Ich gebe ihn ihm. Drei Regeln für die Reihenfolge von Dativ und Akkusativ im Satz.",
     "Порядок додатків: спочатку Dativ чи Akkusativ? Три правила."),
    ("v6_praepositionen", "6. Verben mit Präpositionen", "Kapitel 1", "5 правил + тест из 12 фраз",
     "warten auf, sich freuen über, träumen von: предлоги с Akkusativ и Dativ, вопросы worauf? / auf wen?, ответы darauf / davor и много примеров.",
     "Warten AUF, träumen VON 🤯 Verben mit Präpositionen + Test (12 Sätze)",
     "#deutschlernen #grammatik #präpositionen #deutschb1 #learngerman #немецкийязык",
     "warten auf, sich freuen über, träumen von: Verben mit Präpositionen, Akkusativ oder Dativ, Fragen mit worauf? und auf wen?, Antworten mit darauf und davon. Test mit 12 Sätzen.",
     "Дієслова з прийменниками: warten auf, sich freuen über, worauf? / darauf."),
    ("v7_trennbar", "7. Trennbar oder untrennbar?", "Kapitel 2", "5 правил + тест из 12 фраз",
     "aufstehen и verstehen: отделяемые и неотделяемые приставки, ударение, Partizip II, и когда отделяемый глагол не разделяется (Nebensatz, модальный глагол, zu).",
     "Aufstehen oder verstehen? ✂️ Trennbare Verben einfach erklärt + Test",
     "#deutschlernen #grammatik #trennbareverben #deutscha2 #learngerman #немецкийязык",
     "aufstehen oder verstehen? Trennbare und untrennbare Präfixe, Betonung, Partizip II und wann das Verb nicht getrennt wird: Nebensatz, Modalverb, zu. Test mit 12 Sätzen.", None),
    ("v8_ndeklination", "8. n-Deklination", "Kapitel 2", "5 правил + тест из 12 фраз",
     "der Student, den Studenten: какие слова относятся к n-Deklination (-e, -ist, -ent, -ant…), окончание во всех падежах, des Namens, Herrn Müller и типичные ошибки.",
     "Den Student oder den StudentEN? 🎓 n-Deklination + Test",
     "#deutschlernen #grammatik #ndeklination #deutschb1 #learngerman #немецкийязык",
     "der Student, den Studenten, dem Studenten: Welche Nomen gehören zur n-Deklination (-e, -ist, -ent, -ant), des Namens, Herrn Müller und typische Fehler. Test mit 12 Sätzen.", None),
    ("v9_adjektiv_der", "9. Adjektive nach der, die, das", "Kapitel 3", "4 правила + таблица + тест из 12 фраз",
     "Склонение прилагательных после определённого артикля: всего два окончания -e и -en, полная таблица, то же после dieser/jeder/welcher и примеры из жизни.",
     "Der neue oder den neuen? 🤔 Adjektivendungen nach der, die, das + Test",
     "#deutschlernen #grammatik #adjektive #deutschb1 #germangrammar #немецкийязык",
     "der neue Film, den neuen Film: Nach der, die, das gibt es nur zwei Endungen, -e und -en. Mit Tabelle, dieser/jeder/welcher und Beispielen aus dem Alltag. Test mit 12 Sätzen.", None),
    ("v10_adjektiv_ein", "10. Adjektive nach ein und ohne Artikel", "Kapitel 3", "4 правила + таблица + тест из 12 фраз",
     "ein neuer Film, ein neues Auto: окончания после ein/kein/mein, таблица, прилагательные без артикля (heißer Kaffee, mit kaltem Wasser) и все три типа рядом.",
     "Ein neuer, ein neues, eine neue 😵 Adjektive nach ein + ohne Artikel + Test",
     "#deutschlernen #grammatik #adjektive #deutscha2 #learngerman #немецкийязык",
     "ein neuer Film, ein neues Auto, heißer Kaffee, mit kaltem Wasser: Adjektivendungen nach ein/kein/mein und ohne Artikel, mit Tabelle und allen drei Typen im Vergleich. Test mit 12 Sätzen.", None),
]

for vid, title, kap, topic, about, tt, tags, de, uk in ASPEKTE:
    base = f"aspekte-b1plus/{vid}"
    mats = [f"{base}/subtitles_de.srt", f"{base}/project", "aspekte-b1plus/SCENARII_1-5.md", "aspekte-b1plus/engine"]
    add(id=vid, src=f"{base}/{vid}.mp4", group="aspekte", title=title, level=kap, topic=topic, about=about,
        tiktok=f"{tt} {tags}",
        yt_title=f"{tt} #shorts",
        yt_desc=f"{de}\n{about}\n\n{ASPEKTE_DE}\n{ASPEKTE_RU}\n\n{tags}",
        materials=mats)
    if uk:
        add(id=f"{vid}_uk", src=f"{base}/{vid}_uk.mp4", group="aspekte_uk", title=title, level=kap, topic="🇺🇦 субтитры",
            about="Тот же ролик: немецкая озвучка и немецкие субтитры, под ними перевод каждой фразы на украинский.",
            tiktok=f"{tt} 🇺🇦 {UK_TAGS}",
            yt_title=f"{tt} 🇺🇦 #shorts",
            yt_desc=f"{de}\n{uk}\n\n{ASPEKTE_UK}\n\n{UK_TAGS}",
            materials=[f"{base}/subtitles_uk.srt", f"{base}/subtitles_de.srt", f"{base}/project_uk",
                       "aspekte-b1plus/engine/add_uk_subs.py", "aspekte-b1plus/engine/uk_translations.py",
                       "aspekte-b1plus/engine/render_uk.sh"])

# ---------- Серия der · die · das (тексты берутся из meta.md каждого эпизода) ----------
ARTIKEL = [
    ("ep1_die_ung", "1. Immer die! -ung, -heit, -keit, -schaft"),
    ("ep2_der", "2. Immer der! -ling, -ismus, -ist, -or…"),
    ("ep3_das_chen", "3. Immer das! -chen, -um, -ment, -ma, -o"),
    ("ep4_die_ion", "4. Immer die! -ion, -tät, -ik, -ie, -ei"),
    ("ep5_das_ge", "5. Immer das! Ge-, -nis, -tum, -ett"),
]
for ep, title in ARTIKEL:
    base = f"songs/artikel_serie/{ep}"
    mats = [f"{base}/meta.md", f"{base}/text.md", f"{base}/lines.json", f"{base}/beats.json", f"{base}/song.wav",
            "songs/artikel_serie/engine"]
    for fmt in ("v", "h"):
        vid = ep if fmt == "v" else f"{ep}_youtube"
        add(id=vid, src=f"{base}/{vid}.mp4", group="artikel", title=title, level="A1–B1",
            topic="🎵 песня" + (" · YouTube 16:9" if fmt == "h" else ""),
            about="Песня про артикли по окончаниям: слова с эмодзи, артикль цветом (der синий, die красный, das зелёный), украинский перевод.",
            meta_md=f"{base}/meta.md",
            cover={"tiktok": f"{base}/{ep}_cover_tiktok.png", "youtube": f"{base}/{ep}_cover_youtube.png"},
            materials=mats)

# ---------- Песни ----------
SONG_UK = "Пісня з перекладом українською: співай разом і запам'ятовуй."
add(id="ich_mache_weiter", src="songs/ich_mache_weiter/ich_mache_weiter.mp4", group="songs",
    title="Ich mache weiter", level="A2–B1", topic="🎵 отделяемые глаголы",
    about="Около 60 отделяемых глаголов в трёх формах: Infinitiv, Präsens, Perfekt. Префикс оранжевый, ge зелёный, bin/habe отмечены как sein/haben.",
    tiktok="Ich stehe auf, ich bin aufgestanden 🎵 Trennbare Verben als Song #deutschlernen #trennbareverben #germansong #німецькамова #вивчаюнімецьку #learngerman",
    yt_title="Ich stehe auf, ich bin aufgestanden 🎵 Trennbare Verben als Song #deutschlernen #shorts",
    yt_desc="Ich mache weiter: ein Song mit rund 60 trennbaren Verben – Infinitiv, Präsens und Perfekt. aufstehen, ich stehe auf, ich bin aufgestanden.\n"
            "Відокремлювані дієслова в трьох формах. " + SONG_UK + "\n\n"
            "#deutschlernen #trennbareverben #germansong #німецькамова #вивчаюнімецьку #learngerman",
    cover={"tiktok": "songs/ich_mache_weiter/ich_mache_weiter_cover_tiktok.png"},
    materials=["songs/ich_mache_weiter/subtitles_de.srt", "songs/ich_mache_weiter/subtitles_de_uk.srt",
               "songs/ich_mache_weiter/project", "songs/make_covers.py"])
add(id="ich_mache_weiter_youtube", src="songs/ich_mache_weiter/ich_mache_weiter_youtube.mp4", group="songs",
    title="Ich mache weiter · YouTube 16:9", level="A2–B1", topic="🎵 отделяемые глаголы",
    about="Горизонтальная версия: карточка слева, список глаголов справа.",
    yt_title="Trennbare Verben als Song 🎵 Ich mache weiter | A2–B1 #deutschlernen #trennbareverben #germansong",
    yt_desc="Ich mache weiter: ein Lernsong mit rund 60 trennbaren Verben. Zu jedem Verb: Infinitiv, Präsens und Perfekt (aufstehen – ich stehe auf – ich bin aufgestanden). Präfix in Orange, ge- in Grün, sein/haben markiert.\n"
            "Пісня про відокремлювані дієслова німецької мови: інфінітив, теперішній час і Perfekt. " + SONG_UK + "\n\n"
            "#deutschlernen #trennbareverben #germansong #learngerman #німецькамова #вивчаюнімецьку #deutschmitmusik",
    cover={"youtube": "songs/ich_mache_weiter/ich_mache_weiter_cover_youtube.png"},
    materials=["songs/ich_mache_weiter/subtitles_de_uk.srt", "songs/ich_mache_weiter/project_youtube",
               "songs/ich_mache_weiter/project", "songs/make_covers.py"])

add(id="drei_formen", src="songs/drei_formen/drei_formen.mp4", group="songs",
    title="Drei Formen, sing sie laut", level="A2–B1", topic="🎵 сильные глаголы",
    about="28 сильных глаголов в трёх формах: Infinitiv, Präteritum, Partizip II, и к каждому пример в Perfekt с отметкой sein или haben.",
    tiktok="Gehen, ging, gegangen 🎵 Starke Verben als Song – sing mit! #deutschlernen #starkeverben #germansong #німецькамова #вивчаюнімецьку #learngerman",
    yt_title="Gehen, ging, gegangen 🎵 Starke Verben als Song – sing mit! #deutschlernen #shorts",
    yt_desc="Drei Formen, sing sie laut: 28 starke Verben mit Infinitiv, Präteritum und Partizip II, dazu ein Beispiel im Perfekt mit sein oder haben.\n"
            "Сильні дієслова в трьох формах. " + SONG_UK + "\n\n"
            "#deutschlernen #starkeverben #germansong #німецькамова #вивчаюнімецьку #learngerman",
    cover={"tiktok": "songs/drei_formen/drei_formen_cover_tiktok.png"},
    materials=["songs/drei_formen/subtitles_de.srt", "songs/drei_formen/subtitles_de_uk.srt",
               "songs/drei_formen/project", "songs/make_covers.py"])
add(id="drei_formen_youtube", src="songs/drei_formen/drei_formen_youtube.mp4", group="songs",
    title="Drei Formen · YouTube 16:9", level="A2–B1", topic="🎵 сильные глаголы",
    about="Горизонтальная версия: карточка слева, список глаголов справа.",
    yt_title="Starke Verben als Song 🎵 gehen, ging, gegangen | A2–B1 #deutschlernen #starkeverben #germansong",
    yt_desc="Drei Formen, sing sie laut: ein Lernsong mit 28 starken Verben – Infinitiv, Präteritum, Partizip II (gehen – ging – gegangen) und ein Beispielsatz im Perfekt mit sein oder haben. Die drei Formen in drei Farben.\n"
            "Пісня про сильні дієслова німецької мови: три форми й приклад у Perfekt. " + SONG_UK + "\n\n"
            "#deutschlernen #starkeverben #germansong #learngerman #німецькамова #вивчаюнімецьку #deutschmitmusik",
    cover={"youtube": "songs/drei_formen/drei_formen_cover_youtube.png"},
    materials=["songs/drei_formen/subtitles_de_uk.srt", "songs/drei_formen/project_youtube",
               "songs/drei_formen/project", "songs/make_covers.py"])

add(id="hallo_abc", src="songs/abc_lied/hallo_abc.mp4", group="songs",
    title="Hallo, ABC! (для детей)", level="A1 · дети", topic="🎵 алфавит",
    about="Анимированный клип про немецкий алфавит: плитка буквы с подсказкой «sprich: Be», персонаж и слово с артиклем цветом; в припеве загораются все 26 букв.",
    tiktok="Das ABC für Kinder 🎵 Hallo, ABC! Sing mit! #deutschlernen #alphabet #kinderlied #deutschfürkinder #німецькадлядітей #вивчаюнімецьку",
    yt_title="Das ABC für Kinder 🎵 Hallo, ABC! Sing mit! #kinderlied #alphabet #shorts",
    yt_desc="Hallo, ABC! Ein Kinderlied über das deutsche Alphabet: zu jedem Buchstaben ein Bild und ein Wort mit Artikel. Am Ende: Ä, Ö, Ü und ß.\n"
            "Дитяча пісня про німецький алфавіт: кожна літера з картинкою і словом. " + SONG_UK + "\n\n"
            "#deutschlernen #alphabet #kinderlied #deutschfürkinder #німецькадлядітей #вивчаюнімецьку",
    cover={"tiktok": "songs/abc_lied/hallo_abc_cover_tiktok.png"},
    materials=["songs/abc_lied/text.md", "songs/abc_lied/subtitles_de_uk.srt", "songs/abc_lied/project"])
add(id="hallo_abc_youtube", src="songs/abc_lied/hallo_abc_youtube.mp4", group="songs",
    title="Hallo, ABC! · YouTube 16:9", level="A1 · дети", topic="🎵 алфавит",
    about="Горизонтальная версия детского клипа про алфавит.",
    yt_title="Hallo, ABC! 🎵 Das deutsche Alphabet für Kinder | Kinderlied #kinderlied #alphabet #deutschlernen",
    yt_desc="Hallo, ABC! Ein fröhliches Kinderlied über das deutsche Alphabet. Zu jedem Buchstaben: die Aussprache (sprich: Be), ein gezeichnetes Bild und ein Wort mit Artikel – der in Blau, die in Rot, das in Grün. Im Refrain leuchten alle 26 Buchstaben, Ä, Ö, Ü und ß bekommen eine eigene Strophe.\n"
            "Дитяча пісня про німецький алфавіт з картинками та перекладом українською. Співайте разом!\n\n"
            "#kinderlied #alphabet #deutschlernen #deutschfürkinder #abc #німецькадлядітей #вивчаюнімецьку",
    cover={"youtube": "songs/abc_lied/hallo_abc_cover_youtube.png"},
    materials=["songs/abc_lied/text.md", "songs/abc_lied/project_youtube", "songs/abc_lied/project"])

# Заготовки без видео (тексты песен для Suno)
DRAFTS = ["songs/grammatik_hits", "songs/next_hit/topics.html"]
