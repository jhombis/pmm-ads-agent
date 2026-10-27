---
cliente: Tuff Truck Towing
slug: tuff-truck-towing
nicho: towing
pais: US
cuentas_comparables: 31 (21 maduras + 10 con menos de 90 días) · 1 en Oklahoma
periodo: 90d
actualizado: 2026-10-27
---

# Benchmark interno — Tuff Truck Towing

Fuentes:
- **Rangos generales**: `knowledge/benchmarks/towing-us.md` (consolidado del 2026-10-01, 7 extracciones de Windsor, tiene menos de 90 días).
- **Refresh liviano de esta sesión**: una sola llamada a Windsor (`google_ads`), nivel cuenta por tipo de campaña, del 2026-07-29 al 2026-10-26. Cubre 36 cuentas de towing/roadside del MCC; 31 tuvieron gasto con 50 clics o más. Display queda fuera del cálculo.
- **Oklahoma**: cuenta de OKC del MCC (425-405-2574).
- **Equipment / medium-duty**: search terms y keywords de 12 meses (2025-10-27 → 2026-10-26) de las 36 cuentas. Crudo en `knowledge/benchmarks/raw/towing-us-2026-10-27-equipment-terms.json`.

Esta sesión no tiene credenciales de la Google Ads API. Una cuenta es "nueva" cuando su gasto de Search en 12 meses es menor que 1,1 × su gasto en 90 días, es decir, cuando arrancó dentro de la ventana. Con esa regla hay 10 cuentas nuevas.

## Rangos esperados para este nicho/país

**Solo Search**, que es lo que va a lanzar Tuff Truck (PMax no va al inicio, estándar #9):

| Métrica | P25 | Mediana | P75 | Consolidado 10-01 (mediana) |
|---|---|---|---|---|
| CPC (todas, n=30) | $5.29 | $7.22 | $8.62 | $5.14–7.02 |
| CTR (todas) | 7.1% | 8.7% | 10.2% | — |
| Tasa conv. (todas) | 17.0% | 25.8% | 38.3% | 26% |
| CPL (todas) | $13.99 | **$33.01** | $51.67 | **$25.98–31.91** |
| CPL (maduras, n=20) | $12.48 | $15.10 | $36.27 | — |
| CPL (nuevas, <90 días, n=10) | $44.84 | **$51.34** | $69.58 | cohorte nueva $51–63 |
| CPC (nuevas) | $6.52 | $8.24 | $9.94 | $7.3–7.6 |
| Tasa conv. (nuevas) | 14.2% | 15.5% | 21.6% | 14–19% |
| Conv./mes (maduras) | 16 | 25 | 37 | — |

**Nivel cuenta (Search + PMax), maduras (n=21)**:
- CPC $4.39 / $5.41 / $6.47
- CTR 5.3% / 7.6% / 8.8%
- Tasa de conversión 21.8% / 32.8% / 37.7%
- **CPL $12.23 / $16.10 / $26.01**
- 24 / 47 / 54 conversiones al mes
- Gasto real de $424 / $740 / $1,071 al mes

Coincide con el consolidado: CPL $14.59–16.01 y gasto de $680–728 en la mediana.

**Qué se movió en el refresh.** La mediana de Search subió de $26–32 a $33. La razón es que hoy un tercio de la muestra (10 de 30) son cuentas con menos de 90 días, con una mediana de $51. Las maduras siguen igual. El rango del consolidado se mantiene.

"Conversión" aquí es casi siempre "Calls from Ads", sin calificar (ver Advertencias).

**CPL objetivo inicial sugerido**: la mediana de Solo Search de las dos extracciones ($26–33) ±20% → **$21–40**. Ese número va a `strategy.md` como meta a partir del mes 3.
- **Meses 1–2**: lo esperable es la cohorte nueva, con **~$51** (P25 $45, P75 $70). No hay que juzgar la cuenta contra el rango anterior antes del día 60.
- **Meta a 6 meses**: la mediana de Search madura, **~$15**.
- **El CPL máximo aceptable sigue PENDIENTE.** Sale del ticket y el margen por línea (brief). El benchmark es una referencia y no reemplaza esa cuenta.

**Escenarios de presupuesto**. El presupuesto está PENDIENTE; los montos son de pauta, sin fee.

| Pauta/mes | $400 | $700 | $1,000 |
|---|---|---|---|
| Diario (÷30.4) | $13.2 | $23.0 | $32.9 |
| Clics/día (CPC de $6.15 madura a $8.24 nueva) | 1.6–2.1 | 2.8–3.7 | 4.0–5.3 |
| Conv./mes, meses 1–2 (CPL nueva $51; P75 $70) | ~8 (6) | ~14 (10) | ~19 (14) |
| Conv./mes, mes 3+ (CPL $26–33) | 12–15 | 21–27 | 30–38 |
| Conv./mes, cuenta madura (CPL $15) | ~26 | ~46 | ~66 |
| Límite de fragmentación (playbook §4) | 1 campaña, 2–3 grupos | 1 campaña, 3–5 grupos | 1 campaña, 3–5 grupos |
| tCPA (~30 conv/30 días) | no se alcanza | no antes del mes 4–6 | apenas, desde el mes 3, en el escenario medio |
| Max. clics → Max. conv. (15+ conv/mes, §5) | ~mes 3, si llega | mes 2–3 | mes 2 |

Cómo leer la tabla:
- **$400** queda por debajo del piso de bajo volumen del playbook (3 clics/día). Es una cuenta de muy pocos datos: no se puede separar equipment hauling en su propio grupo con presupuesto propio, y cualquier tasa de conversión de los primeros 90 días será ruido.
- **$700** está en la mediana del gasto real del nicho ($740 en las cuentas maduras). Es el mínimo razonable para towing + un grupo de equipment.
- **$1,000** permite salir de aprendizaje con holgura.

Hay tres razones para esperar menos que la tabla:
1. **El horario es lun–vie 7–21**: 70 de 168 horas semanales (42%). La demanda de towing de noche y en fin de semana se pierde.
2. **La geo es recortada**: Tulsa solo al este de Memorial.
3. **Si la conversión principal es una llamada de 60 s o más**, el volumen baja frente a "Calls from Ads".

Con esas tres cosas, el escenario de $1,000 probablemente no llega a 30 conversiones calificadas en 30 días antes del mes 4.

## Lo que hacen las cuentas que mejor rinden
Fuente: `towing-us.md`, cuartil superior con CPL de $8–13. El refresh no vuelve a sacar la estructura.
- **Estructura**: una campaña Search de radio con 1–2 ad groups consolidados y 5–16 keywords. Dos o tres términos hacen el 80% del volumen. Ninguna usa SKAG.
- **Mejores Search maduras del refresh**: CPL de $10.8–12.6, CPC de $2.55–6.21 y tasa de conversión del 24–52%, con un gasto de $180 a $1,150 al mes. **Con pocas keywords y presupuesto modesto se llega a un CPL de $11–13.**
- **Puja**: Maximizar conversiones sin tCPA en todas las cuentas top. Las cuentas que se quedaron en Maximizar clics tienen un CPL de $70–83.
  - Para Tuff Truck aplica el playbook §5: Max. clics **con tope de CPC** solo mientras haya menos de 15 conv/mes, y pasar a Max. conversiones apenas se cumpla la condición.
  - El tope de CPC se fija con el CPC de nuevas ($8.24) como referencia, no con el de Semrush ($3.35–4.59).
- **Geo**: Presencia en todas las Search top. "Presencia o interés" solo aparece en campañas PMax o heavy-duty.
- **Match**: el MCC está casi todo en amplia, y amplia no rinde mejor. El 23% del gasto Search se fue en términos con 0 conversiones. Para Tuff Truck: **frase por defecto** (estándar #2), por control y no porque baje el CPL.
- **Keywords de ciudad** ("tow truck / towing + ciudad"): CPL de ~$8. Con Broken Arrow, Bixby, Coweta, Catoosa y "east tulsa" son el núcleo natural.
- **Impression share**: mediana del 26%, sin saturación. Más presupuesto escala casi linealmente.
- No se ve en Windsor: programación, extensiones y geo exacta. Hay que verificarlo por API cuando haya credenciales.

## Keywords que más convierten en el nicho (agregado)
Fuente: `towing-us.md`, 27 cuentas, 90 días.

| Keyword | Conv. | CPL | Uso para Tuff Truck |
|---|---|---|---|
| towing near me | 775–790 | $11–17.66 | núcleo (frase) |
| tow truck near me | 155–173 | $9–18 | núcleo |
| tow truck / towing + ciudad | ~90 | ~$8 | BA, Bixby, Coweta, Catoosa, "tulsa" con geo recortada |
| towing company near me | 25–40 | $13–16.5 | núcleo |
| cheap towing / cheap tow truck near me | 25–36 | $8–18.5 | **no negativizar "cheap"** |
| towing service / tow truck service | 13–24 | $4.6–34.6 | núcleo |
| marca propia (exacta) | 95–107 | $8.5–14 | marca con 90 búsquedas/mes: no justifica campaña aparte (brief) |
| roadside assistance | 75–76 | $11–28.60 | **ojo**: en amplia sale a $67–154. Solo si el cliente hace roadside (la home lo lista) y en frase |

No hay keywords de equipment, forklift ni contenedores con volumen en el MCC (ver la sección de equipment más abajo).

## Negativas frecuentes del nicho
Detalle por tema en `towing-us.md`. Para Tuff Truck aplican:
- **Siempre**:
  - aseguradoras y motor clubs (AAA, Geico, State Farm…)
  - "phone number"
  - jump starter, battery pack y otros productos
  - junk, cash for cars, salvage
  - impound, repo, "car was towed"
  - renta (u haul, penske, ryder)
  - talleres, empleo y DIY
  - informacionales ("average tow cost")
  - precios irreales ("$40 towing")
- **Competidores locales por nombre**, una lista por cuenta. Del brief: Tow Tulsa, Speedy's, Tow N Go, Storey Wrecker, BA Towing.
- **Fuera del área**: Tulsa oeste y sur (según Bree), Owasso, Sand Springs, Sapulpa, Jenks si queda fuera, OKC y otros estados.
- **Heavy-duty**: "semi", "18 wheeler", "heavy wrecker", "tractor trailer", salvo que el cliente diga que lo hace (brief). En el MCC es el tema "pesado" con más gasto (abajo).
- **Para equipment hauling**, del crudo de 12 meses: "car hauler", "car hauling", "rv hauler", "trailer rental", "for rent", "for sale", "hitch", "trailer repair", "gooseneck", "uhaul", "hot shot", "load board" y "dispatch" (brief: posibles brokers).
  - Ojo: "trailer" a secas **no** se negativiza si el cliente remolca trailers (`towing-us.md`).
- **Con conflicto con servicios del cliente**: "flatbed equipment" está en la lista de negativas del nicho, pero para Tuff Truck puede ser una búsqueda válida de traslado de equipo. **No se aplica**; se revisa en los search terms.
- **Roadside** (fuel, lockout, jump, tires): la home lo ofrece, así que **no se negativiza** hasta confirmar con el cliente.

## Historial propio del cliente
**No hay cuenta en el MCC.**
- Windsor tiene 64 cuentas de Google Ads y ninguna es de Tuff Truck.
- El tag AW-1004387232 de la web es de una cuenta fuera del MCC: se ignora, y su dueño está PENDIENTE en el brief.
- Semrush no le ve anuncios pagados.

No hay contra qué comparar. La primera lectura propia llega en `/weekly-review` día 14–30.

**CallFire** (20–26 oct, sin Ads) da la base orgánica que hay que restar después: ~6 llamadas/día y 13 calificadas en 7 días.

## Mercado Oklahoma: la cuenta comparable más cercana
Es la única cuenta del MCC en Oklahoma: OKC metro, 24/7, cuenta 425-405-2574, activa desde el 2026-09-15. Configuración:
- 1 campaña Search ("ENHPRM Radius"), 1 ad group ("Ad group 1") y unas 40 keywords, **todas en amplia**.
- Puja: **Maximizar conversiones**. No usa PMax.
- Conversiones: "Calls from Ads" + "Form Fill".
- Según su `strategy.md` y su log del 01-oct, la reestructura y las 238 negativas propuestas estaban **sin aplicar** a esa fecha.

| Periodo | Gasto | Clics | Impr. | CPC | CTR | Tasa conv. | Conv. | CPL | Search IS | IS perdido presup. / ranking |
|---|---|---|---|---|---|---|---|---|---|---|
| Sep (15–30, 16 días) | $648.85 | 94 | 1,689 | $6.90 | 5.6% | 8.5% | 8 (7 llamadas + 1 form) | $81.11 | 17.3% | 20% / 63% |
| Oct (1–26) | $1,226.48 | 127 | 1,904 | $9.66 | 6.7% | 22.8% | 29 (26 llamadas + 3 form) | $42.29 | 24.5% | 33% / 43% |
| **Total 42 días** | **$1,875.33** | **221** | **3,593** | **$8.49** | **6.2%** | **16.7%** | **37** | **$50.68** | — | — |

Lectura para Tuff Truck:
- **El CPC real de towing en Oklahoma ronda los $7–10 en una cuenta nueva**, el doble de lo que dice Semrush para Tulsa ($3.35–4.59). Para el presupuesto hay que planificar con $8–8.5 y no con Semrush.
- **La curva de una cuenta nueva en OK es la de la cohorte del MCC.** El CPL bajó de $81 en el mes 1 a $42 en el mes 2, y en octubre lleva un ritmo de ~33 conversiones cada 30 días con ~$47/día (~$1,430/mes).
  - El total de 42 días ($50.68) cae justo en la mediana de cuentas nuevas ($51.34).
  - El volumen es parcial (127 clics en octubre). Las conversiones son llamadas sin umbral de duración verificado.
- Por keyword (42 días):
  - "towing near me": $868.24, 104 clics, 15 conv. (CPL $57.88)
  - "roadside assistance": $373.12, 47 clics, 6 conv. ($62.19)
  - "tow truck near me": $78.04, 3 conv.
  - "cheap towing near me": $52.54, 2 conv.

  Todas tienen menos de 50 clics salvo "towing near me", así que **por keyword es ruido**. Lo único que se puede afirmar es que "towing near me" concentra el 46% del gasto.
- **No es un comparable 1:1.** OKC es un metro más grande, la cuenta es 24/7, usa amplia y tiene un paquete de $2,250. Tuff Truck trabaja en horario comercial, con geo recortada y frase. Sirve para el CPC y para la curva de aprendizaje, no para el volumen.
- En un informe para el cliente, esta cuenta va anonimizada ("cuenta de towing en Oklahoma City del MCC").

## Equipment, forklift, contenedores y medium-duty: ¿hay demanda que convierte en el MCC?
Search terms de 12 meses (2025-10-27 → 2026-10-26) en las 36 cuentas de towing, que en ese periodo gastaron **$145,482 en Search**. El filtro buscó términos con equipment, forklift, skid, bobcat, excavator, backhoe, tractor, machine, container, conex, lumber, medium, box truck, heavy, semi, 18 wheel, haul, flatbed transport o trailer. Salieron **601 términos, 985 impresiones, 62 clics, $339.83 y 17 conversiones**: el 0.23% del gasto Search.

| Tema | Términos | Impr. | Clics | Gasto | Conv. | CPC | Cuentas |
|---|---|---|---|---|---|---|---|
| **Equipo / maquinaria** (heavy equipment towing/hauling/movers, farm equipment, machinery moving, skid steer…) | 40 | 64 | 7 | $37.14 | 4 | $5.31 | 8 |
| **Forklift** | 4 | 5 | 1 | $3.09 | 1 | $3.09 | 3 |
| **Contenedores** (container, conex) | 1 | 2 | 1 | $4.54 | 0 | $4.54 | 1 |
| **Madera (lumber)** | 0 | 0 | 0 | $0 | 0 | — | 0 |
| **Medium-duty / box truck** | 27 | 41 | 2 | $9.17 | 0 | $4.58 | 17 |
| **Subtotal de los servicios de Tuff Truck** | **72** | **112** | **11** | **$53.95** | **5** | $4.90 | 18 |
| Heavy-duty / semi (que Tuff Truck no ofrece) | 219 | 437 | 31 | $177.09 | 9 | $5.71 | 25 |
| Remolque de trailers / RV | 156 | 215 | 7 | $34.01 | 2 | $4.86 | 29 |
| Ruido: compra, renta o reparación de trailers, car hauler, uhaul | 106 | 155 | 13 | $74.79 | 1 | $5.75 | 25 |
| "hauling" genérico (nombres de empresas, tow haul) | 43 | 56 | 0 | $0 | 0 | — | 16 |

**Lectura: no es ruido comprobado ni demanda comprobada. Es un tema no probado.**
- **11 clics en 12 meses es ruido** (playbook §9). Las 5 conversiones (CPL aparente de ~$11) no se pueden usar para nada. Los términos que convirtieron fueron:
  - "equipment hauling near me"
  - "equipment towing near me"
  - "heavy equipment towing near me"
  - "farm equipment haulers"
  - "forklift towing near me"
- **Casi nadie en el MCC puja por estos temas**, y por eso el volumen es tan bajo. Solo dos cuentas tienen keywords de ese tipo:
  - una campaña "heavy" de radio, con la única keyword de equipment del MCC: "heavy equipment hauling" en amplia ($4.86, 1 clic, 1 conversión en 12 meses);
  - un ad group "Heavy Duty/Semi".

  Lo que se ve son búsquedas que entraron por amplia desde keywords genéricas. Además, Google oculta los términos de bajo volumen y Windsor cubre solo parte del gasto (playbook §2). Por eso el dato no mide la demanda real.
- **Las cuentas que sí pujaron por heavy dan una señal mala, aunque con poco volumen:**
  - El ad group dedicado Heavy Duty/Semi de una cuenta (12 keywords en amplia + exacta) lleva **$303.78, 44 clics, 973 impresiones y 4 conversiones en 12 meses: CPL ~$76 y conversión del 9%**. Es menos de 50 clics, así que es indicio y no conclusión. Aun así, es 5 veces el CPL de towing liviano en la misma cuenta.
  - La otra cuenta tiene una campaña "Heavy Radius" con $1,298 y 103 conversiones en keywords "heavy towing" (amplia). Pero en sus search terms solo ~$46 llevan palabras heavy, semi o equipment, así que la amplia sirvió sobre todo búsquedas genéricas de towing. **Ese CPL de $12.6 no es el de heavy ni el de equipment.**
- **Medium-duty y box truck**: 41 impresiones y 2 clics en 17 cuentas. La demanda existe pero es mínima. Semrush da 110 búsquedas/mes nacionales para "medium duty towing near me". **Va dentro del ad group de towing** como variante en frase ("medium duty towing", "box truck towing"), no como grupo propio.
- **Contenedores y madera**: no hay datos en el MCC (0–2 impresiones) ni en Semrush. **No hay base para pautarlos al inicio.** Si el cliente insiste, se agregan como keywords en frase dentro del grupo de equipment, y se miran los search terms.
- **La demanda externa existe y es más cara**, con volumen nacional de Semrush:
  - "equipment hauling near me": 720/mes a $4.78
  - "forklift towing": 210 a $5.31
  - "forklift transport near me": 50 a $6.27
  - "machinery moving tulsa": 70

  La parte de Tulsa este y Broken Arrow será una fracción de eso. Antes de decidir hay que validar con Keyword Planner geolocalizado.

**Qué hacer con esto en `/strategy`:**
1. Equipment, forklift y maquinaria van como **un ad group de prueba** dentro de la única campaña, en frase, con landing propia (la que pide `audit-site.md`). Solo en los escenarios de $700 o más.
2. Ese grupo se mide aparte (conversiones de llamada y formulario).
3. Se revisa a los 60–90 días, o al llegar a **≥50 clics**, lo que pase después.
4. Hasta entonces no se le asigna un CPL objetivo propio. Es un servicio planificado, a menudo B2B y de ticket alto (brief), y el CPL máximo sale del margen del cliente, no de este benchmark.
5. Heavy-duty, semi y 18 wheeler se negativizan.

## Advertencias
- **Windsor, no la API.** No hay etiquetas `nicho:`/`pais:`: las cuentas se identificaron por nombre. Hay que asumir que todas son de US.
- **Solo una cuenta comparable en Oklahoma**, y es de OKC, no de Tulsa: no hay ninguna en el MCC.
- **No hay cuentas de equipment hauling.** Las dos cuentas con "Hauling" en el nombre son de junk o demolición y quedaron fuera.
- **Las conversiones son llamadas sin calificar** ("Calls from Ads" ≈ 86% en el consolidado). La conversión de Tuff Truck debe ser una llamada de 60 s o más. Con eso, el CPL real por lead calificado queda **por encima** de estos rangos.
- **El refresh no normaliza por días activos.** Las 10 cuentas nuevas tienen menos de 90 días, así que sus conversiones por mes salen bajas. Por eso solo se citan sus CPL, CPC y tasa de conversión.
- **El refresh no vuelve a sacar** estructura, puja, keywords top ni negativas: se usó `towing-us.md` (01-oct, menos de 90 días). Esta sesión solo hizo 7 llamadas a Windsor.
- **Equipment**: 11 clics en 12 meses es una muestra demasiado chica para concluir. Los search terms cubren solo parte del gasto, y casi ninguna cuenta puja por esos temas.
- **CallFire ya recibe llamadas orgánicas** en el CTN (~6/día). Sin la conversión de llamada de Google (número de reenvío), Ads se confunde con lo orgánico y el CPL saldría artificialmente bajo.

**Siguiente**: `/competitors` (todavía no existe `competitors.md`) y después `/strategy`. Para que `/strategy` cierre la estructura y el CPL máximo, Jhombis necesita el presupuesto de pauta y el ticket por línea.
