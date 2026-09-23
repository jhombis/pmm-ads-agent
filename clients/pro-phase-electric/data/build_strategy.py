# Genera data/ads-search-nwa.md y data/keywords.csv (copy validado por largo) para Pro Phase Electric — strategy v4.
import csv, sys

OUT = '/home/user/pmm-ads-agent/clients/pro-phase-electric/data/'
errors = []


def chk(txt, n, where):
    if len(txt) > n:
        errors.append(f'{where}: "{txt}" = {len(txt)} > {n}')
    return txt


SHARED_H = [
    "Licensed, Bonded & Insured",
    "4.9-Star Rated on Google",
    "Open 7 Days a Week",
    "Get a Free Quote Today",
    "Talk to a Local Electrician",
    "Local NWA Electricians",
    "Fair, Honest Pricing",
    "Nextdoor Neighborhood Fave",
    "We Show Up When We Say",
    "Clean, Code-Compliant Work",
    "Early Appointments From 5 AM",
    "Weekend Service Available",
]
SHARED_D = [
    "Licensed, bonded & insured electricians. 4.9 stars on Google. Call for a free quote today.",
    "Open 7 days a week, 5 AM to 4 PM. Local Lowell-based team serving all of NW Arkansas.",
    "Fair, honest pricing and clean, code-compliant work. We show up when we say we will.",
]

AG = [
    # name, fase, landing, pinned H1 x3, specific unpinned (to reach 14), specific description, keywords
    dict(name="Electrician - NWA", fase="F1", url="https://prophaseelectricar.com/",
         h1=["{KeyWord:Licensed NWA Electrician}", "Licensed Electrician Near You", "Northwest Arkansas Electrician"],
         hs=["Serving All of NW Arkansas", "Rogers, Fayetteville & More"],
         d="Local electricians for Fayetteville, Rogers, Springdale, Bentonville & all of NWA.",
         kw=[("electrician near me", "EXACT", 440), ("electricians near me", "EXACT", 109), ("electrician", "EXACT", 660),
             ("electricians", "EXACT", 0), ("local electrician", "EXACT", 40),
             ("electrician fayetteville", "EXACT", 210), ("electrician rogers", "EXACT", 140), ("electrician springdale", "EXACT", 120),
             ("electrician bentonville", "EXACT", 80),
             ("electrician near me", "PHRASE", 0), ("electricians near me", "PHRASE", 0), ("local electrician", "PHRASE", 0),
             ("licensed electrician", "PHRASE", 40), ("residential electrician", "PHRASE", 33), ("electrical contractor near me", "PHRASE", 15),
             ("electrical company near me", "PHRASE", 4), ("electrician open now", "PHRASE", 0), ("home electrician", "PHRASE", 0),
             ("electrician northwest arkansas", "PHRASE", 40), ("electrician nwa", "PHRASE", 30), ("nwa electrician", "PHRASE", 0),
             ("electrician fayetteville", "PHRASE", 0), ("electricians fayetteville", "PHRASE", 50), ("electricians in fayetteville", "PHRASE", 20),
             ("fayetteville electrician", "PHRASE", 0),
             ("electrician rogers", "PHRASE", 0), ("electricians rogers", "PHRASE", 40), ("rogers electrician", "PHRASE", 0),
             ("electrician springdale", "PHRASE", 0), ("electricians springdale", "PHRASE", 0), ("springdale electrician", "PHRASE", 0),
             ("electrician bentonville", "PHRASE", 0), ("electricians bentonville", "PHRASE", 30), ("bentonville electrician", "PHRASE", 0),
             ("electrician bella vista", "PHRASE", 30), ("electrician lowell", "PHRASE", 10), ("electrician centerton", "PHRASE", 20),
             ("electrician cave springs", "PHRASE", 0), ("electrician pea ridge", "PHRASE", 0), ("electrician farmington", "PHRASE", 0),
             ("electrician prairie grove", "PHRASE", 0), ("electrician west fork", "PHRASE", 0), ("electrician tontitown", "PHRASE", 0),
             ("electrician huntsville", "PHRASE", 0)],
         neg=["panel", "breaker box", "ev charger", "car charger", "tesla", "repair"]),
    dict(name="Electrical Repair", fase="F1", url="https://prophaseelectricar.com/residential-electrical-service/ (F1, verificar que hable de reparaciones) → /electrical-repair/ cuando exista",
         h1=["Electrical Repair in NWA", "Breaker & Outlet Repair", "Electrical Repairs Done Right"],
         hs=["Breakers, Outlets & Wiring", "Lighting Repair & Installs"],
         d="Breakers tripping, dead outlets, flickering lights? We find the problem and fix it right.",
         kw=[("electrical repair near me", "EXACT", 22), ("circuit breaker repair", "EXACT", 12), ("outlet repair", "EXACT", 3),
             ("electrical repair", "PHRASE", 22), ("electrician repair", "PHRASE", 0), ("circuit breaker repair", "PHRASE", 0),
             ("circuit breaker replacement", "PHRASE", 49), ("breaker replacement", "PHRASE", 0), ("outlet repair", "PHRASE", 0),
             ("outlet installation near me", "PHRASE", 1), ("electrical wiring repair", "PHRASE", 2),
             ("wiring repair", "PHRASE", 0), ("lighting repair near me", "PHRASE", 1)],
         neg=["panel", "breaker box", "ev", "charger", "tesla"]),
    dict(name="Electrical Panel Upgrade", fase="F2 (pausado hasta landing)", url="https://prophaseelectricar.com/electrical-panel-upgrade/ (CREAR)",
         h1=["Electrical Panel Upgrades", "Panel Replacement in NWA", "200 Amp Panel Upgrades"],
         hs=["Upgrade to 200 Amp Service", "Free Panel Upgrade Quotes"],
         d="Upgrade or replace your electrical panel safely and up to code. Free quotes on panel work.",
         kw=[("electrical panel upgrade", "EXACT", 22), ("electrical panel replacement", "EXACT", 15), ("breaker box replacement", "EXACT", 3),
             ("panel upgrade near me", "EXACT", 1), ("electrical panel upgrade", "PHRASE", 0), ("electrical panel replacement", "PHRASE", 0),
             ("panel upgrade", "PHRASE", 0), ("panel replacement", "PHRASE", 0), ("breaker box replacement", "PHRASE", 0),
             ("fuse box replacement", "PHRASE", 3), ("200 amp panel upgrade", "PHRASE", 0), ("200 amp service upgrade", "PHRASE", 0),
             ("electrical panel replacement cost", "PHRASE", 4), ("electrical service upgrade", "PHRASE", 0),
             ("electric panel installation", "PHRASE", 0)],
         neg=["ev", "charger", "tesla", "solar"]),
    dict(name="EV Charger Installation", fase="F2 (pausado hasta landing)", url="https://prophaseelectricar.com/ev-charger-installation/ (CREAR)",
         h1=["EV Charger Installation", "Home EV Charger Installers", "Level 2 EV Charger Installs"],
         hs=["Level 2 Home EV Chargers", "Free EV Charger Quotes"],
         d="Level 2 EV charger installs for your home or business, done safely and up to code.",
         kw=[("ev charger installation", "EXACT", 73), ("ev charger installation near me", "EXACT", 40), 
             ("electric car charger installation", "EXACT", 15), ("ev charger installation", "PHRASE", 0), ("ev charger installer", "PHRASE", 1),
             ("electric car charger installation", "PHRASE", 0),
             ("level 2 charger installation", "PHRASE", 2),
             ("nema 14-50 outlet installation", "PHRASE", 0), ("ev charging station installation", "PHRASE", 0),
             ("ev charger installation cost", "PHRASE", 4), ("home ev charger installation", "PHRASE", 4)],
         neg=["panel upgrade cost only", ]),
]
AG[-1]['neg'] = []

md = ["# Anuncios — Search NWA (Pro Phase Electric)\n",
      "Idioma: EN. **1 RSA por ad group** (pauta <$1,500/mes; playbook §9: con ~3 clics/día un A/B es ruido). H1 pinneado a la posición 1 = el H1 del RSA. Los H1 alternativos quedan listos para un 2.º RSA solo si sube el volumen.",
      "Estructura v2 (23-sep): 2 ad groups activos en F1 (NWA + Repair) y 2 en F2 (Panel, EV). Las ciudades van dentro de *Electrician - NWA*; el RSA A usa inserción de keyword en el H1 (`{KeyWord:Licensed NWA Electrician}`), así que las keywords de ciudad van **sin \"ar\"** para que el titular no salga \"Electrician Rogers Ar\". Si la keyword pasa de 30 caracteres, Google muestra el texto por defecto.",
      "Largos validados por script: headlines ≤30, descripciones ≤90, callouts ≤25, snippets ≤25, sitelinks ≤25/35.\n"]
kwrows = []
for ag in AG:
    n = ag['name']
    for h in ag['h1']:
        chk(h[len('{KeyWord:'):-1] if h.startswith('{KeyWord:') else h, 30, n + ' H1')
    unp = SHARED_H + ag['hs']
    assert len(unp) == 14, (n, len(unp))
    for h in unp:
        chk(h, 30, n)
    desc = [ag['d']] + SHARED_D
    for d in desc:
        chk(d, 90, n + ' desc')
    md.append(f"## {n} — {ag['fase']}\nLanding: {ag['url']}\n")
    L = lambda h: len(h[9:-1]) if h.startswith('{KeyWord:') else len(h)
    md.append(f"**RSA — H1 pinneado (posición 1):** {ag['h1'][0]} ({L(ag['h1'][0])})\n")
    md.append("H1 alternativos (para un 2.º RSA si sube el volumen): " + " · ".join(f"{h} ({L(h)})" for h in ag['h1'][1:]))
    md.append("\n**Headlines sin pin (14):**")
    for h in unp:
        md.append(f"- {h} ({len(h)})")
    md.append("\n**Descripciones (4):**")
    for d in desc:
        md.append(f"- {d} ({len(d)})")
    md.append("")
    for k, m, v in ag['kw']:
        kwrows.append([k, v, '', 'comercial', n, '', m, ag['fase']])

EXT = """## Extensiones (nivel campaña)
**Llamada:** (479) 287-3650. Programación L–D 5:00–16:00. Informes de llamadas activados. Conversión: llamadas ≥60 s.

**Sitelinks** (texto ≤25 · descripciones ≤35):
| Texto | URL | Desc. 1 | Desc. 2 |
|---|---|---|---|
| Get a Free Quote | /contact-us/ | Tell us what you need done | We'll call you back fast |
| 4.9-Star Google Reviews | /reviews/ | See what NWA neighbors say | Real reviews from local homeowners |
| All Electrical Services | /services/ | Panels, EV chargers, repairs | Lighting, outlets, wiring & more |
| Safety Inspections | /electrical-safety-inspections/ | Panels, wiring & breakers checked | Find code issues before they grow |
| Residential Electrical | /residential-electrical-service/ | Repairs, upgrades, installs | For homes across Northwest Arkansas |
| *(F2)* Panel Upgrades | /electrical-panel-upgrade/ | Upgrade to 200 amp service | Free quotes on panel work |
| *(F2)* EV Charger Installs | /ev-charger-installation/ | Level 2 chargers, installed | Home or business installs |

Se quita el sitelink a /portfolio/.

**Callouts (≤25):** Licensed, Bonded, Insured · Open 7 Days a Week · 4.9-Star Google Rating · Free Quotes · Local NWA Electricians · Fair, Honest Pricing · Nextdoor Fave 2023 · Residential & Commercial

**Structured snippet — Service catalog:** Panel Upgrades · EV Chargers · Breaker Repair · Outlets & Wiring · Lighting & Fans · Safety Inspections · Smoke Detectors · Thermostats

**Ubicación:** requiere vincular el GBP (hoy PMM no tiene acceso). Bloquea el activo, no el lanzamiento.
**Imágenes:** fotos propias del portfolio (panel, iluminación, trabajos terminados). Sin stock.
"""
for c in ["Licensed, Bonded, Insured", "Open 7 Days a Week", "4.9-Star Google Rating", "Free Quotes", "Local NWA Electricians",
          "Fair, Honest Pricing", "Nextdoor Fave 2023", "Residential & Commercial"]:
    chk(c, 25, 'callout')
for s in ["Panel Upgrades", "EV Chargers", "Breaker Repair", "Outlets & Wiring", "Lighting & Fans", "Safety Inspections", "Smoke Detectors", "Thermostats"]:
    chk(s, 25, 'snippet')
for t, d1, d2 in [("Get a Free Quote", "Tell us what you need done", "We'll call you back fast"),
                  ("4.9-Star Google Reviews", "See what NWA neighbors say", "Real reviews from local homeowners"),
                  ("All Electrical Services", "Panels, EV chargers, repairs", "Lighting, outlets, wiring & more"),
                  ("Safety Inspections", "Panels, wiring & breakers checked", "Find code issues before they grow"),
                  ("Residential Electrical", "Repairs, upgrades, installs", "For homes across Northwest Arkansas"),
                  ("Panel Upgrades", "Upgrade to 200 amp service", "Free quotes on panel work"),
                  ("EV Charger Installs", "Level 2 chargers, installed", "Home or business installs")]:
    chk(t, 25, 'sitelink'); chk(d1, 35, 'sitelink d1'); chk(d2, 35, 'sitelink d2')
md.append(EXT)
md.append("## Negativas por ad group (enrutamiento STAG)")
for ag in AG:
    if ag['neg']:
        md.append(f"- **{ag['name']}**: " + ", ".join(f'"{x}"' for x in ag['neg']) + " (frase)")

if errors:
    print("\n".join(errors)); sys.exit(1)
open(OUT + 'ads-search-nwa.md', 'w').write("\n".join(md) + "\n")

# keywords.csv: active + discarded
disc = [
    ("electrical services", 33100, 13.30, "genérica / baja intención", "descartada F1", "D: $692 → 2 conv; Pro Phase: $190 → 1 conv"),
    ("home electrical", 1000, 13.03, "genérica", "descartada F1", "D: $945 → 3 conv; Pro Phase: $129 → 0"),
    ("electrical contractors", 9900, 11.01, "B2B / constructores", "descartada F1", "Pro Phase: $75 → 0; mezcla comercial/industrial"),
    ("emergency electrician", 27100, 21.48, "comercial 24/7", "negativa", "El cliente no es 24/7"),
    ("24 hour electrician", 12100, 20.00, "comercial 24/7", "negativa", "El cliente no es 24/7"),
    ("same day electrician", 1000, 30.36, "comercial", "descartada F1", "No hay promesa same-day confirmada; CPC $30"),
    ("generator installation", 60500, 13.98, "comercial", "negativa", "Servicio no listado (confirmar)"),
    ("ceiling fan installation", 49500, 6.04, "mixta / DIY, ticket bajo", "descartada F1", "D: $152 → 0 conv"),
    ("recessed lighting installation", 27100, 5.12, "ticket bajo", "descartada F1", ""),
    ("light fixture installation", 4400, 5.88, "ticket bajo", "descartada F1", ""),
    ("gfci outlet installation", 40500, 2.48, "informacional / DIY", "descartada", ""),
    ("breaker keeps tripping", 4400, 3.59, "informacional", "descartada F1", "Posible prueba F3 en el grupo Repair"),
    ("smoke detector installation", 4400, 8.68, "ticket bajo", "descartada", ""),
    ("thermostat installation", 0, 0, "ticket bajo / HVAC", "descartada", ""),
    ("doorbell installation", 0, 0, "ticket bajo", "descartada", ""),
    ("data line installation", 0, 0, "ticket bajo / nicho", "descartada", ""),
    ("electric company near me", 9900, 13.27, "ambigua (utility)", "negativa si trae cooperativas", ""),
    ("prophase electric", 40, 0, "marca propia", "negativa en Search (sin campaña de marca F1)", "Orgánico en posición 3"),
    ("mister sparky / mr electric / epic electric ...", 0, 0, "competidor", "negativa", "Estándar PMM 5"),
    ("carroll electric / ozarks electric / swepco", 0, 0, "utility", "negativa", "$68.58 gastados en 11 días"),
]
with open(OUT + 'keywords.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['keyword', 'vol_nwa_est', 'cpc_us', 'intencion', 'ad_group', 'ciudad', 'match', 'fase_o_decision', 'nota'])
    for k, v, _, i, ag, c, m, fase in kwrows:
        city = next((x for x in ['fayetteville', 'rogers', 'springdale', 'bentonville', 'bella vista', 'lowell', 'centerton', 'cave springs',
                                 'pea ridge', 'farmington', 'prairie grove', 'west fork', 'tontitown', 'huntsville'] if x in k), '')
        w.writerow([k, v, '', i, ag, city, m, fase, ''])
    for k, v, cpc, i, dec, note in disc:
        w.writerow([k, v, cpc, i, '', '', '', dec, note])
print("OK", len(kwrows), "keywords activas;", len(AG), "ad groups")
for ag in AG:
    print(ag['name'], len(ag['kw']), sum(v for _, _, v in ag['kw']))
