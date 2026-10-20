---
cliente: Electrical Service Solutions
slug: electrical-service-solutions
nicho: electricista (solo paneles eléctricos)
pais: US
cuentas_comparables: 5 (3 electricistas + 1 HVAC + 1 plomería como nicho afín)
periodo: 90d (2026-07-22 → 2026-10-19)
actualizado: 2026-10-20
---

# Benchmark interno — Electrical Service Solutions

Fuente: Windsor.ai (`google_ads`), sin la API. El MCC no tiene etiquetas `nicho:*`; las cuentas se filtraron por nombre. En el conector solo quedan **3 electricistas con datos**, así que amplié a dos nichos afines de servicios para el hogar (HVAC y plomería). Las métricas son **solo de campañas Search**: el PMax de A y el Display de E van aparte. Crudo: `knowledge/benchmarks/raw/electrician-us-2026-10-20.json`.

| Cuenta | Nicho / mercado | Puja | Gasto 90d | Clics | CPC | CTR | Tasa conv. | Conv. | CPL | Conv./mes | CPL sin marca |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | Electricista, mercado chico (CO) | Max. conversiones, tCPA $20 | $964.15 | 184 | $5.24 | 5.7% | 28.9% | 53.1 | **$18.14** | 18.0 | $21.24 |
| B | Electricista, mercado caro (CA) | Max. clics | $3,951.20 | 486 | $8.13 | 4.2% | 1.6% | 8 | $493.90 | 2.7 | $493.90 |
| C | Electricista, mercado medio (AR), gasta desde el 11-sep | Max. clics | $1,160.60 | 107 | $10.85 | 3.2% | 1.9% | 2 | $580.30 | ~1.5 | $580.30 |
| D | HVAC, mercado chico (SC), nicho afín | Max. conversiones | $1,125.95 | 90 | $12.51 | 6.9% | 36.7% | 33 | **$34.12** | 11.1 | $85.61 (18 clics) |
| E | Plomería, mercado chico (AZ), nicho afín | Max. clics | $839.51 | 120 | $7.00 | 4.3% | 8.3% | 10 | $83.95 | 3.4 | $98.61 |
| **ESS** | 384-080-6970 | — | $0 | 0 | — | — | — | — | — | — | — |

## Rangos esperados para este nicho/país
| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $7.00 | $8.13 | $10.85 |
| CTR | 4.2% | 4.3% | 5.7% |
| Tasa conv. | 1.9% | 8.3% | 28.9% |
| CPL | $34.12 | $83.95 | $493.90 |
| Conv./mes | 2.7 | 3.4 | 11.1 |

En el CPL, el P25 es el mejor cuartil. Solo las 3 electricistas: CPC $6.69 / $8.13 / $9.49 y CPL $256 / $494 / $537, con 2 de las 3 en Max. clics.

**La distribución vuelve a ser bimodal**, como en septiembre:
- **Max. conversiones** (A, D): tasa de conversión de 29–37%, CPL de $18–34 y 11–18 conv./mes. Las dos tienen historial largo y **marca propia**: en D, la marca hace 29 de las 33 conversiones.
- **Max. clics** (B, C, E): tasa de conversión de 1.6–8.3%, CPL de $84–580 y 1.5–3.4 conv./mes.
- La mediana ($83.95) es la de E, la plomería. No es una cuenta de electricista.

**CPL objetivo inicial sugerido**: con la regla de la mediana ±20% sale **$67–101**. Ese rango pide ≥10% de conversión a CPC ≤$10, y ESS arranca en Max. clics con tope (estándar 6), sin marca y en un nicho más estrecho. Propongo **$100–150 por conversión** (llamada ≥60 s o formulario) para la fase 1, y $280 como techo de alarma (el escenario pesimista). Hay que contrastarlo con el CPL máximo cuando tengamos ticket, margen y tasa de cierre (PENDIENTE en el brief). Un upgrade de panel es un trabajo de ticket alto, así que el CPL aceptable probablemente quede por encima de este rango.

**Con presupuesto de $1,293.75/mes** ($42.56/día): ~92–129 clics/mes y **~5–15 conversiones/mes**, ~9 en el escenario base → **tCPA no alcanzable** con esta pauta (≥30 conv. en 30 días pediría $3,000–4,500/mes al CPL objetivo).

| Escenario | CPC | Clics/mes | Tasa conv. | Conv./mes | CPL |
|---|---|---|---|---|---|
| Pesimista | $14 (Semrush, paneles US) | 92 | 5% | 4.6 | $280 |
| Base | $12 | 108 | 8% (mediana del benchmark) | 8.6 | $150 |
| Optimista | $10 | 129 | 12% | 15.5 | $83 |

- **Umbral de Max. conversiones (15/mes, playbook §5)**: solo se cruza en el escenario optimista. En el base se queda en Max. clics con tope de CPC hasta juntar 15+ conversiones/mes estables y limpias. Para 15/mes con un CPL de $100–150 harían falta **$1,500–2,250/mes** de pauta.
- **El riesgo más grande es no llegar a gastar el presupuesto, no quedarse corto.** Ver "Paneles en el MCC": las keywords de paneles en cuentas con más geografía imprimen ~5 veces al día. Antes de fijar la pauta y el tope, hay que sacar el volumen real de los 4 ZIP + Monroeville en Keyword Planner (pendiente del brief).
- Límite de fragmentación ($600–1,500): 1 campaña y 3–5 grupos, con 1 RSA por grupo (estándar 4).

## Paneles en el MCC
El cliente solo vende paneles, así que busqué en las 3 cuentas de electricistas toda keyword o search term con panel, breaker, fuse, amp/servicio, meter, service upgrade/change, rewire o commercial (90 días).

**Keywords de paneles con impresiones** (todas en phrase o exact, salvo una):
| Cuenta | Keywords | Impr. | Clics | Gasto | Conv. |
|---|---|---|---|---|---|
| C: grupo "Electrical Panel Upgrade", desde el 23-sep (27 días) | panel upgrade, electrical panel replacement (cost), electrical service upgrade, breaker box replacement, fuse box replacement, electric panel installation | 134 | 6 | $50.82 | 0 |
| C: "breaker replacement" y "circuit breaker replacement" (grupo de reparación) | 2 | 51 | 0 | $0 | 0 |
| B: dentro del grupo genérico | electrical panel upgrade (cost), electrical panel replacement, circuit breaker repair | 158 | 4 | $26.30 | 0 |
| **Total** | | **343** | **10** | **$77.12** | **0** |

Lo más caro fue "electrical panel replacement cost": $37.86 en 4 clics. Es una búsqueda de precio.

**Search terms de paneles** (en su mayoría los disparó el broad genérico de B, no keywords de panel):
| Tipo | Impr. | Clics | Gasto | Conv. | Ejemplos |
|---|---|---|---|---|---|
| Intención de servicio | 242 | 7 | $51.00 | 2* | "electrical panel", "200 amps panel", "main breaker panel 400 amp", "house fuse panel", "breaker box upgrade" (0 clics) |
| Precio / información | 124 | 8 | $67.74 | 0 | "cost to replace an electrical panel", "upgrading electrical panel cost", "how much is a breaker box for a house", "should i upgrade to 200 amp service" |
| Marca o modelo del panel | 58 | 2 | $12.56 | 0 | "zinsco panel", "sylvania electrical panel", "span panel", "federal pacific…" |
| Comercial | 26 | 0 | $0 | 0 | "commercial electrician (near me)", "commercial electrical contractors" |
| Breaker suelto / DIY / rewire (fuera del alcance) | — | 14 | $101.14 | 0 | "what does a tripped breaker look like", "wire for 40 amp breaker", "circuit breaker numbering system", "cost to rewire a house" |

\* Las 2 conversiones salen de **1 clic** ("circuit breaker box", $8.38). No es una tasa.

Lectura:
- **El volumen es ruido**: 17 clics de paneles, $131.30 y 2 conversiones en 90 días, sumando 3 cuentas. Con menos de 50 clics no se puede concluir nada sobre la tasa de conversión de paneles (playbook §9). Lo único que sí se lee es el **CPC real de los clics de panel: ~$7.72** (CA y AR), por debajo de los $8–18 de Semrush. El CPC de Pittsburgh no se observa en ninguna cuenta.
- **La demanda de paneles que capturamos es muy chica**: 424 impresiones de search terms de panel en 90 días entre las 3 cuentas, y ~5 impresiones al día en el grupo de C. Ninguna de esas cuentas estaba concentrada en paneles, porque el broad genérico se llevaba el presupuesto, pero la señal es clara. Con una geo mucho más chica que NWA, ESS puede tener menos búsquedas de las que su pauta paga.
- **La mitad del gasto en paneles fue de precio o información** ($67.74 de $131.30, 0 conversiones). /strategy decide si "cost / how much" va como negativa o a un tope bajo: en un nicho de ticket alto, quien pregunta el precio puede estar comprando, pero sin una sola conversión que lo respalde no se puja por él.
- **El comercial no tiene datos**: 26 impresiones y 0 clics. Ninguna cuenta del MCC tiene un grupo comercial. El grupo comercial de ESS sale de Semrush, no del benchmark.
- **Patrón a evitar**: en B, las keywords de panel conviven en un solo grupo con "home electrical" ($1,262.97) y EV ($589.64), y el presupuesto se va a lo genérico. En ESS los paneles son todo el alcance, así que esto no aplica tal cual, pero confirma por qué cada tema va en su propio grupo, con phrase.

## Lo que hacen las cuentas que mejor rinden (A y D)
- **Estructura**: 1 campaña Search Radius con 1–2 grupos (A: 1 grupo; D: "HVAC Contractor" y "Heating Contractor"). Pauta real de $325–380/mes en Search.
- **Puja**: Max. conversiones. A tiene tCPA $20 (valor vigente; Windsor no da la fecha) y ~16 conv./mes en Search (jul 16, ago 25, sep 16.5): tCPA con historial, consistente con el playbook. D, sin tCPA.
- **Marca propia**: A, 11 de 53 conversiones a ~$6.27; D, 29 de 33 a ~$27. **ESS no tiene demanda de marca** (brief: 20 búsquedas/mes, frase genérica), así que su referencia es el CPL sin marca: A $21.24 y D $85.61 (este último sobre 18 clics, ruido).
- **Keywords**: genéricas de intención ("electricians", "electrician near me"), oficio + ciudad y marca. Ninguna puja por paneles.
- **Match types**: casi todo broad, con algunas ciudades en phrase. Funciona por Max. conversiones con historial en mercados chicos; **choca con el estándar PMM (phrase)** y no es modelo para ESS.
- **Conversiones**: A mide "Calls from ads" (47) + "Website Calls" (6). D solo cuenta "Calls from ads"; tiene 13 "Website Calls" fuera de la columna de conversiones. B mide formulario (5) + llamadas del sitio (3) y 0 "Calls from ads". ESS necesita las tres: llamada desde el anuncio, llamada al CTN (412) 666-9290 desde la web y formulario.
- **Geo**: radio. Presencia vs. interés, programación y extensiones no se leen en Windsor.
- **Cuota de impresiones**: A 38.9% (29.6% perdido por presupuesto); D 21.9% (58.9% perdido por ranking). Ninguna satura su mercado.

## Keywords que más convierten en el nicho (agregado)
| Keyword | Cuentas | Match | Conv. | Gasto | CPL |
|---|---|---|---|---|---|
| marca propia | A, D, E | broad/phrase | 42 | $903.12 | $21.50 (no aplica a ESS) |
| electricians | A | broad | 19.3 | $380.22 | $19.68 |
| electrician near me | A (B: 0 conv. en $205) | broad/exact | 11.5 | $492.48 | $42.82 |
| electricista + ciudad | A, C | phrase/broad | 8 | $453 | $57 (A $19.56; C $316) |
| home electrical | B | broad | 4 | $1,262.97 | $315.74 |
| air conditioner (HVAC) | D | broad | 4 | $329.37 | $82.34 |
| electrical services | B, C | broad | 3 | $890.17 | $296.72 |
| keywords de paneles | B, C | phrase/exact | 0 | $77.12 | — |

Sin conversiones o con CPL alto en B (Max. clics): "ev charger installation near me" ($391.72, 1 conv.), "emergency electrician" ($487.23, 1 conv.), "ceiling fan installation near me" + "electrician ceiling fan installation" ($269.09, 0), "home ev charger installer" ($197.92, 0), "electrical repairs" ($118.04, 0). Para ESS todo eso es negativa.

## Negativas frecuentes del nicho
Salen de los search terms de A, B y C y de la lista PMM. Para ESS hay que sumarles todo lo que no sea panel:
- **Competidores por nombre**: en B, ~25 nombres distintos (baker, chambers, epic, united, faraday, macgray…); en A, rocky mountain, buzz, blazer, ec electric, o dwyers. Ojo: en A, los nombres de competidores "convierten" (blazer 2, ec electric 2, o dwyers 1). Son llamadas de gente que buscaba a otro, no leads.
- **Empresas de energía**: carroll electric, ozarks electric, bentonville electric (C). En Pittsburgh el equivalente es **Duquesne Light** (verificar en los search terms).
- **Producto, marca y modelo**: tesla charger / wall connector, juicebox, nema 14 50, harbor breeze / hampton bay / minka aire, eaton outlets, "qpf2", "dp 4075". Para ESS: **marcas de panel como producto** (zinsco, sylvania, span, leviton, federal pacific, challenger, square d), salvo que vayan con replace/upgrade, y "breaker for ev charger".
- **DIY e información**: "what does a tripped breaker look like", "circuit breaker numbering system", "wire for 40 amp breaker", "subpanel wiring", "breaker panel setting to save electricity", "wiring", "how to", "diagram".
- **Fuera de alcance para ESS**: ev / charger / tesla, ceiling fan, lighting, outlet, gfci, switch, rewire, troubleshooting, generator, handyman, "low cost", "hourly rate", empleo ("journeyman").

## Historial propio del cliente
**No existe.** La cuenta 384-080-6970 está en el conector de Windsor con **0 filas** en este periodo (y en los últimos 2 años, según el brief): sin campañas, sin impresiones, sin gasto. No hay CPL histórico. El tCPA, cuando llegue, tiene que salir del CPA que se observe en ESS, no de este benchmark (playbook §5).

## Advertencias
- **Pocas cuentas y nicho afín**: 3 electricistas con datos (las otras 2 de la extracción de septiembre ya no están en el conector) + 1 HVAC + 1 plomería. Los percentiles son orientativos. Excluidas: ESS (vacía) y la HVAC 244-642-6584 (en pausa, $0 en 90 días).
- **Ninguna comparable vende solo paneles, ni está en Pennsylvania o en el Noreste.** El CPC y el volumen de Pittsburgh no se observan en el MCC: salen de Semrush y quedan por confirmar con Keyword Planner con la geo exacta.
- **Paneles con <50 clics**: 17 clics de search terms y 10 de keywords en 90 días. Cualquier tasa de conversión de paneles es ruido.
- C tiene 39 días de gasto y reestructuró la cuenta el 23-sep. Su CPL es un diagnóstico de configuración, no un rendimiento maduro.
- `budget_amount` y `target_cpa` son valores vigentes, no históricos. Lo visible en Windsor como search terms es solo parte del gasto: los porcentajes de paneles son sobre el gasto rastreable.
- "Conversión" = llamada desde el anuncio o el sitio (duración mínima de cada cuenta) o formulario. **No es un lead calificado de panel.** El costo por trabajo vendido será más alto; se mide con CallFire (calificada = ≥60 s, llamante único).
- Datos de Windsor y no de la API: sin presencia vs. interés, extensiones ni programación.
- Proponer etiquetas `nicho:electrician` y `pais:US` en el MCC para 324-020-3548, 436-679-0497, 758-301-1023 y 384-080-6970.
