---
cliente: 290 Tow and Recovery
slug: 290-tow-recovery
actualizado: 2026-09-23
version: 1
supuestos:
  - Ticket y margen PENDIENTE. El CPL objetivo sale del benchmark del MCC ($14.57 por llamada, rango $11.70–$17.50), no de la economía del cliente.
  - Servicio estrella / servicio a evitar PENDIENTE. Prioridad asumida - towing light/medium > exotic y long-distance > roadside.
  - El volumen local no viene de Keyword Planner (sin credenciales de la API en este entorno). Se usa volumen nacional de Semrush + search terms reales de la cuenta (6 días). Validarlo con Keyword Planner en la UI antes de /build-campaign.
  - Tracking de conversiones no verificado con Tag Assistant (bloqueante).
  - Capacidad de flatbed, RV y motocicleta sin confirmar.
  - Licencia TDLR y seguro sin confirmar; no se usan en el copy.
  - Sin GBP, así que no hay activo de ubicación ni LSA.
  - El cliente atiende de verdad el radio de 40 mi (el sitio dice "45-minute radius"). Confirmar si cubre Boerne y Fair Oaks Ranch.
---

# Estrategia Google Ads — 290 Tow and Recovery

## Resumen ejecutivo
- **1 campaña Search** consolidada ("Search | Towing | Hill Country 40mi") con **7 ad groups por tema**, $27/día (~$825/mes). No hay presupuesto para separar campañas: la regla de aprendizaje pide ≥3× CPL/día = $44/día por campaña.
- **Frase por defecto y exacta en el top de cada grupo. Sin amplia.** Todo el desperdicio de los primeros 6 días (43% del gasto) entró por amplia.
- **Puja F1**: Maximizar clics con tope de CPC de **$6.50** (mediana Search MCC) hasta tener tracking verificado y ≥15 conversiones. Después, Maximizar conversiones. **tCPA** cuando haya ~30 conversiones en 30 días (estimado: días 45–60).
- **CPL objetivo: $14.57 por llamada** (rango aceptable $11.70–$17.50). En F1 se espera $18–24 mientras aprende. Proyección: **35–55 llamadas/mes** con 125–165 clics.
- La cuenta ya está activa con la plantilla PLL (amplia, Max clics, sin negativas). Se reestructura **dentro de la campaña existente** por /build-campaign, tras aprobación de Jhombis. No se aplica nada todavía.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| Search \| Towing \| Hill Country 40mi (hoy: "290 Tow and Recovery - ENHPRM Radius - $1500/mo. - 09/17/2026", se conserva el nombre PLL si el revendedor lo necesita) | Llamadas (Calls from Ads + Website Calls). Form Fill como secundaria | $27 | 100% | Maximizar clics, tope CPC $6.50 | **Presencia**, radio de 40 mi **recentrado en el centro de Fredericksburg** (30.2752, -98.8720; hoy está ~4 mi al NO). Excluir Fair Oaks Ranch, Bulverde y Spring Branch hasta que el cliente confirme que los atiende | 24/7 (el cliente contesta 24/7). Zona horaria de la cuenta: LA, así que los reportes por hora van con -2 h |

**Configuración obligatoria**: solo red de Búsqueda (sin partners ni Display), rotación "optimizar", aplicación automática de recomendaciones **apagada**, idioma inglés, segmentos de audiencia en observación (sin exclusión).

**Qué NO se crea en F1**
- Marca: no hay búsquedas de "290 tow" y ningún competidor puja por la marca.
- LSA: pista paralela cuando exista GBP, licencia y seguro (ver fases).
- Remarketing: F4. PMax: F5 condicionada.

## Estructura por campaña
### Campaña: Search | Towing | Hill Country 40mi
Volumen = búsquedas/mes en **EE. UU.** (Semrush) solo para ordenar. El volumen local real es una fracción y está PENDIENTE (Keyword Planner). Exacta = [ ], frase = " ".

| Ad group | Keywords (match) | Vol. est. (US) | Landing | H1 pinneado |
|---|---|---|---|---|
| **AG1 Towing Near Me** (núcleo, ~55–60% del gasto esperado) | [tow truck near me], [towing near me], [towing company near me], "tow truck near me", "towing near me", "towing company near me", "towing service near me", "tow service near me", "tow truck company near me", "car towing near me", "tow trucks near me", "car towing service", "tow truck service", "tow my car" | 135k / 110k / 40.5k / 27.1k… | `/` (home, tras ajustar el H1) | Tow Truck Near You - 24/7 |
| **AG2 Wrecker Service** ("wrecker" es el término de TX; 2 de los 3 clics "ok" de la cuenta fueron wrecker) | [wrecker service near me], "wrecker service near me", "wreckers near me", "wrecker service", "wrecker near me" | 12.1k | `/light-medium-duty-towing/` | Wrecker Service Near You |
| **AG3 24/7 Emergency Towing** (intención urgente, CPC distinto) | [24 hour towing near me], "24 hour towing near me", "emergency towing", "24 hour tow truck", "24 hour towing", "emergency tow truck", "towing open now" | 2.9k / 1.9k / 590 | `/` | 24 Hour Towing - Call Now |
| **AG4 Towing + Ciudad** (cada ciudad tiene <100/mes → un solo grupo con inserción de ubicación, no STAG por ciudad) | "towing fredericksburg tx", "tow truck fredericksburg", "fredericksburg towing", "towing kerrville tx", "kerrville towing", "tow truck kerrville tx", "wrecker service kerrville tx", "towing johnson city", "tow truck llano tx", "towing comfort tx", "towing blanco tx" | 10–70 c/u | `/` | {LOCATION(City):Hill Country} Towing |
| **AG5 Exotic & Flatbed Towing** (ticket alto, CPC bajo, sin competidor local) | [exotic car towing], "exotic car towing", "luxury car towing", "classic car towing", "medium duty towing". "flatbed towing near me" y "flatbed tow truck near me" solo si el cliente confirma el flatbed | 320 / 390 / 720 | `/exotic-vehicle-towing/` (**se lanza en pausa hasta que se arreglen los CTA**) | Exotic Car Towing |
| **AG6 Long-Distance Towing** (ticket alto; el genérico lo pagan brokers → solo con ancla) | "long distance towing near me", "long distance car towing", "long distance towing fredericksburg", "long distance towing texas", "tow car to san antonio", "tow car to austin" | 260 + variantes | `/local-long-distance-towing/` | Long-Distance Towing |
| **AG7 Roadside (solo exacta, con tope)** (ticket bajo; 14% del gasto inicial y "car jumper" = $27) | [roadside assistance near me], [roadside service near me], [jump start near me], [flat tire change near me] | 33.1k / 1.3k / 320 | `/roadside-assistance/` | Roadside Assistance Near You |

**Control de presupuesto entre grupos.** Con 1 campaña no hay presupuesto por ad group. La prioridad se controla por match type: AG7 va solo en exacta. **Regla**: si AG7 pasa del 20% del gasto semanal, o AG5/AG6 no generan llamadas en 30 días con más de $100 de gasto, se pausan.

**Negativas específicas por grupo** (además de la lista de cuenta):
- AG1 / AG3: "roadside", "jump", "tire" (empujan roadside hacia AG7).
- AG4: "near me" (evita competir con AG1; ciudad sola).
- AG5: "cheap", "near me" solo si canibaliza AG1 (revisar en la semana 2).
- AG6: "shipping", "transport", "carrier" y "enclosed".
- AG7: "towing", "tow truck" (las búsquedas de grúa van a AG1).

## Keywords descartadas y por qué
Detalle completo en `data/keywords.csv` (77 términos).

| Keyword | Motivo |
|---|---|
| roadside assistance (genérico), emergency roadside assistance | AAA/seguro. $9.69 sin conversión en la cuenta |
| car jumper, car dollies, rv haulers, what does roadside assistance cover | Desperdicio real de la cuenta: producto, equipo, transporte, informacional ($59.40) |
| cheap tow truck / cheap towing near me | Buscador de precio. $11.84 sin conversión |
| fuel delivery near me | CPC $7.88 con ticket bajo |
| accident towing | CPC $8.50. Revisar en F3 si el cliente trabaja con aseguradoras |
| heavy duty / semi truck towing | Fuera de servicio (light/medium) |
| long distance towing (genérico), enclosed car transport | SERP pagada de brokers de auto transport |
| car lockout | Compite con cerrajeros. Ticket bajo |
| rv / motorcycle towing | PENDIENTE capacidad. Moto es candidata a F2 (el sitio dice que remolca motos) |
| towing cost per mile, how much does a tow cost | Informacional. Insumo del ángulo "precio claro" |
| towing san antonio, towing fredericksburg va | Fuera de mercado |
| marcas de competidores | Estándar PMM #5 |
| gruas cerca de mi | No hay anuncios en español. Prueba en F3 |

## Copy
Completo en **`data/ads-search-towing.md`**: 7 ad groups × 3 RSA, 15 headlines + 4 descripciones cada uno, límites validados.
- **Ángulos**: 24/7 real, **precio claro antes de enganchar / sin cargos ocultos** (gap de la competencia y la queja pública contra Mr. Wrecker), **Navy Veteran Owned** (diferenciador real del sitio), 10% Senior Discount, local de Fredericksburg frente a los números 877 de las redes lead-gen.
- **Pruebas**: RSA B fija el ángulo precio en la posición 2; RSA C fija el ángulo confianza (veterano).
- **Assets**: 4 sitelinks (uno por servicio), 8 callouts, snippet de servicios, llamada con número de reenvío. Ubicación: no hasta que exista el GBP. Imágenes: no hasta tener fotos propias.
- **Fuera del copy hasta confirmarlos**: "licensed & insured", número TDLR, ETA en minutos, flatbed.

## Landings requeridas
| URL | Existe | Ad groups | Responsable | Bloqueante |
|---|---|---|---|---|
| `/` | Sí | AG1, AG3, AG4 | PMM | No. **Cambiar el H1 del hero** a "24/7 Towing & Tow Truck Service in Fredericksburg, TX" y alinear "45-minute radius" con 40 mi (1 h) |
| `/light-medium-duty-towing/` | Sí | AG2 | PMM | No. Subir los CTA de llamar/cotizar arriba del texto (hoy aparecen tras ~1,400 px en móvil) |
| `/exotic-vehicle-towing/` | Sí | AG5 | PMM | **Sí**: faltan los CTA (bloque vacío en móvil). AG5 se lanza en pausa hasta arreglarlo |
| `/local-long-distance-towing/` | Sí | AG6 | PMM | No |
| `/roadside-assistance/` | Sí | AG7 | PMM | No |
| Página de gracias (`/thank-you/`) | No | Form Fill | PMM | **Sí** para medir el formulario (redirect del formulario Elementor) |
| Velocidad móvil (LCP 5.7–6.9 s en páginas de servicio) | — | Todas | PMM | No. Mejora de F2: WebP, caché, CSS/JS sin usar |

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |
|---|---|---|---|
| **F0 — Corrección** (antes de reestructurar, ~3–5 días) | Se mantiene la actual o se pausa. **Decisión de Jhombis**; hoy sigue gastando con 43% de desperdicio | — | Tracking verificado con Tag Assistant (Calls from Ads con umbral de 60 s, Website Calls, Form Fill), CTA de exotic arreglado, página de gracias creada, negativas cargadas, geo recentrada |
| **F1 — Lanzamiento controlado** (días 1–30) | $825 | Search Towing $27/día (100%) | ≥15 conversiones verificadas, CPC promedio ≤ $7, desperdicio en search terms < 15% |
| **F2 — Maximizar conversiones** (días 30–60) | $825 | Search $27/día. Reasignación entre ad groups por pausa o activación, no por presupuesto | ≥30 conversiones en 30 días y CPL ≤ $17.50 → tCPA = CPL real de 30 días × 1.1 |
| **F3 — tCPA + expansión** (días 60–90) | $825 (escalar solo si el cliente amplía el fee) | Search con tCPA. Pruebas: ad group en español, moto/RV si se confirma, accident towing si trabaja con aseguradoras, amplia en AG1 **solo con aprobación de Jhombis** | CPL estable ±20% durante 4 semanas |
| **Pista LSA** (en paralelo, cuando haya GBP) | Pay-per-lead, aparte del presupuesto de Search (o se divide el presupuesto; decisión del cliente) | — | GBP verificado + licencia TDLR + seguro + background check |
| **F4 — RLSA** | Dentro de los $825 | Audiencia de visitantes del sitio en observación, luego ajuste | Lista ≥1,000 usuarios |
| **F5 — PMax** | Condicionado | — | Ver "Por qué NO" |

## Por qué NO (todavía)
- **PMax**: requiere 30+ conversiones/mes con tracking confiable, Search estable, exclusión de marca y **assets propios**. Hoy hay 0 conversiones verificadas, cero fotos propias y no hay GBP. En el MCC, PMax baja el CPL (Grand Valley $5.86, A&D $6.50), pero solo en cuentas con historial. Se reevalúa a los 90 días.
- **Amplia**: en 6 días con amplia salió CPC de $11.83 y 43% de desperdicio ("car jumper", "car dollies", "rv haulers"). Las cuentas top del MCC usan amplia, pero con Max conversiones y meses de señal. Se prueba en F3 solo con aprobación.
- **Display / Demand Gen / Video**: no para towing local. Denton (MCC) quemó $1,377 en clics basura de Display.
- **Campaña de marca**: sin búsquedas de marca. Se reevalúa cuando aparezca "290 tow" en los search terms.
- **Campañas separadas por servicio**: con $27/día, dividir deja cada campaña por debajo de 1× CPL/día y ninguna sale de aprendizaje. Si el fee sube a más de $1,500 de pauta, separar Roadside y Long-distance/Exotic.
- **STAG por ciudad**: ninguna ciudad pasa de 100 búsquedas/mes.
- **Maximizar conversiones desde el día 1**: sin conversiones verificadas, el algoritmo no tiene señal y con $27/día sube los CPC. Por eso Max clics con tope primero.

## Riesgos y supuestos
- **Volumen**: ninguna cuenta small-town del MCC gasta $825/mes (mediana $392). Si al recentrar el radio y quitar la amplia la campaña no gasta $27/día, se abre AG7 a frase o se suma "motorcycle towing", no se vuelve a la amplia. Validar con Keyword Planner (geo 40 mi de 78624) antes de /build-campaign.
- **CPL vs. economía**: el CPL máximo del brief (~$14) es provisional (ticket supuesto $175). Si el ticket real es menor, ni la mediana del MCC es rentable. **Confirmar ticket y margen antes de F2.**
- **Conteo inflado**: las 3 conversiones son primarias. Hay que verificar que la misma llamada no cuente en Calls from Ads y en Website Calls, y usar un umbral de 60 s.
- **Sin reseñas ni GBP**: el Map Pack (Douglas 157★, Tic Tac 70★, Integrity 89★) se lleva la llamada antes que el anuncio. Crear el GBP es la acción de mayor impacto fuera de Ads.
- **Borde de San Antonio**: el 35% del gasto inicial fue a Fair Oaks Ranch. Si el cliente sí lo atiende, se quita la exclusión y se vigila el CPC.
- **Zona horaria LA vs. Central**: cualquier programación futura va con -2 h.
- **La cuenta sigue activa sin cambios** hasta que Jhombis apruebe. Cada semana en la configuración actual cuesta ~$190 con alrededor de 40% de desperdicio.
