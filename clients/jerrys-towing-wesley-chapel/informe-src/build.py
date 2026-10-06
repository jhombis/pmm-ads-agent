import json, re, sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from build_common import *
sys.path.insert(0, str(ROOT / 'scripts'))
from informe_html import logo_uri
from html import escape

URL_ES = sys.argv[1] if len(sys.argv) > 1 else 'https://claude.ai/artifact/PENDIENTE-ES'
URL_EN = sys.argv[2] if len(sys.argv) > 2 else 'https://claude.ai/artifact/PENDIENTE-EN'
BASE = (ROOT / 'knowledge/estilo-informes/plantilla.html').read_text().replace('{{PMM_LOGO}}', logo_uri())
J = lambda x: json.dumps(x, ensure_ascii=False)

MES = {'es': ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'],
       'en': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}
def dm(d, lang):
    y, m, dd = d.split('-')
    return f'{dd}-{MES[lang][int(m)-1]}' if lang == 'es' else f'{MES[lang][int(m)-1]} {int(dd)}'

def daily_rows(lang):
    out = []
    for d, imp, clk, cost, conv, isv in DAILY:
        cpc = f'${cost/clk:.2f}' if clk else '—'
        isx = '<10%' if isv < .1 else f'{isv*100:.0f}%'
        out.append(f'<tr><td style="white-space:nowrap">{dm(d, lang)}</td><td class="r">{imp}</td><td class="r">{clk}</td><td class="r">${cost:.2f}</td><td class="r">{cpc}</td><td class="r">{escape(isx)}</td><td class="r">—</td><td class="r">—</td></tr>')
    lab = 'Search 7 días (agregado)' if lang == 'es' else 'Search 7 days (aggregate)'
    out.append(f'<tr><td><b>{lab}</b></td><td class="r"><b>223</b></td><td class="r"><b>23</b></td><td class="r"><b>$174.54</b></td><td class="r"><b>$7.59</b></td><td class="r"><b>30.1%</b></td><td class="r"><b>45.1%</b></td><td class="r"><b>25.5%</b></td></tr>')
    lab = 'P. Max 5 días (desde 01-oct)' if lang == 'es' else 'P. Max 5 days (since Oct 1)'
    out.append(f'<tr><td><b>{lab}</b></td><td class="r">1,143</td><td class="r">16</td><td class="r">$22.51</td><td class="r">$1.41</td><td class="r">—</td><td class="r">—</td><td class="r">—</td></tr>')
    return '\n            '.join(out)

def serps():
    return '\n'.join(f'''      <div class="serp">
        <div class="spon">Sponsored · {escape(g)}</div>
        <div class="url">jerrystowingservice.com</div>
        <div class="hl">{escape(a)} | {escape(b)} | {escape(c)}</div>
        <div class="ds">{escape(d1)} {escape(d2)}</div>
      </div>''' for g, a, b, c, d1, d2 in SERP)

from content_es import ES
from content_en import EN

def build(lang, T):
    s = BASE
    s = s.replace('<title>{{Cliente}} · {{Tipo de informe}}</title>', f"<title>{T['title']}</title>")
    s = re.sub(r'\n<!--\n  PLANTILLA DEL INFORME PMM.*?-->', '', s, flags=re.S)
    body = T['body'].replace('@@DAILY@@', daily_rows(lang)).replace('@@SERP@@', serps()) \
        .replace('@@URL_OTHER@@', URL_EN if lang == 'es' else URL_ES).replace('@@LOGO@@', logo_uri())
    body = body.replace('\n      <div>\n', '\n      <div style="min-width:0">\n').replace('\n      <div class="callout">', '\n      <div class="callout" style="min-width:0">')
    i0 = s.index('<div class="wrap">'); i1 = s.rindex('<script>')
    s = s[:i0] + body + '\n\n' + s[i1:]
    D = T['data']
    reps = [
        (r"  const steps = \[\n.*?\n  \];", f"  const steps = {J(D['steps'])};"),
        (r"const start = new Date\('[^']*'\), end = new Date\('[^']*'\);", "const start = new Date('2026-09-29'), end = new Date('2027-01-31');"),
        (r"const months = \[[^\]]*\];", "const months = ['2026-10-01','2026-11-01','2026-12-01','2027-01-01'];"),
        (r"const mname = \{.*?\};", f"const mname = {J(D['mname'])};"),
        (r"  const rows = \[\n.*?\n  \];", f"  const rows = {J(D['rows'])};"),
        (r"const today = '[^']*';", "const today = '2026-10-06';"),
        (r"  const phases = \[\n.*?\n  \];", f"  const phases = {J(D['phases'])};"),
        (r"const ACTIVE = '[^']*';\n  const ags = \[\n.*?\n  \];", f"const ACTIVE = 'F1';\n  const ags = {J(D['ags'])};"),
        (r"  const h1 = \[\n.*?\n  \];", f"  const h1 = {J(D['h1'])};"),
        (r"const pool = \[[^\]]*\];", f"const pool = {J(POOL)};"),
        (r"const descs = \[[^\]]*\];", f"const descs = {J(DESCS_TNM)};"),
        (r"const negs = \[\[.*?\]\];", f"const negs = {J(D['negs'])};"),
        (r"const rub = \[\[.*?\]\];", f"const rub = {J(D['rub'])};"),
        (r"  const CL = \[\n.*?\n  \];", f"  const CL = {J(D['CL'])};"),
        (r"const PHT = \{.*?\};", f"const PHT = {J(D['PHT'])};"),
        (r"const KEY = '[^']*';", f"const KEY = 'jerrys-filters-{lang}';"),
        (r"  const qs = \[\n.*?\n  \];", f"  const qs = {J(D['qs'])};"),
        (r"const msg = `[^`]*`;", f"const msg = {J(D['msg'])};"),
    ]
    for pat, new in reps:
        s2, n = re.subn(pat, lambda m: new, s, count=1, flags=re.S)
        assert n == 1, pat
        s = s2
    if lang == 'en':
        s = s.replace('<html lang="es">', '<html lang="en">')
        for a, b in T['renderer']:
            assert a in s, a
            s = s.replace(a, b)
    return s

for lang, T in (('es', ES), ('en', EN)):
    out = C / f'plan-{lang}.html'
    out.write_text(build(lang, T))
    print(out, len(out.read_text()))
