---
cliente: RR Roadside Relief
slug: rr-roadside-relief
fase_actual: 0
actualizado: 2026-10-08
---
# Checklist — RR Roadside Relief

Base: `knowledge/checklists/setup-cuenta.md` + tareas propias del cliente. La cuenta ya está activa desde el 2026-09-15, así que algunos ítems de Fase 0/1 ya están ✅ (verificados por Windsor o por la web). ⛔ = bloqueante para pasar de fase.

## Fase 0 — Fundación (correcciones con la cuenta activa)
### Cuenta y conversiones
- [x] (PMM) Call tracking conectado: CallFire (405) 536-9093 → (405) 953-5281; export y resumen en `log/2026-10-08.md`
- [x] (PMM) Cuenta vinculada al MCC de PMM (425-405-2574)
- [ ] (PMM) Facturación verificada
- [ ] ⛔ (PMM) "Calls from Ads" con duración mínima de 60 s, única conversión primaria de llamada
- [ ] ⛔ (PMM) Tag Assistant: `AW-18397439627` es de esta cuenta; "Form Fill" sin doble conteo (Site Kit `GT-PHCMTZJ8` + GTM `GTM-TS99RXK7`)
- [ ] ⛔ (PMM) Conversión de **llamadas desde la web** (número de desvío de Google en el sitio o clic en `tel:(405)5369093`): Ads cuenta 7 de 19 llamadas calificadas (CallFire, 16-sep → 01-oct)
- [ ] (PMM) Conversiones secundarias marcadas como secundarias
- [ ] (PMM) GA4 (`GT-PHCMTZJ8`) vinculado y audiencia "Todos los visitantes" importada
- [ ] (PMM) Campos ocultos UTM + GCLID en los formularios de Elementor
- [ ] (PMM) Aplicación automática de recomendaciones DESACTIVADA (verificar)

### Negativas
- [ ] ⛔ (Jhombis) OK para aplicar `data/2026-10-01-negatives.txt` (238 términos)
- [ ] ⛔ (PMM) Aplicar `data/negatives-nicho.txt` §A–C (competidores, agregadores, servicios que no ofrece)
- [ ] ⛔ (PMM) Quitar las negativas existentes que bloquean servicios: `[tire change near me]`, `tire change service near me`, `tire repair near me`, `flat tire service`, `flat tire service near me`, `[Flat tire repair]`, `flat tire repair near me`, `mobile`, `quick`, `budget` (§F)
- [ ] (PMM) Revisar las demás negativas amplias de una palabra (discount, new, national, elite, marcas de autos)
- [ ] (PMM) Crear la lista compartida "PMM Universal" a nivel de cuenta (vía API/Editor; Windsor no puede)

### Confirmaciones del cliente (vía Jhombis)
- [ ] ⛔ (Cliente) Presupuesto real de pauta (el paquete de $2,250 no es todo pauta)
- [ ] ⛔ (Cliente) Área de servicio real → radio de la campaña (supuesto: 25 mi desde OKC)
- [x] (PMM) 24/7 real verificado con CallFire: 22 de 23 llamadas nocturnas contestadas (16-sep → 08-oct)
- [ ] (Cliente) Proceso de respuesta: quién contesta; revisar 5 llamadas perdidas de día en 23 días
- [ ] (Cliente) Tarifas/oferta sostenible (habilita AG4 y los headlines de precio ⚠)
- [ ] (Cliente) ¿Atienden en español? (habilita AG10)
- [ ] (Cliente) Licencia y seguro (callout "Licensed & Insured" ⚠, requisito LSA)
- [ ] (Cliente) Ticket promedio y tasa de cierre → CPL máximo real
- [ ] (Cliente) ¿ETA realista? (no prometemos <30 min sin confirmar)

### GBP y LSA
- [ ] ⛔ (Cliente) Google Business Profile creado/verificado, categoría "Towing service", acceso para PMM
- [ ] (PMM) GBP vinculado a Google Ads (activo de ubicación)
- [ ] (PMM) Solicitud LSA iniciada (después del GBP)

### Landing (pista paralela, ver `audit-site.md`)
- [x] (PMM) Auditoría → `audit-site.md` 10/22
- [ ] ⛔ (PMM/quien edite ⚠) Formulario de 4 campos arriba: home, /light-medium-duty-towing/, /roadside-assistance/
- [ ] ⛔ (PMM) PageSpeed móvil medido; logo 676 KB → <30 KB; headers → <100 KB; caché de página
- [ ] (PMM) H1 en home + H1 de servicio con "Oklahoma City"
- [ ] (PMM) Botón "Call Now" fijo en móvil
- [ ] (PMM) /thank-you/ con URL propia
- [ ] (Cliente) Indicar quién edita la web (PMM vs tercero)

## Fase 1 — Relanzamiento Search (`/build-campaign`)
- [ ] (PMM) Ad groups AG1–AG9 creados en la campaña 24255091376 según `strategy.md` (AG10 solo con español confirmado y landing ES)
- [x] (PMM) Red: solo Búsqueda, sin partners ni Display (verificado)
- [x] (PMM) Ubicación: Presencia (verificado)
- [ ] (PMM) Radio ajustado al área confirmada; idiomas EN + ES
- [ ] (PMM) Programación: 24/7 solo si el cliente confirma que contesta de noche
- [x] (PMM) Puja: Maximizar conversiones (verificado)
- [ ] (PMM) Keywords en frase/exacta según `data/keywords.csv`; "Ad group 1" (amplia) en PAUSA
- [ ] (PMM) Negativas de ruteo por ad group (`data/negatives-nicho.txt` §D–E)
- [ ] (PMM) 3 RSA por grupo, H1 pinneado, 15H/4D, sin headlines ⚠ no confirmados, fuerza "Buena" o más
- [ ] (PMM) Extensiones: 4+ sitelinks, 6+ callouts, snippet Services, llamada, ubicación (requiere GBP)
- [ ] (PMM) URLs finales verificadas (200, https, sin redirect)
- [ ] (PMM) Presupuesto diario según la pauta confirmada (supuesto $43/día)
- [ ] (PMM) Anuncios aprobados (revisar 24 h después)
- [ ] (PMM) Primera conversión registrada con llamada ≥60 s

## Fase 2 — Limpieza (D7 2026-10-15 · D14 2026-10-22 · D30 2026-11-07)
- [ ] D7: search terms revisados, negativas agregadas
- [ ] D7: llamadas CallFire vs conversiones de Ads (calificadas ≥60 s, perdidas, costo por llamada calificada)
- [ ] D7: keywords sin impresiones identificadas (no pausar aún)
- [ ] D14: search terms revisados, negativas agregadas
- [ ] D14: keywords/ad groups con gasto >$90 y 0 conversiones marcados para revisión
- [ ] D30: search terms revisados, negativas agregadas
- [ ] D30: keywords con 0 impresiones en 30 días pausadas
- [ ] D30: RSA de peor rendimiento por grupo reemplazado
- [ ] D30: reporte de calidad de leads del cliente recibido (% de llamadas reales; llamadas nocturnas perdidas)
- [ ] D30: IS perdido por ranking < 40%
- [ ] (PMM) Landings nuevas publicadas: /flat-tire-change/, /car-lockout/, /jump-start/, /flatbed-motorcycle-towing/ (y /es/ si aplica) y ad groups re-apuntados

## Fase 3 — Optimización de puja (estimada ~2026-11-16)
- [ ] ≥30 conversiones en 30 días con tracking verificado (CallFire ya ve ~35 calificadas/30 d; falta que Ads las cuente)
- [ ] Cliente confirma ≥70% de leads reales
- [ ] tCPA = CPA real observado (no el deseado)
- [ ] Presupuesto reajustado según CPA y capacidad (3 flatbeds)
- [ ] Ajustes por horario/dispositivo evaluados con datos

## Fase 4 — Remarketing (no antes de 2027-Q1)
- [ ] Audiencia de visitantes ≥1,000 en 30 días (hoy ~250–300 clics/mes: requiere más presupuesto o tráfico orgánico)
- [ ] RLSA en observación en Search

## Fase 5 — Performance Max (bloqueada: presupuesto y assets)
- [ ] Pauta total ≥ ~$120/día
- [ ] tCPA estable 4 semanas
- [ ] 5+ fotos reales, logo y 1 video corto de los flatbeds
- [ ] Anti-spam en el formulario (honeypot/reCAPTCHA v3)
- [ ] Conversión de landing ≥5% confirmada

## Fase 6 — Conversiones offline (futuro, requiere CRM)
- [ ] Cliente registra los leads con GCLID

## Recurrente (semanal, /weekly-review)
- [ ] Search terms → negativas
- [ ] Gasto vs presupuesto mensual
- [ ] CPA vs objetivo (≤$45 F1–F2; $12–18 desde el mes 3); tendencia 7d vs 28d
- [ ] Anuncios rechazados/limitados
- [ ] IS perdido por presupuesto y por ranking
- [ ] Calidad de leads reportada por el cliente
- [ ] Log en `log/YYYY-MM-DD.md`
- [ ] Invierno: alerta de tormentas de hielo → subir presupuesto 50–100% si hay capacidad
