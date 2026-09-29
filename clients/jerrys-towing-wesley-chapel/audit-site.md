---
cliente: Jerry's Auto Body Solutions & Towing Service
slug: jerrys-towing-wesley-chapel
url: https://jerrystowingservice.com/
actualizado: 2026-09-29
veredicto: REQUIERE AJUSTES ANTES DE LANZAR
score: 11/22
---

# Auditoría de landing — Jerry's Auto Body Solutions & Towing Service

## Veredicto
Sitio de una sola página, limpio, con llamada visible y los tags instalados. La cuenta registra Website Calls, Form Fill y Calls from Ads (vía GTM), pero **ninguna está verificada** y el formulario no tiene página de gracias. La cuenta gasta desde el 22/08 con Maximizar conversiones: si "Website Calls" es un clic en `tel:`, el algoritmo optimiza hacia clics, no hacia leads. **Prioridad 1.**

## Bloqueantes (resolver en Fase 0)
- [ ] Conversión de llamada: verificar en Google Ads la acción "Calls from ads" (≥60 s) y el clic en `tel:` del sitio (evento GTM → AW-18347420212). Probar con Tag Assistant. — PMM — 1 h
- [ ] Conversión de formulario: agregar redirección del formulario de Elementor a `/thank-you/` y disparar la conversión ahí, o usar el evento `submit_lead_form` vía GTM. Probar con un envío real. — PMM — 1 h
- [ ] Revisar que las conversiones primarias de la cuenta sean **solo** llamada ≥60 s + formulario. Si "clic en teléfono" cuenta como primaria, el CPL sale inflado (en el MCC hay tasas de conversión del 40–50%, que sugieren justo eso). — PMM — 0.5 h

## Mejoras (Fase 2–3)
- [ ] **H1**: la página no tiene `<h1>`. Poner "24/7 Towing in Wesley Chapel, FL" (o "Towing Near You — Wesley Chapel & Pasco County"). — PMM — 0.25 h
- [ ] Formulario: pasar de 6 campos a 3 (Nombre, Teléfono, Ubicación del vehículo). En towing la gente llama; el formulario es secundario. — PMM — 0.5 h
- [ ] Prueba social: no hay reseñas ni testimonios. Poner el widget de reseñas de GBP o 3 reseñas reales con estrellas en cuanto existan. — Cliente (conseguir reseñas) / PMM — 1 h
- [ ] Confianza: agregar "Licensed & Insured", años de experiencia, fotos reales de las grúas y el equipo. — Cliente (material) — 1 h
- [ ] Oferta concreta: "Free quote" es genérico. Proponer algo como "Upfront flat-rate local tows" o "ETA ~30 min en Wesley Chapel" si lo sostienen. — Cliente — decisión
- [ ] Botón de llamada fijo abajo en móvil (el header ya es sticky; confirmar que el teléfono se ve en móvil sin hacer scroll). Normalizar a `tel:+18133810435`. — PMM — 0.25 h
- [ ] Versión en español o bloque "Hablamos Español" si contestan en español. — Cliente/PMM
- [ ] Si hacen carrocería: sección o página de Collision Repair (accident tow → reparación). — PMM

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| / | **ninguno** (H2: "Towing Services", "Why Choose Jerry's?") | Free Quote, llamar | 6 campos, Elementor, mensaje inline | 16 enlaces `tel:`, header sticky | Ninguna | Una sola página con anclas. Solo hay además /privacy-policy/ |

## Tracking encontrado
- GTM: `GTM-5VX6B6KS`
- Google Ads: `AW-18347420212` (config vía gtag / Site Kit)
- Google tag / GA4: `GT-5DDGBBK6` (Site Kit, `event_source: site-kit`)
- No se ve `send_to` de conversión en el HTML: las conversiones están dentro de GTM. La cuenta registra (08-22→09-28) **Website Calls 9, Form Fill 6, Calls from Ads 6**. **Verificar en GTM + Tag Assistant** qué dispara Website Calls y Form Fill.
- Formulario sin página de gracias (no hay `redirect_to`).

## Velocidad
- PageSpeed API devolvió 429 (sin `PAGESPEED_API_KEY` en la sesión). PENDIENTE: correr el score móvil.
- HTML: 140 KB, TTFB + descarga 1.8 s desde el contenedor. Elementor Pro con CSS inline pesado (1,300+ referencias). Riesgo medio de LCP > 2.5 s en móvil. Revisar caché y optimización de imágenes.

## Rúbrica
| Ítem | Puntos |
|---|---|
| Headline refleja el servicio | 1 (hay H2 de servicios, sin H1) |
| Formulario corto visible | 1 (6 campos, al final) |
| Clic para llamar | 2 |
| Oferta clara | 1 |
| Prueba social | 0 |
| Confianza | 1 (family-owned; sin licensed/insured) |
| Velocidad móvil | 1 (sin medir) |
| Google Tag | 2 |
| Página de gracias medible | 0 → **bloqueante** |
| Páginas por servicio | 1 (en towing con near-me, una sola página es aceptable) |
| Sin fugas | 1 (pocas fugas; no se revisó en detalle) |
| **Total** | **11/22** |

## Landings que la estrategia va a necesitar
- Home actual (towing general / near me): sirve una vez que tenga H1 y prueba social.
- `/roadside-assistance/`: jump start, fuel delivery y cambio de llanta tienen intención distinta a "tow".
- `/medium-duty-towing/`: box trucks y flotas, ticket alto.
- `/es/` o una landing de "grúa": solo si contestan en español.
- `/collision-repair/`: solo si confirman que hacen carrocería.

## Qué ya rankea orgánico (Semrush)
No consultado: el dominio es de 08/2026 y no se espera tráfico orgánico todavía. Correr Semrush `domain_overview` en la revisión del día 30.
