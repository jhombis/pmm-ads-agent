---
cliente: Jump Towing LLC
slug: jump-towing
D0: 2026-10-01
actualizado: 2026-10-01
fase_actual: 0
plan_es: https://claude.ai/artifact/G41fXXn8ejrpzJN7JykQu5
plan_en: https://claude.ai/artifact/U2e1QfnLLPYpek6vs2bGpn
---

# Roadmap — Jump Towing LLC

> Las fechas son proyección; la condición de paso es la que manda. `/weekly-review` avanza de fase solo cuando la condición se cumple.
> Inputs: brief.md, strategy.md v1 y benchmark.md. **audit-site.md no existe** (jumptowing.com bloqueado por el proxy), así que la Fase 0 se estima con el supuesto de que la landing necesita ajustes que hace PMM.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Fundación | 2026-10-01 → 2026-10-11 | 🔄 en curso (hay bloqueantes del cliente) |
| 1 — Lanzamiento Search | 2026-10-12 → 2026-10-19 | ⏳ |
| 2 — Limpieza D7 · D14 · D30 | 2026-10-19 · 2026-10-26 · 2026-11-11 | ⏳ |
| 3 — tCPA | 2026-11-25 (primer chequeo 2026-11-11) | ⏳, probablemente ⛔ con $825 (ver supuesto) |
| 4 — Remarketing | no antes de 2027-T1 | ⏳, probablemente no califica (tráfico) |
| 5 — PMax | no realista con $825/mes | ⛔ por presupuesto |
| 6 — Conversiones offline | fuera de alcance | — |
| Pista Landing | 2026-10-01 → 2026-10-09 | 🔄 |
| Pista LSA | 2026-10-02 → 2026-10-30 | ⏳ (depende del GBP) |

## Fase 0 — Fundación
- **Fecha estimada**: 2026-10-01 → 2026-10-11 (D0+10). Base de 3 días por ajustes de landing que hace PMM, más ~7 días de espera por los datos del cliente (ticket, teléfono, GBP, servicios).
- **Condición de paso**: todos los ítems bloqueantes de Fase 0 en `checklist.md` en ✅.
- **Tareas**:
  - (Jhombis, **hoy**) Decidir qué se hace con la campaña activa de 220-410-9619. Gasta ~$190/semana a CPL $65.57 con broad, Maximizar clics, ad group en español y geo dudosa. Recomendación: **pausarla** hasta el lanzamiento de v1. Si no se pausa, como mínimo: borrar el ad group en español, aplicar negativas universales + nicho, verificar la geo (Presencia, 10 mi) y pasar las keywords broad a phrase.
  - (Cliente) Ticket promedio, margen y tasa de cierre → PMM calcula el CPL máximo y valida el objetivo de $21–31.
  - (Cliente) Teléfono principal + aprobación del número de reenvío de Google.
  - (Cliente) Proceso de respuesta: quién contesta, en cuánto tiempo, qué pasa si está ocupado (buzón o devolución de llamada en <5 min).
  - (Cliente) Confirmar los servicios de roadside (lockout, llanta, combustible), flatbed, motos, licencia/seguro y precio base. Eso desbloquea R2, R3 y los headlines [C].
  - (Cliente) GBP: ¿existe y está verificado? Acceso de administrador para PMM.
  - (PMM) /audit-landing de jumptowing.com desde un entorno con acceso.
  - (PMM) Conversiones: "Llamada desde anuncio ≥60 s" y "Llamada a número de reenvío en web ≥60 s" como primarias; formulario y clic en teléfono como secundarias. Probar con Tag Assistant. **Ojo**: hay que revisar qué cuenta hoy como conversión en 220-410-9619 (7 conversiones) y degradar a secundaria cualquier conversión que no sea una llamada calificada.
  - (PMM) Lista universal PMM + `data/negatives-nicho.txt` a nivel de cuenta.
  - (PMM) Aplicación automática de recomendaciones desactivada.
- **Riesgos**:
  - Si el cliente tarda más de 7 días en dar ticket, teléfono y servicios, la Fase 0 se extiende y la campaña vieja sigue gastando si no se pausa.
  - Si el CPL máximo sale menor a ~$20, la estrategia v1 no es rentable y hay que rehacerla (subir ticket con roadside y precio mínimo, o pausar).

## Fase 1 — Lanzamiento Search
- **Fecha estimada**: 2026-10-12 (lunes) → 2026-10-19.
- **Condición de paso**: campaña activa 7 días, anuncios aprobados y ≥1 conversión de llamada ≥60 s registrada.
- **Qué se lanza**: "Search | Towing & Roadside | 10mi | v1", $31/día, Maximizar conversiones, lun–vie 6–18 y sáb 6–15:30.
  - Ad groups T1–T4 + R1. R2 y R3 solo si el cliente confirmó el servicio y la landing existe.
  - Ese mismo día se pausa la campaña vieja.
- **Riesgos**:
  - Proceso de respuesta del cliente sin definir: un CPL bueno con llamadas perdidas no da dinero. Pedir al cliente un registro de llamadas perdidas la semana 1.
  - Primera semana con poco volumen (~4–5 clics/día): no tocar la puja antes del D14.

## Fase 2 — Limpieza
- **Fechas**: D7 = 2026-10-19 · D14 = 2026-10-26 · D30 = 2026-11-11.
- **Condición de paso**:
  - Tres revisiones hechas.
  - Negativas de search terms aplicadas.
  - Keywords sin impresiones en 30 días pausadas.
  - RSA peor por grupo reemplazado.
  - Calidad de leads reportada por el cliente (hoja simple: llamada → ¿trabajo? sí/no).
- **Qué se revisa**:
  - Search terms: en particular otras ciudades, aseguradoras y competidores, que fueron el desperdicio de la cuenta vieja.
  - Gasto ≥$62 (2× CPL objetivo) sin conversión por ad group.
  - Gasto real vs $825.
  - IS perdido por presupuesto.

## Fase 3 — Optimización de puja (tCPA)
- **Fecha estimada**: **2026-11-25**. Primer chequeo el 2026-11-11 (D30).
- **Supuesto del cálculo**:
  - $31/día ÷ CPL benchmark Search $25.98 = 1.19 conversiones por día activo. Con ~26.5 días activos/mes salen ≈ 1.05 por día calendario, así que 30 conversiones toman ≈ 29 días.
  - +2 semanas porque el presupuesto diario ($31) es menor que 3× CPL ($78).
  - Ventana de evaluación: 2026-10-26 → 2026-11-25.
- **Condición de paso**: ≥30 conversiones de llamada ≥60 s en 30 días, con el tracking verificado.
- **Acción**: tCPA = CPL real de 30 días (no el deseado). Reajustar el presupuesto según la capacidad del cliente.
- **Si no se cumple**: es lo más probable. A CPL $35 salen ~23/mes y al CPL de la cuenta vieja ($65) ~13/mes. Entonces se queda en Maximizar conversiones, que funciona bien sin tCPA. Revisar en este orden:
  1. Conversión de la landing (<5% es un problema de landing).
  2. Ampliar horario a domingo/noches si el cliente puede contestar.
  3. Presupuesto a $1,100–1,200.

  **No forzar tCPA con menos datos.**

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
| /audit-landing de jumptowing.com (velocidad, llamada, horario, prueba social, tag) | PMM | 2026-10-05 | Bloqueante F0 |
| Crear /towing: H1 "Towing in Brooklyn Park & the NW Metro", botón de llamada fijo con número de reenvío, área de servicio, horario visible, formulario corto | PMM | 2026-10-09 | Bloqueante F0 |
| Crear /jump-start | PMM | 2026-10-09 | Bloqueante para R1 |
| Crear /car-lockout y /flat-tire-fuel | PMM | tras confirmar servicio | Bloqueante para R2/R3 |
| /towing-brooklyn-park (landing por ciudad) | PMM | Fase 2 (≤ 2026-11-11) | Mejora |
| Reseñas de GBP visibles en las landings | PMM + Cliente | cuando exista GBP | Mejora |
| Precio base visible ("Local Tows From $XX") | Cliente decide, PMM publica | Fase 2 | Mejora (gap de competencia) |

## Pista paralela — LSA
- **2026-10-02**: confirmar que Towing está disponible en el área de Minneapolis en el panel de LSA. Requiere GBP.
- **2026-10-05**: iniciar la solicitud (licencia, seguro, background check del dueño/técnicos).
- **2026-10-16 → 2026-10-30**: verificación (2–4 semanas).
- **Después**: presupuesto semanal aparte de los $825 (a definir con Jhombis), disputar leads no válidos, plan de reseñas (el ranking LSA pesa reseñas y tasa de respuesta).
- **Riesgo**: el horario no 24/7 baja la tasa de respuesta si LSA programa fuera de horario. Configurar el horario en LSA igual al real.

## Estacionalidad y ventanas
- **Invierno en Minnesota (nov–feb) es la temporada alta** de towing y roadside: baterías muertas, autos en zanjas, tormentas de nieve. Lanzar el 2026-10-12 deja la limpieza de Fase 2 (D30 = 2026-11-11) hecha justo antes del pico.
- **No retrasar el lanzamiento.** Si se pierden las primeras heladas (finales de oct–nov), se pierde la mejor ventana del año para aprender barato.
- En dic–feb, el IS perdido por presupuesto va a subir. Hay que preparar la propuesta de presupuesto de invierno ($1,100–1,200) para la revisión del 2026-11-25.
- En tormentas de nieve, la demanda nocturna y de domingo se dispara. Es el mejor argumento para que el cliente evalúe cubrir esos horarios.

## Historial de cambios
- 2026-10-01: creado (D0 = 2026-10-01).
