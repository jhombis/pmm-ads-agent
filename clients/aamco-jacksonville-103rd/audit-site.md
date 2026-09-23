---
cliente: AAMCO Transmissions & Total Car Care — 103rd St (Jacksonville)
slug: aamco-jacksonville-103rd
url: https://aamco-jacksonvillefl.com/ · https://103rd.aamco-jacksonvillefl.com/
actualizado: 2026-09-23
veredicto: REQUIERE AJUSTES (auditoría parcial, página no inspeccionada visualmente)
score: 11/22 provisional (5 ítems sin verificar, puntuados 1 por defecto)
---

# Auditoría de landing — AAMCO 103rd St

> **Limitación**: el entorno cloud bloquea `aamco-jacksonvillefl.com` (red restringida). PageSpeed API también sin cuota (no hay `PAGESPEED_API_KEY`). La auditoría se armó con **GA4 (propiedad 465445685), el informe de landing pages de Google Ads y Semrush**. Lo que requiere ver la página (H1, campos del form, botón de llamada, velocidad) queda **N/V (no verificado)** con tareas para cerrarlo.

## Veredicto
La cuenta ya está activa, así que esto no bloquea un lanzamiento. Pero hay 3 problemas que afectan la medición y la conversión:
1. No hay página de gracias.
2. El formulario convierte muy poco y en el subdominio 103rd no registra envíos.
3. Todo el tráfico pagado cae en la home genérica, aunque el sitio ya tiene páginas por servicio.

## Bloqueantes (resolver antes de reestructurar la campaña)
- [ ] **Página de gracias con URL propia**. En GA4 no hay ninguna vista de `/thank-you` ni similar en 90 días; la confirmación es inline. La conversión de Ads "Form Fill" no se puede verificar con Tag Assistant de forma limpia. — Crear `/thank-you/` y redirigir el form ahí; conversión por URL. — PMM + quien edita el sitio — 2 h
- [ ] **Formulario del subdominio 103rd: 8 form_start, 0 form_submit en 90 días**. En el dominio raíz: 27 starts → 6 submits (22%). Posible form roto o sin evento en el subdominio. — Enviar un lead de prueba desde `103rd.aamco-jacksonvillefl.com` en móvil y confirmar que llega y que registra. — PMM — 1 h
- [ ] **GA4 sin eventos clave**: 0 key events en 90 días. Ni form_submit ni clic a teléfono están marcados. — Marcar `form_submit` (o la página de gracias) y crear un evento `click_tel` (clic en enlaces `tel:`) como eventos clave. — PMM — 1 h
- [ ] **Clic para llamar no medido en la web** (N/V si existe el botón). La conversión "Website Calls [Jacksonville 103 Rd]" dejó de registrar en may-2026, cuando entró CallRail. — Confirmar que el número dinámico de CallRail aparece en el header móvil como `tel:` y medir el clic. — PMM — 1 h

## Mejoras
- [ ] **Usar las páginas de servicio que ya existen** como URL final por ad group (ver tabla abajo). Hoy el 100% del tráfico pagado va a `/`. — PMM — 1 h
- [ ] **Unificar dominio**. Hay 3 dominios para la misma sede: anuncio → `aamco-jacksonvillefl.com` y `103rd.aamco-jacksonvillefl.com`; GBP → `aamcojacksonville.com/Home` (dominio viejo, sin ranking útil en Semrush). Hay que decidir la URL canónica de la sede 103rd y apuntar GBP y anuncios a ella. — Cliente/franquicia — 2 h
- [ ] **Quitar o bloquear páginas de prueba públicas**: `/test/` y `/test-2/` (47 vistas en 90 días). También redirigir las URL legacy `/Sites/US/FL/Jacksonville/...` (recibe tráfico con 0% de interacción). — Quien edita el sitio — 1 h
- [ ] **Home multi-sede** (existe `/locations/`). Si la landing lista varias sedes, el usuario del Westside puede llamar a otra sede. Para Ads: página o subdominio solo 103rd, con dirección, mapa y un solo número. — N/V
- [ ] **Prueba social arriba**: "507 Google reviews · 4.4★". Hoy los testimonios están en `/testimonials/` (14 vistas), no en la landing. — N/V
- [ ] **Oferta visible arriba**: "Free Transmission Check" / cupones de `/special-offers/` (18 vistas). El anuncio promete inspección gratis; la landing debe repetirla en el H1 o el subtítulo. — N/V
- [ ] **Tráfico basura en GA4**: 913 sesiones "direct" a `/` con 10% de interacción y 24 s, más hits a URLs legacy. Parece bot. Filtrarlo para que no ensucie la lectura.

## Rúbrica
| Ítem | Puntaje | Evidencia |
|---|---|---|
| Headline refleja el servicio buscado | 1 | Todo el tráfico va a `/` (home general). Existen páginas por servicio, pero no se usan. H1 N/V |
| Formulario corto visible arriba (móvil) | 1 | Hay form en `/` y `/contact/`. Tasa start→submit 22% (baja). Campos y posición N/V |
| Clic para llamar en móvil | 1 (N/V) | No hay evento de clic a teléfono en GA4. CallRail activo |
| Oferta clara | 1 | `/special-offers/` existe; anuncio: "Free Transmission Inspection". Visibilidad en la landing N/V |
| Prueba social | 1 (N/V) | `/testimonials/` existe; GBP 507 reseñas 4.4★ |
| Confianza | 1 (N/V) | Marca AAMCO, BBB A+ (según anuncio). Garantía nacional N/V |
| Velocidad móvil | 1 (N/V) | PageSpeed sin cuota; el informe de Google Ads no devolvió speed score |
| Google Tag presente | 2 | GA4 recibe hits en ambos hosts; la conversión de Ads "Form Fill [Jacksonville 103 Rd]" registra (4 en 90 días) |
| Página de gracias medible | 0 | Sin URL de gracias en GA4 |
| Páginas por servicio | 1 | Existen: transmisión automática/manual, A/C, check engine, frenos, diagnóstico, etc. No enlazadas desde Ads |
| Sin fugas | 1 | Sitio multi-sede, páginas `/test`, URLs legacy, 3 dominios |
| **Total** | **11/22** | provisional |

## Detalle por página (datos GA4 y Ads, 90 días)
| URL | Tráfico | Interacción | Form | Nota |
|---|---|---|---|---|
| `aamco-jacksonvillefl.com/` | Ads: 60 clics / $250 (Search) | cpc: 285 sesiones, 40% engaged, 116 s | 16 starts / 6 submits | Home genérica; destino de casi todo |
| `103rd.aamco-jacksonvillefl.com/` | Ads: 219 clics / $913 (Search + PMax) | — | 8 starts / **0 submits** | Subdominio de la sede; revisar form |
| `/contact/` | 37 vistas | — | 11 starts | |
| `/service/automatic-transmissions/` | 41 vistas | orgánico bajo | — | Candidata para ad group Transmisión |
| `/service/manual-transmissions/` | 49 vistas | rankea "clutch repair jacksonville" #5 | — | |
| `/service/check-engine-light-service/` | 24 vistas | rankea "check engine light jacksonville" #5 | — | Candidata para Motor / check engine |
| `/service/air-conditioning/` | 39 vistas | orgánico 75% engaged | — | Candidata para A/C |
| `/special-offers/` | 18 vistas | — | — | Oferta escondida |
| `/test-2/`, `/test/` | 47 vistas | — | — | **Páginas de prueba públicas** |

## Tracking encontrado
- **GA4**: propiedad 465445685 recibe `aamco-jacksonvillefl.com` y `103rd.aamco-jacksonvillefl.com`. Eventos: page_view, scroll, form_start (35), form_submit (6), click saliente (20). **0 eventos clave.**
- **Google Ads**: auto-tagging activo; "Form Fill [Jacksonville 103 Rd]" registra (tag de Ads presente). "Website Calls [Jacksonville 103 Rd]" sin datos desde may-2026.
- **CallRail**: activo (importa a Ads desde abr-2026). DNI en el sitio: N/V.
- Meta Pixel: hay tráfico `fb / paid`, así que alguien corre Meta. N/V.

## Velocidad
N/V. PageSpeed API devolvió 429 (cuota diaria agotada sin clave). Pendiente: correr `python scripts/pagespeed.py https://103rd.aamco-jacksonvillefl.com/ --strategy mobile` con `PAGESPEED_API_KEY`, o pegar el score desde pagespeed.web.dev.

## Landings que la estrategia va a necesitar
Casi todas ya existen; hay que adaptarlas para la sede 103rd: headline con el servicio + "103rd St / Westside", número CallRail de la sede, form corto arriba y gracias con URL propia.
| Ad group propuesto | Página existente | Acción |
|---|---|---|
| Marca 103rd | `103rd.aamco-jacksonvillefl.com/` | Arreglar form; dirección y mapa arriba |
| Transmisión – reparación / síntomas / rebuild | `/service/automatic-transmissions/` | Versión sede 103rd; H1 "Transmission Repair on 103rd St" |
| Mecánico general | `/auto-service/` | Versión sede 103rd |
| Motor / check engine | `/service/check-engine-light-service/` | Versión sede 103rd |
| A/C (opcional) | `/service/air-conditioning/` | Versión sede 103rd |
| Página de gracias | **no existe** | Crear `/thank-you/` |

**Faltan 1 página nueva (gracias) y 4–5 adaptaciones por sede.**

## Qué ya rankea orgánico (Semrush, US)
El orgánico es débil (casi 0 tráfico estimado). Lo más relevante:
| Keyword | Pos. | Vol. | URL |
|---|---|---|---|
| aamco 103rd | 4 | 110 | `/` |
| clutch repair jacksonville | 5 | 70 | `/service/manual-transmissions/` |
| check engine light jacksonville | 5 | 90 | `/service/check-engine-light-service/` |
| muffler shop jacksonville fl | 9 | 110 | `/service/exhaust/` |
| ac blowing hot jacksonville | 12 | 70 | `/service/air-conditioning/` |
| transmission repair jacksonville fl | 27 | 210 | `/` |
| transmission shops in jacksonville | 36 | 140 | `/` |

Lectura: para transmisión no-marca no hay presencia orgánica (pos. 26–55). Search pagado es el único canal para ese término, lo que refuerza darle prioridad en la reestructura. `aamcojacksonville.com` (el dominio del GBP) no rankea nada útil.

## Para cerrar los N/V
1. Habilitar `aamco-jacksonvillefl.com` en la red del entorno (o correr esto localmente) y volver a correr `/audit-landing`.
2. `PAGESPEED_API_KEY` en el entorno.
3. Captura móvil de `103rd.aamco-jacksonvillefl.com` (sin scroll) si no se habilita la red.
