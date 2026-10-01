---
cliente: Spillane's Towing & Recovery
slug: spillanes-towing
D0: 2026-10-01
actualizado: 2026-10-01
fase_actual: 0
plan_es: https://claude.ai/artifact/5jRVHYZDmtkZjJ5NY8SZP5
plan_en: https://claude.ai/artifact/EKPVNm3B52xtdNnq9aL9w7
---

# Roadmap — Spillane's Towing & Recovery

> Caso especial: la cuenta **ya está activa** (campaña Search desde 2026-08-20, con gasto real desde septiembre). La Fase 0 no detiene la pauta: corrige lo urgente sobre la campaña viva y prepara la reestructuración. La Fase 1 es un **relanzamiento** con la estructura de `strategy.md`, no una cuenta nueva.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Fundación y corrección inmediata | 2026-10-01 → 2026-10-12 | 🔄 en curso |
| 1 — Relanzamiento Search (6 ad groups) | 2026-10-13 → 2026-10-20 | ⏳ pendiente |
| 2 — Limpieza D7 · D14 · D30 | 2026-10-20 · 2026-10-27 · 2026-11-12 | ⏳ pendiente |
| 3 — tCPA | ~2026-12-08 (rango 2026-11-24 → 2027-01-05) | ⏳ pendiente |
| 4 — Remarketing (RLSA) | reevaluar 2027-02 | ⛔ probablemente no califica (audiencia <1,000/30d) |
| 5 — Performance Max | no antes de 2027-03; **no realista con $989/mes** | ⛔ bloqueada |
| 6 — Conversiones offline | fuera de alcance | — |
| Pista Landing | bloqueantes 2026-10-06 · servicios 2026-10-27 → 2026-11-24 | 🔄 |
| Pista Reputación | arranque 2026-10-13 | ⏳ |

## Fase 0 — Fundación y corrección inmediata
- **Fecha estimada**: 2026-10-01 → 2026-10-12. Base D0+3 por los ajustes de landing que hace PMM, extendida a D0+11 porque varios bloqueantes dependen del cliente (+7–14 días).
- **Condición de paso**: todas las tareas bloqueantes de Fase 0 en `checklist.md` ✅.
- **Tareas, bloque A: sobre la campaña viva, sin esperar al cliente** (PMM, 2026-10-01 → 10-03):
  1. Aplicar la lista "PMM Universal", el bloque Towing y `data/negatives-nicho.txt` a nivel de cuenta (`/negatives`).
  2. Pausar la keyword `roadside assistance` (BROAD), que se lleva el 72% del gasto. Pausar `spillane's towing` (BROAD) y agregar la marca como negativa.
  3. Configurar "Calls from Ads" y "Website Calls" con **duración mínima de 60 s**; confirmar cuáles son primarias.
  4. Verificar en la UI: ubicación solo por **presencia** (radio de 12 mi), socios y Display apagados, recomendaciones automáticas apagadas, programación actual.
  5. Exportar Auction Insights (30 días) desde la UI: es el dato de competencia que falta en `competitors.md`.
  6. Tag Assistant sobre spillanestowingrecovery.com: un solo Google Tag, reemplazo de número OK y sin doble conteo.
- **Tareas, bloque B: depende del cliente** (vence 2026-10-12):
  1. **Ticket promedio y margen** por tipo de servicio → CPL máximo real.
  2. **Quién contesta de 11pm a 7am** y en cuánto tiempo → define si la campaña corre 24/7 o de 6:00 a 23:00.
  3. **Acceso de PMM al GBP** (para el activo de ubicación y la pista de reputación).
  4. Confirmar los claims: 50+ años (o desde qué año), 21 camiones / 16 flatbeds vigentes, taller propio, licencia y seguro.
  5. Servicios a evitar: lockout, llantas, long distance y heavy-duty.
  6. Fotos reales de la flota (8–10).
  7. Confirmar que (802) 216-3105 desvía a la línea principal.
- **Riesgos**:
  - **Sin proceso conocido de respuesta a leads**: si las llamadas nocturnas no se contestan, cualquier mejora de CPL es ficticia. Es bloqueante para dejar 24/7.
  - Si el ticket no llega antes del 10-12, F1 se lanza con CPL objetivo $35 provisional y el tCPA queda condicionado.

## Fase 1 — Relanzamiento Search
- **Fecha estimada**: lanzar el 2026-10-13 (martes), evaluar el 2026-10-20.
- **Condición de paso**: estructura nueva activa 7 días, anuncios aprobados, ≥1 conversión registrada con la regla de llamada ≥60 s.
- **Qué se lanza** (`strategy.md`, F1):
  - Misma campaña, $32.50/día, Maximizar conversiones.
  - 6 ad groups (Towing Near Me, 24/7 Emergency, Tow Truck, Towing Burlington VT, Accident & Recovery, Flatbed) en frase y exacta, 3 RSA cada uno.
  - Las 7 keywords BROAD pausadas. Extensiones completas.
  - Ejecución: `/build-campaign`, adaptado para modificar la campaña existente en lugar de crear una nueva.
- **Advertencias**:
  - El presupuesto ($32.50/día) está por debajo de 3× el CPL del benchmark ($48/día): el aprendizaje va a ser lento.
  - El volumen reportado va a bajar por el umbral de 60 s; no confundirlo con un deterioro.
  - Si el proceso de respuesta a leads sigue sin definir, la evaluación de F1 no es confiable.
- **Riesgos**: algunos ad groups (AG2 Emergency, AG5 Accident & Recovery) quedan con estado "pocas búsquedas". Es esperado y se resuelve en D30.

## Fase 2 — Limpieza (D7 · D14 · D30)
- **Fechas**: **2026-10-20** (D7) · **2026-10-27** (D14) · **2026-11-12** (D30).
- **Condición de paso**: las tres revisiones hechas, negativas aplicadas, keywords sin impresiones pausadas, RSA peor por grupo reemplazado.
- **Qué se revisa**:
  - Search terms: AAA, aseguradoras, impound, lockout y fuera de área son los sospechosos habituales.
  - Gasto sin conversión por ad group.
  - CPC (meta: bajar de $11.90 a ≤$7).
  - Cuota perdida por ranking (meta: <25%).
  - En D30: fusionar AG2 y AG5 si tienen <50 impresiones; decidir la prueba de "road service near me" para F3.
- **Reporte de calidad de leads** del cliente en D30: hoja simple con fecha, origen y si fue trabajo pagado.

## Fase 3 — Optimización de puja (tCPA)
- **Fecha estimada**: **~2026-12-08** (rango 2026-11-24 → 2027-01-05).
- **Supuestos**:
  - Conv./día esperadas = $32.50 ÷ CPL ~$30 (objetivo F1–F2) ≈ 1.1/día → ~28 días para 30 conversiones desde el relanzamiento (2026-10-13 → ~11-10).
  - +2 semanas por presupuesto <3× CPL/día → ~11-24.
  - +2 semanas de colchón porque la regla de 60 s reduce las conversiones contadas → **~12-08**.
  - Si el CPL baja a la mediana del MCC ($16), podría llegar el 11-24.
- **Condición de paso**: ≥30 conversiones en una ventana de 30 días, con llamada ≥60 s y formulario verificados.
- **Acción**:
  - tCPA = CPA real de los últimos 30 días (+10% de margen). Nunca el CPA "deseado".
  - Si el CPA real supera el CPL máximo del brief, **no subir presupuesto**: revisar keywords, landing y oferta antes.
  - Presupuesto: mantener $989; subir a ~$1,300 solo si se pierde >20% de cuota por presupuesto y el cliente confirma capacidad.
- **Si no se cumple en fecha**:
  - Revisar la conversión de la landing (<5% → pista Landing).
  - Revisar la calidad del tráfico (search terms).
  - Revisar si el umbral de 60 s está filtrando llamadas reales.
  - **No forzar tCPA** con menos datos.

## Fase 4 — Remarketing
- **Fecha estimada**: reevaluar en 2027-02. **Probablemente no califica.**
- **Condición de paso**: audiencia ≥1,000 usuarios en 30 días (mínimo de Google para listas en Search).
- **Por qué no ahora**: la landing de Ads recibe ~150–200 clics al mes y el sitio principal unas ~380 visitas orgánicas. Aun sumando ambos dominios no se llega a 1,000 en 30 días.
- **Acción mientras tanto**: crear ya la audiencia "Todos los visitantes" de ambos dominios en GA4, con duración de 540 días, para que acumule.
- **Si se llega**: RLSA en observación, luego ajuste de puja. Display remarketing (mínimo 100 usuarios) solo como prueba de $3–5/día, excluyendo apps.

## Fase 5 — Performance Max
- **Fecha estimada**: no antes de 2027-03 (tCPA del 12-08 + 4 semanas estable + condiciones de reputación y assets). **No realista con el presupuesto actual.**
- **Condición de paso**: TODAS las de `knowledge/estrategias/pmax-cuando-y-como.md`, más **≥3.8★ en el GBP** (condición propia de esta cuenta).
- **Condiciones que fallan hoy**:
  1. **Presupuesto**: PMax pide ≥3× CPA/día ≈ $75/día con CPA $25, contra $32.50 de toda la cuenta (y el 20–30% para PMax serían $7–10/día). Para cumplirla habría que llevar la cuenta a ~$3,000/mes, decisión del cliente.
  2. **Conversiones**: 14 al mes hoy, pide 30 con llamada ≥60 s verificada.
  3. **Reputación**: 3.2★. PMax empuja a Maps, donde convierte mal.
  4. **Assets**: no hay fotos ni video propios.
  5. **Landing**: sin thank-you page ni anti-spam.
- **Si no califica**: quedarse en Search, con remarketing cuando la audiencia lo permita.

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance (sin CRM). El cliente usa Towbook en el sitio principal: si exporta trabajos con GCLID, se reevalúa en 2027.

## Pista paralela — Landing (`audit-site.md`)
| Tarea | Tipo | Responsable | Fecha |
|---|---|---|---|
| H1 "24/7 Towing in Burlington & South Burlington, VT" + flota en el hero | Bloqueante F0 | PMM | 2026-10-06 |
| Form de 3 campos en el hero móvil | Bloqueante F0 | PMM | 2026-10-06 |
| `/thank-you/` + conversión "Form Fill" por page-view | Bloqueante F0 | PMM | 2026-10-06 |
| Quitar el link "Google" (share.google) | Bloqueante práctico | PMM | 2026-10-02 |
| Medir PageSpeed móvil (API key o manual) y corregir si el score es <40 | Bloqueante F0 | PMM | 2026-10-06 |
| `/towing/` (AG1–AG4) | Mejora F2 | PMM | 2026-10-27 |
| `/accident-recovery/` (AG5): **antes de la primera nieve** | Mejora F2 (prioridad estacional) | PMM | 2026-11-10 |
| `/flatbed-towing/` (AG6) | Mejora F2–F3 | PMM | 2026-11-24 |
| Oferta concreta (tiempo de llegada / tarifa local) cuando el cliente la confirme | Mejora F3 | PMM + Cliente | tras confirmación |
| 4–6 reseñas reales con ciudad + fotos de flota | Mejora F2 | Cliente (material) / PMM | 2026-11-12 |
| Unificar horario 24/7 entre el sitio principal y la landing | Mejora F1 | Cliente | 2026-10-12 |

## Pista paralela — Reputación (no es Ads, pero limita a Ads)
- **2026-10-13**: el cliente empieza a pedir reseña por SMS o QR a cada trabajo de servicio voluntario (no impound). Meta: +30 reseñas en 90 días.
- **Desde que PMM tenga acceso al GBP**: responder todas las reseñas negativas.
- Evaluar separar la operación de impound en otro perfil o número si es viable (lo decide el cliente).
- Hito: 3.5★ (habilita seller ratings) y 3.8★ (condición de PMax). Revisión mensual en `/weekly-review`.

## Pista paralela — LSA
- No aplica: towing no es categoría de Local Services Ads.

## Estacionalidad y ventanas
- **Invierno en Vermont (nov–mar)**: picos de demanda en tormentas (winch-outs, salidas de pista, baterías). Relanzar el 10-13 da 3 semanas de aprendizaje antes de la primera nieve (normalmente a mediados o fines de noviembre).
- `/accident-recovery/` y AG5 deben estar listos para el 11-10.
- En tormentas fuertes, revisar en el momento la cuota perdida por presupuesto. Si es >20% con CPL ≤ objetivo, considerar +20–30% de presupuesto temporal (con aprobación del cliente y confirmando capacidad).
- **Verano (jun–ago)**: menor demanda. Evaluar bajar presupuesto o reasignarlo a la prueba de roadside/flatbed.

## Historial de cambios
- 2026-10-01: creado (D0 = 2026-10-01).
- 2026-10-01: plan ES/EN rehecho con la plantilla PMM (`plan-es.html`, `plan-en.html`) y republicado en las mismas URLs.
