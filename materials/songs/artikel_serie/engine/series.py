# Данные серии «Артикли по окончаниям»: единый источник для текстов Suno, клипов, обложек и описаний
# Каждый блок: окончание (как поётся), как показать на экране, слова (без артикля), эмодзи-иконка, перевод (uk)

STYLE = ("german educational chant, rhythmic spoken-sung male baritone vocal, chill lo-fi pop beat, "
         "soft piano and light percussion, call and response, slow and very clear German pronunciation, "
         "short pause after each word, 88 bpm")

INTRO = ["Der, die, das — wer weiß das?", "Hör aufs Ende, dann weißt du das!"]

EPISODES = [
    {"id": "ep1_die_ung", "no": 1, "art": "die", "title": "Immer die! Teil 1",
     "blocks": [
        {"sing": "ung", "show": "-ung", "q": "Endet ein Wort auf", "a": "Immer die!",
         "words": [("Wohnung","🏠","квартира"),("Zeitung","📰","газета"),("Meinung","💬","думка"),
                   ("Lösung","💡","рішення"),("Prüfung","📝","іспит"),("Erfahrung","🧗","досвід")]},
        {"sing": "heit", "show": "-heit", "q": "Endet ein Wort auf", "a": "Immer die!",
         "words": [("Freiheit","🕊️","свобода"),("Gesundheit","❤️","здоров'я"),("Wahrheit","✅","правда"),
                   ("Kindheit","🧸","дитинство"),("Krankheit","🤒","хвороба"),("Gelegenheit","🚪","нагода")]},
        {"sing": "keit", "show": "-keit", "q": "Endet ein Wort auf", "a": "Immer die!",
         "words": [("Möglichkeit","🔑","можливість"),("Schwierigkeit","🧩","труднощі"),("Geschwindigkeit","🚄","швидкість"),
                   ("Süßigkeit","🍬","солодощі"),("Pünktlichkeit","⏰","пунктуальність"),("Sehenswürdigkeit","🏰","пам'ятка")]},
        {"sing": "schaft", "show": "-schaft", "q": "Endet ein Wort auf", "a": "Immer die!",
         "words": [("Freundschaft","🤝","дружба"),("Mannschaft","⚽","команда"),("Landschaft","🏞️","краєвид"),
                   ("Wirtschaft","📈","економіка"),("Gesellschaft","👥","суспільство"),("Wissenschaft","🔬","наука")]},
     ]},
    {"id": "ep2_der", "no": 2, "art": "der", "title": "Immer der!",
     "blocks": [
        {"sing": "ling", "show": "-ling", "q": "Endet ein Wort auf", "a": "Immer der!",
         "words": [("Frühling","🌷","весна"),("Schmetterling","🦋","метелик"),("Liebling","😍","улюбленець"),
                   ("Zwilling","👯","близнюк"),("Lehrling","🧑‍🔧","учень"),("Feigling","🙈","боягуз")]},
        {"sing": "ismus", "show": "-ismus", "q": "Endet ein Wort auf", "a": "Immer der!",
         "words": [("Tourismus","🧳","туризм"),("Optimismus","🌞","оптимізм"),("Egoismus","🪞","егоїзм"),
                   ("Journalismus","🗞️","журналістика"),("Realismus","🖼️","реалізм"),("Kapitalismus","💰","капіталізм")]},
        {"sing": "ist", "show": "-ist", "q": "Endet ein Wort auf", "a": "Immer der!",
         "words": [("Tourist","📸","турист"),("Polizist","👮","поліцейський"),("Journalist","🎤","журналіст"),
                   ("Pianist","🎹","піаніст"),("Optimist","😄","оптиміст"),("Spezialist","🧠","спеціаліст")]},
        {"sing": "or", "show": "-or", "q": "Endet ein Wort auf", "a": "Fast immer der!",
         "words": [("Motor","⚙️","двигун"),("Autor","✍️","автор"),("Doktor","🩺","лікар"),
                   ("Professor","🎓","професор"),("Direktor","💼","директор"),("Traktor","🚜","трактор")]},
        {"sing": "ig“ oder „ich", "show": "-ig / -ich", "q": "Endet ein Wort auf", "a": "Immer der!",
         "words": [("Honig","🍯","мед"),("König","👑","король"),("Käfig","🐦","клітка"),
                   ("Essig","🧴","оцет"),("Teppich","🧶","килим"),("Pfirsich","🍑","персик")]},
        {"sing": "ent“ oder „ant", "show": "-ent / -ant", "q": "Endet ein Wort auf", "a": "Fast immer der!",
         "words": [("Student","🎒","студент"),("Präsident","🏛️","президент"),("Patient","🛏️","пацієнт"),
                   ("Kontinent","🌍","континент"),("Elefant","🐘","слон"),("Praktikant","🧑‍💻","практикант")]},
     ], "exceptions": ["das Labor", "das Tor", "das Talent", "das Restaurant", "das Prozent"]},
    {"id": "ep3_das_chen", "no": 3, "art": "das", "title": "Immer das! Teil 1",
     "blocks": [
        {"sing": "chen“ oder „lein", "show": "-chen / -lein", "q": "Endet ein Wort auf", "a": "Immer das!",
         "words": [("Mädchen","👧","дівчинка"),("Brötchen","🥐","булочка"),("Märchen","🧚","казка"),
                   ("Kätzchen","🐱","кошеня"),("Büchlein","📕","книжечка"),("Vöglein","🐤","пташка")]},
        {"sing": "um", "show": "-um", "q": "Endet ein Wort auf", "a": "Fast immer das!",
         "words": [("Museum","🏛️","музей"),("Zentrum","🎯","центр"),("Datum","📅","дата"),
                   ("Studium","📚","навчання"),("Gymnasium","🏫","гімназія"),("Publikum","👏","публіка")]},
        {"sing": "ment", "show": "-ment", "q": "Endet ein Wort auf", "a": "Fast immer das!",
         "words": [("Instrument","🎻","інструмент"),("Dokument","📄","документ"),("Experiment","🧪","експеримент"),
                   ("Apartment","🏢","апартаменти"),("Medikament","💊","ліки"),("Parlament","🏛️","парламент")]},
        {"sing": "ma", "show": "-ma", "q": "Endet ein Wort auf", "a": "Fast immer das!",
         "words": [("Thema","🗂️","тема"),("Klima","🌦️","клімат"),("Drama","🎭","драма"),
                   ("Komma","✒️","кома"),("Schema","📐","схема"),("Dilemma","🤔","дилема")]},
        {"sing": "o", "show": "-o", "q": "Endet ein Wort auf", "a": "Fast immer das!",
         "words": [("Auto","🚗","машина"),("Kino","🎬","кіно"),("Büro","🖥️","офіс"),
                   ("Radio","📻","радіо"),("Foto","📷","фото"),("Konto","🏦","рахунок")]},
     ], "exceptions": ["der Moment", "der Konsum", "die Firma", "die Oma", "der Euro", "die Disco"]},
    {"id": "ep4_die_ion", "no": 4, "art": "die", "title": "Immer die! Teil 2",
     "blocks": [
        {"sing": "ion", "show": "-ion", "q": "Endet ein Wort auf", "a": "Immer die!",
         "words": [("Information","ℹ️","інформація"),("Situation","🚦","ситуація"),("Region","🗺️","регіон"),
                   ("Lektion","📖","урок"),("Station","🚉","станція"),("Religion","🙏","релігія")]},
        {"sing": "tät", "show": "-tät", "q": "Endet ein Wort auf", "a": "Immer die!",
         "words": [("Universität","🎓","університет"),("Qualität","⭐","якість"),("Realität","🌐","реальність"),
                   ("Kreativität","🎨","креативність"),("Nationalität","🛂","національність"),("Spezialität","🍲","фірмова страва")]},
        {"sing": "ik", "show": "-ik", "q": "Endet ein Wort auf", "a": "Fast immer die!",
         "words": [("Musik","🎵","музика"),("Politik","🗳️","політика"),("Physik","⚛️","фізика"),
                   ("Grammatik","🔤","граматика"),("Fabrik","🏭","фабрика"),("Klinik","🏥","клініка")]},
        {"sing": "ie", "line": "Endet ein Wort auf „ie“, wie Energie?", "show": "-ie", "q": "Endet ein Wort auf", "a": "Immer die!",
         "words": [("Familie","👨‍👩‍👧","сім'я"),("Energie","⚡","енергія"),("Fantasie","🦄","фантазія"),
                   ("Biologie","🌱","біологія"),("Therapie","🛋️","терапія"),("Industrie","🏗️","промисловість")]},
        {"sing": "ei", "show": "-ei", "q": "Endet ein Wort auf", "a": "Fast immer die!",
         "words": [("Polizei","🚓","поліція"),("Bäckerei","🥨","пекарня"),("Bücherei","📚","бібліотека"),
                   ("Partei","🗳️","партія"),("Türkei","🇹🇷","Туреччина"),("Metzgerei","🥩","м'ясна крамниця")]},
     ], "exceptions": ["der Atlantik", "das Genie", "das Ei", "der Papagei"]},
    {"id": "ep5_das_ge", "no": 5, "art": "das", "title": "Immer das! Teil 2",
     "blocks": [
        {"sing": "Ge", "line": "Beginnt ein Wort mit „Ge“?", "show": "Ge-", "q": "Beginnt ein Wort mit", "a": "Meistens das!",
         "words": [("Gebäude","🏢","будівля"),("Gemüse","🥦","овочі"),("Getränk","🥤","напій"),
                   ("Geschenk","🎁","подарунок"),("Gesicht","🙂","обличчя"),("Gespräch","🗣️","розмова")]},
        {"sing": "nis", "show": "-nis", "q": "Endet ein Wort auf", "a": "Fast immer das!",
         "words": [("Ergebnis","🏁","результат"),("Zeugnis","📜","атестат"),("Erlebnis","🎢","враження"),
                   ("Geheimnis","🤫","таємниця"),("Ereignis","📣","подія"),("Hindernis","🚧","перешкода")]},
        {"sing": "tum", "show": "-tum", "q": "Endet ein Wort auf", "a": "Meistens das!",
         "words": [("Eigentum","🔐","власність"),("Wachstum","🌳","зростання"),("Christentum","⛪","християнство"),
                   ("Altertum","🏺","античність"),("Heiligtum","🕍","святиня"),("Königtum","👑","королівство")]},
        {"sing": "ett", "show": "-ett", "q": "Endet ein Wort auf", "a": "Immer das!",
         "words": [("Bett","🛏️","ліжко"),("Ballett","🩰","балет"),("Etikett","🏷️","етикетка"),
                   ("Tablett","🍽️","таця"),("Skelett","💀","скелет"),("Kabinett","🗄️","кабінет")]},
        {"sing": "Verb", "line": "Wird ein Verb zum Nomen?", "show": "Verb → Nomen", "q": "Wird ein Verb zum Nomen", "a": "Immer das!",
         "words": [("Essen","🍝","їжа"),("Leben","🌈","життя"),("Lernen","📖","навчання"),
                   ("Schwimmen","🏊","плавання"),("Treffen","☕","зустріч"),("Wissen","🧠","знання")]},
     ], "exceptions": ["der Geschmack", "der Gedanke", "die Geduld", "die Erlaubnis", "der Irrtum", "der Reichtum"]},
]

RECAP = {
    "ep1_die_ung": "Ung, heit, keit, schaft — immer die!",
    "ep2_der": "Ling, ismus, ist und or, ig und ent — immer der!",
    "ep3_das_chen": "Chen und lein, um und ment, ma und o — immer das!",
    "ep4_die_ion": "Ion, tät, ik, ie und ei — immer die!",
    "ep5_das_ge": "Ge und nis, tum und ett, Verb als Nomen — immer das!",
}

for e in EPISODES:
    e.setdefault("exceptions", [])
    e["recap"] = RECAP[e["id"]]
    for b in e["blocks"]:
        b.setdefault("line", f'{b["q"]} „{b["sing"]}“?')


def lyrics(e):
    """Текст для поля Lyrics в Suno"""
    out = ["[Intro]", *INTRO, ""]
    for i, b in enumerate(e["blocks"], 1):
        ws = [f'{e["art"]} {w[0]}' for w in b["words"]]
        out += [f"[Verse {i}]", b["line"], b["a"],
                ", ".join(ws[:3]) + ",", ", ".join(ws[3:]) + ".",
                f'„{b["sing"]}“ — {b["a"].lower()}' if b["sing"] != "Verb" else f'Verb als Nomen — {b["a"].lower()}', ""]
    out += ["[Outro]", e["recap"], "Der, die, das — jetzt weißt du das!"]
    return "\n".join(out)
