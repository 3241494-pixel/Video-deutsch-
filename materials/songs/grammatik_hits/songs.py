# 5 тем × 3 варианта песен для Suno. В вариантах одной темы слова, сюжет и примеры не повторяются.
# python songs.py -> <тема>/v1..v3.md и страница ../grammatik_hits/suno.html
TOPICS = [
 {"id": "t1_konjunktiv", "no": 1, "title": "Wenn ich könnte", "gram": "Konjunktiv II", "level": "B1", "genre": "mood-pop с фальцетом", "color": "#7B4FD0",
  "vars": [
   {"title": "Wenn ich könnte",
    "plot": "Два часа ночи, он у окна, хочет позвонить ей и поехать к ней последним поездом, но не решается.",
    "keys": "würde anrufen · wäre bei dir · hätte Zeit · könnte gehen · sollte schlafen",
    "style": "melancholic mood pop, soft male falsetto chorus, airy synth pads, fingerpicked guitar, sparse drums, 92 bpm, intimate and emotional, slow and very clear German pronunciation, pauses between lines",
    "lyrics": """[Intro]
Wenn ich könnte...
Wenn ich könnte...

[Verse 1]
Es ist zwei Uhr nachts, ich steh am Fenster
Die Stadt ist leise, nur das Licht ist noch wach
Dein Name leuchtet auf in meinem Handy
Ich schreib „Hallo“ und lösch es wieder, schwach

[Pre-Chorus]
Ich weiß, ich sollte schlafen
Doch mein Herz ist noch nicht müde

[Chorus]
Wenn ich könnte, würde ich dich anrufen
Wenn ich mutig wäre, wär ich jetzt bei dir
Wenn ich Zeit hätte, würde ich den Zug nehmen
Wenn ich könnte... wärst du jetzt hier

[Verse 2]
Der letzte Zug fährt um halb drei nach Hamburg
Ich hab die Jacke an, die Schuhe auch
Ich könnte gehen, ich könnte bleiben
Ich hätte so viel Lust und so viel Angst im Bauch

[Pre-Chorus]
Ich weiß, ich sollte schlafen
Doch mein Herz ist noch nicht müde

[Chorus]
Wenn ich könnte, würde ich dich anrufen
Wenn ich mutig wäre, wär ich jetzt bei dir
Wenn ich Zeit hätte, würde ich den Zug nehmen
Wenn ich könnte... wärst du jetzt hier

[Bridge]
Würdest du lachen? Würdest du weinen?
Hättest du Zeit für mich, nur eine Nacht?
Wäre es leichter, wenn ich ehrlich wäre?
Wenn ich nur sagen könnte: Ich hab an dich gedacht

[Final Chorus]
Wenn ich könnte, würde ich dich anrufen
Wenn ich mutig wäre, wär ich jetzt bei dir
Wenn ich Zeit hätte, würde ich den Zug nehmen
Wenn ich könnte... wärst du jetzt hier

[Outro]
Ich würde... ich wäre... ich hätte...
Wenn ich könnte."""},
   {"title": "Wenn ich reich wäre",
    "plot": "Понедельник, дождь, на счёте три евро. Она покупает лотерейный билет и мечтает о яхте, острове и новой машине для мамы.",
    "keys": "hätte ein Boot · wäre frei · würde kündigen · bekäme ein Auto · bräuchte nur dich",
    "style": "bittersweet mood pop, dreamy synths, finger snaps, warm bass, female vocal with soaring falsetto hook, 100 bpm, catchy and light, slow and very clear German pronunciation",
    "lyrics": """[Intro]
Was wäre, wenn...?
Was wäre, wenn...?

[Verse 1]
Montagmorgen, Regen, mein Konto ist leer
Ich zähl mein Kleingeld: drei Euro, nicht mehr
Ich kauf ein Los am Kiosk, nur zum Spaß
Ich schließe die Augen und denke: Was wäre, wenn...

[Pre-Chorus]
Nur einmal Glück...
Nur ein kleines Stück...

[Chorus]
Wenn ich reich wäre, hätte ich ein Boot
Ich würde segeln bis zum Abendrot
Wenn ich Millionen hätte, wär ich frei
Ich würde kündigen, und mein Chef wär nicht dabei

[Verse 2]
Ich hätte ein Haus auf einer Insel im Meer
Mit Palmen und Sonne, was will man mehr?
Ich würde frühstücken um zwölf Uhr im Bett
Und Mama bekäme ein Auto, ganz neu und ganz nett

[Pre-Chorus]
Nur einmal Glück...
Nur ein kleines Stück...

[Chorus]
Wenn ich reich wäre, hätte ich ein Boot
Ich würde segeln bis zum Abendrot
Wenn ich Millionen hätte, wär ich frei
Ich würde kündigen, und mein Chef wär nicht dabei

[Bridge]
Doch dann hält die Bahn, die Tür geht auf
Ich steig aus, ich lauf und lauf
Du wartest schon, du lachst mich an
Ich bräuchte kein Geld, wenn ich dich haben kann

[Final Chorus]
Wenn ich reich wäre, hätte ich ein Boot
Ich würde segeln bis zum Abendrot
Wenn ich Millionen hätte, wär ich frei
Doch ich hab dich, und du bist dabei

[Outro]
Hätte, wäre, würde...
Was wäre, wenn?"""},
   {"title": "Wär ich ein Vogel",
    "plot": "Она лежит в траве и смотрит на облака. Фантазии: если бы я была птицей, звездой, волшебницей, если бы у меня была машина времени.",
    "keys": "Wär ich ein Vogel, würde ich fliegen · Wenn ich zaubern könnte · Hätte ich eine Zeitmaschine · wüsste alles",
    "style": "dreamy ethereal mood pop, breathy female falsetto, music box and soft piano, gentle beat, 88 bpm, cinematic and tender, whispered verses, slow and very clear German pronunciation",
    "lyrics": """[Intro]
La-la-la...
Wär ich ein Vogel...

[Verse 1]
Ich lieg im Gras und schau nach oben
Die Wolken ziehen langsam vorbei
Ein kleiner Vogel singt da oben
Und ich denk: Der ist so frei

[Pre-Chorus]
Wenn ich nur Flügel hätte...
Nur für einen Tag...

[Chorus]
Wär ich ein Vogel, würde ich fliegen
Hoch über Wolken, bis zu dir
Wär ich ein Stern, würde ich leuchten
Jede Nacht vor deiner Tür

[Verse 2]
Wenn ich zaubern könnte, wäre immer Sommer
Kein Winter, kein Regen, kein Grau
Hätte ich eine Zeitmaschine
Wär ich wieder sieben und wüsste alles genau

[Pre-Chorus]
Wenn ich nur Flügel hätte...
Nur für einen Tag...

[Chorus]
Wär ich ein Vogel, würde ich fliegen
Hoch über Wolken, bis zu dir
Wär ich ein Stern, würde ich leuchten
Jede Nacht vor deiner Tür

[Bridge]
Und wenn ich der Mond wäre
Würde ich dir Licht geben
Und wenn du das Meer wärst
Würd ich jede Nacht zu dir schweben

[Final Chorus]
Wär ich ein Vogel, würde ich fliegen
Hoch über Wolken, bis zu dir
Wär ich ein Stern, würde ich leuchten
Jede Nacht vor deiner Tür

[Outro]
Wär ich ein Vogel...
Ich wär bei dir."""},
  ]},
 {"id": "t2_modalverben", "no": 2, "title": "Ich muss nicht, ich will", "gram": "Модальные глаголы", "level": "A2", "genre": "техно-шлагер гимн", "color": "#E0313F",
  "vars": [
   {"title": "Ich muss nicht, ich will",
    "plot": "Всю неделю «надо»: офис, письма, улыбаться. В пятницу вечером можно всё: танцевать до утра.",
    "keys": "muss ins Büro · soll pünktlich sein · will tanzen · kann bis morgens · darf heute Nacht",
    "style": "techno schlager anthem, four-on-the-floor kick, 128 bpm, big festival synth leads, crowd shouts hey, euphoric singalong chorus, powerful female lead vocal, very clear German pronunciation",
    "lyrics": """[Intro]
Hey! Hey!
Freitag, achtzehn Uhr!

[Verse 1]
Die ganze Woche muss ich früh raus
Ich muss ins Büro, muss Mails schreiben, muss nach Haus
Ich muss lächeln, ich muss nett sein
Doch heute Nacht, da lass ich das sein!

[Pre-Chorus]
Und jetzt? Jetzt darf ich!
Und jetzt? Jetzt kann ich!

[Chorus]
Ich muss nicht, ich will!
Ich will tanzen, ich will laut sein, niemand sagt: Sei still!
Ich kann bis morgens, ich darf heute Nacht
Ich muss nicht, ich will! Bis die Sonne lacht!

[Verse 2]
Am Montag soll ich wieder funktionieren
Ich soll pünktlich sein und nicht diskutieren
Doch Montag ist weit, und Freitag ist hier
Ich will nur den Bass und tanzen mit dir

[Pre-Chorus]
Und jetzt? Jetzt darf ich!
Und jetzt? Jetzt kann ich!

[Chorus]
Ich muss nicht, ich will!
Ich will tanzen, ich will laut sein, niemand sagt: Sei still!
Ich kann bis morgens, ich darf heute Nacht
Ich muss nicht, ich will! Bis die Sonne lacht!

[Bridge]
Ich muss? Nein!
Ich will? Ja!
Ich kann? Ja!
Ich darf? Ja! Ja! Ja!

[Final Chorus]
Ich muss nicht, ich will!
Ich will tanzen, ich will laut sein, niemand sagt: Sei still!
Ich kann bis morgens, ich darf heute Nacht
Ich muss nicht, ich will! Bis die Sonne lacht!

[Outro]
Ich muss nicht...
Ich will!"""},
   {"title": "Jetzt darf ich",
    "plot": "Детство: «ты должен есть овощи, тебе нельзя мороженое». Теперь взрослый и всё можно. Но теперь надо платить счета, и в детстве было неплохо.",
    "keys": "du sollst Gemüse essen · du darfst kein Eis · so lang ich mag · ich muss Rechnungen zahlen · du musst nicht",
    "style": "techno schlager party, 126 bpm, retro 90s rave synths, stomping kick, male and female duet, call-and-response chorus, crowd chant, funny and nostalgic, very clear German pronunciation",
    "lyrics": """[Intro]
Mama sagt...
Papa sagt...

[Verse 1]
Mit sieben hieß es immer: Du sollst Gemüse essen!
Du sollst dein Zimmer aufräumen und die Hausaufgaben nicht vergessen!
Du darfst kein Eis vor dem Essen, du darfst nicht so lange fernsehen
Um acht Uhr sollst du schlafen, du darfst nicht mehr rausgehen!

[Pre-Chorus]
Doch heute bin ich groß! (Groß!)
Heute geht es los! (Los!)

[Chorus]
Jetzt darf ich! Eis zum Frühstück, jeden Tag!
Jetzt darf ich! Fernsehen, so lang ich mag!
Niemand sagt mehr: Du sollst, du musst!
Jetzt darf ich, und ich hab so viel Lust!

[Verse 2]
Doch jetzt muss ich Rechnungen zahlen
Ich muss kochen und putzen, das ist nicht normal!
Ich soll Sport machen, soll früh ins Bett
Mama, ich glaub, früher war es doch ganz nett!

[Pre-Chorus]
Doch heute bin ich groß! (Groß!)
Heute geht es los! (Los!)

[Chorus]
Jetzt darf ich! Eis zum Frühstück, jeden Tag!
Jetzt darf ich! Fernsehen, so lang ich mag!
Niemand sagt mehr: Du sollst, du musst!
Jetzt darf ich, und ich hab so viel Lust!

[Bridge]
Darf ich? (Ja, du darfst!)
Soll ich? (Nein, du sollst nicht!)
Muss ich? (Nein, du musst nicht!)
Mag ich? (Na klar, du magst!)

[Final Chorus]
Jetzt darf ich! Eis zum Frühstück, jeden Tag!
Jetzt darf ich! Fernsehen, so lang ich mag!
Niemand sagt mehr: Du sollst, du musst!
Jetzt darf ich, und ich hab so viel Lust!

[Outro]
Jetzt darf ich...
(Du darfst!)"""},
   {"title": "Ich kann das",
    "plot": "Год назад в пекарне смогла сказать только «Hallo», продавщица засмеялась. Сегодня заказывает булочки и сама всё объясняет врачу. Гимн тем, кто учит немецкий.",
    "keys": "konnte nur Hallo · wollte Brötchen kaufen · ich möchte lernen · kann bestellen · darf Fehler machen",
    "style": "uplifting techno schlager anthem, 130 bpm, euphoric piano chords over pounding kick, stadium chant, motivational, female lead with gang vocals, very clear and slow German pronunciation",
    "lyrics": """[Intro]
Eins, zwei, drei:
Ich kann das!

[Verse 1]
Vor einem Jahr konnte ich nur „Hallo“
Ich wollte Brötchen kaufen und sagte nur: „So...“
Die Frau beim Bäcker hat gelacht
Ich bin nach Hause gegangen und hab gedacht:

[Pre-Chorus]
Ich möchte das lernen! Ich will es verstehen!
Ich muss nicht perfekt sein, ich muss nur weitergehen!

[Chorus]
Ich kann das! Ich kann Deutsch sprechen!
Ich kann das! Kein Fehler wird mich brechen!
Ich will mehr, ich möchte fliegen
Ich kann das, und ich werde siegen!

[Verse 2]
Heute kann ich Brötchen bestellen
Und beim Arzt kann ich alles selbst erzählen
Ich darf noch Fehler machen, das ist okay
Morgen kann ich mehr, und übermorgen: olé!

[Pre-Chorus]
Ich möchte das lernen! Ich will es verstehen!
Ich muss nicht perfekt sein, ich muss nur weitergehen!

[Chorus]
Ich kann das! Ich kann Deutsch sprechen!
Ich kann das! Kein Fehler wird mich brechen!
Ich will mehr, ich möchte fliegen
Ich kann das, und ich werde siegen!

[Bridge]
Können? Ich kann!
Wollen? Ich will!
Möchten? Ich möchte!
Dürfen? Ich darf!

[Final Chorus]
Ich kann das! Ich kann Deutsch sprechen!
Ich kann das! Kein Fehler wird mich brechen!
Ich will mehr, ich möchte fliegen
Ich kann das, und ich werde siegen!

[Outro]
Ich kann das!
Du kannst das!"""},
  ]},
 {"id": "t3_wo_wohin", "no": 3, "title": "Wo oder wohin?", "gram": "Akkusativ / Dativ", "level": "A2–B1", "genre": "afro-pop с танцем", "color": "#E8840C",
  "vars": [
   {"title": "Wo oder wohin?",
    "plot": "Танец-челлендж: каждое движение «куда» (Akkusativ), каждая позиция «где» (Dativ). Руки вверх, на стол, к колонке, в круг.",
    "keys": "auf die Tanzfläche → auf der Tanzfläche · in die Luft → in der Luft · auf den Tisch → auf dem Tisch · in den Kreis → im Kreis",
    "style": "afro-pop dance song, amapiano log drum, 112 bpm, bright marimba, catchy call-and-response chorus, warm male vocal, summer vibe, dance challenge hook, very clear German pronunciation",
    "lyrics": """[Intro]
Wo? Da!
Wohin? Dahin!
Los geht's!

[Verse 1]
Die Musik ist an, ich spring auf die Tanzfläche
Jetzt tanz ich auf der Tanzfläche, mitten drin, hey!
Ich lauf neben dich, jetzt tanz ich neben dir
Ich spring auf die Bühne, jetzt bin ich auf der Bühne hier

[Pre-Chorus]
Bewegung? Akkusativ!
Position? Dativ!

[Chorus]
Wo oder wohin? Wo oder wohin?
Wohin: den, die, das! Wo: dem, der, dem!
Hände in die Luft! Jetzt sind sie in der Luft!
Wo oder wohin? Tanz mit mir, ich ruf!

[Verse 2]
Ich spring auf den Tisch, jetzt tanz ich auf dem Tisch
Ich spring vor die Box, ich steh vor der Box, so frisch
Wir laufen in den Kreis, wir tanzen im Kreis
Wo ist die Party? Hier! Und es ist so heiß!

[Pre-Chorus]
Bewegung? Akkusativ!
Position? Dativ!

[Chorus]
Wo oder wohin? Wo oder wohin?
Wohin: den, die, das! Wo: dem, der, dem!
Hände in die Luft! Jetzt sind sie in der Luft!
Wo oder wohin? Tanz mit mir, ich ruf!

[Bridge]
Wohin? An die Wand! Wo? An der Wand!
Wohin? In die Mitte! Wo? In der Mitte!
Wohin? Auf den Boden! Wo? Auf dem Boden!
Wohin? Unter den Mond! Wo? Unter dem Mond!

[Final Chorus]
Wo oder wohin? Wo oder wohin?
Wohin: den, die, das! Wo: dem, der, dem!
Hände in die Luft! Jetzt sind sie in der Luft!
Wo oder wohin? Tanz mit mir, ich ruf!

[Outro]
Wo? Da!
Wohin? Dahin!"""},
   {"title": "Wohin mit der Katze?",
    "plot": "Смешная история дома: куда бы я ни положила вещь, кошка уже там. Пары глаголов legen/liegen, stellen/stehen, hängen, setzen/sitzen.",
    "keys": "lege das Buch auf das Sofa → liegt auf dem Sofa · stelle die Vase ins Regal → steht im Regal · hänge die Jacke an die Tür → hängt an der Tür · setze sie auf das Bett → sitzt auf dem Bett",
    "style": "playful afrobeats pop, 108 bpm, bouncy bass, shakers and talking drum, funny storytelling, bright female vocal with spoken interjections, meow ad-libs, very clear German pronunciation",
    "lyrics": """[Intro]
Miau!
Wo ist die Katze?

[Verse 1]
Ich lege mein Buch auf das Sofa
Fünf Minuten später liegt die Katze auf dem Sofa
Ich stelle die Vase ins Regal
Jetzt steht die Katze im Regal, total normal!
Ich hänge die Jacke an die Tür
Jetzt hängt die Katze an der Tür und schaut zu mir

[Pre-Chorus]
Legen, stellen, hängen: wohin? Akkusativ!
Liegen, stehen, hängen: wo? Dativ!

[Chorus]
Wohin mit der Katze? Wohin? Wohin?
Auf das Bett! Jetzt sitzt sie auf dem Bett.
In den Korb! Jetzt liegt sie im Korb. Wie nett!
Wo ist die Katze? Wo? Wo? Wo?
Unter dem Schrank! Na so was, oh!

[Verse 2]
Ich lege die Brille neben den Laptop
Wo ist die Brille? Unter der Katze! Stopp!
Ich hänge das Bild über das Sofa
Jetzt hängt es über dem Sofa, und die Katze schläft darunter, oha!

[Pre-Chorus]
Legen, stellen, hängen: wohin? Akkusativ!
Liegen, stehen, hängen: wo? Dativ!

[Chorus]
Wohin mit der Katze? Wohin? Wohin?
Auf das Bett! Jetzt sitzt sie auf dem Bett.
In den Korb! Jetzt liegt sie im Korb. Wie nett!
Wo ist die Katze? Wo? Wo? Wo?
Unter dem Schrank! Na so was, oh!

[Bridge]
Die Katze springt: Akkusativ!
Die Katze schläft: Dativ, Dativ!
Sie springt auf den Stuhl, sie schläft auf dem Stuhl
Sie springt in die Kiste, sie schläft in der Kiste, cool!

[Final Chorus]
Wohin mit der Katze? Wohin? Wohin?
Auf das Bett! Jetzt sitzt sie auf dem Bett.
In den Korb! Jetzt liegt sie im Korb. Wie nett!
Wo ist die Katze? Wo? Wo? Wo?
Unter dem Schrank! Na so was, oh!

[Outro]
Miau!
Sie ist da."""},
   {"title": "Ich geh in die Stadt",
    "plot": "Летняя суббота по городу: в парк и в парке, в кафе, на пляж, в кино, на озеро, в клуб. Дуэт, где один спрашивает «куда?», другой отвечает «где».",
    "keys": "in den Park → im Park · ins Café → im Café · an den Strand → am Strand · ins Kino → im Kino · an den See → am See · in den Club → im Club",
    "style": "sunny afro-pop summer anthem, 115 bpm, afro-house groove, highlife guitar riffs, hand claps, male and female vocals trading lines, dance hook, very clear German pronunciation",
    "lyrics": """[Intro]
Wohin gehst du?
Und wo bist du?

[Verse 1]
Samstag, Sonne, ich geh in den Park
Jetzt bin ich im Park, und die Musik ist stark
Du rufst: Komm ins Café, ich bin gleich da!
Jetzt sind wir im Café, wunderbar!

[Pre-Chorus]
In den, in die, ins: wenn ich geh!
Im, in der, im: wenn ich da bin, eh!

[Chorus]
Wohin? In die Stadt! Wo? In der Stadt!
Wohin? An den Strand! Wo? Am Strand!
Wohin? Ins Kino! Wo? Im Kino!
Wohin gehen wir heute? Komm, nimm meine Hand!

[Verse 2]
Am Abend fahren wir an den See
Wir schwimmen im See, ich will nie mehr gehen, nee!
Dann gehen wir in den Club, die Nacht ist jung
Wir tanzen im Club, die ganze Nacht im Schwung

[Pre-Chorus]
In den, in die, ins: wenn ich geh!
Im, in der, im: wenn ich da bin, eh!

[Chorus]
Wohin? In die Stadt! Wo? In der Stadt!
Wohin? An den Strand! Wo? Am Strand!
Wohin? Ins Kino! Wo? Im Kino!
Wohin gehen wir heute? Komm, nimm meine Hand!

[Bridge]
Ich geh in die Schule, ich bin in der Schule
Ich geh in den Supermarkt, ich bin im Supermarkt
Ich fahr in die Berge, ich wohne in den Bergen
Und du? Wohin gehst du? Sing mit!

[Final Chorus]
Wohin? In die Stadt! Wo? In der Stadt!
Wohin? An den Strand! Wo? Am Strand!
Wohin? Ins Kino! Wo? Im Kino!
Wohin gehen wir heute? Komm, nimm meine Hand!

[Outro]
Wohin? Mit dir!
Wo? Bei dir!"""},
  ]},
 {"id": "t4_verb_ende", "no": 4, "title": "Verb ans Ende", "gram": "weil / dass", "level": "A2–B1", "genre": "Deutschrap", "color": "#1C6FD6",
  "vars": [
   {"title": "Verb ans Ende",
    "plot": "Опоздание на работу: автобус не пришёл, зонта нет, телефон сел, ключа нет. Каждое оправдание с weil, глагол в конце.",
    "keys": "weil der Bus nicht kam · weil ich keinen Schirm mitnahm · dass du so sauer bist · weil ich es nicht geladen habe · dass er mich deckt",
    "style": "German rap, boom bap meets modern trap, 90 bpm, punchy 808, piano sample, confident male rapper, melodic sung hook, storytelling, very clear articulation of every word",
    "lyrics": """[Intro]
Yo. Merk dir eins:
Mit weil und dass geht das Verb ans Ende.
Los!

[Verse 1]
Ich komm zu spät, weil der Bus nicht kam
Ich steh im Regen, weil ich keinen Schirm mitnahm
Der Chef schaut böse, weil es schon neun ist
Ich sag: Es tut mir leid, dass du so sauer bist
Ich hab verschlafen, weil ich lange gelernt habe
Und ich glaube, dass ich jetzt ein Problem habe

[Hook]
Verb ans Ende! (Ende!) Verb ans Ende! (Ende!)
Mit weil und mit dass geht das Verb ans Ende!
Ich sag, dass ich komme. Ich komm, weil ich will.
Verb ans Ende... und dann ist es still.

[Verse 2]
Mein Handy ist tot, weil ich es nicht geladen habe
Die Tür ist zu, weil ich den Schlüssel nicht mehr habe
Mein Kollege sagt, dass er mich heute deckt
Ich hoffe, dass der Chef das nicht so schnell checkt
Ich renne die Treppe hoch, weil ich keine Zeit hab
Und ich weiß, dass ich morgen einen besseren Plan hab

[Hook]
Verb ans Ende! (Ende!) Verb ans Ende! (Ende!)
Mit weil und mit dass geht das Verb ans Ende!
Ich sag, dass ich komme. Ich komm, weil ich will.
Verb ans Ende... und dann ist es still.

[Bridge]
(spoken)
Ich bin müde.
Warum? Weil ich nicht geschlafen habe.
Ich weiß es.
Was? Dass ich zu spät bin.

[Hook]
Verb ans Ende! (Ende!) Verb ans Ende! (Ende!)
Mit weil und mit dass geht das Verb ans Ende!
Ich sag, dass ich komme. Ich komm, weil ich will.
Verb ans Ende... und dann ist es still.

[Outro]
Weil... dass...
Ende."""},
   {"title": "Ich weiß, dass ich's schaffe",
    "plot": "Мотивационный рэп: учитель, соседи и брат говорят, что не получится. Он отвечает: я знаю, что справлюсь. Все примеры с dass после sagen, meinen, glauben, hoffen, wissen.",
    "keys": "sagt, dass ich zu langsam bin · meinen, dass ich nie gewinne · glaubt, dass ich es kann · hoffe, dass die Halle brennt · dass ich wieder aufstehen kann",
    "style": "motivational Deutschrap, 95 bpm, dark cinematic strings, hard drums, male rapper verses, emotional sung chorus by female vocalist, rising energy, very clear German articulation",
    "lyrics": """[Intro]
Sie sagen, dass ich's nicht schaffe.
(Pause)
Und ich sage: Doch.

[Verse 1]
Mein Lehrer sagt, dass ich zu langsam bin
Die Nachbarn meinen, dass ich nie gewinn
Mein Bruder lacht, dass ich jeden Tag Vokabeln lern
Doch ich glaube, dass ich leuchte wie ein Stern
Mama sagt leise, dass sie an mich glaubt
Und dass mir niemand meine Träume raubt

[Chorus]
Ich weiß, dass ich es schaffe
Ich weiß, dass ich es kann
Ihr sagt, dass ich falle
Ich sag, dass ich wieder aufstehen kann!

[Verse 2]
Ich hoffe, dass die Halle heute brennt
Ich träume, dass mich morgen jeder kennt
Ich merke, dass die Angst jetzt kleiner wird
Und ich spüre, dass mein Herz nicht mehr friert
Ich zeig euch allen, dass ich weiter geh
Und dass ich heute ganz oben steh

[Chorus]
Ich weiß, dass ich es schaffe
Ich weiß, dass ich es kann
Ihr sagt, dass ich falle
Ich sag, dass ich wieder aufstehen kann!

[Bridge]
Er sagt, dass... Verb am Ende.
Sie glaubt, dass... Verb am Ende.
Ich weiß, dass ich es schaffe.
Und jetzt wisst ihr: Das Verb steht am Ende.

[Final Chorus]
Ich weiß, dass ich es schaffe
Ich weiß, dass ich es kann
Ihr sagt, dass ich falle
Ich sag, dass ich wieder aufstehen kann!

[Outro]
Dass ich es schaffe.
Dass ich es kann."""},
   {"title": "Obwohl",
    "plot": "Спокойный берлинский вечер: холодный кофе, сломанный велосипед, дорогая аренда, пицца и Späti с другом. Больше союзов с глаголом в конце: obwohl, wenn, ob, weil.",
    "keys": "obwohl er schon kalt ist · weil das Fahrrad kaputt ist · obwohl die Miete so hoch ist · ob du Zeit hast · wenn du Hunger hast",
    "style": "laid-back Deutschrap, lo-fi boom bap, 88 bpm, jazzy Rhodes, vinyl crackle, relaxed male flow, chill sung hook, Berlin street vibe at night, very clear German pronunciation",
    "lyrics": """[Intro]
Weil, dass, obwohl, wenn:
Alle schicken das Verb ans Ende.
Hör zu.

[Verse 1]
Ich trink meinen Kaffee, obwohl er schon kalt ist
Ich nehm die U-Bahn, weil das Fahrrad kaputt ist
Ich bleib in Berlin, obwohl die Miete so hoch ist
Weil diese Stadt für mich wie ein Zuhause ist
Ich lauf durch die Straßen, obwohl es schon spät ist
Weil die Nacht hier so schön und so laut ist

[Hook]
Weil, obwohl, dass, wenn
Am Ende steht das Verb, und du kennst den Trend
Wenn du Zeit hast, ruf an
Wenn du Lust hast, komm ran!

[Verse 2]
Ich frag mich, ob du heute Abend Zeit hast
Wir holen Pizza, wenn du Hunger hast
Ich wette, dass der Späti noch offen ist
Und wenn nicht, egal, weil du hier bist
Wir sitzen auf dem Dach, obwohl es kalt wird
Und ich hoffe, dass die Nacht nie alt wird

[Hook]
Weil, obwohl, dass, wenn
Am Ende steht das Verb, und du kennst den Trend
Wenn du Zeit hast, ruf an
Wenn du Lust hast, komm ran!

[Bridge]
(spoken)
Obwohl es spät ist, bleib ich wach.
Weil ich dich mag.
Und wenn du gehst, ist es nicht dasselbe.

[Hook]
Weil, obwohl, dass, wenn
Am Ende steht das Verb, und du kennst den Trend
Wenn du Zeit hast, ruf an
Wenn du Lust hast, komm ran!

[Outro]
Obwohl... weil... wenn...
Verb am Ende."""},
  ]},
 {"id": "t5_reflexiv", "no": 5, "title": "Ich zieh mich an", "gram": "Возвратные глаголы", "level": "A2", "genre": "bedroom pop", "color": "#1E9E52",
  "vars": [
   {"title": "Ich zieh mich an",
    "plot": "Утро: потягиваюсь, умываюсь, чищу зубы, одеваюсь, тороплюсь. Тихо и уютно, первый снег за окном.",
    "keys": "ich strecke mich · ich wasche mich · ich putze mir die Zähne · ich ziehe mich an · ich beeile mich · ich verspäte mich nicht",
    "style": "lo-fi bedroom pop, 80 bpm, soft drum machine, warm detuned guitar, cozy morning mood, intimate soft female vocal, light reverb, slow and very clear German pronunciation",
    "lyrics": """[Intro]
Mmm...
Sieben Uhr...

[Verse 1]
Ich wache auf, das Licht ist noch grau
Ich strecke mich und gähne, ich weiß nicht genau
Ich stehe auf und schau mich im Spiegel an
Ich wasche mich mit kaltem Wasser, und dann...

[Pre-Chorus]
Ich putze mir die Zähne (mir!)
Ich kämme mir die Haare (mir!)

[Chorus]
Ich zieh mich an, ich zieh mich an
Den gelben Pulli, den ich so mag
Ich beeile mich, ich beeile mich
Ich verspäte mich nicht, nicht an diesem Tag

[Verse 2]
Ich setze mich ans Fenster mit meinem Kaffee
Draußen liegt der erste Schnee
Ich schminke mich ein bisschen, nur für mich
Ich föhne mir die Haare, und dann beeil ich mich

[Pre-Chorus]
Ich putze mir die Zähne (mir!)
Ich kämme mir die Haare (mir!)

[Chorus]
Ich zieh mich an, ich zieh mich an
Den gelben Pulli, den ich so mag
Ich beeile mich, ich beeile mich
Ich verspäte mich nicht, nicht an diesem Tag

[Bridge]
Ich: mich. Du: dich. Er, sie: sich.
Wir: uns. Ihr: euch. Sie: sich.
(whisper) Und du?
Ziehst du dich auch an?

[Final Chorus]
Ich zieh mich an, ich zieh mich an
Den gelben Pulli, den ich so mag
Ich beeile mich, ich beeile mich
Ich verspäte mich nicht, nicht an diesem Tag

[Outro]
Mmm...
Ich bin bereit."""},
   {"title": "Ich verliebe mich",
    "plot": "Встреча на вокзале: он опоздал, она сердится, но он извиняется и улыбается. Чувства через возвратные глаголы, в том числе «мы друг друга» (uns).",
    "keys": "wir treffen uns · ich ärgere mich · du entschuldigst dich · ich freue mich auf · ich verliebe mich · wir erinnern uns · wir verstehen uns",
    "style": "dreamy bedroom pop, 85 bpm, jangly clean guitar, soft synth pads, tape hiss, gentle male vocal with soft harmonies, nostalgic summer love, slow and very clear German pronunciation",
    "lyrics": """[Intro]
Du kommst zu spät...
Wie immer.

[Verse 1]
Wir treffen uns am Bahnhof, du kommst zu spät
Ich ärgere mich kurz, bis der Wind sich dreht
Du lachst und entschuldigst dich ganz leise
Und ich freue mich auf unsere kleine Reise

[Pre-Chorus]
Und plötzlich...
Ganz plötzlich...

[Chorus]
Ich verliebe mich, ich verliebe mich
In dein Lachen und in dein Gesicht
Ich fühle mich leicht, ich fühl mich so gut
Verliebst du dich auch? Hast du den Mut?

[Verse 2]
Wir erinnern uns an den ersten Tag
Ich hab mich nicht getraut zu sagen, was ich mag
Heute trau ich mich und nehme deine Hand
Wir verstehen uns ohne Worte, wie das Meer und der Sand

[Pre-Chorus]
Und plötzlich...
Ganz plötzlich...

[Chorus]
Ich verliebe mich, ich verliebe mich
In dein Lachen und in dein Gesicht
Ich fühle mich leicht, ich fühl mich so gut
Verliebst du dich auch? Hast du den Mut?

[Bridge]
Ich freue mich, du freust dich, wir freuen uns
Ich verliebe mich, du verliebst dich
Wir verlieben uns

[Final Chorus]
Ich verliebe mich, ich verliebe mich
In dein Lachen und in dein Gesicht
Ich fühle mich leicht, ich fühl mich so gut
Verliebst du dich auch? Hast du den Mut?

[Outro]
Wir verlieben uns...
Mmm."""},
   {"title": "Ich leg mich hin",
    "plot": "Вечер дома после длинного дня: тёплый душ, чай с мёдом, плед, книга и дождь по крыше. Колыбельная.",
    "keys": "ich dusche mich · ich mache mir einen Tee · ich wickle mich in die Decke · ich entspanne mich · ich lege mich hin · ich erhole mich · leg dich hin",
    "style": "sleepy bedroom pop lullaby, 72 bpm, soft Rhodes piano, rain sounds, brushed drums, whispery female vocal, cozy and calm, very slow and very clear German pronunciation",
    "lyrics": """[Intro]
(Regen...)
Endlich zu Hause.

[Verse 1]
Ich komme nach Hause, es regnet, es ist spät
Ich dusche mich warm, bis der Stress vergeht
Ich mache mir einen Tee mit Honig drin
Und wickle mich in die Decke, so wie ich bin

[Pre-Chorus]
Ich entspanne mich...
Ich beruhige mich...

[Chorus]
Ich leg mich hin, ich leg mich hin
Der Regen singt leise auf dem Dach
Ich kuschle mich ins Kissen ein
Und bleib noch ein bisschen wach

[Verse 2]
Ich langweile mich nicht, ich liebe die Ruh
Ich lese ein Buch, die Augen fallen zu
Ich erhole mich, mein Kopf wird leer
Ich wünsche mir nichts, nichts mehr

[Pre-Chorus]
Ich entspanne mich...
Ich beruhige mich...

[Chorus]
Ich leg mich hin, ich leg mich hin
Der Regen singt leise auf dem Dach
Ich kuschle mich ins Kissen ein
Und bleib noch ein bisschen wach

[Bridge]
(whisper)
Und du? Leg dich auch hin.
Entspann dich.
Ich verabschiede mich.
Gute Nacht.

[Final Chorus]
Ich leg mich hin, ich leg mich hin
Der Regen singt leise auf dem Dach
Ich kuschle mich ins Kissen ein
Und schlaf ganz langsam ein

[Outro]
Gute Nacht...
(Regen...)"""},
  ]},
]

if __name__ == "__main__":
    import os, html
    ROOT = os.path.dirname(os.path.abspath(__file__))
    for t in TOPICS:
        for k, v in enumerate(t["vars"], 1):
            d = f"{ROOT}/{t['id']}/v{k}"; os.makedirs(d, exist_ok=True)
            open(f"{d}/text.md", "w").write(
                f"# {t['no']}.{k} {v['title']}\n\n{t['gram']} · {t['level']} · {t['genre']}\n\n**Сюжет:** {v['plot']}\n\n"
                f"**Ключевые примеры:** {v['keys']}\n\n## Style\n```\n{v['style']}\n```\n\n## Lyrics\n```\n{v['lyrics']}\n```\n")
    print("ok")
