# Первое видео: «Bruno versteht nur Deutsch»

Ролик: `bruno_nur_deutsch.mp4` (1080x1920, 68 с, H.264 + AAC). Субтитры отдельно: `subtitles_de.srt`.

## Откуда формат
Исходник: самое просматриваемое разобранное видео рейтинга, @ronralfovi4, 7063161633681509633, 72,2 млн просмотров (`../videos/7063161633681509633/analysis.md`).
Взяли структуру, а не содержание: стикер «ответ на комментарий» висит весь ролик, собака сначала игнорирует, развязка в конце, когда она смотрит прямо в камеру. Сверху добавлен урок: 5 команд-императивов, вежливая форма с Sie, слово das Leckerli.

## Сценарий (немецкий, A2–B1)
| время | сцена | текст |
|---|---|---|
| 1.2–6.6 с | hook | Jemand hat mich gefragt: Versteht dein Hund wirklich nur Deutsch? Gute Frage. Heute machen wir den Test. |
| 7.3–13.7 с | intro | Das ist Bruno. Bruno ist ein deutscher Schäferhund. Er ist drei Jahre alt, und er liegt am liebsten auf seinem roten Spielzeug. |
| 14.5–19.7 с | t1 | Erster Test. Ich sage es auf Englisch: Sit! Bruno bewegt sich nicht. Er schaut einfach weg. |
| 20.6–24.9 с | sitz | Jetzt auf Deutsch: Sitz! Und sofort setzt er sich hin. Sitz bedeutet: Setz dich! |
| 25.7–30.2 с | platz | Nächster Befehl: Platz! Bruno legt sich wieder hin. Platz heißt: Leg dich hin! |
| 31.0–34.7 с | komm | Und jetzt: Komm her! Bruno steht auf und kommt langsam zu mir. |
| 35.5–40.5 с | aus | Er hat sein Spielzeug im Maul. Ich sage: Aus! Und er lässt es fallen. Braver Hund! |
| 41.5–50.2 с | grammar | Übrigens: Sitz, Platz und Komm her sind Imperative. Zu einem Menschen sagt man höflicher: Könnten Sie sich bitte setzen? Aber Bruno mag keine langen Sätze. |
| 51.2–54.4 с | twist | Letzter Test. Ich flüstere ganz leise: Willst du ein Leckerli? |
| 56.0–61.1 с | reveal | Plötzlich hebt er den Kopf und schaut mich direkt an. Dieses Wort versteht er in jeder Sprache. |
| 62.0–65.8 с | cta | Welches Wort soll Bruno als Nächstes lernen? Schreib es in die Kommentare! |

## Как собрано
- Озвучка: Piper `de_DE-thorsten-high` (sherpa-onnx), по сценам, склейка с паузами: `project/build_voice.py` → `audio/voice.wav`, `project/timeline.json`.
- Тайминги слов: faster-whisper large-v3-turbo → `project/words.json`; текст субтитров берётся из сценария.
- Музыка: MusicGen small, 30 с, зациклена с кроссфейдом, приглушена под голос (`audio/bgm.wav`). **Лицензия весов MusicGen CC-BY-NC 4.0: только некоммерческое использование.** Для монетизируемого аккаунта музыку заменить на трек из библиотеки TikTok.
- Видео: HyperFrames, `project/gen.py` собирает `project/index.html` из `template.html` + таймингов. Рендер: скопировать `project/` в локальную папку, `hyperframes render -o video_silent.mp4`, затем свести звук ffmpeg (команда в истории треда).
