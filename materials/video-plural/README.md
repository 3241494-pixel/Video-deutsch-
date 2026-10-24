# Видео 2: «Plural im Deutschen» (множественное число существительных)

Ролик: `plural_deutsch.mp4` (1080x1920, 98.6 с, H.264 + AAC, -14 LUFS). Субтитры отдельно: `subtitles_de.srt`.
Светлая тема, анимации GSAP, немецкая озвучка, уровень A2–B1.

## Структура
| время | сцена | что на экране |
|---|---|---|
| 0–10 с | хук | Tisch → Tische, Buch → Bücher, Auto → Autos, «chaotisch?!», «6 Regeln» |
| 10–19 с | правило 1: -e | der Tag, der Hund, das Jahr; «oft maskulin» |
| 19–29 с | правило 2: умлаут + -e | der Stuhl, die Hand, der Zug; a o u → ä ö ü |
| 29–38 с | правило 3: -er | das Kind, das Buch, das Haus; «oft neutral, mit Umlaut» |
| 38–47 с | правило 4: -n / -en | die Lampe, die Frau, die Zeitung; «fast alle femininen» |
| 47–57 с | правило 5: -s | das Auto, das Handy, das Hotel; иностранные слова |
| 57–67 с | правило 6: без окончания | der Lehrer, das Zimmer, der Apfel (Äpfel) |
| 67–73 с | совет | учить слово с артиклем и плюралем, карточка das Buch → die Bücher |
| 73–92 с | тест | 5 слов (Katze, Baum, Kino, Glas, Koffer), таймер 5 с «Pause drücken!», ответы с подсветкой |
| 92–99 с | CTA | «Wie viele hast du richtig?» + 0/5 · 3/5 · 5/5 |

Полный текст озвучки: `project/script.json`. Отличия формы мн. числа (умлаут, окончание) подсвечиваются цветом правила.

## Как собрано (тот же пайплайн, что у первого ролика)
- Озвучка: Piper `de_DE-thorsten-high`, speed 0.95, по сценам → `project/build_voice.py` → `audio/voice.wav`, `project/timeline.json`.
- Тайминги слов: faster-whisper large-v3-turbo с подсказкой-сценарием → `project/fw.words.json`.
- Видео: `project/gen.py` строит `proj/index.html` из `template.html` (сцены, анимации и караоке-субтитры генерируются кодом). Рендер `hyperframes render -o video_silent.mp4` (~3.5 мин).
- Музыка: **взята из первого ролика** (`../first-video/audio/bgm.wav`, MusicGen, CC-BY-NC, только некоммерческое использование), зациклена с кроссфейдом 1.5 с, приглушена под голос (sidechain), +11 dB и лимитер → `audio/mix.wav`.
- Сборка: `ffmpeg -i video_silent.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k plural_deutsch.mp4`.
- Озвучка окончаний: Piper читает «-e», «-er», «-s» правильно, а «-en» плохо, поэтому в правиле 4 голос говорит «Plural mit n», а на экране «-n / -en».
