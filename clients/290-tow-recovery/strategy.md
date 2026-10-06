---
cliente: 290 Tow and Recovery
slug: 290-tow-recovery
actualizado: 2026-10-06
version: 3
supuestos:
  - Ticket y margen PENDIENTE. El CPL objetivo sale del benchmark consolidado (knowledge/benchmarks/towing-us.md), no de la economía del cliente.
  - Las 6 conversiones del período (09-17 → 10-05) no están verificadas. 3 vienen de búsquedas de competidores o "junk cars". El CPL real es desconocido hasta revisar Detalles de llamadas con el cliente.
  - Volumen local sin Keyword Planner (no hay credenciales de API). Se usan Semrush US y los search terms reales (531 impresiones, 53 clics).
  - Fair Oaks Ranch, Bulverde y Spring Branch sin confirmar como área de servicio.
  - Flatbed confirmado por la web ("rollback and wrecker trucks", /about-us/). RV, moto y medium duty sin confirmar.
  - Licencia TDLR y seguro sin confirmar; no se usan en el copy.
  - Sin GBP: no hay activo de ubicación ni LSA.
---

# Estrategia Google Ads — 290 Tow and Recovery

> **v3 (2026-10-06)**: reanálisis con 18 días de datos (`log/2026-10-06-diagnose.md`), la auditoría v3 del sitio y los estándares nuevos del repo (playbook de analítica, benchmark `towing-us.md`).
>
> Qué cambia frente a la v2:
> - **CPL objetivo realista para una cuenta nueva.** La meta de $14.57 era de cuentas maduras.
> - **1 RSA por ad group.**
> - **Se reutiliza el AG2 que ya existe en la cuenta.**
> - **Exotic deja de estar bloqueado.**
> - **"cheap" sale de las negativas.**
> - **Se suman 63 negativas nuevas.**
> - **Proyección de llamadas corregida a 14–24/mes.** Antes era 35–55.

## Resumen ejecutivo
- **Situación.** La reestructura de la v2 **no se aplicó**. La cuenta sigue con la plantilla PLL: amplia, Maximizar clics sin tope visible y sin negativas. En 18 días gastó **$530.14**, con 53 clics a un CPC de **$10.00**, 6 conversiones y CPL de **$88.36**. El **45.8% de lo rastreable** ($126.66 de $276.32) es desperdicio claro.
- **Estructura (sin cambios de fondo).** 1 campaña Search consolidada con **3 ad groups**: Towing, Exotic & Long-Distance y Roadside. Está dentro del límite de fragmentación del playbook ($600–1,500 → 1 campaña, 3–5 grupos).
- **Orden de ejecución** (playbook):
  1. Medición: Detalles de llamadas, umbral de 60 s, Form Fill como secundaria hasta tener `/thank-you/`.
  2. Negativas.
  3. Estructura: frase + exacta, sin amplia.
  4. Puja: Maximizar clics con tope de **$6.50**.
  5. Creatividad: 1 RSA por grupo.
- **CPL objetivo** (`towing-us.md`):
  - meses 1–2: **$30–60** (cohorte nueva, mediana $51–63)
  - meses 3–6: **$21–38**
  - meta a 6 meses: **$15–16**
- **Proyección.** $27/día ÷ $6.50 ≈ 4.2 clics/día (~126/mes). Con CVR de 11–19% salen **~14–24 llamadas/mes** en el mes 2, a un CPL de ~$34–59. Hay que decírselo al cliente: las 35–55 de la v1 eran números de cuentas maduras.
- **Maximizar conversiones** con ≥15 conversiones **verificadas**/mes; **tCPA** con ~30 en 30 días, fijado desde el CPA observado. Con $825/mes eso exige un CPL ≤ $27.50: realista hacia el mes 4 (~ene-2027), no antes.

## Matemática de presupuesto (playbook §4)
| Escenario | CPC | Clics/mes | Tasa conv. | Llamadas/mes | CPL | Referencia |
|---|---|---|---|---|---|---|
| Hoy (sin cambios) | $10.00 | ~82 | 11.3% (53 clics) | ~9 | ~$88 | Lo observado del 09-17 al 10-05 |
| Conservador | $6.50 | ~126 | 8% | ~10 | ~$82 | CVR bajo la cohorte nueva |
| **Base** | **$6.50** | **~126** | **11–19%** | **~14–24** | **~$34–59** | Cohorte nueva del MCC (meses 1–2) |
| Optimista | $5.00 | ~165 | 27% | ~44 | ~$19 | Mediana de cuentas maduras (mes 4+) |

Si el tope de $6.50 recorta el volumen porque "towing near me" hoy cuesta $9.67, la campaña puede no gastar los $27/día. En ese caso, primero se abren keywords de ciudad (CPL ≈ $8 en el MCC) y AG3 a frase. **No se sube el tope sin revisar antes los search terms.**

## Campañas
| Campaña | Objetivo | Presupuesto/día | Puja | Geo | Horario |
|---|---|---|---|---|---|
| Se conserva la existente: "290 Tow and Recovery - ENHPRM Radius - $1500/mo. - 09/17/2026" (nombre PLL) | Llamadas: Calls from Ads + Website Calls como primarias. Form Fill **secundaria** hasta que exista `/thank-you/` | $27 (tope mensual $820.80) | Maximizar clics, tope CPC **$6.50** → Maximizar conversiones con ≥15 conv verificadas/mes → tCPA con ~30/30 días | **Presencia**, radio de 40 mi recentrado en Fredericksburg (30.2752, -98.8720). Excluir Fair Oaks Ranch, Bulverde y Spring Branch **solo si el cliente confirma** que no los atiende ($120.84 = 22.9% del gasto; 1 conversión, de un competidor) | 24/7 (el cliente contesta 24/7; zona horaria de la cuenta pendiente de verificar en la UI) |

**Configuración obligatoria**: solo red de Búsqueda (ya está así), rotación "optimizar", recomendaciones automáticas **apagadas**, idioma inglés, audiencias en observación.

## Estructura
| Ad group | Keywords (frase "" · exacta []) | Datos reales 09-17 → 10-06 | Landing | H1 pinneado | % gasto esperado |
|---|---|---|---|---|---|
| **AG1 Towing** (existe como "Ad group 1 - Towing General": se conserva y se cambian keywords y RSA) | [tow truck near me], [towing near me], [towing company near me], [wrecker service near me], "tow truck near me", "towing near me", "towing company near me", "towing service near me", "tow service near me", "tow truck company near me", "tow truck company", "car towing near me", "tow trucks near me", "tow truck service", "wrecker service near me", "wreckers near me", "24 hour towing", "emergency towing", "cheap tow truck near me", "towing fredericksburg", "tow truck fredericksburg", "towing kerrville", "kerrville towing", "tow truck kerrville", "towing johnson city", "tow truck llano", "towing comfort", "towing blanco", "towing harper" (ciudades sin sufijo de estado, regla de /strategy; las negativas de Virginia y Tennessee cubren las colisiones) | towing near me $299.70, 31 clics, 4 conv · wreckers near me $21.44 · tow truck near me $17.84 · towing fredericksburg tx $9.84 | `/` (con H1 de texto) | `{KeyWord:24/7 Towing Near You}` | ~85% |
| **AG2 Exotic & Long-Distance** (existe en la cuenta como "Ad group 2 - Exotic Car & Long Distance towing": 0 impresiones, RSA PLL; se rellena) | [exotic car towing], "exotic car towing", "luxury car towing", "classic car towing", "flatbed towing near me", "flatbed tow truck near me", "rollback tow truck service", "long distance towing near me", "long distance car towing", "long distance towing fredericksburg", "long distance towing texas", "tow car to san antonio", "tow car to austin" | Sin datos (0 impr.) | URL final por keyword: exotic y flatbed → `/exotic-vehicle-towing/` (**CTA verificados el 10-06**); long-distance → `/local-long-distance-towing/` | Exotic & Long-Distance Towing | ~5–10% |
| **AG3 Roadside** (nuevo; sale de AG1) | [roadside assistance near me], [roadside service near me], [jump start near me], [flat tire change near me] | "roadside assistance" amplia: **$140.05 (26% del gasto)**, 15 clics, 2 conv, y trajo casi todo el desperdicio. "roadside service near me" exacta: $11.74, 1 clic | `/roadside-assistance/` | Roadside Assistance Near You | ≤10% |

**Se eliminan**:
- todas las keywords en amplia de la plantilla, sobre todo **"roadside assistance"**
- "towing car", "tow a car" y "tow company" en amplia

**Reglas de control**:
- AG3 > 20% del gasto semanal → pausar.
- AG2 > $100 sin llamadas en 30 días → pausar.
- Si la campaña gasta < 70% del presupuesto en el D7 → abrir AG3 a frase o sumar keywords de ciudad. **Nunca volver a la amplia** (exige ~50 conversiones limpias, tCPA maduro y OK de Jhombis).
- Volver a separar un grupo solo si AG1 supera ~300 clics/mes.

**Negativas por grupo**:
- AG1: roadside, jump, tire, exotic, long distance.
- AG2: shipping, transport, carrier, enclosed.
- AG3: towing, tow truck, wrecker.

## Negativas
- **Universal PMM** (`knowledge/negativas-universales.md`).
- **Nicho + cliente** (`data/negatives-nicho.txt`, v2 del 10-06, **sin "cheap"**). En el MCC convierte igual que el genérico (CVR 34.5%, CPL $16.59), y aquí "cheap tow truck near me" trajo 1 conversión.
- **63 nuevas** de los search terms (`data/2026-10-06-negatives.txt`):
  - aseguradoras y planes (toyotacare, mopar, hagerty…)
  - "phone number"
  - batería como producto
  - junk / we buy
  - talleres
  - competidores nuevos (comal, mission, barbee, rst, five star towing…)
  - ciudades fuera del área
- **No se niegan**:
  - "jump start" ni "flat tire": el cliente declara roadside
  - español: hubo 1 conversión con "roservi cerca de mi"; se prueba en F3
  - RV y lockout hasta que el cliente confirme
- Todo se aplica con `/negatives` y OK de Jhombis.

## Copy
Completo en `data/ads-search-towing.md` (v3): **1 RSA por ad group** (estándar PMM para cuentas con <$1,500/mes: con ~4 clics/día un A/B es ruido, playbook §9), con 15 headlines y 4 descripciones.
- **Reemplaza** el RSA actual de AG1. Hoy su anuncio lleva "Battery Jumpstarts", "Tire Change" y "Emergency Roadside" como titulares en el grupo de towing, y eso empuja tráfico de roadside.
- **Ángulos**: 24/7 real, precio claro antes de enganchar (si el cliente lo confirma), Navy Veteran Owned, 10% Senior Discount, número 830 local frente a las redes 877.
- **Assets**: 4 sitelinks, 8 callouts, snippet de servicios, llamada. Ubicación cuando exista el GBP. Imágenes cuando haya fotos propias.
- **No se promete**: "licensed & insured", número TDLR, ETA en minutos.

## Landings requeridas
| URL | Estado | Ad groups | Responsable | Bloqueante |
|---|---|---|---|---|
| `/thank-you/` + redirect del formulario (quitar popup "Your Booking Is Not Yet Confirmed") | No existe (404) | Form Fill | PMM | **Sí** |
| `/` | H1 de texto (hoy no hay `<h1>`; el hero es imagen) y velocidad (móvil 43, LCP 6.7 s) | AG1 | PMM | No (bloquea si el score baja de 40) |
| `/exotic-vehicle-towing/` | Lista: CTA verificados en el HTML el 10-06 | AG2 | — | No |
| `/local-long-distance-towing/` | Lista | AG2 | — | No |
| `/roadside-assistance/` | Lista | AG3 | — | No |

## Presupuesto por fase
| Fase | Total/mes | Qué pasa | Condición para pasar |
|---|---|---|---|
| **F0 — Medición + negativas** (10-06 → 10-08) | $825 (sigue corriendo) | Revisar las 8 llamadas en Detalles de llamadas con el cliente · umbral 60 s · Form Fill secundaria · aplicar negativas | Medición verificada con Tag Assistant + negativas aplicadas |
| **F1 — Reestructura** (10-09 → 10-16) | $825 | 3 grupos en frase/exacta · tope CPC $6.50 · 1 RSA por grupo · geo según el cliente | 7 días activa, anuncios aprobados, ≥1 conversión verificada con el cliente |
| **F2 — Limpieza** (D7 10-16 · D14 10-23 · D30 11-08) | $825 | Search terms → negativas · reglas de control | 3 revisiones hechas, desperdicio < 15% de lo rastreable |
| **F3 — Maximizar conversiones → tCPA** (~11-09 → ~ene-2027) | $825 (escalar solo si sube el fee) | Max conv con ≥15 conv verificadas/mes · tCPA con ~30/30 días · prueba de grupo en español | CPL estable ±20% durante 4 semanas |
| **Pista GBP + LSA** | LSA pay-per-lead, aparte o de los $825 (decide el cliente) | GBP → activo de ubicación → LSA | GBP verificado + licencia TDLR + seguro + background check |
| **F4 — RLSA** | Dentro de los $825 | Audiencia de visitantes en observación | ≥1,000 usuarios/30 días (no se alcanza con ~126 clics/mes) |
| **F5 — PMax** | Condicionado | — | 6–12 meses de Search estable (benchmark), 30+ conv/mes y assets propios |

## Por qué NO (todavía)
- **PMax**: en el MCC funciona solo después de 6–12 meses de Search estable. Las 2 cuentas que lo lanzaron antes de los 3 meses fracasaron. Aquí faltan conversiones verificadas, fotos propias, GBP y presupuesto (~$44/día solo para PMax).
- **Amplia**: en 18 días, 45.8% de desperdicio rastreable, y "roadside assistance" en amplia se llevó el 26% del gasto. El estándar exige ~50 conversiones limpias y tCPA maduro.
- **Display / Demand Gen / Video**: no para towing local.
- **Campaña de marca**: no hay búsquedas de "290 tow" en los search terms.
- **Remarketing**: la audiencia no llega a 1,000 visitantes.
- **Grupo en español** (todavía no): hubo 1 conversión con "roservi cerca de mi" ($9.19). En el MCC, los grupos en español funcionan en TX. Se prueba en F3 con frase ("grua cerca de mi", "servicio de grua") si el cliente atiende en español.

## Riesgos y supuestos
- **Conversiones sin verificar**: 3 de 6 vienen de competidores o junk, y hubo 8 llamadas para 4 conversiones de Calls from Ads. Sin revisar Detalles de llamadas, el CPL de $88.36 no es interpretable.
- **Volumen con tope**: si $6.50 no alcanza la subasta, la campaña gasta menos. Mitigación: keywords de ciudad y AG3 a frase, nunca amplia.
- **Economía**: si el ticket real es bajo (~$175), un CPL de $30–60 en los meses 1–2 no es rentable. Confirmar ticket y margen.
- **Sin GBP ni reseñas**: el Map Pack (Douglas 157★, Tic Tac 70★, Integrity 89★) capta la llamada antes que el anuncio.
- **Respuesta a leads**: sin confirmar quién contesta de noche.
- **Historial de cambios**: alguien renombró AG1 y quitó 2 keywords sin documentarlo. Toda escritura futura va con fecha en `log/`.
