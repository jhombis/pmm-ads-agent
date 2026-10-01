---
cliente: Hemet Affordable Burial and Cremation
slug: hemet-affordable-burial-cremation
actualizado: 2026-10-01
version: 1
supuestos:
  - Sin audit-site.md: el sitio está bloqueado por el proxy del entorno; URLs de landing por confirmar en /audit-landing.
  - Sin competitors.md formal: se usa la competencia del brief + los competidores vistos en search terms.
  - Sin benchmark.md formal: benchmark leído directo del MCC vía Windsor (5 cuentas funerarias, abr–sep 2026), ver abajo.
  - Margen real y precio de servicios completos PENDIENTES: CPL máximo del brief ($60) es un supuesto.
  - Personal hispanohablante sin confirmar: el grupo en español queda para Fase 2.
---

# Estrategia Google Ads — Hemet Affordable Burial and Cremation

## Resumen ejecutivo
- **No es una cuenta nueva.** La cuenta 751-429-2721 corre desde el 07/05/2026: ~$1,390/mes en Search con 12.4 conv/mes (**CPA $113**), más un Display de $31/mes con 2,000+ clics y **0 conversiones**. Esto es una **reestructuración**, no un lanzamiento.
- Problemas a corregir: ~50% del gasto en **concordancia amplia**; ~**18% del gasto en términos de competidores e irrelevantes** (Wiefels, Emerson Bartlett, Dearly Beloved, coroner, hospice…); la marca se mezcla con la genérica ($207 en 90 días); el Display es tráfico basura.
- Propuesta: **2 campañas Search** (genérica consolidada con 4 ad groups + marca), Display pausado, solo frase/exacta, negativas de nicho, geo por las 5 ciudades + 3 zonas no incorporadas.
- Presupuesto: **$1,500/mes** → genérica $44/día y marca $5/día. **CPL objetivo F1 ≤ $100**; meta F2 = mediana del MCC (**$83 ±20%**).
- **tCPA no es alcanzable con este presupuesto** (hacen falta ~30 conv/30 días y hoy hay ~12). Se mantiene Maximizar conversiones sin tCPA. Se revisa si el presupuesto sube o si el volumen de conversiones se duplica.

## Diagnóstico de la cuenta actual (90 días, jul–sep 2026)
| Métrica | Valor | Lectura |
|---|---|---|
| Gasto Search | $3,997 · 308 clics · 30 conv | CPC **$13**: muy alto frente al CPC de Semrush ($3.5–5), por la amplia y por pujar en términos genéricos caros |
| CPA mensual | jun $80 · jul $137 · ago $197 · sep $96 | Inestable; 12 conv/mes no alcanzan para que la puja automática estabilice |
| Amplia vs frase | Amplia $2,038 / 20 conv · Frase $1,959 / 10 conv | La amplia trajo más conversiones, pero los search terms muestran la fuga. La frase gastó $568 en 2 keywords sin conversión (`funeral homes in hemet california`, `funeral homes`) |
| Competidores en search terms | **~$495** | Wiefels (×6 variantes), Valley Mortuary, Circle of Life, Emerson Bartlett, Dearly Beloved… |
| Irrelevantes | **~$209** | coroner ($41), hospice, cementerio, mariachi, urns, caskets, final expense, VA, Lake Elsinore, Menifee |
| Marca dentro de la genérica | $207 / 24 clics / 2 conv | A $8.6 por clic, cuando en una campaña de marca debería costar ~$1–2 |
| Display | $91 / 1,641 clics / 0 conv | Clics accidentales (apps). **Pausar** (estándar #8) |
| Conversiones primarias | Calls from Ads 21 · Website Calls 5 · Form Fill 4 | Las acciones locales (direcciones, visitas) ya son secundarias. **Verificar la duración mínima de llamada** (≥90 s recomendado en este nicho) |

## Benchmark MCC (funerarias, abr–sep 2026, vía Windsor)
| Cuenta | Search $/mes | Search conv/mes | Search CPA | PMax CPA |
|---|---|---|---|---|
| Swan Burial & Cremation | $913 | 15.0 | **$61** | $40 |
| Inland Memorial (cuenta anterior del mismo dueño, pausada en ago) | $307 | 4.6 | $67 | $29 |
| Sunflower Cremation | $1,928 | 23.3 | $83 | $21 |
| **Hemet Affordable (este cliente)** | $1,394 | 12.4 | **$113** | — |
| Murrieta Valley Funeral Home | $1,244 | 6.8 | $182 | $57 |
| Colton Sunflower (nueva, ago) | $1,378 | 3.5 | $394 | — |

Mediana Search de las cuentas maduras: **~$83**. El PMax "barato" de las otras cuentas requiere auditar qué conversiones cuenta (posible inflación por acciones locales o llamadas cortas) antes de usarlo como referencia. Esto se le encarga a `/benchmark-interno`.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| Search \| Funeral & Cremation \| Hemet Valley | Llamadas + formularios | **$44** | 90% | Maximizar conversiones (sin tCPA) | Presencia: Hemet, San Jacinto, Winchester, Beaumont, Banning + Valle Vista, East Hemet, Homeland* | 24/7 |
| Search \| Brand | Captar la marca barata y defenderla | **$5** (techo; gasto real esperado ~$1–3/día) | 10% | Maximizar clics con CPC máx. $3 | Mismo geo | 24/7 |
| ~~Responsive Display~~ | — | **Pausar** | — | — | — | — |

\*Las 3 zonas no incorporadas necesitan aprobación de Jhombis: son el mismo mercado y no salen del área real de servicio.

**Por qué una sola campaña genérica** (desviación consciente del estándar #3): la regla de aprendizaje pide ≥3× CPL/día por campaña (~$250/día). Con $44/día, dividir por servicio dejaría cada campaña con ~$10/día y 2–3 conversiones al mes, sin señal suficiente. Se separa por ad group; si el presupuesto sube a ≥$3,000/mes, Funeral Home pasa a ser campaña propia.

**Cómo se prioriza "servicios completos" sin campaña propia:** el grupo Funeral Home lleva los términos de mayor volumen (`funeral home near me` 40K) y su copy empuja capilla, velación y recepción. En la llamada se ofrece pasar de la cremación o entierro directo al servicio completo, y eso pertenece al guion del cliente (eslabón 4).

## Estructura por campaña

### Campaña: Search | Funeral & Cremation | Hemet Valley
Configuración: solo red de Búsqueda (sin socios ni Display), presencia, rotación optimizada, recomendaciones automáticas apagadas, idioma EN (en Fase 2 se suma ES si se aprueba el grupo en español).

| Ad group | Keywords (match) | Vol. est. (US) | Landing | H1 pinneado |
|---|---|---|---|---|
| **Funeral Home** (estrella) | "funeral home near me", [funeral home near me], "funeral homes near me", "funeral home hemet", [funeral home hemet], "mortuary near me", "mortuary hemet", [mortuary hemet], "funeral services near me", "funeral chapel near me", "memorial service near me", "funeral home san jacinto ca", "funeral home beaumont ca", "funeral home banning ca", "funeral homes" | ~150K nacional (geo local: bajo) | /funeral-services (PENDIENTE) | Funeral Home in Hemet, CA |
| **Cremation** | "cremation services near me", [cremation services near me], "cremation near me", "direct cremation near me", [direct cremation near me], "cremation hemet", [cremation hemet], "cremation hemet ca", "crematory near me", "crematorium near me", "simple cremation near me", "cremation with viewing", "service and cremation" | ~50K nacional | /cremation (PENDIENTE) | Cremation Services Hemet |
| **Affordable** (intención de precio) | "affordable cremation near me", "cheap cremation near me", "low cost cremation near me", "cremation cost near me", "cremation prices near me", "affordable funeral homes near me", "cheapest mortuary near me", "low cost cremation riverside county" | ~7K nacional | /price-list (GPL, PENDIENTE) | Affordable Cremation Hemet |
| **Burial** | "burial services near me", [burial services near me], "burial near me", "burial service", "direct burial near me", "affordable burial", "low cost burial services", "burial packages" | ~5K nacional | /burial (PENDIENTE) | Burial Services in Hemet |

Negativas específicas por grupo (negativas cruzadas para que cada término caiga en su grupo):
- Funeral Home: `cremation`, `burial`, `cheap`, `cheapest`, `affordable`, `low cost`.
- Cremation: `cheap`, `cheapest`, `affordable`, `low cost`, `cost`, `price`, `prices`.
- Burial: `cheap`, `cheapest`.
- Affordable: ninguna.

**Ad group Emergencia/24-7**: no aplica como grupo aparte. En este nicho la urgencia ya está en todos los términos "near me" y no hay búsquedas del tipo "emergency funeral home". La disponibilidad 24/7 va en el copy y en los callouts.

### Campaña: Search | Brand
| Ad group | Keywords (match) | Vol. est. | Landing | H1 pinneado |
|---|---|---|---|---|
| Brand | [hemet affordable burial and cremation], "hemet affordable burial", "hemet affordable cremation", [inland memorial hemet], [harford chapel hemet] | ~30/mes | Home | Hemet Affordable Cremation |

En la campaña genérica se agregan los términos de marca como negativas, para que no compitan con la de marca.

## Keywords descartadas y por qué
| Término / patrón | Motivo |
|---|---|
| `cremation cost`, `how much does cremation cost`, `average funeral cost` | Informacional. Con amplia gastó $384 con CPA de $192. Solo se cubre la variante con "near me" |
| `what to do when someone dies`, `death what to do` | Informacional, CPC bajo y sin intención de contratar |
| `cremation insurance`, `final expense`, `cremation plans` | Seguros y planes, otro producto |
| `pre need funeral plans`, `funeral pre planning` | Ciclo largo y volumen bajo. Pasa a Fase 3 con campaña propia |
| `funerarias cerca de mi` (1,900) | Sí hay demanda (convirtió 1 vez), pero hace falta confirmar personal hispanohablante. Pasa a Fase 2 |
| Competidores (Wiefels, Hemet Valley Mortuary, Miller-Jones, etc.) | Estándar #5. ~$495 de gasto en 90 días |
| Fuera del área (Palm Springs, Lake Elsinore, Menifee, Perris, Riverside) | Fuera del área de servicio confirmada |

Detalle completo en `data/keywords.csv`.

## Copy
En `data/ads-search.md`: 5 grupos × 15 headlines + 4 descripciones (EN, límites validados), 3 RSA por grupo (pin en posición 2: precio / confianza / 24-7), sitelinks, callouts, snippet, llamada y ubicación.

Ángulos, según brief y competencia:
- **Precio claro con valor local.** $1,095 no es el más barato ($439+ San Jacinto Valley, $980 Simplicity), así que no se compite por "el más barato" sino por "precio publicado + funeraria local + capilla histórica + sin presión".
- **Entierro directo a $1,995** como diferencial: casi nadie publica precio de entierro en el valle.
- **24/7 con persona real** (confirmado), familiar y con licencia.
- **No** se menciona Inland Memorial (reputación mixta) ni el número FD hasta confirmar cuál está vigente. Los precios deben coincidir con el GPL.

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| /funeral-services (servicios completos: capilla, velación, recepción, precio desde) | PENDIENTE (/audit-landing) | Cliente / PMM | Sí, para que el grupo estrella apunte a algo distinto de la home. Mientras tanto, la home |
| /cremation (simple $1,095 + cremación con velación) | PENDIENTE | Cliente / PMM | No (temporal: home) |
| /burial (directo $1,995 + tradicional) | PENDIENTE | Cliente / PMM | No (temporal: home) |
| /price-list (GPL publicado, exigido por CA B&P §7685) | PENDIENTE | Cliente | **Sí**: cumplimiento legal y landing del grupo Affordable |
| Thank-you page con conversión de formulario | PENDIENTE | PMM | **Sí**: verificar con Tag Assistant (estándar #7) |

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |
|---|---|---|---|
| **F0 — Limpieza** (semana 1) | sin cambio | — | Display pausado; amplias pasadas a frase; negativas aplicadas; conversiones verificadas (llamada ≥90 s, form con Tag Assistant); GBP nuevo vinculado |
| **F1 — Reestructura** (30–45 días) | $1,500 | Genérica $44/día · Marca $5/día | ≥12 conv/mes **y** CPA ≤ $100 **y** desperdicio en search terms <10% del gasto |
| **F2 — Optimización** | $1,500 (o más si el cliente aprueba) | Reasignar keywords y ad groups según CPA; sumar grupo **Español** si hay personal | CPA ≤ $85 dos meses seguidos; cliente confirma que los leads se convierten en casos (feedback cualitativo, sin CRM) |
| **F3 — Pre-need** | +$300–500 | Campaña Pre-need aparte (otro mensaje, otra landing) | F2 cumplida y landing de pre-planning lista |
| **F4 — RLSA** | sin cambio | Audiencia de visitantes del sitio en observación sobre la genérica | ≥1,000 usuarios en lista |
| **F5 — PMax** | evaluar | Ver abajo | 30+ conv/mes con tracking confiable + GBP con reseñas + assets propios |

## Por qué NO (todavía)
- **PMax**: el cliente tiene ~12 conv/mes (el umbral es 30), una ficha de Google nueva sin reseñas y no tiene fotos ni videos propios confirmados. PMax se comería la marca y Maps, y reportaría conversiones locales infladas. Las otras funerarias del MCC muestran PMax con CPA de $21–57, pero primero hay que auditar qué cuentan esas conversiones (`/benchmark-interno`).
- **Amplia**: aunque en los datos trajo más conversiones, generó ~$700 de fuga en competidores e irrelevantes. Se pasa todo a frase/exacta y se vuelve a evaluar solo con tCPA maduro y aprobación de Jhombis (estándar #2).
- **Display**: 0 conversiones con 2,000+ clics. Para un servicio local de este tipo, el Display es ruido.
- **Campaña por servicio**: el presupuesto no alcanza para que cada campaña salga del aprendizaje (ver arriba).
- **LSA**: la categoría "funeral home" no aparece como disponible. Sigue `PENDIENTE` verificarlo; no es bloqueante.

## Riesgos y supuestos
1. **CPA objetivo ($85–100) por encima del CPL máximo supuesto ($60).** Si el margen real por caso es de ~$500, la cuenta no es rentable con cremación directa sola. Hace falta el margen real y la mezcla de servicios (un servicio completo deja mucho más margen). Es el pendiente número 1 con el cliente.
2. **Calidad de las conversiones**: 70% son "Calls from Ads". Si la duración mínima está en el default, hay llamadas cortas o de comparación de precios contadas como lead. Verificar en F0.
3. **Ficha de Google nueva** con pocas o ninguna reseña, en la misma dirección que la ficha de Inland Memorial: riesgo de suspensión o duplicado y prueba social débil en Maps.
4. **CPC alto ($13)**: al quitar la amplia y los términos genéricos caros, el volumen de clics puede caer. Si el gasto queda por debajo del presupuesto, se amplían las variantes en frase antes de volver a la amplia.
5. **Inconsistencia de presupuesto**: el nombre de la cuenta dice "$2800" y la campaña "$2500/mo", pero el gasto real es ~$1,400/mes y el brief dice $1,500. Confirmar si $2,800 es la facturación total al cliente (fee incluido).
6. Sitio no auditado: landings y tracking por confirmar en `/audit-landing`.
