---
cliente: Precision Towing
slug: precision-towing
actualizado: 2026-10-06
version: 2
cambios_v2: "Reescrita el 2026-10-06 con el playbook de analítica y los estándares vigentes: 1 campaña y 4 grupos (límite de fragmentación), 1 RSA por grupo, puja Max. clics con tope durante la reestructura, ciudades por inserción de keyword, marca como grupo, sin horas en el copy, landing alternativa en GHL/Leadpages. Datos de la cuenta al 2026-10-05."
supuestos:
  - "Ticket promedio y margen PENDIENTE: CPL objetivo tomado del benchmark consolidado ($21–38), no del margen real"
  - "$825/mes = pauta neta (el presupuesto diario configurado hoy es $32; se baja a $27)"
  - "Zona horaria de la cuenta no verificada (Windsor no la expone); la programación se fija tras leer customer.time_zone"
  - "Cobertura nocturna (22:00–07:00) no confirmada: sin '24 hour' y programación 6:30–22:30"
  - "Flatbed, winch/4x4, medium duty, cambio de llanta en carretera y nombre histórico Miller's: no confirmados; claims condicionados en ads-search.md"
  - "Origen de la conversión 'Form Fill' sin verificar"
  - "Velocidad de landing estimada, no medida"
---

# Estrategia Google Ads — Precision Towing (v2)

## Resumen ejecutivo
Una sola campaña Search, **"Search - Precision Towing KRV"**, con **4 ad groups** (Tow Truck & Towing con las ciudades dentro, Roadside Assistance, RV & Trailer Towing, Marca), **$27/día** ($825/mes), **frase y exacta** sin amplia, **Maximizar clics con tope de CPC $9** mientras la estructura nueva acumula datos, presencia en el radio real (21 mi + dos puntos de 8 mi) y programación 6:30–22:30 en hora de la cuenta. Reemplaza a la campaña actual (107 keywords en amplia, 2 grupos, $32/día, sin programación, CPC $24 en las últimas dos semanas), que se pausa el día de la activación. Se eliminan 14 keywords que chocan con las negativas (incluidas `b&d towing` y `b&m towing`), se aplican 283 negativas de nicho más la universal, se quitan las 4 negativas de marca propia y se protege el grupo de trailers con negativas de compra. **CPL objetivo $26 (rango $21–38), alarma $47.** PMax sigue pausada; no califica con este presupuesto.

**Matemática de presupuesto (playbook §4)**: tope mensual = $27 × 30,4 = **$821**. Clics/día = $27 ÷ CPC: con el CPC real de las dos últimas semanas ($24) son **1,1 clics/día**; con el tope de $9, **3 clics/día ≈ 91/mes**; con el CPC mediano del nicho ($7), 3,9. Prospectos/mes = clics × tasa de conversión: 91 × 30% = **~27 llamadas/mes** con tope, contra ~15 si se deja Max. conversiones al CPC actual. Lo que decide el resultado no es la estructura sino el CPC.

**Límite de fragmentación**: $825 está en el tramo $600–1.500 → **1 campaña, 3–5 grupos** (incluidos los de fases futuras). La v1 proponía Towing + Marca como campañas separadas; con $3/día la de marca nunca saldría de aprendizaje y la de genéricos tampoco alcanza 3× CPL/día ($78). Marca va como grupo: tiene volumen real (8 clics, 2 conv en 53 días) pero no el suficiente para una campaña.

**Límites de bajo volumen (playbook §9)**: con 60–90 clics/mes no se concluye nada de A/B de anuncios (por eso 1 RSA por grupo), ni de audiencias en observación, ni se lee una tasa de conversión por grupo con menos de 50 clics. El grupo de trailers (17 keywords, ~5 clics/mes) y el de marca se evalúan a 90 días, no a 30.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| Search - Precision Towing KRV | Llamadas (Calls from Ads + Website Calls); formulario secundario hasta verificar "Form Fill" | $27 | 100% | **Max. clics, tope CPC $9** → Max. conversiones con 15+ conv/mes estables y medición limpia → tCPA desde el CPA observado con 30 conv en 30 días | Presencia: radio 21 mi 5212 Lake Isabella Blvd + 8 mi (35.674769,-118.033108) + 8 mi (35.739446,-118.936733). Excluir resto de US y todos los países | Lun–Dom 6:30–22:30 **en `customer.time_zone`** (verificar; el cliente atiende 7–22 Pacífico) |
| ENHPRM Radius (actual) | — | se pausa el día de la activación | — | — | — | — |
| P. Max (actual) | — | pausada, $0 | — | — | — | — |

Por qué Max. clics con tope y no Max. conversiones: la cuenta tiene ~23 conv/mes (>15), pero su CPC pasó de $7 a $24 en dos semanas con Max. conversiones en una subasta de 70 impresiones semanales, y la reestructura (keywords nuevas en frase) reinicia el aprendizaje. El tope de $9 (P75 del nicho) compra 3 clics/día en vez de 1; con CVR ≥30% son más llamadas por el mismo dinero. Condición explícita para volver a Max. conversiones: 15+ conv/mes durante 4 semanas con "Form Fill" verificada y llamadas ≥30 s. tCPA solo con 30/30d, fijado desde el CPA que se observe (no desde los $26 deseados).

Ajustes comunes (estándar 8, playbook §6): solo Búsqueda, sin socios ni Display; recomendaciones automáticas apagadas; sin exclusiones de audiencia; rotación optimizar; inglés; todos los dispositivos (97% del gasto es móvil; desktop y tablet 6 clics y 0 conv en 53 días: se ajusta −50% en Fase 2 si siguen en 0); activo de llamada con reporte y conversión ≥30 s; activo de ubicación vinculado a GBP (pendiente acceso). Conversiones primarias: "Calls from Ads", "Website Calls"; "Form Fill" primaria solo cuando se verifique su disparador; "Clicks to call" y acciones locales secundarias.

## Estructura por campaña

### Campaña: Search - Precision Towing KRV
Detalle de las 87 keywords en `data/keywords.csv` (77 frase, 10 exacta); copy en `data/ads-search.md`. Las ciudades no tienen grupo propio: ninguna combinación ciudad+towing llega a 100 búsquedas/mes y el límite de fragmentación no lo permite; van como keywords dentro de AG1 y el H1 alternativo usa `{KeyWord:Towing Near Me}` para que "kernville towing" o "towing lake isabella" vean su término en el anuncio.

| Ad group | Keywords (match) | Vol. est. | Landing | H1 pinneado |
|---|---|---|---|---|
| **AG1 Tow Truck & Towing KRV** (estrella, ~65% del gasto esperado) | Exacta: [towing near me], [tow truck near me], [towing company near me], [tow truck company near me], [kernville towing], [towing lake isabella], [lake isabella towing]. Frase: towing near me, tow truck near me, towing company near me, tow company near me, towing service near me, tow service near me, tow trucks near me, tow truck service, towing services, car towing near me, car towing service, emergency towing, emergency towing near me, emergency tow truck near me, flatbed towing near me, light duty towing, medium duty towing, wrecker service, tow truck, kernville towing, towing kernville, tow truck kernville, towing lake isabella, lake isabella towing, tow truck lake isabella, towing lake isabella ca, kern river valley towing, kern valley towing, towing wofford heights, towing bodfish, towing weldon, towing mountain mesa, tow truck wofford heights (40) | ~600–900 impr/mes disponibles en el radio (IS 35–50%) | `/light-medium-duty-towing/` reescrita, o landing GHL/Leadpages "Tow Truck Lake Isabella & Kern River Valley" | "Tow Truck Near Lake Isabella" (alt. `{KeyWord:Towing Near Me}`) |
| **AG2 Roadside Assistance** (~20%) | Frase: roadside assistance near me, roadside service near me, roadside service, emergency roadside assistance, roadside assistance, flat tire service near me, flat tire roadside assistance, roadside tire service, flat tire change service, jump start near me, jump start service, car jump start service, car lockout service, vehicle lockout service, locked keys in car, winch out service, winch out near me, car stuck in sand, off road recovery near me, off road recovery (20) | Alto nacional; RRN es el único que paga a escala | `/roadside-assistance/` con H2 por subservicio, o landing propia | "Roadside Assistance Near You" |
| **AG3 RV & Trailer Towing** (~10%) | Frase: 5th wheel towing service, 5th wheel towing near me, 5th wheel towing service near me, fifth wheel towing service, 5th wheel transport, tow truck 5th wheel, rv towing near me, rv towing service, rv towing service near me → `/5th-wheel-towing/`; exacta [travel trailer towing service] + frase travel trailer towing service, travel trailer moving service, travel trailer transport service, camper towing service, camper towing near me, trailer towing service, trailer towing near me → `/travel-trailer-towing/` (17) | 50–1.000/mes nacional; hoy 0 conv en 53 d por búsquedas de compra | `/5th-wheel-towing/` y `/travel-trailer-towing/` con frase "we tow, we don't sell hitches" | "5th Wheel Towing Service" |
| **AG4 Marca** (~5%) | Exacta: [precision towing], [precision automotive lake isabella]. Frase: precision towing lake isabella, precision towing ca, precision automotive towing, precision automotive lake isabella, precision auto lake isabella, precision automotive paint collision towing, miller's kern valley towing, millers kern valley towing (10) | ~10–20 búsquedas/mes reales (8 clics, 2 conv en 53 d) | `/` (home) | "Precision Towing Lake Isabella" |

Negativas específicas por grupo (además de las de campaña):
- AG1: `roadside`, `flat tire`, `jump start`, `lockout`, `winch`, `5th wheel`, `fifth wheel`, `travel trailer`, `camper`, `rv`, `trailer towing` (para que caigan en su grupo) + sección "NIVEL AD GROUP" de `data/negatives-nicho.txt` (taller: smog, auto repair, starter, alternator, paint, collision…).
- AG2: `5th wheel`, `trailer`, `rv`, `tire shop`, `tire place` + sección taller. No negativar `tow truck` ni `towing` (muchas búsquedas de roadside los incluyen).
- AG3: `roadside`, `flat tire`, `car`, `sedan`, `suv` + lista de compra (hitch, for sale, best truck, capacity, dolly, forest river, cargo, toy hauler, calculator…) + sección taller.
- AG4 Marca: `near me`, `tow truck near me`, `towing service`, `towing near me` (sin "precision"), `palm bay`, `florida`, `ohio`, `inc`, `jobs`, `reviews`. **No** recibe la sección taller: sus keywords contienen "automotive", "paint" y "collision".
- Campaña: quitar las 4 negativas de marca propia que hoy existen (`precision`, `precision automotive`, [precision towing], [precision automotive lake isabella]) o AG4 nunca imprimirá.

Nota sobre "tow truck" en frase: es la keyword que más gasta ($402, 10,5 conv, CPL $38) y la que trajo "starter and alternator repair"; se mantiene en frase con las negativas de taller y es la primera en pausarse si en D14 supera $47 de CPL.

## Keywords descartadas y por qué
| Grupo | Ejemplos | Motivo | Destino |
|---|---|---|---|
| Marcas de competidores (15 marcas, ~85 variantes) | b&d towing, b&m, golden empire, inyo, a&a, nitro, chinos, b&b, a&m, transcend, nobles, pepe's, ibarra's, gomez, lead-gen | $143,88 (30% del rastreable) en 53 d con 2,5 conv; dos están hoy como keywords positivas | Negativa de campaña; eliminar las 2 keywords |
| Taller / mecánica | starter and alternator repair, smog check, auto service | $72,40 (15%) con 0 conv; sin campaña de taller en Fase 1 | Negativa de ad group en AG1–AG3 |
| Heavy duty / semi | heavy duty towing near me (CPC $7,37), semi truck towing near me | Capacidad que el cliente no tiene | Negativa |
| Compra e info de trailers | 5th wheel tow hitch (1.300/mes), best truck for towing 5th wheel, tow dolly for sale, forest river | Producto/informacional; $46 + $15 con 0 conv | Negativa |
| Aseguradoras y planes | aaa towing, aaa roadside assistance, geico, allstate, "phone number" | Navegacional; CVR 13–18% en el MCC | Negativa |
| Fuera de área | towing bakersfield, tehachapi, ridgecrest | Presencia lo filtra; refuerzo | Negativa |
| 24 hour / 24/7 | 24 hour towing near me, "towing 24 hours near me" (keyword activa hoy) | Sin cobertura nocturna confirmada; $16,45 sin conv | Negativa y eliminar 2 keywords; si el cliente confirma, pasan a AG1 en frase |
| Precio de referencia | how much does a tow cost, towing prices, hourly rate | Sin landing de precios (playbook §6.5). **"cheap" no se negativa**: CVR 34%, CPL $16,59 en 23 cuentas | Negativa |
| Chatarra / gratis | free towing, junk car, cash for cars | Chatarra | Negativa |
| Boat, motorhome, motorcycle, long distance, accident | 7 keywords de boat activas hoy con 0 conv | Capacidad o CPC alto sin datos | Negativa (boat) / fase 2; eliminar las 7 keywords de boat y motorhome |

## Copy
Copy completo (1 RSA por grupo con 15 headlines + 4 descripciones, H1 pinneada, H1 alternativa documentada, sitelinks, callouts, snippets) en `data/ads-search.md`. Sin teléfono ni horas en el texto: "Open 7 Days A Week" en vez de "7 AM–10 PM" hasta confirmar la zona horaria de la cuenta (caso Pro Phase del playbook). Ángulos: local dispatch sin call center; 4.8★ · 850+ reseñas; grúa + taller de 17 bahías en una llamada; 33 años, AAA Approved, NAPA AutoCare, Gold Seal Smog; "After-Hours Emergency" condicionado. Claims que esperan confirmación del cliente: after-hours, flatbed, medium duty, winch/4x4, nombre Miller's.

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| Vía A (acceso a WordPress antes del 2026-10-10): `/thank-you/` + redirect en 7 formularios; footer 7–22; `/light-medium-duty-towing/` reescrita; sticky móvil; sellos | No / reescribir | Cliente edita, PMM redacta | Sí (conversión de formulario, estándar 7) |
| Vía B (sin acceso): 3 landings propias en GoHighLevel (`/landing-ghl`: towing, roadside, trailer) o Leadpages + 1 página de gracias, con formulario de 3 campos, conversión propia y dominio `go.precisiontowingca.com` (CNAME del cliente) o subdominio de la plataforma | No | PMM | Sí hasta publicarlas y pasar Tag Assistant |
| `/` (home) para AG4 Marca: H1, agregado de reseñas, horario real | Sí (ajustar) | Cliente | No |
| `/roadside-assistance/`, `/5th-wheel-towing/`, `/travel-trailer-towing/` ajustes ligeros (solo vía A) | Sí (ajustar) | Cliente | No |
| Landings por ciudad | No crear | — | — |

Decisión el 2026-10-10: si no hay acceso, se ejecuta la vía B y `data/keywords.csv` se actualiza con las URLs finales nuevas antes de `/build-campaign`.

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |
|---|---|---|---|
| **0 · Setup** (2026-10-06 → 2026-10-17) | $825 sigue en la campaña actual, bajada a $27/día | Esta semana sin esperar al cliente: presupuesto $32 → $27; negativas + eliminación de 14 keywords; amplias a frase; programación 6:30–22:30 tras leer la zona horaria; "Calls from Ads" ≥30 s; verificar "Form Fill"; crear la estructura nueva en pausa | Medición verificada (llamada + formulario, Tag Assistant) · landing vía A o B publicada · negativas aplicadas · proceso de respuesta a leads definido · estructura creada en pausa |
| **1 · Relanzamiento** (día 0–30) | $825 | $27/día, Max. clics tope $9 | ≥15 conv/mes limpias y CPL ≤ $47 → pasar a Max. conversiones. Revisiones D7, D14, D30. Si el gasto cae bajo $18/día en D7, subir el tope a $11 antes que abrir amplia |
| **2 · Max. conversiones** (día 30–60) | $825 | Igual; Max. conv. sin tCPA | 30 conv en 30 días con tracking verificado → tCPA = CPA observado |
| **3 · tCPA y reasignación** (día 60–90) | $825 (o más si el cliente confirma margen: PENDIENTE) | tCPA desde el CPA real, −10% cada 2 semanas hasta $26 si se sostiene; desktop −50% si sigue en 0; AG3 se pausa hasta abril si sigue en 0 | 30 conv/mes sostenidas 2 meses · CPL ≤ $26 · hoja de calidad de leads del cliente |
| **4 · Remarketing** (día 90+) | +10% | Display de remarketing si la lista ≥100 y hay fotos; RLSA no alcanzará 1.000 | Fase 3 cumplida |
| **5 · PMax** (mes 6+) | 20–30% de Search | Solo si la pauta sube a ≥ $2.000/mes | Todas las de `pmax-cuando-y-como.md` |
| **Paralelo · LSA** | aparte | — | Licencia, seguro y background check confirmados (PENDIENTE) |

## Por qué NO (todavía)
- **Dos campañas (Towing + Marca)**: el límite de fragmentación para $825/mes es una campaña con 3–5 grupos; $3/día de marca no sale de aprendizaje. Marca es un grupo.
- **Maximizar conversiones ahora**: es lo que hay y produjo CPC $24 y CPL $94 en las dos últimas semanas; vuelve cuando la estructura nueva tenga 15+ conv/mes limpias.
- **tCPA ahora**: hay ~23 conv/mes, no 30 en 30 días, y el CPA observado ($43) no es el deseado; fijarlo a $26 asfixiaría el volumen (caso Integrity Plumbing del playbook).
- **Amplia / AI Max**: explica el 53% de desperdicio rastreable; solo con ~50 conversiones limpias acumuladas, tCPA maduro y aprobación de Jhombis.
- **3 RSA por grupo**: con 2–3 clics/día un A/B es ruido (estándar 4 vigente: 1 RSA, máx. 2, bajo $1.500/mes).
- **Grupos por ciudad**: 0–20 búsquedas/mes por combinación; inserción de keyword en el H1 resuelve lo mismo.
- **"24 hour" y precio**: sin cobertura nocturna confirmada ni landing de precios.
- **PMax, Display, Video**: PMax tendría $5–8/día contra $78 necesarios; fracasó en las 2 cuentas del MCC que la abrieron antes de 3 meses. Display solo como remarketing en Fase 4.
- **Campaña de taller / smog**: fuera del objetivo; se negativa en AG1–AG3.
- **Horas en el copy** ("7 AM–10 PM"): no hasta verificar `customer.time_zone` (caso Pro Phase).

## Riesgos y supuestos
- **CPC**: si con tope de $9 la campaña no gasta $18/día en la primera semana, subir el tope a $11 y luego $13 antes de abrir amplia; nunca quitar el tope.
- **Landing**: si el cliente no da acceso ni DNS, la vía B queda en subdominio de GHL/Leadpages (funciona para Ads, peor para marca); se documenta.
- **"Form Fill"**: si dispara con un evento de clic y no con un envío real, se pasa a secundaria; optimizar hacia ella sería peor que no medirla.
- **Volumen rural**: salir de amplia baja impresiones; se compensa con Roadside, trailers y marca y con el tope de CPC, no con presupuesto.
- **Golden Empire** a 5 mi con 45 camiones: vigilar Auction Insights en cada revisión.
- **CPL objetivo provisional** del benchmark; se recalcula cuando el cliente dé ticket y tasa de cierre.
- **Estacionalidad**: temporada baja de noviembre a marzo; AG3 trailers se reactiva en abril.

Siguiente skill: `/roadmap` (hecho el 2026-10-06, ver roadmap.md v2) y, para la landing vía B, `/landing-ghl precision-towing todos`.
