"""Genera data/build-spec.json (entrada de scripts/build_campaign.py) desde strategy v4 + data/ y knowledge/.

Uso: python clients/pro-phase-electric/data/make_build_spec.py
"""
import csv, json, re, runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
C = ROOT / 'clients/pro-phase-electric'
HOME = 'https://prophaseelectricar.com/'

# Copy (headlines/descriptions/keywords/routing) de la estrategia
g = runpy.run_path(str(C / 'data/build_strategy.py'))  # genera ads-search-nwa.md y keywords.csv

# Universal PMM desde knowledge (hasta "Marcas de competidores"), sin términos que chocan con este cliente
EXCLUDE_UNIVERSAL = {'free',      # el sitio ofrece "Get a Free Quote"
                     'county',    # "electrician benton county" es búsqueda buena
                     'code'}      # "up to code" es lenguaje comercial del oficio
txt = (ROOT / 'knowledge/negativas-universales.md').read_text().split('## Marcas de competidores')[0]
universal = []
for line in txt.splitlines():
    if not line or line.startswith('#') or line.startswith('Aplicar') or line.startswith('(Ojo'):
        continue
    for t in re.findall(r'"[^"]+"|[^,]+', line):
        t = t.strip().strip('"').strip()
        if t and t.lower() not in EXCLUDE_UNIVERSAL and t not in universal:
            universal.append(t)

niche = []
for line in (C / 'data/negatives-nicho.txt').read_text().splitlines():
    if line.startswith('#') or '|' not in line:
        continue
    t, m = [x.strip() for x in line.split('|')[:2]]
    niche.append([t, m])

ad_groups = []
for ag in g['AG']:
    headlines = [{'text': ag['h1'][0], 'pin': 'HEADLINE_1'}] + [{'text': h} for h in g['SHARED_H'] + ag['hs']]
    ad_groups.append({
        'name': ag['name'],
        'status': 'ENABLED',
        'keywords': [[k, m] for k, m, _ in ag['kw']],
        'negatives_phrase': ag['neg'],
        'rsa': {'headlines': headlines, 'descriptions': [ag['d']] + g['SHARED_D'],
                'final_url': HOME, 'path1': 'Electrician', 'path2': 'NWA'},
    })

spec = {
    'customer_id': '7583011023',
    'campaign': {
        'name': 'Pro Phase Electric - Search NWA - $1500/mo. - 09/23/2026',
        'status': 'ENABLED',
        'daily_budget_usd': 27,
        'bidding': {'type': 'TARGET_SPEND', 'cpc_bid_ceiling_usd': 12},
        'geo_presence': [9057047, 9057115, 1013254],   # Benton County AR, Washington County AR, Huntsville AR
        'language': 1000,
        'schedule_account_tz': {'days': 'ALL', 'start_hour': 3, 'end_hour': 14},  # PT = 5–16 Arkansas
    },
    'shared_negative_lists': {
        'PMM Universal': [[t, 'PHRASE'] for t in universal],
        'pro-phase-electric nicho': niche,
    },
    'ad_groups': ad_groups,
    'assets': {
        'reuse_call_asset_id': 415859037062,
        'sitelinks': [
            ['Get a Free Quote', HOME + 'contact-us/', 'Tell us what you need done', "We'll call you back fast"],
            ['4.9-Star Google Reviews', HOME + 'reviews/', 'See what NWA neighbors say', 'Real reviews from local homeowners'],
            ['All Electrical Services', HOME + 'services/', 'Panels, EV chargers, repairs', 'Lighting, outlets, wiring & more'],
            ['Safety Inspections', HOME + 'electrical-safety-inspections/', 'Panels, wiring & breakers checked', 'Find code issues before they grow'],
            ['Residential Electrical', HOME + 'residential-electrical-service/', 'Repairs, upgrades, installs', 'For homes across Northwest Arkansas'],
        ],
        'callouts': ['Licensed, Bonded, Insured', 'Open 7 Days a Week', '4.9-Star Google Rating', 'Free Quotes',
                     'Local NWA Electricians', 'Fair, Honest Pricing', 'Nextdoor Fave 2023', 'Residential & Commercial'],
        'structured_snippet': {'header': 'Service catalog',
                               'values': ['Panel Upgrades', 'EV Chargers', 'Breaker Repair', 'Outlets & Wiring',
                                          'Lighting & Fans', 'Safety Inspections', 'Smoke Detectors', 'Thermostats']},
    },
    'pause_campaign_after_enable': '24208591381',
}
out = C / 'data/build-spec.json'
out.write_text(json.dumps(spec, indent=2, ensure_ascii=False))
print(out, '| universal', len(universal), '| nicho', len(niche), '| ad groups', len(ad_groups),
      '| keywords', sum(len(a['keywords']) for a in ad_groups))
