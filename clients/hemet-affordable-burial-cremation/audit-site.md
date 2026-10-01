---
cliente: Hemet Affordable Burial and Cremation
slug: hemet-affordable-burial-cremation
url: https://hemetaffordablecremation.com/
actualizado: 2026-10-01
veredicto: REQUIERE AJUSTES ANTES DE LANZAR
score: 11/22
---

# Auditoría de landing — Hemet Affordable Burial and Cremation

## Veredicto
**Requiere ajustes urgentes, y la cuenta ya está gastando.** El sitio **no tiene Google Tag** en ninguna página, así que hoy no se mide ni el formulario ni las llamadas desde el sitio. La campaña puja con Maximizar conversiones viendo solo "Calls from Ads". Además, el formulario solo muestra un mensaje en la misma página, sin página de gracias. El contenido (precios, licencia, 24/7, paquetes) es bueno; lo que falla es la medición y la estructura de conversión.

## Bloqueantes (resolver en Fase 0)
- [ ] **Google Tag ausente**: instalar el Google Tag (AW-) en todo el sitio, vía plugin de header de WordPress o GTM. No apareció `gtag`, `googletagmanager`, `AW-`, `G-` ni `GTM-` en el HTML de 9 páginas, ni peticiones de red al renderizar con Chromium (móvil, con `?gclid=`). Las conversiones "Form Fill" (última 2026-09-01) y "Website Calls" (última 2026-09-13) dejaron de registrar, lo que sugiere que el tag **se perdió en un rediseño reciente** (los assets son de abr–jul 2026). — PMM (con acceso a WordPress) — 1 h
- [ ] **Número de reenvío de Google (Website Calls) no funciona**: con `gclid` el teléfono sigue en (951) 658-3288; sin tag no hay reemplazo. Configurar el snippet de llamadas en el sitio y reactivar la conversión. — PMM — 0.5 h
- [ ] **Sin página de gracias**: el formulario de Elementor muestra un mensaje en la misma página. Agregar la acción "Redirect" a `/thank-you/` (página nueva, con la conversión Form Fill) o medir el evento de envío con GTM. — PMM/Cliente (WordPress) — 1 h
- [ ] **Probar todo con Tag Assistant**: envío de formulario de prueba, clic en el teléfono en móvil y llamada al número de reenvío. — PMM — 0.5 h
- [ ] **Dejar de mandar tráfico a la home** (39 clics y $442 en 90 días, 0 conversiones): no tiene H1 ni formulario. Los grupos deben apuntar a /cremation, /burial o /pricing (ver mapeo abajo). — PMM (en la reestructura) — 0 h

## Mejoras (Fase 2–3)
- [ ] **Precio arriba en /cremation y /burial**: hoy esas páginas no muestran ningún precio. Agregar debajo del H1 "Simple Cremation $1,095 · With Viewing $1,495" y "Direct Burial $1,995 · Graveside $2,495". Son las páginas de servicio que reciben tráfico pagado. — Cliente/PMM — 1 h
- [ ] **H1 con intención y ciudad**: "Cremation" → "Cremation Services in Hemet, CA"; "Burial" → "Burial Services in Hemet, CA"; en la home falta el H1 (hoy es un H2). — Cliente/PMM — 0.5 h
- [ ] **Formulario arriba en móvil**: en /cremation aparece a ~1,600 px (unas 2 pantallas de scroll). Subirlo o poner un botón "Arrange Online" que salte al formulario. Hacer el **email opcional** (hoy los 3 primeros campos son obligatorios); en este nicho el teléfono es lo que importa. — Cliente/PMM — 1 h
- [ ] **Landing de servicios completos** (servicio estrella): no existe. Los paquetes sí existen en /pricing (Memorial $2,600 · Traditional + Cremation $2,795 · Traditional with Burial $2,995 · Graveside $2,495). Crear `/funeral-services/` con fotos **reales** de la capilla, la sala de velación y el salón de recepción, y estos paquetes. — Cliente/PMM — 3–4 h
- [ ] **Prueba social en páginas de servicio**: la home tiene testimonios (texto, 5★) e imagen "Review us on Google", pero no muestra calificación ni cantidad de reseñas, y /cremation, /burial y /pricing no tienen ninguna. Un testimonio dice "Don't let the old reviews fool you!", que confirma el problema de reputación heredado. Agregar 2–3 testimonios a cada página de servicio y un widget del GBP nuevo cuando tenga reseñas. — Cliente — 1 h
- [ ] **Página de veteranos**: hay paquetes de veteranos ($1,250 / $2,500 / $4,000) sin landing propia. Sirve para un ad group futuro (`veteran cremation`, `veteran funeral`). — Cliente/PMM — 2 h
- [ ] **Fugas**: menú de 42–54 enlaces, obituarios y enlace externo a Google. Para las landings pagadas, valorar una plantilla sin menú (o con menú reducido). — PMM — 2 h
- [ ] **Velocidad**: medir en PageSpeed real (ver sección Velocidad). — PMM — 0.25 h

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| / (home) | **ninguno** (H2: "A Local Funeral Home Families Can Rely On") | View Pricing · Arrange Online → /contact-us · Call Now | **No** | Sí, header sticky | Testimonios de texto (5★), "Review us on Google" | Precios $1,095 / $1,995 visibles. 39 clics pagados, 0 conv |
| /cremation/ | "Cremation" | View Pricing · Arrange Online · Call Now | Sí: Name*, Phone*, Email*, Message, a ~1,600 px | Sí, sticky | **Ninguna** | **Sin precio.** Landing con más tráfico pagado (89 clics, $958, 6 conv) |
| /burial/ | "Burial" | Igual | Sí, igual | Sí | Ninguna | Sin precio. 17 clics, 1 conv |
| /pricing/ | **ninguno** | View GPL · Arrange Online · Call Now ×N | **No** | Sí | Ninguna | 11 paquetes con precio (ver abajo). 26 clics, 1 conv |
| /contact-us/ | "Contact Us" | — | Sí: Name*, Phone*, Email*, Comments, arriba (344 px) | Sí | — | "Arrange Online" de todo el sitio apunta aquí |
| /about-us/ | "About Us" | Arrange Online · Call Now | Sí (pie) | Sí | — | Confirma FD2486, "originally known as Hartford Chapel", "current ownership began more recently" |
| /why-choose-us/ | "Why Families in Hemet Choose Us" | Igual | Sí (pie) | Sí | — | Buenos argumentos: licencia, capilla histórica, 24/7, coordinación con hospitales y el condado |
| /faqs/, /obituaries/ | — | — | — | — | — | Fuera del embudo pagado |
| GPL (PDF, 2026-03-25) | — | — | — | — | — | ✅ Publicado (cumple CA B&P §7685). Direct cremation $1,095 y Direct burial $1,995 **coinciden** con los anuncios |

**Paquetes publicados en /pricing** (resuelven el pendiente del brief sobre servicios completos):
| Paquete | Precio |
|---|---|
| Simple Cremation | $1,095 |
| Simple Cremation with Private Viewing | $1,495 |
| Simple Viewing with Witness | $1,895 |
| Graveside Service (burial) | $2,495 |
| Cremation with Memorial Service | $2,600 |
| Traditional Service followed by Cremation | $2,795 |
| Traditional Service with Burial | $2,995 |
| Direct Burial | $1,995 |
| Veteran Simple Cremation | $1,250 |
| Veteran Cremation with Graveside | $2,500 |
| Veteran Traditional Service with Burial | $4,000 |

**Dato operativo importante**: la cremación se hace en **Sunflower Crematory** (tercero), no en un crematorio propio. En el MCC hay cuentas de "Sunflower Cremation Services" (672-338-0346) y "Colton Sunflower Burial and Cremation" (151-776-2744): posible relación comercial o de dueños. **Confirmar**, porque podrían competir en las mismas subastas.

## Tracking encontrado
| Elemento | Estado |
|---|---|
| Google Tag / gtag.js (AW-, G-) | ❌ No encontrado (HTML de 9 páginas + render con Chromium) |
| GTM | ❌ |
| GA4 | ❌ |
| Meta Pixel | ❌ |
| Número de reenvío de Google (Website Calls) | ❌ Sin reemplazo con gclid |
| reCAPTCHA (antispam del formulario) | ✅ en las páginas con formulario |
| Plataforma | WordPress + Elementor + LiteSpeed Cache (JS diferido) |
| Conversiones en la cuenta | "Calls from Ads" (sí funciona, no depende del sitio) · "Form Fill" y "Website Calls" **sin registros desde mediados de septiembre** |

## Velocidad
- **Score PageSpeed: PENDIENTE.** La API devolvió 429 (cuota diaria agotada) y no hay `PAGESPEED_API_KEY`. Pedir a Jhombis el score de pagespeed.web.dev o configurar la clave.
- Medición indicativa con Chromium headless (iPhone 13, a través del proxy del entorno, **no comparable con PageSpeed**): página liviana (128–182 KB transferidos), imágenes WebP, CLS 0.02–0.05 (bien). El LCP medido (22–29 s) está inflado por el proxy y el JS diferido de LiteSpeed; no se usa para puntuar.
- HTML servido en ~1.6–2.2 s por curl (también a través del proxy).
- Puntuación provisional: 1/2 hasta tener el score real.

## Rúbrica
| Ítem | Puntos | Nota |
|---|---|---|
| Headline refleja el servicio buscado | 1 | Hay páginas por servicio, pero el H1 es genérico ("Cremation") y la home no tiene H1 |
| Formulario corto visible arriba (móvil) | 1 | 4 campos, pero a ~2 pantallas en /cremation; no hay formulario en la home ni en /pricing |
| Clic para llamar en móvil | 2 | Header sticky con "Call Now (951) 658-3288" |
| Oferta clara | 1 | Precios claros en la home y /pricing; ausentes en /cremation y /burial |
| Prueba social | 1 | Testimonios solo en la home, sin calificación ni conteo |
| Confianza | 2 | FD2486, familiar, capilla histórica de más de 100 años, 24/7, GPL |
| Velocidad móvil | 1 | Provisional (sin score real) |
| Google Tag presente | **0** | **Bloqueante** |
| Página de gracias medible | **0** | **Bloqueante** |
| Páginas por servicio | 1 | Cremation / Burial / Pricing sí; servicios completos y veteranos no |
| Sin fugas | 1 | Menú grande y obituarios; sin pop-ups |
| **Total** | **11/22** | |

## Landings que la estrategia va a necesitar
Mapeo para la reestructura (reemplaza las URLs "PENDIENTE" de `strategy.md`):
| Ad group | Landing ahora | Landing ideal (crear o ajustar) |
|---|---|---|
| Funeral Home | /pricing/ (tiene los paquetes completos) | **/funeral-services/** (crear) |
| Cremation | /cremation/ | /cremation/ con precios y formulario arriba |
| Affordable | /pricing/ | /pricing/ con H1 y formulario |
| Burial | /burial/ | /burial/ con precios y formulario arriba |
| Brand | / | / (con H1) |
| Futuro: Veteranos | /pricing/ | /veterans/ (crear) |
| Futuro: Español | — | /es/ o landing en español (si hay personal) |

## Qué ya rankea orgánico (Semrush, us)
Dominio con poco tráfico orgánico (~8 visitas/mes, 104 keywords). Relevancia local útil:
| Keyword | Pos. | Vol. | URL |
|---|---|---|---|
| morturary's in hemet | 6 | 110 | / |
| hemet mortuary | 9 | 210 | / |
| funeral homes in hemet ca | 10 | 210 | / |
| mortuary in hemet | 10 | 110 | / |
| mortuary hemet ca | 11 | 40 | / |
| hemet ca obits | 19 | 140 | /obituaries/ |
| hemet obituaries | 27 | 260 | /obituaries/ |

Lectura: la marca nueva ya aparece en el top 10 de los términos locales "mortuary/funeral home Hemet". Eso refuerza mantener esos términos (exacta) en Search, donde orgánico y pagado se suman en la página de resultados.
