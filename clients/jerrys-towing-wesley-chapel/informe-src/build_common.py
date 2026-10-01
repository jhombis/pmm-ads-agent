"""Datos compartidos ES/EN del plan de Jerry's (todo sale de clients/jerrys-towing-wesley-chapel/).

Regenerar: python3 clients/jerrys-towing-wesley-chapel/informe-src/build.py <url-es> <url-en>
(URLs en el front matter de roadmap.md) y luego scripts/informe_html.py check."""
import csv, json, re
from pathlib import Path

ROOT = Path('/home/user/pmm-ads-agent')
C = ROOT / 'clients/jerrys-towing-wesley-chapel'
SCR = Path(__file__).resolve().parent

# Serie diaria (data/2026-09-29-campaign-daily.csv) + IS diario de Windsor (log 2026-09-29)
IS = {'2026-09-15': .2206, '2026-09-16': .2155, '2026-09-17': .1441, '2026-09-18': .1308, '2026-09-19': .2346,
      '2026-09-20': .1264, '2026-09-21': .1772, '2026-09-22': .2901, '2026-09-23': .1562, '2026-09-24': .0999,
      '2026-09-25': .3293, '2026-09-26': .2222, '2026-09-27': .1731, '2026-09-28': .2647}
DAILY = []
for r in csv.DictReader(open(C / 'data/2026-09-29-campaign-daily.csv')):
    if r['fecha'] in IS:
        DAILY.append((r['fecha'], int(r['impresiones']), int(r['clics']), float(r['costo']), float(r['conversiones']), IS[r['fecha']]))

# Anuncios (data/ads-search.md): variante A de cada grupo
ADS = (C / 'data/ads-search.md').read_text()
def rsa_a(group):
    blk = ADS.split(f'## Ad group: {group}')[1].split('## Ad group:')[0]
    a = blk.split('### RSA A')[1].split('### RSA B')[0]
    hl = re.findall(r'^\| \d+ \| (.+?) \| \d+ \|', a, re.M)
    ds = re.findall(r'^- D\d \(\d+\): (.+)$', blk, re.M)
    return hl, ds

GROUPS = ['Towing Near Me', 'Cheap Towing', 'Roadside Assistance', 'Wesley Chapel Towing']
PINS = {'Towing Near Me': ['Towing Near You 24/7', 'Tow Truck Near You', 'Local Towing Company'],
        'Cheap Towing': ['Affordable Towing Near You', 'Low-Cost Local Towing', 'Upfront Towing Prices'],
        'Roadside Assistance': ['Roadside Assistance 24/7', 'Jump Starts & Tire Changes', 'Out of Gas? We Deliver'],
        'Wesley Chapel Towing': ['Towing in Wesley Chapel', 'Wesley Chapel Tow Truck', 'Pasco County Towing'],
        'Grúa ES': ['Grúa Cerca de Usted 24/7', 'Servicio de Grúa Local', 'Grúa en Wesley Chapel']}
POOL = ['Available 24/7 - Call Now', 'Fast Local Dispatch', 'Serving Wesley Chapel & Pasco', "Stuck? We're On The Way",
        'Towing Day or Night', 'Free Quote - Upfront Pricing', 'No Hidden Fees', 'Honest, Upfront Prices',
        'Get a Free Towing Quote', 'Local & Family-Owned', 'Honest. Local. Reliable.', 'You Choose Where It Goes',
        'Light & Medium-Duty Towing', 'Safe, Careful Towing', "Jerry's Towing Service"]
for p in POOL:
    assert p in ADS, p
SERP = []
for g in GROUPS:
    hl, ds = rsa_a(g)
    SERP.append((g, hl[0], hl[1], hl[2], ds[0], ds[1]))
DESCS_TNM = rsa_a('Towing Near Me')[1]

# Negativas por bloque (data/negatives-nicho.txt)
NEG = {}
sec = None
for line in (C / 'data/negatives-nicho.txt').read_text().splitlines():
    if line.startswith('## '):
        sec = line[3:]
        NEG[sec] = []
    elif sec and line.strip() and not line.startswith('#'):
        NEG[sec].append(line.strip())
NEG.pop('EXCEPCIONES a la lista universal para esta cuenta (NO aplicar estas universales)', None)
SHORT = {'Nicho towing — compra/empleo/equipo (no es servicio)': 'compra', 'Nicho towing — vehículo remolcado por terceros / impound': 'impound',
         'Servicios públicos / aseguradoras / clubes': 'publico', 'Servicios que no ofrece (confirmar con cliente)': 'nosvc',
         'Competidores y terceros (estándar PMM #5) — NO incluir "jerry"/"jerrys"': 'comp',
         'Fuera de área (parche; lo de fondo es geo = Presencia + radio 20 mi)': 'area'}
NEGC = {SHORT[k]: len(v) for k, v in NEG.items()}
NEG_TOTAL = sum(NEGC.values())

# Validación: ninguna negativa (frase) dentro de una keyword que se queda activa
KW = [r for r in csv.DictReader(open(C / 'data/keywords.csv'))
      if not any(x in r['accion'] for x in ('PAUSAR', 'pausar', 'descartar', 'no:', 'condicional: '))]
def words(s): return ' ' + re.sub(r'[^a-z0-9ñáéíóú$&\' ]', ' ', s.lower()) + ' '
CLASH = [(n, k['keyword']) for v in NEG.values() for n in v for k in KW if words(n).strip() and words(n) in words(k['keyword'])]
KW_ACTIVE = len(KW)

if __name__ == '__main__':
    print(len(DAILY), 'días'); print(SERP[0]); print(NEGC, NEG_TOTAL); print('choques:', CLASH, 'kw activas', KW_ACTIVE)

# Lista universal PMM (knowledge/negativas-universales.md), sin las excepciones de este cliente
UNI = []
for line in (ROOT / 'knowledge/negativas-universales.md').read_text().splitlines():
    if line and not line.startswith('#') and ',' in line:
        UNI += [t.strip().strip('"') for t in line.split(',') if t.strip()]
EXC = ['cheapest', 'insurance claim', 'county']
UNI = [u for u in UNI if u not in EXC]
UNI_CLASH = [(n, k['keyword']) for n in UNI for k in KW if words(n) in words(k['keyword'])]
if __name__ == '__main__':
    print('universal', len(UNI), 'choques universal:', UNI_CLASH)
