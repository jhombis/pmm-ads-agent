---
nicho: towing
pais: US
cuentas: 30 (23 maduras: ≥$700 gasto y ≥15 conv. en 90d)
periodo: últimos 90 días (2026-07-03 → 2026-10-01)
actualizado: 2026-10-01
fuente: Windsor.ai (google_ads)
---
## Cuentas maduras (n=23)
| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $4.02 | $5.05 | $6.33 |
| CTR | 4.8% | 7.1% | 8.2% |
| Tasa conv. | 21% | 27% | 38% |
| CPL | $12.45 | $16.01 | $32.07 |
| Conv./mes | 17 | 36 | 54 |
| Presupuesto/mes (gasto) | $374 | $680 | $918 |
| IS búsqueda | 22% | 27% | 32% |

## Todas las cuentas (n=30, incluye altas 2026)
| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $4.51 | $5.41 | $6.88 |
| CPL | $13.15 | $25.15 | $47.66 |
| Conv./mes | 5.8 | 21.7 | 47.2 |

- Altas de 2026 en sus primeros 1–3 meses: CPL de $57–81.
- CPL de Search puro en el cuartil superior: mediana ≈ $12.90. PMax reporta $6–11 (incluye acciones de Maps).

## Estructura que mejor funciona
- 1 campaña Search "ENHPRM Radius" con Maximizar conversiones (sin tCPA en ninguna cuenta).
- PMax agregado tras 6–12 meses de Search estable, en 4 de las 8 mejores cuentas.
- Todo el MCC towing usa BROAD. La diferencia la hace la keyword que concentra el gasto: "towing near me" (CPL ~$13) contra "roadside assistance" (CPL $67–154).

## Keywords top por conversiones (agregado)
1. towing near me (broad): 126 conv., CPL $13.9, presente en 9 cuentas
2. marca propia (exact): CPL ~$14
3. towing company near me / tow truck company: CPL $15–29
4. road service near me: CPL $21
5. tow truck (broad): CPL $51
6. roadside assistance (cualquier variante, broad): CPL $67–154. **Evitar como keyword principal**

## Negativas que más gasto ahorraron
Pendiente: requiere GAQL sobre `campaign_criterion` negativo (no disponible en Windsor).

## Errores comunes vistos en cuentas del P25
- Gasto concentrado en "roadside assistance" broad (compite con AAA, aseguradoras, CAA).
- Marca propia y competidores pagados dentro de la campaña genérica.
- Tasas de conversión <10%, que apuntan a tracking de llamadas roto o tráfico de bajo ticket (lockout, llantas).
