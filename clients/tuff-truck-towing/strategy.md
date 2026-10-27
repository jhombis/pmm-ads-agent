---
cliente: Tuff Truck Towing
slug: tuff-truck-towing
actualizado: 2026-10-27
version: 1.1
customer_id: 727-278-3398
supuestos:
  - Pauta en medios confirmada: 52.5% del paquete de $1,400 = $735/mes (Jhombis, 27-oct).
  - La cuenta 727-278-3398 está conectada a Windsor (27-oct) y está vacía: sin campañas, acciones de conversión ni gasto. No se pudo leer su zona horaria (Windsor no devuelve filas sin campañas): verificarla antes de programar el horario.
  - Ticket y margen por línea PENDIENTES. No hay CPL máximo: se usa el CPL del benchmark como objetivo provisional.
  - Límites de Tulsa PENDIENTES con Bree (Memorial Dr / Hwy 51). Claremore es condicional.
  - Peso máximo que mueve el cliente sin confirmar: "heavy equipment" queda fuera hasta saberlo.
  - Volumen local estimado como volumen nacional de Semrush × ~0.08%, una proporción de población supuesta (inferido; ~260k habitantes en el área, sin censo verificado). Keyword Planner geolocalizado sin correr.
  - Horario lun–vie 7–21 tomado del cliente. La web dice 24/7: el copy no lo promete.
---

# Estrategia Google Ads — Tuff Truck Towing

## Resumen ejecutivo
- **1 campaña Search** ("Towing & Hauling") con **3 ad groups**:
  - T1 Towing Near Me
  - T2 Towing Ciudades
  - E1 Equipment & Container Hauling, como **prueba**
  
  Va en la cuenta **727-278-3398**. Sin marca, sin PMax, sin Display.
- **Matemática** (playbook §4):
  - Pauta de **$735/mes** → **$34/día** en días activos (lun–vie, ~21.7 días/mes).
  - CPC real esperado de ~$8.24 (cuentas nuevas del MCC; Oklahoma $8.49) → **~4.1 clics por día activo, ~90 clics/mes**.
  - Con la tasa de conversión de cuentas nuevas (15.5%) → **~14 conversiones/mes en los meses 1–2**. Desde el mes 3, 22–28 (benchmark).
- **Puja**: Maximizar clics con **tope de CPC de $9** mientras haya menos de 15 conversiones/mes. Se pasa a **Maximizar conversiones** con 15+ conversiones/mes estables y medición limpia, probablemente en el mes 2–3.
- **CPL objetivo**: ~$51 en los meses 1–2 (cohorte nueva) y **$21–40 desde el mes 3** (mediana Search ±20%). Meta a 6 meses: ~$15. El **CPL máximo del cliente está PENDIENTE** (ticket y margen).
- **tCPA**: no antes del **mes 4–6**, y solo con ~30 conversiones calificadas en 30 días, desde el CPA observado. Con $735, el horario comercial y la geo recortada, es probable que no se llegue (ver Riesgos).

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| Search \| Towing & Hauling \| BA-East Tulsa \| v1 | Llamadas ≥60 s (+ formulario cuando exista) | **$34** ($735/mes) | 100% | Maximizar clics, tope de CPC $9 | **Presencia**. Ciudades: Broken Arrow, Bixby, Coweta, Catoosa. Tulsa **solo al este de Memorial Dr** (ZIP completos y pines, con exclusiones; ver abajo). Claremore condicional. Excluir el resto de países | **Lun–vie 7:00–21:00** America/Chicago |
| ~~Marca~~ | — | — | — | — | — | No en F1: "tuff truck towing" tiene 90 búsquedas/mes, el sitio está #1 orgánico y nadie puja por la marca (Semrush). Si aparece en search terms con CPC bajo, se agrega en exacta a T2 |
| LSA (pista paralela) | Llamadas | Presupuesto aparte, a definir | — | — | Mismas ciudades | Igual al horario |

**Por qué una sola campaña.**
- La regla de aprendizaje pide ≥3× CPL por día y campaña: $153/día con CPL de $51. Con $34/día no alcanza ni para una, así que no se separa towing de hauling en campañas distintas.
- El límite de fragmentación para $600–1,500 es **1 campaña con 3–5 grupos**. Aquí son 3, con lugar para 1 de Claremore.
- El cuartil superior del benchmark (CPL de $8–13) usa justo esto: una campaña "Radius" con 1–2 grupos consolidados.

**Cómo se arma la geo de Tulsa.**
- Google Ads no admite polígonos, así que Tulsa se arma con:
  - ZIP completos que queden **al este de Memorial Dr**;
  - pines de radio chico para los ZIP que cruzan Memorial;
  - **exclusión** del resto de Tulsa (ciudad) para que la ubicación por presencia no se extienda.
- La lista de ZIP sale del mapa con Bree antes de /build-campaign. No se usa "Tulsa" como ciudad objetivo en ningún caso.

**Por qué el horario no lleva margen.** El estándar es horario comercial + margen, pero el cliente dio lun–vie 7–21. Una llamada pagada que nadie atiende es desperdicio puro. CallFire muestra llamadas contestadas un sábado, así que se amplía a fin de semana solo si el cliente confirma que contesta (pregunta abierta).

**Presupuesto con programación solo de lunes a viernes.** $34/día × ~21.7 días activos ≈ $738/mes. El tope mensual de Google es $34 × 30.4 = $1,034, así que hay que vigilar la semana 1 para que el gasto no pase de ~$170 (5 días × $34).

**Configuración fija (estándares PMM):**
- Solo red de Búsqueda: sin socios ni Display.
- Recomendaciones automáticas apagadas.
- Rotación optimizada.
- Sin exclusiones de audiencia.
- Idioma inglés.
- Todos los dispositivos.

## Estructura por campaña
### Campaña: Search | Towing & Hauling | BA-East Tulsa | v1
Volúmenes: Semrush US. "Local est." es el volumen nacional × ~0.08% para los "near me", o el volumen de ciudad tal cual. Detalle en `data/keywords.csv`.

| Ad group | Keywords (match) | Vol. est./mes | Landing | H1 pinneado |
|---|---|---|---|---|
| **T1 Towing Near Me** | [towing near me], [tow truck near me], [towing company near me], "towing near me", "tow truck near me", "towing company near me", "tow truck company near me", "towing service near me", "tow service near me", "car towing near me", "truck towing near me", "cheap towing near me", "cheap tow truck near me", "flatbed towing near me", "flatbed tow truck near me", "rollback tow truck near me", "medium duty towing", "box truck towing", "towing near me open now" | ~290 local est. (375k nacional) | /towing (crear) | Tow Truck Near You · Towing Service Near You |
| **T2 Towing Ciudades** | [towing broken arrow], [tow truck broken arrow], [towing tulsa], [tow truck tulsa], "towing broken arrow", "broken arrow towing", "tow truck broken arrow", "wrecker service broken arrow", "towing bixby", "tow truck bixby", "towing coweta", "tow truck coweta", "towing catoosa", "tow truck catoosa", "towing tulsa", "tow truck tulsa", "towing company tulsa", "towing service tulsa", "wrecker service tulsa" · [C] "tow truck claremore" | Broken Arrow ~220. Tulsa: 1,570 en toda la ciudad, de los que solo entra la parte este (s/d). Bixby, Coweta y Catoosa sin datos en Semrush | /towing (crear; bloque de área de servicio) | {KeyWord:Broken Arrow Towing} · Towing in Broken Arrow, OK |
| **E1 Equipment & Container Hauling** (prueba) | [equipment hauling near me], [forklift transport], [forklift towing], "equipment hauling", "equipment transport near me", "equipment hauling services", "construction equipment hauling", "forklift towing near me", "forklift hauling", "forklift moving", "skid steer transport", "skid steer hauling", "tractor hauling", "machinery moving tulsa", "flatbed hauling near me", "shipping container hauling", "container hauling near me", "container moving near me", "conex box moving", "20 ft container transport", "lumber hauling" | ~5–10 local est. + "machinery moving tulsa" (70). **Muy bajo**: es una prueba | /equipment (crear) | {KeyWord:Equipment Hauling} · Equipment & Forklift Hauling |

- **Medium-duty va dentro de T1, no en un grupo propio.** En el MCC hay 2 clics en 12 meses (benchmark) y la demanda local es mínima. El copy de T1 y T2 dice "Light & Medium-Duty" y "Cars, Pickups & Box Trucks".
- **Por qué T2 agrupa ciudades.** Ninguna ciudad de la geo pasa de 100 búsquedas/mes una vez recortada: Broken Arrow suma ~220 entre todas sus variantes, y de Tulsa solo entra la parte este. Por eso van con inserción de keyword en el H1, no en un grupo por ciudad. Si Broken Arrow solo supera 50 clics/mes, se evalúa separarla en F3.
- **Por qué E1 es una prueba.**
  - En el MCC el tema está sin probar: 11 clics en 12 meses.
  - El volumen local es bajo y el CPC es alto ($5–8).
  - Ningún competidor tiene una página de forklifts ni de skid steers (competitors.md).
  - Se activa **solo con la landing /equipment publicada** y se evalúa a los **50 clics** o a los 90 días, lo que pase después. No tiene CPL objetivo propio hasta conocer el ticket.
- **Por qué no hay grupo "Emergency/24-7".** El cliente no es 24/7.

Negativas cruzadas por ad group (para que cada búsqueda caiga en su grupo):
- **T1**: broken arrow, bixby, coweta, catoosa, tulsa, claremore, equipment, forklift, skid steer, container, conex, lumber, tractor, machinery.
- **T2**: near me, equipment, forklift, skid steer, container, conex, lumber, tractor, machinery.
- **E1**: tow truck, towing near me, car towing, flatbed towing, wrecker.

## Keywords descartadas y por qué
| Keyword | Vol. | Motivo |
|---|---|---|
| tuff truck towing (marca) | 90 | Sin campaña de marca: ya está #1 orgánico y nadie puja por ella |
| heavy equipment hauling (+ near me) | 1,900 / 320 | [C] Solo si el camión del cliente lo carga; hoy está fuera |
| machinery moving (sin ciudad) | 480 | Mezcla rigging y mudanzas industriales; solo va la versión con Tulsa |
| shipping container moving / storage container moving | 1,000 / 880 | CPC de $7.75–7.87 y mezcla compra y mudanza tipo PODS |
| moving a shipping container | 260 | Informacional, CPC $8.23 |
| material hauling near me / dump truck | 110 / — | Volteo (/hauling): fuera del foco del brief y con otro teléfono |
| lumber delivery near me | 390 | Retail (aserraderos, home centers) |
| roadside assistance tulsa | 40 | Fuera del foco; en el benchmark sale a $67–154 en amplia |
| semi / 18 wheeler / heavy duty towing | — | No lo ofrece |
| hot shot hauling, load board, dispatch | — | Brokers y carga por contrato, no cliente final |
| competidores por nombre | — | Regla PMM |
| español (grúa) | — | No hay mercado hispano relevante ni ad group en español |

Lista completa en `data/negatives-nicho.txt`: ~170 términos de nicho, área, competidores y ruido de equipment, más la universal PMM a nivel de cuenta. **De la universal no se aplican "equipment" ni "cheapest".**

## Copy
Está en `data/ads-search-towing-hauling.md`:
- 1 RSA por grupo, con 15 headlines y 4 descripciones; longitudes validadas por script.
- **Ángulos sacados del gap de competencia:**
  - Licencia visible ("OK DPS Licensed Wrecker", DPS #53342-W): ningún competidor la muestra.
  - "Family-Owned" y "Based in Broken Arrow, OK".
  - "Light & Medium-Duty" y "Cars, Pickups & Box Trucks".
  - En E1: forklifts, skid steers y contenedores de 20 ft, temas sin dueño en la zona.
- **Prohibido:** 24/7, años, reseñas, tiempos de llegada, heavy-duty y teléfonos en el texto.
- **Pendientes de confirmar [C]:** horario visible, "Free Hauling Quote", "Talk to a Local Dispatcher".
- **Extensiones:**
  - llamada con número de reenvío de Google, en el horario del cliente;
  - 4 sitelinks, que dependen de las landings;
  - 6 callouts y el snippet "Services";
  - ubicación cuando haya acceso al GBP;
  - imágenes con fotos reales [C].

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| /towing (T1, T2). H1 "Light & Medium-Duty Towing in Broken Arrow & East Tulsa". Llamada fija en móvil, formulario de 4 campos con /thank-you, horario real, DPS/MC/DOT, área de servicio (BA, Bixby, Coweta, Catoosa, este de Tulsa) y bloque de medium-duty | No | PMM (/landing) o Cliente (Wix) | **Sí** |
| /equipment (E1). H1 "Equipment, Forklift & Container Hauling". Formulario de cotización (qué se mueve, origen, destino, fecha), llamada y peso máximo | No | PMM o Cliente | Sí para activar E1. T1 y T2 pueden lanzar sin ella |
| Home tufftrucktowing.com | Sí (7/22) | Cliente | No se usa como URL final mientras no tenga formulario ni un solo teléfono |

Mínimos del estándar 11 (ver `audit-site.md`):
- número de reenvío de Google con la conversión de llamada desde la web;
- un solo teléfono;
- prueba social (widget del GBP);
- carga rápida en móvil.

**Dónde se publican:** en el Wix del cliente si da acceso a tiempo, o con `/landing` en performancemediamarketing.com/tuff-truck-towing/. La decisión es de Jhombis.

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |
|---|---|---|---|
| **F0: medición, landings, geo** (ya) | $0 | — | Google tag de la cuenta 727-278-3398 en la landing; llamadas desde anuncios ≥60 s y llamada desde la web (número de reenvío) **probadas con Tag Assistant**; landing /towing publicada; ZIP de Tulsa confirmados con Bree; negativas universales + nicho aplicadas; geo confirmada |
| **F1: lanzamiento T1 + T2** (días 1–30) | $735 | $34/día, Max. clics con tope de $9. E1 en pausa hasta que exista /equipment | ≥14 días y ≥80 clics; search terms revisados los días 7 y 14 |
| **F2: E1 + optimización** (días 31–60) | $735 | Igual; E1 se activa si /equipment existe. Se pausan las keywords con gasto ≥2× CPL objetivo (~$100) y 0 conversiones | **15+ conversiones/mes estables** con medición limpia → Maximizar conversiones |
| **F3: Max. conversiones y escala** (días 61–120) | $735 → proponer más presupuesto si el IS perdido por presupuesto es >40% y el CPL está en objetivo | Max. conversiones sin tCPA | CPL ≤ $40 sostenido 30 días. Se evalúa E1 (50 clics) |
| **F4: tCPA** | igual | tCPA = CPA observado de 30 días ×1.1 | Solo con ~30 conversiones calificadas en 30 días (probablemente no antes del mes 4–6) |
| **F5: RLSA / PMax** | — | Ver "Por qué NO" | Condiciones de `knowledge/estrategias/pmax-cuando-y-como.md` |
| **LSA** (paralelo desde F0) | Aparte, a definir | — | GBP verificado + seguro + background check (2–4 semanas). Confirmar que la categoría Towing esté disponible en Broken Arrow |

**Límites de bajo volumen** (playbook §9): con ~90 clics/mes:
- No se podrá comparar T1 contra T2, ni el rendimiento por ciudad o dispositivo, antes del mes 2.
- No se podrá juzgar E1 antes de los 50 clics: probablemente meses.
- Nada de A/B de anuncios. Se decide por search terms, por dinero gastado sin conversión y por llamadas calificadas en CallFire, no por tasas sobre menos de 50 clics.

## Por qué NO (todavía)
- **PMax**: requiere Search estable, 30+ conversiones/mes con tracking confiable, assets propios y exclusión de marca. Hoy no hay tracking verificado, GBP ni historial. En el benchmark, las cuentas que lo lanzaron antes de los 3 meses lo pausaron.
- **Amplia / AI Max**: amplia domina en el MCC y se lleva el 23% del gasto Search en términos sin conversión (competidores, otras ciudades). Aquí, además, la geo de Tulsa es fina y amplia la rompería. Se usa frase + exacta hasta tener ~50 conversiones limpias y la aprobación de Jhombis.
- **Display / Video / Demand Gen**: el remolque es una necesidad inmediata y no se crea demanda.
- **Campaña de marca**: 90 búsquedas/mes, ya #1 orgánico y sin competidores pujando (Semrush).
- **Remarketing / RLSA**: la compra es urgente y no se repite. Puede tener sentido más adelante para hauling B2B (contratistas que vuelven), con listas de ≥1,000 usuarios.
- **Roadside** (lockout, jump, fuel): la web lo ofrece, pero el cliente no lo pidió como foco, y "roadside assistance" compite con AAA y las aseguradoras. Se agrega solo si el cliente lo pide.
- **Maximizar conversiones desde el día 1**: sin historial ni conversiones verificadas, el algoritmo no tiene señal (estándar 6). Max. clics con tope es solo el punto de partida: las cuentas del MCC que se quedan ahí tienen CPL de $70–83.

## Riesgos y supuestos
1. **El horario recorta la demanda.** Los 7 competidores venden 24/7. Con lun–vie 7–21 se cubre el 42% de las horas de la semana. Es el mayor techo de la cuenta y es decisión del cliente.
2. **Hay llamadas orgánicas mezcladas.** El número de tracking (918) 320-7595 ya recibe ~6 llamadas/día desde la web. Si Ads no se mide con el número de reenvío de Google, el CPL sale artificialmente bajo. Sin esa conversión probada, no se lanza.
3. **Presupuesto justo para 3 grupos.** $735/mes está apenas por encima del límite de $600 del playbook. Si el CPC real supera ~$11, los clics bajan de 3/día y E1 deja de tener sentido.
4. **CPL máximo sin calcular.** Ejemplo ilustrativo, no cifra del cliente: un remolque de $150 con 40% de margen y 50% de cierre da un CPL máximo de ~$9 (×0.3). Con un ticket así, el objetivo de $21–40 no sería rentable. Por eso el ticket es bloqueante para validar el objetivo.
5. **CPC real ~2× Semrush.** En Oklahoma se pagan $8.49 frente a $3.35–4.59 en Semrush. Si el CPC supera $9 en las primeras semanas, Max. clics con tope va a frenar el volumen. En ese caso se revisa el tope, no se quita.
6. **La geo de Tulsa es fina.** Si los ZIP quedan mal o se usa "Presencia o interés", se paga por clics de toda Tulsa que el cliente no va a atender.
7. **Cuenta 727-278-3398 sin auditar.** No está en Windsor y no hay API en la sesión. Antes de /build-campaign hay que revisar si ya tiene campañas, conversiones o recomendaciones automáticas activas.
8. **Tag AW-1004387232 en la web**, de otra cuenta. Si se suma al de PMM, puede contar conversiones doble. Hay que resolverlo en F0.
