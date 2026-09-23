---
cliente: Pro Phase Electric
slug: pro-phase-electric
url: https://prophaseelectricar.com/
actualizado: 2026-09-23
veredicto: REQUIERE AJUSTES ANTES DE ESCALAR (la cuenta ya está activa)
score: 12/20 en ítems verificables · velocidad SIN DATO (2 pts)
---

# Auditoría de landing — Pro Phase Electric

> **Fuentes.** Capturas de escritorio de la home y de /services/ que envió Jhombis (FireShot, 2026-09-22), datos de Google Ads de la cuenta 758-301-1023 vía Windsor, Semrush orgánico y búsqueda web.
> **Qué no se pudo ver**: el HTML (tag, `tel:`, destino del formulario), la vista móvil y la velocidad. El sitio está bloqueado por la política de red del entorno y PageSpeed sin API key da 429.
> Para cerrarlo: captura **móvil** de la home (arriba del pliegue), una prueba de envío del formulario (¿a qué URL va?) y el score de pagespeed.web.dev.

## Veredicto
El sitio tiene buena base de confianza: 4.9 ★ en Google con carrusel de reseñas, badge Licensed/Bonded/Insured, Nextdoor Neighborhood Fave 2023, fotos reales, formulario corto y botón de llamada en el header. Pero **no tiene páginas de paneles ni de EV**, el H1 es genérico, y **Google Ads solo mide "Calls from Ads"**. No hay que escalar presupuesto ni abrir ad groups de paneles y EV hasta resolver los 3 bloqueantes.

## Bloqueantes (resolver en Fase 0)
- [ ] **Medir conversiones del sitio en Google Ads.** Tres piezas:
  - (a) Envío del formulario "Get a Free Quote" (home y /contact-us/): página de gracias con URL propia o evento de envío.
  - (b) Clic en `tel:` y llamadas desde la web con número de reenvío de Google.
  - (c) Probar todo con Tag Assistant.

  Hoy hay **una sola acción de conversión** ("Calls from Ads"). Las cuentas del MCC que funcionan suman 15–20% más de conversiones con las llamadas del sitio (`benchmark.md`). — PMM — 2–3 h
- [ ] **Landing de paneles eléctricos.** En /services/ el servicio aparece como tarjeta sin enlace; no hay página propia. — PMM o cliente (quién edita: PENDIENTE) — 4–6 h
- [ ] **Landing de instalación de cargadores EV.** Mismo caso. — PMM o cliente — 4–6 h

Cada landing lleva: H1 con el servicio y NWA, el mismo formulario de 4 campos arriba, botón de llamada, widget 4.9 ★, badge Licensed/Bonded/Insured, fotos del servicio del portfolio (ya hay fotos de paneles) y la oferta "Free Quote".

## Mejoras (Fase 2–3)
- [ ] **H1 de la home**: "Electrical Services Done Right" no dice qué ni dónde. Mejor algo como "Licensed Electrician in Northwest Arkansas — Repairs, Panels & EV Chargers" y dejar la frase actual como subtítulo. Ayuda a la experiencia de la landing, hoy *below average* en "electrician".
- [ ] **Oferta más concreta**: "Get a Free Quote" es genérico. Si el cliente lo sostiene: "Free estimates on panel upgrades & EV chargers", "Open 7 days", "Same-week service".
- [ ] **Horario**: no aparece en la home. Mostrar "Open 7 days · 5 AM – 4 PM" en la barra superior (es un diferenciador; `competitors.md`) y alinearlo con el GBP.
- [ ] **Número de licencia de Arkansas** junto al badge Licensed/Bonded/Insured. Agregar años en el negocio y garantía si existen.
- [ ] **Captcha del formulario**: parece de tipo matemático ("6 + ? ="). Es fricción; cambiarlo por reCAPTCHA v3 o honeypot.
- [ ] **Email de contacto en Gmail** (barra superior). Un dominio propio (`info@prophaseelectricar.com`) da más confianza.
- [ ] **Página de reparación** (breakers, outlets, cableado, troubleshooting, reparación de iluminación) para ese ad group. O que la home cumpla ese papel con el H1 nuevo.
- [ ] **Sitelinks**: hoy uno lleva a /portfolio/. Mejor Reviews, Panel Upgrades, EV Chargers y Free Quote cuando existan las páginas.
- [ ] **Landings por ciudad** (Fayetteville, Rogers, Bentonville, Springdale): solo si el volumen lo justifica. La sección "Our Service Areas" ya lista las ciudades.

## Rúbrica
| Ítem | Puntaje | Evidencia |
|---|---|---|
| Headline refleja el servicio buscado | **1** | H1 "Electrical Services Done Right" + "Proudly serving Northwest Arkansas". Sirve para búsquedas genéricas; **0 para paneles y EV** (no hay página). Experiencia de landing *below average* en "electrician" |
| Formulario corto visible arriba (móvil) | **1** | "Get a Free Quote": Name, Email, Phone, How can we help? + captcha. Son 4 campos, pero está **debajo del hero**, así que en móvil casi seguro requiere scroll. Sin captura móvil |
| Clic para llamar en móvil | **2** (escritorio) | Botón amarillo "Call (479) 287-3650" en el header, barra superior "Need electrical help? Call us now!" y "Call Now" en el hero. `tel:` y sticky en móvil sin verificar |
| Oferta clara | **1** | "Get a Free Quote": hay oferta, pero genérica |
| Prueba social | **2** | Widget de Google con 4.9 ★ y carrusel de reseñas con nombre y foto, testimonios en /services/, Nextdoor Neighborhood Fave 2023, portfolio con fotos reales |
| Confianza | **1** | Badge "Licensed · Bonded · Insured" en hero y footer. Faltan número de licencia, años y garantía |
| Velocidad móvil | SIN DATO | PageSpeed 429; `speed_score` vacío en Ads. El hero y el portfolio usan fotos grandes, así que hay riesgo de LCP alto |
| Google Tag presente | **1** | El cliente dice que sí, pero Ads no recibe ninguna conversión del sitio |
| Página de gracias medible | **0** | No hay acción de conversión de formulario. Destino del envío sin verificar |
| Páginas por servicio | **1** | Existen residential, commercial, new build y safety inspections. Las 12 tarjetas de /services/ **no enlazan** a páginas propias; faltan panel, EV y reparación |
| Sin fugas | **2** | Menú de 4 ítems + 2 CTA, sin pop-ups visibles. Único enlace externo: "Review us on Google" |

**Total: 12/20 verificable.** Si la velocidad sale en 2, el máximo posible hoy es 14/22.

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| `/` (URL final del único RSA, 35 de 35 clics) | Electrical Services Done Right | Get a Quote, Call (header); Call Now, Contact Us (hero) | 4 campos + captcha, debajo del hero | Header, barra superior, hero | 4.9 ★ Google + carrusel, Nextdoor 2023, portfolio | Las tarjetas de servicio muestran solo residential, commercial, new build y safety. No menciona paneles ni EV |
| `/services/` | Our Services | Get a Quote, Call, Contact Us | No | Header | 3 testimonios, Nextdoor | 12 tarjetas **sin enlace**. Paneles y EV son las 2 primeras |
| `/contact-us/` | — | — | Sí (no visto) | — | — | 3 clics de anuncios ($29.57) |
| `/reviews/`, `/portfolio/`, `/about-us/` | — | — | — | — | — | /portfolio/ es sitelink hoy |
| `/residential-…`, `/commercial-…`, `/new-build-…`, `/electrical-safety-inspections/` | — | "More info" desde la home | — | — | — | Páginas de servicio que ya existen |
| *(no existe)* panel / EV / reparación | — | — | — | — | — | **Crear** |

## Tracking encontrado
- **Google Ads (758-301-1023)**: 1 acción con datos en 90 días, "Calls from Ads" (1 conversión). No hay "Website Calls", "Form Fill" ni "Clicks to call".
- **Google Tag / GA4**: instalado según el cliente; ID sin verificar. Windsor no tiene una propiedad GA4 de este dominio conectada.
- **Quality Score**: 3–5/10. Experiencia de landing *below average* en "electrician" y "electrician companies near me", *average* en otras 3. CTR esperado *below average* en las 5.
- **Formulario**: destino desconocido (¿email Gmail?). Falta confirmar si redirige a una página de gracias.

## Velocidad
Sin datos. Correr `python scripts/pagespeed.py https://prophaseelectricar.com/ --strategy mobile` con `PAGESPEED_API_KEY`, o pedir el score de pagespeed.web.dev. Si el score móvil es menor a 40, es bloqueante. Riesgo: foto del hero a pantalla completa y galería de 8 fotos en la home.

## Landings que la estrategia va a necesitar
1. **Electrical Panel Upgrade & Replacement — Northwest Arkansas** (panel, 200 amp, breaker box). El portfolio ya tiene fotos de paneles.
2. **EV Charger Installation — Northwest Arkansas** (Level 2, Tesla, NEMA 14-50 install; residencial y comercial).
3. **Electrical Repair**: breakers, outlets, cableado, iluminación. Puede ser la home con el H1 nuevo.
4. *(Fase 3, según volumen)* Ciudad: Fayetteville, Rogers, Bentonville, Springdale.

**Faltan 2 landings obligatorias** (panel, EV), 1 recomendada (reparación) y 4 de ciudad opcionales.

## Qué ya rankea orgánico (Semrush)
Visibilidad casi nula: 27 keywords en el top 100 y ~3 visitas al mes, todas a la home.
- Marca: "prophase electric" (posición 3), "prophase electrical" (posición 6), ~40 búsquedas/mes cada una. La marca la cubre el orgánico; una campaña de marca no es prioridad con este presupuesto.
- Genéricas locales, sin relevancia real: "electrician northwest arkansas" (posición 44), "electricians in bentonville" (51), "commercial electrician nwa" (56).
- El orgánico no cubre ningún término de servicio, así que **Search pagado es el canal** para paneles y EV.
