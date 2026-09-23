---
cliente: Pro Phase Electric
slug: pro-phase-electric
url: https://prophaseelectricar.com/
actualizado: 2026-09-22
veredicto: REQUIERE AJUSTES ANTES DE ESCALAR (la cuenta ya está activa)
score: 5/12 en ítems verificables · 5 ítems (10 pts) SIN VERIFICAR
---

# Auditoría de landing — Pro Phase Electric

> **Auditoría parcial.** No pude cargar el sitio. La política de red de la organización bloquea `prophaseelectricar.com`, archive.org y los lectores externos (403 en el proxy). PageSpeed sin API key devuelve 429 por cuota agotada. No hay proyecto de Semrush para el dominio, y el MCP no deja crearlo. **No vi el HTML, el formulario, el botón de llamada ni la velocidad.**
> Fuentes usadas: datos de Google Ads de la cuenta 758-301-1023 vía Windsor (URL final, Quality Score, experiencia de landing, conversiones), Semrush orgánico (páginas indexadas y keywords) y búsqueda web (títulos y snippets).
> Para cerrar los ítems pendientes, cualquiera de estas opciones:
> 1. Agregar `prophaseelectricar.com` a los dominios permitidos del entorno.
> 2. Agregar `PAGESPEED_API_KEY` al entorno.
> 3. Enviar el HTML (Ctrl+U → `data/site-home.html`) y capturas del móvil (arriba del pliegue, formulario, footer).
> 4. Enviar una captura de Google Ads → Objetivos → Conversiones y una de Tag Assistant en la home.

## Veredicto
Search está enviando todo el tráfico, incluido el de paneles y EV, a una **home genérica**, y **solo se mide "Calls from Ads"**. No hay conversión de llamada desde el sitio ni de formulario, y Google califica la experiencia de la página de destino como *below average* en 2 de las 5 keywords con QS. No se debe escalar presupuesto ni abrir ad groups de paneles y EV hasta resolver los 3 bloqueantes.

## Bloqueantes (resolver en Fase 0)
- [ ] **Medir conversiones del sitio**: llamadas desde la web (número de reenvío de Google o evento `tel:` click) y envío de formulario con página de gracias propia o evento. Probar con Tag Assistant. Hoy la cuenta tiene **una sola acción de conversión** ("Calls from Ads", la extensión de llamada). Las cuentas del MCC que funcionan agregan 15–20% más de conversiones con "Website Calls" (ver `benchmark.md`). — PMM (con acceso al Tag y al CMS) — 2–3 h
- [ ] **Landings de paneles y de EV**: no existen (ni en el índice de Semrush ni en la búsqueda). Sin ellas, los ad groups de mayor ticket caen en la home. Cada una necesita un H1 con el servicio y NWA, el formulario de ≤4 campos, clic para llamar, reseñas, licencia y oferta. — PMM o cliente (según quién edite; PENDIENTE en el brief) — 4–6 h cada una
- [ ] **Verificar móvil (formulario visible arriba y clic para llamar), velocidad y tag.** Son 5 ítems sin verificar que pueden ser bloqueantes. Hay que revisarlos antes de /strategy. — PMM — 0.5 h cuando haya acceso

## Mejoras (Fase 2–3)
- [ ] **Oferta visible**, por ejemplo "Free estimate on panel upgrades & EV chargers" o "Open 7 days", sujeta a lo que el cliente pueda sostener (PENDIENTE en el brief). La competencia de EV ancla precio ("desde $395") y estimado gratis (`competitors.md`).
- [ ] **Horario 5:00–16:00, los 7 días**, visible en el sitio y en el GBP. Es un diferenciador (`competitors.md`, oportunidad 1).
- [ ] **Número de licencia de Arkansas** y "licensed & insured" en el header o arriba del pliegue.
- [ ] **Página de reparación** (breakers, outlets, cableado, troubleshooting) para los ad groups de reparación.
- [ ] **Landings por ciudad** (Fayetteville, Rogers, Bentonville, Springdale) solo si los ad groups de ciudad justifican volumen. Epic y Emperial las tienen. Mientras tanto, headline dinámico o H1 "Electrician in Northwest Arkansas".
- [ ] **Sitelinks**: hoy uno lleva a /portfolio/ ($14.35 por 1 clic). Cambiarlo por páginas de servicio cuando existan.

## Rúbrica
| Ítem | Puntaje | Evidencia |
|---|---|---|
| Headline refleja el servicio buscado | **1** | Todo va a la home. Título "Electrician in Northwest Arkansas", que sirve para búsquedas genéricas y no para paneles ni EV (no hay página). Landing exp. *below average* en "electrician" |
| Formulario corto visible arriba (móvil) | SIN VERIFICAR | Existe /contact-us/; en la home no se sabe |
| Clic para llamar en móvil | SIN VERIFICAR | El teléfono (479) 287-3650 aparece en los snippets; no se sabe si es `tel:` ni si es sticky |
| Oferta clara | SIN VERIFICAR (probable 0) | El brief no registra ofertas |
| Prueba social | **1** | Existe /reviews/; ~33 reseñas con 4.9–5.0 en directorios. No se sabe si hay estrellas y número arriba del pliegue |
| Confianza | **1** | "Licensed" en los perfiles; falta el número de licencia; años y garantía PENDIENTE |
| Velocidad móvil | SIN DATO | PageSpeed 429; `speed_score` vacío en Google Ads |
| Google Tag presente | **1** | El cliente dice que sí. Google Ads no tiene ninguna conversión del sitio, así que el tag no aporta a Ads hoy |
| Página de gracias medible | **0** | No hay acción de conversión de formulario en la cuenta. No se sabe si existe `/thank-you/` |
| Páginas por servicio | **1** | Existen residential, commercial, new build y safety inspections. Faltan panel, EV y reparación |
| Sin fugas | SIN VERIFICAR | — |

**Total verificable: 5 de 12.** Los 5 ítems sin verificar suman 10 puntos. Aun con todos en 2 no llegaría a 22, porque Página de gracias está en 0 y es bloqueante.

## Detalle por página
Páginas indexadas (Semrush + búsqueda). No pude leer H1, CTA ni formulario.

| URL | Rol | Nota |
|---|---|---|
| `/` | URL final del único RSA; 35 de 35 clics | Título "Pro Phase Electric - Electrician in Northwest Arkansas". Es la única página con tráfico orgánico (3 visitas/mes) |
| `/services/` | Listado de 12 servicios | Resúmenes de una línea por servicio (texto que envió Jhombis) |
| `/residential-electrical-service/` | Servicio | Genérica residencial |
| `/commercial-electrical-service/` | Servicio | Rankea en posición 35–56 para "commercial electrician nwa" |
| `/new-build-electrical-installation/` | Servicio | Construcción nueva |
| `/electrical-safety-inspections/` | Servicio | Inspección de paneles, cableado, breakers |
| `/reviews/` | Prueba social | Candidata a sitelink |
| `/about-us/` | Confianza | — |
| `/portfolio/` | Fotos de trabajos | Hoy es sitelink; recibió 1 clic ($14.35) |
| `/contact-us/` | Formulario | 3 clics desde anuncios ($29.57) |
| *(no existe)* panel / EV / reparación | — | **Hay que crearlas** |

## Tracking encontrado
- **Google Ads (758-301-1023)**: 1 acción de conversión con datos en 90 días, "Calls from Ads" (1 conversión). No hay "Website Calls", "Form Fill" ni "Clicks to call".
- **Google Tag / GA4**: el cliente dice que está instalado; no pude verificar el ID (`G-`/`AW-`/GTM). Windsor no tiene una propiedad GA4 de este dominio conectada.
- **Quality Score** (keywords con datos): 3–5/10. Experiencia de landing: *below average* en "electrician" y "electrician companies near me", *average* en "licensed electrician", "electrician near me" y "ev charger installation near me". CTR esperado: *below average* en las 5.

## Velocidad
Sin datos. Hay que correr `python scripts/pagespeed.py https://prophaseelectricar.com/ --strategy mobile` con `PAGESPEED_API_KEY`, o pedir el score de pagespeed.web.dev. Si el score móvil es menor a 40, es bloqueante.

## Landings que la estrategia va a necesitar
Por orden de prioridad para /strategy:
1. **Electrical Panel Upgrade & Replacement — Northwest Arkansas** (panel, 200 amp, breaker box). Es el servicio de mayor ticket y el primero de la lista del cliente.
2. **EV Charger Installation — Northwest Arkansas** (Level 2, Tesla, NEMA 14-50 install, residencial y comercial).
3. **Electrical Repair** (breakers, outlets, cableado, troubleshooting, lighting repair). Puede ser la home si se ajusta el H1 y hay una sección de reparación arriba del pliegue.
4. *(Fase 3, según volumen)* Ciudad: Fayetteville, Rogers, Bentonville, Springdale.

**Faltan 3 landings de servicio** (más 4 de ciudad opcionales).

## Qué ya rankea orgánico (Semrush)
Visibilidad casi nula: 27 keywords en el top 100 y ~3 visitas al mes, todas a la home.
- Marca: "prophase electric" (posición 3), "prophase electrical" (posición 6). Volumen de 40/mes cada una; hay búsqueda de marca y la cubre el orgánico. Una campaña de marca con este presupuesto no es prioridad (lo decide /strategy).
- Genéricas locales, sin relevancia real: "electrician northwest arkansas" (posición 44), "electricians in bentonville" (51), "commercial electrician nwa" (56).
- Ruido de nombre: "new phase electric", "final phase electric", "speakes electric", "mister sparky lowell ar".
- Conclusión: el orgánico no cubre ningún término de servicio. **Search pagado es el canal** para paneles y EV, y las landings nuevas también ayudarían al SEO.
