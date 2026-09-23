---
name: benchmark-interno
description: Busca en el MCC de PMM cuentas del mismo nicho/país y extrae CPC, CPL, tasa de conversión y estructura que funcionó. Escribe benchmark.md del cliente y actualiza knowledge/benchmarks/<nicho>.md. Usar tras /onboard o cuando se pida "cuentas similares", "qué CPL manejamos en X".
---

# /benchmark-interno — Qué nos ha funcionado en cuentas parecidas

## Requisitos
- `clients/<slug>/brief.md` (nicho, país, presupuesto).
- Acceso a Google Ads API (`docs/setup-google-ads-api.md`, `scripts/gaql.py`) **o** Windsor.ai (`google_ads` connector) **o** un CSV exportado del MCC en `knowledge/benchmarks/raw/`.

## Pasos
1. **Identificar cuentas comparables** en el MCC: mismo nicho y país (usar etiquetas de cuenta `nicho:*` y `pais:*`; si no existen, filtrar por nombre y proponer etiquetarlas). Mínimo 3; si hay menos, ampliar a nicho afín y decirlo.
2. **Métricas de 90 días por cuenta** (GAQL en `scripts/queries/benchmark.gaql`): costo, clics, impresiones, conversiones, valor, CPC, CTR, tasa conv., CPL, impression share, presupuesto.
3. **Estructura de las cuentas del cuartil superior**: número de campañas, ad groups por campaña, match types en uso, estrategia de puja, tCPA actual, extensiones activas, programación, geo (presencia vs interés).
4. **Keywords top por conversiones** agregadas (anonimizadas por cuenta).
5. **Negativas** más frecuentes en esas cuentas.
6. **Si el cliente tiene historial propio**: correr lo mismo sobre su cuenta antigua y compararlo contra el benchmark.
7. **Lectura** (playbook §3 y §9): comparar contra la mediana de 3–4 meses, no contra el mejor mes; tasas de conversión sobre <50 clics son ruido; `budget_amount` y `target_cpa` son valores vigentes, no históricos; la inversión real puede ser ~40–60% del monto del contrato.

## Salida: `clients/<slug>/benchmark.md`
```markdown
---
cliente:
slug:
nicho:
pais:
cuentas_comparables: N
periodo: 90d
actualizado:
---

# Benchmark interno — <cliente>

## Rangos esperados para este nicho/país
| Métrica | P25 | Mediana | P75 |
| CPC | | | |
| CTR | | | |
| Tasa conv. | | | |
| CPL | | | |
| Conv./mes | | | |

**CPL objetivo inicial sugerido**: mediana ±20% → $X–$Y
**Con presupuesto de $Z/mes**: ~N conversiones/mes esperadas → tCPA alcanzable en ~D días

## Lo que hacen las cuentas que mejor rinden
- Estructura, match types, puja, programación, geo

## Keywords que más convierten en el nicho (agregado)

## Negativas frecuentes del nicho

## Historial propio del cliente (si existe)
Comparación vs benchmark y diagnóstico de por qué falló o funcionó.

## Advertencias
- Pocas cuentas comparables / nicho afín usado / datos de Windsor en vez de API
```

También actualiza `knowledge/benchmarks/<nicho>-<pais>.md` con los agregados (sin nombres de clientes).

## Al terminar
Resume rangos de CPL, conversiones esperadas con el presupuesto del brief, y si el presupuesto es suficiente para salir de aprendizaje. Siguiente: `/strategy`.
