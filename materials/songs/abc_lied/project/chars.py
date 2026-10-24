# Власні прості SVG-персонажі для кожної літери (viewBox 0 0 400 400), м'який дитячий стиль
OUT = "#3B2F2F"
def eye(x, y, r=16):
    return (f'<g class="eye"><ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*1.15:.0f}" fill="#fff" stroke="{OUT}" stroke-width="5"/>'
            f'<circle cx="{x+2}" cy="{y+3}" r="{r*.55:.0f}" fill="{OUT}"/><circle cx="{x+r*.35+2:.0f}" cy="{y-r*.2:.0f}" r="{r*.22:.0f}" fill="#fff"/></g>')
def eyes(x1, x2, y, r=16): return eye(x1, y, r) + eye(x2, y, r)
def cheeks(x1, x2, y, r=14): return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FF8FA3" opacity=".55"/>' for x in (x1, x2) if x)
def smile(x, y, w=40, h=18): return f'<path d="M{x-w/2},{y} Q{x},{y+h} {x+w/2},{y}" fill="none" stroke="{OUT}" stroke-width="6" stroke-linecap="round"/>'
S = f'stroke="{OUT}" stroke-width="6" stroke-linejoin="round"'

C = {}
C["apfel"] = f'''<path d="M200,110 C130,70 60,120 70,210 C80,300 140,350 200,330 C260,350 320,300 330,210 C340,120 270,70 200,110Z" fill="#FF5A5F" {S}/>
<path d="M200,112 C198,85 205,65 215,50" fill="none" {S}/><path d="M212,70 C240,40 285,50 290,60 C270,85 235,90 212,70Z" fill="#69DB7C" {S}/>
<ellipse cx="135" cy="170" rx="18" ry="30" fill="#fff" opacity=".45"/>{eyes(165,235,215)}{cheeks(140,260,250)}{smile(200,255)}'''
C["biene"] = f'''<ellipse cx="160" cy="130" rx="55" ry="40" fill="#E7F5FF" opacity=".9" {S} transform="rotate(-25 160 130)" class="wing"/>
<ellipse cx="245" cy="130" rx="55" ry="40" fill="#E7F5FF" opacity=".9" {S} transform="rotate(25 245 130)" class="wing"/>
<ellipse cx="200" cy="230" rx="120" ry="95" fill="#FFD43B" {S}/>
<path d="M160,145 C150,200 150,270 165,318" fill="none" stroke="{OUT}" stroke-width="26"/><path d="M240,145 C250,200 250,270 235,318" fill="none" stroke="{OUT}" stroke-width="26"/>
<ellipse cx="200" cy="230" rx="120" ry="95" fill="none" {S}/>
<path d="M175,140 C165,105 150,95 140,90" fill="none" {S}/><path d="M225,140 C235,105 250,95 260,90" fill="none" {S}/><circle cx="138" cy="88" r="10" fill="{OUT}"/><circle cx="262" cy="88" r="10" fill="{OUT}"/>
<path d="M320,230 L350,230" {S}/>{eyes(110,200,215,15)}{smile(150,262,36,14)}{cheeks(85,215,250,11)}'''
C["clown"] = f'''<path d="M120,140 L200,20 L280,140Z" fill="#748FFC" {S}/><circle cx="160" cy="95" r="11" fill="#FFD43B"/><circle cx="225" cy="70" r="9" fill="#FF6B6B"/><circle cx="200" cy="22" r="20" fill="#FF922B" {S}/>
<circle cx="95" cy="200" r="45" fill="#FF922B" {S}/><circle cx="305" cy="200" r="45" fill="#FF922B" {S}/>
<circle cx="200" cy="220" r="110" fill="#FFE8CC" {S}/>{eyes(160,240,195,17)}
<circle cx="200" cy="240" r="26" fill="#FF3B3B" {S}/><path d="M140,275 Q200,330 260,275" fill="#fff" {S}/><path d="M150,282 Q200,318 250,282" fill="none" stroke="#FF6B6B" stroke-width="6"/>{cheeks(130,270,255,16)}
<path d="M170,330 L120,375 L170,370 L200,345 L230,370 L280,375 L230,330Z" fill="#FFD43B" {S}/>'''
C["dino"] = f'''<path d="M300,300 C360,300 385,250 395,220 C360,250 330,255 300,250Z" fill="#69DB7C" {S}/>
<path d="M110,90 L130,60 L150,95 L170,70 L185,110 L210,95 L215,140" fill="#FFA94D" {S}/>
<path d="M90,200 C70,120 110,70 170,75 C235,80 250,140 230,180 C300,180 330,240 310,300 C290,350 150,355 120,320 C100,290 105,240 90,200Z" fill="#69DB7C" {S}/>
<ellipse cx="200" cy="270" rx="55" ry="45" fill="#D3F9D8"/><rect x="140" y="320" width="40" height="50" rx="16" fill="#69DB7C" {S}/><rect x="235" y="320" width="40" height="50" rx="16" fill="#69DB7C" {S}/>
{eyes(140,195,140,16)}{smile(165,185,50,20)}{cheeks(120,215,175,11)}'''
C["elefant"] = f'''<ellipse cx="95" cy="190" rx="75" ry="90" fill="#B4C6E7" {S}/><ellipse cx="305" cy="190" rx="75" ry="90" fill="#B4C6E7" {S}/>
<ellipse cx="95" cy="190" rx="45" ry="58" fill="#FFC9D6"/><ellipse cx="305" cy="190" rx="45" ry="58" fill="#FFC9D6"/>
<circle cx="200" cy="190" r="105" fill="#C5D5F0" {S}/>
<path d="M185,230 C175,290 185,340 230,345 C255,346 262,322 245,318 C220,320 215,300 220,230Z" fill="#C5D5F0" {S}/>
{eyes(160,240,170,15)}{cheeks(140,262,220,14)}'''
C["fuchs"] = f'''<path d="M95,170 L80,50 L175,120Z" fill="#FF922B" {S}/><path d="M305,170 L320,50 L225,120Z" fill="#FF922B" {S}/>
<path d="M100,105 L95,80 L135,110Z" fill="#fff"/><path d="M300,105 L305,80 L265,110Z" fill="#fff"/>
<path d="M70,170 C90,110 310,110 330,170 C330,240 260,310 200,330 C140,310 70,240 70,170Z" fill="#FF922B" {S}/>
<path d="M200,330 C160,315 115,270 115,230 C150,240 180,260 200,290 C220,260 250,240 285,230 C285,270 240,315 200,330Z" fill="#fff"/>
<circle cx="200" cy="300" r="16" fill="{OUT}"/>{eyes(160,240,200,15)}{cheeks(130,270,240,12)}'''
C["giraffe"] = f'''<rect x="165" y="190" width="70" height="200" rx="30" fill="#FFD43B" {S}/>
<circle cx="190" cy="250" r="12" fill="#E8890C"/><circle cx="215" cy="300" r="14" fill="#E8890C"/><circle cx="188" cy="345" r="11" fill="#E8890C"/>
<path d="M165,70 L160,30" {S}/><path d="M235,70 L240,30" {S}/><circle cx="160" cy="28" r="13" fill="#E8890C" {S}/><circle cx="240" cy="28" r="13" fill="#E8890C" {S}/>
<ellipse cx="125" cy="100" rx="35" ry="17" fill="#FFD43B" {S} transform="rotate(-20 125 100)"/><ellipse cx="275" cy="100" rx="35" ry="17" fill="#FFD43B" {S} transform="rotate(20 275 100)"/>
<ellipse cx="200" cy="140" rx="85" ry="80" fill="#FFD43B" {S}/><ellipse cx="200" cy="185" rx="60" ry="40" fill="#FFE8A3" {S}/>
<circle cx="180" cy="185" r="6" fill="{OUT}"/><circle cx="220" cy="185" r="6" fill="{OUT}"/>{eyes(165,235,125,15)}{cheeks(140,260,160,11)}'''
C["hund"] = f'''<ellipse cx="95" cy="175" rx="45" ry="90" fill="#A0522D" {S} transform="rotate(15 95 175)" class="ear"/>
<ellipse cx="305" cy="175" rx="45" ry="90" fill="#A0522D" {S} transform="rotate(-15 305 175)"/>
<circle cx="200" cy="190" r="110" fill="#E3A869" {S}/><ellipse cx="200" cy="245" rx="65" ry="50" fill="#FFF1E0" {S}/>
<ellipse cx="200" cy="220" rx="24" ry="17" fill="{OUT}"/><path d="M175,262 Q200,280 225,262" fill="none" {S}/>
<path d="M200,268 C190,300 210,310 215,290" fill="#FF6B81" {S}/>{eyes(158,242,170,16)}{cheeks(130,270,230,12)}'''
C["igel"] = f'''<path d="M60,280 L40,220 L80,225 L60,160 L105,180 L100,115 L145,150 L160,90 L190,140 L220,85 L240,140 L275,100 L280,160 L325,140 L310,200 L355,205 L325,250 L360,280Z" fill="#8D6E63" {S}/>
<ellipse cx="230" cy="270" rx="120" ry="75" fill="#D7B899" {S}/><circle cx="345" cy="270" r="14" fill="{OUT}"/>
{eye(290,240,14)}{cheeks(275,0,285,12)}{smile(300,290,40,14)}<rect x="160" y="330" width="34" height="34" rx="14" fill="#D7B899" {S}/><rect x="260" y="330" width="34" height="34" rx="14" fill="#D7B899" {S}/>'''
C["jacke"] = f'''<path d="M140,70 L200,95 L260,70 L335,110 L370,250 L320,265 L305,190 L300,350 L100,350 L95,190 L80,265 L30,250 L65,110Z" fill="#FA5252" {S}/>
<path d="M200,95 L200,350" {S}/><path d="M140,70 L175,140 L200,95 L225,140 L260,70" fill="#FFC9C9" {S}/>
<circle cx="180" cy="190" r="8" fill="{OUT}"/><circle cx="180" cy="250" r="8" fill="{OUT}"/><circle cx="180" cy="310" r="8" fill="{OUT}"/>
<rect x="225" y="240" width="55" height="45" rx="10" fill="#FF8787" {S}/>'''
C["katze"] = f'''<path d="M300,300 C370,290 370,200 330,170" fill="none" stroke="{OUT}" stroke-width="30" stroke-linecap="round"/><path d="M300,300 C370,290 370,200 330,170" fill="none" stroke="#B197FC" stroke-width="18" stroke-linecap="round" class="tail"/>
<path d="M95,150 L95,45 L180,105Z" fill="#B197FC" {S}/><path d="M305,150 L305,45 L220,105Z" fill="#B197FC" {S}/><path d="M110,120 L110,75 L150,105Z" fill="#FFC9D6"/><path d="M290,120 L290,75 L250,105Z" fill="#FFC9D6"/>
<ellipse cx="200" cy="200" rx="125" ry="105" fill="#B197FC" {S}/>
<path d="M188,230 L212,230 L200,245Z" fill="#FF6B81" {S}/><path d="M170,262 Q185,275 200,250 Q215,275 230,262" fill="none" {S}/>
<path d="M95,225 L35,215 M95,245 L40,255 M305,225 L365,215 M305,245 L360,255" {S}/>{eyes(150,250,190,18)}{cheeks(125,275,240,13)}'''
C["lampe"] = f'''<rect x="140" y="330" width="120" height="30" rx="14" fill="#748FFC" {S}/><rect x="188" y="200" width="24" height="135" fill="#BAC8FF" {S}/>
<path d="M200,170 L330,170" stroke="#FFE066" stroke-width="0"/><g class="glow" opacity=".7"><circle cx="200" cy="200" r="120" fill="#FFF3BF"/></g>
<path d="M110,200 L150,70 L250,70 L290,200Z" fill="#FFD43B" {S}/>{eyes(175,225,140,13)}{smile(200,170,34,12)}'''
C["maus"] = f'''<path d="M300,290 C360,300 380,250 360,220" fill="none" stroke="#FF8FA3" stroke-width="10" stroke-linecap="round"/>
<circle cx="110" cy="110" r="70" fill="#CED4DA" {S}/><circle cx="290" cy="110" r="70" fill="#CED4DA" {S}/><circle cx="110" cy="110" r="42" fill="#FFC9D6"/><circle cx="290" cy="110" r="42" fill="#FFC9D6"/>
<ellipse cx="200" cy="230" rx="115" ry="100" fill="#DEE2E6" {S}/><circle cx="200" cy="255" r="15" fill="#FF6B81" {S}/>
<path d="M110,250 L50,240 M110,270 L55,285 M290,250 L350,240 M290,270 L345,285" stroke="{OUT}" stroke-width="5"/>{smile(200,285,36,14)}{eyes(160,240,215,16)}'''
C["nudel"] = f'''<path d="M60,220 L340,220 C340,320 280,360 200,360 C120,360 60,320 60,220Z" fill="#4DABF7" {S}/>
<path d="M90,220 C80,160 120,150 130,190 C140,130 180,130 185,180 C200,120 240,130 240,180 C260,130 300,150 290,190 C320,160 330,200 310,220Z" fill="#FFD43B" {S}/>
<path d="M120,200 C150,170 180,210 210,180 C240,160 260,200 290,190" fill="none" stroke="#F59F00" stroke-width="6"/>
<circle cx="230" cy="175" r="16" fill="#FA5252" {S}/>{eyes(160,240,275,15)}{smile(200,315,40,16)}{cheeks(120,280,305,12)}'''
C["obst"] = f'''<path d="M70,230 L330,230 L300,350 L100,350Z" fill="#E8590C" {S}/><path d="M85,260 L315,260 M95,300 L305,300" stroke="#C2410C" stroke-width="6"/>
<circle cx="140" cy="190" r="55" fill="#FF922B" {S}/><path d="M220,120 C200,170 220,230 270,240 C300,245 320,220 300,215 C260,210 240,170 250,120Z" fill="#FFE066" {S}/>
<circle cx="285" cy="185" r="22" fill="#9775FA" {S}/><circle cx="315" cy="200" r="22" fill="#9775FA" {S}/><circle cx="295" cy="220" r="22" fill="#9775FA" {S}/>
<circle cx="200" cy="200" r="40" fill="#FF5A5F" {S}/>{eyes(122,158,185,10)}{smile(140,210,24,10)}'''
C["pinguin"] = f'''<ellipse cx="200" cy="215" rx="115" ry="140" fill="#343A40" {S}/><ellipse cx="200" cy="245" rx="80" ry="105" fill="#fff" {S}/>
<path d="M90,200 C50,230 50,280 70,300 C90,270 100,250 100,230Z" fill="#343A40" {S} class="flap"/><path d="M310,200 C350,230 350,280 330,300 C310,270 300,250 300,230Z" fill="#343A40" {S}/>
<path d="M175,175 L225,175 L200,205Z" fill="#FF922B" {S}/>{eyes(165,235,140,15)}{cheeks(145,255,200,12)}
<ellipse cx="160" cy="360" rx="35" ry="15" fill="#FF922B" {S}/><ellipse cx="240" cy="360" rx="35" ry="15" fill="#FF922B" {S}/>'''
C["qualle"] = f'''<g class="tent"><path d="M120,230 C100,280 140,300 115,360" fill="none" stroke="#F783AC" stroke-width="12" stroke-linecap="round"/><path d="M170,240 C150,290 190,310 165,370" fill="none" stroke="#F783AC" stroke-width="12" stroke-linecap="round"/>
<path d="M230,240 C250,290 210,310 235,370" fill="none" stroke="#F783AC" stroke-width="12" stroke-linecap="round"/><path d="M280,230 C300,280 260,300 285,360" fill="none" stroke="#F783AC" stroke-width="12" stroke-linecap="round"/></g>
<path d="M70,230 C70,120 130,70 200,70 C270,70 330,120 330,230 C300,250 280,215 250,240 C225,215 175,215 150,240 C120,215 100,250 70,230Z" fill="#FCC2D7" {S}/>
<ellipse cx="150" cy="120" rx="25" ry="15" fill="#fff" opacity=".6"/>{eyes(165,235,165,15)}{smile(200,195,36,14)}{cheeks(135,265,195,12)}'''
C["rakete"] = f'''<g class="flame"><path d="M165,300 C160,350 185,380 200,395 C215,380 240,350 235,300Z" fill="#FF922B"/><path d="M180,300 C180,340 195,360 200,370 C205,360 220,340 220,300Z" fill="#FFE066"/></g>
<path d="M140,240 L90,300 L150,290Z" fill="#FA5252" {S}/><path d="M260,240 L310,300 L250,290Z" fill="#FA5252" {S}/>
<path d="M200,30 C260,80 270,200 255,300 L145,300 C130,200 140,80 200,30Z" fill="#F1F3F5" {S}/><path d="M200,30 C230,55 245,85 252,110 L148,110 C155,85 170,55 200,30Z" fill="#FA5252" {S}/>
<circle cx="200" cy="175" r="38" fill="#74C0FC" {S}/>{eyes(186,214,172,9)}'''
C["sonne"] = '<g class="rays">' + "".join(f'<path d="M200,200 L{200+175*__import__("math").cos(a*0.5236):.0f},{200+175*__import__("math").sin(a*0.5236):.0f}" stroke="#FFC107" stroke-width="26" stroke-linecap="round"/>' for a in range(12)) + f'''</g>
<circle cx="200" cy="200" r="115" fill="#FFD43B" {S}/>{eyes(160,240,180,16)}{cheeks(135,265,225,16)}<path d="M160,235 Q200,275 240,235" fill="#fff" {S}/>'''
C["tiger"] = f'''<circle cx="100" cy="100" r="42" fill="#FF922B" {S}/><circle cx="300" cy="100" r="42" fill="#FF922B" {S}/><circle cx="100" cy="100" r="20" fill="#FFF1E0"/><circle cx="300" cy="100" r="20" fill="#FFF1E0"/>
<ellipse cx="200" cy="205" rx="135" ry="120" fill="#FF922B" {S}/>
<path d="M200,88 L188,130 L212,130Z M80,180 L125,190 L85,205Z M320,180 L275,190 L315,205Z M75,240 L120,240 L85,258Z M325,240 L280,240 L315,258Z" fill="{OUT}"/>
<ellipse cx="200" cy="255" rx="75" ry="55" fill="#FFF1E0" {S}/><ellipse cx="200" cy="232" rx="22" ry="15" fill="#FF6B81" {S}/><path d="M170,275 Q185,290 200,250 Q215,290 230,275" fill="none" {S}/>{eyes(150,250,180,17)}'''
C["uhr"] = f'''<circle cx="110" cy="75" r="40" fill="#FFD43B" {S}/><circle cx="290" cy="75" r="40" fill="#FFD43B" {S}/>
<circle cx="200" cy="210" r="150" fill="#4DABF7" {S}/><circle cx="200" cy="210" r="120" fill="#fff" {S}/>
''' + "".join(f'<circle cx="{200+100*__import__("math").cos(a*0.5236):.0f}" cy="{210+100*__import__("math").sin(a*0.5236):.0f}" r="6" fill="{OUT}"/>' for a in range(12)) + f'''
<g class="hand"><path d="M200,210 L200,130" stroke="#FA5252" stroke-width="10" stroke-linecap="round"/></g><path d="M200,210 L255,210" stroke="{OUT}" stroke-width="10" stroke-linecap="round"/><circle cx="200" cy="210" r="12" fill="{OUT}"/>
{eyes(160,240,175,11)}{smile(200,255,40,14)}'''
C["vogel"] = f'''<path d="M320,200 L380,170 L370,230Z" fill="#4DABF7" {S}/><circle cx="200" cy="200" r="120" fill="#74C0FC" {S}/>
<ellipse cx="200" cy="250" rx="75" ry="55" fill="#E7F5FF"/><path d="M210,230 C260,200 320,230 300,280 C270,270 240,260 210,230Z" fill="#4DABF7" {S} class="wing"/>
<path d="M75,195 L35,210 L75,225Z" fill="#FFA94D" {S}/><path d="M190,85 C180,50 210,40 215,70 C230,45 250,60 230,88" fill="#4DABF7" {S}/>
{eyes(125,185,170,16)}{cheeks(110,200,215,11)}'''
C["wal"] = f'''<g class="spout"><path d="M200,90 C190,50 160,40 150,55 M200,90 C210,50 240,40 250,55 M200,90 L200,40" fill="none" stroke="#74C0FC" stroke-width="12" stroke-linecap="round"/></g>
<path d="M330,230 C370,180 395,170 395,210 C385,240 370,250 340,260 C370,280 380,300 370,320 C345,310 330,290 320,270Z" fill="#4C6EF5" {S}/>
<path d="M30,240 C30,150 120,105 210,110 C300,115 345,190 330,260 C315,320 240,345 160,340 C80,335 30,300 30,240Z" fill="#5C7CFA" {S}/>
<path d="M45,265 C80,310 250,320 320,270 C300,320 240,342 160,340 C90,335 55,305 45,265Z" fill="#DBE4FF"/>{eye(120,215,16)}{smile(110,265,50,16)}{cheeks(150,0,255,13)}'''
C["xylofon"] = "".join(f'<rect x="{50+i*55}" y="{110+i*15}" width="45" height="{220-i*30}" rx="10" fill="{c}" {S}/><circle cx="{72+i*55}" cy="{130+i*15}" r="5" fill="#fff"/>' for i, c in enumerate(["#FA5252","#FF922B","#FFD43B","#69DB7C","#4DABF7","#9775FA"])) + \
    f'''<path d="M40,330 L360,250" stroke="#A0522D" stroke-width="14" stroke-linecap="round"/><g class="stick"><path d="M300,40 L220,150" {S}/><circle cx="215" cy="158" r="18" fill="#FA5252" {S}/></g>'''
C["jojo"] = f'''<path d="M200,20 C200,80 200,110 200,140" fill="none" stroke="{OUT}" stroke-width="6"/><circle cx="200" cy="15" r="12" fill="#FA5252" {S}/>
<g class="yo"><circle cx="200" cy="230" r="110" fill="#F06595" {S}/><circle cx="200" cy="230" r="70" fill="#FFDEEB" {S}/><circle cx="200" cy="230" r="18" fill="#F06595" {S}/>
{eyes(165,235,215,12)}{smile(200,262,36,14)}</g>'''
C["zebra"] = f'''<path d="M110,95 L100,30 L150,80Z" fill="#fff" {S}/><path d="M290,95 L300,30 L250,80Z" fill="#fff" {S}/>
<path d="M150,60 C160,20 190,40 200,20 C210,40 240,20 250,60" fill="{OUT}"/>
<ellipse cx="200" cy="180" rx="110" ry="120" fill="#fff" {S}/>
<path d="M95,140 L150,150 L95,165Z M305,140 L250,150 L305,165Z M100,205 L140,210 L105,225Z M300,205 L260,210 L295,225Z M175,70 L200,110 L225,70Z" fill="{OUT}"/>
<ellipse cx="200" cy="275" rx="85" ry="65" fill="#ADB5BD" {S}/><ellipse cx="170" cy="275" rx="12" ry="9" fill="{OUT}"/><ellipse cx="230" cy="275" rx="12" ry="9" fill="{OUT}"/>
<path d="M170,310 Q200,325 230,310" fill="none" {S}/>{eyes(155,245,175,17)}'''
C["baer"] = f'''<circle cx="100" cy="100" r="50" fill="#A0522D" {S}/><circle cx="300" cy="100" r="50" fill="#A0522D" {S}/><circle cx="100" cy="100" r="25" fill="#E3A869"/><circle cx="300" cy="100" r="25" fill="#E3A869"/>
<circle cx="200" cy="210" r="135" fill="#A0522D" {S}/><ellipse cx="200" cy="265" rx="70" ry="55" fill="#E3A869" {S}/>
<ellipse cx="200" cy="240" rx="25" ry="17" fill="{OUT}"/><path d="M175,282 Q200,300 225,282" fill="none" {S}/>{eyes(155,245,180,16)}{cheeks(115,285,240,15)}'''
C["loewe"] = '<g class="mane">' + "".join(f'<circle cx="{200+130*__import__("math").cos(a*0.4488):.0f}" cy="{205+130*__import__("math").sin(a*0.4488):.0f}" r="52" fill="#E8590C" stroke="{OUT}" stroke-width="6"/>' for a in range(14)) + f'''</g>
<circle cx="200" cy="205" r="130" fill="#E8590C"/><circle cx="200" cy="210" r="110" fill="#FFC078" {S}/>
<ellipse cx="200" cy="255" rx="60" ry="45" fill="#FFE8CC" {S}/><path d="M180,235 L220,235 L200,255Z" fill="#A0522D" {S}/><path d="M170,275 Q185,290 200,262 Q215,290 230,275" fill="none" {S}/>{eyes(160,240,190,16)}{cheeks(130,270,240,12)}'''
C["tuer"] = f'''<rect x="95" y="30" width="210" height="350" rx="20" fill="#E8590C" {S}/><rect x="125" y="65" width="150" height="120" rx="12" fill="#FF922B" {S}/>
<rect x="125" y="215" width="150" height="130" rx="12" fill="#FF922B" {S}/><circle cx="270" cy="200" r="15" fill="#FFD43B" {S}/>
<path d="M155,105 L245,105" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity=".6"/>{eyes(170,230,250,14)}{smile(200,295,40,14)}'''
C["fuss"] = f'''<path d="M120,330 C80,320 80,260 110,220 C140,180 140,120 160,90 C185,60 240,70 250,110 C260,150 250,190 280,230 C310,270 330,320 290,345 C250,365 170,345 120,330Z" fill="#FFC9A8" {S}/>
<circle cx="175" cy="70" r="26" fill="#FFC9A8" {S}/><circle cx="225" cy="60" r="20" fill="#FFC9A8" {S}/><circle cx="262" cy="75" r="17" fill="#FFC9A8" {S}/><circle cx="290" cy="98" r="14" fill="#FFC9A8" {S}/><circle cx="140" cy="95" r="17" fill="#FFC9A8" {S}/>
{eyes(175,235,220,15)}{smile(205,275,44,16)}{cheeks(150,265,255,13)}'''
