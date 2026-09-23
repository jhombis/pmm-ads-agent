---
cliente: 290 Tow and Recovery
slug: 290-tow-recovery
url: https://290towrecovery.com/
actualizado: 2026-09-23
veredicto: REQUIERE AJUSTES ANTES DE LANZAR
score: 12/22
---

# Auditoría de landing — 290 Tow and Recovery

> **Método (2026-09-23, segunda pasada):** el proxy de la sesión sigue bloqueando `290towrecovery.com`, así que no se leyó el HTML directo. Todo sale de la **API de PageSpeed/Lighthouse** con key: métricas, requests de red, links y capturas móviles de página completa de `/`, `/light-medium-duty-towing/`, `/exotic-vehicle-towing/`, `/local-long-distance-towing/` y `/roadside-assistance/`.
>
> **Sin verificar**: la acción real del botón "Get a Free Quote", el destino del formulario, si el header es sticky al hacer scroll y los eventos de conversión que dispara el tag. Esas cuatro cosas se validan con Tag Assistant.
>
> **Otra cosa**: la cuenta **ya está activa desde el 17/09** (ver `benchmark.md`). Por eso los bloqueantes de tracking son urgentes, no de Fase 0 teórica.

## Veredicto
**Requiere ajustes antes de lanzar (o de seguir gastando).** El sitio es decente para llamadas: el teléfono aparece en el header y hay un CTA "Click here to call" above the fold, más una página por servicio.

Lo que falla es la medición y la confianza:
- no está confirmado que las conversiones disparen;
- el formulario no tiene página de gracias;
- no hay reseñas;
- la licencia TDLR no está visible;
- el móvil es lento, con LCP de 5.7–6.9 s en las páginas de servicio.

## Bloqueantes (resolver en Fase 0)
- [ ] **Verificar las conversiones con Tag Assistant.** El sitio carga GTM-WBX4RZ9K, GA4 G-KH9SFWZK66 y el tag de Google Ads AW-18397446767 (hoy solo se ve remarketing/1p-user-list disparando). Hay que probar tres cosas:
  1. clic en `tel:(830)4638318` → "Website Calls";
  2. llamada desde el anuncio → "Calls from Ads", con umbral de 60–90 s;
  3. envío del formulario → "Form Fill".

  Además, confirmar que AW-18397446767 pertenece a la cuenta 213-019-5545. Responsable: PMM. Esfuerzo: 1.5 h.
- [ ] **Página de gracias medible.** El formulario es Elementor Pro, que por defecto muestra un mensaje inline. Configurar el redirect a `/thank-you/` o un disparador GTM por el evento `submit_success` de Elementor. Responsable: PMM. Esfuerzo: 0.5 h.
- [ ] **Página de exotic: faltan los CTA.** La captura móvil muestra un bloque vacío donde las otras páginas tienen "Get a Free Quote" y "Call Now". Puede ser un widget roto o un lazy-load que no renderizó; confirmarlo en un móvil real. Hasta que se arregle no se usa como landing. Responsable: PMM. Esfuerzo: 0.25 h.

## Mejoras (Fase 2–3)
- [ ] **H1 con intención + ciudad.** El home dice "Serving Texas with Honor & Integrity": no refleja ninguna búsqueda. Usar algo como "24/7 Towing in Fredericksburg, TX – Fast Response, Upfront Pricing". En las páginas de servicio el H1 es el nombre del servicio sin ciudad. (PMM, 1 h)
- [ ] **Confianza.** Mostrar la licencia TDLR #, "Licensed & Insured" y los años de operación junto al CTA. "Navy Veteran Owned" ya está y es un buen diferenciador: subirlo a las páginas de servicio. (PMM + dato del cliente, 0.5 h)
- [ ] **Prueba social.** Hoy no hay ni una reseña. Depende de crear el GBP (bloqueante del brief). Mientras tanto, 3 testimonios reales con nombre y fotos reales de las grúas del cliente en lugar de stock. (Cliente, variable)
- [ ] **Oferta.** El sitio tiene "10% Senior Discount" y "Get a Free Quote". Falta el ángulo de precio claro que salió en /competitors, tipo "Upfront price on the phone — no hidden fees". Agregarlo al hero y a los callouts. (PMM, 0.5 h)
- [ ] **Velocidad móvil.** Ver la sección de velocidad. Comprimir y convertir a WebP las imágenes hero, quitar CSS/JS de Elementor que no se usa y activar un plugin de caché. Objetivo: LCP < 3 s. (PMM, 2 h)
- [ ] **Formulario más corto y arriba.** Tiene 4 campos (Name, Phone, Email, Message) y está al final de las páginas de servicio. Para towing basta con Name, Phone y Ubicación. Es secundario frente a la llamada. (PMM, 0.5 h)
- [ ] **Radio.** El hero dice "within a 45-minute radius" y el brief dice 40 mi. Alinear el texto con la segmentación real.
- [ ] **Páginas por ciudad**: solo si /strategy las justifica con volumen (Kerrville, Boerne, Johnson City).

## Rúbrica
| Ítem | Puntaje | Evidencia |
|---|---|---|
| Headline refleja el servicio buscado | 1 | Las páginas de servicio tienen H1 = servicio, sin ciudad. El H1 del home es genérico |
| Formulario corto visible arriba (móvil) | 1 | 4 campos, al fondo de las páginas de servicio. El home no tiene formulario visible, solo el botón "Get a Free Quote" (acción sin verificar; se carga popup.js de Elementor) |
| Clic para llamar en móvil | 2 | Ícono `tel:` en el header y botón "Click here to call" above the fold. Se carga `sticky.min.js`: probable header sticky, sin confirmar |
| Oferta clara | 1 | 10% Senior Discount y Free Quote. Sin oferta fuerte de precio o ETA |
| Prueba social | 0 | No hay reseñas, estrellas ni testimonios. Las fotos parecen de stock |
| Confianza | 1 | "Navy Veteran Owned & Operated", "Available 24/7". Sin TDLR, seguro ni años |
| Velocidad móvil | 1 | Score de 45–79 según página y corrida. LCP de 3.0–6.9 s |
| Google Tag presente | 2 | GTM, GA4 y AW presentes y disparando. Los eventos de conversión no están verificados (ver bloqueantes) |
| Página de gracias medible | 0 | Formulario Elementor sin redirect detectado |
| Páginas por servicio | 2 | 4 páginas, una por servicio, exotic incluida (Semrush no la tenía indexada) |
| Sin fugas | 1 | Hamburger menu. Las páginas de servicio tienen un bloque de navegación interna antes del formulario. No hay links externos visibles |
| **Total** | **12/22** | |

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| `/` | "Serving Texas with Honor & Integrity" (H2 "Trustworthy Towing in Fredericksburg & Beyond") | Click here to call · Get a Free Quote · Call Now | No visible | Header + 3 botones + footer | No | Chips: Navy Veteran, Fast & Efficient, 10% Senior Discount. "Available 24/7" |
| `/light-medium-duty-towing/` | Light & Medium-Duty Towing | Get a Free Quote · Call Now | 4 campos, al fondo | Header + botón | No | La mejor candidata a landing del grupo general |
| `/exotic-vehicle-towing/` | Exotic Vehicle Towing | **Ninguno visible** (bloque vacío) | Al fondo (sin verificar) | Solo header | No | CLS de 0.198, el peor. Arreglar antes de usarla |
| `/local-long-distance-towing/` | Local & Long-Distance Towing | Get a Free Quote · Call Now | 4 campos + reCAPTCHA | Header + botón | No | Habla de "transportation to another city in Texas" |
| `/roadside-assistance/` | (sin captura revisada en detalle) | — | — | Header | No | Ticket bajo |

Plataforma: **WordPress + Elementor Pro**, tema Hello Elementor, plugin Google Site Kit. PMM la edita.

## Tracking encontrado
- `GTM-WBX4RZ9K` (Tag Manager)
- `G-KH9SFWZK66` (GA4): dispara `g/collect`
- `AW-18397446767` (Google Ads): disparan `viewthroughconversion` y `1p-user-list`, es decir, remarketing/page view. **No se observó ningún evento de conversión** en la carga, lo cual es esperable porque la conversión dispara al hacer clic o enviar.
- `ccm/collect`: Consent Mode / Google Tag gateway activo.
- Enlaces `tel:(830)4638318` en todas las páginas. No hay número de reenvío dinámico en el sitio (Website Call Conversion), así que "Website Calls" probablemente se mide por clic en `tel:`. Verificar.
- Sin Meta Pixel.
- En la cuenta de Ads (Windsor): 3 conversiones primarias (Calls from Ads, Website Calls, Form Fill), cada una con conteo "una por clic". Llevan **0 conversiones con 14 clics**: todavía no sirve como prueba de que el tracking funcione ni de que falle.

## Velocidad
| Página | Móvil score | LCP | CLS | TBT | Peso | Desktop score |
|---|---|---|---|---|---|---|
| `/` | 55–79 (2 corridas) | 3.6–6.9 s | 0–0.099 | 110–500 ms | ~2.1–2.6 MB | 83 |
| `/light-medium-duty-towing/` | 60–69 | 3.0–5.9 s | 0.098–0.1 | 350–550 ms | 2.5–2.7 MB | 92 |
| `/exotic-vehicle-towing/` | 45 | 5.7 s | **0.198** | 670 ms | 2.7 MB | — |
| `/local-long-distance-towing/` | 59 | 5.9 s | 0.098 | 340 ms | ~2.7 MB | 78 |
| `/roadside-assistance/` | 56–60 | 5.7–6.0 s | 0–0.098 | 310–570 ms | 2.7 MB | 77 |

Causas: JS y CSS de Elementor sin usar, imágenes hero pesadas (páginas de ~2.7 MB) y sin caché ni optimización de imágenes aparente. Ninguna página baja de 40, así que no bloquea, pero con LCP de 6 s se pierden llamadas de gente varada con 4G débil en el Hill Country.

## Landings que la estrategia va a necesitar
1. **Light & Medium-Duty Towing** (`/light-medium-duty-towing/`): landing del grupo principal, "towing / tow truck near me". Ajustar el H1 con ciudad y 24/7.
2. **Local & Long-Distance Towing**: sirve para long-distance anclado a ciudad. Separarla solo si /strategy confirma volumen.
3. **Exotic Vehicle Towing**: existe, pero **hay que arreglar los CTA**.
4. **Roadside Assistance**: existe. Baja prioridad por ticket (y la cuenta ya pagó "car jumper").
5. **Por ciudad**: no crear aún. Decide /strategy con Keyword Planner.

**Faltan 0 páginas nuevas.** Hay 1 para reparar (exotic) y 4 con ajustes de H1, confianza y oferta.

## Qué ya rankea orgánico (Semrush)
- 5 keywords orgánicas y tráfico estimado de **0**. La única keyword es "highway 290 wrecker service" (vol. 50), con la mejor posición en la 44 (`/light-medium-duty-towing/`).
- La relevancia orgánica es casi nula: toda la demanda inicial viene de Ads.
