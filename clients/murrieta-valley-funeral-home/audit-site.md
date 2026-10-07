---
cliente: Murrieta Valley Funeral Home
slug: murrieta-valley-funeral-home
url: https://murrietavalleyfuneralhome.com/
actualizado: 2026-10-07
veredicto: REQUIERE AJUSTES ANTES DE LANZAR
score: 11/22
---

# Auditoría de landing — Murrieta Valley Funeral Home

> Fuentes: `data/site-scan.json` (26 páginas, 2026-10-07), HTML de home, /service-options/, /service-pricing/, /contact-us/, /testimonials/, /veteran-services/ descargado y renderizado en Chromium móvil (`data/perf-lab-2026-10-07.json`), GPL en PDF (`data/gpl-2024-02-29.txt`). PageSpeed Insights sin clave: cuota agotada; velocidad medida en laboratorio. El contenedor de GTM (`GTM-MRZ2HJMT`) está bloqueado por el proxy: no se pudo ver qué etiquetas dispara. La cuenta ya gasta (~$1,200/mes), así que "antes de lanzar" aquí significa **antes de seguir pagando clics hacia estas páginas**.

## Veredicto
**11/22. Requiere ajustes antes de seguir pagando tráfico.** La base técnica está (tag, formulario corto, llamada visible), pero no hay ninguna página que hable de cremación, el formulario no tiene página de gracias y la oferta no aparece en ningún lado. Tres bloqueantes:
1. **Ninguna página refleja el servicio que se compra.** La home no tiene H1 (el hero es "Honoring Lives and Telling Unique Stories"); cremación y entierro viven como párrafos dentro de /service-options/ (H1 "Service Options"). Quien busca "cremation near me" aterriza en una funeraria genérica.
2. **Formulario sin página de gracias.** Elementor Pro, 4 campos, mensaje en línea; `/thank-you/` da 404. Form Fill no se puede medir por URL y es imposible saber hoy si la cuenta registra formularios.
3. **Oferta invisible.** El sitio no muestra un solo precio; /service-pricing/ son tres PDF. El GPL real dice **cremación directa $1,361.50–1,656.50 + crematory fee $216.50 y más** (≈ $1,578–1,873 todo incluido), no los $995 que repiten los directorios. Con competidores a $855–995 en la misma SERP, la página tiene que vender otra cosa que precio, y hoy no vende nada.

## Bloqueantes (resolver en Fase 0)
- [ ] **Landing de cremación** (`/cremation/` o `/cremation-services-murrieta/`): H1 "Cremation Services in Murrieta & Temecula", paquetes D/E/F del GPL con precio ($3,015 / $3,500 / $4,000) y cremación directa desde $1,578 todo incluido, formulario de 4 campos arriba, botón de llamada, FD#1853, 3 sedes, reseñas de Google con número. — PMM (contenido) / Cliente (publica en WordPress) — 4 h
- [ ] **Landing de funeral / entierro** (`/funeral-services/`): paquetes A/B/C ($3,995 / $4,070 / $3,200), direct burial $1,995, capilla propia (/facilities/). Misma estructura. — PMM / Cliente — 3 h
- [ ] **Página de gracias** `/thank-you/` (noindex) y el formulario de Elementor con acción "Redirect" hacia ella; conversión Form Fill por URL y probada con Tag Assistant. Registrar la fecha. — PMM (necesita acceso a WordPress) — 1 h
- [ ] **Verificar la medición** (playbook §7): que `AW-16758859270` sea el de la cuenta 769-956-1619; qué etiquetas dispara `GTM-MRZ2HJMT` (llamadas, formulario, número de reenvío); duración mínima de llamada; que las acciones locales (direcciones, visitas) estén como secundarias. — PMM — 1 h, bloqueado hasta tener acceso a la cuenta o al contenedor
- [ ] **Un solo teléfono por página de aterrizaje.** La home muestra (951) 696-0626 en el header y (951) 296-0890 (Temecula Cremation & Burial) en el hero: dos números en la primera pantalla, y ninguno es de reenvío. En las landings de Ads debe ir solo el número de reenvío de Google (o uno de call tracking) y el de Temecula solo en su propia landing. — PMM / Cliente — 30 min

## Mejoras (Fase 2–3)
- [ ] **Oferta y precio en la home**: una línea "Cremation packages from $3,015 · Direct cremation from $1,578 · Payment plans" bajo el hero; hoy el único CTA es "Click Here To Call" sin motivo para hacerlo. — Cliente — 1 h
- [ ] **Prueba social con número**: el carrusel de 5 testimonios no dice cuántas reseñas ni la nota; poner "4.8★ en Google · N reseñas" con enlace a la ficha (hoy hay enlace a Maps en el pie). Conseguir el conteo real: PENDIENTE en brief. — PMM/Cliente — 1 h
- [ ] **Velocidad**: TTFB 1.8–2.2 s (nginx, sin cabeceras de caché en el HTML), 74 peticiones y 601 KB en la home; LCP de laboratorio 2.58 s, al borde. Instalar caché de página (WP Rocket o caché de nginx), precargar la imagen del hero móvil (`murrietavalley-header-mobile.webp`) y cargar Montserrat con `font-display: swap` ya está. — Cliente/PMM — 2 h
- [ ] **Veteranos**: /veteran-services/ existe y tiene contenido útil, pero el formulario está a 2,500 px; subirlo bajo el H1 y poner el botón de llamada en el primer bloque. — Cliente — 1 h
- [ ] **Fugas**: menú de 19 ítems y la home dedica su segunda pantalla a "Recent Obituaries" (10 fotos de difuntos) antes que a servicios. En las landings de Ads, menú corto o sin menú. — PMM — en la landing
- [ ] **Sticky de llamada en móvil**: el botón redondo del header no es fijo; al bajar desaparece. Barra inferior "Call (951) 696-0626" fija. — Cliente — 30 min
- [ ] **Español**: no hay ni una línea en español; si el cliente atiende en español (PENDIENTE), una landing ES para "funerarias cerca de mi". — decisión Jhombis/Cliente
- [ ] **Email con otro dominio** (`staffs@murrietavalleyfh.com` en un sitio `.com` distinto): no bloquea, pero conviene unificar. — Cliente — 15 min

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| / | **ninguno** (H2 "Honoring Lives and Telling Unique Stories") | botón "Click Here To Call" en el hero + icono de teléfono en header | Sí, 4 campos (Name, Phone, Email, Message), arranca a 498 px: visible en la primera pantalla | 696-0626 (header, hero, pie) **y 296-0890 (hero, Temecula)** | carrusel de 5 testimonios ★★★★★ sin conteo; enlace a Google Maps en el pie | Segunda pantalla = Recent Obituaries. Sin precio, sin servicios nombrados. |
| /service-options/ | Service Options | "Call Now" al final | Sí, a 2,500 px | 696-0626 | No | Burial y Cremation como párrafos; menciona "Payment Options" (tarjetas). Única página que habla de cremación. |
| /service-pricing/ | Service Pricing | 3 botones a PDF (GPL, Consumer Guide, Casket Price List) | Sí, a 1,300 px | 696-0626 | No | Sin un solo precio en HTML. Dice "variety of payment options". |
| /veteran-services/ | Veteran Services | — | Sí, a 2,500 px | 696-0626 | No | Honores militares, bandera, Riverside National Cemetery. Buena base para el grupo Veteranos. |
| /contact-us/ | Contact Us | formulario | Sí, 4 campos (Name, Phone, Email, Comments) a 209 px | 696-0626 | No | Horario Mon–Fri 8:30–5, Sat 9–4, Sun closed. Email staffs@murrietavalleyfh.com. |
| /testimonials/ | Testimonials | — | No | 696-0626 | 5+ testimonios con ★ | Texto largo, sin conteo ni enlace por reseña. |
| /facilities/ | Facilities | — | No | 696-0626 | fotos | 159 palabras. |
| /our-story/ · /our-staff/ | Our Story · Our Staff | — | Sí (story) | 696-0626 | "family owned", "four decades", staff 24/7 | Dueños Garland y Laurie Shreves; Peter Hamilton. |
| /why-preplan/ · /planning-checklist/ · /where-to-start/ | sí | — | Sí (abajo) | 696-0626 | No | Contenido pre-need e informativo; sirve para un grupo Pre-planning en fase posterior. |
| /obituaries/ + /obituary/* | — | — | No | — | — | ≈60% del tráfico orgánico (Semrush). Excluir de cualquier URL final. |

## Tracking encontrado
- **Google Tag Manager `GTM-MRZ2HJMT`** (head + noscript) en todas las páginas. Contenido del contenedor no verificable desde aquí (proxy bloquea googletagmanager.com).
- **Site Kit by Google 1.179.0**: `gtag('config','GT-TQSRPXK2')` y **`AW-16758859270`**. No aparece ningún `G-` (GA4) en el HTML; si GA4 existe, va dentro del GT- o del GTM. Verificar.
- **Sin** Meta Pixel, CallRail, Clarity ni Hotjar. **Sin** swap de número de reenvío visible en el HTML (si existe, lo hace GTM).
- Formularios: Elementor Pro (`form_fields[name]`, `[field_46d1864]` = Phone, `[email]`, `[message]`), reCAPTCHA cargado, acción AJAX de Elementor, **sin página de gracias** (`/thank-you/`, `/thanks/` → 404). No hay popups de Elementor en el HTML (0).
- Schema: WebPage, WebSite, Organization, BreadcrumbList (Yoast/RankMath). **Sin `LocalBusiness`/`FuneralHome`, sin `openingHours`, sin `aggregateRating`.**

## Velocidad
Laboratorio (Chromium móvil vía proxy, no PSI): **TTFB 1.8–2.2 s** en 3 corridas de curl, **LCP 2.58 s**, CLS 0, DOMContentLoaded 2.8 s, load 3.0 s, **74 peticiones y 601 KB** (JS 226 KB, imágenes 243 KB, CSS 66 KB, HTML 175 KB). Causas: sin caché de página (nginx sin `cache-control`), WordPress 7.1.3 + Elementor 4.1.4 con 26 scripts, hero móvil en webp sin `preload`, 10 fotos de obituarios en la home (lazy). Score PSI: sin dato (cuota agotada sin clave); con LCP ~2.6 s y TTFB ~2 s, la estimación es 50–65 en móvil. No bloquea, pero el TTFB es lo primero que se arregla con caché.

## Medición (playbook §7)
| Punto | Estado | Acción |
|---|---|---|
| Un solo teléfono por página y que sea el de reenvío | ❌ dos números en la home; ninguno de reenvío | Landings con un solo número (reenvío) |
| Formulario de prueba (gracias, correo, conversión en 24–48 h) | ⏳ no se envió (sería un correo real al cliente) | Hacerlo con el cliente avisado |
| Acciones de conversión activas y cuáles son primarias | ⏳ sin acceso a la cuenta | `account_profile.py` cuando haya credenciales |
| Recursos de llamada (no en revisión) | ⏳ sin acceso | ídem |
| Duración mínima de llamada | ⏳ sin acceso | ≥60–90 s en este nicho |
| Horario de atención vs programación | oficina Mon–Fri 8:30–5, Sat 9–4; staff 24/7 según el sitio | Anuncios 24/7 solo si confirman quién contesta de noche |
| Elementor popups / After Submit | 0 popups en el HTML; After Submit = mensaje inline | Cambiar a Redirect → /thank-you/ |

## Landings que la estrategia va a necesitar
| URL | Estado | Para |
|---|---|---|
| `/cremation/` (nueva) | Crear | Ad group Cremación (direct cremation, cremation near me, cremation cost) · F0 |
| `/funeral-services/` (nueva) | Crear | Ad group Funeral / Burial (funeral homes near me, mortuary, burial) · F0 |
| `/veteran-services/` | Mejorar (formulario arriba, llamada arriba) | Ad group Veteranos · F1 |
| `/` | Mejorar (H1, precio, un solo teléfono) | Campaña de marca · F0 |
| `/thank-you/` | Crear + noindex | Conversión Form Fill · F0 |
| `/temecula-cremation/` | Evaluar | Si Temecula Cremation & Burial se anuncia con su propio número |
| `/why-preplan/` | Existe | Grupo Pre-planning · F3 |
| Landing ES "funerarias" | Decisión | Solo si atienden en español |

Cada landing lleva: H1 con el servicio y la ciudad, formulario de 4 campos arriba, botón de llamada fijo con el número de reenvío, FD#1853, "family owned · 40 years · 3 locations", paquetes con precio del GPL, reseñas de Google con número, y sin menú de 19 ítems.

## Qué ya rankea orgánico (Semrush, 2026-10-07)
Marca en #1: "murrieta valley funeral home" 390/mes, "+ murrieta ca 92562" 320, "+ murrieta ca" 140, "murrieta funeral home" 140, "murrieta mortuary" 140, "mortuary murrieta ca" 110, "funeral homes in murrieta ca" 90. Nada de cremación: el sitio no tiene página para ello. ≈60% del tráfico son nombres de difuntos (/obituary/). Para la estrategia: la marca ya tiene demanda propia (campaña de marca barata) y "cremation" hay que comprarlo porque no se rankea.
