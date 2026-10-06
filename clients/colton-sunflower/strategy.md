---
cliente: Colton Sunflower Burial and Cremation
slug: colton-sunflower
actualizado: 2026-10-06
version: 2.0
nota_v2.0: estructura nueva tras /diagnose 2026-10-06 — se sale de la amplia (92% del gasto) a frase + exacta, 5 grupos (Cremation, Cremation Prices, Funeral Home, Burial, Brand), tope de CPC $7 → $8. Corrige v1.x: la campaña YA tenía tope de $7 (no era "sin tope").
supuestos:
  - audit-site.md (12/22), competitors.md y benchmark.md del 2026-10-01; diagnóstico del 2026-10-06 (log/2026-10-06-diagnose.md).
  - Brief sin entrevista: ticket, margen, capacidad, idioma, mascotas, 24/7 y relación con Inland Memorial / Murrieta Valley están PENDIENTES.
  - Presupuesto: se planifica con el diario actual ($49 ≈ $1,490/mes). El nombre de la campaña dice $2,500/mes; falta confirmar si incluye fee.
  - Sin volumen local por keyword (no hay Keyword Planner con geo en la sesión; Semrush es nacional). El volumen real de frase/exacta se valida en los primeros 7 días con la regla de guarda.
---

# Estrategia Google Ads — Colton Sunflower Burial and Cremation

## Resumen ejecutivo
- La cuenta **ya está activa** (desde 2026-08-03): $3,015.16 gastados, 8 conversiones, **CPA $377** contra $73 de mediana en las funerarias del MCC. Esto es un **rescate**, no un lanzamiento.
- **Causa raíz (diagnóstico del 06-oct)**: la **amplia** se lleva el **92% del gasto** ($2,767.32 de $3,001.71) y encuentra búsquedas nuevas más rápido de lo que se pueden negar. Después de las 76 negativas del 01-oct, el 72% del gasto visible siguió siendo basura. Las keywords de frase/exacta casi no reciben impresiones porque la amplia gana la subasta interna.
- **Estructura nueva**: 1 campaña Search (la actual, para conservar historial) con **5 ad groups**: Cremation, Cremation Prices, Funeral Home, Burial y Brand. **Solo frase + exacta, cero amplia.** 1 RSA por grupo.
- Puja (playbook §5): **Max. clics con tope de CPC**. Ya tiene **tope de $7**; se sube a **$8** el día de la reestructura (IS perdido por ranking de 55–75%; CPC mediano del nicho $8.64). Pasa a **Maximizar conversiones** con 15+ conv/mes estables y Form Fill medido. tCPA no llega con este presupuesto.
- Presupuesto: $49/día (~$1,490/mes). **CPL objetivo: $73** (rango $58–87). Escenario base: ~19–24 conv/mes si la tasa de conversión sube al rango del nicho (8–10%).
- Ángulo frente a la competencia online ($995 de Meadow/After): **crematorio propio, "never leaves our care"**, witness cremation y capilla local.

## Benchmark usado (Search, últimos 30d al 30-sep)
| Cuenta | Puja | Gasto | Conv. | CPA | CPC |
|---|---|---|---|---|---|
| Sunflower Cremation Services (Riverside) | Max conv | $1,052 | 17.5 | $60 | $6.12 |
| Hemet Affordable B&C | Max conv | $1,345 | 14 | $96 | $11.80 |
| Swan B&C | Max conv | $912 | 9 | $101 | $5.66 |
| Murrieta Valley FH | Max conv | $1,155 | 7 | $165 | $9.96 |
| **Colton Sunflower** | **Max clics, tope $7** | **$1,457** | **4** | **$364** | $6.25 |

Las que convierten usan Maximizar conversiones porque tienen 7–20 conv/mes de historial. Colton (~4) sigue en Max. clics con tope (playbook §5). Su mejor keyword es de precio ("cremation cost": $44 de CPA en Riverside).

## Campañas
| Campaña | Objetivo | Presupuesto/día | % | Puja | Geo | Horario |
|---|---|---|---|---|---|---|
| Colton Sunflower — Search (actual, 24095361792) | Llamadas + formularios | $49 | 100% (la marca vive como ad group dentro) | Max. clics, tope $7 → **$8** → Max. conversiones con 15+ conv/mes | Presencia ✅ · radio PENDIENTE (propuesta ~15 mi alrededor de Colton) | 24/7 (las 8 conv fueron entre 9:00 y 19:59, pero con <60 clics por franja no se concluye; se mantiene si alguien contesta de noche) |

**Por qué una campaña y 5 grupos:** con $600–1,500/mes el límite del playbook es 1 campaña y 3–5 grupos. La marca va como **ad group** (no como campaña aparte) para no fragmentar el presupuesto; su gasto es mínimo.

**Por qué cero amplia:** la amplia trajo 7 de las 8 conversiones, pero a $395 cada una, y sigue abriendo búsquedas nuevas sin intención ("legacy", "types of funerals", "plots for burial", otras ciudades, competidores, español). Con frase en términos cortos ("funeral home near me", "cremation services", "direct cremation") se mantiene el alcance comercial y se controla el significado.

**RSA:** 1 por ad group (máx. 2). Con ~8 clics/día un A/B es ruido (playbook §9).

## Estructura por campaña
### Campaña: Colton Sunflower — Search
| Ad group | Keywords (frase "…" · exacta […]) | Landing | H1 pinneado | Cambio |
|---|---|---|---|---|
| **Cremation** (renombra "Cremation Services"; absorbe "Cremation With Service") | [cremation near me] · [cremation services near me] · [direct cremation near me] · [cremation san bernardino] · [crematorium near me] · "cremation services" · "cremation near me" · "direct cremation" · "crematorium" · "crematory" · "affordable/cheap/low cost cremation" · "simple cremation" · "cremation with viewing" · "cremation with memorial service" · "witness cremation" · "funeral and cremation services" · "colton cremation" · "san bernardino cremation" · "cremation services san bernardino" · "cremation fontana/rialto/redlands" | /cremation/ | Cremation Services Near You | 18 nuevas, 6 se mantienen, amplias pausadas |
| **Cremation Prices** (nuevo) | [cremation cost] · [cremation prices] · [how much does cremation cost] · "cremation cost" · "cremation price(s)" · "cost of cremation" · "how much is cremation" · "how much does cremation cost" · "cremation packages" · "simple cremation cost" · "basic cremation cost" | /pricing/ | Cremation Cost in Your Area | grupo nuevo + RSA nuevo |
| **Funeral Home** (se mantiene) | [funeral home near me] · [funeral homes near me] · [mortuary near me] · [funeral homes in colton ca] · [funeral homes in san bernardino ca] · "funeral home near me" · "funeral homes near me" · "mortuary near me" · "funeral homes in colton" · "funeral home colton" · "funeral home san bernardino" · "funeral homes in san bernardino" · "mortuary san bernardino" · "funeral homes in fontana/rialto/redlands" · "affordable funeral home" · "funeral services near me" · "funeral services" · "funeral homes" · "funeral packages" · "funeral home prices" | / (requiere formulario) | Funeral Home in Colton, CA | 19 nuevas, amplias pausadas |
| **Burial** (renombra "Burial Services") | [burial services near me] · "burial services near me" · "burial services" · "direct burial" · "graveside service" · "traditional burial" · "burial near me" | /burial/ | Burial Services Near You | 5 nuevas, amplias pausadas |
| **Brand** (nuevo, condicional) | [sunflower crematory] · [colton sunflower] · [colton sunflower burial and cremation] · "sunflower crematory colton" | / | Colton Sunflower Cremation | grupo nuevo + RSA nuevo |

Lista completa con acción por keyword (crear / mantener / mover / pausar): `data/estructura-2026-10-06.csv`. Volúmenes nacionales en `data/keywords.csv`.

**Migración (sobre la campaña actual, el mismo día):**
1. Crear las keywords nuevas en frase y exacta.
2. Pausar (no borrar) todas las amplias activas. Las 10 que más gastaron suman $2,098 y 4 conversiones.
3. Mover "cremation cost", "cremation price" y "basic cremation cost" al grupo Cremation Prices.
4. Crear los grupos Cremation Prices y Brand, con 1 RSA cada uno (copy en `data/ads-search.md`).
5. Subir el tope de CPC de $7 a $8.
6. Aplicar las negativas propuestas y quitar how / Fontana / online.

**Regla de guarda (volumen)**: si en los primeros 7 días el gasto diario promedio baja de $34 (70% del presupuesto), se agregan más frases cortas ("cremation", "mortuary" con calificadores) y se sube el tope a $9. **No se vuelve a la amplia.**

**Negativas entre grupos** (frase, nivel ad group):
- Cremation: -cost, -price, -prices, -"how much".
- Cremation Prices: -near me (el near me va a Cremation).
- Funeral Home: -cremation, -burial.
- Burial: -cremation.
- Brand: sin negativas; los demás grupos excluyen "sunflower".

**No se puja por** [sunflower cremation] (es Sunflower Cremation Services Riverside, cliente PMM) ni por "inland memorial" / "murrieta valley".

## Keywords descartadas y por qué
| Término | Motivo |
|---|---|
| cremation, funeral home, mortuary (sueltas) | Genéricas, mucha intención informacional; solo con modificador local o "near me" |
| obituaries, recent deaths, funerals today | Informacional/evento (ya negativas) |
| caskets, headstones, urns, plots, costco | Producto (ya negativas; "plots" suelta propuesta el 06-oct) |
| pet/dog/cat cremation | Otro servicio (ya negativas). Revisar si el cliente lo ofrece |
| average cost, in california, assistance, benefits | Investigación o ayudas (ya negativas) |
| inland memorial | Cliente PMM hermano |
| montecito, cortner, emerson, family funeral chapel, meadow, presidio… | Competidores (ya negativas) |
| funeraria cerca de mi (320) | Condicional: solo si atienden en español |
| funeral planning, funeral arrangements, planning a funeral service | Informacionales: $82 en 2 meses, 0 conv; se pausan |
| colton funeral chapel | Ambigua (¿marca del cliente o de otra funeraria?); pasa a Brand solo si se confirma |

## Copy
Completo en `data/ads-search.md`: 15 headlines + 4 descripciones por grupo (v2.0: el copy de "Cremation With Service" se suma al grupo Cremation; Brand usa el de Funeral Home con H1 "Colton Sunflower Cremation"), con límites de caracteres validados, más extensiones. **Actualización 2026-10-01:** el sitio confirma family-owned, 24/7, crematorio propio, licencia FD2479, no hidden fees y los precios ($1,175 cremación, $1,995 entierro). Esos claims ya no llevan `[C]`. Nuevo ad group candidato para F2: **Veteran Cremation** ($1,350 / $2,800).

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| coltonfuneral.com/ | Sí (URL final de Funeral Home y Brand) | Cliente/PMM | Falta formulario |
| coltonfuneral.com/cremation/ | Sí (URL final de Cremation, 3 conv.) | Cliente/PMM | Formulario al pie |
| /pricing/ | **Sí** (URL final de Cremation Prices; $1,175, $1,995, veteranos) | PMM/Cliente | Falta formulario |
| /burial/ | **Sí** | PMM/Cliente | No (formulario al pie) |
| Página de gracias + Form Fill | **No** (Elementor inline; /thank-you/ 404) | PMM | **Sí**: sin esto no se cuentan bien las conversiones ni se puede pasar después a Max conversiones |
| Formulario arriba en / , /cremation/, /pricing/ | No | PMM/Cliente | **Sí** (ver audit-site.md) |

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |
|---|---|---|---|
| F0 Rescate (oct 1–15) | $1,490 | Search 100% | Form Fill medido y probado; negativas "how", "Fontana" y "online" corregidas; estructura v2.0 (5 grupos, frase/exacta, cero amplia); 1 RSA por grupo; tope de CPC $8 |
| F1 Max clics con tope (relanzamiento, ~4–6 sem.) | $1,490 | 1 campaña; Brand dentro como ad group | 30d con ≥10 conv., CPA ≤ $150 y tasa de conversión ≥ 5% |
| F2 Optimización | $1,490 → $2,500 si se confirma neto | Más peso a cremación según CPA; nuevos grupos **Veteran Cremation** y **Pre-Planning**; prueba de "cremation cost" en amplia (OK de Jhombis) | CPA 30d ≤ $87 (P50 +20%) durante 2 revisiones seguidas → subir presupuesto |
| F3 tCPA / PMax | ≥ $2,500 | — | ≥30 conv/30d con tracking confiable (con $1,490 exige CPA ≤ $50; poco probable) |

## Por qué NO (todavía)
- **PMax**: 4 conversiones en 30d contra las 30+/mes que pide `pmax-cuando-y-como.md`. Además no hay assets propios verificados. Riverside y Swan sí tienen PMax, pero con 17–50 conv/mes.
- **Amplia**: 92% del gasto hasta el 06-oct y la causa del desperdicio (72% de basura aun con 542 negativas). Se vuelve a probar solo con tCPA maduro, ~50 conversiones limpias acumuladas y aprobación de Jhombis (CLAUDE.md #2). Riverside usa "cremation cost" en amplia con buen CPA, así que puede ser una prueba en F2.
- **Display / Demand Gen**: no para servicio local de alta intención. Inland Memorial tiene Display con 0 conv.
- **LSA**: en las categorías de LSA que conocemos no aparecen funerarias; verificar en la UI antes de descartarlo.
- **Remarketing/RLSA**: una funeraria es una compra urgente y única; poco valor. Se reevalúa en F2 con audiencias de observación.
- **Campaña en español**: PENDIENTE de saber si atienden en español. La demanda existe (~320/mes "funeraria cerca de mi" y varias búsquedas de precio en ES en los search terms).

## Riesgos y supuestos
1. **Canibalización con Inland Memorial / Sunflower Riverside.** Si son el mismo grupo, sus campañas pueden competir en la misma subasta en Colton y Riverside. Definir los radios para que no se solapen.
2. **Cambios de terceros**: en septiembre hay keywords removidas que no tocamos. Hay que acordar quién edita la cuenta.
3. **CPL objetivo prestado del MCC**: sin ticket ni margen del cliente puede estar mal; ajustar tras /onboard.
4. **Volumen local bajo** (los términos con ciudad tienen de 20 a 200 búsquedas/mes). El grueso viene de "near me" con geo, así que el radio decide el volumen.
5. **Volumen tras salir de la amplia**: las frase/exacta casi no tuvieron impresiones porque la amplia les ganaba. Puede bajar el gasto la primera semana; se aplica la regla de guarda ($34/día) en lugar de volver a la amplia.
6. **Tope de $8**: puede dejar fuera "cremation san bernardino" (~$11.75). Se revisa el IS perdido por ranking en D7.
