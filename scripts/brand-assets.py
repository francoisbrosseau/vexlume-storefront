"""Rebuild outlined RITUWILD identity assets (development tool: fonttools)."""
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'dist/assets'
FONT = TTFont('/usr/share/fonts/opentype/urw-base35/NimbusRoman-Regular.otf')
GLYPHS = FONT.getGlyphSet()
CMAP = FONT.getBestCmap()

def lettering(word, x, baseline, size, tracking=100):
    scale = size / FONT['head'].unitsPerEm
    parts=[]
    for ch in word:
        name=CMAP[ord(ch)]
        pen=SVGPathPen(GLYPHS)
        GLYPHS[name].draw(TransformPen(pen,(scale,0,0,-scale,x,baseline)))
        parts.append('<path d="'+pen.getCommands()+'"/>')
        x+=(FONT['hmtx'][name][0]+tracking)*scale
    return ''.join(parts), x

# The Return & Rise seal: an open daily orbit, hand-drawn R and rooted W.
SEAL='''<g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M94 37A45 45 0 1 0 103 67" stroke-width="1.7"/><path d="M94 37l7-17m-7 17 16-7" stroke-width="1.7"/><path d="M39 76V30h19c23 0 23 29 0 29H40m17 0 21 22" stroke-width="3.2"/><path d="M29 68l10 21 13-21 12 21 14-29" stroke-width="2.7"/><path d="M33 30h13m-13 46h13" stroke-width="1.5"/></g>'''

def svg(body, view, color):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view}" color="{color}" fill="{color}" role="img" aria-label="RITUWILD — routines for a life of your own"><title>RITUWILD — Return &amp; Rise</title>{body}</svg>'

word,end=lettering('RITUWILD',0,76,92,120)
for suffix,color in [('', '#171B1B'),('-light','#F2EDE4'),('-gold','#B99B67')]:
    (ASSETS/f'wordmark{suffix}.svg').write_text(svg(word, f'0 0 {end:.1f} 94',color))
    body=f'<g transform="translate(222 0) scale(.87)">{SEAL}</g><g transform="translate(0 108)">{word}</g>'
    (ASSETS/f'logo{suffix}.svg').write_text(svg(body,f'0 0 {end:.1f} 208',color))
(ASSETS/'symbol.svg').write_text(svg(SEAL,'0 0 120 120','#B99B67'))
(ASSETS/'mark.svg').write_text(svg('<rect width="120" height="120" rx="60" fill="#171B1B"/>'+SEAL,'0 0 120 120','#D2B47E'))
social=f'<rect width="1200" height="630" fill="#171B1B"/><path d="M60 60h1080v510H60Z" fill="none" stroke="#B99B67" opacity=".5"/><g transform="translate(530 85) scale(1.15)" color="#B99B67">{SEAL}</g><g transform="translate(215 220) scale(1.4)" fill="#F2EDE4">{word}</g><text x="600" y="440" text-anchor="middle" fill="#D2B47E" font-family="Arial,sans-serif" font-size="17" letter-spacing="4">SMALL RITUALS. A LIFE OF YOUR OWN.</text>'
(ASSETS/'social.svg').write_text(svg(social,'0 0 1200 630','#B99B67'))
print('Generated outlined wordmarks, stacked logos, Return & Rise seal, favicon and social card.')
