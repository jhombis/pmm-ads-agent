---
cliente: A's Unasa Towing
slug: as-unasa-towing
pais: US
actualizado: 2026-10-22
version: 1.1
supuestos:
  - Ticket promedio y margen PENDIENTES. El CPL máximo de referencia es ~$17 con el piso de $79.99 (brief). El CPL objetivo sale del benchmark, no de la economía del cliente.
  - Horario PENDIENTE (24/7 según el cliente, "Closed Sunday" según la web). F1 arranca con el horario de la web.
  - Área PENDIENTE. Se usan los 4 ZIP del cliente y se proponen 84104 (base) y 84120 (West Valley City) como [C].
  - Keyword Planner geolocalizado no corrido (no hay google-ads.yaml). El volumen local de "near me" se estima como nacional × 0.05% (inferido: los 4 ZIP suman ~152–184k habitantes sobre ~335M).
  - Capacidad medium-duty de la F550, servicios de roadside y motos PENDIENTES. Quedan fuera de F1.
  - GBP no encontrado. Sin activo de ubicación hasta tenerlo.
  - Copy con [C] depende de confirmación del cliente (precio, rotación policial, owner-operated, horario).
---

# Estrategia Google Ads — A's Unasa Towing

## Resumen ejecutivo
- **1 campaña Search** ("Search | Towing | West Valley-Kearns | v1") con **3 ad groups**: genéricos "near me", ciudad (West Valley, Kearns, SLC, Sandy [C]) y accidente/recovery. Es el máximo del límite de fragmentación para <$600/mes (playbook §4). Las 8 mejores cuentas del paquete usan 1 campaña y 1 ad group (benchmark.md).
- **Presupuesto F1**: **$510/mes** (42.5% del paquete de $1,200, confirmado por Jhombis el 22-oct) → **$16.75/día** si es 24/7, o **$19.50/día** si el domingo va apagado (~26 días activos). Matemática: $16.75 ÷ CPC $6.5–7.5 ≈ **2.2–2.6 clics/día → ~68–78 clics/mes → ~10–14 llamadas** con la CVR de la cohorte nueva (14–18%). Las llamadas de ≥60 s serán menos.
- **Puja**: **Maximizar clics con tope de CPC de $7.50** (estándar 6), Presencia, frase + exacta. Pasa a **Maximizar conversiones** con 15+ conversiones/mes limpias, esperable hacia el **mes 3–4**.
- **CPL objetivo**: meses 1–2 sin objetivo, solo control ($33–65 esperado). **Meses 3–6: $24–36** (mediana Search del nicho ±20%). Meta madura: $10.8–16.2.
- **tCPA**: no antes del **mes 6**, con ~30 conversiones en 30 días y fijado desde el CPA observado. Con $510/mes, 30 en 30 días exige un CPL ≤ $17: solo pasa si la cuenta llega a CPL maduro.
- **Bloqueante económico**: el CPL máximo de referencia (~$17 con el piso de $79.99) queda por debajo de todo lo esperable hasta el mes 6. La cuenta solo es rentable si el ticket real es mayor (accidentes, exóticos, millaje). **No lanzar sin la respuesta del ticket.**

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| Search \| Towing \| West Valley-Kearns \| v1 | Llamadas ≥60 s (anuncio + web) y formulario (/thank-you/) | $16.75 (24/7) · $19.50 (dom off) | 100% | Max. clics, tope CPC $7.50 | **Presencia**. ZIP 84118, 84119, 84128, 84092 [C] + 84104 [C], 84120 [C]. Excluir resto de países | F1: lun–sáb 24 h, dom off (horario de la web) hasta que el cliente confirme 24/7 con alguien que conteste (America/Denver) |
| ~~Marca~~ | — | — | — | — | — | No: "unasa towing" tiene 20 búsquedas/mes y nadie puja por la marca (Semrush) |
| ~~LSA~~ | — | — | — | — | — | Towing no es categoría de Local Services Ads (brief) |

**Por qué una sola campaña:** la regla de aprendizaje pide ≥3× CPL/día por campaña, $72–108/día con un CPL de $24–36. Con $16.75–19.50/día no alcanza ni para una, así que todo va en una campaña y la prioridad se maneja por ad group y copy.

**Por qué tope de $7.50:** Semrush da $3.87–4.56 en los términos de SLC; en el MCC, una cuenta madura paga ~$6.0–7.1 en SLC calibrado y las nuevas pagan $6.8–9 en "near me" (benchmark.md). Un tope de $7.50 compra en el rango de las maduras sin quedar fuera de la subasta. Se revisa el día 7: si la pérdida de IS por ranking pasa de 50% y no se gasta el presupuesto, se sube a $9.

**Ritmo con domingo apagado:** con $19.50/día el tope mensual de Google (30.4× el diario) es $593, por encima de los $510. Se controla el gasto cada semana y se baja el diario si a mitad de mes va por encima del ritmo.

**Por qué el horario arranca sin domingo:** la web dice "Closed Sunday", hay 1 grúa y 1 conductor, y ya hubo 1 llamada abandonada de 3 en CallFire. Una llamada pagada que nadie contesta es desperdicio puro (estándar 10). Se abre el domingo cuando el cliente confirme quién contesta.

**Geo**: los 4 ZIP pedidos suman ~152–184k habitantes (web: zip-codes.com, statisticalatlas.com; 84118 tiene cifras inconsistentes entre fuentes). Es un área chica para $16.75/día y deja afuera la base (84104) y 84120, que también es West Valley City. Regla F1: si el día 7 el gasto va por debajo del 70% del presupuesto con IS perdido por ranking <30%, se amplía la geo (radio de ~8 mi desde la base o más ZIP confirmados).

**Configuración fija (estándares PMM):**
- Solo red de Búsqueda: sin socios ni Display (estándar 8).
- Recomendaciones automáticas apagadas. Rotación: optimizar. Sin exclusiones de audiencia. Idioma: inglés.
- Conversiones primarias: "Calls from ads" ≥60 s, "Website calls" ≥60 s (número de reenvío de Google en el sitio → (385) 473-9820, para que CallFire siga registrando) y envío de formulario en /thank-you/. Clic en el teléfono como secundaria.
- Lista universal PMM a nivel de cuenta + `data/negatives-nicho.txt` (178 términos) desde el día 1.

## Estructura por campaña
### Campaña: Search | Towing | West Valley-Kearns | v1
Volúmenes: Semrush US, mensual. "Local est." = nacional × 0.05% (inferido). Detalle en `data/keywords.csv`.

| Ad group | Keywords (match) | Vol. est./mes | Landing | H1 pinneado |
|---|---|---|---|---|
| **AG1 Towing Near Me** | [tow truck near me], [towing near me], [towing company near me], "tow truck near me", "towing near me", "towing company near me", "towing service near me", "tow service near me", "car towing near me", "flatbed towing near me", "flatbed tow truck near me", "towing service", "tow truck service", "24 hour towing near me" [C], "emergency towing near me" [C] | ~175 local est. | /towing-west-valley-kearns/ (crear) | Tow Truck Near You · Towing Service Near You · Local Flatbed Towing |
| **AG2 Towing West Valley & SLC** | [west valley towing], [towing salt lake city], [tow truck salt lake city], "west valley towing", "towing west valley", "towing west valley city", "tow truck west valley", "kearns towing", "tow truck kearns", "towing salt lake city", "tow truck salt lake city", "salt lake towing", "salt lake city towing", "towing sandy utah" [C], "tow truck sandy utah" [C] | ~690 en el metro (solo una parte cae en la geo) | /towing-west-valley-kearns/ (crear) | {KeyWord:West Valley Towing} · Towing in West Valley City · Kearns & West Valley Towing |
| **AG3 Accident & Recovery** | "accident towing near me", "accident recovery", "car accident towing", "winch out service near me", "winch out near me", "vehicle recovery" | <5 local est. (bajo; es el ticket alto) | /accident-recovery/ (mejorar) | Accident Towing & Recovery · Winch-Out & Vehicle Recovery · Wrecked Car? We Tow It |

**Por qué AG2 va separado:** los términos de ciudad suman ~690/mes en el metro (más de los 100 que pide un grupo propio) y necesitan un H1 con la ciudad. Con `{KeyWord:}` un solo grupo cubre West Valley, Kearns, SLC y Sandy sin forzar un grupo por ciudad.

**Por qué AG3 existe con tan poco volumen:** es el ticket que más ayuda a la economía del cliente (brief, competitors.md) y casi nadie tiene landing para eso en SLC. Con volumen chico no compite por presupuesto; si en 60 días no tiene impresiones, se pliega a AG1.

**Por qué no hay grupo "Emergency/24-7":** el horario no está confirmado. "24 hour" y "emergency" entran en AG1 solo si el cliente confirma 24/7 con alguien que conteste.

Negativas cruzadas entre grupos (para que cada búsqueda caiga en su grupo):
- **AG1**: west valley, kearns, salt lake, slc, sandy, accident, wreck, crash, winch, recovery.
- **AG2**: accident, wreck, crash, winch, recovery.
- **AG3**: west valley, kearns, salt lake, sandy (las búsquedas de accidente con ciudad caen en AG3 igual por "accident"; si no, se revisa en search terms).

## Keywords descartadas y por qué
| Keyword | Vol. | Motivo |
|---|---|---|
| cheap towing near me / cheap towing salt lake city | 14,800 nac. / 40 | No se puja: STUCK ancla $50 y cheaptowingsaltlake.com capta "cheap"; el piso de $79.99 ya no cierra la economía. **"cheap" no se negativiza**: en el MCC convierte igual que el genérico (towing-us.md), así que si entra por "towing near me" se deja |
| roadside assistance (near me / salt lake city) | 33,100 nac. / 50 | Mixta con AAA y aseguradoras; CPL de $43 en cuentas nuevas. Pendiente la pregunta #8 del brief |
| lockout / jump start / tire change / fuel delivery near me | 390–2,900 nac. | Ticket bajo con 1 grúa; fuel delivery cuesta $9.18. No se negativizan (son servicios del cliente): simplemente no se pujan en F1 |
| exotic / classic car towing | 320 / 320 nac. | Competencia baja (0.10–0.28) pero volumen local mínimo. F1: sitelink. F4: grupo propio si sube el presupuesto |
| medium duty / box truck towing | 390 / 260 nac. | PENDIENTE: qué mueve la F550 |
| motorcycle towing near me | 1,900 nac. | No está en los servicios del brief |
| sandy towing | 260 | Es Sandy's Towing, de Dayton, Ohio (competitors.md). Negativa |
| utah towing | 110 | Todo el estado: demasiado amplio para 4 ZIP |
| towing cost / how much does a tow cost | 1,600 / 1,600 nac. | No se puja; tampoco se negativiza "cost" o "price" (convierten en el MCC) |
| marcas de competidores (Stauffer's, Adams, Shamrock, Top Notch…) | 90–1,300 nac. | Regla PMM: no pujar salvo prueba controlada. Negativas |
| términos en español (grúa, servicio de grúa) | — | Sin evidencia de demanda en español en el área; fuera de mercados hispanos gasta sin convertir (benchmark.md). Negativas |

## Copy
En `data/ads-search.md`: 1 RSA por ad group (pauta <$1,500/mes), 15 headlines (3 propios pinneados en H1 + 12 del pool) y 4 descripciones, con sitelinks, callouts, snippets, llamada, precio [C] e imagen.
- Ángulos del gap de competencia (competitors.md):
  - **Precio claro de un operador local**: "Tows Starting at $79.99" [C] y "Upfront Price Before We Hook". Ningún operador local publica precio.
  - **Rotación policial como prueba** [C]: nadie la usa. Confirmar antes que siga vigente en West Valley City.
  - **Flatbed + wheel-lift, exóticos y clásicos**: encaja con la grúa del cliente.
  - **Local, no call center** [C]: contra el agregador STUCK (teléfono de Florida).
- Prohibido hasta confirmar: "24/7", tiempos de llegada, número de reseñas, "Licensed & Insured", cualquier precio por debajo de $79.99.

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| /towing-west-valley-kearns/ (AG1, AG2): H1 con West Valley/Kearns, formulario de 3 campos arriba, llamada sticky, horario real, reseñas cuando haya GBP | No | PMM (WordPress del cliente o `/landing` en performancemediamarketing.com/as-unasa-towing/ si no hay acceso) | **Sí** |
| /thank-you/ (conversión de formulario) | No | PMM | **Sí** |
| /accident-recovery/ (AG3): formulario arriba, foto real | Sí, con mejoras | PMM | No (AG3 puede arrancar con la actual) |
| /exotic-classic-vehicle-transport/ (sitelink) | Sí | PMM | No |
| Header de todas las páginas: logo real en lugar del placeholder "Logo." | Placeholder | Cliente (elige) + PMM | No, pero resta confianza desde el primer clic |

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |
|---|---|---|---|
| **F0 — Medición, landing y respuestas** (ya) | $0 | — | Ticket y margen confirmados (CPL máximo); horario y área confirmados; Google tag + 3 conversiones probadas con Tag Assistant; /towing-west-valley-kearns/ y /thank-you/ publicadas; universal + nicho aplicadas |
| **F1 — Lanzamiento** (días 1–30) | $510 | 100%, $16.75/día (o $19.50 sin domingo). Max. clics, tope $7.50 | ≥50 clics; search terms revisados los días 7 y 14; tasa de contestadas ≥80% en CallFire; sin términos fuera de geo |
| **F2 — Limpieza** (días 31–90) | $510 | Igual. Ajustar tope según IS perdido por ranking. Pausar un ad group con gasto ≥2× CPL objetivo (~$72) y 0 conversiones | **15+ conversiones/mes limpias** (≥60 s) → Maximizar conversiones (esperable mes 3–4) |
| **F3 — Maximizar conversiones** (mes 3–6) | $510 → propuesta de subir si IS perdido por presupuesto >40% y CPL ≤ $36 | 100% | ~30 conversiones en 30 días → tCPA = CPA observado de 30 días (no antes del mes 6) |
| **F4 — Expansión** (mes 4+) | Según F3 | Grupo de exóticos y clásicos; roadside o medium-duty solo si el cliente los confirma y hay presupuesto. RLSA: baja prioridad (compra urgente, no se repite) | CPL ≤ objetivo sostenido 30 días |
| **F5 — PMax** | — | Ver "Por qué NO" | Condiciones de `knowledge/estrategias/pmax-cuando-y-como.md` |

**Límites de bajo volumen (playbook §9):** con ~2.5 clics/día no se puede leer una tasa de conversión antes de la semana 3–4 (~50 clics), ni comparar ad groups entre sí en el trimestre, ni hacer A/B de anuncios. AG3 probablemente no junte clics suficientes para concluir nada en 90 días.

## Por qué NO (todavía)
- **PMax**: requiere Search estable, 30+ conversiones/mes con tracking confiable, assets propios y exclusión de marca. Hoy no hay tracking, ni GBP, ni logo. En el MCC, las 2 cuentas que lo lanzaron antes de los 3 meses lo pausaron (towing-us.md).
- **Amplia / AI Max**: el MCC está casi todo en amplia y el 23% del gasto Search del nicho se fue en términos sin conversión. Frase + exacta hasta ~50 conversiones limpias y aprobación de Jhombis.
- **Display / Demand Gen / Video**: el remolque es una necesidad inmediata; no se crea demanda.
- **Campaña de marca**: "unasa towing" tiene 20 búsquedas/mes. Se agrega en exacta si aparece en search terms.
- **Remarketing**: audiencia mínima con ~80 clics/mes, y la compra no se repite.
- **Roadside como grupo propio**: ticket bajo, CPC alto (lockout $5, fuel $9.18) y 1 grúa. Pendiente de lo que conteste el cliente.

## Historial de cambios
- 2026-10-22 v1: creada con $540/mes de referencia.
- 2026-10-22 v1.1: gasto real confirmado por Jhombis: 42.5% de $1,200 = $510/mes. Presupuesto diario $16.75 (24/7) o $19.50 (sin domingo); estructura, puja y tope sin cambios.

## Riesgos y supuestos
1. **La economía no cierra con $79.99.** CPL máximo de referencia ~$17 contra $33–65 en los meses 1–2 y $24–36 en los meses 3–6. Si el ticket promedio real es cercano a $80, la cuenta pierde plata hasta madurar. Es bloqueante.
2. **Geo chica.** 4 ZIP (~152–184k habitantes) pueden no alcanzar para gastar $16.75/día. Se mide el día 7.
3. **Capacidad de respuesta.** 1 grúa y 1 conductor: si está en un servicio, la siguiente llamada se puede perder. Se mide la tasa de contestadas en CallFire cada semana; <80% es problema del cliente, no de la campaña.
4. **Max. clics en el MCC sale peor.** Las 4 cuentas de towing que hoy lo usan tienen CPL de $42–80 o 0 conversiones, pero Windsor no muestra si tenían tope y son casi todas nuevas (benchmark.md). Se mantiene el estándar 6 con tope, frase, negativas desde el día 1 y salida temprana a Maximizar conversiones apenas haya 15/mes.
5. **El CPL real va a ser mayor que el benchmark.** El benchmark cuenta llamadas sin calificar; aquí la conversión es una llamada de ≥60 s.
6. **Sin GBP ni reseñas.** Stauffer's (~4.9★, 424–627) y 4 Wheel (4.7★, 646) dominan la confianza y Maps. Sin activo de ubicación ni seller ratings.
7. **Rotación policial.** West Valley City evalúa reemplazarla por un proveedor único (competitors.md). Si cambia, el headline C6 y la descripción D3 se quitan.
8. **CPC por encima de Semrush.** En el MCC, el CPC real de una cuenta nueva sale 2.2–3.5× Semrush. Si el día 7 el CPC promedio choca contra el tope y no se gasta, se sube a $9.
