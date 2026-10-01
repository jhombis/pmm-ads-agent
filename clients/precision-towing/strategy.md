---
cliente: Precision Towing
slug: precision-towing
actualizado: 2026-09-29
version: 1
supuestos:
  - "Ticket promedio y margen PENDIENTE: CPL objetivo tomado del benchmark ($21–31), no del margen real"
  - "$1500 del nombre de cuenta = fee total; $825 = pauta neta (no confirmado)"
  - "Cobertura nocturna (22:00–07:00) no confirmada: sin '24 hour' y programación 6:30–22:30"
  - "Flatbed, equipo de winch/4x4 y camión medium duty para 5th wheel: no confirmados, claims marcados en ads-search.md"
  - "Nombre histórico Miller's Kern Valley Towing no confirmado por el cliente"
  - "Velocidad de landing estimada, no medida (PageSpeed sin clave)"
  - "Sin Google Ads API en la sesión: geo/programación/extensiones de la cuenta actual no verificados en UI"
---

# Estrategia Google Ads — Precision Towing

## Resumen ejecutivo
Reestructurar la cuenta 753-255-2245 en **2 campañas Search** (Towing Kern River Valley con 4 ad groups + Marca) con **$825/mes** ($27/día), todo en **frase y exacta**, Maximizar conversiones sin tCPA, geo por presencia en el radio real (21 mi + dos puntos de 8 mi) y programación 6:30–22:30. Se elimina la amplia, se separa la marca, se protege el grupo de trailers con negativas de compra y se aplican 269 negativas de nicho más la universal desde el día 1. **CPL objetivo $26 (rango $21–31), alarma $47**; con ese CPL el presupuesto rinde ~32 llamadas/mes y **tCPA (~$30) entra alrededor del día 30–45**. Nada se lanza hasta cerrar los bloqueantes de Fase 0: acceso a web y GTM, conversión de formulario y verificación con Tag Assistant. PMax sigue pausada hasta el mes 6 como mínimo.

Por qué esta estructura y no más campañas: la regla de aprendizaje pide ≥3× CPL/día por campaña ($78/día con CPL $26) y solo hay $27/día. Una campaña con ad groups temáticos concentra la señal; el cuartil superior del MCC (CPL $8–13) usa exactamente eso: 1 campaña Search radio, 1–2 ad groups, 6–16 keywords, Max. conversiones.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| Search - Towing KRV | Llamadas (Calls from Ads + Website Calls); formulario secundario | $24 | 89% | Max. conversiones sin tCPA → tCPA $30 al llegar a 30 conv/30d | Presencia: radio 21 mi 5212 Lake Isabella Blvd + 8 mi (35.674769,-118.033108) + 8 mi (35.739446,-118.936733). Excluir resto de US y todos los países | Lun–Dom 6:30–22:30 |
| Search - Marca | Llamadas | $3 | 11% | Max. conversiones | Misma geo, **sin** expansión: "precision towing" tiene 2.400 búsquedas nacionales de homónimos | Lun–Dom 6:30–22:30 |
| P. Max (existente) | — | $0 | 0% | Pausada | — | — |

Ajustes comunes (estándar 8 y playbook §6): solo red de Búsqueda, sin socios de búsqueda ni Display; recomendaciones automáticas apagadas; sin exclusiones de audiencia; rotación optimizar; idioma inglés; dispositivos todos; activo de llamada con reporte y conversión ≥30 s; activo de ubicación vinculado a GBP (pendiente acceso). Conversiones primarias: "Calls from Ads", "Website Calls" y la nueva de formulario (cuando exista); "Clicks to call" y acciones locales quedan secundarias. **Transición**: la campaña "ENHPRM Radius" sigue activa hasta el día en que se activa la nueva estructura; ese día se pausa. Sin solapamiento de más de 24 h para no competir contra uno mismo.

## Estructura por campaña

### Campaña: Search - Towing KRV
Detalle de las 77 keywords en `data/keywords.csv`; copy completo en `data/ads-search.md`. Una campaña, cuatro temas. Servicio × ciudad no se separa porque ninguna combinación ciudad+towing llega a 100 búsquedas/mes (Semrush 0–20; en cuenta, "kernville towing" 81 impresiones en 6 semanas): las comunidades van en un solo grupo geográfico y en el copy.

| Ad group | Keywords (match) | Vol. est. | Landing | H1 pinneado |
|---|---|---|---|---|
| **AG1 Tow Truck Near Me** (estrella, ~55% del gasto esperado) | [towing near me], [tow truck near me], [towing company near me], [tow truck company near me] en exacta; "towing near me", "tow truck near me", "towing company near me", "tow company near me", "towing service near me", "tow service near me", "tow trucks near me", "tow truck service", "towing services", "car towing near me", "car towing service", "emergency towing", "emergency towing near me", "emergency tow truck near me", "flatbed towing near me", "light duty towing", "medium duty towing", "wrecker service", "tow truck" en frase (23) | Nacional alto; local: ~600–900 impr/mes disponibles (IS actual 50%) | `/light-medium-duty-towing/` reescrita como "Tow Truck Lake Isabella & Kern River Valley" | "Tow Truck Near Lake Isabella" |
| **AG2 Towing Lake Isabella & KRV** (~15%) | [kernville towing], [towing lake isabella], [lake isabella towing] exacta; "kernville towing", "towing kernville", "tow truck kernville", "towing lake isabella", "lake isabella towing", "tow truck lake isabella", "towing lake isabella ca", "kern river valley towing", "kern valley towing", "towing wofford heights", "towing bodfish", "towing weldon", "towing mountain mesa", "tow truck wofford heights" frase (17) | Bajo (Semrush 0–20) pero es el mejor CPL de la cuenta: kernville 6 conv a $14 | `/light-medium-duty-towing/` (misma) | "Towing in Lake Isabella, CA" |
| **AG3 Roadside Assistance** (~20%) | "roadside assistance near me", "roadside service near me", "roadside service", "emergency roadside assistance", "roadside assistance", "flat tire service near me", "flat tire roadside assistance", "roadside tire service", "flat tire change service", "jump start near me", "jump start service", "car jump start service", "car lockout service", "vehicle lockout service", "locked keys in car", "winch out service", "winch out near me", "car stuck in sand", "off road recovery near me", "off road recovery" frase (20) | Alto nacional; RRN es el único que paga a escala | `/roadside-assistance/` con H2 por subservicio | "Roadside Assistance Near You" |
| **AG4 RV & Trailer Towing** (~10%) | "5th wheel towing service", "5th wheel towing near me", "5th wheel towing service near me", "fifth wheel towing service", "5th wheel transport", "tow truck 5th wheel", "rv towing near me", "rv towing service", "rv towing service near me" → `/5th-wheel-towing/`; [travel trailer towing service] exacta + "travel trailer towing service", "travel trailer moving service", "travel trailer transport service", "camper towing service", "camper towing near me", "trailer towing service", "trailer towing near me" → `/travel-trailer-towing/` (URL final a nivel de keyword) (17) | 50–1.000/mes nacional; hoy 0 conv por búsquedas de compra | `/5th-wheel-towing/` y `/travel-trailer-towing/` con frase "we tow, we don't sell hitches" | "5th Wheel Towing Service" |

Negativas específicas del grupo (además de la lista de cuenta):
- AG1/AG2: `roadside`, `flat tire`, `jump start`, `lockout`, `5th wheel`, `fifth wheel`, `travel trailer`, `camper`, `rv` (para que esas búsquedas caigan en su grupo y no en el genérico).
- AG3: `tow truck`, `towing` como frase NO (muchas búsquedas de roadside incluyen "tow"); sí: `5th wheel`, `trailer`, `rv`, `battery replacement`, `new battery`, `tire shop`.
- AG4: lista de compra completa (hitch, for sale, best truck, capacity, dolly, forest river, cargo, toy hauler, calculator…) ya en cuenta; a nivel de grupo añadir `roadside`, `flat tire`, `car`, `sedan`, `suv`.
- Marca: no recibe genéricos: en la campaña Marca negativar `near me`, `tow truck`, `towing service` sin "precision".

Nota sobre "tow truck" en frase: hoy es la keyword que más gasta ($402, CPL $38) y en el nicho rinde peor que "near me" ($25 vs $17). Se mantiene en frase porque en un radio rural captura variantes útiles ("tow truck company", "tow truck lake isabella"), pero es la primera candidata a pausar en la revisión del día 14 si su CPL supera $47.

### Campaña: Search - Marca
| Ad group | Keywords (match) | Vol. est. | Landing | H1 pinneado |
|---|---|---|---|---|
| **AGB Marca** | [precision towing], [precision automotive lake isabella] exacta; "precision towing lake isabella", "precision towing ca", "precision automotive towing", "precision automotive lake isabella", "precision auto lake isabella", "precision automotive paint collision towing", "miller's kern valley towing", "millers kern valley towing" frase (10) | Local: ~10–20 búsquedas/mes reales (8 clics / 2 conv en 6 semanas) | `/` (home) con H1 y agregado de reseñas añadidos | "Precision Towing Lake Isabella" |

Negativas del grupo: `palm bay`, `florida`, `ohio`, `inc` (Precision Towing Inc es otra empresa), `jobs`, `reviews` (van a GBP), más genéricos sin marca. Justificación: marca propia convierte al 37–62% con CPL $9–12 en el MCC; separarla evita que infle el CPL de los genéricos y que la amplia de un competidor se la lleve.

## Keywords descartadas y por qué
| Grupo | Ejemplos | Motivo | Destino |
|---|---|---|---|
| Marcas de competidores (14 marcas, ~80 variantes) | b&d towing, b&m, golden empire, inyo, a&a, nitro, chinos, b&b, a&m, transcend, nobles, pepe's, ibarra's, lead-gen (RRN, lakeisabellatowing.us) | Regla PMM: el clic llega, la venta no; $159 (13,5% del gasto) en 6 semanas | Negativa de cuenta |
| Heavy duty / semi / big rig | heavy duty towing near me (CPC $7,37), semi truck towing near me | Capacidad que el cliente no tiene | Negativa |
| Compra e info de trailers | 5th wheel tow hitch (1.300/mes), best truck for towing 5th wheel, tow dolly for sale, towing capacity, forest river | Producto/informacional; causaron $46 con 0 conv | Negativa |
| Aseguradoras y planes | aaa towing (27.100), aaa roadside assistance (165.000), geico, allstate, "phone number" | Navegacional; en el MCC CVR 13–18% y CPL $32–43 | Negativa |
| Fuera de área | towing bakersfield, tow truck bakersfield, tehachapi, ridgecrest | Presencia lo filtra; refuerzo por si un usuario del radio busca otra ciudad | Negativa |
| 24 hour / 24/7 | 24 hour towing near me (2.900) | Cliente atiende 7–22; clic nocturno = llamada perdida + reseña mala | Negativa hasta confirmar cobertura nocturna; si confirma, pasa a AG1 en frase |
| Precio / costo | how much does a tow cost, towing prices | Sin landing de precios | Negativa; fase 2 si se crea landing. **"cheap" NO se negativa** (CVR 34%, CPL $16,59 en 23 cuentas) |
| Chatarra / gratis | free towing, junk car, cash for cars | Chatarra | Negativa |
| Fase 2 (no negativa, no pujar aún) | long distance towing, motorcycle towing near me, motorhome towing, accident towing | Capacidad o CPC alto ($8,50) sin datos | Evaluar día 60 |
| Taller | smog check, auto repair, mechanic | Sin campaña de taller en Fase 1; el objetivo es towing | Negativa en Search (se retira si se abre campaña de taller) |

## Copy
Copy completo (15 headlines + 4 descripciones por ad group, H1 pinneada por RSA A/B/C, sitelinks, callouts, snippets) en `data/ads-search.md`. Ángulos, en orden de prioridad según competitors.md:
1. **Local dispatch, no call center**: diferencia frente a las 4 redes lead-gen que dominan los "near me".
2. **4.8★ · 850+ Google Reviews**: ningún competidor local muestra reseñas (B&D 26 en Yelp).
3. **Tow + Repair, one call / 17-bay shop**: nadie más lo tiene.
4. **33 años, AAA Approved, NAPA AutoCare, Gold Seal Smog**: sellos que solo el cliente puede reclamar.
5. **Horario real**: "Open Daily 7 AM–10 PM" + "After-Hours Emergency" en vez del "24/7" que todos prometen y pocos cumplen.

Claims condicionados a confirmación del cliente antes de publicar: after-hours (quién contesta), medium duty/flatbed (flota), winch-out/4x4 (equipo), nombre histórico Miller's. Sin teléfono en el texto (política); va en el activo de llamada.

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| `/thank-you/` (noindex, teléfono grande, "we call you back in 5 min", sin menú) + redirect en los 7 formularios Elementor | **No** | Cliente/quien edite la web (PMM redacta) | **Sí** (conversión de formulario, estándar 7) |
| `/light-medium-duty-towing/` reescrita: H1 "Tow Truck in Lake Isabella & the Kern River Valley", teléfono + ETA arriba, form 3 campos, comunidades, sellos, 4 reseñas de grúa, agregado 4,8★ | Sí (reescribir) | PMM redacta / Cliente publica | No para lanzar (la actual convierte al 37%), **sí para Fase 2** |
| `/roadside-assistance/` con H2 por subservicio y mismo bloque de conversión | Sí (ajustar) | Cliente | No |
| `/5th-wheel-towing/` y `/travel-trailer-towing/` con frase "we tow, we don't sell or install hitches" | Sí (ajustar) | Cliente | No |
| `/` con H1, agregado de reseñas y horario real | Sí (ajustar) | Cliente | No |
| Footer de las 9 páginas: horario 7 AM–10 PM | Sí (corregir) | Cliente | **Sí** (anunciar 7–10 con la web diciendo 8–8 destruye la confianza) |
| Botón de llamada sticky en móvil | Sí (ajustar) | Cliente | No, prioridad alta |
| Landings por ciudad | No crear | — | — (volumen insuficiente; revisar día 90) |

Prerrequisito de todas: acceso de edición a WordPress/Elementor y a GTM-NWQH4MVX, o el nombre de quien publica. Es el bloqueante raíz de la auditoría.

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |
|---|---|---|---|
| **0 · Setup** (semana 1–2) | $825 sigue corriendo en la campaña actual | Sin cambios | Acceso web+GTM conseguido · `/thank-you/` + conversión de formulario creadas · Tag Assistant verifica llamada y formulario · horario unificado · negativas universal + nicho aplicadas a la cuenta actual (esto sí se hace ya: recorta el 13% de desperdicio sin esperar) · nueva estructura creada en pausa con /build-campaign |
| **1 · Relanzamiento** (día 0–30) | $825 | Towing KRV $24/día · Marca $3/día | ≥30 conversiones en 30 días con tracking verificado **y** CPL ≤ $47. Revisiones de search terms día 7, 14, 30. Si al día 30 hay 20–29 conv: seguir en Max. conv. hasta el día 45; si CPL > $47 dos semanas seguidas: pausar la keyword/grupo responsable, no bajar presupuesto |
| **2 · tCPA** (día 30–60) | $825 | Igual; tCPA $30 en Towing KRV, bajando a $26 si se sostiene 2 semanas | CPL ≤ $28 durante 2 semanas · IS ≥ 60% · landing estrella reescrita y publicada |
| **3 · Reasignación** (día 60–90) | $825 (o más si el cliente confirma margen para escalar: PENDIENTE) | Según CPA real por grupo: si Roadside ≥ 8 conv/mes con CPL ≤ $31, se separa en campaña propia con $8/día; si AG4 sigue en 0 conv, se pausa y se reintenta en temporada (mayo–sept) | 30 conv/mes sostenidas 2 meses · CPL ≤ $26 · confirmación del cliente de calidad de lead (hoja compartida, sin CRM) |
| **4 · Remarketing / RLSA** (día 90+) | +10% del presupuesto | Audiencia de visitantes del sitio, Display de remarketing con exclusión de apps | Fase 3 cumplida · ≥1.000 visitantes/mes en la audiencia |
| **5 · PMax** (mes 6+) | 20–30% de Search | Un asset group por servicio, exclusión de marca, URL expansion off | Todas las condiciones de `knowledge/estrategias/pmax-cuando-y-como.md`: tCPA estable 4 semanas, 30+ conv/mes verificadas, limpieza de search terms, assets propios, landing ≥5% conv |
| **Paralelo · LSA** | Aparte del presupuesto de Search | — | Solo si el cliente confirma licencia, seguro y background check (PENDIENTE). Arrancar la verificación en Fase 0 porque tarda 2–4 semanas |

Expectativa con $825 (benchmark): CPL mediana $26 → ~32 llamadas/mes; CPL histórico $37,5 → ~22; cohorte nueva $51 → ~16. El cuello de botella es el volumen del mercado (~900 impresiones/mes disponibles con IS 50%), no el dinero: la meta es IS 70–80% en AG1/AG2 y sumar volumen con Roadside y Marca, no gastar más.

## Por qué NO (todavía)
- **PMax**: cuenta de 6 semanas, sin conversión de formulario, sin assets propios, sin limpieza de search terms. Las 2 cuentas del MCC que la lanzaron con < 3 meses fracasaron ($66–69 por conversión) y ya fue pausada aquí (estándar 9). Reevaluar mes 6.
- **Amplia**: en el MCC no rinde mejor que frase (CPL $19,43 vs $17,36, misma CVR) y el 23% del gasto Search del nicho se fue a search terms sin conversión. En esta cuenta explicó el 13,5% de desperdicio en marcas de competidores y compra de trailers. Solo con tCPA maduro y aprobación de Jhombis (estándar 2).
- **Display / Video / Demand Gen**: servicios locales de emergencia; sin pedido expreso no se abren.
- **Landings por ciudad**: 0–20 búsquedas/mes por combinación; un grupo geográfico y comunidades en el copy resuelven lo mismo sin mantener páginas vacías.
- **Campaña de Roadside separada**: no alcanza $78/día por campaña; se separa en Fase 3 si demuestra volumen.
- **"24 hour" y competir por precio**: sin cobertura nocturna confirmada y sin landing de precios. "cheap" se deja entrar por frase y se mide.
- **Campaña de taller / smog**: fuera del objetivo del cliente en Fase 1; se negativiza en Search para no diluir presupuesto.
- **LSA**: pista paralela, no sustituto; depende de licencia y background check que no están confirmados.

## Riesgos y supuestos
- **Acceso a la web**: si el cliente no da acceso ni nombra a quien edite, Fase 0 no cierra y se sigue con la campaña actual solo con negativas y frase (mejora parcial estimada: CPL de $37 a $30). Escalar a Jhombis en la semana 2.
- **Volumen rural**: pasar de amplia a frase reducirá impresiones; se compensa con más temas (Roadside, Marca, trailers) y exacta en los términos que ya convierten. Si el día 14 el gasto cae por debajo de $18/día, reactivar "tow truck" y "towing service" en frase amplia (sin comillas) antes que volver a amplia pura.
- **Golden Empire Towing** tiene sede a 5 mi (Mountain Mesa) y flota de 45 camiones; hoy sin pauta detectable. Vigilar Auction Insights en cada revisión; si aparece, priorizar marca, AG2 y prueba social donde no puede competir.
- **CPL objetivo provisional**: sale del benchmark, no del margen del cliente. Cuando entregue ticket y tasa de cierre se recalcula (margen × cierre × 0,3) y puede cambiar el veredicto de AG3 y AG4.
- **Calidad de la conversión**: el 86% de las conversiones del nicho son llamadas sin filtro de duración. Se fija ≥30 s en el activo de llamada y se pide al cliente marcar leads calificados en una hoja compartida desde el día 1 (sin CRM).
- **Claims no confirmados** (after-hours, flatbed, medium duty, winch, nombre histórico): hay sustitutos en `data/ads-search.md`; no publicar sin confirmación.
- **Presupuesto**: si $825 no es la pauta neta, recalcular los repartos; la estructura no cambia.
- **Estacionalidad**: Lake Isabella tiene pico de visitantes de mayo a septiembre (Kern River). El histórico es de agosto–septiembre; el CPL de invierno puede subir por menos volumen. No es motivo para volver a amplia.

Siguiente skill: `/roadmap`.
