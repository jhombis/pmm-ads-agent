---
cliente: Pro Phase Electric
slug: pro-phase-electric
pais: US
actualizado: 2026-09-23
version: 4
base: knowledge/playbook-analitica.md (método) + estándares PMM de CLAUDE.md
supuestos:
  - Ticket promedio, margen y tasa de cierre desconocidos → sin CPL máximo; se usan escenarios y un CPL objetivo provisional
  - Volúmenes = Semrush nacional × 0.18% (población de NWA), salvo las keywords con ciudad, que ya son locales. Keyword Planner disponible vía API desde el 23-sep, todavía no consultado
  - Área de servicio = condados de Benton y Washington + Huntsville (Madison). Falta confirmar Siloam Springs, Gentry y el oeste de Benton
  - Landings de paneles y EV no existen; sus ad groups quedan pausados hasta F2
  - Velocidad móvil y vista móvil del sitio sin verificar (audit-site.md)
  - PMM no tiene acceso al GBP → sin activo de ubicación en F1
  - No instala generadores (se niegan hasta confirmar)
  - El cliente atiende de 7:00 a 18:00 Central los 7 días y tiene alguien que contesta en ese horario
---

# Estrategia Google Ads — Pro Phase Electric

> **Ejecutada el 23-sep** (campaña 24273708366, ver `log/2026-09-23-build.md`) con dos desvíos decididos por Jhombis: los 4 ad groups activos desde el día 1 y **todas las URLs finales a la home** hasta que existan las landings; la medición de la Fase 0 se cierra en paralelo.
>
> **v4 (23-sep).** Estrategia regenerada con el playbook de analítica como base. Cambios contra v3: proyección de leads por escenarios (la v1–v3 usaba una tasa de conversión de 17–25% tomada de cuentas que cuentan llamadas del anuncio), CPL objetivo y condiciones de paso recalculadas, Reparación con landing propia, medición del playbook en F0, y la decisión de separar ciudades sujeta a volumen mínimo.

## Datos (antes de la estrategia)
Cuenta 758-301-1023. La campaña actual está activa desde el 01-sep y gasta desde el 11-sep. Datos al 22-sep.

| | Valor |
|---|---|
| Gasto acumulado | **$469.62** · 38 clics · **1 conversión** ("Calls from Ads") |
| CPC | $18.00 en la primera semana (11–15 sep) → **$9.80 en los últimos 7 días** (16–22 sep: $196.07 / 20 clics) |
| Estado | *Limited — budget constrained*; IS 22%, perdida por presupuesto 46.5%, por ranking 31.4% |
| Puja / match | Max. clics **sin tope**, keywords en broad, 1 RSA, todo a la home |
| Desperdicio (sobre $290.74 rastreables de $442.75 al 21-sep) | Cooperativas $68.58 · competencia $68.90 · DIY/producto $81.12 · genéricas ("electrical", "electrical companies" a $23/clic) $72.14. **Ningún término rastreable era de alta intención local**; 75% no tenía intención comercial alguna |

Lectura (playbook §3): mucha IS perdida por presupuesto con gasto bajo = el presupuesto se agota en tráfico equivocado. **Faltan filtros, no dinero.** Con 1 conversión no hay nada que optimizar todavía: el orden es medición → negativas → estructura → puja → creatividad.

## Matemática de presupuesto (playbook §4)
- **Inversión real: $825/mes** de un contrato de $1,500 (55%). Diario $27 → tope mensual $27 × 30.4 = **$821**.
- **Clics/día = $27 ÷ $9.80 ≈ 2.8 → ~84 clics/mes.** Este número manda sobre cualquier ambición de estructura.
- **Prospectos/mes = clics × tasa de conversión** (llamadas ≥60 s + llamadas del sitio + formularios):

| Escenario | Tasa de conv. | Prospectos/mes | CPL | Referencia |
|---|---|---|---|---|
| Conservador | 5% | ~4 | ~$195 | Piso de lo "sano" en servicios locales (playbook §3) |
| **Base** | **10–15%** | **~8–13** | **~$65–100** | Medio del rango sano, con llamadas del anuncio contadas |
| Optimista | 25% | ~21 | ~$39 | Cuentas A/B del MCC (mercados chicos, CPC $3.60–5.20) |

- **CPL objetivo provisional: ≤ $85** (medio del escenario base). **Aspiracional: $40–60.** El CPL **máximo** sale de ticket × margen × tasa de cierre × 0.3 cuando el cliente los dé. Si un panel deja $500+ de margen, $85 es sano; si el trabajo típico es un outlet de $150, no.
- **Límite de fragmentación ($600–1,500/mes): 1 campaña, 3–5 grupos** contando los de fases futuras → 4 grupos.

## Resumen ejecutivo
- **1 campaña Search**, "Search NWA", con **4 ad groups**: 2 activos en F1 (**Electrician - NWA**, con near me y todas las ciudades, y **Electrical Repair**) y 2 en F2 cuando existan sus landings (**Panel Upgrade** y **EV Charger**). Reemplaza a la actual.
- **Presupuesto $825/mes ≈ $27/día** en esa campaña. **~84 clics/mes → ~8–13 prospectos en el escenario base.**
- **Puja: Max. clics con tope de CPC $12** (1 conversión de historial; playbook §5). Pasa a **Max. conversiones** con 15+ conv/mes estables y medición limpia. En el escenario base eso **no ocurre con $825**: el paso real depende de subir la pauta.
- **1 RSA por ad group**, frase + exacta, cero broad. Presencia en los condados de Benton y Washington + Huntsville, L–D 7:00–18:00 Central.
- **tCPA**: solo con ~30 conv/30d, desde el CPA histórico. Con $825 no se alcanza; con $1,500–1,800 solo si el CPL baja a ≤$55. Sin marca, PMax, Display ni RLSA. LSA en espera.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | Puja | Geo | Horario |
|---|---|---|---|---|---|
| Pro Phase Electric - Search NWA - $1500/mo. - [fecha de lanzamiento] | Llamadas + formularios | $27 (100%) | Max. clics, tope CPC $12 → Max. conversiones con 15+ conv/mes | **Presencia**: condados de Benton y Washington (AR) + Huntsville (AR). Resto excluido | L–D 7:00–18:00 **hora Central** = **5:00–16:00 en la zona de la cuenta** (America/Los_Angeles) |
| *(actual)* Pro Phase Electric - ENHPRM Radius - $1500/mo. - 09/01/2026 | — | $27 → **se pausa** el día que sale la nueva | Max. clics (en F0: tope de CPC $12) | — | — |

Configuración fija: solo red de Búsqueda (socios y Display apagados: mezclan tráfico y contaminan la lectura), aplicación automática de recomendaciones apagada, rotación optimizar, idioma EN, sin segmentos de audiencia como exclusión.

**Por qué campaña nueva y no reestructurar la actual:** 3 semanas de historia, 1 conversión y 736 negativas heredadas de otra cuenta (Grand Junction). No hay aprendizaje que conservar. Las conversiones y el historial de la cuenta se mantienen igual.

## Estructura (playbook §8)
### Campaña: Search NWA
| Ad group | Fase | Keywords (match) | Vol. est. NWA/mes | Landing | H1 pinneado del RSA (alternativos) |
|---|---|---|---|---|---|
| **Electrician - NWA** (núcleo: servicio + near me + ciudades) | F1 | [electrician near me], [electricians near me], [electrician], [electricians], [local electrician], [electrician fayetteville], [electrician rogers], [electrician springdale], [electrician bentonville] + frase: "licensed electrician", "residential electrician", "electrician northwest arkansas", "fayetteville electrician", "electricians rogers", "electrician bella vista", "electrician centerton"… (44) | ~1,500 sin contar [electrician] | `/` | **{KeyWord:Licensed NWA Electrician}** (Licensed Electrician Near You · Northwest Arkansas Electrician) |
| **Electrical Repair** (reparación, no urgencias: el cliente no es 24/7) | F1 | [electrical repair near me], [circuit breaker repair], [outlet repair] + frase: "circuit breaker replacement", "wiring repair", "lighting repair near me"… (13) | ~112 | **`/residential-electrical-service/`** en F1 (existe; verificar que el H1 y el texto hablen de reparaciones) → `/electrical-repair/` cuando exista | **Electrical Repair in NWA** (Breaker & Outlet Repair · Electrical Repairs Done Right) |
| **Electrical Panel Upgrade** (ticket alto) | **F2** (pausado) | [electrical panel upgrade], [electrical panel replacement], [breaker box replacement], [panel upgrade near me] + frase: "fuse box replacement", "200 amp panel upgrade", "electrical service upgrade"… (15) | ~48 | `/electrical-panel-upgrade/` **(crear)** | **Electrical Panel Upgrades** (Panel Replacement in NWA · 200 Amp Panel Upgrades) |
| **EV Charger Installation** (servicio emergente; el cliente lo presta) | **F2** (pausado) | [ev charger installation], [ev charger installation near me], [electric car charger installation] + frase: "level 2 charger installation", "nema 14-50 outlet installation", "home ev charger installation"… (11; sin keywords Tesla) | ~139 | `/ev-charger-installation/` **(crear)** | **EV Charger Installation** (Home EV Charger Installers · Level 2 EV Charger Installs) |

**Por qué así:**
- **Pocos grupos a propósito.** Con ~84 clics/mes, un grupo por ciudad (v1) dejaba ~13 clics por grupo; ningún dato llegaba a ser legible. Las ciudades comparten la intención "necesito un electricista" y van en el núcleo. La relevancia del titular se mantiene con inserción de keyword (`{KeyWord:Licensed NWA Electrician}` → "Electrician Rogers"), por eso las keywords de ciudad van **sin "ar"**. Si la keyword pasa de 30 caracteres, se muestra el texto por defecto.
- **Reparación aparte** porque la intención (un problema concreto) y el anuncio son distintos, y **con su propia página** (playbook §8: cada grupo a su página de servicio, nunca todo a la home).
- **Paneles y EV aparte** por ticket, landing y copy propios. No se sirven hasta tener landing (estándar 11).
- **Separar ciudades** se decide en F3, solo si una ciudad acumula **≥50 clics** en el grupo NWA con diferencias claras, o si sube el presupuesto. Antes de eso, cualquier diferencia entre ciudades es ruido (playbook §9).

**Enrutamiento (negativas de frase por ad group):**
- NWA: panel, breaker box, ev charger, car charger, tesla, repair.
- Repair: panel, breaker box, ev, charger, tesla.
- Panel: ev, charger, tesla, solar.

**Sin ad group de Emergencia/24-7:** el cliente no atiende 24/7. "emergency", "24 hour", "24/7" y "after hours" son negativas.

Detalle: `data/keywords.csv` (83 activas + descartadas).

## Keywords descartadas y por qué
| Keyword | Vol. US | CPC | Decisión | Por qué |
|---|---|---|---|---|
| electrical services / home electrical / electrical contractors | 33,100 / 1,000 / 9,900 | $11–13 | Fuera | Genéricas. En el MCC: $1,637 → 5 conv. (cuenta D); en Pro Phase: $394 → 1 conv. |
| tesla charger / tesla wall connector installation | 4,400 / 5,400 | $7–9 | Fuera + negativas combinadas | Atraen compra de producto: en Ideal Electric el EV gastó ~$430 con 1 conv. por "tesla home charger" (playbook §6.2) |
| electrical troubleshooting | 2,900 | $5.47 | Fuera | DIY/informativa (playbook §6.3) |
| emergency / 24 hour electrician | 27,100 / 12,100 | $20–21 | Negativa | No es 24/7 |
| same day electrician | 1,000 | $30 | Fuera | No hay promesa de mismo día confirmada; CPC $30 |
| generator installation | 60,500 | $14 | Negativa | No está en la lista de servicios (confirmar) |
| ceiling fan / recessed lighting / light fixture installation | 49,500 / 27,100 / 4,400 | $5–6 | No se puja (**no se niega**) | Ticket bajo; D gastó $152 con 0 conv. Si entran por el grupo NWA, son leads válidos |
| gfci outlet installation, breaker keeps tripping | 40,500 / 4,400 | $2–4 | Fuera | Informacionales / DIY |
| smoke detector, doorbell, thermostat, data line | — | — | No se puja (no se niega) | Ticket bajo |
| prophase electric (marca) | 40 + 40 | — | Sin campaña de marca | Orgánico en posición 3; no hay evidencia de competidores pujando por la marca |
| Competidores y empresas de energía | — | — | Negativa | Estándar 5 y playbook §6.1/6.4; $137 perdidos en 11 días |

## Negativas
Aplicadas a nivel campaña (listas compartidas cuando se construya con la API):
- **Universal PMM** + **nicho** + **las 6 categorías del playbook** (§6): cooperativas y utilities (Carroll, Ozarks, SWEPCO, Entergy, "power outage", "pay my bill"…), marcas de producto ("tesla home charger", generac, leviton, lutron…), DIY ("wire size", "diagram", "how to replace", "not working"…), competencia (22 marcas locales en frase), precio de referencia ("hourly rate", "how much does"…) y fuera de servicio (24h, generadores, handyman).
- **No se niegan** `zinsco`, `siemens` ni `eaton` ("zinsco panel replacement" es un lead de paneles), ni `free` (el sitio ofrece Free Quote), ni los servicios de ticket bajo que el cliente sí presta.
- Archivos: `data/negatives-nicho.txt` (campaña nueva) y `data/2026-09-22-negatives-editor.csv` (134, pendiente de importar en la actual). Validados contra todas las keywords: 0 choques.

## Copy
Completo en **`data/ads-search-nwa.md`** (largos validados por script). **1 RSA por ad group** con H1 pinneado a la keyword del grupo y 14 headlines sin pin; los H1 alternativos quedan guardados para un 2.º RSA solo si sube el volumen (con ~3 clics/día un A/B es ruido).
- **Confianza**: Licensed, Bonded & Insured · 4.9-Star Rated on Google · Nextdoor Neighborhood Fave
- **Diferenciales**: Open 7 Days a Week · Weekend Service Available · Open 7 Days, 7 AM–6 PM · Fair, Honest Pricing · We Show Up When We Say
- **Oferta**: Get a Free Quote Today
- **Local**: Local NWA Electricians · Serving All of NW Arkansas · Rogers, Fayetteville & More

4 descripciones: una del grupo y 3 compartidas (confianza + quote, horario 7 días, precio justo + puntualidad).

Extensiones: llamada (7–18 Central = 5–16 en la cuenta), 5 sitelinks (Free Quote, Reviews, Services, Safety Inspections, Residential; Panel y EV en F2; se quita /portfolio/), 8 callouts, snippet "Service catalog", imágenes propias del portfolio, ubicación cuando haya acceso al GBP.
**No se usa**: "same day", "24/7", "emergency", número de reseñas ni la marca Tesla.

## Medición (playbook §7) — va antes de cualquier ajuste de puja
- **Un solo teléfono** en todo el sitio, y que sea el número de reenvío de la acción de conversión. Hoy aparece (479) 287-3650 en la barra superior, el header y el hero: cambiarlos todos al de reenvío.
- **Formulario de prueba**: mensaje de gracias, llegada del correo (hoy a un Gmail) y conversión registrada en 24–48 h.
- **Acciones de conversión**: primarias solo formulario + llamadas ≥60 s (anuncio y sitio). Nada de vistas ni clics como primarias.
- **Recurso de llamada**: aprobado, no en revisión; filtro de duración en 60 s (no más alto).
- **Horario de anuncios = horario de atención**: 7:00–18:00 Central, 7 días (orden de pedido). La cuenta está en hora del Pacífico: se programa 5:00–16:00 (verificado en ambas campañas el 23-sep).
- **Popups y "After Submit"** si el sitio usa Elementor.
- **Fecha de cada arreglo** registrada en el log, para comparar antes y después.

## Landings requeridas
| URL | Existe | Para | Bloqueante |
|---|---|---|---|
| Página de gracias del formulario (`/thank-you/`) o evento de envío | ? | Medir el formulario | **Sí, para lanzar F1** (estándar 7) |
| `/` (H1 → "Licensed Electrician in Northwest Arkansas…") | Sí (H1 genérico) | Grupo NWA | No. Mejora QS y experiencia de landing (hoy *below average*) |
| `/residential-electrical-service/` | Sí | Grupo Repair en F1 | Verificar que hable de reparaciones antes de lanzar |
| `/electrical-repair/` | No | Grupo Repair | **Recomendada para F1–F2** (playbook §8) |
| `/electrical-panel-upgrade/` | **No** | Grupo Panel | **Sí, para activar Panel (F2)** |
| `/ev-charger-installation/` | **No** | Grupo EV | **Sí, para activar EV (F2)** |
| Landings por ciudad | No | — | No (F3, solo si se separan ciudades) |

## Presupuesto y fases
| Fase | Fechas est. | Total/mes | Qué pasa | Condición para pasar |
|---|---|---|---|---|
| **F0 — Medición + contención** | 23-sep → ~30-sep | $825 (campaña actual) | Campaña actual: importar las 134 negativas, pausar "home electrical", "electrical services", "electrical contractors" y "home electrical services", techo de CPC $12, programación 7–18 Central (5–16 en la cuenta). Medición del playbook §7 (arriba). Pedir acceso al GBP | Formulario + llamadas del sitio **probados con Tag Assistant** (≥1 conversión de prueba en cada acción), un solo teléfono en el sitio, recurso de llamada aprobado |
| **F1 — Lanzamiento Search NWA** | ~1-oct → ~8-oct | $825 | NWA + Repair, 1 RSA c/u, Max. clics con tope $12. Se pausa la actual. Search terms en D3 y D7 | 7 días activa, anuncios aprobados, ≥1 conversión **del sitio** |
| **F2 — Limpieza + Paneles/EV** | D7 8-oct · D14 15-oct · D30 31-oct | $825 | Revisiones; activar Panel y EV cuando sus landings pasen /audit-landing | 30 días desde F1, **≥8 conversiones y CPL ≤ $100** con tendencia a la baja |
| **F3 — Decisión de presupuesto** | ~1–15-nov | Propuesta: $1,500–1,800 | Presentar la matemática al cliente: con $825 el techo es ~8–13 prospectos/mes. Pausar lo que gaste >2× CPL objetivo sin conversión; evaluar separar ciudades (≥50 clics por ciudad) | Aprobación del aumento, o seguir en $825 con Max. clics con tope y revisión mensual |
| **Cambio de puja** | cuando se cumpla | — | Max. clics → **Max. conversiones** | **15+ conv/30 días estables** con medición limpia. A CPL ~$85 hacen falta ~$1,275/mes de pauta: con $825 solo en el escenario optimista; con el aumento a $1,500–1,800, alcanzable |
| **tCPA** | Sin fecha en el escenario base. ~5-ene-2027 solo si se aprueba el aumento hacia el 15-nov **y** el CPL baja a ≤$55 | — | tCPA = CPA histórico observado +10–20% | ~30 conv/30 días. A CPL $85 eso pide ~$2,550/mes de pauta; a $55, ~$1,650 |
| F4 — RLSA | sin fecha | — | Observación | Lista ≥1,000 usuarios (con ~84 clics/mes no llega) |
| F5 — PMax | no planificada | — | Ver "Por qué NO" | Condiciones de `knowledge/estrategias/pmax-cuando-y-como.md` |
| Pista LSA | cuando el cliente acepte | aparte | Electricista califica en US | Acceso al GBP + licencia + seguro + background check |

**Evaluación:** sobre 30 días, nunca por día ni por semana. En las semanas 1–3 un CPL de hasta $150 es ruido de arranque, no una señal.

## Qué NO se va a poder concluir (playbook §9)
- Con ~84 clics/mes, **ninguna comparación entre anuncios, ciudades o keywords** es significativa en el primer trimestre. Por eso hay 1 RSA por grupo y las ciudades no se separan.
- Una tasa de conversión sobre menos de 50 clics es azar. El primer mes con muchas o pocas conversiones no es una base: se compara contra la mediana de 3 meses.
- Las audiencias en observación no darán señal a este volumen.

## Por qué NO (todavía)
- **PMax**: no cumple ninguna condición (30+ conv/mes, tCPA estable, ~$150/día, video, anti-spam moderno).
- **Amplia / AI Max**: requiere ~50 conversiones limpias acumuladas y tCPA maduro. La campaña actual en broad mostró el costo.
- **Max. conversiones desde el día 1**: con 1 conversión de historial puja a ciegas (playbook §5; caso Noah's Tow Truck: sobregasto y 0 conversiones).
- **Display / Demand Gen / Video**: servicio local, sin audiencias ni presupuesto.
- **Campaña de marca**: ~80 búsquedas/mes y orgánico en posición 3. Se abre con $2–3/día solo si hay competidores pujando por la marca.
- **Campañas separadas por servicio o grupos por ciudad**: superan el límite de fragmentación para $825/mes.
- **Ad group de emergencias**: el cliente no es 24/7.

## Riesgos y lo que no se puede saber
- **El techo con $825 es bajo**: ~8–13 prospectos/mes en el escenario base. Hay que decírselo al cliente en F1, no esperar a que lo descubra.
- **CPC**: $9.80 en la última semana con Max. clics sin tope y broad. Con tope de $12 y keywords de ciudad (parte superior $14–46 según Semrush) puede subir o perder impresiones; se revisa en D7.
- **La conversión es una llamada ≥60 s o un formulario, no un trabajo.** Sin CRM, hoja mensual del cliente con las llamadas que se volvieron trabajo.
- **No se puede saber desde los datos**: ticket y margen, qué servicios presta realmente (generadores), la cobertura real (Siloam Springs, Gentry), el historial de cambios de la cuenta y si alguien contesta todas las llamadas de 7 a 18.
- **Sin acceso al GBP**: sin activo de ubicación ni Maps vía Ads, contra Mister Sparky con ~2,480 reseñas.
- **Velocidad móvil sin medir**: si el score es <40, pasa a bloqueante de F1.
