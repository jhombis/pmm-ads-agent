---
cliente: Tuff Truck Towing
slug: tuff-truck-towing
campaña: Search | Towing & Hauling | BA-East Tulsa | v1
idioma: EN
actualizado: 2026-10-27
---

# RSA: Search | Towing & Hauling

- **1 RSA por ad group**: la pauta (~$700/mes) es menor que $1,500, y con ~3 clics/día un A/B sería ruido (estándar 4, playbook §9).
- Longitudes validadas por script: headlines ≤30 y descripciones ≤90. `{KeyWord:}` se cuenta sin la envoltura.
- **Las afirmaciones marcadas [C] dependen de que el cliente las confirme.** No se publican hasta que estén en el brief. Si no se confirman, se reemplazan por una headline del pool sin [C].
- **Prohibido en el copy**:
  - "24/7", "24 Hour", "Open Now": la web los dice, pero el horario del cliente es lun–vie 7–21.
  - Número de reseñas o años en el negocio: PENDIENTE.
  - Tiempos de llegada concretos.
  - "Heavy duty", semis.
  - Teléfono en el texto (lo rechaza PHONE_NUMBER_IN_AD_TEXT).

## Pool común de headlines
| # | Headline | Largo | Fuente / nota |
|---|---|---|---|
| C1 | Family-Owned Towing Company | 27 | cliente |
| C2 | Based in Broken Arrow, OK | 25 | web (JSON-LD) |
| C3 | Light & Medium-Duty Towing | 26 | cliente + web |
| C4 | Flatbed Towing Available | 24 | web |
| C5 | OK DPS Licensed Wrecker | 23 | web: DPS #53342-W |
| C6 | Licensed & Insured | 18 | web (/hauling: "insured and permitted") |
| C7 | 5 Trucks Ready to Roll | 22 | cliente |
| C8 | Call Now for a Quick Quote | 26 | |
| C9 | Open Mon-Fri 7 AM to 9 PM | 25 | [C] la web dice 24/7 |
| C10 | All Major Cards Accepted | 24 | web |
| C11 | Cars, Pickups & Box Trucks | 26 | medium-duty |
| C12 | Fast, Professional Towing | 25 | web |
| C13 | Talk to a Local Dispatcher | 26 | [C] quién contesta |

## Descripciones
| # | Descripción | Largo | Uso |
|---|---|---|---|
| D1 | Family-owned light and medium-duty towing in Broken Arrow, Bixby, Coweta and Catoosa. | 85 | T1, T2 |
| D2 | Licensed Oklahoma wrecker (DPS 53342-W), insured and permitted. Call for a quick quote. | 87 | todos |
| D3 | Open Mon-Fri 7 AM to 9 PM. Call now and talk to our local team about your tow. | 78 | T1, T2 [C] |
| D4 | Cars, pickups, work trucks and box trucks. Flatbed service available. Call us today. | 84 | T1, T2 |
| DE1 | Forklifts, skid steers, small equipment, 20 ft containers and lumber moved by flatbed. | 86 | E1 |
| DE2 | Family-owned and DOT registered. Tell us what needs moving and get a quote. Call now. | 85 | E1 |

- **T1 y T2**: D1, D2, D3, D4.
- **E1**: DE1, DE2, D2, y D3 adaptada si el cliente confirma horario.

## Headlines propios por ad group (H1 pinneado)
| Ad group | Pin H1 (rotan entre sí) | Otros propios | Del pool |
|---|---|---|---|
| T1 Towing Near Me | Tow Truck Near You (18) · Towing Service Near You (23) | Local Towing Company (20) | 12: todo el pool salvo C13 hasta que se confirme |
| T2 Towing Ciudades | {KeyWord:Broken Arrow Towing} (19) · Towing in Broken Arrow, OK (26) | Bixby, Coweta & Catoosa (23) | 12: igual que T1 |
| E1 Equipment & Container Hauling | {KeyWord:Equipment Hauling} (17) · Equipment & Forklift Hauling (28) | Forklift & Skid Steer Moves (27) · 20 ft Container Hauling (23) · Flatbed Equipment Transport (27) · Lumber & Small Load Hauling (27) · Get a Free Hauling Quote (24) [C] | 8: C1, C2, C5, C6, C7, C8, C9, C10 |

En T2, la inserción de keyword pone "Towing Tulsa", "Towing Bixby" o "Tow Truck Coweta" según la keyword que dispara el anuncio. Las keywords de ciudad van sin el sufijo de estado. El texto por defecto ("Broken Arrow Towing") cubre las keywords demasiado largas.

## Extensiones (nivel campaña salvo que se indique)
- **Llamada**: número de reenvío de Google sobre el (918) 320-7595, programada lun–vie 7:00–21:00. Conversión "Llamadas desde anuncios" con umbral de ≥60 s.
- **Sitelinks** (los 4 dependen de las landings; si no existen, no se crean):
  - Light-Duty Towing → /towing
  - Medium-Duty & Box Trucks → /towing#medium-duty
  - Equipment & Forklift Hauling → /equipment
  - Get a Quote → /towing#quote (formulario)
- **Callouts**: Family-Owned · Licensed & Insured · Flatbed Service · Light & Medium Duty · All Major Cards Accepted · Based in Broken Arrow
- **Snippet "Services"**: Light-Duty Towing, Medium-Duty Towing, Flatbed Towing, Equipment Hauling, Forklift Transport, Container Hauling
- **Ubicación**: requiere vincular el GBP (PENDIENTE: acceso).
- **Imágenes**: fotos reales del sitio (grúa cargando una pickup, SUV en flatbed). [C] Hay que pedir permiso y versiones en buena resolución.
