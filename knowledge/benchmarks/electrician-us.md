---
nicho: electrician
pais: US
cuentas: 5 electricistas (3 con datos al 2026-10-19 + 2 de la extracción del 2026-09-22 que ya no están en el conector); + 2 de nicho afín (HVAC, plomería) como referencia aparte
periodo: últimos 90 días. 3 cuentas en 2026-07-22 → 2026-10-19; 2 cuentas en 2026-06-24 → 2026-09-21
actualizado: 2026-10-20
fuente: Windsor.ai (google_ads), solo campañas Search. Crudo de la extracción del 20-oct en raw/electrician-us-2026-10-20.json
---
| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $5.24 | $5.38 | $8.13 |
| CTR | 3.2% | 4.2% | 5.7% |
| Tasa conv. | 1.9% | 2.8% | 28.9% |
| CPL | $18.14 | $193.59 | $493.90 |
| Conv./mes | 1.6 | 2.7 | 13.0 |
| Presupuesto/mes (pauta real Search) | $196 | $326 | $905 |

En el CPL, el P25 es el mejor cuartil. Las 5 cuentas son las 4 de la extracción del 22-sep más una cuenta nueva que entonces tenía 11 días y ahora tiene ~39 días de gasto. Las 3 que siguen en el conector se actualizaron al 20-oct.

**Distribución bimodal. No usar la mediana como objetivo.**
- Max. conversiones (2 cuentas, mercados chicos CO/NC): CPC $3.60–5.24, tasa conv. 29–31%, CPL $12–18, 13–18 conv./mes. La de CO se sostiene en 3 meses (Search: jul 16, ago 25, sep 16.5 conv.); agosto fue un pico.
- Max. clics (3 cuentas: 2 en California y 1 en Arkansas): CPC $5.38–10.85, tasa conv. 1.6–2.8%, CPL $190–580, 1–3 conv./mes.

**Solo las 3 cuentas vigentes (20-oct)**: CPC $6.69 / $8.13 / $9.49 · CTR 3.7% / 4.2% / 4.9% · tasa conv. 1.8% / 1.9% / 15.4% · CPL $256 / $494 / $537 · conv./mes 2.1 / 2.7 / 10.3. Dos de las tres pujan a clics.

**Nicho afín (referencia, no entra en los percentiles)**: una HVAC con Max. conversiones (CPC $12.51, tasa conv. 36.7%, CPL $34.12; sin marca, $85.61, con 88% de las conversiones de marca) y una plomería con Max. clics (CPC $7.00, tasa conv. 8.3%, CPL $83.95). Combinadas con las 3 electricistas vigentes: CPC $7.00 / $8.13 / $10.85 · tasa conv. 1.9% / 8.3% / 28.9% · CPL $34 / $84 / $494.

**Contradicción con la versión del 22-sep** (4 cuentas): la mediana del CPC pasó de $5.29 a $5.38 y la del CPL de $105.85 a $193.59, porque ahora pesa una cuenta más en Max. clics. Esta versión tiene más cuentas detrás (5), así que es la que queda. La conclusión no cambia: Max. conversiones con historial da un CPL 10–30 veces menor que Max. clics.

## Estructura que mejor funciona
- 1 campaña Search Radius, 1–4 ad groups, **Max. conversiones** (una con tCPA $20, fijado con ~16 conv./mes de historial).
- Keywords: "electrician(s)", "electrician near me", "electrical companies", electrician + ciudad y marca propia (~20% de las conversiones a un CPL de ~$6).
- Conversiones: "Calls from ads" + llamadas desde el sitio (15–20% del total) + formulario cuando existe.
- Usan broad; con el estándar PMM se replica en phrase.
- Cuota de impresiones de Search de 19–40%; ninguna satura su mercado.

## Keywords top por conversiones (agregado)
| Keyword | Conv. | CPL | Fuente |
|---|---|---|---|
| electricians | 31.7 / 19.3 | $20.42 / $19.68 | 22-sep (2 cuentas) / 20-oct (1 cuenta) |
| electrician near me | 10 / 11.5 | $21.86 / $24.97 | idem; en Max. clics (CA): 0 conv. en $205 |
| marca propia | 16 / 11 | $5.95 / $6.27 | idem |
| electrician + ciudad | ~5 / 7 | ~$22 / $19.56 | idem; en Max. clics (AR): 1 conv. en $316 |
| wiring electrician | 8 | $7.14 | 22-sep |
| electrical companies / electric company | 7 | $17.52 | 22-sep |
| a licensed electrician | 4 | $5.24 | 22-sep |
| home electrical (Max. clics) | 4 | $315.74 | 20-oct |
| electrical services (Max. clics) | 3 | $296.72 | 20-oct |

## Paneles eléctricos (extracción del 20-oct, 3 cuentas)
- **Volumen mínimo**: en 90 días, las keywords de panel (panel upgrade/replacement, breaker box / fuse box replacement, electrical service upgrade) sumaron 343 impresiones, 10 clics, $77.12 y 0 conv. Los search terms de panel sumaron 424 impresiones, 17 clics, $131.30 y 2 conv. (las 2 de **un solo clic**). Con <50 clics, la tasa de conversión es ruido.
- **CPC real de los clics de panel: ~$7.72** (CA, AR), por debajo de los $8–18 de Semrush.
- Un grupo de paneles en phrase, en un mercado de tamaño medio, imprimió ~5 veces al día. **Una cuenta que solo venda paneles en una geo chica puede quedarse sin demanda antes que sin presupuesto**: validar con Keyword Planner y la geo exacta.
- La mitad del gasto en paneles fue de precio o información ("cost to replace an electrical panel", "how much is a breaker box", "should i upgrade to 200 amp service"), con 0 conversiones.
- Comercial ("commercial electrician near me", "commercial electrical contractors"): 26 impresiones y 0 clics. Ninguna cuenta tiene un grupo comercial; no hay benchmark.

## Negativas que más gasto ahorraron
- Empresas de energía y cooperativas locales (en mercados con cooperativas "X Electric" se roban las búsquedas de "electric"): nombre de la cooperativa, "electric bill", "pay bill", "power outage".
- Competidores por nombre. En una cuenta con Max. conversiones, los nombres de competidores registran "conversiones": son llamadas de gente que buscaba a otro, no leads.
- Producto / DIY: "nema 14 50 outlet", "charger for home" sin "install", "junction box", "replacing ceiling fan", tesla charger / wall connector, marcas de ventiladores, números de parte de breakers ("qpf2", "dp 4075"), marcas de panel como producto ("zinsco panel", "sylvania electrical panel", "span panel"), "what does a tripped breaker look like", "wire for 40 amp breaker", "subpanel wiring".
- "handyman", "low cost", "hourly rate", "motor repair", "ac unit repair", "journeyman".

## Errores comunes vistos en cuentas del P25
- Max. clics como estrategia final: CPL 10–30 veces el del grupo Max. conversiones.
- Plantilla genérica en broad ("home electrical", "electrical services") sin ciudad ni marca. Al 20-oct, en una cuenta: "home electrical" $1,263 con 4 conv. y "electrical services" $692 con 2, en 90 días.
- Keywords de servicio de ticket alto (EV, paneles, ventiladores) metidas en el mismo ad group genérico: en una cuenta, EV $590 con 1 conv., ventiladores $269 con 0 y paneles $26 con 0, en 90 días.
- Medición incompleta: solo "Calls from ads", o solo formulario + llamadas del sitio, con "Calls from ads" en 0. Hay que medir las tres.
- Search partners activo ($42 y 0 conv. en una cuenta).
