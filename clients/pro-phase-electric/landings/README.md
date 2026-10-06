---
cliente: Pro Phase Electric
slug: pro-phase-electric
pais: US
actualizado: 2026-10-01
---

# Landings GoHighLevel — Pro Phase Electric

Fuente: `make_specs.py` (genera cada `spec.json`) → `python scripts/landing_build.py clients/pro-phase-electric/landings`. **Se edita el spec o `make_specs.py`, nunca el HTML.** Montaje: `docs/setup-gohighlevel.md`.

| Página | Ad group | URL final (propuesta) | Keyword principal | Indexar | QA bloqueantes | Estado |
|---|---|---|---|---|---|---|
| electrician-northwest-arkansas | Electrician - NWA | https://go.prophaseelectricar.com/electrician-northwest-arkansas | electrician northwest arkansas | No (solo Ads) | 3 | borrador |
| electrical-repair-nwa | Electrical Repair | https://go.prophaseelectricar.com/electrical-repair-nwa | electrical repair | No (solo Ads) | 3 | borrador |
| electrical-panel-upgrade-nwa | Electrical Panel Upgrade | https://go.prophaseelectricar.com/electrical-panel-upgrade-nwa | electrical panel upgrade | No (solo Ads) | 3 | borrador |
| ev-charger-installation-nwa | EV Charger Installation | https://go.prophaseelectricar.com/ev-charger-installation-nwa | ev charger installation | No (solo Ads) | 3 | borrador |

**Por qué no se indexan:** van en un subdominio de GHL, como Funnel solo para Ads. El SEO es del sitio principal del cliente; indexar copias por servicio en otro dominio compite con él. Se puede cambiar a `indexar: true` (535+ palabras únicas por página) si el cliente quiere posicionar Paneles y EV, que su sitio no tiene.

## Bloqueantes (los mismos 3 en las 4 páginas)
| Bloqueante | Quién | Cómo |
|---|---|---|
| `ghl.form_id` | PMM | Crear en GHL un formulario de 4 campos con ocultos `gclid`, `utm_source`, `utm_campaign`, `utm_term` (+ `service`) y pegar el ID |
| `legal.privacidad_url` | Cliente/PMM | URL de la política de privacidad (en el sitio o en GHL) |
| Etiqueta de conversión del formulario | PMM | Nueva acción "GHL Form" (Website, Submit lead form) en 758-301-1023 → `tracking.conversion_label_form`. El AW-ID ya está (AW-18410300787) |

## Avisos (no bloquean)
- **Conversión por clic en `tel:`**: crear una acción secundaria → `conversion_label_call`.
- **Prueba social**: se ve "4.9★ on Google", pero sin número de reseñas ni reseñas citadas (no se inventan). Pegar 2–3 reseñas reales con autor y fuente cuando haya acceso al GBP, más el total.
- **Licencia de Arkansas, años, garantía, tiempo de respuesta**: no están confirmados, por eso no aparecen. Agregarlos al spec cuando el cliente los dé.
- **Colores provisionales** (carbón + el amarillo del botón del sitio), sin logo. Confirmar con el logo del cliente.
- **Dominio** `go.prophaseelectricar.com`: es la propuesta; necesita el CNAME en el DNS del cliente.
- **Teléfono**: hoy es el fijo (479) 287-3650. Si se usa un número de seguimiento de GHL, cambiar `negocio.telefono` y regenerar.

## Después de montarlas
1. Prueba con `?gclid=TEST123`, Tag Assistant (la conversión dispara una sola vez en la página de gracias) y PageSpeed móvil ≥70.
2. Cambiar las URLs finales de los 4 RSA y de las keywords en Search NWA (requiere OK, con la lista de cambios a la vista).
3. Actualizar `strategy.md` (columna Landing) y el checklist.
