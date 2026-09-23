---
cliente: 290 Tow and Recovery
slug: 290-tow-recovery
nicho: towing
pais: US
cuentas_comparables: 21
periodo: 90d (2026-06-24 → 2026-09-21) + 12 meses (2025-09-22 → 2026-09-21)
fuente: Windsor.ai (connector google_ads). Sin Google Ads API en la sesión.
actualizado: 2026-09-23
---

# Benchmark interno — 290 Tow and Recovery

## Cuentas usadas
Hay 31 cuentas de towing de PLL en Windsor. Entran al benchmark **21**: las que tuvieron gasto activo los 90 días completos y más de $750 de gasto en el periodo.

| Excluida | Motivo |
|---|---|
| Denton Affordable Towing (TX) | $57 en 90 días. En 12 meses, 4.731 clics por $1.377 vienen de Display: es tráfico basura |
| Budget Towing & Recovery | $56 en 90 días, prácticamente apagada |
| Vance, A&D Towing of Boston | Sin gasto en los 90 días (pausadas). Solo aparecen en el análisis de 12 meses |
| A1 Roadside Services | Sin datos en Windsor |
| J&S, Envy | Menos de $420 en 90 días y 37–54 clics: muestra insuficiente |
| Precision, First Response, Spillane's | Arrancaron entre el 14 y el 20 de agosto de 2026: periodo parcial |
| Beachaven Auto Care & Towing | Mezcla taller mecánico y grúa, y solo corre PMax |

**Texas**: solo hay 2 cuentas de TX. JJ's Towing (El Paso) entra al benchmark. Denton está excluida.
**Small-town / rural** (subgrupo): Cook's (Bloomsburg/Berwick, PA), Pirate (Greenville, NC), A&D Towing Service (Roanoke, VA), California Towing (Redding/Shasta, CA) y Veterans (Augusta, GA). Precision (Kern River Valley, CA) es rural pero tiene solo 5 semanas de datos.

## Rangos esperados para este nicho/país (90 días, 21 cuentas)
| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC (cuenta, Search+PMax) | $3.78 | $4.84 | $5.94 |
| CPC (solo Search) | $4.86 | $6.48 | $7.82 |
| CTR | 4.8% | 6.6% | 7.8% |
| Tasa conv. (solo Search) | 23.7% | 27.3% | 39.9% |
| CPL (cuenta) | $12.01 | $15.19 | $31.54 |
| **CPL (solo Search)** | **$13.15** | **$14.57** | **$33.27** |
| Conv./mes | 18 | 35 | 59 |
| Gasto real/mes | $357 | $706 | $1.062 |

En la tabla de CPL, P25 es el mejor cuartil (el CPL más bajo).

**12 meses** (21 cuentas, sin Beachaven): CPC $4.03 / $4.44 / $5.49 · tasa conv. 21% / 29% / 35% · CPL $10.43 / $15.13 / $28.63. Coincide con los 90 días, así que el rango es estable.

### Subgrupos relevantes para 290
| Subgrupo | CPC Search (pooled) | Conv. Search | CPL Search (pooled) | CPL cuenta P25–P75 | Gasto real/mes |
|---|---|---|---|---|---|
| Small-town (5 cuentas) | $4.48 | 34.9% | **$12.84** | $12.01–$14.47 | $262–$706 (mediana $392) |
| Tier $799–$1.500 (12 cuentas) | $5.51 | 29.4% | $18.74 | $12.29–$39.02 | $277–$515 (mediana $375) |
| Texas: JJ's (El Paso, EN+ES) | $3.32 | 26.8% | $12.38 | — | $431 |
| Metros caras (Phoenix, LA, Bay Area, Tampa, Colorado Springs) | $6.5–$10.9 | 14–26% | $30–$66 | — | — |

**CPL objetivo inicial sugerido** (mediana de Search $14.57 ±20%): **$11.70–$17.50 por llamada**.
**Con $825/mes de pauta** (solo Search, sin PMax al inicio):

| Escenario | CPL | Llamadas/mes |
|---|---|---|
| Como las cuentas small-town (pooled) | $12.84 | ~64 |
| Mediana de Search del MCC | $14.57 | ~57 |
| Tier de presupuesto similar (pooled) | $18.74 | ~44 |
| Cuartil malo de Search | $33.27 | ~25 |

- **Rango realista: 35–55 llamadas/mes** en los primeros 60 días (aprendizaje sin historial). Si rinde como las cuentas small-town, llegaría a 55–65 después.
- **tCPA**: 30 conversiones en 30 días exigen un CPL de $27.50 o menos. Es alcanzable desde el mes 1 si el tracking de llamadas cuenta bien, así que el tCPA sería evaluable hacia el día 30–45.
- **Volumen**: ninguna cuenta small-town del MCC gasta $825/mes. La mediana es $392 y la única que gasta más de $1.000 (California Towing, Redding) lo logra con PMax + Search. Existe el riesgo de que un radio de 40 mi alrededor de Fredericksburg no tenga volumen para gastar $27/día en términos de alta intención. Hay que validarlo con Keyword Planner en /strategy (incluir Kerrville, Boerne, Johnson City, Llano, Mason y la I-10).

## Lo que hacen las cuentas que mejor rinden
Cuartil superior por CPL: A&D Towing Service ($8.35), Beech Grove ($9.18), Mosby's ($9.45), Ken's ($11.32), Grand Valley ($11.33) y Veterans ($12.01).
- **Estructura**: 1 campaña Search "ENHPRM Radius" (segmentación por radio) con **1 solo ad group** ("Ad group 1" / "Towing Service") y pocas keywords genéricas de alta intención. Ninguna usa STAG por ciudad o servicio. A este volumen, un ad group consolidado junta las señales.
- **Match types**: casi todo en **amplia** ("towing near me", "tow truck near me") con Maximizar conversiones. Hay algo de frase en Beech Grove ("tow truck service", "tow truck indianapolis"). Esto choca con el estándar PMM de concordancia de frase. Funciona en esas cuentas porque tienen historial y señal de conversión abundante. Para 290, sin historial verificado, conviene **arrancar en frase** y dejar la amplia como prueba posterior.
- **Puja**: Maximizar conversiones sin tCPA en 20 de 21. Grand Valley usa Impression Share en Search y ahí su CPL de Search sube a $27.68: peor que el de las cuentas con Max Conversions.
- **PMax**: 4 de las 6 mejores tienen PMax además de Search (Mosby's, Ken's, Grand Valley, A&D). PMax les baja el CPL de cuenta: Grand Valley $5.86 en PMax contra $27.68 en Search, A&D $6.50 contra $12.47. Beech Grove y Veterans consiguen $9–12 **solo con Search**. Esto respalda el estándar de lanzar solo con Search y añadir PMax cuando haya más de 30 conversiones al mes y tracking confiable.
- **Geo**: las mejores están en mercados medianos o pequeños (Roanoke, Augusta, Wichita, Louisville, suburbios de Indianápolis). Las peores están en metros con CPC de $6.5–$11 (Phoenix, LA, Bay Area, Tampa, Colorado Springs). Fredericksburg se parece más al primer grupo.
- **Idioma**: JJ's (El Paso) separa ad groups en inglés y en español ("gruas el paso tx", "grúas cerca de mi") con CPL de $12. En Hill Country el volumen en español será menor, pero vale evaluarlo en /strategy.
- **Conversión principal**: "Calls from ads" (la extensión de llamada) aporta el 70–100% de las conversiones. Es coherente con el objetivo de llamadas de 290.
- **No extraído** (Windsor no lo da de forma fiable en esta consulta): extensiones activas, programación y presencia vs. interés. Hay que revisarlo por API cuando haya credenciales.

## Keywords que más convierten en el nicho (agregado, 90d)
Son indicativas: el keyword view de Windsor devolvió filas incompletas.
1. **towing near me** (amplia): es la keyword principal en casi todas las cuentas. En una sola cuenta suma ~$1.280 y ~106 conversiones (CPL ~$12).
2. **tow truck near me / tow trucks near me** (amplia).
3. **towing company near me / tow company near me** (amplia).
4. **tow truck service / tow service** (frase y amplia).
5. **[ciudad] + towing / tow truck** (p. ej. "towing company augusta ga", "tow truck indianapolis").
6. **Español** (El Paso): "gruas cerca de mi", "gruas el paso tx".
7. **Marca propia** ("mosby towing", "veterans towing", "grand valley towing"). **No cuenta como demanda nueva**: estas conversiones inflan la tasa de las cuentas. Coincide con el brief: sin campaña de marca al inicio.
8. **roadside assistance** (amplia, una cuenta): 30 conversiones con $392. Funciona, pero también atrae a quien busca AAA o el seguro (ver negativas).

## Negativas frecuentes del nicho
Salen de search terms con gasto de $15 o más y 0 conversiones en 90 días:
- **Precio bajo**: cheap, cheapest, $40, $50, "cheap towing", "cheapest tow truck".
- **Competidores por nombre** (el mayor desperdicio recurrente): jb towing, al towing, northside towing, r&r towing phone number, b&b towing, go&go towing, hudsonville towing. **Hay que armar la lista de competidores locales de Fredericksburg y Kerrville en /competitors.**
- **Servicios no ofrecidos o de ticket bajo**: car battery change / replacement, at home battery replacement, tire place near me, roadside tire service, ran out of gas / emergency gas for car, motorcycle towing (si no lo ofrece).
- **Programas gratuitos o de terceros**: freeway assistance, roadside assistance near me (AAA o seguro).
- **Idioma**: español y coreano en cuentas sin anuncios en ese idioma.
- La propia marca aparece con gasto y 0 conversiones en 3 cuentas: evaluar negativizarla en Search si no hay campaña de marca.

## Historial propio del cliente
**PENDIENTE.** La cuenta 213-019-5545 ("Premium Local Listings 004046 ($1500 290 Tow and Recovery)") **no aparece en Windsor.ai**: no figura entre las cuentas del connector google_ads. Tampoco hay Google Ads API en la sesión: no existe `google-ads.yaml` en el repo ni la librería `google-ads` instalada. Hay dos caminos:
1. Conectar la cuenta 213-019-5545 en Windsor (es lo más rápido).
2. Configurar la API (`docs/setup-google-ads-api.md`) y correr `python scripts/gaql.py --customer 2130195545 --file scripts/queries/benchmark.gaql`.

Cuando esté disponible, hay que comparar su CPC, CPL y tasa de conversión contra el subgrupo small-town y revisar qué conversiones contaba.

## Advertencias
- **Las conversiones son llamadas, no leads calificados.** "Calls from ads" cuenta cualquier llamada que supere el umbral de duración configurado, y Windsor no expone ese umbral. Hay señales de conteo inflado:
  - Tasa de conversión de Search del 48–53% en Beech Grove, Ken's y Mosby's.
  - Keywords con más conversiones que clics (p. ej. 15.5 conversiones con 5 clics en una fila).
  - Probables llamadas repetidas del mismo usuario.
  - Hay que tratar el CPL del MCC como **costo por llamada** y verificar el umbral (60–90 s) en la cuenta de 290.
- **Posible conteo doble**: algunas cuentas suman "Calls from ads" + "Website Calls" + "Form Fill" como conversiones primarias. Las acciones locales (direcciones, clics para llamar en Maps) están como secundarias y no inflan la columna de conversiones, salvo en California Towing, que tiene 524 all_conversions contra 225 conversiones.
- **Cuentas sin conversiones confiables**: Budget (0 conversiones) y Denton (Display basura) quedaron fuera. Envy y J&S tienen 6 conversiones cada una: muestra insuficiente.
- **Gasto real vs. el 55% del fee**: en el tier de $799–$1.200 el gasto real mediano es **$375/mes, ~33–45% del fee**. En el tier de $1.500, Summit y Kritical gastan ~$750–$770/mes (~50%) y Point A2B solo $282. Los $825/mes de 290 quedan en el extremo alto de su tier. Hay que confirmar que ese presupuesto se va a gastar de verdad.
- **Solo 1 cuenta de TX comparable** (El Paso, que es metro y bilingüe). No hay ninguna cuenta del Hill Country ni de un pueblo de Texas. El subgrupo small-town viene de otros estados.
- **Calidad de los datos de Windsor**: los desgloses por keyword y por geo devolvieron filas parciales (dos consultas del mismo keyword dieron valores distintos). Los agregados por cuenta y por campaña sí son consistentes entre sí. Los datos de keywords son indicativos.
- Los nombres de algunas cuentas cambiaron de fee (Fishhawk $2.100 → $2.400, All Pro $2.000 → $1.000).
