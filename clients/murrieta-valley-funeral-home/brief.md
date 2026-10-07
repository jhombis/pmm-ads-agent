---
cliente: Murrieta Valley Funeral Home
slug: murrieta-valley-funeral-home
pais: US
idioma: EN
nicho: funeraria / cremación
actualizado: 2026-10-07
estado: onboarding — audit-landing corrido
origen: investigar-cliente
customer_id: 769-956-1619
completitud: 64%
plan_es: https://claude.ai/artifact/5yeMtWsJVvj3Xtq1ZhQ3m9
plan_en: https://claude.ai/artifact/G539P3LqFyTSedy3KTD6Y7
---

# Brief — Murrieta Valley Funeral Home

> Investigado el 2026-10-07 sin entrevista (/investigar-cliente). Cada dato lleva su fuente. En la primera corrida el dominio estuvo bloqueado por el proxy; en /audit-landing (mismo día) sí se pudo leer el sitio completo (26 páginas) y el GPL en PDF: lo marcado `(web)` ya está contrastado con el HTML y lo marcado `(GPL)` sale del PDF. La API de Google Ads no tenía credenciales y Windsor no estaba autorizado: las cifras de la cuenta son de segunda mano, de extracciones hechas el 2026-09-29/10-01 para Colton Sunflower y Hemet Affordable (`data/mcc-referencias-2026-10-01.md`). Hay que correr `account_profile.py --customer 7699561619` en cuanto haya credenciales.

## Grupo de empresas (importa para geos y negativas de marca)
- Tres marcas bajo el mismo sitio (web, página Contact Us): **Murrieta Valley Funeral Home** (24651 Washington Ave, Murrieta 92562, FD1853, (951) 696-0626) · **Temecula Cremation & Burial** (41743 Enterprise Cir N #103, Temecula 92590, FD2316, (951) 296-0890; su GPL está alojado en murrietavalleyfuneralhome.com) · **Options Funeral & Cremation Service** (601 Crane St Suite D, Lake Elsinore 92530, (951) 674-3703).
- **Colton Sunflower Burial and Cremation** (cliente PMM, cuenta 151-776-2744) usa el correo `Garland@murrietavalleyfh.com` (inferido: mismo dominio de correo que `staffs@murrietavalleyfh.com` del contacto de Murrieta → mismo grupo; sin confirmar por el cliente).
- Dueños: "Our Story" y "Our Staff" nombran a **Garland y Laurie Shreves** como dueños ("over four decades"); la página de obituarios y BBB nombran a **Peter Hamilton, Owner & Director, FDR2787** (web). Posible cambio de dueño: PENDIENTE.
- BBB: fundada 12/13/2005, 20 años, **no acreditada** (web).
- Competidor directo **Inland Memorial, Inc. – Murrieta** (cremación $855, Parting) es la cuenta PMM 934-241-5137 del grupo de Hemet, pausada en ago 2026 (clients/hemet-affordable-burial-cremation/brief.md). Dos clientes PMM en la misma subasta si se reactiva.

## Negocio
- URL: https://murrietavalleyfuneralhome.com/ (web). El dominio `murrietavalleyfh.com` es solo de correo (web).
- Base y área de servicio: Murrieta, CA. "Our funeral homes proudly serve the Southwest Riverside County communities of **Murrieta, Temecula, Wildomar, Menifee, Lake Elsinore, and Fallbrook**" (web). Geo de la cuenta: Presencia (MCC vía Windsor, patrón de las 5 cuentas del nicho; el radio exacto queda PENDIENTE hasta tener `account-profile.json`).
- Servicios (por prioridad): cremación directa · servicios funerarios y memoriales ("from traditional to uniquely innovative and personal") · entierro · servicios para veteranos · celebrant services · pre-planning (web: Our Story, home, Planning Checklist). Orden real de rentabilidad: PENDIENTE.
- Servicio estrella / servicio a evitar: PENDIENTE (sin datos por campaña/keyword de la cuenta). Lo que ya convierte en la cuenta: la búsqueda de marca "murrieta valley mortuary" (MCC vía Windsor). Referencia del nicho en el MCC: las keywords que más convierten son marca, "cremation cost", "mortuary <ciudad>", "funeral homes in <ciudad>" y "near me" (knowledge/benchmarks/funeraria-us.md).
- Diferenciadores: locally/family owned, 40+ años de experiencia de la familia, licencia FD1853 visible, servicios para veteranos con honores militares, "a staff member available 24 hours a day, 7 days a week", tres sedes en el suroeste del condado, reseñas 4.8–4.9 en Google/Birdeye (web).
- Ofertas sostenibles: **los $995 de los directorios son falsos**. GPL efectivo 2024-02-29: direct cremation **$1,361.50–1,656.50 + crematory fee $216.50 y más** (≈ $1,578–1,873 todo incluido); direct burial **$1,995**; paquetes: Memorial service with cremation **$3,015**, Viewing with cremation **$3,500**, Witness cremation with ceremony $4,000, Traditional service/burial **$3,995**, Traditional + cremation $4,070, Custom $3,200 (GPL). "Multiple payment options", tarjetas aceptadas (web: /service-options/); 3% de recargo con tarjeta (GPL). El sitio **no muestra ningún precio en HTML** (solo PDF). Promociones o planes de pago reales: PENDIENTE.
- Búsqueda de marca: **sí**: "murrieta valley funeral home" 390/mes + variantes con ciudad 320 + 140, "murrieta valley funeral home obituaries" 40, "murrieta valley mortuary" 20 (Semrush). El sitio es #1 orgánico en todas (Semrush) y la marca convierte barato en la cuenta (MCC vía Windsor).

## Mercado y demanda (Semrush, db us, 2026-10-07)
- Términos locales explícitos con volumen mínimo: "murrieta funeral home" 140 (CPC $2.87), "murrieta mortuary" 140, "mortuary murrieta ca" 110, "funeral homes in murrieta ca" 90, "funeral homes in temecula ca" 70, "murrieta cremation" 20 (CPC $6.91), "cremation services murrieta" 20 ($9.06), "temecula cremation" 20 ($5.54), "cremation lake elsinore" 20, "cremation sun city" 30 ($7.25).
- El volumen está en "near me" (se captura con geo de presencia): "funeral homes near me" 60.5K ($3.54), "cremation near me" 18.1K ($4.72), "cremation services near me" 14.8K ($4.97), "mortuary near me" 5.4K ($5.24), "direct cremation near me" 1.9K, "cheap/low cost cremation near me" 1.6K + 1.6K, "affordable cremation near me" 590, "burial services near me" 1.9K.
- Informacional/precio (intención mixta): "cremation cost" 12.1K, "how much does cremation cost" 8.1K, "funeral costs" 2.9K. En el MCC "cremation cost" en amplia convierte con Max conversiones y tracking completo (benchmark); con Max clics se vuelve fuga.
- Español: "funerarias cerca de mi" 1,900/mes nacional; si el cliente atiende en español es un ad group aparte (convirtió en Hemet). PENDIENTE.
- Veteranos: "veteran funeral services" 170, "military funeral honors" 1,300 (informacional). Pre-need: "pre planning funeral" 320.
- Ningún anunciante registrado por Semrush en 12 meses para "cremation murrieta ca" ni "funeral homes temecula ca": la subasta local explícita está poco medida; la competencia real está en "near me" (nacionales: After.com, Meadow, Neptune).
- Tráfico orgánico del sitio: 537 keywords, ~2,376 visitas/mes, pero ≈60% son nombres de difuntos que llegan a /obituary/ (sin intención comercial) (Semrush).

## Objetivo y economía
- Objetivo primario: llamadas + formularios (inferido: las cuentas del nicho en el MCC miden Form Fill + Calls from Ads + Website Calls; no se vio la lista de conversiones de esta cuenta). Confirmar: PENDIENTE.
- Presupuesto mensual: Search **$1,155–1,244/mes** (MCC vía Windsor: promedio abr–sep y 90 d jul–sep). Gasto de PMax y monto del contrato: PENDIENTE.
- Ticket promedio / margen: precios públicos (GPL) cremación directa ≈ $1,578–1,873 · paquetes con cremación $3,015–4,070 · entierro directo $1,995 · paquetes con entierro $3,200–3,995. Mezcla de servicios y margen: PENDIENTE.
- Capacidad (casos/mes): PENDIENTE.
- **CPL máximo aceptable**: PENDIENTE (falta margen y mezcla). Referencia rotulada: CPL histórico de la cuenta **$162–182** (Search, MCC vía Windsor) y mediana del nicho en el MCC **$73** (P25 $58 · P75 $133; knowledge/benchmarks/funeraria-us.md).
- Historial Google Ads: cuenta **769-956-1619** en el MCC de PMM, "Murrieta Valley FH" (clients/colton-sunflower/brief.md). Search con **Maximizar conversiones** sin tCPA: $1,244/mes, 6.8 conv/mes, **CPA $182** (abr–sep 2026); 90 d jul–sep: $3,399, 21 conv, CPL $162, CPC ~$9.96. PMax con CPA $57 sin auditar qué conversiones cuenta (MCC vía Windsor). Es la cuenta madura con **peor CPL del nicho en el MCC** (2.2× la mediana) y menor volumen de conversiones (7/mes vs 10). Fecha de inicio y estructura de campañas: PENDIENTE (requiere `account-profile.json`).

## Operación
- Horario / 24-7: oficina Mon–Fri 8:30am–5pm, Sat 9am–4pm, Sun closed (web: /contact-us/, confirmado en HTML); "staff member available 24 hours a day, 7 days a week" (web: Our Staff); Yelp lista "Open 24 hours". Hay atención 24/7 para primeras llamadas (inferido: los tres textos coinciden; quién contesta de noche PENDIENTE).
- Respuesta a leads (quién, tiempo): PENDIENTE.
- Teléfono / call tracking: (951) 696-0626 principal (web). Call tracking / número de reenvío: PENDIENTE.
- CRM (solo referencia): PENDIENTE.
- GBP: Google 4.9★ según BestProsInTown y 4.8★/148 en Birdeye (web); conteo de reseñas en Google, verificación y acceso de PMM: PENDIENTE. Yelp 4.0★/59 con 11 reseñas de 1★ (quejas de proceso y de cobros tras el pago) (web).

## Competencia
| Competidor | URL | Nota |
|---|---|---|
| England Family Mortuary (Temecula) | englandfamilymortuary.com | 4.7★/125 Yelp · crematorio propio · 24/7 · directa **$1,495** · marca 880/mes · 2º competidor orgánico (Semrush, web) |
| Miller-Jones Mortuary & Crematory (Dignity/SCI, Murrieta desde 2014) | dignitymemorial.com | 4.8★/21 Yelp · directa $1,395 · marca 720/mes · página en español que cubre Murrieta (web, Semrush) |
| Evans-Brown Mortuary (Menifee/Sun City/Perris) | — | directa $1,195 · marca 880/mes (web, Semrush) |
| Inland Memorial – Murrieta | — | directa **$855** · cuenta PMM 934-241-5137 pausada (web, repo) |
| Valley Cremation Service | valleycremationservice.com | ~$995 · 1er competidor orgánico, 18 keywords comunes (Semrush) |
| After.com · Meadow Memorials · Thomas Miller · Walker Family | after.com, meadowmemorials.com… | ~$995 online; landings SEO "cremation in Temecula/Murrieta" (web) |
| Parting Destiny (Temecula) · Dearly Beloved Mortuary | partingdestiny.com, dearlybelovedmortuary.com | pequeños; competidores orgánicos 3º y 4º (Semrush) |

Lectura: con cremación directa real de ≈ $1,578+ (GPL) el cliente es **más caro que todos los locales listados** ($855–1,495) y que los online ($995). No puede competir por precio en "cheap/affordable cremation"; el ángulo es paquetes con servicio ($3,015–4,000), local + 3 sedes + 40 años + veteranos + capilla propia, y evitar o negativizar "cheap", "cheapest", "low cost" (decisión en /strategy).

## Web y tracking
- Plataforma / quién edita: **WordPress 7.1.3 + Elementor Pro 4.1.4 + Site Kit by Google**, nginx sin caché de página (web, audit-site.md). Quién edita y acceso de PMM: PENDIENTE.
- Tag/GA4: **GTM-MRZ2HJMT** en todas las páginas + Site Kit con `GT-TQSRPXK2` y **`AW-16758859270`**; sin `G-` visible (web). Verificar que el AW sea el de 769-956-1619 y qué dispara el GTM: PENDIENTE (contenedor bloqueado por el proxy).
- Formulario → destino: Elementor Pro, 4 campos (Name, Phone, Email, Message) en casi todas las páginas, reCAPTCHA, **sin página de gracias** (`/thank-you/` 404), mensaje inline (web). Destino del correo: `staffs@murrietavalleyfh.com` (inferido: es el email de contacto publicado). Form Fill medible por URL: no, hasta crear /thank-you/.
- Requisitos de política: FTC Funeral Rule y CA B&P §7685: GPL publicado en PDF ✅ (web), licencia **FD1853** visible en GPL y Facebook ✅ (web). Tono sobrio en anuncios; no prometer "sin cargos" mientras el GPL tenga recargo del 3% con tarjeta y "crematory fee as quoted".

## LSA (solo US)
- Aplica: **no por ahora**: "funeral home" no es categoría habitual de LSA en California y no se verificó disponibilidad en Riverside County (mismo criterio que Hemet y Colton). Licencia FD1853 y seguro: licencia sí (web); seguro y background check: PENDIENTE.

## Pendientes
- [ ] **Bloqueante**: credenciales de la API (o Windsor) para `account_profile.py --customer 7699561619`: estructura, conversiones, search terms y geo real de la cuenta.
- [ ] **Bloqueante**: margen y mezcla de servicios (cremación directa vs servicio completo) + capacidad → CPL máximo.
- [x] Google Tag / GTM presentes en todo el sitio (audit-site.md 2026-10-07).
- [ ] **Bloqueante**: página de gracias + Form Fill medible, verificar que AW-16758859270 sea el de la cuenta, duración mínima de llamada y número de reenvío (un solo teléfono por landing).
- [ ] **Bloqueante**: landings de cremación y funeral/entierro (hoy no existen) antes de seguir pagando clics.
- [ ] GBP: conteo de reseñas en Google, verificación y acceso de PMM (activo de ubicación), para las tres sedes.
- [ ] Confirmar el grupo (Colton Sunflower, Temecula Cremation & Burial, Options) y el dueño actual (Shreves vs Hamilton); coordinar geos y negativas de marca entre cuentas PMM, incluida Inland Memorial Murrieta.
- [ ] Quién contesta de noche y en cuánto tiempo se devuelve un lead.
- [ ] ¿Atienden en español? Decide ad group ES vs negativas del grupo E.
- [ ] Ofertas sostenibles (planes de pago, pre-need con precio congelado) y servicio que más quiere vender el dueño.
- [ ] Acceso al WordPress (Elementor Pro) para la página de gracias, el redirect del formulario y las landings.
- [x] /audit-landing corrido (2026-10-07): 11/22, requiere ajustes.

## Fuentes consultadas
| Fuente | Estado | Archivo |
|---|---|---|
| Google Ads API (cuenta 769-956-1619) | sin credenciales (no hay `google-ads.yaml` ni `GOOGLE_ADS_*`) | `data/mcc-referencias-2026-10-01.md` (cifras de segunda mano, Windsor 2026-09-29/10-01) |
| Web (26 páginas) | ok en la segunda corrida (/audit-landing); la primera fue bloqueada por el proxy | `data/site-scan.json`, `data/web-findings-2026-10-07.md`, `data/gpl-2024-02-29.txt` |
| PageSpeed | sin clave; API pública con cuota agotada (429). Velocidad medida en laboratorio | `data/perf-lab-2026-10-07.json` |
| Semrush | ok (domain_rank, phrase_these ×2, resource_organic, domain_organic_organic, phrase_adwords_historical ×2) | `data/semrush-2026-10-07.json` |
| Windsor | sin autorizar en esta sesión | — |
| GBP | solo agregadores de terceros | `data/web-findings-2026-10-07.md` |

## Hallazgos que ya importan para la estrategia
- **CPL de Search $162–182 contra $73 de mediana del nicho en el MCC**, con Max conversiones y solo ~7 conv/mes: antes de tocar puja hay que ver search terms y acciones de conversión (orden del playbook: medición → negativas → estructura → puja).
- **La marca se la están cobrando dentro de la genérica** (patrón visto en Hemet: $8.6/clic por marca): con 390 + 460 búsquedas/mes de marca, una campaña de marca aparte a $1–2/clic es la conversión más barata disponible.
- **Dos cuentas PMM en la misma subasta**: Inland Memorial Murrieta ($855) está pausada; si se reactiva compite con este cliente. Colton Sunflower es del mismo grupo: alinear geos y negativas de marca.
- **El volumen está en "near me", no en "cremation murrieta"** (20/mes): la estructura debe ser por servicio (Cremación / Funeral-Burial / Marca), no por ciudad, dentro del límite de fragmentación para $1,200/mes (1 campaña, 3–5 grupos + marca).
- **Reputación desigual**: Google 4.8–4.9 vs Yelp 4.0 con 11 reseñas de 1★; la landing debe mostrar las de Google y el GBP debe estar ligado como activo de ubicación.
- **PMax a $57 de CPA sin auditar**: puede estar contando acciones locales o llamadas cortas; no usar como referencia hasta ver la lista de conversiones.
- **Tracking presente pero sin cerrar**: GTM + AW-16758859270 en todas las páginas, pero el formulario no tiene página de gracias y hay dos teléfonos en la home sin número de reenvío. Verificar qué conversiones registra la cuenta antes de leer cualquier CPL.
- **El precio real de cremación directa es ≈ $1,578–1,873 (GPL), no $995**: el cliente es el más caro de la SERP local. "Cheap/low cost cremation" (3,200 búsquedas/mes) es tráfico que no va a convertir; decidir en /strategy si se negativiza.
- **Landing**: 11/22 en audit-site.md. No existe página de cremación; el tráfico de Ads aterriza en una home sin H1, sin precio y con obituarios en la segunda pantalla.

## Preguntas para el cliente (solo lo que no se pudo investigar)
1. **(Bloquea el CPL máximo)** ¿Qué porcentaje de casos termina en cremación directa ($995) vs servicio completo, y cuál es el margen aproximado de cada uno?
2. **(Bloquea el CPL máximo)** ¿Cuántos casos nuevos al mes pueden atender entre las tres sedes?
3. **(Bloquea el lanzamiento)** ¿Quién contesta el (951) 696-0626 de noche y fines de semana (director, answering service) y en cuánto tiempo devuelven un formulario? ¿Aceptan un número de reenvío para medir llamadas?
4. **(Bloquea el lanzamiento)** ¿Quién administra el WordPress (Elementor)? Necesitamos acceso para crear la página de gracias, redirigir el formulario y montar las landings de cremación y funeral.
5. ¿La ficha de Google de Murrieta (y las de Temecula y Lake Elsinore) están verificadas y nos pueden dar acceso como administradores?
6. ¿Quién es el dueño actual (Garland y Laurie Shreves, o Peter Hamilton)? ¿Colton Sunflower, Temecula Cremation & Burial y Options son del mismo grupo? Lo necesitamos para no competir contra sus propias cuentas.
7. ¿Atienden familias en español? Hay 1,900 búsquedas/mes de "funerarias cerca de mi".
8. ¿Qué servicio quieren vender más (cremación directa, paquetes con servicio, veteranos, pre-need)? ¿Podemos publicar en la landing los precios del GPL (cremación directa desde $1,578 todo incluido, paquetes $3,015–4,000) y qué plan de pago pueden sostener?
