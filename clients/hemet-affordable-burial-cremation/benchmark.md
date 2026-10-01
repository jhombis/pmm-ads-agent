---
cliente: Hemet Affordable Burial and Cremation
slug: hemet-affordable-burial-cremation
nicho: funeraria / cremación
pais: US
cuentas_comparables: 5
periodo: 90d (2026-07-03 → 2026-09-30)
actualizado: 2026-10-01
---

# Benchmark interno — Hemet Affordable Burial and Cremation

Fuente: Windsor.ai (`google_ads`) sobre el MCC de PMM. Las cuentas comparables se identificaron por nombre porque no hay etiquetas `nicho:`/`pais:`:
- Swan Burial & Cremation (162-865-0456)
- Sunflower Cremation Services (672-338-0346)
- Murrieta Valley Funeral Home (769-956-1619)
- Inland Memorial Inc. (934-241-5137): cuenta anterior del mismo dueño, pausada en ago 2026
- Colton Sunflower Burial and Cremation (151-776-2744): activa desde 2026-08-03

Todas son funerarias o crematorios del Inland Empire / sur de California. El cliente se excluye de los percentiles y se compara aparte.

## Rangos esperados para este nicho/país — campañas Search
| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $5.94 | $5.94 | $8.64 |
| CTR | 4.3% | 7.8% | 9.2% |
| Tasa conv. | 5.8% | 8.3% | 11.9% |
| CPL | $58 | **$73** | $164 |
| Conv./mes | 3.5 | 7.0 | 15.3 |
| Gasto Search/mes | $889 | $1,029 | $1,145 |

Por cuenta (Search, 90 días):
| Cuenta | CPC | CTR | Conv. | CPL | Conv./mes | Gasto/mes |
|---|---|---|---|---|---|---|
| Sunflower | $5.94 | 4.3% | 11.9% | **$50** | 20.6 | $1,029 |
| Swan | $4.79 | 11.0% | 8.3% | **$58** | 15.3 | $889 |
| Inland Memorial (parcial) | $8.64 | 3.6% | 11.9% | $73 | 3.5 | $255 |
| Murrieta Valley | $9.41 | 9.2% | 5.8% | $164 | 7.0 | $1,145 |
| Colton Sunflower (nueva) | $5.94 | 7.8% | 1.5% | $394 | 3.5 | $1,378 |
| **Hemet Affordable (cliente)** | **$12.98** | 8.1% | 9.7% | **$133** | 10.0 | $1,332 |

Referencia PMax (4 cuentas): CPL P25 $25 · mediana **$41** · P75 $59; CPC mediana $3.73. **No es comparable con Search** (ver Advertencias).

**CPL objetivo inicial sugerido**: mediana ±20% → **$58–$88**. Para la Fase 1 de la reestructura se mantiene **≤ $100** como paso intermedio desde los $133 actuales.
**Con $1,500/mes**: a CPL $73 → **~20 conv/mes**; al CPL actual del cliente ($133) → ~11. Para 30 conv/30 días (tCPA) harían falta **~$2,200/mes** a CPL mediano. El presupuesto **no alcanza para salir rápido del aprendizaje**: la regla pide 3× CPL/día = $219/día y hay $49. Se trabaja con Maximizar conversiones sin tCPA.

## Lo que hacen las cuentas que mejor rinden (Sunflower, Swan)
- **Estructura**: 1 campaña Search ("ZETA/ENHPRM Radius") + 1 PMax. Una sola campaña Search consolidada, igual que la propuesta de `strategy.md`.
- **Puja**: Maximizar conversiones en las dos campañas, sin tCPA.
- **Geo**: ⚠️ **"Presencia o interés"**, contra el estándar #1 de PMM. Hemet y Murrieta usan presencia. Corregirlo en esas cuentas es tarea aparte, fuera de este cliente.
- **Match types**: amplia en su keyword principal.
- **Impression share (30 días)**: Swan pierde **84% por presupuesto**, así que su CPL bajo es en parte de "comer solo lo más barato". Sunflower pierde 58% por ranking. El cliente tiene **41% de IS**, con 32% perdido por presupuesto y 28% por ranking.
- **Landing**: el CPL bajo coincide con cuentas cuyo término principal es de precio ("cremation cost") y presumiblemente con precio visible en la landing. No se auditaron sus sitios.

## Keywords que más convierten en el nicho (agregado, Search, 90 días)
| Keyword (match) | Gasto | Clics | Conv. | CPL | Cuentas |
|---|---|---|---|---|---|
| **cremation cost** (amplia) | $2,191 | 361 | **86.3** | **$25** | 2 |
| crematorium (amplia) | $395 | 42 | 15 | $26 | 1 |
| funeral homes (amplia) | $72 | 8 | 7 | $10 | 3 |
| funeral homes near me (amplia) | $80 | 6 | 4 | $20 | 1 |
| cremation (amplia) | $94 | 5 | 4 | $24 | 1 |
| cremation places near me (amplia) | $27 | 5 | 2 | $13 | 1 |
| funeral home near me (amplia) | $28 | 6 | 1 | $28 | 1 |
| veteran funeral services (amplia) | $2 | 1 | 1 | $2 | 1 |
| simple cremation cost (amplia) | $19 | 3 | 1 | $19 | 1 |

**Hallazgo que cambia `strategy.md`**: "cremation cost" es el motor de conversiones del nicho en el MCC (86 conv a $25). En la cuenta del cliente gastó $384 con 2 conv (CPA $192) apuntando a /cremation, **una página sin precios**. Hipótesis: el término funciona si la landing muestra el precio. → En la Fase 1 se agrega **"cremation cost" (frase) al grupo Affordable con landing /pricing/**, en vez de descartarlo. Si a los 30 días da CPA > $150, se pausa.

## Negativas frecuentes del nicho
No disponible vía Windsor: las listas compartidas no se exponen. La base de nicho del cliente está en `data/negatives-nicho.txt`, construida desde sus search terms; se propone como base para `knowledge/benchmarks/funeraria-us.md`.

## Historial propio del cliente
**Cuenta actual (751-429-2721)**, Search, 90 días: CPC **$12.98 (2.2× la mediana)**, conversión 9.7% (por encima de la mediana), CPL $133 (entre la mediana y P75).
Diagnóstico: el problema **no es la conversión, es el costo del clic**. Las causas probables:
1. ~51% del gasto en amplia sobre términos genéricos caros.
2. ~18% de fuga a competidores e irrelevantes.
3. La marca pagada al CPC genérico.
4. 28% de IS perdido por ranking (calidad del anuncio y de la landing: sin precio en /cremation y /burial, sin tag).

Bajar el CPC a ~$7 con la misma conversión llevaría el CPL a ~$72, la mediana.

**Cuenta anterior (Inland Memorial, 934-241-5137)**: su PMax tuvo 40 conv en 90 días (CPL $22), 38 de ellas "Calls from ads". Sin registros de duración ni de calidad, no sirve como prueba de que PMax funcione para este negocio.

## Advertencias
- **5 cuentas comparables**, con 2 que distorsionan: Inland (pausada a mitad del período) y Colton (2 meses de vida). Con solo Sunflower, Swan y Murrieta, la mediana de CPL sería $58.
- **Conversiones no homogéneas**: en todas las cuentas domina "Calls from ads", sin evidencia de duración mínima uniforme. En PMax, "Calls from ads" puede incluir llamadas desde el activo de ubicación (Maps), por eso su CPL parece tan bajo. **PMax no es comparable con Search** mientras no se verifique la duración mínima por cuenta.
- Datos de Windsor, no de la API directa (sin `scripts/gaql.py` en esta sesión).
- La métrica es CPL, no costo por caso: ninguna cuenta del nicho importa conversiones offline.
- Posible relación comercial: el cliente crema en "Sunflower Crematory" y hay dos cuentas Sunflower en el benchmark. Si son del mismo grupo, pueden competir en la subasta de Hemet (Sunflower usa "presencia o interés").
