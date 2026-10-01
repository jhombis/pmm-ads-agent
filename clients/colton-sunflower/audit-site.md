---
cliente: Colton Sunflower Burial and Cremation
slug: colton-sunflower
url: https://coltonfuneral.com/
actualizado: 2026-10-01
veredicto: REQUIERE AJUSTES ANTES DE LANZAR (antes del relanzamiento de Fase 1; la campaña actual sigue activa)
score: 12/22
---

# Auditoría de landing — Colton Sunflower Burial and Cremation

## Veredicto
El sitio tiene una **oferta muy fuerte**: precios publicados desde $1,175, crematorio propio, licencia FD2479 y 24/7. Pero **no se puede medir el formulario** (no hay página de gracias) y la home, que es la URL final de varios anuncios, **no tiene formulario**. Esos dos puntos son bloqueantes para pasar a Maximizar conversiones.

## Bloqueantes (resolver en Fase 0)
- [ ] **Página de gracias medible**: el formulario de Elementor muestra un mensaje en la misma página y /thank-you/ da 404. Hacer que redirija a `/thank-you/` y crear la conversión "Form Fill" por URL; o, como alternativa, un evento de GTM en `submit_success` de Elementor. — PMM — 1–2 h
- [ ] **Formulario en las URL finales**: la home y /pricing/ no tienen formulario, y en /cremation/ y /burial/ está al final de la página. Agregar formulario corto arriba (o un botón "Get Pricing / Arrange Now" que haga scroll a él) y cambiar las URL finales de los anuncios a páginas con formulario. — PMM (si tiene acceso a WordPress) o Cliente — 2–3 h
- [ ] **Formulario más corto**: hoy tiene 4 campos y todos son obligatorios, incluido "Message". Dejar Nombre + Teléfono obligatorios y Email + Mensaje opcionales. — PMM/Cliente — 15 min

## Mejoras (Fase 2–3)
- [ ] **Prueba social**: no hay reseñas en el sitio. Agregar un widget de reseñas de Google (estrellas + número) cerca del hero y de los precios. — Cliente/PMM — 1 h
- [ ] **H1**: la home y /pricing/ no tienen H1, y el de /cremation/ dice solo "Cremation". Usar "Affordable Cremation & Burial in Colton, CA" en la home y "Cremation Services in Colton, CA — From $1,175" en /cremation/. — PMM — 30 min
- [ ] **Botón de llamada sticky en móvil**: el header es sticky solo en desktop (`sticky_on: desktop`). Activarlo también en móvil o agregar una barra inferior "Call Now". — PMM — 30 min
- [ ] **Velocidad**: el TTFB es de 1.3–3.5 s y no hay caché de página (nginx/Plesk, PHP 8.3, sin cabeceras de caché). La página pesa ~1.3 MB en 47 requests (Elementor + JetEngine + JetElements, tweenjs 112 KB). Instalar caché de página (WP Rocket o LiteSpeed/Redis según el hosting), quitar JetElements/tweenjs si no se usan y precargar la imagen del hero móvil. — PMM — 2–3 h
- [ ] **"Arrange Online"** lleva a /contact-us/, que es solo un formulario. Renombrarlo "Request Arrangements" o crear un arreglo online real; hoy la expectativa no se cumple. — Cliente — decisión
- [ ] **Email de contacto** `Garland@murrietavalleyfh.com` (dominio de Murrieta Valley FH) en /contact-us/: confunde a la familia. Usar un correo del dominio coltonfuneral.com. — Cliente — 15 min
- [ ] **Fugas**: menú de 10 ítems y el GPL en PDF. Aceptable en una funeraria; no tocar por ahora.

## Rúbrica
| Ítem | Puntos | Nota |
|---|---|---|
| Headline refleja el servicio | 1 | Hay páginas por servicio, pero falta H1 en la home y en /pricing/; el de /cremation/ es genérico |
| Formulario corto visible arriba (móvil) | **0** | La home y /pricing/ no tienen; en el resto está al pie, con 4 campos obligatorios |
| Clic para llamar en móvil | 1 | Botón "Call Now" en el header, pero no es sticky en móvil |
| Oferta clara | 2 | Simple Cremation $1,175 · Direct Burial $1,995 · 7 paquetes con precio |
| Prueba social | 0 | Sin reseñas ni estrellas |
| Confianza | 2 | Licencia FD2479, family-owned, crematorio propio, 24/7, GPL público |
| Velocidad móvil | 1 | Estimada (no se pudo medir el LCP, ver abajo). TTFB alto |
| Google Tag | 2 | AW-18369353359 + GT-578K2F5D (Site Kit) + GTM-K98Q3DKL |
| Página de gracias medible | **0** | No existe (Elementor inline; /thank-you/ 404) |
| Páginas por servicio | 2 | /cremation/, /burial/, /pricing/, /pre-planning/ |
| Sin fugas | 1 | Menú grande; email de otro dominio |
| **Total** | **12/22** | |

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| / | — (H2: "Affordable Burial and Cremation in Colton, CA") | View Pricing · Call Now · Arrange Online | **No** | (909) 254-4100 header + footer | No | Muestra $1,175 y $1,995; "never leaves our care" |
| /cremation/ | Cremation | igual | Sí, al pie (4 campos, reCAPTCHA) | Sí | No | Crematorio propio, witness cremation, viewing, capilla |
| /pricing/ | — | Call Now por paquete | **No** | Sí | No | 7 paquetes + 2 de veteranos ($1,350 / $2,800) + graveside $3,900 |
| /burial/ | — (H2 "Chapel Funeral Services in Colton, CA") | igual | Sí, al pie | Sí | No | Coordina con hospitales, cementerios y el coroner |
| /contact-us/ | — ("Immediate Assistance – Available 24 Hours") | Form | Sí | Sí + (800) 848-0905 | No | Email @murrietavalleyfh.com |
| /pre-planning/ | Funeral Pre-Planning in Colton | | Sí | Sí | No | **Vende preneed → no negativizar "prepaid"/"pre-planning"** |

## Tracking encontrado
- Google Site Kit: `gtag config GT-578K2F5D` + `AW-18369353359`. Verificar que el AW sea el de la cuenta 151-776-2744.
- GTM: `GTM-K98Q3DKL` (con noscript).
- reCAPTCHA en los formularios.
- No hay píxel de Meta ni call tracking de terceros (CallRail, etc.).
- La cuenta registra "Website Calls" y "Calls from Ads", pero **ninguna conversión de formulario**, que es consistente con que no haya página de gracias.

## Velocidad
- No se pudo medir LCP/score: no hay `PAGESPEED_API_KEY` y Chromium no valida el certificado del sitio a través del proxy del entorno. Pedir el score a Jhombis (pagespeed.web.dev) o configurar la clave.
- Estimación: HTML 106 KB + 47 recursos ≈ 1.3 MB (JS 484 KB, CSS 362 KB, imágenes 329 KB). TTFB medido 1.3–3.5 s **sin caché de página**. Con 3 scripts bloqueantes en `<head>`, el LCP móvil probablemente quede en 3–5 s (score estimado 40–60). **No se considera bloqueante** porque no se pudo confirmar un score menor a 40, pero es la mejora técnica con más impacto.
- Imagen del hero móvil `colton-header-mobile.webp` (88 KB): conviene precargarla.

## Landings que la estrategia va a necesitar
| Ad group | URL recomendada | Estado |
|---|---|---|
| Cremation - Direct & Affordable | /cremation/ (con formulario arriba) | Existe; falta subir el formulario |
| Cremation - Cost & Prices | **/pricing/** | Existe, con precios. Falta formulario y H1 |
| Cremation With Service | /pricing/ (ancla a "Cremation with Memorial Service $2,600") o /cremation/ | Existe |
| Funeral Home | / (agregar formulario) o /burial/ | Falta formulario en la home |
| Burial Services | **/burial/** | Existe; formulario al pie |
| (Futuro) Veteranos | /pricing/#veteran | Existe: paquetes $1,350 / $2,800 → posible ad group "Veteran Cremation" |

No hace falta crear páginas nuevas: hay que ajustar las existentes.

## Qué ya rankea orgánico (Semrush)
El sitio es nuevo (uploads de 2026-05) y casi no tiene visibilidad. Lo mejor es "sunflower cremation" en posición 24 (260/mes) y "colton funeral home" en 43 (390/mes). También rankea por "colton cemetery" y "hermosa gardens cemetery colton" (posiciones 50–90). Tráfico orgánico ≈ 0, así que **Ads es prácticamente el único canal**. La marca "Colton Sunflower" no tiene búsquedas medibles; "sunflower cremation" lo comparte con Sunflower Riverside.

## Hallazgo de negocio
El dominio de contacto (`murrietavalleyfh.com`) y la dirección (2050 Key St, la misma que Sunflower Crematory) indican que Colton Sunflower forma parte del grupo **Murrieta Valley Funeral Home** (cliente PMM 769-956-1619), y probablemente también de Inland Memorial / Sunflower Crematory. Hay que confirmarlo y coordinar geos y negativas de marca entre esas cuentas.
