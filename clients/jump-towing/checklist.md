---
cliente: Jump Towing LLC
slug: jump-towing
fase_actual: 0
actualizado: 2026-10-01
---

# Checklist — Jump Towing LLC

Base: `knowledge/checklists/setup-cuenta.md`, adaptada a este cliente. Responsable entre paréntesis. **[B]** = bloqueante para lanzar. /weekly-review lo actualiza.

## Fase 0 — Fundación
### Decisión urgente
- [ ] **[B]** (Jhombis) Decidir qué se hace con la campaña activa "ENHPRM Radius" en 220-410-9619: pausar (recomendado) o corregirla en caliente. Si se corrige: borrar el ad group en español, aplicar negativas, Presencia a 10 mi, broad → phrase.

### Cuenta
- [x] (PMM) Cuenta vinculada al MCC de PMM (220-410-9619)
- [ ] (PMM) Facturación verificada
- [ ] **[B]** (PMM) Revisar las conversiones existentes de 220-410-9619 (¿qué son las 7?) y degradar a secundaria cualquiera que no sea una llamada ≥60 s
- [ ] **[B]** (PMM) Lista de negativas universal PMM aplicada a nivel de cuenta
- [ ] **[B]** (PMM) `data/negatives-nicho.txt` aplicada (revisar antes: motos, lockout, flatbed según lo que confirme el cliente)
- [ ] **[B]** (PMM) Aplicación automática de recomendaciones DESACTIVADA

### Tracking
- [ ] **[B]** (Cliente) Teléfono principal confirmado y número de reenvío de Google aprobado
- [ ] **[B]** (PMM) Google Tag en todas las páginas de jumptowing.com
- [ ] **[B]** (PMM) Conversión "Llamada desde anuncio" (≥60 s), primaria
- [ ] **[B]** (PMM) Conversión "Llamada al número de reenvío en web" (≥60 s), primaria, probada con Tag Assistant
- [ ] (PMM) Conversión "Clic en teléfono" (móvil), secundaria
- [ ] (PMM) Conversión "Formulario", secundaria, probada con Tag Assistant
- [ ] (PMM) GA4 vinculado y audiencia "Todos los visitantes" importada
- [ ] (PMM) Campos ocultos UTM + GCLID en el formulario

### Economía y operación
- [ ] **[B]** (Cliente) Ticket promedio, margen y tasa de cierre → (PMM) CPL máximo calculado en brief y objetivo de $21–31 validado
- [ ] **[B]** (Cliente) Proceso de respuesta definido: quién contesta, tiempo (<60 s ideal), qué pasa si está ocupado
- [ ] (Cliente) Capacidad de trabajos/mes
- [ ] (Cliente) Decidir si se cubren domingos o noches (solo si alguien contesta)

### Servicios y claims (desbloquean copy [C] y ad groups)
- [ ] (Cliente) Confirmar roadside: jump start / lockout / cambio de llanta / combustible → activa R2, R3
- [ ] (Cliente) Confirmar flatbed, motos, long distance
- [ ] (Cliente) Confirmar licencia y seguro (para "Licensed & Insured")
- [ ] (Cliente) Precio base para "Local Tows From $XX" (opcional, gap de competencia)
- [ ] (Cliente) Fotos propias de grúas y equipo (activo de imagen)

### GBP y landing
- [ ] **[B]** (PMM) /audit-landing de jumptowing.com aprobado o ajustes bloqueantes resueltos
- [ ] **[B]** (PMM) Landing /towing creada (H1 de ciudad, botón de llamada fijo, horario, área de servicio)
- [ ] (PMM) Landing /jump-start creada (bloqueante solo para R1)
- [ ] (PMM) Landings /car-lockout y /flat-tire-fuel (solo si se confirma el servicio)
- [ ] (Cliente) GBP verificado con categoría "Towing service" y acceso de administrador para PMM
- [ ] (PMM) GBP vinculado a Google Ads (activo de ubicación)

### LSA (US, pista paralela)
- [ ] (PMM) Verificar disponibilidad de Towing en LSA para el área de Minneapolis
- [ ] (Cliente + PMM) Solicitud LSA iniciada: licencia, seguro, background check
- [ ] (PMM) Horario de LSA = horario real del cliente

## Fase 1 — Lanzamiento Search
- [ ] (PMM) Campaña "Search | Towing & Roadside | 10mi | v1" creada según `strategy.md` (/build-campaign), en pausa
- [ ] (PMM) Red: solo Búsqueda, socios y Display apagados
- [ ] (PMM) Ubicación: Presencia, radio de 10 mi en (45.093312, -93.343931); resto de países excluidos
- [ ] (PMM) Programación: lun–vie 6:00–18:00, sáb 6:00–15:30, dom off (America/Chicago)
- [ ] (PMM) Puja: Maximizar conversiones, sin tCPA
- [ ] (PMM) Keywords en phrase + exacta para los top de cada grupo; sin broad
- [ ] (PMM) Negativas cruzadas entre ad groups (ver strategy.md)
- [ ] (PMM) 3 RSA por ad group, H1 pinneado, 15H/4D, fuerza "Buena" o superior; sin claims [C] no confirmados
- [ ] (PMM) Extensiones: sitelinks (4+), callouts (6+), snippet de servicios, llamada, ubicación (si hay GBP)
- [ ] (PMM) URLs finales verificadas (200, https, sin redirect)
- [ ] (PMM) Presupuesto $31/día
- [ ] (PMM) Campaña vieja "ENHPRM Radius" pausada el mismo día del lanzamiento
- [ ] (PMM) Anuncios aprobados (revisar 24 h después)
- [ ] (PMM) Primera llamada ≥60 s registrada

## Fase 2 — Limpieza (D7 2026-10-19 · D14 2026-10-26 · D30 2026-11-11)
- [ ] (PMM) D7: search terms revisados, negativas agregadas (otras ciudades, aseguradoras, competidores)
- [ ] (PMM) D7: keywords sin impresiones identificadas (no pausar aún)
- [ ] (PMM) D7: gasto real vs ritmo de $825/mes
- [ ] (PMM) D14: search terms revisados, negativas agregadas
- [ ] (PMM) D14: ad groups/keywords con ≥$62 de gasto y 0 conversiones marcados para revisión
- [ ] (PMM) D30: search terms revisados, negativas agregadas
- [ ] (PMM) D30: keywords con 0 impresiones en 30 días pausadas
- [ ] (PMM) D30: RSA de peor rendimiento por grupo reemplazado
- [ ] (Cliente) D30: reporte de calidad de leads recibido (llamada → trabajo sí/no)
- [ ] (PMM) D30: preparar propuesta de presupuesto de invierno si el IS perdido por presupuesto es >40%

## Fase 3 — Optimización de puja (estimada 2026-11-25)
- [ ] (PMM) ≥30 llamadas ≥60 s en 30 días confirmadas
- [ ] (PMM) tCPA = CPL real de 30 días (no el deseado)
- [ ] (PMM) Presupuesto reajustado según CPL y capacidad del cliente
- [ ] (PMM) Ajustes por horario/dispositivo evaluados con datos

## Fase 4 — Remarketing (opcional; probablemente no califica)
- [ ] (PMM) Audiencia de visitantes ≥1,000 en 30 días
- [ ] (PMM) RLSA en observación en Search

## Fase 5 — Performance Max (bloqueada por presupuesto; ver roadmap)
- [ ] (PMM) Condiciones de `pmax-cuando-y-como.md` verificadas (requiere ≥$78/día solo para PMax)

## Fase 6 — Conversiones offline (fuera de alcance, sin CRM)

## Recurrente (semanal, /weekly-review)
- [ ] Search terms → negativas
- [ ] Gasto vs presupuesto mensual ($825)
- [ ] CPL vs objetivo ($21–31); tendencia 7d vs 28d
- [ ] Anuncios rechazados o limitados
- [ ] IS perdido por presupuesto y por ranking
- [ ] Calidad de leads reportada por el cliente
- [ ] Log escrito en `log/YYYY-MM-DD.md`
