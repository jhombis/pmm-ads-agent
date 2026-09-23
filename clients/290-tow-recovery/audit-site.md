---
cliente: 290 Tow and Recovery
slug: 290-tow-recovery
url: https://290towrecovery.com/
actualizado: 2026-09-23
veredicto: NO EVALUABLE — bloqueado por red
score: N/E (0 de 11 ítems verificados)
---

# Auditoría de landing — 290 Tow and Recovery

## Veredicto
**No evaluable: bloqueado por red.** El proxy de salida de la sesión bloquea `290towrecovery.com` (`EGRESS_BLOCKED`, reintentado el 2026-09-23). No se pudo leer el HTML ni medir la velocidad. No hay hallazgos inventados: los ítems de la rúbrica quedan **PENDIENTE**. La auditoría se tiene que repetir antes de /strategy, porque 5 de los 11 ítems son bloqueantes potenciales: headline, clic para llamar, Google Tag, página de gracias y velocidad.

## Qué se intentó y resultado
| Fuente | Resultado |
|---|---|
| WebFetch `https://290towrecovery.com/` | ❌ `EGRESS_BLOCKED` (proxy de la sesión) |
| `scripts/pagespeed.py --strategy mobile` | ❌ Llega a googleapis.com, pero devuelve **HTTP 429 Too Many Requests** en 2 intentos. No hay `PAGESPEED_API_KEY` y la cuota anónima está agotada |
| WebFetch a Wayback Machine | ❌ El dominio no es accesible desde la herramienta |
| WebSearch (dominio, marca y teléfono (830) 463-8318) | ⚠️ Sin resultados del sitio ni del teléfono. El sitio no aparece en la búsqueda de marca. Salen competidores (ver abajo) |
| Semrush `domain_rank` + `resource_organic` (db us) | ✅ Datos obtenidos (ver secciones de páginas y orgánico) |

## Qué hace falta para completar la auditoría (elegir una opción)
1. **Allowlist del dominio** en la política de red del entorno (Claude Code on the web → configuración del entorno → Network access: agregar `290towrecovery.com` y `www.290towrecovery.com`). Luego se vuelve a correr `/audit-landing`.
2. **O que Jhombis pegue**:
   - el HTML de la home y de cada página de servicio (Ctrl+U → copiar), o capturas en **móvil** (above the fold + página completa) de: `/`, `/light-medium-duty-towing/`, `/local-long-distance-towing/`, `/roadside-assistance/` y la página de exotic si existe;
   - la URL a la que lleva el formulario al enviarse (¿página de gracias propia o mensaje inline?);
   - el score de PageSpeed móvil de la home y de una página de servicio (pagespeed.web.dev): score, LCP, CLS y peso.
3. **Velocidad por script**: definir `PAGESPEED_API_KEY` en los secretos del entorno. La API sí es alcanzable. Hoy solo falla por cuota.

## Bloqueantes (resolver en Fase 0)
- [ ] **Auditoría no ejecutada.** Desbloquear el acceso (opción 1, 2 o 3 de arriba) y repetir `/audit-landing`. Responsable: PMM (Jhombis). Esfuerzo: 0.5 h.
- [ ] **Tracking de llamadas** (ya estaba en el checklist desde /onboard): Google Tag, conversión de clic en `tel:` y llamadas desde anuncios con número de reenvío de Google, probados con Tag Assistant. Sin tracking no se lanza (estándar PMM #7). No se pudo verificar si hay algún tag instalado. Responsable: PMM. Esfuerzo: 2 h.
- [ ] Los ítems bloqueantes de la rúbrica siguen **PENDIENTE** hasta verificarlos: headline por servicio, clic para llamar sticky en móvil, formulario corto, página de gracias medible, velocidad (bloquea si el score < 40).

## Mejoras (Fase 2–3)
- PENDIENTE: dependen de la auditoría real.

## Rúbrica
| Ítem | Puntaje | Estado |
|---|---|---|
| Headline refleja el servicio buscado | — | PENDIENTE. Hay páginas por servicio indexadas, pero no se pudo ver el H1 |
| Formulario corto visible arriba (móvil) | — | PENDIENTE |
| Clic para llamar en móvil | — | PENDIENTE (crítico: el objetivo son llamadas 24/7) |
| Oferta clara | — | PENDIENTE (el brief no tiene ofertas definidas) |
| Prueba social | — | PENDIENTE (sin GBP no hay reseñas de Google que mostrar) |
| Confianza (licencia TDLR, seguro) | — | PENDIENTE (el brief pide el número TDLR visible) |
| Velocidad móvil | — | PENDIENTE (PageSpeed 429) |
| Google Tag presente | — | PENDIENTE |
| Página de gracias medible | — | PENDIENTE (secundario: el objetivo principal son llamadas) |
| Páginas por servicio | — | Parcialmente verificado vía Semrush: existen 3 páginas de servicio (ver abajo). No se puntúa sin ver el contenido |
| Sin fugas | — | PENDIENTE |

## Detalle por página
URLs confirmadas por el índice de Semrush (db us). Todo el contenido está sin verificar.

| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| https://290towrecovery.com/ | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | Home indexada |
| https://290towrecovery.com/light-medium-duty-towing/ | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | Servicio 1 del brief |
| https://290towrecovery.com/local-long-distance-towing/ | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | Servicio 2 del brief |
| https://290towrecovery.com/roadside-assistance/ | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | Servicio 4 del brief |
| Exotic Vehicle Towing | — | — | — | — | — | **No aparece en el índice de Semrush.** PENDIENTE confirmar si la página existe |
| https://290towrecovery.com/privacy-policy/ | — | — | — | — | — | Existe (útil para el cumplimiento de políticas de Ads) |

No se detectaron páginas por ciudad en el índice. Eso no prueba que no existan.

## Tracking encontrado
PENDIENTE: no se pudo leer el HTML. Al desbloquear, buscar `gtag`, `googletagmanager`, `GTM-`, `G-`, `AW-`, `fbq`, los enlaces `tel:` y el número de reenvío.

## Velocidad
PENDIENTE. `scripts/pagespeed.py` responde HTTP 429, porque sin `PAGESPEED_API_KEY` la cuota anónima está agotada. No hay score, LCP, CLS ni peso.

## Landings que la estrategia va a necesitar
Según el brief (4 servicios, radio de 40 mi desde Fredericksburg, objetivo = llamadas). El volumen por ciudad se valida en /strategy con Keyword Planner:
1. **Light & Medium-Duty Towing**: la página existe. Validar el H1, el tel sticky y la prueba social.
2. **Local & Long-Distance Towing**: la página existe. Conviene separar long-distance si /strategy confirma que es el servicio de mayor ticket.
3. **Exotic Vehicle Towing**: **posible faltante**. Crearla si no existe y si el ticket la justifica.
4. **Roadside Assistance**: la página existe. Ticket bajo según la hipótesis del brief, así que la prioridad depende de la economía.
5. **Por ciudad (hipótesis, no crear aún)**: Kerrville, Johnson City, Boerne y Stonewall/Hwy 290. Solo si Keyword Planner muestra volumen. Si no, se agrupa por tema (estándar PMM #3).

## Qué ya rankea orgánico (Semrush)
- Semrush Rank: 21,658,742. **5 keywords** orgánicas, tráfico estimado de **0**. No tiene keywords pagadas en Semrush.
- Única keyword: **"highway 290 wrecker service"** (vol. 50, CPC $2.66). Rankea en la posición 44 con `/light-medium-duty-towing/` y entre la 73 y la 82 con la home, long-distance, roadside y privacy-policy.
- Lectura: la relevancia orgánica es casi nula, así que toda la demanda inicial vendrá de Ads. El término "wrecker" aparece como variante para evaluar en /strategy.
- Competidores que aparecieron en la búsqueda (para /competitors, sin validar): West Central Towing & Recovery (Fredericksburg), Axpress Towing (Stonewall, US-290), Eckert Towing, Douglas Towing and Roadside Assistance, True Towing, Benchmark Towing (heavy duty), T & A Towing and Recovery, Midway Wrecker Service (Kerrville).
