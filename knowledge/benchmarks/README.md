# Benchmarks internos PMM

Esta carpeta la llena `/benchmark-interno`. Un archivo por nicho (`towing.md`, `plumbing.md`, `electrician.md`, `abogados-co.md`, …) con métricas reales del MCC de PMM, no de reportes de la industria.

## Formato de cada archivo
```
---
nicho: towing
pais: US
cuentas: 6
periodo: últimos 90 días
actualizado: 2026-09-22
---
| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | | | |
| CTR | | | |
| Tasa conv. | | | |
| CPL | | | |
| Conv./mes | | | |
| Presupuesto/mes | | | |

## Estructura que mejor funciona
(qué campañas, ad groups, match types y pujas usan las cuentas del P75)

## Keywords top por conversiones (agregado)

## Negativas que más gasto ahorraron

## Errores comunes vistos en cuentas del P25
```

## Cómo se genera
1. `scripts/mcc_accounts.py --nicho towing` lista cuentas del MCC etiquetadas con ese nicho (usar etiquetas de cuenta en Google Ads: `nicho:towing`, `pais:US`).
2. `scripts/gaql.py` corre la consulta de métricas por cuenta.
3. El skill calcula percentiles y escribe el archivo.

Sin acceso a la API en la sesión, el skill puede leer un export CSV en `knowledge/benchmarks/raw/` o consultar Windsor.ai.

## Regla de uso
Los benchmarks se usan para fijar **expectativas iniciales** en `strategy.md` (CPL objetivo = mediana del nicho ±20%) y como referencia en /weekly-review. Nunca como promesa al cliente.
