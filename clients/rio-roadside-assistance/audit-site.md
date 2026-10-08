---
cliente: Rio Roadside Assistance
slug: rio-roadside-assistance
url: PENDIENTE (final URL de los anuncios no obtenida; rioroadsideassistance.com no se pudo abrir)
actualizado: 2026-10-07
veredicto: REQUIERE AJUSTES ANTES DE LANZAR
score: SIN DATO/22 (la página no se pudo leer; el veredicto sale de la medición y del tracking, no de la rúbrica)
---

# Auditoría de landing — Rio Roadside Assistance

## Veredicto
**No se pudo auditar la página**: la cuenta no entregó su URL final (Windsor falló en esa consulta y luego pidió volver a autorizar) y el dominio probable `rioroadsideassistance.com`, igual que cualquier web externa, está bloqueado por la política de red de este entorno (DNS y proxy devuelven 403/ENOTFOUND; también Yelp y los competidores). Aun así el veredicto es **REQUIERE AJUSTES ANTES DE LANZAR**, por dos bloqueantes que no dependen de leer la página: la cuenta lleva 24 clics y 0 conversiones de cualquier tipo (ni llamadas desde el anuncio), y no hay ninguna acción de conversión verificada. Mientras eso siga así, la campaña está pagando tráfico que no se puede evaluar (estándar PMM #7: sin tracking no se lanza).

## Bloqueantes (resolver en Fase 0)
- [ ] **Confirmar la URL final de los anuncios y quién edita la web** (o si no hay web y los anuncios van a una ficha o a una landing de PMM) — Cliente/Jhombis — 0.5 h
- [ ] **Verificar con Tag Assistant las acciones de conversión**: llamadas desde anuncio (call asset), llamadas desde la web (número de reenvío), formulario con página de gracias. 0 de 24 clics convirtió; en la cohorte nueva del MCC lo normal eran 3–4 — PMM — 1 h
- [ ] **Un solo teléfono en todo el sitio y que sea el de reenvío**; el número de Yelp (550) 782-9250 tiene un código de área que no es de Massachusetts: confirmar cuál es el número real y cuál el de tracking — PMM/Cliente — 0.5 h
- [ ] **Habilitar el dominio en la red del entorno** (Allowed domains) o pasar el HTML exportado a `data/` para poder correr `site_scan.py` y PageSpeed — Jhombis — 0.2 h
- [ ] **Horario de atención contra programación**: el 4-oct (domingo) no tiene datos en la cuenta y Yelp dice 7:00–23:00; alinear programación de anuncios con el horario real — PMM — 0.3 h

## Mejoras (Fase 2–3)
- [ ] Una página por servicio (flat tire · jump start · lockout · fuel delivery · towing si aplica) con el término de búsqueda en el H1, formulario ≤4 campos arriba y botón de llamada sticky; hoy la campaña envía todo a una sola URL (PENDIENTE confirmar)
- [ ] Precio cerrado visible si el cliente lo sostiene (las redes nacionales anuncian $49 plano y rangos $89–199): es la oferta que el usuario espera en este nicho
- [ ] Prueba social: número de reseñas y estrellas de GBP en la landing (PENDIENTE: ficha de Google no encontrada)
- [ ] Versión en portugués/español de la landing si el cliente atiende en ese idioma (demanda detectada en search terms)
- [ ] Licencia y seguro visibles (requisito de confianza y de LSA)

## Rúbrica
| Ítem | Puntos | Nota |
|---|---|---|
| Headline refleja el servicio buscado | SIN DATO | página no leída |
| Formulario corto visible arriba (móvil) | SIN DATO | — |
| Clic para llamar en móvil | SIN DATO | — |
| Oferta clara | SIN DATO | — |
| Prueba social | SIN DATO | GBP no encontrada en búsqueda web |
| Confianza (licencia, seguro, años) | SIN DATO | Yelp sin confirmar: "10+ años" |
| Velocidad móvil | SIN DATO | sin `PAGESPEED_API_KEY` y sin acceso al dominio |
| Google Tag presente | SIN DATO (0 conversiones de todo tipo en 24 clics: sospecha de tag ausente o acción de llamada sin crear) | bloqueante hasta verificar |
| Página de gracias medible | SIN DATO | — |
| Páginas por servicio | SIN DATO (la campaña usa una sola URL final, por confirmar) | — |
| Sin fugas | SIN DATO | — |

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| PENDIENTE | — | — | — | — | — | no se pudo abrir ninguna página |

## Tracking encontrado
Nada verificable en el HTML (no leído). Desde la cuenta (Windsor, 25-sep → 7-oct): `conversions` 0, `all_conversions` 0, `phone_calls` 0 en 24 clics; la consulta de `conversion_action_name` falló (502) antes de que Windsor se desconectara, así que ni siquiera se sabe qué acciones existen. Verificar en Google Ads: acciones de conversión, cuáles son primarias, estado del recurso de llamada y umbral de duración (60–90 s).

## Velocidad
Sin dato: `PAGESPEED_API_KEY` no está definida y el dominio no es accesible desde el entorno. Pedir a Jhombis el score móvil de PageSpeed Insights o habilitar el dominio y correr `python scripts/pagespeed.py <url> --strategy mobile`.

## Landings que la estrategia va a necesitar
Según el brief (servicios inferidos de las keywords y de la ficha de Yelp sin confirmar) y el límite de fragmentación ($608/mes → 1 campaña, 3–5 ad groups):
1. `/roadside-assistance-boston/` — genérico de roadside con ciudades del radio (H1 con inserción de ciudad)
2. `/flat-tire-change/` — flat tire service, mobile tire change, spare tire
3. `/jump-start/` — car jump start, dead battery, (mobile battery replacement si lo ofrecen)
4. `/lockout-fuel-delivery/` — car lockout, ran out of gas (puede ir junto al principio por volumen)
5. `/towing/` — solo si Rio tiene grúa (PENDIENTE)
6. Versión PT/ES de la 1 si atienden en ese idioma
Cada una: H1 = término del grupo, botón de llamada sticky, formulario de 3 campos (nombre, teléfono, ubicación), página de gracias propia, precio desde si existe, reseñas de GBP. Se pueden generar con `/landing-ghl` en cuanto haya URL y contenido confirmados.

## Qué ya rankea orgánico (Semrush)
`domain_rank` de rioroadsideassistance.com: NOTHING FOUND (sin keywords orgánicas ni pagadas registradas). O el dominio es otro, o el sitio es nuevo y sin autoridad: la campaña no puede apoyarse en relevancia orgánica previa y la keyword de marca no tiene volumen (0 en Semrush).
