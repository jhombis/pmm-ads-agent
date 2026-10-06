---
cliente: Precision Towing
slug: precision-towing
url: https://precisiontowingca.com/
actualizado: 2026-10-06
veredicto: REQUIERE AJUSTES ANTES DE LANZAR
score: 12/22
---

# Auditoría de landing — Precision Towing

> Re-verificación 2026-10-06 (curl de home, /light-medium-duty-towing/, /schedule-a-tow/ y /thank-you/): **sin cambios en el sitio**. Horario sigue en 8–8, /thank-you/ sigue en 404, los formularios siguen sin redirect, sin sellos AAA/NAPA, sin sticky móvil. Novedades fuera del sitio: (1) en Google Ads apareció la conversión "Form Fill" (1 registro) sin página de gracias: hay que ver sobre qué evento dispara antes de contarla como lead; (2) PMM tiene ahora dos vías propias para la landing sin depender del cliente: `/landing-ghl` (GoHighLevel, `scripts/landing_build.py`) y Leadpages (cuenta de PMM conectada, plan Grow, con 2 páginas de otro cliente ya publicadas). Con eso el "bloqueante raíz" deja de ser un bloqueo absoluto: si el acceso a WordPress no llega en la semana del 2026-10-06, las landings de Ads se montan en GHL/Leadpages con formulario corto, página de gracias y conversión propias, y precisiontowingca.com queda como sitio orgánico.

> Método (2026-09-29): 9 páginas descargadas con `curl` y parseadas con Python (WebFetch bloqueado para el dominio). PageSpeed API sin clave devolvió 429 (cuota diaria agotada) y no hay `PAGESPEED_API_KEY`: la velocidad es una **estimación por peso** y hay que confirmarla. Semrush `domain_overview` + `organic_research` (db us) ejecutados; no hay proyecto de `site_audit`. precisionautomotiveus.com y bbb.org bloqueados (no auditados). Archivos fuente en el scratchpad de la sesión (`audit/*.html`, `sizes.txt`).

## Veredicto
La web es limpia, tiene una página por servicio con H1 correcto, teléfono de tracking con `tel:` en todas partes y GTM + gtag de Ads instalados, pero **no existe página de gracias ni ninguna forma de medir el formulario** (Elementor responde con popup, sin redirect), no hay formulario corto arriba del pliegue en ninguna landing, el botón de llamada no es sticky en móvil, faltan sellos/licencia y el horario publicado (8–8) contradice el real (7–10). Nada de esto lo puede corregir PMM en precisiontowingca.com sin acceso de edición; desde el 2026-10-06 la salida es montar las landings de Ads en GoHighLevel o Leadpages (ver nota de re-verificación) si el acceso no llega.

Bloqueantes (rúbrica = 0 o estándar PMM 7): página de gracias / conversión de formulario, acceso de edición web + GTM, verificación con Tag Assistant.

## Bloqueantes (resolver en Fase 0)
- [ ] **Acceso de edición a precisiontowingca.com (WordPress/Elementor) y a GTM-NWQH4MVX**, o nombre de quien aplica cambios — Cliente — 0,5 h. **Plazo: 2026-10-10.** Si no llega, se decide la vía B: landings de Ads en GoHighLevel (`/landing-ghl`) o Leadpages, con dominio propio (p. ej. `go.precisiontowingca.com` requiere CNAME del cliente; sin DNS, subdominio de Leadpages/GHL), formulario de 3 campos, página de gracias y conversiones propias. Los ítems siguientes se resuelven en esa landing en vez de en WordPress — PMM — 4 h
- [ ] **Conversión de formulario medible** (hoy 0 conversiones de formulario configuradas; el envío solo muestra el popup "Your Booking Is Not Yet Confirmed", `triggers: []`, sin `redirect`). Dos vías, elegir según acceso: (a) crear `/thank-you/` (noindex, con teléfono grande y "te llamamos en X min") y poner Redirect en la acción del formulario de `/schedule-a-tow/` y de los 6 formularios "Contact Us" de las páginas de servicio → conversión por URL de destino; (b) si solo hay acceso a GTM: trigger sobre el evento JS `submit_success` de Elementor Pro → etiqueta de conversión en AW-18347302928. Recomendada (a)+(b) — Cliente (web) / PMM (GTM + Ads) — 2 h
- [ ] **Verificar con Tag Assistant** que `AW-18347302928` dispara la conversión "Website Calls" al tocar `tel:(760)6064160` y que la nueva conversión de formulario dispara al enviar; documentar en checklist — PMM — 1 h
- [ ] **Unificar horario**: la landing dice "Monday – Sunday 8 AM – 8 PM" en el footer de las 9 páginas y en `/schedule-a-tow/`; el real es 7 AM – 10 PM. Si Ads anuncia 7–10 y la web dice 8–8, el usuario duda y no llama a las 9 PM. Cambio de un texto en el footer template de Elementor (ID 51) — Cliente / PMM si consigue acceso — 0,25 h

## Mejoras (Fase 2–3)
Prioridad alta (hacer en Fase 1 en cuanto haya acceso; suben el score en 5–6 puntos):
- [ ] **Reescribir la landing estrella `/light-medium-duty-towing/`** para que refleje lo que la gente busca: H1 tipo "Tow Truck in Lake Isabella & the Kern River Valley — Call Now, We Dispatch Directly" (los términos que convierten hoy son "tow truck", "towing near me", "towing lake isabella", "kernville towing"; nadie busca "light & medium-duty"). Primer bloque: teléfono grande + 2 líneas de promesa (respuesta directa, 33 años, X trucks) + lista de comunidades (Lake Isabella, Kernville, Wofford Heights, Bodfish, Weldon, Mountain Mesa, Hwy 178/155) — PMM redacta / Cliente publica — 2 h
- [ ] **Formulario corto arriba del pliegue** en la landing estrella y en roadside: 3 campos (Name, Phone, "Where are you? / What happened?") justo debajo del H1, con texto "We call you back in 5 min". Hoy el formulario de 4 campos de las páginas de servicio está al final, después del texto, del CTA y de dos bloques de Quick Links; el de `/schedule-a-tow/` tiene 9 campos (largo para una emergencia) — Cliente — 1 h
- [ ] **Botón de llamada sticky en móvil**: la sección del header `0cb3e2e` tiene `sticky: top` solo con `sticky_on: ["desktop"]`. Activar sticky en mobile/tablet o añadir una barra inferior fija "Call (760) 606-4160" — Cliente — 0,5 h
- [ ] **Sellos y confianza**: AAA Approved Auto Repair, NAPA AutoCare, California Gold Seal Smog Check no aparecen en ninguna de las 9 páginas (búsqueda de "AAA", "NAPA", "Smog", "licensed", "insured": 0 resultados). Añadir franja de logos bajo el hero + línea "Licensed & insured · CHP permit #…" cuando el cliente confirme el permiso — Cliente — 1 h
- [ ] **Prueba social con número**: hay 8 reseñas de 5★ con nombre en carrusel (home y `/reviews/`), pero sin agregado ("4.8★ · 850+ Google reviews"), sin fotos y solo en 2 de 9 páginas; 3 de las 8 hablan del taller (Tony, Cindy, Sabrina) y 1 es genérica. Poner "4.8★ Google · 850+ reviews" en el hero de todas las páginas de servicio y seleccionar las 4 reseñas de grúa (Celina, Sean, Crystal, Junior) para las landings de towing — PMM selecciona / Cliente publica — 1 h
- [ ] **Oferta concreta**: lo único visible es "Get A Free Quote". Para emergencia, la oferta es tiempo: "Direct dispatch — no call center · ETA on the phone · After-hours available". Confirmar con el cliente ETA promedio y si puede prometer "we answer 7 AM–10 PM, 7 days" — Cliente decide / PMM redacta — 0,5 h

Prioridad media:
- [ ] `/5th-wheel-towing/` y `/travel-trailer-towing/`: añadir una frase de intención ("We tow your 5th wheel or travel trailer to/from campgrounds, storage or repair — we do not sell or install hitches") para filtrar la intención de compra que hoy consume presupuesto (hitch, cargo trailer, toy hauler) — Cliente — 0,5 h
- [ ] `/roadside-assistance/`: listar explícitamente jump start, lockout, flat tire change, fuel delivery, winch-out; el H1 genérico no conecta con esas búsquedas — Cliente — 0,5 h
- [ ] **Velocidad**: hero desktop `precision-towing-header.jpg` (477 KB, 1920×760 JPEG) y hero móvil (266 KB) están ambos en el DOM y se descargan los dos en móvil; convertir a WebP ≤120 KB, servir solo uno por breakpoint, `fetchpriority="high"` en el LCP; recortar las 3 familias de Google Fonts (Russo One, Bai Jamjuree, Days One pedidas con 18 pesos cada una) a 2 pesos; activar caché de navegador (no hay `cache-control` ni `expires` en ningún asset) y compresión/caché a nivel de servidor o CDN (nginx/Plesk sin CDN) — Cliente / hosting — 2 h
- [ ] Reducir fugas: menú de 10 ítems duplicado (barra desktop + barra móvil se renderizan ambas en móvil, logo dos veces), dos bloques "Quick Links" repetidos en cada página de servicio, y en las landings de Ads el botón "Get A Free Quote" saca al usuario a `/schedule-a-tow/` (9 campos). En las landings pagadas: menú reducido, sin Quick Links, CTA primario = llamar — Cliente — 1 h
- [ ] Bug del formulario de `/schedule-a-tow/`: el campo "Desired Date/Time" tiene `name="form_fields[email]"` y el campo Email es `type="text"` (sin validación); si Elementor usa el campo `email` como reply-to, las respuestas del cliente van a una fecha. Corregir IDs — Cliente — 0,25 h
- [ ] Home sin `<h1>` (solo H2 "Lake Isabella's Most Trusted Towing & Auto Care"), sin meta description en ninguna página, sin schema LocalBusiness. No afecta a Ads directamente; sí a marca y a la calidad percibida — Cliente — 0,5 h

Prioridad baja / fase futura:
- [ ] Página de marca: `/reviews/` sirve de landing para campaña de marca solo si se le añade teléfono arriba y agregado de reseñas.
- [ ] Confirmar destino real de los envíos (la página muestra amirepair22@gmail.com; las acciones del formulario son server-side y no se ven en el HTML).

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| `/` | **Ninguno** (H2 "Lake Isabella's Most Trusted Towing & Auto Care") | "Get A Free Quote" → /schedule-a-tow/ + "Call Now" (header, hero, bloque "Dependable Care") | **No** | Sí, `tel:(760)6064160` ×7 (header desktop, icono header móvil, 2 botones, footer) | Carrusel 8 reseñas 5★ con nombre, sin agregado ni fotos | Hero 1920×760 JPEG 477 KB + móvil 266 KB; 5 tarjetas de servicio duplicadas (desktop/móvil); "33 Years", "After-Hours Emergency Towing", "Local, Direct Service"; horario 8–8 |
| `/light-medium-duty-towing/` | "Light & Medium-Duty Towing" | Quote + Call Now tras 3 párrafos | Sí, 4 campos (Name*, Phone*, Email*, Message), **al final de la página** | Sí ×5 | Ninguna en la página | Landing estrella. Copy genérico, sin comunidades, sin sellos, sin ETA. Requiere reescritura (ver Mejoras) |
| `/5th-wheel-towing/` | "5th Wheel Towing" | Quote + Call Now | Sí, 4 campos, al final | Sí ×5 | Ninguna | Sin filtro de intención (compra vs remolque) |
| `/travel-trailer-towing/` | "Travel Trailer Towing" | Quote + Call Now | Sí, 4 campos, al final | Sí ×5 | Ninguna | Ídem. Candidata a fusionarse con 5th wheel en un solo ad group |
| `/roadside-assistance/` | "Roadside Assistance" | Quote + Call Now | Sí, 4 campos, al final | Sí ×5 | Ninguna | No enumera jump start / lockout / flat tire en H2 |
| `/auto-repair-collision-service/` | "Auto Repair & Collision Service" | Quote + Call Now | Sí, 4 campos, al final | Sí ×5 | Ninguna | Sin campaña en Fase 1; no se usa como landing |
| `/reviews/` | Ninguno (H2 "What People Are Saying About Us") | Solo header/footer | No | Sí ×4 | 8 reseñas 5★ (mismas que home) + imagen "Review us on Google" + link externo a Google | Posible landing de marca con ajustes |
| `/schedule-a-tow/` | "Schedule A Tow" | Header/footer | **9 campos** (Name*, Phone*, Email*, Vehicle Y/M/M, Service Needed, Pick Up, Drop Off, Desired Date/Time, Comments); sin redirect; popup "Your Booking Is Not Yet Confirmed — Please give us a call" | Sí ×4 + teléfono en texto | Ninguna | Muestra email amirepair22@gmail.com, dirección y horario 8–8. Bug de IDs de campos |
| `/about-us/` | "About Us" | Quote + Call Now | Sí, 4 campos, al final | Sí ×5 | Ninguna | "33 years", "17-bay", "no third-party dispatch" |
| `/thank-you/`, `/thanks/`, `/gracias/`, `/contact/`, `/contact-us/`, `/thankyou/`, `/booking-confirmed/`, `/confirmation/` | — | — | — | — | — | **404**. Sitemap (`wp-sitemap-posts-page-1.xml`) confirma 10 páginas: las 9 anteriores + `/privacy-policy/`. No hay páginas por ciudad |

Común a todas: header con "Get A Free Quote" + "Call Now (760) 606-4160" (sticky solo en desktop), barra móvil adicional con icono de teléfono, menú de 10 ítems, footer con teléfono, horario 8–8, link externo a Google (`share.google/...`), popup Elementor 1704 sin triggers automáticos (solo post-envío). Sin meta description en ninguna. Título de pestaña "<Servicio> – Precision Towing". Sin `ld+json`.

## Rúbrica
| Ítem | Puntos | Evidencia |
|---|---|---|
| Headline refleja el servicio buscado | 1 | H1 por servicio, pero con jerga ("Light & Medium-Duty") y home sin H1; los términos que convierten son "tow truck", "towing near me", "kernville towing" |
| Formulario corto visible arriba (móvil) | 1 | Existe form de 4 campos en páginas de servicio, pero al final de la página; home sin form; schedule 9 campos |
| Clic para llamar en móvil | 1 | Botón "Call Now" en header visible al cargar + icono; **no sticky en móvil** (`sticky_on: desktop`) |
| Oferta clara | 1 | Solo "Get A Free Quote"; sin ETA, sin "24/7" real, sin precio orientativo |
| Prueba social | 1 | 8 reseñas 5★ con nombre en home y /reviews/; sin agregado (4,8★ / ~850), sin fotos, ausente en páginas de servicio |
| Confianza | 1 | "33 years", "17-bay", "no call center"; sin licencia/CHP, seguro, ni sellos AAA/NAPA/Gold Seal |
| Velocidad móvil | 1 | **Estimación** (ver abajo): ~2 MB transferidos, TTFB 1,6–2,1 s, sin caché; score estimado 35–55, LCP > 2,5 s. No se puede afirmar < 40 → no bloqueante hasta medir |
| Google Tag presente | 2 | GTM-NWQH4MVX + gtag GT-NCTDVBBQ (Site Kit) + `gtag('config','AW-18347302928')` en las 9 páginas |
| Página de gracias medible | **0** | No existe; form responde con popup; sin redirect. **Bloqueante** |
| Páginas por servicio | 2 | Una por cada uno de los 5 servicios |
| Sin fugas | 1 | Menú de 10 ítems (×2 en móvil), Quick Links duplicados, link externo a Google en footer, CTA que saca de la landing a un form de 9 campos; sin pop-ups agresivos |
| **Total** | **12/22** | |

## Tracking encontrado
- **GTM-NWQH4MVX**: `gtm.js` en `<head>` + iframe `ns.html` en `<body>`, en las 9 páginas. Contenido del contenedor no verificable sin acceso.
- **gtag (Google Site Kit)**: `googletagmanager.com/gtag/js?id=GT-NCTDVBBQ` con `gtag('config','GT-NCTDVBBQ')` y **`gtag('config','AW-18347302928')`** (cuenta de Ads 753-255-2245, confirmado propio). `gtag('set','linker',{domains:['precisiontowingca.com']})`. Site Kit también carga `googlesitekit-events-provider-content-events` (eventos automáticos de formularios de Site Kit; no equivale a una conversión de Ads).
- **GA4 (`G-`)**: no visible en el HTML; puede estar dentro del tag GT- o de GTM. Sin acceso no se confirma.
- **Meta Pixel (`fbq`)**, Clarity, Hotjar, CallRail/CTM: **ninguno**. El teléfono (760) 606-4160 es estático (sin script de DNI): el call tracking es un número de reenvío fijo, sirve igual para Ads.
- **Conversiones**: "Website Calls" (clic en `tel:` medido por AW-18347302928) funciona (7 conv. históricas). **No hay conversión de formulario** y no hay URL de gracias sobre la que crearla. Plugin de formularios: Elementor Pro (`elementor-form`, `method="post"`, acción server-side; `data-settings` sin `redirect_to`).
- Elementor Pro 4.1.0, Elementor 4.3.2, tema Hello Elementor 3.4.9, WordPress con Site Kit, PHP 8.3.35 sobre nginx/Plesk.

## Velocidad
**No medida — estimación por peso y tiempos de curl.** PageSpeed API sin clave: HTTP 429 (cuota diaria del proyecto público agotada); `PAGESPEED_API_KEY` no definida en el entorno. Pedir a Jhombis correr PSI móvil de `https://precisiontowingca.com/` y de `/light-medium-duty-towing/` o definir la clave para `scripts/pagespeed.py`.

Datos medidos (home):
- HTML 151 KB sin comprimir → 27 KB gzip. TTFB 1,6–2,1 s en 3 muestras (a través del proxy de la sesión; el TTFB real probablemente 0,8–1,5 s). Sin CDN, sin `cache-control`/`expires` en imágenes ni JS/CSS.
- 60 recursos referenciados, **2,65 MB sin comprimir**. Imágenes ≈ 1,8 MB (hero desktop JPEG 477 KB + hero móvil JPEG 266 KB, ambos en el DOM y ambos descargados en móvil; `image1.webp` 201 KB, `image2.webp` 224 KB, 5 thumbnails WebP 99–138 KB = 595 KB, logo PNG 32 KB cargado dos veces). JS ≈ 470 KB raw (Swiper 144 → 38 KB gz, jQuery 88 → 30 KB gz, Elementor frontend/pro ~180 KB, jQuery UI, smartmenus, sticky). CSS ≈ 330 KB raw. 3 familias de Google Fonts pedidas con 18 variantes cada una.
- Transferencia estimada en móvil: **~2,0–2,2 MB**, de los cuales ~1,8 MB son imágenes no cacheables.

Estimación: score móvil **35–55**, LCP **3,5–5 s** en 4G (hero JPEG grande, sin `fetchpriority`, fuentes bloqueantes), CLS bajo (imágenes con width/height). Causas principales por orden: peso de imágenes hero (doble hero), sin caché/CDN, fuentes, TTFB. No se marca como bloqueante porque no se puede confirmar score < 40; queda en Mejoras con prioridad media y **"PENDIENTE medir"** en el checklist.

## Landings que la estrategia va a necesitar

**Actualización 2026-10-06**: la estrategia v2 pasa a **una sola campaña con 4 grupos** (límite de fragmentación del playbook para $600–1.500/mes). Cambia el mapa: AG1 Tow Truck & Towing KRV (incluye las ciudades por inserción de keyword) → landing estrella; AG2 Roadside → /roadside-assistance/; AG3 RV & Trailer → /5th-wheel-towing/ y /travel-trailer-towing/; AG4 Marca → home. Si se va por GHL/Leadpages, son **3 landings propias + 1 página de gracias** (towing, roadside, trailer) y la marca sigue a la home del sitio actual.
Contexto: mercado rural (Kern River Valley, radio 21 mi), $825/mes, 76 clics en 6 semanas, CPC $13,80. Con ese volumen **no se justifican landings por ciudad**: "kernville towing" (6 conv) es el único término geográfico con tracción y se resuelve mencionando las comunidades en la landing estrella y en los ad groups, no con páginas separadas. Las 5 páginas de servicio ya existen; lo que falta es una página nueva y reescribir una.

| # | Landing | Estado | Campaña / ad group que la usará | Acción |
|---|---|---|---|---|
| 1 | `/light-medium-duty-towing/` → landing "Tow Truck / Towing Lake Isabella & Kern River Valley" | Existe, **reescribir** | Search — Towing (ad groups: towing general, tow truck near me, towing + comunidades Lake Isabella/Kernville/Wofford Heights/Bodfish/Weldon/Mountain Mesa) | H1 con el término buscado, teléfono + ETA arriba, form 3 campos, comunidades y Hwy 178/155, sellos, 3 reseñas de towing, agregado 4,8★ |
| 2 | `/roadside-assistance/` | Existe, ajustar | Search — Roadside (jump start, lockout, flat tire, fuel, winch-out) | Enumerar servicios en H2, mismo bloque de conversión que #1 |
| 3 | `/5th-wheel-towing/` (cubriendo también travel trailer) o ambas páginas | Existen, ajustar | Search — RV/Trailer Towing (un solo ad group, frase; bajo volumen) | Frase de intención "we tow, we don't sell/install", mismo bloque de conversión. Si se fusionan, `/travel-trailer-towing/` redirige a `/5th-wheel-towing/` |
| 4 | `/` (home) | Existe | Search — Marca ("precision towing", "precision automotive lake isabella") | Añadir H1, agregado de reseñas y horario real; sin más cambios |
| 5 | `/thank-you/` | **No existe, crear** | Todas (conversión de formulario) | Noindex, teléfono grande, "we'll call you back in 5 minutes", sin menú |
| — | `/auto-repair-collision-service/` | Existe | Sin campaña en Fase 1 | Nada por ahora |
| — | Landings por ciudad (Kernville, Wofford Heights, Bodfish, Weldon, Mountain Mesa) | No crear | — | Volumen insuficiente; revisar en el día 90 si algún término ciudad+towing supera ~10 conv/mes |

Resumen: **1 landing nueva (`/thank-you/`) + 1 reescritura profunda (estrella) + 3 ajustes ligeros; 0 landings por ciudad.**

## Qué ya rankea orgánico (Semrush)
`domain_rank` (db us): Semrush Rank 23.272.516, **4 keywords orgánicas, 0 tráfico orgánico estimado, 0 keywords de pago detectadas**. Sitio nuevo (uploads de agosto 2026), sin autoridad; la estrategia no puede apoyarse en relevancia orgánica previa.

`resource_organic` (db us):

| Keyword | Pos. | Vol. | CPC | URL |
|---|---|---|---|---|
| precision towing | 51 | 2.400 | $2,15 | /light-medium-duty-towing/ |
| precision towing inc | 54 | 90 | — | / |
| precision towing palm bay | 37 / 42 | 40 | — | / |

Lectura para /strategy: no rankea por ningún término no-marca. "precision towing" tiene 2.400 búsquedas/mes **nacionales** porque hay varias empresas homónimas (Precision Towing Palm Bay FL, "Precision Towing Inc"): la campaña de marca debe ir con geotarget estricto de presencia y variantes locales ("precision towing lake isabella", "precision automotive lake isabella", "precision automotive towing"), y negativar "palm bay" y otras ciudades ajenas. Semrush `site_audit` no disponible (dominio sin proyecto).

## Datos no obtenidos y por qué
- Score PageSpeed real: API sin clave con cuota agotada (429); no hay `PAGESPEED_API_KEY`.
- Contenido de GTM-NWQH4MVX y presencia de GA4: sin acceso al contenedor.
- Destino real del formulario y acciones post-envío: son server-side de Elementor Pro; solo se ve el popup.
- precisionautomotiveus.com (sitio del taller, fuente de sellos) y BBB: dominios bloqueados en esta sesión.
- Semrush `site_audit`: sin proyecto configurado para el dominio.
