---
cliente: 290 Tow and Recovery
slug: 290-tow-recovery
url: https://290towrecovery.com/
actualizado: 2026-10-06
version: 3
veredicto: REQUIERE AJUSTES ANTES DE LANZAR
score: 12/22
---

# Auditoría de landing — 290 Tow and Recovery

> **Método (2026-10-06, tercera pasada):** el sitio ya es accesible desde el entorno.
> - Se leyó el HTML de las 9 páginas con `scripts/site_scan.py` → `data/site-scan.json`.
> - Se revisó el HTML de home, about, exotic y schedule-a-tow.
> - Se probaron las URLs de página de gracias (`/thank-you/`, `/thank-you-page/`, `/gracias/`: todas dan 404).
> - Se corrió PageSpeed móvil sobre home, light-medium y exotic → `data/pagespeed.json`.
>
> Sigue sin verificar: qué eventos de conversión disparan al hacer clic o enviar. Eso solo se ve con Tag Assistant.

## Veredicto
**Requiere ajustes antes de lanzar la reestructuración.**
- El sitio sirve para llamadas: el teléfono está en el header y hay botones "Call Now" en todas las páginas, con una página por servicio.
- El formulario se mide sin página de gracias (corrección del 06-oct). En el `<head>` hay un script que, con el evento `submit_success` de Elementor (solo se dispara cuando el envío pasa la validación del captcha en el servidor), empuja `gtm.formSubmit` al dataLayer. Jhombis lo usa en vez de `/thank-you/`. Falta probar el disparo con Tag Assistant.
- Al enviar sale un popup de Elementor ("Your Booking Is Not Yet Confirmed – Please give us a call at (830) 463-8318 now to confirm!"). Es un tema de experiencia, no de medición.
- El home móvil empeoró: score 43, LCP 6.7 s, TBT 1,170 ms.

**Corrección respecto de la versión del 23/09:** la página `/exotic-vehicle-towing/` **sí tiene** los CTA "Get A Free Quote" y "Call Now (830) 463-8318" en el HTML, después del texto. El "bloque vacío" de la captura de PageSpeed era un render incompleto, no un error del sitio, así que **deja de ser bloqueante**. Las keywords exotic pueden activarse.

## Bloqueantes (resolver en Fase 0)
- [ ] **Probar el disparo de Form Fill** (reemplaza a `/thank-you/`, decisión de Jhombis del 06-oct). Con GTM Preview y Tag Assistant:
  - un envío válido dispara la conversión **1 vez**;
  - un envío con el captcha fallido o con campos inválidos **no** la dispara;
  - ningún trigger nativo de "Form Submission" de GTM dispara también. Eso duplicaría el conteo, porque `gtm.formSubmit` es el nombre que usa ese trigger.
  - En Ads, el recuento de la acción tiene que ser "Una".
  - Responsable: PMM. Esfuerzo: 0.5 h.
- [ ] **Verificar conversiones con Tag Assistant**:
  - "Calls from Ads" (umbral 60 s)
  - "Website Calls" (clic en `tel:(830)4638318`)
  - "Form Fill"
  - Confirmar que AW-18397446767 es de la cuenta 213-019-5545.
  - Responsable: PMM. Esfuerzo: 1 h.

## Mejoras (Fase 2–3)
- [ ] **H1 del home**:
  - Hoy no hay ningún `<h1>`: el titular "Serving Texas with Honor & Integrity" es una imagen sin `alt`.
  - Poner un H1 de texto: "24/7 Towing & Tow Truck Service in Fredericksburg, TX".
  - (PMM, 0.5 h)
- [ ] **Velocidad móvil del home** (score 43, LCP 6.7 s, TBT 1,170 ms, 2.2 MB):
  - convertir el hero de imagen a texto
  - WebP y caché
  - quitar el JS/CSS de Elementor que no se usa
  - Objetivo: LCP < 3 s. (PMM, 2 h)
- [ ] **Confianza visible en texto**:
  - "Navy Veteran Owned & Operated", "10% Senior Discount" y el radio de servicio hoy están solo en la imagen del hero.
  - Pasarlos a texto y sumar licencia TDLR # + "Licensed & Insured" cuando el cliente los confirme.
  - (PMM + dato del cliente)
- [ ] **Prueba social**: cero reseñas en el sitio y sin `aggregateRating`. Depende del GBP. Mientras tanto, 3 testimonios reales con nombre. (Cliente)
- [ ] **SEO técnico**:
  - Sin `meta description` en ninguna página.
  - Sin JSON-LD `LocalBusiness`/`TowingService` (horario 24/7, `areaServed`, teléfono).
  - Imágenes sin `alt`.
  - (PMM, 1 h)
- [ ] **Formularios**:
  - El de "Contact Us" tiene 4 campos (Name, Phone, Email, Message) y está al final.
  - El de "Schedule A Tow" tiene 9: Name, Phone, Email, Vehicle Year/Make/Model, Service Needed, Pick Up Location, Drop Off Location, Desired Date/Time, Comments.
  - Para emergencias basta con Name, Phone y Location.
  - (PMM, 0.5 h)
- [ ] **Oferta**: sumar "Upfront price on the phone — no hidden fees" al hero y a los callouts, si el cliente lo confirma.

## Rúbrica
| Ítem | Puntaje | Evidencia (2026-10-06) |
|---|---|---|
| Headline refleja el servicio buscado | 1 | Páginas de servicio con H1 = servicio, sin ciudad. Home sin H1 (hero en imagen) |
| Formulario corto visible arriba (móvil) | 1 | 4 campos, al final de cada página. Schedule A Tow: 9 campos |
| Clic para llamar en móvil | 2 | `tel:(830)4638318` en header, botones "Call Now" y footer en las 9 páginas |
| Oferta clara | 1 | "Get A Free Quote". El 10% senior discount solo está en la imagen |
| Prueba social | 0 | Sin reseñas, sin estrellas, sin testimonios |
| Confianza | 1 | "Available 24/7" en texto. Navy Veteran solo en imagen. Sin TDLR ni seguro |
| Velocidad móvil | 1 | Home 43 · light-medium 55 · exotic 62 (no bloquea: ninguna <40) |
| Google Tag presente | 2 | GTM-WBX4RZ9K y AW-18397446767 en el HTML de todas las páginas. GA4 G-KH9SFWZK66 carga vía GTM |
| Conversión de formulario medible | 1 | Sin página de gracias (decisión). Script `submit_success` → `gtm.formSubmit` después de validar el captcha. Falta probarlo con Tag Assistant: sube a 2 si pasa |
| Páginas por servicio | 2 | 4 servicios + about + schedule-a-tow |
| Sin fugas | 1 | Sin links externos. Popup de "booking" después de enviar |
| **Total** | **13/22** | |

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| `/` | **ninguno** (H2 "Trustworthy Towing in Fredericksburg & Beyond") | Get A Free Quote · Call Now (×3) | No | Header + botones + footer | No | Hero en imagen. 461 palabras |
| `/light-medium-duty-towing/` | Light & Medium-Duty Towing | Get A Free Quote · Call Now | 4 campos | Sí | No | Landing de wrecker y sitelink |
| `/exotic-vehicle-towing/` | Exotic Vehicle Towing | Get A Free Quote · Call Now (**verificado en HTML**) | 4 campos | Sí | No | Ya no bloquea |
| `/local-long-distance-towing/` | Local & Long-Distance Towing | Get A Free Quote · Call Now | 4 campos | Sí | No | |
| `/roadside-assistance/` | Roadside Assistance | Get A Free Quote · Call Now | 4 campos | Sí | No | |
| `/about-us/` | About Us | Get A Free Quote · Call Now | 4 campos | Sí | No | **Confirma "rollback and wrecker trucks"** (flatbed = rollback) |
| `/schedule-a-tow/` | Schedule A Tow | Submit | **9 campos** | Sí | No | Útil para long-distance programado |
| `/privacy-policy/` | Privacy Policy | — | — | Sí | — | Email 290towandrecovery@gmail.com |

Plataforma: WordPress + Elementor Pro, tema Hello Elementor, Google Site Kit. La edita PMM.

## Tracking encontrado
- En el HTML de todas las páginas: `GTM-WBX4RZ9K` y `AW-18397446767` (gtag).
- GA4 `G-KH9SFWZK66` carga vía GTM/Site Kit: se ve en las requests de PageSpeed del 23/09, no en el HTML.
- Teléfono único en todo el sitio: (830) 463-8318. No hay número de reenvío dinámico, así que "Website Calls" se mide por clic en `tel:`.
- Sin Meta Pixel, CallRail, Clarity ni Hotjar.
- Formulario Elementor sin `action` (AJAX). "After Submit" = popup "Your Booking Is Not Yet Confirmed".
- Script en el `<head>`: `jQuery(document).on('submit_success', 'form[class^="elementor-form"]', …)`, que hace `dataLayer.push({event: 'gtm.formSubmit', 'gtm.elementId': …})`. Es la fuente de Form Fill.

## Velocidad (PageSpeed móvil, 2026-10-06)
| Página | Score | LCP | CLS | TBT | Peso |
|---|---|---|---|---|---|
| `/` | **43** | 6.7 s | 0 | 1,170 ms | 2.2 MB |
| `/light-medium-duty-towing/` | 55 | 5.9 s | 0.001 | 680 ms | 2.7 MB |
| `/exotic-vehicle-towing/` | 62 | 5.9 s | 0.031 | 350 ms | 2.4 MB |

El 23/09 el home midió 55–79. La caída a 43 viene del TBT (JS). Las causas son las mismas: imágenes hero pesadas y CSS/JS de Elementor sin usar. Si el score baja de 40, pasa a bloqueante.

## Landings que la estrategia va a necesitar
| URL | Estado | Para |
|---|---|---|
| `/` | Mejora (H1 de texto + velocidad) | AG1 Towing |
| `/exotic-vehicle-towing/` | Lista (CTA verificados) | AG2, keywords exotic |
| `/local-long-distance-towing/` | Lista | AG2, keywords long-distance |
| `/roadside-assistance/` | Lista | AG3 Roadside |
| ~~`/thank-you/`~~ | No se crea (decisión de Jhombis): Form Fill sale del script `submit_success` | — |

## Qué ya rankea orgánico (Semrush, 2026-09-23)
- 5 keywords, tráfico ≈ 0. La única con posición es "highway 290 wrecker service": posición 44 con `/light-medium-duty-towing/`.
- Sin `meta description` ni schema, así que el orgánico no va a mejorar solo.
