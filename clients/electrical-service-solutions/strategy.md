---
cliente: Electrical Service Solutions
slug: electrical-service-solutions
pais: US
actualizado: 2026-10-20
version: 1.1
supuestos:
  - "Sin ticket, margen ni tasa de cierre: el CPL objetivo sale del benchmark interno ($100–150), no del margen del cliente"
  - "Sin volumen por ZIP: todos los volúmenes son nacionales (Semrush us). El volumen de los 4 ZIP + Monroeville sale de Keyword Planner antes de lanzar"
  - "Zona horaria de la cuenta 384-080-6970 sin confirmar: la programación va en hora del Este del cliente y se convierte al configurar"
  - "Condiciones del financiamiento sin confirmar: los anuncios dicen solo 'Financing Available'"
---

# Estrategia Google Ads — Electrical Service Solutions

> Versión 1.1 (20-oct): la auditoría de la web ya está hecha (`audit-site.md`, 10/22, requiere ajustes). Quedan dos supuestos: el ticket y el volumen por ZIP. Cada decisión que depende de ellos dice qué la cambia. Nada de esto se escribe en Google Ads sin aprobación de Jhombis con la lista de cambios a la vista.

## Datos (antes de la estrategia)
- **Cliente**: contratista eléctrico con 40+ años que **solo quiere trabajos de paneles**: upgrades residenciales y comerciales, y cambio de servicio (brief).
- **Geo**: ZIP 15102 (Bethel Park), 15241 (Upper St. Clair), 15228 (Mt. Lebanon), 15237 (McCandless / North Hills) y Monroeville (15146). Sin dirección publicada (brief).
- **Pauta**: $1,293.75/mes = 57.5% del contrato de $2,250 → $42.56/día (brief).
- **Cuenta**: 384-080-6970, sin historial: 0 filas en 2 años (brief, benchmark).
- **Competencia**: Semrush no ve a ningún electricista local pujando. En paneles solo pujan Angi, HomeAdvisor y anunciantes de otros estados. Mr. Electric y South Hills Electric también ofrecen financiamiento (competitors.md).
- **Benchmark**: 5 cuentas, distribución bimodal. Max. conversiones con historial: CPL $18–34. Max. clics: CPL $84–580. El CPC real de los clics de panel en el MCC fue ~$7.72 (otros mercados, 17 clics: ruido). En paneles, $67.74 de $131.30 se fueron en búsquedas de precio, con 0 conversiones (benchmark.md).
- **Keywords**: 55 términos clasificados en `data/keywords.csv` (volúmenes nacionales, Semrush).

## Matemática de presupuesto (playbook §4)
- $42.56/día ÷ CPC ~$12 ≈ **3.5 clics/día → ~108 clics/mes**.
- Escenarios (benchmark.md):

| Escenario | CPC | Clics/mes | Tasa conv. | Conv./mes | CPL |
|---|---|---|---|---|---|
| Pesimista | $14 | 92 | 5% | 4.6 | $280 |
| **Base** | **$12** | **108** | **8%** | **8.6** | **$150** |
| Optimista | $10 | 129 | 12% | 15.5 | $83 |

- **Límite de fragmentación** ($600–1,500/mes): 1 campaña y 3–5 grupos. Van **4 grupos**.
- **Regla de aprendizaje**: cada campaña con Smart Bidding necesita ≥3× CPL/día, es decir $300–450/día. No se alcanza, y por eso va 1 sola campaña con Max. clics con tope.
- **tCPA**: no es alcanzable con esta pauta (≥30 conv. en 30 días pediría $3,000–4,500/mes).

## Resumen ejecutivo
1. **1 campaña Search** de paneles, 4 grupos (upgrade/reemplazo de panel, cambio de servicio, fusibles, panel comercial), con los **$42.56/día** completos.
2. **Puja**: Max. clics con **tope de CPC de $15**, frase + exacta, **Presencia** en los 4 ZIP + Monroeville, horario del cliente (L–V 9–21, S–D 9–17, hora del Este).
3. **CPL objetivo F1: $100–150** (benchmark), con techo de alarma en $280. Se reemplaza por el CPL máximo cuando llegue el ticket.
4. **~9 prospectos/mes** en el escenario base. **Max. conversiones** cuando haya 15+ conversiones/mes estables 2 meses seguidos con medición limpia; tCPA no entra en el horizonte con esta pauta.
5. **No van**: "electrician" genérico ni ningún otro servicio eléctrico, marca, PMax, Display ni remarketing. LSA va como pista paralela cuando haya GBP y licencia.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| ESS · Search · Paneles · South Hills/North Hills/Monroeville | Llamadas y formularios de paneles | $42.56 | 100% | Max. clics, tope CPC $15 | Presencia: ZIP 15102, 15241, 15228, 15237 + Monroeville, PA. Excluir el resto de países | L–V 9:00–21:00 · S–D 9:00–17:00 (hora del Este) |

Configuración: solo red de Búsqueda (sin socios ni Display), rotación optimizada, sin aplicación automática de recomendaciones, sin segmentos de audiencia como exclusión, AI Max apagado.

**Tope de $15**: el CPC real de los clics de panel en el MCC fue ~$7.72 y Semrush da $8–18. Con $15, el presupuesto paga ≥2.8 clics/día, y quedan fuera casi todas las subastas de "near me" de $18–37. Se revisa a D7 y D14: si la cuota perdida por ranking pasa del 60% **y** se gasta menos del 60% del presupuesto, sube a $18.

**Horario**: si la cuenta está en hora del Pacífico, L–V 6:00–18:00 y S–D 6:00–14:00 (−3 h). Las emergencias y la noche no se abren hasta saber quién contesta (estándar 10).

## Estructura por campaña
### Campaña: ESS · Search · Paneles
| Ad group | Keywords (match) | Vol. US/mes | Landing | H1 pinneado |
|---|---|---|---|---|
| **Panel Upgrade** | [electrical panel upgrade], [electrical panel replacement], [breaker box replacement], [electrical panel upgrade near me], [electrical panel replacement near me] + frase: electrical panel upgrade, electrical panel replacement, electric panel upgrade, panel upgrade, electrical panel installation, breaker box replacement, breaker panel replacement, circuit breaker panel replacement, main panel upgrade, breaker box upgrade, breaker panel upgrade, circuit breaker panel upgrade, panel upgrade electrician, electrician for panel upgrade, electrical box replacement, electric panel replacement near me, panel upgrade near me, zinsco panel replacement, federal pacific panel replacement, fpe panel replacement | ~44,300 | /residential-electric-service-panel-upgrades-replacements/ | Electrical Panel Upgrades |
| **Service Upgrade** | [electrical service upgrade], [200 amp panel upgrade] + frase: electrical service upgrade (near me), upgrade electrical service, electrical service change, 200 amp service upgrade, upgrade to 200 amp service, 100 amp to 200 amp upgrade, 400 amp service upgrade, meter base replacement | ~2,800 | /residential-electric-service-panel-upgrades-replacements/ (sección "Panel Upgrade or Service Change-Out?") | Electrical Service Upgrades |
| **Fuse Box** | [fuse box replacement] + frase: fuse box replacement (near me), replace fuse box, replace fuse box with breaker panel, fuse panel replacement, fuse box to breaker box | ~2,000 | /residential-electric-service-panel-upgrades-replacements/ (menciona fusibles) | Fuse Box Replacement |
| **Commercial Panel** | [commercial electrical panel upgrade] + frase: commercial electrical panel, commercial electrical panel upgrade, commercial electrical service upgrade, commercial panel replacement | ~350 | /commercial-electric-service-panel-upgrades-replacements/ | Commercial Panel Upgrades |

- Los volúmenes son **nacionales**. En 4 ZIP + Monroeville serán una fracción mínima: Keyword Planner con la geo exacta es la condición para fijar el tope y confirmar que la pauta se puede gastar.
- **Ciudades**: no hay grupos por ciudad (ninguna combinación servicio × ciudad tiene ≥100 búsquedas). Las ciudades van en headlines y en la geo.
- **Comercial**: el grupo se deja por pedido del cliente, pero con esta geo es probable que casi no imprima. Si a D30 tiene <50 impresiones, en F2 se prueba [commercial electrician near me] en exacta, con las negativas de "lo que el cliente no hace" (competitors.md: 4,400/mes US, $24.40, cualquier trabajo).
- **Subpaneles** ("subpanel installation", 480/mes US): quedan fuera hasta que el cliente confirme que los hace. Son trabajo de panel, pero de ticket menor.

Negativas específicas por grupo (para que cada búsqueda caiga en su grupo):
- Panel Upgrade: `fuse`, `commercial`
- Service Upgrade: `fuse`, `commercial`
- Fuse Box: `commercial`
- Commercial Panel: `residential`, `home`, `house`

## Keywords descartadas y por qué
| Keyword | Vol. US | Motivo |
|---|---|---|
| electrician pittsburgh / pittsburgh electrician / electrician pittsburgh pa | 590 / 320 / 260 | Genéricas: el cliente solo quiere paneles (brief) |
| commercial electrician near me / commercial electrical contractor near me | 4,400 / 320 | Cualquier trabajo comercial. Prueba en F2 solo si el grupo comercial no imprime |
| electrical panel replacement cost / electrical panel upgrade cost / panel upgrade cost | 2,400 / 1,300 / 320 | Precio: $67.74 con 0 conversiones en el benchmark |
| 200 amp service | 720 | Sin verbo de servicio: trae calibres de cable y precios |
| electrical financing | 260 | El financiamiento es mensaje, no segmentación |
| subpanel installation / sub panel installation | 480 / 390 | F2, si el cliente confirma que los hace |
| electrical service solutions (marca) | 20 | No hay búsqueda de marca real |

Detalle en `data/keywords.csv`.

## Negativas
- **Lista universal PMM** a nivel de cuenta desde el día 1 (`knowledge/negativas-universales.md`), con estos ajustes para el cliente: **no** se niegan `replace`, `panel`, `service`, `upgrade`, `commercial`, `breaker` ni marcas de panel (zinsco, federal pacific, siemens, eaton, square d; reconciliación PMM del 23-sep). `free` **no** se niega: la web ofrece "Get A Free Quote" (audit-site.md, playbook §6.5).
- **Nicho** (`data/negatives-nicho.txt`, 123 términos a nivel de campaña):
  - Lo que el cliente no hace (generadores, EV, iluminación, tomas, ventiladores, rewiring, inspecciones…).
  - Paneles que no son eléctricos (solar panel en exacta, garage door panel, wall panel…).
  - Precio e información (cost to, how much, average cost, diagram…).
  - Compra de producto, empleo y Duquesne Light.
  - 27 entradas de competidores y agregadores (South Hills Electric solo en exacta, porque "South Hills" es la zona del cliente).
  - Genéricas de electricista en exacta.
- **Lista final aprobada** (/negatives init, 20-oct; `data/2026-10-20-negatives.txt`): 167 de cuenta + 136 de campaña (bloque de electricistas + 97 de nicho únicas) + 8 por ad group. 11 excluidas por choque (free, for free, no cost, utility/utilities, marcas de panel, not working). Se aplican con Windsor al crear la campaña.
- **Validación**: 0 choques contra las 42 keywords activas de F1 (comprobado por script). "solar" no se niega suelto: un upgrade de panel para solar es un lead válido.

## Copy
Detalle en `data/ads-search-paneles.md`. 1 RSA por grupo (pauta <$1,500/mes, estándar 4): H1 pinneado + 2 headlines del grupo + 12 compartidas = 15; 4 descripciones (la comercial cambia la primera por una de verticales).

- **Ángulo** (competitors.md): especialista en paneles + 40+ años + financiamiento, el combo que ningún local junta.
- **Headlines compartidas**: 40+ Years Of Experience · Financing Available · Electrical Panel Specialists · Panel & Service Upgrades · Residential & Commercial · Open 7 Days A Week · Bethel Park & Mt. Lebanon · Upper St. Clair & McCandless · Serving Monroeville, PA · Ask About Financing Options · Get A Free Quote · Permits & Inspection Handled.
- **Extensiones**:
  - Llamada al CTN (412) 666-9290, con el horario del cliente.
  - 4 sitelinks: Panel Upgrades, Service Upgrades, Commercial Panels y Financing. El de Financing apunta a la sección de financiamiento **de la web**, porque los sitelinks tienen que ser del mismo dominio.
  - Callouts: 40+ Years Experience, Financing Available, Free Quotes, Permits & Inspection, Open 7 Days, Residential & Commercial, Panel Specialists, Service Change-Outs.
  - Snippet de servicios.
- **Sí se usa** (lo dice la web): Free Quote, permisos e inspección incluidos, trabajo de noche y fines de semana en comercial, financiamiento "on approved credit".
- **No se promete** (no hay fuente): licensed & insured, 24/7, same-day ni condiciones de financiamiento en el anuncio. La web publica plazos de 7–20 años, pero en un anuncio los plazos o cuotas pueden obligar a divulgar APR y condiciones.

## Medición (playbook §7) — va antes de cualquier ajuste de puja
| Acción | Tipo | Cómo | Estado |
|---|---|---|---|
| Calls from ads | Primaria | Extensión de llamada con el CTN (412) 666-9290 y desvío de Google; duración mínima 60 s | PENDIENTE (bloqueante) |
| Formulario enviado | Primaria | Redirect de Elementor a /thank-you/ + Google Tag; el envío llega a chris@electrical-service-solutions.com | PENDIENTE: hoy no hay tag ni página de gracias (audit-site.md) |
| Clic en tel: de la web | Secundaria | Evento del Google Tag sobre el enlace al CTN | PENDIENTE |
| Llamadas calificadas | Fuente de verdad | CallFire: llamante único con ≥60 s contestados (`knowledge/call-tracking.md`) | Listo: el CTN reenvía y se contesta |

Todo se prueba con Tag Assistant antes de gastar (estándar 7). Como el CTN se publica en la web y en los anuncios, CallFire mezcla las dos fuentes. La parte de Ads sale de "Calls from ads".

## Landings requeridas
Auditoría del 20-oct (`audit-site.md`): 10/22, **requiere ajustes antes de lanzar**. Las páginas de servicio ya existen. Lo que falta es medición y que el formulario quede arriba.

| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| /residential-electric-service-panel-upgrades-replacements/ (Panel Upgrade, Service Upgrade, Fuse Box) | Sí. H1 correcto; formulario a 2,821 px | PMM: subir el formulario o un botón debajo del H1 | **Sí** (formulario arriba) |
| /commercial-electric-service-panel-upgrades-replacements/ (Commercial Panel) | Sí. H1 correcto; formulario a 2,622 px | PMM: igual que la residencial | **Sí** (formulario arriba) |
| Google Tag + conversiones (formulario y clic en tel:) en todo el sitio | No: Site Kit instalado sin conectar | PMM | **Sí** |
| /thank-you/ (Redirect del formulario de Elementor) | No | PMM | **Sí** |
| /financing/ (destino del sitelink; hoy el menú sale a purefinancegroup.com) | No | PMM | No (sin ella, el sitelink de financiamiento se omite) |

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |
|---|---|---|---|
| F0 · Medición y web | $0 | — | Calls from ads + formulario probados con Tag Assistant; bloqueantes de audit-site.md resueltos (tag, /thank-you/, formulario arriba); universal + nicho aplicadas; volumen por ZIP revisado en Keyword Planner |
| F1 · Lanzamiento | $1,293.75 | Search Paneles 100% ($42.56/día), Max. clics tope $15 | 30 días corridos, ≥50 clics, search terms limpiados 2 veces, CPL observado |
| F2 · Optimización | $1,293.75 | Igual; ajuste del tope a D7/D14 y prueba comercial si no imprime | 15+ conversiones/mes 2 meses seguidos con medición limpia (calificadas en CallFire) |
| F3 · Max. conversiones | $1,293.75 (o más si el cliente escala: PENDIENTE) | Search Paneles 100%, sin tCPA | tCPA solo con ~30 conv. en 30 días, desde el CPA observado. Con esta pauta no llega: pediría $3,000–4,500/mes |
| LSA (pista paralela) | aparte, si el cliente lo aprueba | — | GBP verificado con acceso, licencia y seguro visibles, background check; confirmar qué tipos de trabajo de panel permite LSA para electricista |

## Qué NO se va a poder concluir (playbook §9)
- Con ~108 clics/mes, **no hay A/B de anuncios**: 1 RSA por grupo.
- Una tasa por grupo pide 50+ clics. Panel Upgrade llega en ~1 mes; Service Upgrade y Fuse Box en 2–4 meses. Commercial probablemente no llegue con esta geo.
- Con 4–15 conversiones/mes, un mes con el doble es un pico, no la nueva base: se compara contra la mediana de 3 meses.
- Las audiencias en observación no dan señal.

## Por qué NO (todavía)
- **PMax**: pide Search estable, 30+ conversiones/mes con tracking confiable, exclusión de marca y assets propios (`knowledge/estrategias/pmax-cuando-y-como.md`). Con ~9 al mes, no.
- **Amplia / AI Max**: requiere ~50 conversiones limpias acumuladas, tCPA maduro y aprobación de Jhombis. Con un solo servicio y tanta ambigüedad en "panel", la amplia compraría solar, garage y precio.
- **Display / Demand Gen**: servicio local de ticket alto; no hay assets propios ni presupuesto para dividir.
- **Campaña de marca**: no hay búsqueda de marca (20/mes de una frase genérica; brief).
- **Remarketing / RLSA**: con ~108 clics/mes la lista no llega a 1,000 usuarios en un plazo útil.
- **"Electrician" genérico y emergencias**: el cliente solo quiere paneles; las emergencias no se abren hasta saber quién contesta de noche.

## Riesgos y supuestos
- **Demanda**: con 4 ZIP + Monroeville, la pauta puede no gastarse (benchmark: ~5 impresiones/día de paneles en un grupo con más geo). Si a D14 se gasta <60% con cuota de impresiones >80%, se propone al cliente ampliar a ZIP vecinos. No se toca la geo sin su aprobación.
- **Web con bloqueantes** (audit-site.md): sin Google Tag, sin página de gracias y con el formulario a ~3 pantallas en móvil. F1 no arranca hasta resolverlos (4–5 h de PMM).
- **CPL sin ticket**: $100–150 es una referencia de cuentas de servicio general. Un panel tiene ticket más alto, así que el CPL aceptable probablemente sea mayor. Se recalcula con margen × cierre × 0.3.
- **Financiamiento neutralizado**: Mr. Electric y South Hills también lo ofrecen. Sin condiciones concretas, "Financing Available" diferencia poco.
- **"Panel" ambiguo**: "panel upgrade near me" ($36.67) y "panel upgrade" traen solar, garage y paredes. Lo cubren las negativas y la revisión de search terms a D3, D7 y D14.
- **Reseñas**: CW tiene 869+ y Luminous 542; las del GBP del cliente siguen sin dato. Si son pocas, pedirlas es parte del plan (sin GBP tampoco hay activo de ubicación).
- **Zona horaria de la cuenta** sin confirmar: la programación se convierte al configurar.
