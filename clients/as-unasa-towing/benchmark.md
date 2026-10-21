---
cliente: A's Unasa Towing
slug: as-unasa-towing
nicho: towing
pais: US
cuentas_comparables: 15 por paquete ($799–1,500) + 8 de metro mediana (4 están en los dos grupos) → 19 cuentas distintas
periodo: 90d (2026-07-23 → 2026-10-20) + serie mensual oct-2025 → oct-2026 para la cohorte nueva
actualizado: 2026-10-21
fuente: Windsor.ai (google_ads, MCC PMM) + Semrush (CPC por ciudad). Crudos en knowledge/benchmarks/raw/towing-us-2026-10-21-*
---

# Benchmark interno — A's Unasa Towing

**Fuente y método.** Usé Windsor.ai (`google_ads`) sobre el MCC de PMM porque esta sesión no tiene `google-ads.yaml` (Google Ads API no disponible). La ventana es de 90 días, del 2026-07-23 al 2026-10-20.

Hay 27 cuentas de towing/roadside en US con 30 días o más de gasto. Las identifiqué por nombre, porque el MCC no tiene etiquetas `nicho:`/`pais:`. Dejé fuera 4 cuentas con menos de 30 días y la propia cuenta del cliente.

Las cuentas van anonimizadas (A–S). Para cada una doy el tipo de mercado y el estado, nunca el nombre.

**Por qué saqué datos nuevos si el consolidado tiene solo 20 días.** `knowledge/benchmarks/towing-us.md` (2026-10-01) sigue vigente, porque tiene menos de 90 días. Pero no traía tres cortes que hacen falta para este cliente:
- por tamaño de paquete
- por tipo de metro
- la curva de la cohorte nueva mes a mes

Desde entonces, además, 8 cuentas lanzadas entre agosto y septiembre sumaron 3 semanas más de datos. La extracción nueva se sumó al consolidado (ver ese archivo).

**Historial propio: no hay.** La cuenta 730-795-5909 está en el conector, pero no tiene ninguna fila de gasto entre oct-2025 y oct-2026 (Windsor, pull mensual de 13 meses). Es una cuenta nueva: todo lo que sigue es expectativa, no diagnóstico.

## Rangos esperados para este nicho/país

### 1. Cuentas comparables por paquete ($799–1,500), 90 días

n = 15. Gasto/mes y conv./mes normalizados por días con gasto.

| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $4.16 | $5.46 | $7.79 |
| CTR | 6.7% | 7.8% | 9.3% |
| Tasa conv. | 17.7% | 25.1% | 35.3% |
| CPL | $12.23 | $15.99 | $40.50 |
| Conv./mes | 19.1 | 22.7 | 36.9 |
| Gasto real en medios/mes | $423 | $539 | $830 |

- Solo las **maduras** de ese paquete (n = 9, primer gasto antes de abr-2026): CPC $4.25 / **$4.95** / $5.46 · CVR 24.6% / **34.2%** / 36.8% · **CPL $11.41 / $13.52 / $15.99** · 18.5 / **28** / 51.3 conv. al mes · gasto $331 / **$448** / $508 al mes.
- Solo las **"solo Search"** de ese paquete (n = 8): CPL $12.33 / $14.17 / $55.64 · CPC $4.42 / $5.20 / $8.60.
- Como referencia del nicho completo (27 cuentas): CPL $12.98 / $20.49 / $38.13. Las campañas Search del nicho (29 campañas) dan **$14.25 / $29.90 / $50.91**.

### 2. Metros medianas del oeste e interior (n = 8)

Son Las Vegas, Colorado Springs, Phoenix (2), Bakersfield, Louisville, Wichita y Oklahoma City. Cada cuenta quedó en el metro donde está la mayor parte de su gasto según el informe geo de Windsor. Ese informe solo cubre una parte del gasto.

| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $5.06 | $6.40 | $8.21 |
| CTR | 4.4% | 5.5% | 6.5% |
| Tasa conv. | 14.7% | 23.8% | 34.8% |
| CPL | $15.49 | $30.06 | $41.22 |

Este grupo sale peor que el de paquete porque mezcla 3 cuentas nuevas (Phoenix, Bakersfield y Oklahoma City) y 1 madura con Maximizar clics (Phoenix). Las 4 maduras con Maximizar conversiones tienen CPL de $10.55–28.57.

**El comparable más cercano a Salt Lake City es la cuenta H (Las Vegas, NV)**:
- Metro mediana del oeste, paquete de $1,000.
- Semrush le da $3.44–3.69 de CPC en "towing/tow truck las vegas"; Salt Lake City tiene $3.87–4.56 en "towing/tow truck salt lake city".
- Con **$448 al mes** de medios hace **CPC $5.46, CVR 34.2%, CPL $15.99 y 28 conversiones al mes**. Su campaña Search sola da un CPL de $15.15.
- Lleva más de 12 meses activa y tiene PMax desde 2025. Es la meta a 6 meses o más, no el arranque.

### 3. Del CPC de Semrush al CPC real (calibración, inferida)

En las cuentas maduras del MCC, el CPC real de la cuenta fue **1.1–2.25 veces** el CPC que Semrush da para "towing + ciudad", con una mediana de ~1.56× en 6 metros:

| Metro | Ratio |
|---|---|
| Louisville | 1.11 |
| Colorado Springs | 1.21 |
| Las Vegas | 1.53 |
| Indianapolis | 1.59 |
| Augusta | 2.18 |
| Wichita | 2.25 |

En las cuentas nuevas el ratio fue de 1.27× (El Paso), 2.22× (Oklahoma City) y 3.53× (Bakersfield).

Lo mismo pasa con las keywords nacionales. Semrush da $3.81 para "towing near me" y $4.36 para "tow truck near me". En el MCC, las maduras pagaron $6.26 y $6.22 (1.4–1.6×), y las nuevas $9.04 y $9.02 (2.1–2.4×).

**Aplicado a Salt Lake City** ($3.87–4.56 en Semrush, según el brief):
- **CPC real de ~$6.0–7.1 como cuenta madura**
- **~$8.6–10.1 en los primeros meses** si se repite el ratio de las nuevas

El CPC pooled de la cohorte nueva del MCC es $6.8–6.9. Para planificar uso **$7–10 en los meses 1–2 y $5–7 desde el mes 4**. Es una inferencia: compara el CPC de toda la cuenta con el de una keyword de ciudad.

### 4. Cohorte de cuentas nuevas (lo que importa para el lanzamiento)

Son las 15 cuentas de towing lanzadas en 2026. M1 = mes calendario del lanzamiento, que suele ser parcial. Oct-2026 cubre solo 20 días.

| Edad | Cuenta-meses | CPC | CVR | CPL pooled | CPL mediana (rango) |
|---|---|---|---|---|---|
| M1 | 15 | $6.89 | 14.4% | $47.82 | **$65.24** ($13.5–108.3) |
| M2 | 13 | $6.08 | 18.3% | $33.20 | **$40.56** ($10.3–65.0) |
| M3 | 6 | $4.65 | 17.0% | $27.44 | **$37.44** ($16.7–75.9) |
| M4–M7 | 7 (3 cuentas) | $4.65 | 21.1% | $22.08 | **$21.65** ($11.1–44.5) |

Con bloques exactos de 30 días desde el primer gasto, en las 7 cuentas que completaron el primer bloque, los días 1–30 dan **CPC $6.82, CVR 14.9% y CPL $45.82**. Los días 31–60, en las 3 que los completaron, dan CPL $46.62.

**Lectura para A's Unasa**:
- **Meses 1–2**: CPL de $33–65 por llamada.
- **Mes 3**: $27–37.
- **Meses 4–6**: ~$22.
- **Meta a 6 meses o más**: la mediana madura del paquete, **$13.52** (rango P25–P75 de $11.41–15.99).

La brecha con las maduras está en la tasa de conversión (14–18% contra 34%), no solo en el CPC. Coincide con el consolidado, que dice $51–63 en los meses 1–2 y convergencia a $15–28 en los meses 3–6.

**Excepción a no tomar como base**: la cuenta D (paquete de $1,200, El Paso TX) tuvo un CPL de $10–17 desde el mes 1. Es un mercado bilingüe con CPC de $2.49–4.26, y el 60% de su gasto va al ad group en español. No es replicable en Salt Lake City sin evidencia de demanda en español; ver Advertencias.

### CPL objetivo inicial sugerido
- **Meses 1–2 (sin objetivo, solo control)**: esperar $33–65. No juzgar la cuenta contra las maduras en los primeros 60 días.
- **Meses 3–6**: la mediana de las campañas Search del nicho ($29.90) ±20% da **$24–36**. Es el número para `strategy.md`.
- **Meta a 6 meses o más**: la mediana madura del paquete ($13.52) ±20% da **$10.8–16.2**.

### Con un presupuesto de $396–540 al mes en medios
**De dónde sale el rango de $396–540**:
- El brief lo toma del 33–45% del consolidado para paquetes de $799–1,200.
- Con los datos de hoy, los paquetes de $799–1,200 (n = 9) mandan a medios el **37% / 45% / 47%** (P25 / mediana / P75). En un paquete de $1,200 eso da **$444 / $540 / $564**.
- Las 2 cuentas de $1,200 con 30 días o más de gasto gastan **$539** (45%) y **$639** (53%) al mes.
- **$540 es el número más respaldado.** El gasto real lo tiene que confirmar Jhombis; sigue PENDIENTE en el brief.

Eso equivale a **$13.0–17.8 al día**.

| Escenario | CPC | Clics/mes | Clics/día | Conv./mes (llamadas sin calificar) |
|---|---|---|---|---|
| M1 (CPL $48–65) | $6.9–10 | 39–78 | 1.3–2.6 | **6–11** |
| M2 (CPL $33–41) | ~$6–9 | — | — | **10–16** |
| M3 (CPL $27–37) | ~$5–7 | — | — | **11–20** |
| M4–6 (CPL ~$22) | ~$5 | 80–109 | 2.6–3.6 | **18–25** |
| Madura (CPL $11.41–15.99) | $4.95–5.46 | 73–109 | 2.4–3.6 | **25–47** |

**Qué implica**:
- **Hay muy poco volumen.** Con 1.3–2.6 clics al día en los meses 1–2, la cuenta queda por debajo del rango del playbook (3–15 clics al día). Una tasa de conversión es interpretable recién hacia la semana 3–4, cuando pasa los ~50 clics (playbook §9). Un A/B de anuncios no se puede leer en todo el trimestre.
- **Para pasar a Maximizar conversiones** (15 o más conv. al mes, estándar #6) hace falta un CPL de $26 o menos con $396, o de $36 o menos con $540.
  - Con $540, el mes 3 queda en el límite (11–20) y desde el mes 4 se cumple (18–25).
  - Con $396, recién desde el mes 4 (18).
- **Para tCPA** (~30 conv. en 30 días) hace falta un CPL de $13–18. Eso solo pasa con el CPL de una cuenta madura (mediana de $13.52). Con $540 no conviene planificarlo antes del mes 6. Con $396 queda en el límite incluso maduro (29 al mes con la mediana).
- **Cobertura de la demanda**: las campañas Search del nicho tienen una cuota de impresiones de 19% / 25% / 31% y pierden 26% / 32% / 47% por presupuesto. Ninguna satura la demanda. Con $13–18 al día, el cliente va a estar limitado por presupuesto, y es normal: las mejores cuentas del paquete gastan **$6–23 al día** (presupuesto vigente).
- **Capacidad**: 6–25 llamadas al mes no satura 1 grúa. El riesgo no es el volumen, es contestar (ver brief: horario y 1 conductor).
- **Economía**: con el piso publicado de $79.99, el brief calcula un CPL máximo de ~$17. Solo el CPL maduro ($11–16) entra en ese número. Los meses 1–5 ($22–65) pierden plata salvo que el ticket real sea más alto. **El ticket sigue siendo la pregunta #1.**

## Lo que hacen las cuentas que mejor rinden

La mitad superior del paquete (8 de 15) son las cuentas A–H, con CPL de $7.75–15.99.

| Cuenta | Mercado | Paquete | Campañas | CPC | CVR | CPL | Medios/mes |
|---|---|---|---|---|---|---|---|
| A | VA, ciudad chica | $1,000 | Search + PMax | $1.88 | 24.2% | $7.75 | $398 |
| B | TN | $1,000 | solo PMax | $4.25 | 52.1% | $8.16 | $470 |
| C | Indianápolis, IN | $900 | solo Search | $4.95 | 43.4% | $11.41 | $331 |
| D | El Paso, TX (bilingüe) | $1,200 | solo Search (nueva, jul-26) | $3.74 | 31.1% | $12.03 | $539 |
| E | GA, ciudad mediana | $1,399 | solo Search | $4.53 | 36.4% | $12.44 | $693 |
| F | NC, pueblo | $799 | solo Search | $4.08 | 30.2% | $13.52 | $277 |
| G | PA, pueblo | $799 | solo Search | $5.46 | 36.8% | $14.83 | $275 |
| H | Las Vegas, NV | $1,000 | Search + PMax | $5.46 | 34.2% | $15.99 | $448 |

La mitad inferior del paquete son las cuentas I–O, con CPL de $31.54–73.25.
- 5 de esas 7 son nuevas (I, J, K, L, N): lanzadas entre jun y sep de 2026, en Phoenix, Bay Area, Bakersfield, FL y TX.
- O (Phoenix, $799) es madura, con **Maximizar clics** y CPL de $73.25.
- M (Los Ángeles, $1,500) es madura y solo Search, con CPC de $12.51 y CPL de $50.91. Es el patrón de "metro cara con paquete bajo".

**Estructura de A–H**:
- **1 campaña Search por radio** ("ENHPRM Radius"; C usa "Search Mobile").
- **1 solo ad group** en las 7 que tienen Search. La excepción es D: 2 ad groups, EN + ES, en un mercado bilingüe.
- El presupuesto vigente es de $6–23 al día.
- **"towing near me" concentra el gasto de keyword**: 68% en E, 85% en H y 91% en G.
- Ninguna usa SKAG ni grupos por ciudad. Cumple el límite de fragmentación del playbook: con menos de $600 al mes, 1 campaña y 2–3 grupos.

**PMax**: está en 3 de 8 (A, B, H), y siempre es madura, desde 2024–2025. El CPL pooled del nicho da $14.47 en PMax contra $20.59 en Search, pero PMax incluye acciones de Maps y no se lanza al inicio (estándar #9).

**Puja** (valor vigente, no histórico):
- Las 8 usan **Maximizar conversiones**.
- Hoy hay 4 cuentas de towing en **Maximizar clics**:
  - O, madura: CPL $73.25
  - una nueva de 26 días: CPL $42.25
  - una de 20 días: CPL $80.27
  - una de 23 días: 0 conversiones con $258
- **Contradicción con el estándar #6** (cuenta nueva → Maximizar clics con tope de CPC): en el MCC, Maximizar clics sale peor en las dos extracciones. Pero Windsor no expone el tope de CPC, así que no sé si esas cuentas lo tenían, y la variable se confunde con la edad de la cuenta. **Se mantiene el estándar** (decisión de Jhombis, 23-sep-2026), con dos cuidados:
  - el tope de CPC importa; como referencia, el CPC pooled de la cohorte nueva es $6.82–6.89 y el CPC calibrado de Salt Lake City como cuenta madura es de $6.0–7.1
  - pasar a Maximizar conversiones apenas haya 15 o más conversiones al mes limpias, que con este presupuesto sería el mes 3–4

**Match types**: todo el MCC está en amplia (19 de 19 cuentas).

| Match | Cuentas | Gasto | CPL |
|---|---|---|---|
| Amplia | 19 | $24,132 | $19.91 |
| Frase | 6 | $1,078 | $15.07 |

El mejor ejemplo de frase es C: "tow truck service", "tow truck + ciudad", "towing services + ciudad" y "tow truck companies near me" en frase, con $296 y 34.5 conversiones (~$8.59).

La muestra de frase es chica. La razón para usar frase (estándar #2) es controlar el desperdicio de amplia, no esperar un CPL más bajo.

**Geo, programación y extensiones**: Windsor no los expone. Según el consolidado, el cuartil superior usa "Presencia".

## Keywords que más convierten en el nicho (agregado)

Fuente: `keyword_text` de 19 cuentas comparables, 90 días.

| Tema | Maduras: CPC / CVR / CPL | Nuevas (2026): CPC / CVR / CPL | Cuentas |
|---|---|---|---|
| towing near me | $6.26 / 37.0% / **$16.93** | $9.04 / 18.3% / **$49.38** | 15 |
| tow truck near me | $6.22 / 52.2% / **$11.93** | $9.02 / 26.3% / $34.27 | 17 |
| tow/towing service (+ near me) | $4.09 / 41.8% / $9.79 | $7.26 / 26.1% / $27.88 | 15 |
| towing/tow truck company (+ near me) | $5.74 / 43.4% / $13.24 | $9.51 / 18.8% / $50.73 | 11 |
| servicio + ciudad ("tow truck louisville ky", "towing augusta ga") | $4.64 / 35.8% / **$12.96** | $11.52 / 31.5% / $36.60 | 11 |
| cheap towing / tow truck near me | $5.23 / 64.3% / $8.14 | $8.09 / 21.6% / $37.51 | 8 |
| roadside assistance (+ near me, company) | $4.50 / 28.2% / $15.96 | $7.73 / 17.8% / $43.46 | 12 |
| roadside específico (llanta, jump, batería) | $7.08 / 26.1% / $27.14 | $5.82 / 11.1% / $52.37 | 5 |
| marca propia | $4.55 / 43.4% / $10.47 | — | 6 |
| español (gruas cerca de mi, servicio de grúa, auxilio vial) | $10.27 / 18.8% / $54.80 (1 cuenta, Los Ángeles) | $4.58 / 24.5% / $18.67 (sobre todo D, El Paso) | 5 |

Las conversiones a nivel keyword son una parte de las de la cuenta, porque las llamadas del activo y PMax no se atribuyen a keyword. Sirven para ordenar.

**Para A's Unasa**, con los volúmenes de Semrush del brief y lo que convierte en el MCC:
- **Núcleo**, en frase: "towing near me" (110k nacional), "tow truck near me" (135k), "towing company near me" (49.5k), "towing service" y "tow truck service".
- **Ciudad** (en el MCC, servicio + ciudad convierte a $12.96 en las maduras):
  - "towing salt lake city" (140/mes, $3.87)
  - "tow truck salt lake city" (110, $4.56)
  - "salt lake towing" (110, $3.67)
  - "salt lake city towing" (90, $4.52)
  - "west valley towing" (110, $3.34)
  - "kearns towing" (20)
  - "towing sandy utah" / "tow truck sandy utah" (20 c/u)
- **Diferenciador**: "flatbed tow truck near me" (320, $4.09). En el MCC, "flatbed towing near me" tuvo $21 con 0 conversiones en 1 cuenta; la muestra no alcanza para concluir.
- **"cheap towing salt lake city"** (40, $3.50): cheap convierte en el MCC ($8 en las maduras, $38 en las nuevas), pero choca con la economía del piso de $79.99. Hay que decidirlo en `/strategy`.
- **Roadside**: CPL de $16–43, y el específico (llanta, jump, batería) de $27–52, con poco volumen. Con 1 grúa y un ticket bajo, va como secundario o no va. Pendiente de lo que conteste el cliente en la pregunta #8 del brief.
- **Exotic & classic transport y medium-duty**: **no hay datos en el MCC**. Ninguna cuenta comparable tiene keywords de esos servicios con clics. Si entran, es como prueba, sin benchmark.
- **No usar "sandy towing"** (260/mes, CPC $1.61): el brief lo marca como búsqueda de navegación hacia otra empresa.

## Negativas frecuentes del nicho

La lista completa por tema está en `knowledge/benchmarks/towing-us.md` (728 términos con $5,166 de gasto sin conversión). Para este cliente, desde el día 1, además de la lista universal:
- **Siempre**:
  - aseguradoras y motor clubs (aaa, geico, state farm, progressive…)
  - "phone number"
  - batería o jump starter como producto
  - compra o renta de trailers
  - junk, salvage, cash for cars
  - impound, "car was towed" y tow yard
  - renta de equipo (u haul, penske…)
  - talleres
  - informacionales ("average tow cost")
  - empleo y DIY
- **Precio irreal**: "$50 towing", "$40 tow". En el brief, stuck.solutions publica "$50 towing in Salt Lake City".
- **Competidores locales por nombre**: es el desperdicio recurrente más grande en cuentas con amplia. La lista la arma `/competitors` (`competitors.md`). Los primeros candidatos del brief son Adams, Stauffer's, Cheap Towing Salt Lake, Taylorsville Towing, Shamrock, Speedy, Quick Tow y Bullock's.
- **Fuera del área**: ciudades y ZIP de Utah fuera de los que confirme el cliente. Ojo: en el brief, 84104, donde está la base, no está en la lista. Con frase y Presencia el riesgo baja, pero no desaparece.
- **Según lo que confirme el cliente**:
  - heavy duty, semi y 18 wheeler (con una F550 no aplica)
  - motorcycle towing
  - long distance
  - **No** negativizar lockout, jump, fuel ni tire change si se queda con roadside. En el MCC son servicios válidos; se negativizan solo si el cliente los excluye.
- **Español**: negativizar los términos en español si no hay ad group ES. Según el consolidado, fuera de los mercados hispanos gasta sin convertir. En esta extracción, las keywords en español de una cuenta nueva de Minneapolis gastaron $91 con 2 conversiones.
- **No negativizar** cheap, affordable, price ni cost como palabra suelta. En el consolidado convierten igual que el genérico.

## Historial propio del cliente
No hay. La cuenta 730-795-5909 tiene 0 filas de gasto entre oct-2025 y oct-2026 (Windsor). No hay una cuenta anterior del cliente identificada en el MCC.

## Advertencias
- **Datos de Windsor.ai, no de la API**:
  - El paquete sale del nombre vigente de la cuenta, y algunos nombres cambiaron.
  - `bidding_strategy_type` y `budget_amount` son valores vigentes, no históricos (playbook §2).
  - El informe geo cubre solo una parte del gasto.
  - Windsor no expone geo (Presencia o interés), programación, extensiones, tope de CPC ni historial de cambios.
- **Conversión = llamada sin calificar.** En el consolidado, el ~86% son "Calls from Ads", con un umbral de duración que no se conoce. Si para A's Unasa la conversión primaria es una llamada de 60 s o más, **el CPL real va a ser más alto que todos estos rangos**. En CallFire el cliente tuvo 1 llamada calificada de 3 (n = 3, no es una tasa).
- **La cohorte nueva es chica**: 7 cuentas con un primer bloque completo de 30 días, y solo 3 cuentas llegan a M4–M7. Los rangos de meses 3–6 son orientativos.
- **El gasto al mes está normalizado por días con gasto.** Infla un poco el de las cuentas que pausan.
- **Calibración Semrush → CPC real**: es inferida (CPC de toda la cuenta contra el CPC de una keyword de ciudad), con 6 metros maduros y 3 nuevos.
- **Español en Salt Lake City / West Valley**: no hay datos de demanda en español en el brief ni en el MCC para Utah. No copiar el modelo de D sin evidencia (Semrush en español o lo que diga el cliente).
- **Sin etiquetas `nicho:`/`pais:` en el MCC**: las cuentas se identificaron por nombre. Conviene etiquetarlas.
- No sé cuáles de estas cuentas son de compañeros (playbook §10). El benchmark las usa solo en agregado y anonimizadas.

**Siguiente**: `/strategy`. Antes hacen falta las respuestas del cliente sobre ticket, horario y área (brief) y `competitors.md`.
