---
cliente: Colton Sunflower Burial and Cremation
slug: colton-sunflower
fase_actual: 0
actualizado: 2026-10-06
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
- [ ] ⚠️ (PMM) Página /thank-you/ + redirect del formulario de Elementor (hoy es mensaje inline; /thank-you/ da 404)
- [ ] ⚠️ (PMM) Conversión "Form Fill" (URL /thank-you/) creada y probada con Tag Assistant
- [ ] ⚠️ (PMM/Cliente) Formulario arriba en /, /cremation/ y /pricing/; Email y Mensaje opcionales
- [ ] (PMM) Verificar que AW-18369353359 sea el tag de la cuenta 151-776-2744
- [ ] ⚠️ (PMM) "Calls from Ads" con duración mínima de 60s — verificar configuración
- [x] (PMM) "Website Calls" existe — verificar que sea clic en teléfono o desvío, como primaria
- [ ] (PMM) Conversiones secundarias marcadas como secundarias
- [ ] (PMM) GA4 vinculado y audiencia "Todos los visitantes" importada
- [ ] (PMM) Campos ocultos UTM + GCLID en el formulario
- [x] (PMM) Negativas universales/nicho: 466 previas + 76 nuevas (2026-10-01)
- [ ] ⚠️ (Claude, tras OK) Quitar las negativas amplias que bloquean demanda: how, Fontana, online
- [ ] (Claude, tras OK) 18 negativas de data/2026-10-06-negatives.txt (incluye las 5 del 01-oct)
- [ ] ⚠️ (PMM) Autoaplicación de recomendaciones DESACTIVADA — verificar
- [x] (Claude) /audit-landing 2026-10-01: 12/22, requiere ajustes (ver audit-site.md)
- [ ] (PMM) Score de PageSpeed móvil (no se pudo medir aquí)
- [ ] (Cliente) Proceso de respuesta a leads: quién contesta, en cuánto tiempo, horario; ¿24/7?
- [ ] (Cliente) Número de call tracking aprobado
- [ ] ⚠️ (Jhombis/Cliente) /onboard: ticket, margen, capacidad, idioma ES, mascotas, **radio real**
- [ ] ⚠️ (Jhombis) Relación con Inland Memorial / Sunflower Riverside → radios sin solape
- [ ] (Jhombis) ¿$2,500/mes netos o con fee? (diario actual $49)
- [ ] (Jhombis) Acordar quién más edita la cuenta (keywords removidas por terceros)
- [x] Claims del copy confirmados en el sitio (2026-10-01)
- [ ] (Cliente) Cambiar el email de contacto @murrietavalleyfh.com por uno de coltonfuneral.com
- [ ] (Jhombis) Confirmar si Colton Sunflower es del grupo Murrieta Valley FH (cliente PMM)
- [ ] ⚠️ (Jhombis) Definir zonas entre Colton, Sunflower Riverside e Inland Memorial: las tres convierten o pujan en San Bernardino
- [ ] (PMM) Etiquetar las cuentas funerarias del MCC con nicho:funeral / pais:US
- [ ] (Cliente) Conseguir y mostrar reseñas de Google: Meadow anuncia 5 estrellas

## Fase 1 — Relanzamiento
- [x] Campaña Search existente (se reestructura, no se crea de cero)
- [ ] ⚠️ Red: solo Búsqueda; socios y Display apagados — verificar
- [x] Ubicación: Presencia solamente
- [ ] Países restantes excluidos — verificar
- [ ] Programación según horario del cliente (24/7 solo si contestan)
- [x] Puja: Max clics ya tiene tope de CPC $7 (detectado 2026-10-06)
- [ ] ⚠️ Puja: subir tope de $7 a $8 el día de la reestructura
- [ ] Puja: Max conversiones cuando haya 15+ conv/mes estables con Form Fill medido
- [ ] ⚠️ Estructura v2.0: 5 ad groups (Cremation, Cremation Prices, Funeral Home, Burial, Brand), frase + exacta, pausar todas las amplias (data/estructura-2026-10-06.csv)
- [ ] Regla de guarda D7: si el gasto < $34/día, agregar frases y subir tope a $9 (sin volver a la amplia)
- [ ] Negativas entre ad groups (cremation/burial/cost)
- [ ] ⚠️ 1 RSA por grupo (máx. 2), H1 pinneado, 15H/4D, fuerza "Buena"+; reemplazar el RSA 819740188547
- [ ] Extensiones: sitelinks 4+, callouts 6+, snippets, llamada, ubicación
- [ ] URLs finales verificadas (200, https, sin redirect)
- [ ] Presupuesto $49/día (+ marca $5/día si se confirma)
- [ ] Anuncios aprobados (revisar 24h después)
- [ ] ⚠️ Primera conversión registrada después del relanzamiento

## Mejoras de landing (Fase 2–3, ver audit-site.md)
- [ ] (Cliente/PMM) Widget de reseñas de Google
- [ ] (PMM) H1 en la home, /pricing/ y /cremation/
- [ ] (PMM) Botón de llamada sticky en móvil
- [ ] (PMM) Caché de página + quitar JS sin uso (TTFB 1.3–3.5 s)

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
- [ ] CPA vs objetivo ($73); tendencia 7d vs 28d
- [ ] Anuncios rechazados / limitados
- [ ] IS perdido por presupuesto y por ranking
- [ ] Calidad de leads reportada
- [ ] Log en log/YYYY-MM-DD.md

## Hecho fuera de fase
- [x] 2026-09-29 Investigación inicial + brief prellenado — Claude
- [x] 2026-10-01 76 negativas + 3 keywords del competidor pausadas — Claude
- [x] 2026-10-01 Weekly review + strategy v1 — Claude
- [x] 2026-10-01 /audit-landing, /competitors, /benchmark-interno — Claude
- [x] 2026-10-06 /diagnose + estructura v2.0 — Claude
