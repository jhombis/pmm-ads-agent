---
cliente: Murrieta Valley Funeral Home
slug: murrieta-valley-funeral-home
nicho: funeraria / cremación
pais: US
cuentas_comparables: 5
periodo: 90d (2026-07-03 → 2026-09-30)
actualizado: 2026-10-08
---

# Benchmark interno — Murrieta Valley Funeral Home

> **Sin extracción nueva**: en esta sesión no hay credenciales de la API ni Windsor autorizado. Se reutiliza la extracción del 2026-10-01 (`knowledge/benchmarks/funeraria-us.md`, 5 cuentas funerarias del MCC, 90 días, vía Windsor) y las cifras por cuenta que quedaron en los archivos de Colton y Hemet. **La cuenta del cliente (769-956-1619) es una de las 5**: los percentiles la incluyen, así que su posición relativa está ligeramente suavizada. Hay que repetir con `scripts/queries/benchmark.gaql` cuando haya acceso; las cuentas siguen sin etiquetas `nicho:funeral` / `pais:US` en el MCC.

## Rangos esperados para este nicho/país (Search, 90 d)
| Métrica | P25 | Mediana | P75 | **Murrieta (769-956-1619)** |
|---|---|---|---|---|
| CPC | $5.94 | $8.64 | $9.41 | **$9.96** (sobre P75) |
| CTR | 4.3% | 8.1% | 9.2% | sin dato |
| Tasa conv. | 8.3% | 9.7% | 11.9% | **~5.8%** (implícita: 21 conv / ~341 clics) |
| CPL | $58 | $73 | $133 | **$162–182** (sobre P75) |
| Conv./mes | 7 | 10 | 15 | **7** (P25) |
| Gasto Search/mes | $889 | $1,029 | $1,145 | $1,155–1,244 |

CPL de la cuenta completa (Search + PMax): P25 $42 · mediana $56 · P75 $108. La PMax de Murrieta reporta CPA $57, sin auditar qué conversiones cuenta.

**CPL objetivo inicial sugerido**: mediana ±20% → **$58–$88** (punto medio $73).
**Con $1,200/mes**: a $73 son ~16 conv/mes; a $133 (P75) son 9; al CPL actual, 7. Para **Max. conversiones** (estándar #6: 15+/mes) hace falta llegar a la mediana; para **tCPA** (~30 en 30 días) haría falta CPA ≤ $40, por debajo del P25: **no alcanzable con este presupuesto**. Hoy la cuenta usa Max. conversiones con 7 conv/mes, por debajo del umbral.

## Lo que hacen las cuentas que mejor rinden
- **Sunflower Riverside (CPL ~$50) y Swan (~$58)**: 1 campaña Search con 1 ad group genérico, keywords amplias con Maximizar conversiones (sin tCPA), tracking completo (Form Fill + Calls from Ads + Website Calls); su mejor keyword es "cremation cost" (amplia): 23 conv, $44 CPA en 90 d. PMax madura (29–49 conv/90 d) lanzada tras 6–12 meses de Search. IS perdido por presupuesto 26–75%.
- **Hemet (~$113–133)**: 3 ad groups (General / Cremation / Burial), frase + amplia, Max conv, CPC alto ($12–13) pero 9.7% de conversión.
- **Común**: geo por presencia; marca convirtiendo barato dentro de cada cuenta ("murrieta valley mortuary", "swan funeral home", "sunflower cremation"); Display responsive con 0 conversiones en todas.
- **Lectura para Murrieta**: la cuenta ya tiene la puja y la estructura "correctas" del nicho (Max conv) y aun así rinde en el P25. Lo que la separa de las mejores no es la puja: es **la tasa de conversión (5.8% vs 9.7%)**, que apunta a landing (sin página de cremación, sin precio, formulario sin gracias: audit-site.md) y a medición incompleta, más un CPC por encima del P75 que sugiere términos genéricos caros o marca pagada dentro de la genérica.

## Keywords que más convierten en el nicho (agregado, 90 d)
- **Marca propia**: "<marca> funeral home", "<marca> mortuary", "<marca> cremation" (la mayor parte de las conversiones baratas).
- **Precio**: "cremation cost" (amplia, con Max conv), "low cost cremation <condado>", "cheapest mortuary near me", "average cost of cremation in california". **Ojo para Murrieta**: estas convierten en cuentas con cremación directa a $1,095–1,175; con un GPL de ≈ $1,578+ el clic de precio es más difícil de cerrar (competitors.md).
- **Ciudad + servicio**: "mortuary <ciudad>", "funeral homes in <ciudad> ca", "<ciudad> cremation", "direct cremation in <ciudad>".
- **Near me**: "funeral homes near me", "mortuaries near me", "cremations near me", "cremation services near me".
- **Español**: "funeraria cerca de mi", "cuanto cuesta cremar una persona" (convirtió en Hemet).
- **Pre-need**: "pre need funeral plans" (convirtió en Hemet).

## Negativas frecuentes del nicho
Obituarios / "recent deaths" / "funerals today", productos (casket, headstone, urn, plots, costco), mascotas (también en plural), "average cost" / ayudas / "benefits", competidores online (Meadow, After, Neptune, Tulip, Trident, Smart). Lista de Colton (542 términos) en `clients/colton-sunflower/data/negatives-nicho.txt` como base. **No** usar "how" ni "cheapest" en amplia en cuentas baratas; en Murrieta, "cheap/cheapest/$499/low cost" sí se negativizan por posición de precio (competitors.md).

## Historial propio del cliente
| | Murrieta (abr–sep 2026) | Mediana nicho |
|---|---|---|
| Puja | Max conversiones | Max conversiones |
| Match | sin dato (requiere API) | mixto |
| Conversiones medidas | sin dato; patrón del nicho: Form Fill + llamadas | formulario + llamadas |
| Tasa conv. | ~5.8% | 9.7% |
| CPC | $9.96 | $8.64 |
| CPL | $162–182 | $73 |
| Conv./mes | 6.8–7 | 10 |

Diagnóstico provisional: **no es la puja, es la landing y la medición.** Con la puja de las mejores cuentas, Murrieta convierte a la mitad de la tasa del nicho y paga el CPC más alto. Las causas visibles (audit-site.md): tráfico de cremación aterrizando en una home sin H1 ni precio, formulario sin página de gracias (posibles Form Fill no contados → CPL inflado), dos teléfonos sin reenvío, y un precio de cremación directa que no compite con los $995 de la SERP. Orden: medición → negativas de precio y competidores → landings por servicio → marca aparte → recién entonces revisar puja.

## Advertencias
- Extracción reutilizada del 2026-10-01, no nueva; datos de Windsor, no de la API; sin search terms ni lista de conversiones de la cuenta.
- 5 cuentas, una de Tucson (Swan) y una con poco gasto (Inland, $170–307/mes); la del cliente está dentro del benchmark.
- La tasa de conversión de Murrieta (5.8%) es implícita: 21 conv / ($3,399 ÷ $9.96 CPC); clics reales sin confirmar.
- PMax a $57 de CPA en Murrieta sin auditar (posible inflación por acciones locales o llamadas cortas). No usar como referencia hasta ver la lista de conversiones.
- Inland Memorial Murrieta (cuenta hermana, pausada) y Colton Sunflower (mismo grupo) pueden solaparse en la subasta.
- Propuesta pendiente: etiquetar las 5 cuentas con `nicho:funeral` y `pais:US` en el MCC.
