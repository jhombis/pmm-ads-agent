---
cliente: Colton Sunflower Burial and Cremation
slug: colton-sunflower
fase_actual: 0
actualizado: 2026-10-01
---
# Checklist — Colton Sunflower

⚠️ = bloqueante para salir de la fase. Cuenta heredada activa: algunos ítems de "setup" ya existen y solo se verifican.
Eliminado de la base: solicitud LSA (la categoría no aplica) y la Fase 5 PMax (no califica con el presupuesto; ver roadmap).

## Fase 0 — Rescate / fundación
- [x] (PMM) Cuenta vinculada al MCC de PMM (151-776-2744)
- [ ] (PMM) Facturación verificada
- [ ] (Cliente) GBP verificado, con la categoría principal correcta ("Funeral home")
- [ ] (PMM) GBP vinculado a Google Ads (activo de ubicación)
- [ ] (PMM) Google Tag en todas las páginas de coltonfuneral.com — verificar
- [ ] ⚠️ (PMM) Conversión "Form Fill" creada y probada con Tag Assistant — hoy NO existe
- [ ] ⚠️ (PMM) "Calls from Ads" con duración mínima de 60s — verificar configuración
- [x] (PMM) "Website Calls" existe — verificar que sea clic en teléfono o desvío, como primaria
- [ ] (PMM) Conversiones secundarias marcadas como secundarias
- [ ] (PMM) GA4 vinculado y audiencia "Todos los visitantes" importada
- [ ] (PMM) Campos ocultos UTM + GCLID en el formulario
- [x] (PMM) Negativas universales/nicho: 466 previas + 76 nuevas (2026-10-01)
- [ ] ⚠️ (Claude, tras OK) Quitar las negativas amplias que bloquean demanda: how, Fontana, online
- [ ] (Claude, tras OK) 5 negativas de data/2026-10-01-negatives.txt
- [ ] ⚠️ (PMM) Autoaplicación de recomendaciones DESACTIVADA — verificar
- [ ] (PMM) /audit-landing (bloqueado por proxy; correr desde otro entorno)
- [ ] (Cliente) Proceso de respuesta a leads: quién contesta, en cuánto tiempo, horario; ¿24/7?
- [ ] (Cliente) Número de call tracking aprobado
- [ ] ⚠️ (Jhombis/Cliente) /onboard: ticket, margen, capacidad, idioma ES, mascotas, **radio real**
- [ ] ⚠️ (Jhombis) Relación con Inland Memorial / Sunflower Riverside → radios sin solape
- [ ] (Jhombis) ¿$2,500/mes netos o con fee? (diario actual $49)
- [ ] (Jhombis) Acordar quién más edita la cuenta (keywords removidas por terceros)
- [ ] (Cliente) Confirmar los claims [C] del copy: family-owned, 24/7, crematorio propio, licencias, precio desde $X

## Fase 1 — Relanzamiento
- [x] Campaña Search existente (se reestructura, no se crea de cero)
- [ ] ⚠️ Red: solo Búsqueda; socios y Display apagados — verificar
- [x] Ubicación: Presencia solamente
- [ ] Países restantes excluidos — verificar
- [ ] Programación según horario del cliente (24/7 solo si contestan)
- [ ] ⚠️ Puja: Max clics → Maximizar conversiones (sin tCPA), después de Form Fill
- [ ] ⚠️ 5 ad groups según strategy.md; keywords en frase + exacta en los términos principales
- [ ] Negativas entre ad groups (cremation/burial/cost)
- [ ] ⚠️ 3 RSA por grupo, H1 pinneado, 15H/4D, fuerza "Buena"+
- [ ] Extensiones: sitelinks 4+, callouts 6+, snippets, llamada, ubicación
- [ ] URLs finales verificadas (200, https, sin redirect)
- [ ] Presupuesto $49/día (+ marca $5/día si se confirma)
- [ ] Anuncios aprobados (revisar 24h después)
- [ ] ⚠️ Primera conversión registrada después del relanzamiento

## Fase 2 — Limpieza (2026-10-22 · 2026-10-29 · 2026-11-14)
- [ ] D7: search terms → negativas
- [ ] D7: keywords sin impresiones identificadas
- [ ] D14: search terms → negativas
- [ ] D14: keywords con >$200 de gasto y 0 conv marcadas
- [ ] D30: search terms → negativas
- [ ] D30: keywords con 0 impresiones en 30d pausadas
- [ ] D30: peor RSA por grupo reemplazado
- [ ] D30: reporte de calidad de leads del cliente
- [ ] D30: CPA 30d ≤ $150 con ≥10 conv

## Fase 3 — Puja (improbable con $49/día)
- [ ] ≥30 conversiones en 30 días confirmadas
- [ ] tCPA = CPA real observado
- [ ] Presupuesto reajustado según CPA y capacidad
- [ ] Ajustes por horario/dispositivo evaluados

## Fase 4 — Remarketing (opcional)
- [ ] Audiencia de visitantes ≥1000 en 30d
- [ ] RLSA en observación en Search

## Fase 6 — Offline (futuro)
- [ ] El cliente marca mensualmente las llamadas que se convirtieron en servicio (interim sin CRM)

## Recurrente (semanal, /weekly-review)
- [ ] Search terms → negativas
- [ ] Gasto vs presupuesto mensual
- [ ] CPA vs objetivo ($100); tendencia 7d vs 28d
- [ ] Anuncios rechazados / limitados
- [ ] IS perdido por presupuesto y por ranking
- [ ] Calidad de leads reportada
- [ ] Log en log/YYYY-MM-DD.md

## Hecho fuera de fase
- [x] 2026-09-29 Investigación inicial + brief prellenado — Claude
- [x] 2026-10-01 76 negativas + 3 keywords del competidor pausadas — Claude
- [x] 2026-10-01 Weekly review + strategy v1 — Claude
