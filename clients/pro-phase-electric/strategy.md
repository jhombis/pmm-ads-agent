---
cliente: Pro Phase Electric
slug: pro-phase-electric
pais: US
actualizado: 2026-09-23
version: 2
supuestos:
  - Ticket promedio, margen y tasa de cierre desconocidos → sin CPL máximo; se usa el CPL objetivo del benchmark ($40–60 por llamada)
  - Volúmenes = Semrush nacional × 0.18% (población de NWA), salvo las keywords con ciudad, que ya son locales. Sin Keyword Planner (no hay google-ads.yaml)
  - Área de servicio = condados de Benton y Washington + Huntsville (Madison). Falta confirmar Siloam Springs, Gentry y el oeste de Benton
  - Landings de paneles y EV no existen; sus ad groups quedan pausados hasta F2
  - Velocidad móvil y vista móvil del sitio sin verificar (audit-site.md)
  - PMM no tiene acceso al GBP → sin activo de ubicación en F1
  - No instala generadores (se niegan hasta confirmar)
  - El cliente atiende de 5:00 a 16:00 los 7 días y tiene alguien que contesta en ese horario
---

# Estrategia Google Ads — Pro Phase Electric

## Resumen ejecutivo
- **1 campaña Search**, "Search NWA", con **4 ad groups**: 2 activos en F1 (**Electrician - NWA**, que incluye near me y todas las ciudades, y **Electrical Repair**) y 2 que se activan en F2 cuando existan sus landings (**Paneles** y **EV**). Se reemplaza la campaña actual (Max. clics, broad, 1 RSA, 736 negativas heredadas).
- **Presupuesto: $825/mes ≈ $27/día**, todo en esa campaña. No alcanza para dividir por servicio ni para muchos ad groups: la regla de aprendizaje pide ≥3× CPL/día (~$120–180) y ni una sola campaña llega.
- **Puja: Max. conversiones sin tCPA.** Conversión principal: llamadas ≥60 s (anuncio + sitio) y formulario. Solo match de frase y exacta.
- **CPL objetivo: $40–60 por llamada** (benchmark, grupo Max. conversiones ajustado al CPC de NWA). Se esperan **~12–20 llamadas/mes**.
- **tCPA no es alcanzable con este presupuesto** (hacen falta ~30 conv./30 días). Con $1,500–1,800 de pauta se llegaría en ~60 días desde F1. Sin marca, PMax, Display ni RLSA en esta etapa. LSA queda como pista paralela, sujeta a GBP y documentos.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| Pro Phase Electric - Search NWA - $1500/mo. - [fecha de lanzamiento] | Llamadas + formularios | $27 | 100% | Max. conversiones (sin tCPA) | **Presencia**: condados de Benton y Washington (AR) + Huntsville (AR). Resto excluido | L–D 5:00–16:00 (zona horaria de la cuenta) |
| *(actual)* Pro Phase Electric - ENHPRM Radius - $1500/mo. - 09/01/2026 | — | $27 → **se pausa** el día que sale la nueva | — | Max. clics (hasta F1: techo de CPC $12) | — | — |

Configuración fija (estándares PMM): socios de búsqueda y Display **apagados**, aplicación automática de recomendaciones **apagada**, rotación **optimizar**, idioma EN, sin segmentos de audiencia como exclusión.

**Por qué una campaña nueva y no reestructurar la actual:** la actual tiene 3 semanas de historia, 1 conversión y una plantilla de 736 negativas de otra cuenta (Grand Junction). No hay aprendizaje que conservar, y empezar limpio evita arrastrar negativas que bloquean servicios. Las conversiones y el historial de la cuenta se conservan igual.

## Estructura por campaña
### Campaña: Search NWA
| Ad group | Fase | Keywords (match) | Vol. est. NWA/mes | Landing | H1 pinneado (RSA A/B/C) |
|---|---|---|---|---|---|
| Electrician - NWA | F1 | [electrician near me], [electricians near me], [electrician], [electricians], [local electrician], [electrician fayetteville], [electrician rogers], [electrician springdale], [electrician bentonville] + frase: "licensed electrician", "residential electrician", "electrician northwest arkansas", "fayetteville electrician", "electricians rogers", "electrician bella vista", "electrician centerton"… (44) | ~1,500 sin contar [electrician] (~2,160 con él) | `/` | {KeyWord:Licensed NWA Electrician} / Licensed Electrician Near You / Northwest Arkansas Electrician |
| Electrical Repair | F1 | [electrical repair near me], [circuit breaker repair], [outlet repair] + frase: "circuit breaker replacement", "electrical troubleshooting", "wiring repair", "lighting repair near me"… (14) | ~117 | `/` (F2: `/electrical-repair/` opcional) | Electrical Repair in NWA / Breaker & Outlet Repair / Electrical Repairs Done Right |
| Electrical Panel Upgrade | **F2** (pausado) | [electrical panel upgrade], [electrical panel replacement], [breaker box replacement], [panel upgrade near me] + frase: "fuse box replacement", "200 amp panel upgrade", "electrical service upgrade"… (15) | ~48 | `/electrical-panel-upgrade/` **(crear)** | Electrical Panel Upgrades / Panel Replacement in NWA / 200 Amp Panel Upgrades |
| EV Charger Installation | **F2** (pausado) | [ev charger installation], [ev charger installation near me], [tesla charger installation], [electric car charger installation] + frase: "tesla wall connector installation", "level 2 charger installation", "nema 14-50 outlet installation"… (14) | ~157 | `/ev-charger-installation/` **(crear)** | EV Charger Installation / Home EV Charger Installers / Tesla & Level 2 Installs |

**Por qué solo 2 ad groups activos (v2, 23-sep).** En la v1 separé cada ciudad con ≥100 búsquedas/mes aplicando la regla STAG al pie de la letra. Con $27/día el límite es el presupuesto, no la demanda: ~80 clics/mes contra ~2,000 búsquedas comerciales, y hoy ya se pierde 47% de IS por presupuesto. Con 6 grupos quedaban ~13 clics por grupo y ~4 por RSA al mes, datos inútiles para las revisiones D7/D14/D30. Las ciudades comparten la misma intención ("necesito un electricista"), así que van juntas. La relevancia del titular se mantiene con inserción de keyword en el H1 del RSA A (`{KeyWord:Licensed NWA Electrician}` → "Electrician Rogers"). Por eso las keywords de ciudad van **sin "ar"**. Reparación va aparte porque la intención y el anuncio son distintos (un problema concreto). Paneles y EV van aparte por ticket, landing y copy propios. **Separar ciudades es decisión de F3**: si sube el presupuesto, o si los search terms muestran que una ciudad convierte distinto o tiene QS bajo.

**Enrutamiento (negativas de frase por ad group):**
- NWA: panel, breaker box, ev charger, car charger, tesla, repair.
- Repair: panel, breaker box, ev, charger, tesla.

En F1, las búsquedas de paneles y EV no se sirven, porque no hay landing. Es deliberado (estándar 11).

**Sin ad group de Emergencia/24-7:** el cliente no atiende 24/7. "emergency", "24 hour", "24/7" y "after hours" son negativas.

Detalle de keywords: `data/keywords.csv` (87 activas + descartadas).

## Keywords descartadas y por qué
| Keyword | Vol. US | CPC | Decisión | Por qué |
|---|---|---|---|---|
| electrical services / home electrical / electrical contractors | 33,100 / 1,000 / 9,900 | $11–13 | Fuera en F1 | Genéricas. En el MCC: $1,637 → 5 conv. (cuenta D); en Pro Phase: $394 → 1 conv. |
| emergency / 24 hour electrician | 27,100 / 12,100 | $20–21 | Negativa | No es 24/7 |
| same day electrician | 1,000 | $30 | Fuera en F1 | No hay promesa de mismo día confirmada; CPC $30 |
| generator installation | 60,500 | $14 | Negativa | No está en la lista de servicios (confirmar) |
| ceiling fan / recessed lighting / light fixture installation | 49,500 / 27,100 / 4,400 | $5–6 | No se puja en F1 (**no se niega**) | Ticket bajo; D gastó $152 con 0 conv. Si entran por el grupo NWA, son leads válidos |
| gfci outlet installation, breaker keeps tripping | 40,500 / 4,400 | $2–4 | Fuera | Informacionales / DIY. "breaker keeps tripping" puede probarse en F3 |
| smoke detector, doorbell, thermostat, data line | — | — | No se puja (no se niega) | Ticket bajo |
| prophase electric (marca) | 40 + 40 | — | Negativa en Search | Orgánico en posición 3. Sin campaña de marca en F1 (ver "Por qué NO") |
| Competidores y empresas de energía | — | — | Negativa | Estándar 5; $137 perdidos en 11 días |

## Copy
Completo en **`data/ads-search-nwa.md`** (largos validados por script). Por ad group: 3 RSA con H1 pinneado a la keyword y 14 headlines sin pin que rotan beneficios y ofertas:
- **Confianza**: Licensed, Bonded & Insured · 4.9-Star Rated on Google · Nextdoor Neighborhood Fave
- **Diferenciales frente a competencia**: Open 7 Days a Week · Weekend Service Available · Early Appointments From 5 AM · Fair, Honest Pricing · We Show Up When We Say
- **Oferta**: Get a Free Quote Today
- **Local**: Local NWA Electricians · Serving All of NW Arkansas · Rogers, Fayetteville & More

4 descripciones: una propia del ad group y 3 compartidas (confianza + quote, horario de 7 días, precio justo + puntualidad).

Extensiones:
- Llamada, con horario de 5 a 16.
- 5 sitelinks: Free Quote, Reviews, Services, Safety Inspections, Residential. Se agregan Panel y EV en F2, y se quita /portfolio/.
- 8 callouts.
- Snippet "Service catalog".
- Imágenes propias del portfolio.
- Ubicación: pendiente del acceso al GBP.

**No se usa:** "same day", "24/7", "emergency" ni número de reseñas (no está confirmado).

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| `/` (H1 → "Licensed Electrician in Northwest Arkansas…") | Sí (H1 genérico) | PMM o cliente (quién edita: PENDIENTE) | No. Mejora QS y experiencia de landing |
| `/electrical-panel-upgrade/` | **No** | PMM o cliente | **Sí para el ad group de Paneles (F2)** |
| `/ev-charger-installation/` | **No** | PMM o cliente | **Sí para el ad group de EV (F2)** |
| `/electrical-repair/` | No | PMM o cliente | No (la home cubre) |
| Página de gracias del formulario (`/thank-you/`) o evento de envío | ? | PMM | **Sí, para lanzar F1** (estándar 7) |
| `/fayetteville-electrician/` y las otras 3 ciudades | No | — | No (F3, solo si se separan ciudades y su QS sigue bajo) |

## Presupuesto por fase
| Fase | Fechas est. | Total/mes | Por campaña | Qué pasa | Condición para pasar |
|---|---|---|---|---|---|
| **F0 — Contención + tracking** | 23-sep → ~30-sep | $825 (campaña actual) | Actual: $27/día | En la campaña actual: importar `2026-09-22-negatives-editor.csv`, pausar las keywords broad "home electrical", "electrical services", "electrical contractors" y "home electrical services", y poner techo de CPC de $12. Configurar las conversiones de llamadas del sitio y del formulario. Presencia, horario, socios y Display apagados. Pedir acceso al GBP | Llamadas del sitio + formulario **probados con Tag Assistant** (≥1 conversión de prueba en cada acción) |
| **F1 — Lanzamiento Search NWA** | ~1-oct → ~21-oct | $825 | Search NWA: $27/día (la actual se pausa) | 2 ad groups (NWA + Repair), Max. conversiones. Revisión de search terms los días 3, 7 y 14 | Landings de paneles y EV publicadas y auditadas **y** ≥14 días de F1 sin problemas de tracking |
| **F2 — Paneles + EV** | ~22-oct → ~15-nov | $825 | Search NWA: $27/día | Activar los ad groups de Paneles y EV, con sus sitelinks | 30 días desde F1, ≥10 conversiones, CPL ≤ $60 |
| **F3 — Optimizar y proponer escala** | ~15-nov → | Propuesta: $1,500–1,800 | Search NWA (única); ad group Marca solo si hay competidores pujando por ella | Reasignar según el CPA por ad group; evaluar separar ciudades, pausar lo que gaste >2× CPL sin conversión, proponer más presupuesto. Separar Paneles+EV en campaña propia solo si queda ≥3× CPL/día | ~30 conv./30 días → **tCPA** al CPA real +10–20% |
| F4 — RLSA | después de F3 | — | Observación | Listas de visitantes. Con el tráfico actual difícilmente llegan a 1,000 usuarios | Lista ≥1,000 usuarios |
| F5 — PMax | no planificada | — | — | Ver "Por qué NO" | Condiciones de `knowledge/estrategias/pmax-cuando-y-como.md` |
| Pista paralela — LSA | cuando el cliente acepte | aparte | — | Electricista califica en US | Acceso al GBP + licencia + seguro + background check |

**CPL en aprendizaje:** durante las semanas 1–3 de F1 se tolera hasta $80. Se evalúa sobre 30 días, no por día.

## Por qué NO (todavía)
- **PMax**: no cumple ninguna condición. No hay 30+ conv./mes (proyección 12–20), el tracking no está verificado, no hay feed ni assets de video, y con $27/día canibalizaría Search y Maps sin control de search terms.
- **Amplia**: requiere un tCPA maduro y tracking confiable (estándar 2). La campaña actual en broad demostró el costo: 75% del gasto visible sin intención.
- **Display / Demand Gen / Video**: servicio local, sin audiencias ni presupuesto; son clics baratos de baja intención.
- **Campaña de marca**: "prophase electric" tiene ~80 búsquedas/mes y el orgánico está en posición 3. No se sabe si hay competidores pujando por la marca. Una campaña de marca se llevaría ~10% del presupuesto en llamadas que llegarían igual. Se abre con $2–3/día si Auction Insights o el SERP muestran competidores en la marca.
- **Campañas separadas por servicio**: $27/día no alcanza ni para una campaña según la regla de 3× CPL. Dividir retrasaría el aprendizaje sin ganar control, porque el control ya lo dan los ad groups y las negativas de enrutamiento.
- **Ad group de emergencias**: el cliente no es 24/7.
- **Ad groups y landings por ciudad**: con ~80 clics/mes fragmentarían los datos sin sumar alcance. Se reevalúan en F3 con más presupuesto o si los search terms muestran diferencias por ciudad.

## Riesgos y supuestos
- **Presupuesto limitado por diseño.** Hay ~2,000+ búsquedas comerciales/mes en NWA y $825 compran ~80 clics. La IS perdida por presupuesto va a quedar alta (hoy 47%). Es normal y no debe llevar a abrir broad.
- **CPC alto**: $14–46 en la parte superior para "electrician + ciudad". Si el CPC real pasa de $15, se reevalúa el CPL objetivo.
- **La conversión es una llamada ≥60 s, no un trabajo.** Sin CRM no se mide el costo por cliente. Pedir al cliente que marque las llamadas que terminaron en trabajo (a mano, mensual) para validar el CPL.
- **Sin ticket ni margen no hay CPL máximo.** Si un cambio de panel deja $500+ de margen, $60 por llamada es sano. Si el trabajo típico es un outlet de $150, no. **Pedir ticket y margen antes de F2.**
- **Sin acceso al GBP** no hay activo de ubicación ni presencia en Maps vía Ads, contra Mister Sparky con ~2,480 reseñas.
- **Velocidad móvil sin medir**: si el score es menor a 40, pasa a bloqueante de F1.
- **Área de servicio**: si el cliente no cubre todo Benton y Washington (por ejemplo Siloam Springs o Gentry), cambiar a radio.
