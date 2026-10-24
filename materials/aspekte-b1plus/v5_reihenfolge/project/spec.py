# Видео 5: Stellung der Objekte (Aspekte neu B1+, Kapitel 1, Modul 3)
from colors import *
CHIP = "🇩🇪 Aspekte B1+ · Kapitel 1"
D_ = lambda s: f"<span class='dat'>{s}</span>"
A_ = lambda s: f"<span class='akk'>{s}</span>"
BLOCKS = [
 {"kind": "rule", "title": "Wer kommt <b>zuerst</b>?", **c(ORANGE),
  "segs": ["Ich gebe dem Polizisten meinen Ausweis.", "Ich gebe ihn ihm.", "Warum ändert sich die Reihenfolge?"],
  "rows": [{"em": "👮", "l": f"Ich gebe {D_('dem Polizisten')} {A_('meinen Ausweis')}.", "at": 0},
           {"em": "🪪", "l": f"Ich gebe {A_('ihn')} {D_('ihm')}.", "at": 1}],
  "notes": [{"html": f"{D_('Dativ')} · {A_('Akkusativ')}", "at": 2}]},
 {"kind": "rule", "num": 1, "label": "Zwei Nomen", "badge": f"{D_('Dativ')} → {A_('Akkusativ')}", "badge_at": 1, **c(BLUE),
  "segs": ["Regel eins: zwei Nomen.", "Zuerst Dativ, dann Akkusativ.", "Ich gebe dem Polizisten meinen Ausweis.", "Ich schenke meiner Mutter Blumen."],
  "rows": [{"em": "👮", "l": f"Ich gebe {D_('dem Polizisten')} {A_('meinen Ausweis')}.", "at": 2},
           {"em": "💐", "l": f"Ich schenke {D_('meiner Mutter')} {A_('Blumen')}.", "at": 3}]},
 {"kind": "rule", "num": 2, "label": "Pronomen + Nomen", "badge": "Pronomen zuerst", "badge_at": 1, **c(GREEN),
  "segs": ["Regel zwei: ein Pronomen und ein Nomen.", "Das Pronomen kommt zuerst.", "Ich gebe ihm meinen Ausweis.", "Ich gebe ihn dem Polizisten."],
  "rows": [{"em": "👮", "l": f"Ich gebe {D_('ihm')} {A_('meinen Ausweis')}.", "at": 2},
           {"em": "🪪", "l": f"Ich gebe {A_('ihn')} {D_('dem Polizisten')}.", "at": 3}],
  "notes": [{"html": "Pronomen = kurz → nach vorne", "at": 3}]},
 {"kind": "rule", "num": 3, "label": "Zwei Pronomen", "badge": f"{A_('Akkusativ')} → {D_('Dativ')}", "badge_at": 1, **c(PURPLE),
  "segs": ["Regel drei: zwei Pronomen.", "Jetzt zuerst Akkusativ, dann Dativ.", "Ich gebe ihn ihm.", "Ich zeige es dir."],
  "rows": [{"em": "🪪", "l": f"Ich gebe {A_('ihn')} {D_('ihm')}.", "at": 2}, {"em": "📱", "l": f"Ich zeige {A_('es')} {D_('dir')}.", "at": 3}]},
 {"kind": "rule", "num": 4, "label": "Also:", **c(RED),
  "segs": ["Also, noch einmal:", "Zwei Nomen: Dativ zuerst.", "Pronomen immer nach vorne.", "Zwei Pronomen: Akkusativ zuerst."],
  "rows": [{"em": "1️⃣", "l": f"2 Nomen: {D_('Dativ')} → {A_('Akkusativ')}", "at": 1},
           {"em": "2️⃣", "l": "Pronomen + Nomen: <b>Pronomen zuerst</b>", "at": 2},
           {"em": "3️⃣", "l": f"2 Pronomen: {A_('Akkusativ')} → {D_('Dativ')}", "at": 3}]},
 {"kind": "quiz", "title": "Richtig oder falsch?", **c(ORANGE),
  "intro": ["Und jetzt der Test!", "Richtig oder falsch?"],
  "q_say": ["Eins: Ich erkläre die Regel dir.", "Zwei: Ich schenke meinem Vater ein Buch.", "Drei: Ich zeige es ihr."],
  "a_say": ["Eins ist falsch. Richtig ist: Ich erkläre dir die Regel.", "Zwei ist richtig.", "Drei ist richtig."],
  "items": [{"em": "❓", "q": "Ich erkläre die Regel dir.", "a": f"❌ Ich erkläre {D_('dir')} {A_('die Regel')}."},
            {"em": "❓", "q": "Ich schenke meinem Vater ein Buch.", "a": "✅ richtig"},
            {"em": "❓", "q": "Ich zeige es ihr.", "a": "✅ richtig"}]},
]
CTA = {"say": "Wie viele hast du richtig? Schreib es in die Kommentare!", "t1": "Wie viele hast du <b>richtig</b>? 🏆",
       "t2": "Schreib es in die Kommentare!", "chips": ["0/3", "2/3", "3/3 🔥"]}
