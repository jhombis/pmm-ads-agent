---
cliente: 290 Tow and Recovery
slug: 290-tow-recovery
D0: 2026-09-24
actualizado: 2026-10-06
fase_actual: 1
plan_es: https://claude.ai/artifact/1ioZ9Qfes7GymvgprjRRbV
plan_en: https://claude.ai/artifact/8kNSv1uraooYbcADP5mzDY
---

# Roadmap — 290 Tow and Recovery

> **Reprogramado el 2026-10-06.** La Fase 0 (24/09 → 29/09) y la reestructura (30/09) **no se ejecutaron**. La cuenta siguió con la plantilla PLL: en 18 días gastó $530.14 a un CPL de $88.36, con 45.8% de desperdicio rastreable (`log/2026-10-06-diagnose.md`). Las fechas se recalculan desde hoy; las condiciones de paso no cambian.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Medición + negativas | 2026-10-06 → 2026-10-08 | 🔄 en curso (atrasada desde el 29/09) |
| 1 — Reestructura Search | aplicada 2026-10-06 · condición 2026-10-13 | 🔄 aplicada, en prueba |
| 2 — Limpieza D7 · D14 · D30 | 2026-10-13 · 2026-10-20 · 2026-11-05 | ⏳ pendiente |
| 3 — Maximizar conversiones → tCPA | Max conv ~2026-11-06 · tCPA ~2027-01 | ⏳ pendiente |
| 4 — Remarketing (RLSA) | Sin fecha | ⛔ no califica por volumen |
| 5 — Performance Max | No antes de 2027-03 | ⛔ bloqueada |
| 6 — Conversiones offline | Fuera de alcance | ⏳ futuro |
| Pista Landing | 2026-10-06 → 2026-10-23 | 🔄 en curso |
| Pista GBP + LSA | GBP ~2026-10-27 · LSA ~2026-11-24 | ⏳ pendiente (cliente) |

## Fase 0 — Medición + negativas
- **Fecha estimada**: 2026-10-06 → 2026-10-08.
- **Condición de paso**: medición verificada y negativas aplicadas.
  - Medición: Calls from Ads con umbral de 60 s, Website Calls probada y Form Fill como secundaria hasta que exista `/thank-you/`.
  - Negativas: universal + nicho v2 + las 63 nuevas.
  - Ambas con OK de Jhombis.
- **Tareas**:
  - **PMM, 10-07**:
    - Revisar en Detalles de llamadas las 8 llamadas (25-sep, 28-sep, 29-sep, 2-oct, 4-oct): duración, código de área y hora.
    - Confirmar el umbral de 60 s y que AW-18397446767 es de esta cuenta.
  - **PMM, 10-07**: pasar Form Fill a secundaria. Crear `/thank-you/` con redirect del formulario y quitar el popup "Your Booking Is Not Yet Confirmed". Probar con Tag Assistant.
  - **PMM, 10-07, requiere OK**: `/negatives` con la universal, `data/negatives-nicho.txt` (sin "cheap") y `data/2026-10-06-negatives.txt`.
  - **Cliente**: cruzar las 8 llamadas (¿clientes o gente buscando a otra grúa?); quién contesta de noche; ticket y margen; área real (Fair Oaks Ranch/Bulverde/Spring Branch); roadside que presta.
  - **Jhombis**: avisar al cliente que la proyección realista es **~14–24 llamadas/mes en el mes 2**, no 35–55.
- **Riesgos**:
  - Cada día sin negativas cuesta ~$27, con ~46% de desperdicio.
  - Si el cliente no responde, la reestructura sale igual con supuestos (geo sin exclusiones).

## Fase 1 — Reestructura Search
- **Aplicada el 2026-10-06** (adelantada con OK de Jhombis; detalle e IDs en `log/2026-10-06.md`). La condición se revisa el **2026-10-13**.
- **Falta en la UI**: fijar el H1 de los 3 RSA, URL final por keyword de exotic/flatbed en AG2, confirmar "Presencia" y el call asset.
- **Reserva**: la medición de F0 sigue sin verificar; hasta cerrarla, las conversiones nuevas no cuentan para la condición si no se cruzan con el cliente.
- **Condición de paso**: 7 días activa, anuncios aprobados y ≥1 conversión verificada con el cliente.
- **Qué se lanza** (`/build-campaign` o manual, según `strategy.md` v3):
  - Campaña existente conservada, con 3 grupos:
    - AG1 "Ad group 1 - Towing General": keywords nuevas en frase/exacta y RSA nuevo.
    - AG2 "Ad group 2 - Exotic Car & Long Distance towing": se rellena, con URL por keyword.
    - AG3 Roadside, nuevo, solo exacta.
  - Se eliminan todas las keywords en amplia, sobre todo "roadside assistance" ($140.05, 26% del gasto).
  - Maximizar clics con **tope de CPC de $6.50** · $27/día · 24/7 · presencia en 40 mi recentrado.
  - 1 RSA por grupo, de `data/ads-search-towing.md`.
- **Riesgos**:
  - Con el tope, la campaña puede no gastar los $27 ("towing near me" hoy cuesta $9.67). Si en el D7 gasta < 70%: sumar keywords de ciudad y abrir AG3 a frase. Nunca volver a la amplia.

## Fase 2 — Limpieza
- **Fechas**: **2026-10-13** (D7) · **2026-10-20** (D14) · **2026-11-05** (D30), contadas desde el 10-06.
- **Condición de paso**: 3 revisiones con `/weekly-review`, negativas aplicadas, desperdicio < 15% del gasto rastreable y keywords sin impresiones en 30 días pausadas.
- **Qué se revisa**:
  - search terms
  - % de gasto de AG3 (tope 20%)
  - AG2 (> $100 sin llamadas → pausar)
  - CPC real contra el tope
  - geo
  - calidad de las llamadas reportada por el cliente en el D30

## Fase 3 — Optimización de puja
- **Paso A, Maximizar conversiones**: ~2026-11-06.
  - Condición: ≥15 conversiones **verificadas**/mes con medición limpia (estándar 6).
  - Supuesto: ~126 clics/mes × 11–19% = 14–24 conversiones/mes. Es alcanzable en el mes 2 solo si se sostiene el escenario base.
- **Paso B, tCPA**: ~2027-01.
  - Condición: ~30 conversiones en 30 días, fijado desde el CPA observado × 1.1.
  - Supuesto: con $825/mes, 30 conversiones exigen un CPL ≤ $27.50. La cohorte del MCC converge a $15–28 recién en los meses 3–6 (`towing-us.md`).
- **Si no se cumple en fecha**:
  - CVR < 10%: landing (H1, velocidad).
  - CPC > $7: keywords de ciudad.
  - Volumen insuficiente: Maximizar conversiones sin tCPA como estado estable.
  - **Nunca forzar tCPA.**

## Fase 4 — Remarketing
- **Fecha estimada**: sin fecha.
- **Condición**: ≥1,000 visitantes en 30 días. Con ~126 clics/mes y orgánico ≈ 0, no se alcanza. Además, towing es compra de emergencia.

## Fase 5 — Performance Max
- **Fecha estimada**: no antes de **2027-03** (6 meses de Search estable).
- **Condiciones que fallan** (`pmax-cuando-y-como.md` + `towing-us.md`):
  1. Las cuentas del MCC lo agregan después de 6–12 meses de Search. Las 2 que lo lanzaron antes de los 3 meses fracasaron.
  2. No hay 30+ conversiones/mes verificadas.
  3. No hay assets propios (fotos de stock) ni GBP.
  4. Presupuesto: ~$44/día solo para PMax, contra $27 del total.
- **Qué la destraba**: pauta ≥ $1,300/mes, fotos y video reales de las grúas, y GBP con reseñas.

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance, sin CRM.
- **Mínimo útil**: una hoja compartida llamada → trabajo sí/no → ticket, para medir la calidad en el D30.

## Pista paralela — Landing
| Ajuste | Tipo | Fecha | Responsable |
|---|---|---|---|
| `/thank-you/` + redirect del formulario y quitar el popup "Not Yet Confirmed" | **Bloqueante F0** | 2026-10-07 | PMM |
| H1 de texto en el home ("24/7 Towing & Tow Truck Service in Fredericksburg, TX"); hoy no hay `<h1>` | Mejora (landing de AG1) | 2026-10-09 | PMM |
| Velocidad del home: móvil 43, LCP 6.7 s, TBT 1,170 ms → objetivo LCP < 3 s | Mejora (bloquea si baja de 40) | 2026-10-16 | PMM |
| Navy Veteran, 10% Senior Discount y radio en texto (hoy solo en la imagen) | Mejora | 2026-10-16 | PMM |
| Meta description + JSON-LD LocalBusiness/TowingService + `alt` en las imágenes | Mejora | 2026-10-23 | PMM |
| TDLR # + "Licensed & Insured" | Mejora | Al recibir el dato | Cliente → PMM |
| Formulario de emergencia de 3 campos | Mejora F2 | 2026-10-23 | PMM |
| ~~CTA de exotic~~ | **Resuelto**: verificados en el HTML el 10-06 | — | — |

## Pista paralela — GBP + LSA
- **2026-10-06 → ~2026-10-27**: el cliente crea el GBP como área de servicio, categoría "Towing service", con verificación por video. PMM da la guía. Después se vincula a Ads y arranca la campaña de reseñas.
- **~2026-10-27**: solicitud LSA con licencia TDLR, seguro y background check.
- **~2026-11-24**: LSA verificado (2–4 semanas). Presupuesto aparte o tomado de los $825: decide el cliente.
- **Bloqueante**: sin GBP no avanza nada de esta pista.

## Estacionalidad y ventanas
- **Otoño en Fredericksburg** (vinerías; Oktoberfest fue a inicios de octubre) y **luces de fin de año** (nov–dic): más visitantes en la Hwy 290. La presencia los capta.
- **Heladas de invierno**: picos de accidentes y jump starts. Revisar el tope de CPC y la capacidad del cliente.
- Conclusión: no hay razón para esperar. Cada semana sin reestructurar cuesta ~$190 con ~46% de desperdicio.

## Historial de cambios
- 2026-10-06: reestructura F1 aplicada en la cuenta (adelantada del 10-09). F2 → D7 10-13 · D14 10-20 · D30 11-05; Max conv → ~11-06.
- 2026-10-06: reprogramado tras el diagnóstico de 18 días.
  - F0 → 10-06/10-08 y F1 → 10-09.
  - Proyección corregida a 14–24 llamadas/mes.
  - tCPA → ~ene-2027 y PMax → ≥2027-03.
  - CTA de exotic resuelto.
  - Plan migrado a la plantilla PMM ES + EN.
- 2026-09-24: estructura consolidada de 7 a 3 ad groups (strategy.md v2).
- 2026-09-24: creado.
