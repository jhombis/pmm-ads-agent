---
cliente: Jump Towing LLC
slug: jump-towing
fase_actual: 0
actualizado: 2026-10-08
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
- [x] (PMM) Call tracking: CallFire (612) 665-6274 → (612) 616-0723, conectado al MCP (08-oct)
- [x] (PMM) Dónde se usa el número de CallFire: en la web jumptowing.com (tel: en el sitio, 08-oct). Falta saber si también está en la extensión de llamada y en el GBP
- [ ] (PMM) Explicar el hueco del 26-sep al 02-oct sin llamadas (¿campaña pausada o limitada?)
- [ ] **[B]** (PMM) Google Tag en todas las páginas de jumptowing.com
- [ ] **[B]** (PMM) Conversión "Llamada desde anuncio" (≥60 s), primaria
- [ ] **[B]** (PMM) Conversión "Llamada al número de reenvío en web" (≥60 s), primaria, probada con Tag Assistant
- [ ] (PMM) Conversión "Clic en teléfono" (móvil), secundaria
- [ ] (PMM) Conversión "Formulario", secundaria, probada con Tag Assistant
- [ ] (PMM) GA4 vinculado y audiencia "Todos los visitantes" importada
- [ ] (PMM) Campos ocultos UTM + GCLID en el formulario

### Economía y operación
- [ ] **[B]** (Cliente) Ticket promedio, margen y tasa de cierre → (PMM) CPL máximo calculado en brief y objetivo de $21–31 validado
- [ ] **[B]** (Cliente) Proceso de respuesta definido: quién contesta, tiempo (<60 s ideal), qué pasa si está ocupado (CallFire: 89% contestadas, 2 perdidas en horario el 06 y 07-oct)
- [ ] (Cliente) Capacidad de trabajos/mes
- [ ] (Cliente) Decidir si se cubren domingos o noches (solo si alguien contesta)

### Servicios y claims (desbloquean copy [C] y ad groups)
- [ ] (Cliente) Confirmar roadside: jump start / lockout / cambio de llanta / combustible → activa las keywords de G4
- [ ] (Cliente) Confirmar flatbed, motos, long distance
- [ ] (Cliente) Confirmar licencia y seguro (para "Licensed & Insured")
- [ ] (Cliente) Precio base para "Local Tows From $XX" (opcional, gap de competencia)
- [ ] (Cliente) Fotos propias de grúas y equipo (activo de imagen)

### GBP y landing
- [ ] **[B]** (PMM) /audit-landing de jumptowing.com aprobado o ajustes bloqueantes resueltos
- [x] (PMM) Landing /jump-towing/towing/ publicada en el dominio de PMM (08-oct, solo llamada)
- [x] (PMM) Landing /jump-towing/roadside/ publicada en el dominio de PMM (08-oct, solo llamada; jump start + remolque)
- [ ] (PMM) Formulario GHL con gclid/UTM y redirección a /gracias/ → ghl.form_id en los dos spec.json (hoy: excepción solo llamada aprobada por Jhombis el 08-oct)
- [x] (PMM) Política de privacidad para las landings → jumptowing.com/privacy-policy/ (08-oct)
- [x] (PMM) Conversión en las landings: GTM del cliente GTM-T9JFQNTC (AW-18347375568, llamadas web + clic) (08-oct)
- [x] (PMM) Landings publicadas en Plesk: 200 y H1 verificados desde el servidor (08-oct)
- [ ] **[B]** (PMM) Tag Assistant en las landings: el número cambia al de reenvío de Google y el clic en llamada dispara la conversión una vez
- [ ] (PMM) Confirmar que AW-18347375568 es la cuenta 220-410-9619
- [ ] (Jhombis) Confirmar el dominio de las landings: el de PMM (listas) o jumptowing.com (/landing-ghl)
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
- [ ] **[B]** (PMM) Verificar la zona horaria de la cuenta (customer.time_zone) y el horario en la orden de pedido antes de programar y de dejar horas en los anuncios (playbook §11: horario mal convertido entre zonas)
- [ ] (PMM) Programación: lun–vie 6:00–18:00, sáb 6:00–15:30, dom off (America/Chicago)
- [ ] (PMM) Puja: Maximizar clics con tope de CPC $8
- [ ] (PMM) Keywords en phrase + exacta para los top de cada grupo; sin broad
- [ ] (PMM) Negativas cruzadas entre ad groups (ver strategy.md)
- [ ] (PMM) 1 RSA por ad group (máx. 2), H1 pinneado, 15H/4D, fuerza "Buena" o superior; sin claims [C] no confirmados
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
- [ ] (PMM) D7: llamadas CallFire (contestadas, calificadas ≥60 s, perdidas en horario)
- [ ] (PMM) D14: search terms revisados, negativas agregadas
- [ ] (PMM) D14: ad groups/keywords con ≥$62 de gasto y 0 conversiones marcados para revisión
- [ ] (PMM) D30: search terms revisados, negativas agregadas
- [ ] (PMM) D30: keywords con 0 impresiones en 30 días pausadas
- [ ] (PMM) D30: costo por llamada calificada (CallFire) vs meta de $41.51
- [ ] (Cliente) D30: reporte de calidad de leads recibido (llamada → trabajo sí/no)
- [ ] (PMM) D30: preparar propuesta de presupuesto de invierno si el IS perdido por presupuesto es >40%

## Fase 3 — Optimización de puja (estimada 2026-11-25)
- [ ] (PMM) ≥15 llamadas calificadas en 30 días → pasar a Maximizar conversiones
- [ ] (PMM) ≥30 llamadas calificadas en 30 días confirmadas (para tCPA)
- [ ] (PMM) tCPA = CPA real de 30 días (no el deseado)
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
- [ ] Costo por llamada calificada vs meta F2 ($41.51); tendencia 7d vs 28d
- [ ] Anuncios rechazados o limitados
- [ ] IS perdido por presupuesto y por ranking
- [ ] Llamadas CallFire: contestadas, calificadas ≥60 s, costo por calificada, perdidas en horario
- [ ] Calidad de leads reportada por el cliente
- [ ] Log escrito en `log/YYYY-MM-DD.md`
