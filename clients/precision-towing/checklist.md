---
cliente: Precision Towing
slug: precision-towing
fase_actual: 0
actualizado: 2026-10-06
D0: 2026-10-06
version: 2
---

# Checklist — Precision Towing (v2)

Generado por /roadmap desde `knowledge/checklists/setup-cuenta.md`, adaptado a este cliente y re-baseline el 2026-10-06. Responsable entre paréntesis. /weekly-review lo actualiza. ⚠ = bloqueante de la fase. Nada se escribe en Google Ads sin OK de Jhombis con la lista de cambios a la vista; cada cambio queda con fecha en `log/`.

## Fase 0 — Fundación (2026-10-06 → 2026-10-17)
Ya cumplido:
- [x] (PMM) Cuenta 753-255-2245 vinculada al MCC de PMM, acceso admin
- [x] (PMM) Facturación configurada y verificada (gasta desde el 2026-08-14)
- [x] (PMM) Google Tag instalado en las 9 páginas (GTM-NWQH4MVX + gtag AW-18347302928)
- [x] (PMM) Conversiones "Calls from Ads" y "Website Calls" creadas y registrando
- [x] (Cliente) Número de call tracking aprobado: (760) 606-4160 → (760) 379-6222
- [x] (PMM) Diagnóstico de la cuenta `log/2026-10-06-diagnose.md`

Acciones en la cuenta, 2026-10-07, con OK de Jhombis (Windsor):
- [ ] ⚠ (PMM) Presupuesto diario de ENHPRM Radius $32 → $27 ($825/30,4)
- [ ] ⚠ (PMM) Eliminar 14 keywords de `data/2026-10-06-keyword-removals.txt` (b&d towing, b&m towing, 2 de "24 hours", 7 de boat, motorhome, toy hauler, cargo trailer)
- [ ] ⚠ (PMM) Aplicar negativas de campaña de `data/2026-10-06-negatives.txt` (universal con 3 excepciones + nicho) y las de ad group (sección NIVEL AD GROUP) en los 2 grupos actuales
- [ ] ⚠ (PMM) Quitar las 4 negativas de marca propia de la campaña (`precision`, `precision automotive`, [precision towing], [precision automotive lake isabella]) — solo cuando el grupo AG4 Marca exista; mientras, dejarlas
- [ ] (PMM) Pasar las 93 keywords restantes de amplia a frase (puente hasta la estructura nueva)
- [ ] ⚠ (PMM) Leer `customer.time_zone` en la UI y fijar programación 6:30–22:30 en esa zona (hoy la campaña sirve 24/7)
- [ ] (PMM) "Calls from Ads" con duración mínima 30 s; "Clicks to call" y acciones locales como secundarias
- [ ] ⚠ (PMM) Verificar en la UI sobre qué evento dispara "Form Fill" (1 conv entre 09-29 y 10-05); si no es un envío real, pasarla a secundaria
- [ ] ⚠ (PMM) Aplicación automática de recomendaciones DESACTIVADA
- [ ] (PMM) Verificar en la UI: "Presencia", radios 21 mi + 8 mi + 8 mi, países excluidos; socios de búsqueda y Display apagados; estado del activo de llamada (no en revisión)
- [ ] (PMM) GA4 vinculado (¿está dentro de GT-NCTDVBBQ?) y audiencia "Todos los visitantes" creada
- [ ] (PMM) Hoja compartida de calidad de leads entregada al cliente (fecha, hora, canal, ¿calificado?, ¿cerrado?)
- [ ] (PMM) Pedir PageSpeed móvil de home y landing estrella, o `PAGESPEED_API_KEY`

Dependen del cliente (pedir vía Jhombis; respuesta antes del 2026-10-10):
- [ ] ⚠ (Cliente) Acceso de edición a precisiontowingca.com y a GTM-NWQH4MVX, o contacto de quien publica. Si no llega el 2026-10-10 → vía B
- [ ] ⚠ (Cliente) Proceso de respuesta a leads: quién contesta 7–22, quién fuera de horario, tiempo de respuesta a formularios
- [ ] (Cliente) Confirmar 5 claims antes de publicar anuncios: after-hours (quién contesta), flatbed, camión medium duty para 5th wheel, equipo de winch/4x4, nombre histórico "Miller's Kern Valley Towing"
- [ ] (Cliente) ¿Cambio de llanta en carretera? (hay negativas exactas de "flat tire service" en la cuenta; AG2 las necesita)
- [ ] (Cliente) Ticket promedio y margen por servicio → (PMM) recalcular CPL máximo (margen × cierre × 0,3)
- [ ] (Cliente) Confirmar $825 como pauta neta y si hay margen para escalar
- [ ] (Cliente) Licencia CHP / motor carrier, seguro y background check → pista LSA
- [ ] (Cliente) CNAME `go.precisiontowingca.com` si se monta la landing en GHL/Leadpages (vía B)
- [ ] (Cliente) GBP verificado, categoría "Towing service", horario 7–22 unificado, acceso de administrador para PMM
- [ ] (Cliente) 5+ fotos propias de camiones y taller + logo

Landing (vía A si hay acceso antes del 2026-10-10; si no, vía B):
- [ ] ⚠ (PMM) Decisión vía A / vía B el 2026-10-10
- [ ] ⚠ Vía A (Cliente): `/thank-you/` noindex + Redirect en los 7 formularios Elementor; footer de las 9 páginas con "Monday – Sunday 7 AM – 10 PM"; bug de IDs del formulario /schedule-a-tow/
- [ ] ⚠ Vía B (PMM): `/landing-ghl precision-towing todos` (o Leadpages): landings towing, roadside y trailer + página de gracias, formulario de 3 campos con gclid/UTM, conversión propia; montaje según `docs/setup-gohighlevel.md`
- [ ] ⚠ (PMM) Conversión de formulario real creada y probada con Tag Assistant en móvil; "Website Calls" re-verificada
- [ ] (PMM) GBP vinculado a Google Ads (activo de ubicación) cuando haya acceso
- [ ] ⚠ (PMM) `/build-campaign`: "Search - Precision Towing KRV" con 4 grupos creada en pausa según strategy.md v2 y data/ads-search.md; URLs finales actualizadas en data/keywords.csv

## Fase 1 — Lanzamiento Search (2026-10-20 → 2026-10-27)
- [ ] (PMM) Campaña "Search - Precision Towing KRV" con AG1 Tow Truck & Towing KRV, AG2 Roadside Assistance, AG3 RV & Trailer Towing, AG4 Marca
- [ ] (PMM) Red: solo Búsqueda, socios y Display apagados
- [ ] (PMM) Ubicación: Presencia; radio 21 mi + 2 × 8 mi; resto de países excluidos
- [ ] (PMM) Programación Lun–Dom 6:30–22:30 en la zona horaria de la cuenta
- [ ] (PMM) Puja: Maximizar clics con tope de CPC $9
- [ ] (PMM) 87 keywords (77 frase, 10 exacta) según data/keywords.csv; negativas de ad group por grupo según strategy.md (taller solo en AG1–AG3)
- [ ] (PMM) Negativas de marca propia retiradas de la campaña (AG4 debe imprimir)
- [ ] (PMM) 1 RSA por grupo, H1 pinneada, 15H/4D, fuerza ≥ "Buena"; claims condicionados sustituidos si el cliente no confirmó; sin horas ni teléfono en el texto
- [ ] (PMM) Extensiones: 5 sitelinks, 9 callouts, snippet Services, llamada (760) 606-4160 con reporte, ubicación (si GBP vinculado)
- [ ] (PMM) URLs finales verificadas (200, https, sin redirect)
- [ ] (PMM) Presupuesto diario $27
- [ ] (PMM) Activar la nueva y pausar ENHPRM Radius el mismo día; PMax sigue pausada
- [ ] (PMM) Anuncios aprobados (revisar 24 h después)
- [ ] (PMM) Primera conversión de cada tipo registrada (llamada anuncio, llamada web, formulario)
- [ ] (PMM) Gasto ≥ $18/día en D7; si no, tope de CPC a $11
- [ ] (PMM) Auction Insights D7: Golden Empire, B&D, redes lead-gen

## Fase 2 — Limpieza (2026-10-27 · 2026-11-03 · 2026-11-19) y paso a Max. conversiones
- [ ] D7 (2026-10-27): search terms revisados, negativas agregadas; keywords sin impresiones identificadas
- [ ] D14 (2026-11-03): search terms revisados; keywords con > $47 y 0 conv marcadas ("tow truck", "roadside assistance" primero); CPC medio contra el tope
- [ ] D30 (2026-11-19): search terms revisados; keywords con 0 impresiones en 30 días pausadas; hoja de calidad de leads recibida; desktop −50% si sigue en 0 conv
- [ ] D30: decisión AG3 trailers (pausar hasta 2027-04-15 si 0 conv) y "24 hour" (solo con cobertura nocturna confirmada)
- [ ] D30: ≥15 conv limpias en 30 días y CPL ≤ $47 → cambiar a Maximizar conversiones sin tCPA
- [ ] (PMM/Cliente) Landing estrella definitiva publicada antes del D30
- [ ] (Cliente, vía A) Sticky móvil; sellos; agregado 4,8★; ajustes en roadside, 5th wheel, travel trailer; home con H1

## Fase 3 — Optimización de puja (estimada 2026-12-03; rango 2026-11-19 → 2026-12-17)
- [ ] ≥30 conversiones en 30 días con tracking verificado, ya en Max. conversiones ≥2 semanas
- [ ] tCPA = CPA observado (no el deseado); −10% cada 2 semanas si se sostiene, hasta $26
- [ ] Reparto por grupo según CPA; capacidad del cliente (camiones/conductores: PENDIENTE)
- [ ] Ajustes por horario/dispositivo con 60 días de datos
- [ ] (Cliente) Velocidad y fugas de menú (vía A)

## Fase 4 — Remarketing (revisión 2027-01-20) ⛔ probable bloqueo por audiencia
- [ ] Audiencia ≥1.000 en 30 días (proyección 100–200: RLSA no alcanza)
- [ ] Display remarketing opcional con lista ≥100, exclusión de apps y fotos propias

## Fase 5 — Performance Max (2027-04-06 como muy pronto) ⛔ no califica con $825/mes
- [ ] Condiciones de `pmax-cuando-y-como.md` (falla presupuesto: $5–8/día vs ≥$78)
- [ ] Cliente confirma pauta ≥ $2.000/mes (única vía)
- [ ] Exclusión de marca, asset groups por servicio, tCPA +10–20%, evaluación a 4 semanas

## Fase 6 — Conversiones offline (futuro, requiere CRM)
- [ ] Cliente registra leads cerrados con GCLID (hoy: hoja compartida)
- [ ] Importación de conversiones offline; optimización a valor

## Pista paralela — LSA (solo si el cliente confirma licencia, seguro y background check)
- [ ] (Cliente) Respuesta antes del 2026-10-10
- [ ] (PMM) Solicitud LSA iniciada (2026-10-13 si aplica) · verificación 2026-10-27 → 2026-11-10
- [ ] (PMM) Presupuesto semanal LSA ($50–75) aparte; reseñas y tasa de respuesta

## Recurrente (semanal, /weekly-review)
- [ ] Search terms → negativas (competidores nuevos, taller, compra de trailers, aseguradoras)
- [ ] Gasto vs $825 mensual; CPC medio vs tope
- [ ] CPL vs objetivo $21–38 (alarma $47); tendencia 7d vs 28d
- [ ] Anuncios rechazados / limitados; activo de llamada
- [ ] IS perdido por presupuesto y por ranking (meta 70–80% en AG1)
- [ ] Auction Insights: Golden Empire, B&D, Gomez, redes lead-gen
- [ ] Calidad de leads reportada por el cliente
- [ ] Log en `log/YYYY-MM-DD.md`
