---
cliente: Spillane's Towing & Recovery
slug: spillanes-towing
nicho: towing
pais: US
cuentas_comparables: 30 (23 maduras)
periodo: 90d (2026-07-03 → 2026-10-01)
actualizado: 2026-10-01
---

# Benchmark interno — Spillane's Towing & Recovery

Fuente: Windsor.ai (`google_ads`), 30 cuentas de towing del MCC con gasto en 90d, sin contar la del cliente. Agregados anónimos en `knowledge/benchmarks/towing-us.md`; crudo en `knowledge/benchmarks/raw/towing-us-2026-10-01.json`.
"Maduras" = ≥$700 de gasto y ≥15 conversiones en 90d (23 cuentas). Las 7 excluidas son las altas de 2026 (IDs 0040xx), que todavía están en sus primeros 1–3 meses.

## Rangos esperados para este nicho/país
| Métrica | P25 | Mediana | P75 | Spillane's (sept. 2026) |
|---|---|---|---|---|
| CPC | $4.02 | $5.05 | $6.33 | **$11.90** (el más alto del MCC towing) |
| CTR | 4.8% | 7.1% | 8.2% | 11.4% (inflado por la marca) |
| Tasa conv. | 21% | 27% | 38% | 17.7% |
| CPL | $12.45 | $16.01 | $32.07 | **$67.15** |
| Conv./mes | 17 | 36 | 54 | 14 |
| Gasto/mes | $374 | $680 | $918 | $940 |
| IS búsqueda | 22% | 27% | 32% | 40.7% (perdido: 37.6% ranking, 23.8% presupuesto) |

En las CPL bajas pesa PMax: en las cuentas del cuartil superior que la tienen, PMax reporta CPL de $6–11 contra $12–26 de su Search, y suele sumar acciones de Maps de menor calidad. **CPL de Search puro en el cuartil superior: mediana ≈ $12.90** (rango $9.70–26.25).

**CPL objetivo inicial sugerido**: mediana madura ±20% → **$12.80–19.20**. Para Spillane's lo ajusto a **$25–35 en el mes 3 y $20 en el mes 6**, por tres razones:
1. Mercado chico (Chittenden ~170k hab.), con poco volumen y cuota del 40% ya alcanzada.
2. Reputación de 3.2★, que deprime la tasa de conversión frente a pares de 4.5★+.
3. Esta cuenta es solo Search, sin PMax que baje el promedio.

**Con presupuesto de $989/mes**: si el CPC baja a ~$6 y la tasa de conversión sube a 20–25% → ~165 clics → **~33–41 conv./mes, CPL ~$24–30**. Si nada cambia (CPC $11.90, 17.7%): ~83 clics → ~15 conv./mes. **tCPA alcanzable en ~60–90 días** si la reestructuración baja el CPC; hoy (14/mes) no se llega a las ~30 conv. en 30 días.

Ojo: el CPL de este benchmark no es el CPL máximo del brief (~$21 con ticket supuesto de $200). Hay que confirmar el ticket antes de fijar un tCPA.

## Curva de aprendizaje en cuentas comparables (CPL mensual)
| Cuenta (anónima) | Mes 1 | Mes 2 | Mes 3 | Estable |
|---|---|---|---|---|
| A: alta jun-2025, ~$700/mes, Search | sin conv. (parcial) | $45 | $13.5 | $8–13 |
| B: alta jun-2025, ~$1,600/mes, Search + PMax | $22 (parcial) | $10.6 | $8.0 | $7–10 |
| C: alta jun-2026, ~$540/mes, Search | $13.5 | $10.3 | $16.7 | — |
| **Spillane's**: alta ago-2026, ~$940/mes, Search | **$67** | | | |

Spillane's arranca peor que los pares en el mes 1. El caso A muestra que un mes 2 de $45 puede bajar a $13 en el mes 3, pero A apuntaba a "towing near me", no a "roadside assistance".

## Lo que hacen las cuentas que mejor rinden
- **Estructura**: plantilla PMM "ENHPRM Radius", 1 campaña Search por cuenta con radio. 4 de las 8 del cuartil superior suman **PMax** una vez estable (aprox. 6–12 meses después del alta de Search).
- **Puja**: todas en **Maximizar conversiones sin tCPA**. Nadie pasó a tCPA, ni siquiera con 100+ conv./mes. Oportunidad a evaluar en `/strategy`.
- **Match types**: **todo el MCC towing está en BROAD**, incluido el cuartil superior. La diferencia no es el match type sino **qué keyword absorbe el gasto**: en las mejores cuentas es **"towing near me"** (cuenta B: $991 → 88 conv., CPL $11.3; cuenta A: $387 → 31 conv., CPL $12.5). En Spillane's es **"roadside assistance"** ($677 → 10 conv., CPL $67.7).
- **Geo**: radio alrededor de la base (plantilla "Radius"). Presencia vs. interés no se pudo leer por Windsor: verificar en la UI.
- **Extensiones, programación, presupuestos por campaña**: no disponibles en Windsor. Pendiente cuando esté la API.

## Keywords que más convierten en el nicho (agregado, 90d, gasto > $30)
| Keyword | Match | Gasto | Conv. | CPL | Cuentas |
|---|---|---|---|---|---|
| towing near me | BROAD | $1,748 | 126 | $13.9 | 9 |
| tow truck | BROAD | $257 | 5 | $51.3 | 1 |
| [marca propia] | EXACT | $115 | 8 | $14.4 | 1 |
| tow truck company (near me) | BROAD | $87 | 3 | $29 | 2 |
| towing company near me | BROAD | $30 | 2 | $15 | 1 |
| road service near me | BROAD | $63 | 3 | $21 | 1 |
| roadside assistance / road side assistance (near me) | BROAD | $154 | 1 | $154 | 4 |

"roadside assistance" es la peor keyword del nicho en el MCC: $154 por 1 conversión en otras 4 cuentas. Confirma el diagnóstico de Spillane's.

Nota: el reporte de keywords de Windsor cubre solo una parte del gasto (el resto va a otras keywords por debajo del filtro de $30, a PMax o a coincidencias sin keyword). Tómalo como dirección, no como cifra total.

## Negativas frecuentes del nicho
No disponibles en Windsor (las negativas no son métricas). Usar `knowledge/negativas-universales.md` + la lista de "Keywords a NO pujar" de `competitors.md`. Pendiente: exportar con GAQL (`campaign_criterion` negativo) cuando esté la API, para consolidar la lista de nicho.

## Historial propio del cliente
| | Spillane's | Mediana madura | Diagnóstico |
|---|---|---|---|
| CPC | $11.90 | $5.05 | 2.4×. Broad sobre "roadside assistance" compite con AAA/aseguradoras, y la landing sin H1 de towing baja el Quality Score |
| Conv. rate | 17.7% | 27% | Tráfico de lockout, llantas, CAA, competidores e impound (marca) que no convierte en trabajo |
| CPL | $67 | $16 | 4.2×. Es el peor de las cuentas maduras y comparable a las altas 2026 en mes 1–2 ($57–81) |
| IS | 40.7% | 27% | Ya tiene más cuota que la mediana: **el techo es de mercado, no de presupuesto**. Subir presupuesto no arregla el CPL |
| Gasto en marca | 18% | — | Spillane's ya es #1 orgánico en su marca; el gasto es redundante |

**Por qué va mal**: 1) el 72% del gasto en "roadside assistance" broad, 2) términos no comerciales o de bajo ticket sin negativas, 3) CPC inflado por relevancia baja. No es un problema de presupuesto ni de mercado: el mismo template rinde $12–16 de CPL cuando el gasto se concentra en "towing near me".

## Advertencias
- **Datos de Windsor, no de la API**: sin extensiones, negativas, programación ni tipo de ubicación (presencia/interés).
- **Las conversiones no son comparables 1:1**: varias cuentas tienen tasas de conversión de 40–50%, lo que sugiere que cuentan llamadas sin umbral de duración, o acciones de PMax/Maps. El CPL del MCC es "CPL de conversión de Ads", no de lead calificado.
- **Mezcla de mercados**: cuentas en CA, TX, FL, etc., con más volumen que Vermont. Ninguna está en Nueva Inglaterra.
- **Spillane's lleva ~6 semanas**, solo un mes con gasto. Comparar contra el mes 1–2 de los pares, no contra el estable.
