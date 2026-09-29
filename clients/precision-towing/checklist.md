---
cliente: Precision Towing
slug: precision-towing
fase_actual: 0
actualizado: 2026-09-29
D0: 2026-09-29
---

# Checklist — Precision Towing

Generado por /roadmap desde `knowledge/checklists/setup-cuenta.md`, adaptado a este cliente. Responsable entre paréntesis. /weekly-review lo actualiza. ⚠ = bloqueante de la fase.

## Fase 0 — Fundación (2026-09-29 → 2026-10-13)
Ya cumplido:
- [x] (PMM) Cuenta 753-255-2245 vinculada al MCC de PMM, acceso admin
- [x] (PMM) Facturación configurada y verificada (la cuenta gasta desde el 2026-08-14)
- [x] (PMM) Google Tag instalado en las 9 páginas (GTM-NWQH4MVX + gtag AW-18347302928)
- [x] (PMM) Conversión "Calls from Ads" y "Website Calls" creadas y funcionando
- [x] (Cliente) Número de call tracking aprobado: (760) 606-4160 → (760) 379-6222

Esta semana, sin depender del cliente:
- [ ] ⚠ (PMM) Lista de negativas universal PMM aplicada a nivel de cuenta (con excepciones: no "cheap/cheapest", no "trailer")
- [ ] ⚠ (PMM) Lista `data/negatives-nicho.txt` (269 términos) aplicada a nivel de cuenta con `/negatives`
- [ ] (PMM) 22 keywords amplias de "ENHPRM Radius" pasadas a frase (puente hasta la estructura nueva)
- [ ] (PMM) "Calls from Ads" con duración mínima 30 s; "Clicks to call" y acciones locales marcadas como secundarias
- [ ] ⚠ (PMM) Aplicación automática de recomendaciones DESACTIVADA
- [ ] (PMM) Verificar en la UI: ubicación "Presencia", radios 21 mi + 8 mi + 8 mi, países excluidos; socios de búsqueda y Display apagados en la campaña actual
- [ ] (PMM) GA4 vinculado (confirmar si existe dentro de GT-NCTDVBBQ) y audiencia "Todos los visitantes" creada para acumular desde ya
- [ ] (PMM) Hoja compartida de calidad de leads entregada al cliente (fecha, hora, canal, ¿calificado?, ¿cerrado?)
- [ ] (PMM) Pedir PageSpeed móvil de home y landing estrella a Jhombis, o `PAGESPEED_API_KEY`

Dependen del cliente (pedir vía Jhombis esta semana):
- [ ] ⚠ (Cliente) Acceso de edición a precisiontowingca.com (WordPress/Elementor) y a GTM-NWQH4MVX, o contacto de quien publica
- [ ] ⚠ (Cliente) Proceso de respuesta a leads definido: quién contesta el teléfono 7–22, quién fuera de horario, tiempo de respuesta a formularios
- [ ] ⚠ (Cliente) `/thank-you/` creada (noindex) y Redirect configurado en los 7 formularios Elementor
- [ ] ⚠ (PMM) Conversión "Form - Thank You" creada en AW-18347302928 (URL de destino; respaldo: trigger `submit_success` en GTM) y probada con Tag Assistant
- [ ] ⚠ (PMM) Conversión "Website Calls" re-verificada con Tag Assistant en móvil
- [ ] ⚠ (Cliente) Footer de las 9 páginas y /schedule-a-tow/ con horario real "Monday – Sunday 7 AM – 10 PM"
- [ ] (Cliente) Bug de IDs del formulario /schedule-a-tow/ corregido (campo fecha con name=email; email sin validación)
- [ ] (PMM) Campos ocultos UTM + GCLID en los formularios
- [ ] (Cliente) GBP "Precision Automotive, Paint & Collision & Towing" verificado, categoría principal "Towing service", horario 7–22 unificado; acceso de administrador para PMM
- [ ] (PMM) GBP vinculado a Google Ads (activo de ubicación)
- [ ] (Cliente) Confirmar 5 claims antes de publicar anuncios: after-hours (quién contesta), flatbed en flota, camión medium duty para 5th wheel, equipo de winch/4x4, nombre histórico "Miller's Kern Valley Towing"
- [ ] (Cliente) Ticket promedio y margen por servicio → (PMM) recalcular CPL máximo (margen × cierre × 0,3)
- [ ] (Cliente) Confirmar que $825 es pauta neta y si hay margen para escalar
- [ ] (Cliente) Licencia CHP / motor carrier, seguro y disposición al background check → decide pista LSA (respuesta antes del 2026-10-06)
- [ ] (Cliente) 5+ fotos propias de camiones y taller + logo (para activos de imagen y futuro remarketing)
- [ ] ⚠ (PMM) `/build-campaign`: "Search - Towing KRV" y "Search - Marca" creadas en pausa según strategy.md y data/ads-search.md
- [ ] (PMM) Landing aprobada por /audit-landing o bloqueantes resueltos (hoy 12/22, REQUIERE AJUSTES)

## Fase 1 — Lanzamiento Search (2026-10-14 → 2026-10-21)
- [ ] (PMM) Campaña "Search - Towing KRV" con 4 ad groups y "Search - Marca" con 1, según strategy.md
- [ ] (PMM) Red: solo Búsqueda, socios y Display apagados
- [ ] (PMM) Ubicación: Presencia solamente; radio 21 mi + 2 × 8 mi; resto de países excluidos
- [ ] (PMM) Programación Lun–Dom 6:30–22:30
- [ ] (PMM) Puja: Maximizar conversiones sin tCPA en ambas
- [ ] (PMM) 87 keywords en frase; 8 exactas (towing near me, tow truck near me, towing company near me, tow truck company near me, kernville towing, towing lake isabella, lake isabella towing, travel trailer towing service, precision towing, precision automotive lake isabella)
- [ ] (PMM) Negativas a nivel de ad group aplicadas (cruces AG1/AG3/AG4 y genéricos en Marca) según strategy.md
- [ ] (PMM) 3 RSA por ad group, H1 pinneada, 15H/4D, fuerza "Buena" o superior; claims condicionados sustituidos si el cliente no confirmó
- [ ] (PMM) Extensiones: 5 sitelinks, 9 callouts, snippet Services, llamada (760) 606-4160 con reporte, ubicación (si GBP vinculado)
- [ ] (PMM) URLs finales verificadas (200, https, sin redirect): /light-medium-duty-towing/, /roadside-assistance/, /5th-wheel-towing/, /travel-trailer-towing/, /
- [ ] (PMM) Presupuesto diario: $24 + $3
- [ ] (PMM) Activar estructura nueva y pausar "ENHPRM Radius" el mismo día; PMax sigue pausada
- [ ] (PMM) Anuncios aprobados por políticas (revisar 24 h después)
- [ ] (PMM) Primera conversión registrada de cada tipo (llamada anuncio, llamada web, formulario)
- [ ] (PMM) Auction Insights D7: ¿aparece Golden Empire, B&D o redes lead-gen?

## Fase 2 — Limpieza (2026-10-21 · 2026-10-28 · 2026-11-13)
- [ ] D7 (2026-10-21): search terms revisados, negativas agregadas
- [ ] D7: keywords sin impresiones identificadas (no pausar aún); gasto diario ≥ $18 (si no, ampliar frase)
- [ ] D14 (2026-10-28): search terms revisados, negativas agregadas
- [ ] D14: keywords con > $47 de gasto y 0 conversiones marcadas ("tow truck", "roadside assistance" primero)
- [ ] D30 (2026-11-13): search terms revisados, negativas agregadas
- [ ] D30: keywords con 0 impresiones en 30 días pausadas
- [ ] D30: RSA con peor rendimiento por grupo reemplazado
- [ ] D30: reporte de calidad de leads del cliente recibido (hoja compartida)
- [ ] D30: decisión AG4 (pausar hasta 2027-04-15 si 0 conv) y "24 hour" (activar solo si hay cobertura nocturna confirmada)
- [ ] (PMM/Cliente) Landing estrella reescrita y publicada antes del D30
- [ ] (Cliente) Botón de llamada sticky en móvil; sellos AAA/NAPA/Gold Seal; agregado 4,8★ en páginas de servicio
- [ ] (Cliente) /roadside-assistance/ con H2 por subservicio; /5th-wheel-towing/ y /travel-trailer-towing/ con frase de intención; home con H1

## Fase 3 — Optimización de puja (estimada 2026-11-26; rango 2026-11-13 → 2026-12-09)
- [ ] ≥30 conversiones en 30 días confirmadas con tracking verificado (sin contar la campaña vieja)
- [ ] tCPA en "Search - Towing KRV" = CPA real observado (esperado $30–35); Marca sigue en Max. conversiones
- [ ] Bajar tCPA 10% cada 2 semanas si se sostiene, hasta $26
- [ ] Presupuesto reajustado por ad group según CPA y capacidad del cliente (camiones/conductores: PENDIENTE)
- [ ] Ajustes de puja por horario/dispositivo evaluados con 60 días de datos
- [ ] Si Roadside ≥ 8 conv/mes con CPL ≤ $31: separar en campaña propia ($8/día)
- [ ] (Cliente) Velocidad: hero WebP, fuentes, caché/CDN; fugas de menú en landings pagadas

## Fase 4 — Remarketing (revisión 2027-01-15) ⛔ probable bloqueo por audiencia
- [ ] Audiencia de visitantes ≥1.000 usuarios en 30 días (hoy proyección 100–200: no alcanza para RLSA)
- [ ] RLSA en observación en ambas campañas (cuando la lista lo permita)
- [ ] Display remarketing opcional con exclusión de apps si lista ≥100 y hay fotos propias

## Fase 5 — Performance Max (2027-03-30 como muy pronto) ⛔ no califica con $825/mes
- [ ] Condiciones de `pmax-cuando-y-como.md` verificadas (hoy falla presupuesto: $5–8/día vs ≥$78 necesarios)
- [ ] Cliente confirma margen para escalar a ≥ $2.000/mes (única vía para que califique)
- [ ] Exclusión de marca, asset groups por servicio con assets propios, tCPA +10–20%, evaluación a 4 semanas

## Fase 6 — Conversiones offline (futuro, requiere CRM)
- [ ] Cliente registra leads cerrados con GCLID (hoy: hoja compartida sin GCLID)
- [ ] Importación de conversiones offline configurada
- [ ] Optimización cambiada a valor de conversión

## Pista paralela — LSA (solo si el cliente confirma licencia, seguro y background check)
- [ ] (Cliente) Respuesta sobre licencia CHP / motor carrier y seguro antes del 2026-10-06
- [ ] (PMM) Solicitud LSA iniciada (2026-10-06 si aplica)
- [ ] (PMM) Verificación completada (2026-10-20 → 2026-11-03)
- [ ] (PMM) Presupuesto semanal LSA ($50–75) aparte de los $825; gestión de reseñas y tasa de respuesta

## Recurrente (semanal, /weekly-review)
- [ ] Search terms → negativas (marcas de competidores nuevas, compra de trailers, aseguradoras)
- [ ] Gasto vs $825 mensual
- [ ] CPL vs objetivo $21–31 (alarma $47); tendencia 7d vs 28d
- [ ] Anuncios rechazados / limitados
- [ ] Impression share perdido por presupuesto y por ranking (meta 70–80% en AG1/AG2)
- [ ] Auction Insights: Golden Empire, B&D, redes lead-gen
- [ ] Calidad de leads reportada por el cliente (hoja compartida)
- [ ] Log escrito en `log/YYYY-MM-DD.md`
