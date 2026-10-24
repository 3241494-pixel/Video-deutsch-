# Прив'язка слів тексту пісні до розпізнаних слів (difflib) + інтерполяція пропусків
import json, re, difflib
def norm(w): return re.sub(r"[^a-zäöüß]", "", w.lower())
lines, sec = [], None
for l in open("lyrics.txt").read().splitlines():
    l = l.strip()
    if not l: continue
    if l.startswith("["): sec = l.strip("[]"); continue
    toks = [t for t in l.split() if norm(t)]
    lines.append({"sec": sec, "text": l, "words": toks})
LW = [(i, j, norm(t)) for i, L in enumerate(lines) for j, t in enumerate(L["words"])]
R = json.load(open("vw2.json")); RN = [norm(w["word"]) for w in R]
sm = difflib.SequenceMatcher(None, [x[2] for x in LW], RN, autojunk=False)
T = [None] * len(LW)
for a, b, n in sm.get_matching_blocks():
    for k in range(n): T[a+k] = [R[b+k]["start"], R[b+k]["end"]]
# близькі за написанням (zieh/ziehe) у блоках replace
for tag, a1, a2, b1, b2 in sm.get_opcodes():
    if tag == "replace" and a2 - a1 == b2 - b1:
        for k in range(a2 - a1): T[a1+k] = [R[b1+k]["start"], R[b1+k]["end"]]
matched = sum(t is not None for t in T)
# інтерполяція
i = 0
while i < len(T):
    if T[i] is None:
        j = i
        while j < len(T) and T[j] is None: j += 1
        s = T[i-1][1] if i else 0.0; e = T[j][0] if j < len(T) else s + 0.5 * (j - i)
        step = (e - s) / (j - i)
        for k in range(i, j): T[k] = [round(s + step*(k-i), 3), round(s + step*(k-i+1), 3)]
        i = j
    else: i += 1
for (li, j, _), t in zip(LW, T): lines[li].setdefault("t", []).append(t)
# ремонт: велика пауза всередині рядка -> перше слово ближче до другого; слово не довше 1.2 с
for L in lines:
    t = L["t"]
    for k in range(len(t)): t[k][1] = min(t[k][1], t[k][0] + 1.2)
    if len(t) > 1 and t[1][0] - t[0][0] > 2.0: t[0] = [round(t[1][0] - 0.8, 3), round(t[1][0] - 0.1, 3)]
    for k in range(2, len(t) - 1):
        if t[k][0] - t[k-1][0] > 2.0:  # хибний збіг: розтягуємо рівномірно між сусідами
            a, b = t[k-1][1], t[k+1][0]; t[k] = [round(a + .05, 3), round(min(b, a + .6), 3)]
# ручні правки з окремого розпізнавання фрагмента 222–240 с
FIX = {55: [223.2, 224.0, 224.1, 224.5, 224.9, 225.0, 225.3], 56: [225.9, 227.1, 227.2, 227.6, 227.9, 228.0, 228.3]}
for k, st in FIX.items():
    lines[k]["t"] = [[a, round(min(a + .6, b - .02), 3)] for a, b in zip(st, st[1:] + [st[-1] + .7])]
for L in lines: L["start"], L["end"] = L["t"][0][0], L["t"][-1][1]
json.dump(lines, open("lines.json", "w"), ensure_ascii=False, indent=0)
print("matched", matched, "of", len(LW))
for k, L in enumerate(lines): print(k, L["sec"][:12], round(L["start"],1), round(L["end"],1), round(L["end"]-L["start"],1))
