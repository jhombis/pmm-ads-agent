---
cliente: 290 Tow and Recovery
slug: 290-tow-recovery
nicho: towing
pais: US
cuentas_comparables: 21
periodo: 90d (2026-06-24 → 2026-09-21) + 12 meses (2025-09-22 → 2026-09-21)
fuente: Windsor.ai (connector google_ads). Sin Google Ads API en la sesión. Historial propio 213-019-5545 leído 2026-09-23.
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

## Historial propio de la cuenta (213-019-5545)
**Fuente**: Windsor.ai (connector google_ads), leído el 2026-09-23 (hoy incluido, parcial). CSV en `data/hist-*.csv`.

**No hay historial previo.** La cuenta se lanzó el **2026-09-17** (la primera impresión es del 18/09). "Todo el historial", "12 meses" y "90 días" son lo mismo: **6 días**. No sirve como benchmark propio. Lo que sí deja ver es cómo quedó montada la cuenta y qué tráfico atrae.

### Qué está corriendo
| Campaña | Tipo | Estado | Puja | Presupuesto | Geo | Redes |
|---|---|---|---|---|---|---|
| 290 Tow and Recovery - ENHPRM Radius - $1500/mo. - 09/17/2026 | Search | Activa | **Maximizar clics** (TARGET_SPEND) | $27/día | Presencia, radio de 40 mi (centro 30.315, -98.925, ~4 mi al NO del centro de Fredericksburg) + 1 ubicación excluida (Windsor no dice cuál) | Solo Google Search: partners y Display apagados |

- Estructura: la plantilla PLL "ENHPRM Radius", con **1 ad group ("Ad group 1") y 10 keywords, todas en amplia**: towing near me, towing company near me, tow truck near me, wrecker service near me, roadside service near me, roadside assistance, roadside assistance near me, emergency roadside, towing car, tow a car.
- Programación: sin programación de anuncios, así que corre 24/7 (coincide con el brief). La zona horaria de la cuenta es **America/Los_Angeles**, pero el cliente está en hora Central. Hay que tenerlo en cuenta al leer los reportes por hora y al programar anuncios.
- Extensión de llamada: (830) 463-8318, con la acción de conversión de llamada definida a nivel de cuenta.
- No hay PMax, Display ni otras campañas.

### Resultados (2026-09-18 → 2026-09-23)
| Métrica | 290 (6 días) | MCC Search P25 / Mediana / P75 | Small-town (Search, pooled) |
|---|---|---|---|
| Gasto | $165.57 (~$33/día en los 3 días completos) | — | — |
| Impresiones / clics | 85 / 14 | — | — |
| CTR | 16.5% | 4.8% / 6.6% / 7.8% (cuenta) | — |
| **CPC** | **$11.83** | $4.86 / $6.48 / $7.82 | $4.48 |
| Conversiones | **0** (all_conversions 0, phone_calls 0) | — | — |
| Tasa conv. | 0% (0/14) | 23.7% / 27.3% / 39.9% | 34.9% |
| CPL | n/a | $13.15 / $14.57 / $33.27 | $12.84 |

Por mes: solo septiembre de 2026, con los mismos números. Por red: 100% Search.

**Lectura**:
- 14 clics es una muestra mínima. Con la tasa mediana del MCC (27%) se esperaban unas 3–4 conversiones, así que 0 **todavía no es estadísticamente anormal**. Aun así, que no se haya registrado ni una llamada de la extensión (phone_calls = 0) en 85 impresiones y 14 clics refuerza el bloqueante de tracking.
- **El CPC de $11.83 es 1.8 veces la mediana de Search del MCC y 2.6 veces el del subgrupo small-town.** La causa probable es Maximizar clics en amplia con un presupuesto chico, en una zona con poca subasta y con el borde del radio tocando el área de San Antonio. Con ese CPC, aunque convierta al 27%, el CPL sería de unos **$44**: 3 veces el CPL máximo provisional ($14) y por encima del P75 del MCC.
- El CTR del 16.5% es alto, pero en una muestra de 85 impresiones con amplia no dice nada de la calidad.

### Keywords (spend / clics / conv.)
towing near me $75.68 / 7 / 0 · towing company near me $27.76 / 2 / 0 · wrecker service near me $21.70 / 2 / 0 · tow truck near me $17.84 / 1 / 0 · roadside service near me $11.74 / 1 / 0 · roadside assistance $10.85 / 1 / 0. El resto tiene $0. Las keywords de **roadside suman $22.59 (14%) y todas son amplias**: es el servicio de ticket más bajo.

### Search terms y desperdicio
Los términos visibles suman $120.57 de $165.57. **$45 (27%) no aparecen** en el reporte (umbral de privacidad de Google).
- **Desperdicio claro: $71.24 = 59% del gasto visible (43% del total).**
  - "car jumper" $27.48 (2 clics): alguien buscando un arrancador para comprar, no un servicio.
  - "car dollies for towing" $12.61: equipo.
  - "cheap tow truck near me" $11.84: precio bajo.
  - "rv haulers in texas" $11.43: transporte/hauling.
  - "what does roadside assistance cover" $7.88: informacional o de seguro.
  - "emergency roadside assistance" $9.69 es dudoso (AAA/seguro).
- **Con impresiones pero sin gasto todavía**:
  - Competidores: K&W Towing (Boerne), 5 Star Towing Boerne, Creswell Towing (San Antonio), Gator Towing, Tic Tac Towing, EJ Towing Denton.
  - Áreas fuera de zona: San Antonio ("tow truck san antonio", "towing san antonio near me").
  - Heavy duty: "semi truck tow".
  - Compra de equipo: "rollback tow truck", "wrecker trucks".
  - Precio: "cheapest wrecker service".
  - Español: "gruas", "gruas cerca de mi".
- **Fredericksburg, Virginia**: **no apareció ningún término de VA**. El 100% del gasto por geo está en Texas. Igual hay que añadir "virginia", "va" y "22401" como negativas preventivas, porque en frase "towing fredericksburg" puede captar búsquedas de VA hechas desde Texas.
- **Transport/shipping**: solo "rv haulers in texas" ($11.43). No hubo "car shipping" ni "auto transport" en estos 6 días.
- Los términos con match "EXACT/NEAR_EXACT" son los mejores (tow truck near me, wreckers near me, roadside service near me). Todo el desperdicio entró por **amplia**, lo que confirma el estándar PMM de arrancar en frase.

### Geo (gasto por ciudad)
| Ciudad | Gasto | Clics |
|---|---|---|
| **Fair Oaks Ranch** | **$58.08 (35%)** | 5 |
| Kerrville | $29.48 | 2 |
| Bandera | $15.15 | 1 |
| Kingsland | $12.61 | 1 |
| Blanco | $11.84 | 1 |
| Comfort | $11.74 | 1 |
| **Fredericksburg** | **$11.43 (7%)** | 1 |
| Llano | $7.88 | 1 |
| Granite Shoals | $7.36 | 1 |

Fair Oaks Ranch y Bandera quedan a unos 41–43 mi del centro del radio, en el borde exterior. Fair Oaks Ranch es periferia de San Antonio, donde la subasta es más cara. **El 35% del gasto se va al borde metropolitano y solo el 7% a Fredericksburg.** Hay que confirmar con el cliente si realmente atiende Fair Oaks Ranch y Boerne. Si no, conviene reducir el radio o centrarlo en Fredericksburg y excluir Bexar/Kendall sur.

### Acciones de conversión
| Acción | Tipo | Conteo | Primaria | Ventana |
|---|---|---|---|---|
| Calls from Ads | AD_CALL (extensión de llamada) | Una por clic | Sí | 30 d |
| Website Calls | WEBSITE_CALL (número de reenvío en el sitio) | Una por clic | Sí | 30 d |
| Form Fill | WEBPAGE | Una por clic | Sí | 90 d |

- El conteo "una por clic" está bien para leads.
- Windsor no expone el **umbral de duración de la llamada**. Hay que verificarlo en la UI (recomendado 60–90 s para towing).
- Las 3 son primarias, igual que en las cuentas del MCC con posible conteo doble. Es aceptable mientras no se cuente la misma llamada en dos acciones.
- Windsor no devuelve la fecha de la última conversión recibida por acción, así que **no se puede confirmar desde aquí que el tag y Website Calls estén disparando**. Sigue siendo necesario probarlo con Tag Assistant (bloqueante).

### Diagnóstico vs. benchmark
1. **La cuenta ya está gastando antes de cumplir los estándares PMM**: tracking sin verificar, puja a clics y todo en amplia. Va contra los estándares 2, 6 y 7.
2. La plantilla PLL (1 ad group, amplia, near me) es la misma que usan las mejores cuentas del MCC. Pero esas cuentas pujan con **Maximizar conversiones y tienen historial**. Aquí, con Maximizar clics y sin señal, la amplia salió a CPC de $11.83 con un 43% de desperdicio claro.
3. **Acciones para /strategy**:
   - Pasar a frase o exacta con los términos que sí sirvieron.
   - Cambiar a Maximizar conversiones en cuanto se verifique el tracking. Mientras tanto, Maximizar clics con límite de CPC (~$7).
   - Aplicar ya la lista de negativas universal y la de towing, más competidores, "jumper/jump starter", "dolly/dollies", "hauler(s)", "semi", "cheap", "what does", "virginia/va".
   - Revisar el radio por el borde de San Antonio.
   - Separar o limitar roadside.
4. El benchmark del MCC sigue siendo la referencia para fijar objetivos. Hay que volver a leer esta cuenta a los 30 días (~60 clics) para tener un CPL propio.

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
