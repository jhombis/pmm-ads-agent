"""Genera los spec.json de las 4 landings de Pro Phase Electric (fuente: brief, strategy, audit-site, search terms 23–29 sep).
Uso: python clients/pro-phase-electric/landings/make_specs.py && python scripts/landing_build.py clients/pro-phase-electric/landings
Datos sin confirmar se dejan vacíos (la sección se omite): licencia, total de reseñas, años, garantía, tiempo de respuesta, form_id, privacidad.
"""
import copy, json
from pathlib import Path

HERE = Path(__file__).parent
DOMINIO = 'https://go.prophaseelectricar.com'  # subdominio GHL propuesto; confirmar al conectar el dominio
CIUDADES = ['Lowell', 'Rogers', 'Bentonville', 'Bella Vista', 'Springdale', 'Fayetteville', 'Centerton', 'West Fork', 'Huntsville']

BASE = {
    'idioma': 'en', 'nicho': 'electrician',
    'negocio': {
        'nombre': 'Pro Phase Electric', 'telefono': '+14792873650', 'telefono_display': '(479) 287-3650',
        'direccion': {'calle': '5173 Accident Rd', 'ciudad': 'Lowell', 'region': 'AR', 'cp': '72745', 'pais': 'US'},
        'licencia': '', 'horario': 'Open 7 days, 7 AM–6 PM', 'horario_schema': 'Mo-Su 07:00-18:00',
        'rating': {'valor': '4.9', 'total': '', 'fuente': 'on Google'},
        'logo_url': '', 'url_sitio': 'https://prophaseelectricar.com/', 'gbp_url': '', 'schema_type': 'Electrician',
    },
    # Provisional: carbón + el amarillo del botón de llamada del sitio. Confirmar con el logo del cliente.
    'marca': {'primario': '#1f2937', 'acento': '#f5c518', 'texto': '#111827', 'fondo': '#ffffff'},
    'confianza': [
        {'titulo': '4.9★ on Google', 'texto': 'Rated by NWA homeowners'},
        {'titulo': 'Licensed · Bonded · Insured', 'texto': 'Arkansas electricians'},
        {'titulo': 'Open 7 days', 'texto': '7 AM–6 PM, weekends too'},
        {'titulo': 'Nextdoor Fave 2023', 'texto': 'Neighborhood Favorite'},
    ],
    'resenas': {'h2': '', 'items': []},
    'zona': {'h2': 'Serving Northwest Arkansas', 'texto': 'Based in Lowell and working across Benton and Washington counties, including:',
             'ciudades': CIUDADES, 'mapa_embed_url': ''},
    'ghl': {'form_id': '', 'form_name': '', 'form_height': 520, 'form_embed_html': '', 'chat_widget_html': ''},
    # AW-ID de la cuenta 758-301-1023. Falta la etiqueta de una acción nueva "GHL Form" (y la de clic en teléfono).
    'tracking': {'gtm_id': '', 'google_ads_id': 'AW-18410300787', 'conversion_label_form': '', 'conversion_label_call': '', 'ga4_id': ''},
    'legal': {'privacidad_url': ''},
}

POR_QUE_COMUN = [
    {'titulo': 'Weekends included', 'texto': 'We work 7 days a week, 7 AM to 6 PM. Many local electricians only book Monday to Friday.'},
    {'titulo': 'Local, not a franchise', 'texto': 'A Lowell-based team that knows NWA homes, from older Fayetteville houses to new builds in Bentonville and Centerton.'},
    {'titulo': 'Fair, honest pricing', 'texto': 'Free quote first, so you know the price before any work starts. Customers mention our punctuality and reasonable prices.'},
]

PAGINAS = [
    dict(ag='Electrician - NWA', slug='electrician-northwest-arkansas', servicio='Residential Electrician', ciudad='Northwest Arkansas',
         kw='electrician northwest arkansas',
         kw2=['electrician near me', 'licensed electrician', 'electrician rogers', 'electrician fayetteville', 'electrician springdale', 'electrician bentonville'],
         title='Licensed Electrician in Northwest Arkansas | Pro Phase',
         desc='Licensed, bonded & insured electrician in Northwest Arkansas. Repairs, panels, EV chargers and lighting. Open 7 days. Get a free quote.',
         h1='Licensed Electrician in Northwest Arkansas',
         sub='Repairs, upgrades and new installs for NWA homes, from a tripping breaker or a dead outlet to a new panel or EV charger.',
         oferta='Free quotes · Open 7 days, 7 AM–6 PM',
         bullets=['Licensed, bonded & insured', '4.9★ rated on Google', 'Local team based in Lowell'],
         form_titulo='Get a Free Quote', form_nota='Tell us what you need. We reply during business hours, 7 days a week.',
         inc_h2='Electrical Services for NWA Homes', inc_intro='One licensed team for the jobs most homes need sooner or later.',
         inc=[('Repairs & Troubleshooting', 'Breakers that trip, outlets or switches that stopped working, flickering lights and wiring problems found and fixed.'),
              ('Panels, Outlets & Upgrades', 'Electrical panel upgrades, new circuits and 240V outlets, so your home handles today’s appliances safely.'),
              ('Lighting, Fans & Smart Home', 'Ceiling fans, light fixtures, smoke detectors, thermostats and video doorbells installed the right way.')],
         pq_h2='Why NWA Homeowners Choose Pro Phase',
         faq=[('What areas do you serve?', 'We are based in Lowell and serve Rogers, Bentonville, Bella Vista, Springdale, Fayetteville, Centerton, West Fork, Huntsville and nearby Northwest Arkansas communities.'),
              ('Are you licensed and insured?', 'Yes. Pro Phase Electric is licensed, bonded and insured.'),
              ('Do you work on weekends?', 'Yes. We are open 7 days a week, from 7 AM to 6 PM, Saturdays and Sundays included.'),
              ('Do you offer emergency service at night?', 'No. We are not a 24/7 service. Call us between 7 AM and 6 PM any day of the week and we will schedule your job.'),
              ('How much does an electrician cost?', 'It depends on the job. Tell us what you need and we will give you a free quote before any work starts.')],
         cta='Need a Licensed Electrician in NWA?', cta_txt='Call now or request a free quote. We are open 7 days a week.',
         form_name='LP Electrician NWA'),
    dict(ag='Electrical Repair', slug='electrical-repair-nwa', servicio='Electrical Repair', ciudad='Northwest Arkansas',
         kw='electrical repair',
         kw2=['electrical repair near me', 'circuit breaker repair', 'outlet repair', 'circuit breaker replacement', 'wiring repair', 'lighting repair near me', 'breaker box repair'],
         title='Electrical Repair in NWA | Breakers, Outlets & Wiring',
         desc='Electrical repair in Northwest Arkansas: breakers, outlets, wiring and lighting fixed by licensed electricians. Open 7 days, free quotes.',
         h1='Electrical Repair in Northwest Arkansas',
         sub='Breaker keeps tripping? Outlet not working? Lights flickering? Our licensed electricians find the cause and fix it right.',
         oferta='Free repair quotes · Open 7 days',
         bullets=['Licensed, bonded & insured', '4.9★ rated on Google', 'Weekend appointments'],
         form_titulo='Get a Free Repair Quote', form_nota='Describe the problem. We reply during business hours, 7 days a week.',
         inc_h2='Repairs We Handle Every Week', inc_intro='Most electrical problems start small. Fixing them early keeps your home safe.',
         inc=[('Circuit Breakers', 'Breakers that trip again and again, won’t reset or feel warm: we test the circuit and repair or replace the breaker.'),
              ('Outlets & Switches', 'Dead, loose, scorched or sparking outlets and switches replaced, including GFCI outlets for kitchens, baths and outdoors.'),
              ('Wiring & Lighting', 'Flickering or dimming lights, buzzing fixtures and faulty wiring traced to the source and repaired.')],
         pq_h2='Why Call Pro Phase for Repairs',
         faq=[('Why does my breaker keep tripping?', 'Usually an overloaded circuit, a short or a failing breaker. A licensed electrician can test the circuit and tell you which one it is.'),
              ('Is a warm or sparking outlet dangerous?', 'It can be. Stop using it and have it checked. Heat and sparks are signs of a loose connection or damaged wiring.'),
              ('Do you repair on weekends?', 'Yes. We are open 7 days a week, from 7 AM to 6 PM.'),
              ('Do you offer 24-hour emergency repairs?', 'No. We are not a 24/7 service. Call us between 7 AM and 6 PM any day and we will schedule the repair.'),
              ('How much does an electrical repair cost?', 'It depends on what is causing the problem. We give you a free quote before any work starts.')],
         cta='Electrical Problem at Home?', cta_txt='Call now or send the form for a free repair quote.',
         form_name='LP Electrical Repair'),
    dict(ag='Electrical Panel Upgrade', slug='electrical-panel-upgrade-nwa', servicio='Electrical Panel Upgrade', ciudad='Northwest Arkansas',
         kw='electrical panel upgrade',
         kw2=['electrical panel replacement', 'breaker box replacement', 'panel upgrade near me', 'fuse box replacement', '200 amp panel upgrade', 'electrical service upgrade'],
         title='Electrical Panel Upgrade in NWA | Free Quotes',
         desc='Electrical panel upgrades and breaker box replacement in Northwest Arkansas. 200 amp upgrades by licensed electricians. Free quotes.',
         h1='Electrical Panel Upgrade & Replacement in NWA',
         sub='Old fuse box, a full panel or breakers that keep tripping? Upgrade to a safe panel with room for what your home needs today.',
         oferta='Free panel upgrade quotes',
         bullets=['Licensed, bonded & insured', '4.9★ rated on Google', 'Open 7 days, 7 AM–6 PM'],
         form_titulo='Get a Free Panel Quote', form_nota='Tell us about your current panel. We reply during business hours, 7 days a week.',
         inc_h2='Panel Upgrades, Replacements & Service Upgrades', inc_intro='Your panel is the heart of your home’s electrical system. These are the most common reasons to upgrade it.',
         inc=[('Fuse Box to Breaker Panel', 'Replace an outdated fuse box or an aging breaker box with a modern panel and new breakers.'),
              ('200 Amp Service Upgrades', 'More capacity for an addition, a remodel, new appliances, a hot tub or an EV charger.'),
              ('Breaker Box Replacement', 'Panels that are full, corroded, warm or keep tripping replaced with a safe, properly labeled panel.')],
         pq_h2='Why Homeowners Trust Us With Their Panel',
         faq=[('Should I upgrade to 200 amp service?', 'If you are adding an EV charger, a hot tub, a big appliance or an addition, or your panel is already full, a 200 amp upgrade is often the right call. We check your current service and tell you honestly if you need it.'),
              ('How much does it cost to replace an electrical panel?', 'It depends on the panel size, its location and whether the service needs an upgrade. We give you a free quote before any work starts.'),
              ('What are signs my panel needs replacing?', 'Breakers that trip often, a panel that feels warm, rust or burn marks, a fuse box, flickering lights or no room for new circuits.'),
              ('Can you replace an old fuse box?', 'Yes. We replace fuse boxes and outdated breaker boxes with modern panels.'),
              ('Do you work on weekends?', 'Yes. We are open 7 days a week, from 7 AM to 6 PM.')],
         cta='Ready to Upgrade Your Panel?', cta_txt='Call now or request a free panel upgrade quote.',
         form_name='LP Panel Upgrade'),
    dict(ag='EV Charger Installation', slug='ev-charger-installation-nwa', servicio='EV Charger Installation', ciudad='Northwest Arkansas',
         kw='ev charger installation',
         kw2=['ev charger installation near me', 'electric car charger installation', 'level 2 charger installation', 'home ev charger installation', 'nema 14-50 outlet installation', 'ev charger installer'],
         title='EV Charger Installation in NWA | Level 2 Chargers',
         desc='Home and business EV charger installation in Northwest Arkansas. Level 2 chargers and 240V outlets by licensed electricians. Free quotes.',
         h1='EV Charger Installation in Northwest Arkansas',
         sub='Charge at home overnight. We install Level 2 EV chargers and 240V outlets for homes and businesses across NWA.',
         oferta='Free EV charger installation quotes',
         bullets=['Licensed, bonded & insured', 'Homes and businesses', 'Open 7 days, 7 AM–6 PM'],
         form_titulo='Get a Free EV Charger Quote', form_nota='Tell us your vehicle and where you park. We reply during business hours, 7 days a week.',
         inc_h2='Home & Commercial EV Charging Installs', inc_intro='The right setup depends on your vehicle, your panel and where you park.',
         inc=[('Level 2 Home Chargers', 'Hardwired wall chargers installed in your garage or driveway for faster charging than a regular outlet.'),
              ('240V / NEMA 14-50 Outlets', 'A dedicated 240V outlet on its own circuit, so you can plug in your car’s mobile charger.'),
              ('Commercial Charging', 'EV charging for businesses, offices and properties, planned with your existing electrical service.')],
         pq_h2='Why NWA Drivers Choose Pro Phase',
         faq=[('How much does it cost to install an EV charger at home?', 'It depends on the distance from your panel, the charger you choose and whether your panel has capacity. We give you a free quote before any work starts.'),
              ('Can I install a Level 2 charger at home?', 'In most homes, yes. We check your panel and the circuit it needs, and tell you if an upgrade is required first.'),
              ('Do I need a panel upgrade for an EV charger?', 'Not always. A Level 2 charger needs a dedicated circuit, so if your panel is full or undersized we will recommend the right option.'),
              ('Do you install chargers for businesses?', 'Yes. We install EV charging for residential and commercial properties.'),
              ('Do you work on weekends?', 'Yes. We are open 7 days a week, from 7 AM to 6 PM.')],
         cta='Ready to Charge at Home?', cta_txt='Call now or request a free EV charger installation quote.',
         form_name='LP EV Charger'),
]

for p in PAGINAS:
    s = copy.deepcopy(BASE)
    s['pagina'] = {'slug': p['slug'], 'url_final': f"{DOMINIO}/{p['slug']}", 'servicio': p['servicio'], 'ciudad': p['ciudad'],
                   'keyword_principal': p['kw'], 'keywords_secundarias': p['kw2'], 'title': p['title'], 'meta_description': p['desc'],
                   'og_image': '', 'indexar': False, 'ad_group': p['ag']}
    s['hero'] = {'h1': p['h1'], 'subtitulo': p['sub'], 'oferta': p['oferta'], 'bullets': p['bullets'],
                 'cta_llamar': 'Call Now', 'cta_form': 'Get a Free Quote', 'form_titulo': p['form_titulo'], 'form_nota': p['form_nota'], 'imagen': {}}
    s['incluye'] = {'h2': p['inc_h2'], 'intro': p['inc_intro'], 'items': [{'titulo': a, 'texto': b} for a, b in p['inc']]}
    s['por_que'] = {'h2': p['pq_h2'], 'items': POR_QUE_COMUN}
    s['proceso'] = {'h2': 'How It Works', 'pasos': [
        {'titulo': 'Call or send the form', 'texto': 'Tell us what you need and where you are in NWA.'},
        {'titulo': 'Get your free quote', 'texto': 'A licensed electrician reviews the job and gives you a price before any work starts.'},
        {'titulo': 'Done right', 'texto': 'We schedule a day that works for you, weekends included.'}]}
    s['faq'] = {'items': [{'q': q, 'a': a} for q, a in p['faq']]}
    s['cta_final'] = {'h2': p['cta'], 'texto': p['cta_txt']}
    s['gracias'] = {'slug': p['slug'] + '-thank-you', 'h1': 'Thanks — we got your request',
                    'texto': 'Our team will contact you during business hours (7 AM–6 PM, 7 days a week). Need us sooner? Call (479) 287-3650.',
                    'pasos': [{'titulo': 'We review your request', 'texto': 'We check the details you sent.'},
                              {'titulo': 'We contact you', 'texto': 'By phone or text to set up your free quote.'}]}
    s['ghl']['form_name'] = p['form_name']
    d = HERE / p['slug']
    d.mkdir(exist_ok=True)
    (d / 'spec.json').write_text(json.dumps(s, indent=2, ensure_ascii=False) + '\n')
    print(d / 'spec.json')
