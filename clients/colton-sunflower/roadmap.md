---
cliente: Colton Sunflower Burial and Cremation
slug: colton-sunflower
D0: 2026-10-01
actualizado: 2026-10-06
fase_actual: 0
plan_es: https://claude.ai/artifact/74WA8FWCjHGkiYPWh8h8fy
plan_en: https://claude.ai/artifact/3gJMiMNSMNamGjVe2wZsTv
---

# Roadmap — Colton Sunflower Burial and Cremation

> Esta cuenta se **heredó activa** (desde 2026-08-03, Max clics con tope de $7, CPA $466 en 28d). "Fase 0" aquí significa **rescate**: arreglar el tracking, la puja y la estructura sobre la campaña existente. La campaña **sigue corriendo** durante la Fase 0 porque las negativas ya contienen el desperdicio. Pausarla perdería historial y llamadas.
> Presupuesto $49/día contra un CPL benchmark de $100: el presupuesto es **menos de 3× CPL/día**, así que el aprendizaje será lento, la fase 3 se alarga +2 semanas y **PMax probablemente nunca califica** con este presupuesto.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Rescate / fundación | 2026-10-01 → 2026-10-15 | 🔄 en curso |
| 1 — Relanzamiento con nueva estructura + tope de CPC | 2026-10-15 → 2026-10-22 | ⏳ |
| 2 — Limpieza D7 · D14 · D30 | 2026-10-22 · 2026-10-29 · 2026-11-14 | ⏳ |
| 3 — tCPA | No antes de ~2026-12-13; **improbable con $49/día** | ⏳ |
| 4 — Remarketing (RLSA observación) | Evaluar 2026-11-14 | ⏳ |
| 5 — Performance Max | No realista con el presupuesto actual | ⛔ |
| 6 — Conversiones offline | Fuera de alcance | — |
| Pista Landing | 2026-10-01 → 2026-10-15 (bloqueantes) · F2–3 (mejoras) | 🔄 auditada 12/22 |
| Pista LSA | No aplica (verificar) | — |

## Fase 0 — Rescate / fundación
- **Fecha estimada**: 2026-10-01 → 2026-10-15. Son D0+14 porque varias tareas dependen del cliente (+7–14 días).
- **Condición de paso**: todos los ítems marcados ⚠️ bloqueante en `checklist.md` ✅.
- **Tareas**:
  - (PMM) Crear la conversión **Form Fill** y probarla con Tag Assistant ⚠️
  - (PMM) Verificar las conversiones de llamada: "Calls from Ads" con duración mínima de 60s y "Website Calls" ⚠️
  - (PMM) Confirmar que la red sea solo Búsqueda (sin socios ni Display) y que la autoaplicación de recomendaciones esté OFF ⚠️
  - (Claude, tras OK) Corregir las negativas que bloquean demanda: quitar `how`, `Fontana` y `online` (amplias) ⚠️
  - (Claude, tras OK) Reestructurar a 5 ad groups: amplia → frase/exacta, pausar las 0 impresiones y la duplicada ⚠️
  - (Claude, tras OK) 1 RSA por grupo (máx. 2) con el copy de `data/ads-search.md`; reemplazar el RSA 819740188547 ⚠️
  - (Claude, tras OK) Aplicar las 5 negativas de `data/2026-10-01-negatives.txt`
  - (Jhombis/Cliente) Confirmar en /onboard: ticket, margen, capacidad, idioma ES, mascotas, horario/24-7, radio real ⚠️ (radio y horario)
  - (Jhombis) Aclarar la relación con Inland Memorial / Sunflower Riverside y definir radios sin solape ⚠️
  - (Jhombis) Confirmar si los $2,500/mes son netos o incluyen fee
  - (Jhombis) Acordar quién más edita la cuenta
  - (PMM) Vincular el GBP (activo de ubicación)
- **Riesgos**:
  - Que el cliente tarde en confirmar los datos. Mitigación: lanzar la estructura sin los claims `[C]` y sumarlos después.
  - Que alguien más siga editando la cuenta.

## Fase 1 — Relanzamiento (estructura nueva + Max clics con tope de CPC)
- **Fecha estimada**: 2026-10-15 → 2026-10-22
- **Condición de paso**: estructura de 5 grupos activa 7 días, anuncios aprobados, estructura v2.0 sin amplia, tope de CPC $8 activo y **≥1 conversión de Form Fill o llamada registrada después del cambio**.
- **Qué se lanza**: la campaña actual, reestructurada según `strategy.md`, con $49/día (más marca $5/día si se confirma). Puja: Max clics con tope de CPC $8 (playbook §5: <15 conv/mes). Pasa a Max conversiones cuando haya 15+ conv/mes estables con Form Fill medido.
- **Riesgos**: un tope de $8 puede dejar fuera los términos locales más caros ("cremation san bernardino" ~$11.75). En D7 se mira el IS perdido por ranking en los grupos de cremación y se ajusta el tope.

## Fase 2 — Limpieza
- **Fechas**: D7 **2026-10-22** · D14 **2026-10-29** · D30 **2026-11-14** (contadas desde el relanzamiento).
- **Condición de paso**: las 3 revisiones hechas, negativas aplicadas, keywords con 0 impresiones en 30d pausadas, peor RSA por grupo reemplazado y **CPA 30d ≤ $150 con ≥10 conv**. Esta última es la condición de `strategy.md` para pasar a F2-Optimización.
- **Qué se revisa**: search terms (sobre todo grupos de precio y "near me"), gasto sin conversión > $200 por keyword, peor RSA por grupo, IS perdido por ranking (hoy 55%) y calidad de leads reportada por el cliente.

## Fase 3 — Optimización de puja (tCPA)
- **Fecha estimada**: **no antes de ~2026-12-13**.
  - Cálculo (benchmark 90d, CPL mediana $73): $49/día ÷ $73 = 0.67 conv/día, es decir ~45 días hasta 30 conv; +2 semanas porque el presupuesto es menor a 3× CPL/día (3 × $73 = $219). Contado desde el 2026-10-15.
  - Ojo: tCPA pide **30 conv dentro de una ventana de 30 días**. Con $1,490/mes eso exige CPA ≤ $50 (P25 del nicho: $58). Con $2,500/mes exigiría CPA ≤ $83, que sí es alcanzable.
- **Condición de paso**: ≥30 conversiones en ventana de 30 días con tracking verificado.
- **Acción**: tCPA = CPA real observado; reajustar presupuesto.
- **Si no se cumple**: es lo esperado con este presupuesto. Se queda en **Maximizar conversiones** (si ya hay 15+ conv/mes) o en Max clics con tope. **No forzar tCPA con menos datos.** Si la conversión de la landing es <5%, priorizar la pista Landing.

## Fase 4 — Remarketing
- **Fecha estimada**: evaluar el 2026-11-14 (D30).
- **Condición de paso**: audiencia ≥1000 usuarios en 30d. Con ~230 clics/mes de Ads no llega solo con pago; depende del tráfico orgánico. Requiere GA4 vinculado.
- **Acción**: RLSA en **observación** sobre Search. Display remarketing no se hace (en Inland Memorial: 0 conv).
- **Nota**: una funeraria es una compra urgente y única, así que el valor esperado es bajo. Es opcional.

## Fase 5 — Performance Max
- **Estado**: ⛔ **no califica y probablemente no califique** con este presupuesto.
- **Condiciones que fallan** (`pmax-cuando-y-como.md`):
  1. Hoy hay 4 conv/mes y se piden ≥30.
  2. No hay tCPA activo ni 4 semanas de Search estable.
  3. PMax pide ≥3× CPA/día (≥$300); el presupuesto total es $49.
  4. No hay assets propios verificados.
  5. La tasa de conversión de la landing es desconocida.
- **Qué haría falta**: presupuesto ≥ $3,000/mes netos **y** CPA ≤ $100 sostenido. Mientras tanto: Search + (opcional) RLSA.

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance (sin CRM). Interim: pedir al cliente que marque mensualmente cuáles llamadas fueron servicios contratados.

## Pista paralela — Landing
- ✅ 2026-10-01 `/audit-landing`: 12/22, **requiere ajustes**. El sitio ya tiene /pricing/ con precios ($1,175 / $1,995) y /burial/.
- ⚠️ Fase 0 (PMM, ~4 h): página /thank-you/ + redirect del formulario (Form Fill medible), formulario arriba en /, /cremation/ y /pricing/, Email y Mensaje opcionales.
- Fase 2–3: reseñas de Google en el sitio, H1, botón de llamada sticky en móvil, caché de página (TTFB 1.3–3.5 s). Ya hay reCAPTCHA (sirve para PMax si algún día califica).

## Pista paralela — LSA
- No aplica: las funerarias no figuran en las categorías de LSA que conocemos. (PMM) Verificar en la UI de LSA antes de descartarlo del todo.

## Estacionalidad y ventanas
- La mortalidad en EE. UU. sube en invierno (dic–feb), así que la demanda funeraria también. **Conviene salir de la Fase 1–2 antes de diciembre** para que la estructura nueva y la medición ya estén limpias cuando suba el volumen. Es una razón más para no alargar la Fase 0.

## Historial de cambios
- 2026-10-06: /diagnose — estructura v2.0 (salir de la amplia, 92% del gasto; 5 grupos incl. Brand). Corrección: la campaña ya tenía tope de $7.
- 2026-10-01: /informe — plan ES + EN con el estilo PMM (plan-es.html / plan-en.html); reemplaza a plan.html, cuya URL pasa a ser la versión ES.
- 2026-10-01: ajustado a los estándares nuevos de CLAUDE.md (puja con tope de CPC hasta 15+ conv/mes; 1 RSA por grupo con <$1,500/mes).
- 2026-10-01: CPL benchmark ajustado a $73 (benchmark.md); fecha de tCPA recalculada.
- 2026-10-01: pista Landing actualizada con audit-site.md.
- 2026-10-01: creado. D0 = 2026-10-01 (cuenta heredada activa desde 2026-08-03). Ya hechos antes del roadmap: 76 negativas y 3 keywords del competidor pausadas.
