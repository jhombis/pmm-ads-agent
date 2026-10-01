---
cliente: Colton Sunflower Burial and Cremation
slug: colton-sunflower
actualizado: 2026-10-01
version: 1.1
supuestos:
  - audit-site.md hecho el 2026-10-01 (12/22): landings y claims actualizados en v1.1.
  - Sin competitors.md: competidores tomados de search terms y Semrush.
  - Sin benchmark.md formal: se usan 4 funerarias del MCC (Search, últimos 30d).
  - Brief sin entrevista: ticket, margen, capacidad, idioma, mascotas, 24/7 y relación con Inland Memorial están PENDIENTES.
  - Presupuesto: se planifica con el diario actual ($49 ≈ $1,490/mes). El nombre de la campaña dice $2,500/mes; falta confirmar si incluye fee.
  - Volúmenes de Semrush (US). Los "near me" son nacionales: el volumen local es una fracción.
---

# Estrategia Google Ads — Colton Sunflower Burial and Cremation

## Resumen ejecutivo
- La cuenta **ya está activa** (desde 2026-08-03). Esto no es un lanzamiento, es un **rescate**: CPA de $466 en 28d contra ~$100 de sus hermanas del MCC.
- **1 campaña Search** (se mantiene la actual para no perder historial) con **5 ad groups**. Opcionalmente, 1 campaña de marca de $5/día si se confirma la marca.
- Presupuesto: $49/día ($1,490/mes). **CPL objetivo F1: $100** (mediana MCC). Se esperan ~15 conv/mes.
- Puja: **Maximizar conversiones** (sin tCPA) una vez medido Form Fill. Con este presupuesto, **tCPA no llega** (requiere ~30 conv/mes, es decir CPA ≤ $50). Se reevalúa en F3.
- Lo que más pesa: matar el desperdicio (negativas, ya en curso), pasar de amplia + Max clics a frase/exacta + Max conv, y desbloquear la demanda de precio que hoy bloquean las negativas "how" y "Fontana".

## Benchmark usado (Search, últimos 30d)
| Cuenta | Puja | Gasto | Conv. | CPA | CPC |
|---|---|---|---|---|---|
| Sunflower Cremation Services (Riverside) | Max conv | $1,052 | 17.5 | $60 | $6.12 |
| Hemet Affordable B&C | Max conv | $1,345 | 14 | $96 | $11.80 |
| Swan B&C | Max conv | $912 | 9 | $101 | $5.66 |
| Murrieta Valley FH | Max conv | $1,155 | 7 | $165 | $9.96 |
| **Colton Sunflower** | **Max clics** | **$1,457** | **4** | **$364** | $6.25 |

Patrón: todas las que convierten usan Maximizar conversiones, y su mejor keyword es de precio ("cremation cost": $44 de CPA en Riverside). Hemet paga CPC de ~$12 pero convierte 12% de los clics: Max conv puja más alto por menos clics, y mejores.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| Colton Sunflower — Search (actual, 24095361792) | Llamadas + formularios | $49 | 100% (90% si se activa marca) | Max conversiones (sin tCPA) tras Form Fill | Presencia ✅. Radio PENDIENTE; propuesta: ~15 mi alrededor de Colton (San Bernardino, Rialto, Fontana, Redlands, Loma Linda, Grand Terrace, Highland) | 24/7 **solo si** alguien contesta de noche (PENDIENTE). Si no, 6am–10pm |
| Marca (condicional) | Defender la marca | $5 | ~10% | Max clics con tope de CPC $3 | Igual | Igual |

**Por qué una sola campaña:** la regla de aprendizaje pide ≥3× CPL/día por campaña ($300/día). Con $49 no alcanza ni para una, así que se consolida y se divide por ad groups, como hacen las hermanas que funcionan.

## Estructura por campaña
### Campaña: Colton Sunflower — Search
| Ad group | Keywords (match) | Vol. est. | Landing | H1 pinneado |
|---|---|---|---|---|
| **Cremation - Direct & Affordable** (renombrar el actual "Cremation Services") | [cremation near me], [cremation services near me], [direct cremation near me], [cremation san bernardino], "cremation services", "direct cremation", "crematorium near me", "simple cremation", "affordable/cheap/low cost cremation near me", "cremation services san bernardino", "cremation fontana", "cremation redlands", "colton cremation" | Alto (nacional 18k+); local bajo | /cremation/ | Cremation Services Near You |
| **Cremation - Cost & Prices** (nuevo) | "cremation cost", "cremation cost near me", "cremation prices near me", "how much does cremation cost", "how much is cremation" | Alto | **/pricing/** (existe, con 7 paquetes; falta formulario) | Cremation Cost in Your Area |
| **Cremation With Service** (nuevo) | "cremation with memorial service", "cremation with viewing", "funeral and cremation services", "service and cremation" | Medio | /cremation/ | Cremation With Memorial |
| **Funeral Home** (actual) | [funeral home near me], [funeral homes near me], "mortuary near me", "funeral homes in colton ca", "funeral homes in san bernardino ca", "funeral home san bernardino", "mortuary san bernardino", "funeral homes in fontana ca", "funeral homes in rialto ca", "funeral homes in redlands ca", "affordable funeral homes near me", "funeral packages", "funeral home prices" | Alto | / | Funeral Home in Colton, CA |
| **Burial Services** (actual) | [burial services near me], "direct burial", "direct burial near me", "burial services", "affordable burial" | Medio | **/burial/** | Burial Services Near You |

Detalle con volumen y CPC en `data/keywords.csv`.

**Migración de keywords (sobre la campaña actual):**
- Todas las amplias pasan a frase. Las 3–5 principales de cada grupo se agregan además en exacta.
- Las amplias que gastaron sin convertir se pausan después de crear su versión en frase (no se borran): "cremation with service", "cremation burial near me" (×2, duplicada), "funeral cremation near me", "cremation cost near me", "funeral arrangements", "mortuary near me".
- Se pausan las ~55 keywords con 0 impresiones en 30d.

**Negativas entre grupos** (frase, a nivel ad group, para no canibalizarse):
- Cremation - Direct: -cost, -price, -prices, -"how much", -viewing, -memorial.
- Cremation With Service: -cost, -price, -direct.
- Funeral Home: -cremation (va a los grupos de cremación), -burial.
- Burial Services: -cremation.

### Campaña: Marca (condicional)
| Ad group | Keywords | Vol. | Landing | H1 |
|---|---|---|---|---|
| Brand | [sunflower crematory], [colton funeral home] (*si es la marca*), [colton funeral chapel] (*si es la marca*) | ~400/mes | / | Sunflower Burial & Cremation |

No pujar por [sunflower cremation] si corresponde a Sunflower Riverside (cliente PMM).

## Keywords descartadas y por qué
| Término | Motivo |
|---|---|
| cremation, funeral home, mortuary (sueltas) | Genéricas, mucha intención informacional; solo con modificador local o "near me" |
| obituaries, recent deaths, funerals today | Informacional/evento (ya negativas) |
| caskets, headstones, urns, plots, costco | Producto (ya negativas) |
| pet/dog/cat cremation | Otro servicio (ya negativas). Revisar si el cliente lo ofrece |
| average cost, in california, assistance, benefits | Investigación o ayudas (ya negativas) |
| inland memorial | Cliente PMM hermano |
| montecito, cortner, emerson, family funeral chapel, meadow, presidio… | Competidores (ya negativas) |
| funeraria cerca de mi (320) | Condicional: solo si atienden en español |

## Copy
Completo en `data/ads-search.md`: 5 grupos × 15 headlines + 4 descripciones, con límites de caracteres validados, más extensiones. **Actualización 2026-10-01:** el sitio confirma family-owned, 24/7, crematorio propio, licencia FD2479, no hidden fees y los precios ($1,175 cremación, $1,995 entierro). Esos claims ya no llevan `[C]`. Nuevo ad group candidato para F2: **Veteran Cremation** ($1,350 / $2,800).

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| coltonfuneral.com/ | Sí (URL final actual) | Cliente/PMM | No, pero falta auditar (proxy) |
| coltonfuneral.com/cremation/ | Sí (URL final actual, 3 conv.) | Cliente/PMM | No, pero falta auditar |
| /pricing/ | **Sí** (Simple Cremation $1,175, Direct Burial $1,995, veteranos) | PMM/Cliente | Falta formulario |
| /burial/ | **Sí** | PMM/Cliente | No (formulario al pie) |
| Página de gracias + Form Fill | **No** (Elementor inline; /thank-you/ 404) | PMM | **Sí**: sin esto no se pasa a Max conversiones |
| Formulario arriba en / , /cremation/, /pricing/ | No | PMM/Cliente | **Sí** (ver audit-site.md) |

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |
|---|---|---|---|
| F0 Rescate (oct 1–15) | $1,490 | Search 100% | Form Fill medido y probado; negativas "how", "Fontana" y "online" corregidas; estructura de 5 grupos con frase/exacta; 3 RSA por grupo |
| F1 Max conversiones (aprendizaje, ~4–6 sem.) | $1,490 | Search 90% / Marca 10% (si aplica) | 30d con ≥10 conv. y CPA ≤ $150 |
| F2 Optimización | $1,490 → $2,500 si se confirma neto | Más peso a los grupos de cremación según CPA | CPA 30d ≤ $100 durante 2 revisiones seguidas → subir presupuesto |
| F3 tCPA / PMax | ≥ $2,500 | — | ≥30 conv/30d con tracking confiable (con $1,490 exige CPA ≤ $50; poco probable) |

## Por qué NO (todavía)
- **PMax**: 4 conversiones en 30d contra las 30+/mes que pide `pmax-cuando-y-como.md`. Además no hay assets propios verificados. Riverside y Swan sí tienen PMax, pero con 17–50 conv/mes.
- **Amplia**: es lo que tiene hoy y es la causa del desperdicio, combinada con Max clics. Se vuelve a probar solo con Max conv maduro y aprobación de Jhombis. Riverside usa "cremation cost" en amplia con buen CPA, así que puede ser una prueba en F2.
- **Display / Demand Gen**: no para servicio local de alta intención. Inland Memorial tiene Display con 0 conv.
- **LSA**: en las categorías de LSA que conocemos no aparecen funerarias; verificar en la UI antes de descartarlo.
- **Remarketing/RLSA**: una funeraria es una compra urgente y única; poco valor. Se reevalúa en F2 con audiencias de observación.
- **Campaña en español**: PENDIENTE de saber si atienden en español. La demanda existe (~320/mes "funeraria cerca de mi" y varias búsquedas de precio en ES en los search terms).

## Riesgos y supuestos
1. **Canibalización con Inland Memorial / Sunflower Riverside.** Si son el mismo grupo, sus campañas pueden competir en la misma subasta en Colton y Riverside. Definir los radios para que no se solapen.
2. **Cambios de terceros**: en septiembre hay keywords removidas que no tocamos. Hay que acordar quién edita la cuenta.
3. **CPL objetivo prestado del MCC**: sin ticket ni margen del cliente puede estar mal; ajustar tras /onboard.
4. **Volumen local bajo** (los términos con ciudad tienen de 20 a 200 búsquedas/mes). El grueso viene de "near me" con geo, así que el radio decide el volumen.
5. **Claims sin confirmar** en el copy (`[C]`).
