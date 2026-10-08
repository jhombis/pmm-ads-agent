---
cliente: Jump Towing LLC
slug: jump-towing
D0: 2026-10-01
actualizado: 2026-10-08
fase_actual: 0
plan_es: https://claude.ai/artifact/G41fXXn8ejrpzJN7JykQu5
plan_en: https://claude.ai/artifact/U2e1QfnLLPYpek6vs2bGpn
---

# Roadmap — Jump Towing LLC

> Las fechas son proyección; la condición de paso es la que manda. `/weekly-review` avanza de fase solo cuando la condición se cumple.
> Inputs: brief.md, strategy.md v2, benchmark.md y log/2026-10-08.md (llamadas CallFire). **audit-site.md no existe** (jumptowing.com bloqueado por el proxy), así que la Fase 0 se estima con el supuesto de que la landing necesita ajustes que hace PMM.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Fundación | 2026-10-01 → 2026-10-18 (reprogramada el 08-oct) | 🔄 en curso · call tracking ✅, siguen bloqueantes del cliente y de la landing |
| 1 — Lanzamiento Search | 2026-10-19 → 2026-10-26 | ⏳ |
| 2 — Limpieza D7 · D14 · D30 | 2026-10-26 · 2026-11-02 · 2026-11-18 | ⏳ |
| 3 — Puja: Max. conversiones → tCPA | Max. conv. desde 2026-11-18 si ≥15 calificadas/30d · tCPA no antes de 2026-12-18 | ⏳ (Max. conv. probable; tCPA improbable con $825) |
| 4 — Remarketing | no antes de 2027-T1 | ⏳, probablemente no califica (tráfico) |
| 5 — PMax | no realista con $825/mes | ⛔ por presupuesto |
| 6 — Conversiones offline | fuera de alcance | — |
| Pista Landing | 2026-10-01 → 2026-10-16 | 🔄 |
| Pista LSA | desde que haya GBP + 2–4 semanas | ⏳ (depende del GBP) |

## Fase 0 — Fundación
- **Fecha estimada**: 2026-10-01 → **2026-10-18** (D0+17). Se planeó hasta el 11-oct; al 08-oct siguen abiertos ticket/margen, el audit de la landing, la landing /towing y la decisión sobre la campaña actual, así que se corre una semana. El call tracking ya está resuelto (CallFire).
- **Condición de paso**: todos los ítems bloqueantes de Fase 0 en `checklist.md` en ✅.
- **Tareas**:
  - (Jhombis, **hoy**) Decidir qué se hace con la campaña activa de 220-410-9619. Gasta ~$190/semana a CPL $65.57 con broad, Maximizar clics, ad group en español y geo dudosa. Recomendación: **pausarla** hasta el lanzamiento de v1. Si no se pausa, como mínimo: borrar el ad group en español, aplicar negativas universales + nicho, verificar la geo (Presencia, 10 mi) y pasar las keywords broad a phrase.
  - (Cliente) Ticket promedio, margen y tasa de cierre → PMM calcula el CPL máximo y valida el objetivo de $21–31.
  - ✅ 08-oct: call tracking CallFire (612) 665-6274 → (612) 616-0723, conectado. 28 llamadas, 12 calificadas ≥60 s entre el 14-sep y el 08-oct (`log/2026-10-08.md`).
  - (PMM) Confirmar dónde se usa el número de CallFire (extensión de llamada / web / GBP) y que la conversión de llamada de Ads tenga umbral de 60 s.
  - (PMM) Explicar el hueco del 26-sep al 02-oct (0 llamadas): revisar en Ads si la campaña estuvo pausada o limitada.
  - (Cliente) Proceso de respuesta: quién contesta, en cuánto tiempo, qué pasa si está ocupado. CallFire: 89% contestadas, 2 perdidas en horario el 06 y 07-oct.
  - (Cliente) Confirmar los servicios de roadside (lockout, llanta, combustible), flatbed, motos, licencia/seguro y precio base. Eso desbloquea las keywords de lockout/llanta/combustible de G4 y los headlines [C].
  - (Cliente) GBP: ¿existe y está verificado? Acceso de administrador para PMM.
  - (PMM) /audit-landing de jumptowing.com desde un entorno con acceso.
  - (PMM) Conversiones: "Llamada desde anuncio ≥60 s" y "Llamada a número de reenvío en web ≥60 s" como primarias; formulario y clic en teléfono como secundarias. Probar con Tag Assistant. **Ojo**: hay que revisar qué cuenta hoy como conversión en 220-410-9619 (7 conversiones) y degradar a secundaria cualquier conversión que no sea una llamada calificada.
  - (PMM) Lista universal PMM + `data/negatives-nicho.txt` a nivel de cuenta.
  - (PMM) Aplicación automática de recomendaciones desactivada.
- **Riesgos**:
  - Si el cliente tarda más de 7 días en dar ticket, teléfono y servicios, la Fase 0 se extiende y la campaña vieja sigue gastando si no se pausa.
  - Si el CPL máximo sale menor a ~$20, la estrategia v1 no es rentable y hay que rehacerla (subir ticket con roadside y precio mínimo, o pausar).

## Fase 1 — Lanzamiento Search
- **Fecha estimada**: 2026-10-19 (lunes) → 2026-10-26.
- **Condición de paso**: campaña activa 7 días, anuncios aprobados y ≥1 conversión de llamada ≥60 s registrada.
- **Qué se lanza**: "Search | Towing & Roadside | 10mi | v1", $31/día, **Maximizar clics con tope de CPC $8**, lun–vie 6–18 y sáb 6–15:30.
  - 4 ad groups (G1 Near Me, G2 Brooklyn Park & NW, G3 Minneapolis, G4 Roadside), 1 RSA por grupo. Las keywords de roadside sin confirmar van en pausa.
  - Ese mismo día se pausa la campaña vieja.
- **Riesgos**:
  - Llamadas perdidas: se miden con CallFire cada semana (contestadas, perdidas en horario, en $).
  - Primera semana con poco volumen (~4–5 clics/día): no tocar la puja antes del D14.

## Fase 2 — Limpieza
- **Fechas**: D7 = 2026-10-26 · D14 = 2026-11-02 · D30 = 2026-11-18.
- **Condición de paso**:
  - Tres revisiones hechas.
  - Negativas de search terms aplicadas.
  - Keywords sin impresiones en 30 días pausadas.
  - Llamadas CallFire revisadas en cada corte: calificadas ≥60 s, costo por calificada, perdidas en horario.
  - Calidad de leads reportada por el cliente (hoja simple: llamada → ¿trabajo? sí/no).
- **Qué se revisa**:
  - Search terms: en particular otras ciudades, aseguradoras y competidores, que fueron el desperdicio de la cuenta vieja.
  - Gasto ≥$62 (2× CPL objetivo) sin conversión por keyword.
  - IS perdido por ranking: si es >40% con CPC al tope, subir el tope a $9–10.
  - Gasto real vs $825.
  - IS perdido por presupuesto.

## Fase 3 — Optimización de puja
- **Paso 1: Maximizar conversiones.** Primer chequeo el **2026-11-18** (D30).
  - **Condición**: ≥15 llamadas calificadas ≥60 s en 30 días (CallFire y conversión de Ads alineadas) y medición limpia.
  - **Supuesto**: hoy hay ~14 calificadas/mes (12 entre el 14-sep y el 08-oct) con la campaña vieja. Con phrase, tope de CPC y geo limpia, 15/mes es alcanzable en el primer mes.
- **Paso 2: tCPA.** No antes del **2026-12-18** (30 días después del paso 1).
  - **Condición**: ~30 calificadas en 30 días. tCPA = CPA observado en esos 30 días, nunca la meta.
  - **Supuesto**: $31/día ÷ costo por calificada. A $41.51 (meta F2) salen ~20/mes; a $26 (mediana Search), ~32/mes. Llegar a 30 exige estar en la mediana: es improbable con $825.
- **Si no se cumple**: se queda en la puja actual y se revisa en este orden:
  1. Contestación del cliente (CallFire).
  2. Conversión de la landing (<5% es un problema de landing).
  3. Horario (sábado tarde, domingo).
  4. Presupuesto a $1,100–1,200.

  **No forzar el cambio de puja con menos datos.**

## Fase 4 — Remarketing
- **Fecha estimada**: no antes de 2027-T1.
- **Condición de paso**: audiencia de visitantes ≥1,000 en 30 días.
- **Realidad**: con ~130 clics/mes de Ads más el tráfico orgánico (desconocido), la lista no llega a 1,000. Además, en towing la compra es urgente y no se repite: el remarketing aporta poco. Queda como opcional si GA4 muestra ≥1,000 visitantes/mes.
- **Acción si califica**: RLSA en observación sobre la campaña Search.

## Fase 5 — Performance Max
- **Fecha estimada**: **no realista con $825/mes.**
- **Condiciones que fallan** (`knowledge/estrategias/pmax-cuando-y-como.md`):
  1. **Presupuesto**: PMax necesita ≥3× CPA/día ≈ $78/día solo para PMax. Es 2.5 veces el presupuesto total.
  2. **≥30 conversiones/mes con tCPA estable 4 semanas**: depende de una Fase 3 que probablemente no se cumpla.
  3. **Assets propios**: no hay fotos ni video confirmados.
  4. **GBP**: PENDIENTE.
- **Qué haría falta**: presupuesto ≥$2,000/mes, tCPA estable, GBP con reseñas y 5+ fotos reales. Mientras tanto: Search + LSA.

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance (no hay CRM). Se reevalúa si el cliente empieza a registrar trabajos con GCLID o con número de llamada.

## Pista paralela — Landing
| Tarea | Responsable | Fecha | Tipo |
|---|---|---|---|
| /audit-landing de jumptowing.com (velocidad, llamada, horario, prueba social, tag, un solo teléfono de tracking) | PMM | 2026-10-13 | Bloqueante F0 |
| Crear /towing: H1 "Towing in Brooklyn Park & the NW Metro", botón de llamada fijo con número de reenvío, área de servicio, horario visible, formulario corto | PMM | 2026-10-15 | Bloqueante F0 |
| Crear /roadside con secciones (jump start, lockout*, tire*, fuel*) | PMM | 2026-10-16 | Bloqueante para G4 |
| /towing-brooklyn-park (landing por ciudad) | PMM | Fase 2 (≤ 2026-11-11) | Mejora |
| Reseñas de GBP visibles en las landings | PMM + Cliente | cuando exista GBP | Mejora |
| Precio base visible ("Local Tows From $XX") | Cliente decide, PMM publica | Fase 2 | Mejora (gap de competencia) |

## Pista paralela — LSA
- **Al tener acceso al GBP** (pendiente al 08-oct): confirmar que Towing está disponible en el área de Minneapolis en el panel de LSA.
- **+3 días**: iniciar la solicitud (licencia, seguro, background check del dueño/técnicos).
- **+2–4 semanas**: verificación.
- **Después**: presupuesto semanal aparte de los $825 (a definir con Jhombis), disputar leads no válidos, plan de reseñas (el ranking LSA pesa reseñas y tasa de respuesta).
- **Riesgo**: el horario no 24/7 baja la tasa de respuesta si LSA programa fuera de horario. Configurar el horario en LSA igual al real.

## Estacionalidad y ventanas
- **Invierno en Minnesota (nov–feb) es la temporada alta** de towing y roadside: baterías muertas, autos en zanjas, tormentas de nieve. Lanzar el 2026-10-19 deja la limpieza de Fase 2 (D30 = 2026-11-18) hecha justo antes del pico.
- **No retrasar el lanzamiento.** Si se pierden las primeras heladas (finales de oct–nov), se pierde la mejor ventana del año para aprender barato.
- En dic–feb, el IS perdido por presupuesto va a subir. Hay que preparar la propuesta de presupuesto de invierno ($1,100–1,200) para la revisión del D30 (2026-11-18).
- En tormentas de nieve, la demanda nocturna y de domingo se dispara. Es el mejor argumento para que el cliente evalúe cubrir esos horarios.

## Historial de cambios
- 2026-10-01: creado (D0 = 2026-10-01).
- 2026-10-08: CallFire conectado (12 calificadas, $76.50 por calificada en sep). Estrategia v2: Max. clics con tope de $8, 4 ad groups, 1 RSA. F0 reprogramada al 18-oct y lanzamiento al 19-oct por los bloqueantes abiertos.
