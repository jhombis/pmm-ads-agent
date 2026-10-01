---
nicho: towing
pais: US
cuentas: 27
periodo: últimos 90 días (~2026-07-01 a 2026-09-28)
actualizado: 2026-09-29
fuente: Windsor.ai (google_ads); 32 cuentas del MCC identificadas por nombre, 27 con >= $100 de gasto
---
| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $4,31 | $5,12 | $6,78 |
| CTR | 5,1% | 6,8% | 8,3% |
| Tasa conv. | 17,9% | 25,0% | 37,7% |
| CPL | $12,71 | $17,88 | $42,48 |
| Conv./mes | 6,9 | 27,3 | 49,7 |
| Presupuesto/mes (gasto real) | $256 | $446 | $787 |
| Presupuesto/mes (nominal en nombre de cuenta) | $1.000 | $1.500 | $1.900 |

Percentiles a nivel cuenta (Search + PMax). El gasto real es de mediana el 39% del monto nominal del nombre de la cuenta (el nominal incluye fee).

## Solo Search (n=26)
| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $5,14 | $7,04 | $8,98 |
| CTR | 6,8% | 8,0% | 9,2% |
| Tasa conv. | 19,5% | 26,3% | 38,5% |
| CPL | $13,45 | $26,15 | $46,72 |
| Conv./mes | 6,1 | 18,0 | 30,1 |
| Impression share | 19% | 26% | 31% |

Agregado: Search $33.351 → 1.735 conv (CPL $19,23, CPC $6,30, CVR 32,8%). PMax $18.060 → 1.366 conv (CPL $13,22) en 14 cuentas.

## Cohorte nueva vs madura (Search)
| Cohorte | n | CPL P25 | CPL mediana | CPL P75 | CPC med. | CVR med. |
|---|---|---|---|---|---|---|
| Search lanzada hace < 6 meses | 10 | $31,61 | $51,28 | $63,99 | $7,56 | 18,8% |
| Search con >= 6 meses | 16 | $12,80 | $14,57 | $27,87 | $5,96 | 36,7% |

Una cuenta nueva de towing arranca con CPL 3–4x el de una madura y la brecha es de tasa de conversión, no de CPC. Expectativa: meses 1–2 en $30–50, meses 3–6 convergiendo a $15–28. Usar la cohorte nueva como comparación justa en los primeros 60 días.

## Estructura que mejor funciona
Cuartil superior (7–9 cuentas, CPL $8–13):
- 1 campaña Search de radio con **1 ad group y 6–16 keywords**; 2–3 términos hacen el 80% del volumen. Ninguna usa SKAG. Una cuenta bilingüe separa ad group EN / ES.
- **Puja: Maximizar conversiones en el 100%**; 4 cuentas con tCPA $12–15, todas en la mitad buena. Las 3 cuentas en Maximizar clics están en el fondo (CPL $70–83).
- **Match type**: el MCC está mayoritariamente en amplia (26 cuentas: $29.912 → 1.539 conv, CPL $19,43, CVR 32,5%). Frase (7 cuentas): CPL $17,36, CVR 32,1%. Exacta (2 cuentas): CPL $18,36, CVR 40,8%. Amplia no rinde mejor, solo gasta más: 23% del gasto Search del nicho ($5.166) se fue en search terms con 0 conversiones. En la única cuenta que mezcla exacta y amplia, la exacta rinde al doble (incluye marca). Frase por defecto está respaldado por los datos.
- **PMax**: rinde mejor que Search en cuentas maduras (CPL $6–14 vs $10–26 en la misma cuenta), siempre lanzada con 6–12 meses de Search previo. Las 2 cuentas que la lanzaron con < 3 meses fracasaron ($66–69 gastados, 1–2 conv) y la pausaron.
- **Conversiones**: 86% "Calls from Ads" (extensión de llamada), 9,5% llamadas desde web, 4,6% formularios. Llamadas es el objetivo estándar del nicho.
- Geo (presencia vs interés), programación y extensiones no son visibles por Windsor; verificar en UI/API.

## Keywords top por conversiones (agregado, 27 cuentas, 90 días)
| Keyword | Conv. | Gasto | CPL | CVR | Cuentas |
|---|---|---|---|---|---|
| towing near me | 774,5 | $13.676 | $17,66 | 36,7% | 17 |
| tow truck near me | 172,5 | $3.112 | $18,04 | 42,3% | 20 |
| roadside assistance | 76,0 | $2.174 | $28,60 | 22,8% | 9 |
| [marca propia] (3 cuentas, sumadas) | 106,5 | $1.162 | $10,91 | 37–62% | 3 |
| rv towing (cuenta heavy duty) | 59,2 | $772 | $13,05 | 48,1% | 1 |
| gruas cerca de mi | 28,0 | $648 | $23,13 | 25,0% | 3 |
| cheap towing near me | 25,0 | $463 | $18,53 | 34,2% | 8 |
| towing company near me | 25,0 | $327 | $13,10 | 42,4% | 7 |
| towing service | 23,5 | $813 | $34,58 | 21,0% | 9 |
| wrecker towing | 23,0 | $294 | $12,80 | 21,5% | 1 |
| road service near me | 21,0 | $751 | $35,75 | 21,9% | 1 |
| tow truck service | 19,0 | $88 | $4,63 | 70,4% | 2 |
| tow truck [ciudad] | 16,5 | $142 | $8,63 | 51,6% | 1 |
| asistencia en carretera | 14,0 | $217 | $15,48 | 22,6% | 2 |
| tow service | 13,0 | $147 | $11,34 | 38,2% | 2 |
| gruas [ciudad] | 13,0 | $124 | $9,50 | 32,5% | 1 |
| heavy towing | 12,2 | $128 | $10,50 | 55,3% | 1 |
| tow truck | 11,0 | $278 | $25,30 | 34,4% | 3 |
| servicio de grúa | 9,0 | $217 | $24,06 | 20,0% | 2 |
| grúa cerca de mí | 9,0 | $109 | $12,16 | 31,0% | 2 |
| towing services | 9,0 | $132 | $14,70 | 47,4% | 3 |
| tow company near me | 8,5 | $109 | $12,87 | 47,2% | 2 |

Search terms top (26 cuentas): "tow truck near me" 163,5 conv / CPL $16,51 (26 cuentas); "towing near me" 65 / $17,71; "towing company near me" 40 / $16,48; "tow company near me" 28,5 / $16,01; "cheap towing near me" 26 / $13,66; "roadside assistance near me" 15 / $21,75. "cheap / cheapest / affordable" convierte bien (CVR 34,5%, CPL $16,59): no negativizar. "price / cost / how much" también convierte (CPL $21,67, CVR 26%): no negativizar.

## Negativas que más gasto ahorraron (por tema; gasto total → CPL, CVR, $ en términos sin conversión)
Windsor no expone las listas de negativas; esto sale de los search terms con gasto y 0 conversiones (728 términos, $5.166). El desperdicio está atomizado (término máximo $54), así que se protege por tema:
- Aseguradoras / roadside de fabricante (aaa, geico, allstate, progressive, state farm, usaa, carvana, toyotacare, mopar, onstar, bristol west, root, nrma, caa, road ranger, go auto, walmart): $257 → CPL $32, CVR 18%, $199 sin conv.
- "phone number" / "número de teléfono": $347 → CPL $43, CVR 13%, $250 sin conv.
- Jump start / batería como producto (car jumper, jump starter, jump box, battery pack, battery change): $406 → CPL $45, CVR 14%, $336 sin conv.
- Gasolina (ran out of gas, emergency gas): $119 → CPL $60, $95 sin conv.
- Trailer / RV compra o alquiler (for sale, rental, hitch, dolly, dollies, hauler, toy hauler, cargo trailer, moving service): $80 → CPL $80. No negativizar "trailer" a secas si el cliente remolca trailers.
- Long distance towing: $46 → 1 conv. Negativa salvo cobertura interestatal.
- Motorcycle towing: $68 → CPL $23; negativa salvo equipo.
- Junk / cash for cars / salvage / scrap / we buy: $51.
- Tiendas de llantas (tire shop, tire place, discount tire, big o tires): dentro de tema llantas $520 → CPL $27; mantener "flat tire" si hay roadside.
- Marcas de competidores locales: por cuenta; aparecen en todas las cuentas con amplia.
- Búsquedas en otros idiomas (coreano) en mercados metro.

## Errores comunes vistos en cuentas del P25
- Maximizar clics (TARGET_SPEND): las 3 cuentas que lo usan tienen CPL $70–83.
- Cuentas de < 3 meses sin limpieza de search terms: CVR 7–19% vs 37% en maduras.
- Keywords amplias genéricas de roadside ("roadside assistance", "emergency roadside", "auto towing near me", "car battery help") que traen aseguradoras, baterías y llantas: CPL $29–45.
- PMax lanzada a las 2–3 semanas de vida de la cuenta.
- Mercado metro de CPC alto ($11+) sin tCPA.
- Marca propia mezclada con genéricos en el mismo ad group: infla la CVR aparente de la campaña y esconde el CPL real de los términos genéricos.
