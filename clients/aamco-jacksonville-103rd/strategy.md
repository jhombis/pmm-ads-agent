---
cliente: AAMCO Transmissions & Total Car Care — 103rd St (Jacksonville)
slug: aamco-jacksonville-103rd
actualizado: 2026-09-23
version: 1
modo: propuesta (no ejecutar en Ads sin aprobación de Jhombis)
supuestos:
  - CPL máximo del cliente PENDIENTE (falta ticket, margen y tasa de cierre). Se usa el benchmark CallRail ($26–38) como objetivo provisional
  - Servicio estrella = transmisión; servicio a evitar = oil change como fin (no confirmado por el cliente)
  - Garantía nacional, financiamiento y "free check" vigentes en esta sede (no confirmado)
  - Volumen por ad group estimado: Semrush US × 0.06% (radio 5 mi) y ciudad × 25%. Es conservador (hoy la campaña es elegible a ~18k impresiones/mes con amplia)
  - Landing auditada solo en parte (dominio bloqueado desde el entorno); sin PageSpeed
  - Presupuesto total igual al actual (Search $52.5 + PMax $16 = $68.5/día); fondos del ad pool de la franquicia
---

# Estrategia Google Ads — AAMCO 103rd St

## Resumen ejecutivo
1. **2 campañas Search** en lugar de la actual (1 campaña, 1 ad group, amplia) + PMax: **MARCA 103rd** ($8/día) y **NO-MARCA 103rd** ($60/día, 5 ad groups: 3 de transmisión, 1 general, 1 motor). Mismo presupuesto total que hoy (~$2,070/mes); el PMax se pausa y su presupuesto pasa a no-marca.
2. **Frase por defecto, exacta en los top términos, sin amplia.** Transmisión recibe prioridad por selección de keywords: oil change sale como objetivo y "auto shop near me" se excluye en F1.
3. **CPL objetivo provisional: $26–38 por llamada CallRail** (mediana del benchmark ±20%). Calificado probable: $45–65, a validar contra el CPL máximo del cliente.
4. **Nada se lanza sin Fase 0**: una sola conversión primaria (CallRail, primera llamada ≥ 60 s), página de gracias y form del subdominio arreglado. Sin eso, la reestructura se mediría con la misma señal inflada.
5. tCPA esperado **no antes del día ~45–60 desde el lanzamiento F1**, y solo si no-marca junta ≥30 conversiones limpias en 30 días.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| **MARCA 103rd** | Capturar búsquedas de la sede y defender marca | $8 | 12% | Cuota de impresiones objetivo 90% (parte superior), CPC máx. $4 | Radio 5 mi en 7532 103rd St, **Presencia** | L–V 8:00–17:30 ET (+30 min) |
| **NO-MARCA 103rd** | Llamadas de clientes nuevos, prioridad transmisión | $60 | 88% | Max Conversions **sin tCPA** (conversión: CallRail primera llamada ≥ 60 s + form) | Radio 5 mi, **Presencia** | L–V 8:00–18:00 ET |
| ~~PMax 103rd~~ | — | $0 (pausar) | — | — | — | — |
| ~~Search actual "ZETA Radius"~~ | — | se pausa el día que salen las nuevas | — | — | — | — |

- Red: solo Búsqueda (sin socios ni Display) en ambas. Rotación: optimizar. Recomendaciones automáticas: desactivadas.
- **Regla de aprendizaje (≥3× CPL/día)**: no-marca necesitaría $96/día con CPL de $32; con $60 llega a 1.9×. Por eso transmisión y general **no** se separan en campañas en F1: una sola campaña no-marca con más ad groups. Se separan en F3, cuando el presupuesto de transmisión sola alcance ≥ $96/día.
- Marca no usa Max Conversions a propósito. Sus "conversiones" incluyen clientes actuales llamando por su auto, así que optimizar hacia ellas es circular. Cuota de impresiones con tope de CPC la mantiene arriba y barata.
- La programación queda como hoy (5–15 PT = 8–18 ET), que ya está bien.

## Estructura por campaña

### Campaña: MARCA 103rd
| Ad group | Keywords (concordancia) | Vol. est./mes | Landing | H1 pinneado |
|---|---|---|---|---|
| Marca 103rd | [aamco 103rd], "aamco 103rd", "aamco on 103rd", "aamco 103rd street", "aamco westside", "aamco near me", [aamco], [aamco transmission], [aamco transmission near me], "aamco jacksonville" | ~60 (Semrush); ~70 clics/mes reales en marca hoy | `103rd.aamco-jacksonvillefl.com/` | AAMCO on 103rd Street |

Negativas específicas: otras sedes (biscayne, dunn ave, san jose, atlantic blvd, blanding, orange park, st augustine, st marys).
No excluir en marca: "reviews", "hours", "phone number". Son búsquedas de marca con intención; quien busca el horario suele ser cliente actual (ver riesgo 3).
**Coordinación entre sedes**: [aamco] y "aamco jacksonville" hoy los pujan 4 sedes. Propuesta para toda la cuenta: cada sede puja por su calle o barrio en frase, y [aamco] genérico solo por geo (sin solaparse). Decisión de cuenta: fuera del alcance de esta sede.

### Campaña: NO-MARCA 103rd
| Ad group | Keywords (concordancia) | Vol. est./mes | Landing | H1 pinneado |
|---|---|---|---|---|
| **A · Transmission Repair** | [transmission repair near me], [transmission shop near me], [transmission repair jacksonville fl], [transmission shop jacksonville fl], "transmission repair", "transmission shop", "transmission repair jacksonville", "transmission shop jacksonville", "transmission diagnostic", "transmission slipping", "car won't go in reverse", "car won't go into gear", "transmission leaking fluid", "transmission noise" | ~345 | `/service/automatic-transmissions/` (versión 103rd) | Transmission Repair on 103rd |
| **B · Transmission Rebuild** | [transmission rebuild near me], [transmission replacement near me], "transmission rebuild", "transmission replacement", "rebuilt transmission", "transmission repair cost", "transmission rebuild cost", "transmission financing" | ~20 (bajo; se mantiene por mensaje distinto: financiamiento) | **Nueva**: rebuild + financiamiento 103rd | Transmission Rebuild - 103rd |
| **C · Service, Clutch & Drivetrain** | [transmission service near me], "transmission fluid change", "transmission flush", "clutch repair", "clutch replacement", "cvt transmission repair", "differential repair", "transfer case repair", "4x4 repair" | ~45 | `/service/fluid-change-maintenance/`; clutch → `/service/manual-transmissions/` (URL por keyword) | Transmission Service - 103rd |
| **E · Auto Repair** | [auto repair shop near me], [car repair near me], "auto repair shop", "car repair jacksonville", "auto repair jacksonville", "auto mechanic near me", "car mechanic near me", "mechanic near me", "mechanic jacksonville" | ~900 (el más grande: controlar) | `/auto-service/` (versión 103rd) | Auto Repair on 103rd Street |
| **F · Check Engine & Engine** | [engine repair near me], "check engine light", "engine diagnostic", "car diagnostic", "engine repair", "overheating car repair" | ~65 | `/service/check-engine-light-service/` (versión 103rd) | Check Engine Light? 103rd St |

**Control de reparto dentro de no-marca**: como no hay presupuesto por ad group, E se limita con keywords en frase y exacta, sin "auto shop near me" (CPA $38 en el benchmark). Si en 2 semanas E se lleva >45% del gasto de no-marca y el CPL de transmisión es mejor, se bajan pujas de E con un ajuste en el ad group o se pausan sus keywords genéricas de mayor volumen.

**Anuncio de solo llamada**: se mantiene uno en MARCA y uno en A (hoy se lleva ~31% del gasto y convierte). Se mide aparte para decidir en F2.

Negativas por ad group (evitan que los grupos compitan entre sí):
- A: rebuild, replacement, cost, price, flush, fluid, clutch, cvt
- B: flush, fluid change, clutch
- C: rebuild, replacement
- E: transmission, check engine, engine, oil change, lube, brake(s), tire(s)
- F: transmission, light bulb, "reset"

## Keywords descartadas y por qué
| Término | Motivo | Destino |
|---|---|---|
| oil change / lube / tune up | Ticket bajo; CPC $4.14 dominado por cadenas; hoy funciona como comodín en amplia | Negativa (**decisión del cliente pendiente**) |
| auto shop near me | CPA $38 en el benchmark (el peor con volumen) | Fuera de F1; revisar en F3 |
| brake repair, radiator repair, alternator, starter, cv axle, timing belt | Comerciales, pero no son el foco; las cadenas dominan frenos | Fase 3 "Otros servicios" |
| car/auto ac repair | Estacional (abr–sep), CPC $3 | Fase 3, ad group G en temporada |
| auto repair financing / car repair financing | CPC $5+, genérico | No |
| used / rebuilt transmission for sale, transmission parts/kit | Compra de pieza, no servicio | Negativa |
| marcas de competidores y concesionarios | Política PMM | Negativa |
Detalle: `data/keywords.csv`.

## Copy
Completo en [`data/ads-search-103rd.md`](data/ads-search-103rd.md): 6 ad groups × 15 titulares + 4 descripciones (longitudes validadas), H1 pinneado, extensiones. Ángulos tomados de `competitors.md`:
- **Garantía nacional + financiamiento**: la franquicia los tiene y el anuncio actual no los usa. Es el hueco frente a Duval County, que está en la misma calle.
- **Síntoma en el titular** ("Slipping? Won't Shift?") y **"Repair First, Not Replace"**: poca competencia en términos de síntoma.
- **Prueba social en número**: "507 Google Reviews". Se evita "4.4★" en el texto porque compara mal con los independientes (4.9).
- **Dirección como diferenciador**: "on 103rd", "Westside Jacksonville".

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| `/thank-you/` (redirect del form) | No | PMM + quien edite el sitio | **Sí** (F0) |
| Form del subdominio 103rd funcionando (0 envíos en 90 días) | Revisar | PMM | **Sí** (F0) |
| `103rd.aamco-jacksonvillefl.com/` (marca) | Sí | — | No |
| `/service/automatic-transmissions/` versión 103rd (H1 "Transmission Repair on 103rd St", número CallRail, form corto arriba) | Base sí; versión sede no | Cliente/franquicia | No (se lanza con la actual, se mejora en F2) |
| Rebuild + financiamiento 103rd | **No** | Cliente/franquicia | No (B arranca con `/service/automatic-transmissions/`) |
| `/service/fluid-change-maintenance/`, `/service/manual-transmissions/` | Sí | — | No |
| `/auto-service/` versión 103rd | Base sí | Cliente/franquicia | No |
| `/service/check-engine-light-service/` versión 103rd | Base sí | Cliente/franquicia | No |
| Dominio canónico único para la sede (hoy son 3) | Decisión | Cliente/franquicia | No, pero afecta GBP y la extensión de ubicación |

Supuesto: las rutas `/service/...` están en `aamco-jacksonvillefl.com`. Si el subdominio 103rd tiene las mismas páginas, se usa el subdominio (mejor coherencia con la sede y GA4).

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |
|---|---|---|---|
| **F0 — Medición y landing** (sem. 1–2) | Sin cambio (~$2,070 plan / ~$1,700 gasto real) | Estructura actual sigue corriendo | 1 conversión primaria probada (CallRail primera llamada ≥ 60 s + form con `/thank-you/`); CPL máximo del cliente definido; ofertas confirmadas |
| **F1 — Estructura nueva** (sem. 3–10) | ~$2,070 | Marca $8/d · No-marca $60/d · PMax $0 · campaña vieja pausada | 30 días con ≥25 conversiones limpias/mes en no-marca y CPL no-marca ≤ CPL máximo (o ≤ $38 CallRail si el cliente no lo dio) |
| **F2 — Optimización** (sem. 11–14) | ~$2,070 | Reasignar dentro de no-marca según CPL por ad group; prueba de incrementalidad de [aamco] (bajar puja 2–4 sem.) | CPL estable 2 semanas; search terms limpios (<5% de gasto irrelevante) |
| **F3 — Escala** (mes 4+) | $2,070 → ~$3,000 (recuperar parte del ~50% de IS perdida por presupuesto) | Separar **Transmisión** en campaña propia cuando pueda tener ≥ $96/d; agregar G (A/C, abr–sep) y "Otros servicios"; tCPA en no-marca con ≥30 conv. limpias/30 d | CPL real ≤ CPL máximo al escalar (+20% de presupuesto por paso, 2 semanas entre pasos) |
| **F4 — RLSA** | +5–10% | Audiencias de visitantes en observación con ajuste | Lista ≥1,000 usuarios en Search |
| **F5 — PMax (condicional)** | a definir | Ver abajo | Las 5 condiciones de `knowledge/estrategias/pmax-cuando-y-como.md` |

**Resultados esperados en F1** (no-marca, ~$1,825/mes): CPC ~$6–7 → ~270 clics; ~20% llamadas CallRail → **~55 llamadas**; 50–60% calificadas → **~28–33 leads/mes**. Marca (~$245/mes): ~55 clics, ~14 llamadas (muchas de clientes actuales).

## Por qué NO (todavía)
- **PMax**: hoy no cumple las condiciones. Mide "Calls from ads" (63 de sus 88 conversiones), una señal duplicada; no hay confirmación de exclusión de marca; no hay assets propios validados; y la señal limpia no llega a 30 conversiones al mes. Además compite con Search por las mismas llamadas. Se reevalúa en F5.
- **Amplia**: hoy es el 98–100% del gasto en las 7 sedes y la razón de que "oil change near me" funcione como comodín. Vuelve solo con tCPA maduro, tracking confiable y aprobación de Jhombis (estándar PMM #2).
- **Display / Demand Gen**: no para un taller local. La campaña Display "10% Off New Clients" de St. Augustine (1,140 clics, 12 conversiones en 90 días) confirma el patrón.
- **Separar transmisión y general en campañas distintas**: no alcanza la regla de 3× CPL/día. Se hace en F3.
- **tCPA**: no hasta 30 días de conversión limpia. Fijar tCPA sobre la señal actual haría a Google perseguir llamadas repetidas.
- **LSA**: sí, pero como **pista paralela**, no dentro de esta estrategia. Hay que verificar si la categoría de auto repair está habilitada en Jacksonville y si la franquicia lo permite.

## Riesgos y supuestos
1. **Caída de volumen reportado al pasar de amplia a frase**. Es esperable y en parte deseada: sale el tráfico que entraba por "oil change near me". Mitigación: medir por leads limpios, no contra el histórico inflado. Si en 14 días los clics de no-marca caen >40%, reabrir "mechanic near me" y "auto shop near me" en frase antes que volver a amplia.
2. **CPL máximo desconocido**. Si el cliente da un CPL máximo menor a $45, hay que revisar si E (general) es viable o si todo va a transmisión.
3. **Marca con clientes actuales**. "aamco 103rd" + llamada = muchas llamadas de seguimiento de reparaciones. Es la razón de medir marca por cuota de impresiones y no por CPA. La prueba de incrementalidad de F2 decide cuánto invertir.
4. **Canibalización con otras sedes**: fuera del control de esta estrategia. Si Biscayne o Atlantic siguen pujando [aamco] con su radio, el CPC de marca no baja.
5. **Landings de la franquicia**: si el cliente no puede editar el sitio, B arranca sin landing propia y el mensaje de financiamiento queda solo en el anuncio.
6. **Volúmenes estimados**, no de Keyword Planner. Correr Keyword Planner vía API (geo radio 5 mi) antes de `/build-campaign` para confirmar A y E.
