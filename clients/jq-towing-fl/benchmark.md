---
cliente: JQ Towing
slug: jq-towing-fl
nicho: towing
pais: US
cuentas_comparables: 31
periodo: 90d (2026-07-03 → 2026-09-30)
fuente: Windsor.ai (connector google_ads) — sin Google Ads API en la sesión
actualizado: 2026-10-01
---

# Benchmark interno — JQ Towing

Universo: 36 cuentas towing/roadside del MCC visibles en Windsor (filtro por nombre). 31 con gasto ≥ $100 en 90d (total ≈ $55k, 3.1k conv.). Excluidas por gasto 0: Vance, Budget Towing, Denton Affordable, A & D Boston, A1 Roadside. Crudo por cuenta y campaña: `data/benchmark-raw.csv`.

Métricas por cuenta; conv./mes y presupuesto/mes normalizados por **días con gasto** (12 cuentas lanzaron o pausaron dentro del periodo).

## Rangos esperados para este nicho/país
Todas las cuentas (n=31):

| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $4.52 | $5.68 | $7.31 |
| CTR | 5.2% | 6.8% | 8.2% |
| Tasa conv. | 16.4% | 23.5% | 32.5% |
| CPL | $13.39 | $28.05 | $53.06 |
| Conv./mes | 17.7 | 28.6 | 55.0 |
| Gasto real/mes | $503 | $858 | $1,125 |

El rango es bimodal; la mediana global mezcla dos poblaciones:

| Segmento | n | CPC med. | Tasa conv. med. | CPL P25 / med. / P75 | Conv./mes med. |
|---|---|---|---|---|---|
| Cuentas maduras (≥ 60 días con gasto) | 19 | $5.02 | 31% | $11.75 / $14.97 / $20.78 | 48 |
| Cuentas nuevas (< 60 días, en aprendizaje) | 12 | $7.31 | 14% | $34.79 / $59.13 / $67.97 | 17.7 |
| **Solo campañas Search** (por cuenta) | 30 | $7.02 | 26% | $14.14 / **$31.91** / $55.24 | — |
| Solo PMax (por cuenta) | 13 | — | — | $8.92 / $15.35 / $18.19 | — |
| **Florida** (Fishhawk, Jerry's, J & S; agregado) | 3 | $6.51 | 17% | CPL agregado **$37.8** (32.6 / 48.7 / 60.9) | 7.6–37.7 |

Impression share Search (mediana de 30 campañas): **IS ≈ 26%**, perdido por presupuesto ≈ 30%, por ranking ≈ 35%. Casi todas las cuentas están limitadas por presupuesto, incluso con $1k–1.5k/mes.

**CPL objetivo inicial sugerido**: mediana Search $31.91 ±20% → **$25–$38** (se usa Search, no la mediana global, porque JQ arranca sin PMax por estándar PMM y la mediana global está bajada por PMax + marca propia). Florida ($37.8) cae en el extremo alto del rango.

**Con presupuesto de $879/mes** (~125 clics/mes a CPC Search $7.02; Semrush $3 subestima ~2×):

| Escenario | CPL | Conv./mes | Días hasta ~30 conv. (tCPA) |
|---|---|---|---|
| Base (mediana Search) | $31.91 | ~27.5 | ~33 |
| Florida agregado | $37.8 | ~23 | ~39 |
| Conservador (cuentas nuevas, mes 1–2) | $59.13 | ~15 | ~61 |
| Optimista (cuentas maduras) | $14.97 | ~59 | ~16 |

Lectura: **alcanza para salir de aprendizaje de Maximizar conversiones, pero el umbral de tCPA (30 conv/30d) es límite**: realista en el mes 2–3, no en el mes 1. Además JQ medirá llamadas ≥ 60s (estándar PMM), más estricto que varias cuentas del benchmark (ver Advertencias), así que hay que esperar conteos por debajo del escenario base. No fragmentar: una sola campaña Search.

## Lo que hacen las cuentas que mejor rinden
Cuartil superior por CPL (≤ $13.4 y ≥ 5 conv./mes): 8 cuentas (TN, VA, IN, KY, MI, GA, KS, TX). CPL $8–13, CPC $1.94–6.04.
- **Antigüedad**: todas llevan meses o años activas (la más nueva, desde jun-2026). Ninguna cuenta con menos de 60 días está en el cuartil superior.
- **Campañas**: 1–2 activas. 5 de 8 combinan Search + PMax (PMax = 20–100% del gasto); 3 son solo Search (1 campaña).
- **Puja**: 8/8 Maximizar conversiones **sin tCPA**. Las cuentas con TARGET_SPEND (Max. clics) están todas en el cuartil inferior.
- **Ad groups / match types**: la mayoría usa 1–2 ad groups con concordancia **amplia** (12–40 keywords). Excepciones: dos cuentas con 8–10 ad groups y exacta predominante, y una cuenta antigua con 84 ad groups. A nivel MCC, por gasto de keyword: amplia $16.2k (CPL $21.2), exacta $12.6k (CPL $18.0), frase $7.8k (CPL $24.9). Exacta convierte más barato; amplia funciona en cuentas maduras con Max. conv.; frase no muestra ventaja (es la de menor gasto y suele estar en cuentas nuevas).
- **Marca propia**: 3 del cuartil superior pujan por su propio nombre ("grand valley towing", "mosby towing", "veterans towing", CPL $10–13), lo que baja su CPL.
- **Negativas**: lista a nivel de campaña de ~190 términos presente en 28–31 cuentas (ver abajo) más negativas por ad group en 24 cuentas.
- **Español**: varias cuentas tienen ad group en español ("gruas cerca de mi", "asistencia en carretera", CPL $12–26). Relevante solo si JQ atiende en español.
- No extraído (Windsor no lo expone limpio): programación horaria, tipo de geo (presencia vs. interés), extensiones activas, tCPA histórico.

Implicación para JQ: el estándar PMM (frase + STAG) no tiene evidencia directa a favor en este MCC. Recomendación para /strategy: arrancar con **exacta + frase** en "towing near me", "tow truck near me", "towing company near me" y variantes con ciudad, Max. conv. sin tCPA. Amplia queda como prueba solo con tracking maduro y aprobación (estándar #2).

## Keywords que más convierten en el nicho (agregado, 90d)
| Keyword | # cuentas | Gasto | Conv. | CPL | CPC |
|---|---|---|---|---|---|
| towing near me | 20 | $14.2k | 776 | $18.3 | $6.53 |
| tow truck near me | 23 | $3.4k | 176 | $19.1 | $7.70 |
| roadside assistance | 10 | $2.4k | 77 | $30.9 | $6.53 |
| towing company near me | 9 | $605 | 32 | $18.9 | $6.87 |
| cheap towing near me | 11 | $568 | 28 | $20.3 | $6.68 |
| gruas cerca de mi | 4 | $685 | 29 | $23.6 | $5.86 |
| towing service | 12 | $1.1k | 26 | $41.8 | $7.26 |
| tow truck | 4 | $670 | 22 | $31.2 | $12.65 |
| tow truck service / tow service | 2–2 | $231 | 32 | $4–11 | $3–4 |
| tow truck [ciudad] (Louisville, Indianapolis, Rochester) | 1 c/u | — | 8–16 | $8.5–28 | $3.7–9.1 |
| roadside assistance near me | 11 | $435 | 9 | $48.3 | $8.21 |
| rv towing / heavy towing / wrecker towing | 1 c/u | — | 12–59 | $10–13 | $2.7–6.2 |

"towing near me" concentra ~40% del gasto y conversiones de keywords del MCC. Roadside genérico convierte peor (CPL $31–48) que towing: conviene ad group propio con presupuesto vigilado. Sin conversiones con gasto: "emergency roadside", "auto towing near me", "car battery help", "flat tire assistance near me".

## Negativas frecuentes del nicho
Lista base presente en ≥ 28 de 31 cuentas (campaña):
- **Motor clubs / aseguradoras**: aaa, triple a, aa, agero, allstate, geico, progressive, state farm, usaa, nationwide, esurance, safeco, farmers, travelers, kemper, erie, amica, aarp, good sam / goodsam, onstar / on star, motorclub, national motor club, membership, insurance, american express
- **Marcas de auto / concesionarios**: ford, chevy, chevrolet, toyota, honda, kia, hyundai, lexus, bmw, mercedes, tesla, dodge, ram, jeep, gmc, subaru, nissan, mazda, volvo, cadillac, acura, audi, infiniti, jaguar, land rover, dealer, carmax
- **Impound / repo / "me remolcaron"**: impound, impounded, tow yard, tow lot, yard(s), towed, my car was towed, did you tow my car, find my towed car, repo, repossession, police
- **Renta / equipo / venta**: for sale, rent, rental(s), u haul / uhaul, penske, ryder, hertz, enterprise, jerr dan, copart, parts, accessories, kit
- **Talleres / llantas** (si el cliente no lo ofrece): mechanic, mecanico, car repair, shop(s), pep boys, firestone, flat tire repair (near me), tire repair near me, tire change near me
- **DIY / gratis**: how to, diy, do it yourself, free
- **Competidores nacionales y locales**: swoop dispatch, uber, loves, rudys, wyatts, etc. Para JQ, añadir los competidores de Ocala (J&D, K&J) tras /competitors.

Desperdicio en search terms (Windsor, solo Search, $24k): las categorías de basura ya están casi bloqueadas (precio/info $238, junk cars $63, DIY $19). El desperdicio que queda es **nombres de competidores** ("b&b towing", "jb towing", "northside towing", "ali's towing", "r&r towing phone number"), **ciudades fuera del área** y "grua" suelto. Para JQ: negativa de competidores locales desde el día 1 y revisión semanal de ciudades.

Ojo con "flat tire service", "tire change near me" y "jump start": la lista base los excluye. Si JQ ofrece llanta o jump (pendiente en brief), **no** copiar esas negativas.

## Historial propio del cliente
**PENDIENTE.** La cuenta indicada **986-810-9972 no está disponible en Windsor** ("Account 986-810-9972 is not available"). Tampoco aparece en `get_connectors` (68 cuentas Google Ads conectadas). Y no hay Google Ads API configurada (`google-ads.yaml` no existe).
Para desbloquear: (a) agregar la cuenta a Windsor (https://onboard.windsor.ai?datasource=google_ads), o (b) configurar la API (`docs/setup-google-ads-api.md`) y correr `scripts/queries/benchmark.gaql` sobre ella. Al tenerla, comparar CPL/CPC/IS vs. este benchmark y revisar Auction Insights en Ocala.

## Advertencias
- **Fuente Windsor, no API**: no se pudieron leer configuración de conversiones (umbral de duración de llamada, conteo uno/todos), programación, presencia vs. interés ni extensiones.
- **Conversiones probablemente infladas en varias cuentas**:
  - Tasas de conversión de 38–50% (6 de las 8 cuentas del cuartil superior) son altas para Search y sugieren llamadas cortas contadas como lead.
  - Dos cuentas usan acción "Website Call(s) (20')" (umbral aparente de 20s).
  - "Calls from ads" depende del umbral configurado, que no es visible.
  - Una cuenta tiene 3 acciones primarias (llamadas de anuncio + llamadas web + formulario: 442 conv./90d, CPL $9.9), con posible doble conteo del mismo usuario.
  - El CPL del cuartil superior ($8–13) debe tratarse como **costo por llamada**, no por lead calificado.
- **Marca propia en keywords** de las mejores cuentas baja su CPL; JQ no tiene demanda de marca medible (brief).
- **PMax mejora el CPL agregado** (PMax $13.4 vs. Search $20.5 en agregado), pero incluye marca y acciones locales; no es comparable 1:1 con Search.
- **Mezcla de madurez**: 12/31 cuentas tienen < 60 días con gasto. Por eso hay segmentos separados; usar el escenario conservador para el mes 1.
- **Geo**:
  - Una cuenta de TX gastó $183 en Chihuahua (MX) y otra $9.5 en Ontario (CA). Posible ubicación "presencia o interés" o radio fronterizo; confirma la regla PMM #1.
  - Ubicación del cliente en el nombre/región de Windsor; las 3 cuentas FL no se pudieron ubicar a nivel ciudad.
- **Search terms**: Windsor cubre ~$24k de ~$55k (no incluye PMax). Los conteos de negativas incluyen campañas pausadas.
- **Benchmarks = expectativa inicial, no promesa**. El CPL máximo real de JQ sigue PENDIENTE (ticket, margen, cierre).
