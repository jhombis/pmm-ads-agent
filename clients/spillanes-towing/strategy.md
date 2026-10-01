---
cliente: Spillane's Towing & Recovery
slug: spillanes-towing
actualizado: 2026-10-01
version: 1
supuestos:
  - Ticket y margen PENDIENTES. CPL objetivo tomado del benchmark, no de la economía del cliente
  - Volúmenes de Keyword Planner a nivel Vermont (geo 21162). Radio de 12 mi ≈ 25% del estado (proporción de población)
  - Quién contesta de noche PENDIENTE. El horario 24/7 queda condicionado
  - Servicios a evitar PENDIENTES. Lockout, llantas y jump start excluidos en F1 por bajo ticket; long distance neutral
  - Configuración actual de geo (presencia/interés), programación y duración mínima de llamada NO verificada (Windsor no la expone)
  - Velocidad de la landing sin medir (PageSpeed 429)
---

# Estrategia Google Ads — Spillane's Towing & Recovery

## Resumen ejecutivo
- **Reestructurar la campaña Search existente, no crear una nueva**: se conserva su historial de conversiones y el nombre de la plantilla PMM. Pasa de 7 keywords en concordancia amplia a **6 ad groups temáticos** en frase/exacta, y elimina "roadside assistance" (72% del gasto, CPL $67).
- **1 sola campaña**: $989/mes ($32.50/día) no alcanza para 3× CPL/día ni en una campaña. Separar por servicio diluiría el aprendizaje.
- **Sin marca, sin PMax, sin LSA** (towing no califica). La marca entra como negativa: ya es #1 orgánico y su búsqueda es mayormente impound.
- **CPL objetivo**: $35 en F1, $25 en F2–F3 (la mediana madura del MCC es $16; ajustado por mercado chico, 3.2★ y solo Search). Hay que contrastarlo con el CPL máximo del brief cuando llegue el ticket real.
- **tCPA**: cuando haya ≥30 conv. en 30 días. Estimado: **semana 8–12** después de la reestructuración, si el CPC baja de $11.90 a ~$6.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| Spillane's Towing and Recovery - ENHPRM Radius - $1799/mo. (existente, reestructurada) | Llamadas (≥60 s) + formulario | **$32.50** | 100% | Maximizar conversiones, sin tCPA (se mantiene) | Radio de 12 mi alrededor de 44.490450, -73.111263, **solo presencia**; excluir el resto de países | 24/7 **solo si** el cliente confirma que alguien contesta de 11pm a 7am; si no, 6:00–23:00 todos los días |

Configuración obligatoria (estándares PMM 7–8 y 10):
- Red: solo búsqueda. Socios de búsqueda y Display **apagados**.
- Aplicación automática de recomendaciones **apagada**.
- Rotación: optimizar.
- Conversiones primarias: "Calls from Ads" y "Website Calls" con **duración mínima de 60 s**, más "Form Fill" (page-view de `/thank-you/` cuando exista).
- Verificar la duración mínima actual: con 60 s probablemente baja el número de conversiones reportadas, pero sube su calidad.
- Dispositivos: sin ajustes (99% móvil).

## Estructura por campaña
### Campaña: Spillane's Towing and Recovery (Search, no-marca)
Volumen = búsquedas/mes estimadas dentro del radio (KP Vermont × 25%).

| Ad group | Keywords (match) | Vol. est. | Landing | H1 pinneado |
|---|---|---|---|---|
| AG1 Towing Near Me | [towing near me], [towing company near me], "towing near me", "towing company near me", "towing company", "towing service", "tow service near me", "car towing", "local towing" | ~990 | `/towing/` (hoy `/`) | Towing Near You - 24/7 · Towing Company Near You · Local Towing Service |
| AG2 24/7 Emergency Towing | "24 hour towing", "24/7 towing", "emergency towing", "towing open now", "after hours towing" | ~15 (bajo; se mantiene por intención y CPC distintos; fusionar con AG1 al día 30 si <50 impr.) | `/towing/` | 24/7 Emergency Towing · Emergency Tow Truck 24/7 · Need A Tow Right Now? |
| AG3 Tow Truck | [tow truck near me], "tow truck near me", "tow truck service", "tow truck company", "wrecker service", "flatbed tow truck near me" no (→AG6) | ~620 | `/towing/` | Tow Truck Near You · Local Tow Truck Company · Tow Truck Service 24/7 |
| AG4 Towing Burlington VT | [towing burlington vt], "towing burlington", "tow truck burlington", "towing south burlington", "towing essex", "towing colchester", "towing williston", "towing winooski", "towing shelburne" | ~200 | `/towing/` | Towing In Burlington, VT · Burlington VT Tow Truck · South Burlington Towing |
| AG5 Accident & Recovery | "accident towing", "car accident tow", "winch out", "winch out service", "car stuck in snow", "car stuck in ditch", "vehicle recovery", "car recovery service" | <15 hoy; **estacional nov–mar** | `/accident-recovery/` | Accident & Recovery Towing · Winch-Out & Recovery 24/7 · Stuck In Snow? We Pull You Out |
| AG6 Flatbed Towing | [flatbed towing near me], "flatbed towing", "flatbed tow truck", "awd towing", "flatbed tow near me" | ~30 | `/flatbed-towing/` | Flatbed Towing Near You · Flatbed Tow Truck 24/7 · Safe Flatbed Towing For AWD |

Por qué así: AG1 y AG3 concentran ~90% del volumen y son exactamente lo que convierte en el MCC ("towing near me", CPL $13.9 en 9 cuentas). AG5 y AG6 tienen poco volumen pero son el ticket más alto y el diferenciador (16 flatbeds). Valen un grupo propio para que el copy y la landing coincidan. Ningún servicio×ciudad llega a 100 búsquedas/mes, por eso las ciudades van todas en AG4.

**Keywords actuales a pausar**: las 7 en BROAD (`roadside assistance`, `roadside assistance near me`, `tow truck near me`, `towing service`, `towing company near me`, `tow company`, `spillane's towing`). Se pausan, no se eliminan, para conservar el historial.

Negativas específicas de grupo:
- AG1, AG3, AG4: `accident`, `winch`, `stuck`, `flatbed` (negativas cruzadas para que cada búsqueda caiga en su grupo).
- AG3: `toy`, `for sale`, `driver`, `games`, `lego` (ya en la lista, reforzar).
- AG5: `rehab`, `data`, `addiction` (ambigüedad de "recovery").
- AG6: `for sale`, `rental`, `trailer`.

Cuenta: lista "PMM Universal" + bloque Towing + `data/negatives-nicho.txt` (marca propia, competidores, AAA/aseguradoras, precio, heavy-duty, bajo ticket, impound, fuera de área).

## Keywords descartadas y por qué
| Término | Vol. VT | Motivo |
|---|---|---|
| roadside assistance / road assist / emergency roadside | 880 c/u | Mezcla con AAA y aseguradoras. CPL de $67 en esta cuenta y de $154 en el resto del MCC. **Prueba controlada en F3** solo con "road service near me" |
| aaa roadside / aaa emergency road service | 1,000 | Membresía de competidor. Negativa |
| state farm / geico / progressive / allstate roadside | 50–170 | Aseguradoras. Negativa |
| cheap / $50 / inexpensive towing | 50–170 | Ancla de precio de STUCK ($50). El cliente no compite en precio |
| truck / semi / tractor trailer / heavy duty towing | 30–720 | Heavy-duty sin confirmar (1 wrecker). Negativa en F1 |
| lockout, jump start, tire, fuel | 20–140 | Bajo ticket. Excluido en F1 (pendiente de decisión del cliente) |
| tow yard / towed / impound | 20–30 | Gente que recupera su auto, no clientes |
| marca propia | ~170 (US) | #1 orgánico. Tráfico de impound |
| handys / greniers / sheehan's / pagan / tailhook | 170–590 | Competidores |
| long distance towing | s/d | **Neutral**: ni se puja ni se excluye hasta que el cliente decida (está en su sitio principal) |

Detalle: `data/keywords.csv`.

## Copy
Completo en `data/ads-search.md`: 3 RSA por ad group, 15 headlines (1 pinneada + 14) y 4 descripciones, con límites verificados.
- **Ángulos** (de `competitors.md`): flota de 21 camiones / 16 flatbeds, "Local Crew, Not A Call Center" (contra los agregadores 855/888), base en South Burlington y Chittenden County, y estacionalidad de invierno en AG5.
- **Sin promesas de precio ni de tiempo** de llegada hasta que el cliente las confirme.
- **Extensiones**: 4 sitelinks, 8 callouts, snippet de servicios, llamada, ubicación (requiere acceso al GBP) e imágenes de flota propia.

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| `/` arreglada: H1 con servicio y zona, form de 3 campos arriba, quitar el link al GBP | Sí (con fallas) | PMM | **Sí** (auditoría: bloqueantes 1–2) |
| `/thank-you/` | No | PMM | **Sí** (medición de formulario) |
| `/towing/` (AG1–AG4) | No | PMM | No: AG1–AG4 apuntan a `/` arreglada mientras tanto |
| `/accident-recovery/` (AG5) | No | PMM | No, pero AG5 rinde peor sin ella. Prioridad antes de noviembre (nieve) |
| `/flatbed-towing/` (AG6) | No | PMM | No |

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |
|---|---|---|---|
| **F0 – Corrección inmediata** (semana 0) | $989 | Campaña actual | Negativas aplicadas · roadside y marca fuera · llamadas ≥60 s configuradas · geo verificada en "presencia" · H1 + form + thank-you en la landing · Tag Assistant OK |
| **F1 – Nueva estructura** (semanas 1–4) | $989 ($32.50/día) | 100% Search no-marca, 6 ad groups | ≥20 conv./mes · CPL ≤ $40 · revisión de search terms en días 7, 14 y 30 completada |
| **F2 – Estabilización + tCPA** (semanas 5–12) | $989 | Ídem; `/towing/`, `/accident-recovery/` y `/flatbed-towing/` publicadas | ≥30 conv. en 30 días → activar tCPA = CPA real de 30 días +10%. Objetivo CPL ≤ $25 |
| **F3 – Expansión controlada** (mes 4+) | $989–1,300 | 85% genérica · 15% ad group de prueba "road service near me" (frase) | Subir presupuesto solo si se pierde >20% de cuota por presupuesto con CPL ≤ objetivo y el cliente confirma capacidad. Lockout y long distance según decisión del cliente |
| **F4 – Remarketing** (mes 5+) | +$50–100 | RLSA en observación sobre la genérica; luego ajuste de puja | Lista de visitantes ≥1,000 usuarios (en Search) |
| **F5 – PMax** (condicionado) | 20–30% del Search | Asset group Towing | Ver "Por qué NO" |

## Por qué NO (todavía)
- **PMax**: no se cumple ninguna de las condiciones de `pmax-cuando-y-como.md`. Hay 14 conv./mes (pide ≥30), no hay tCPA estable, la llamada ≥60 s no está verificada, no hay assets propios (fotos de flota) y la landing no tiene thank-you ni anti-spam. Además, PMax empuja tráfico a Maps, donde 3.2★ convierte mal. **Condición adicional para esta cuenta: ≥3.8★ en el GBP.** Los PMax del MCC reportan CPL bajos inflados por acciones de Maps.
- **Amplia**: todo el MCC towing está en broad, y aquí la amplia sobre "roadside assistance" quemó el 72% del presupuesto. Volver a la amplia requiere tCPA maduro, tracking ≥60 s confiable y aprobación de Jhombis (estándar 2).
- **Display / Video / Demand Gen**: servicio de urgencia. Nadie compra una grúa desde un banner.
- **Marca**: #1 orgánico, sin competidores pujando por ella y búsqueda dominada por impound. Revisar en Auction Insights al día 30: si alguien puja por "spillane's", se crea una campaña de marca con $3/día y negativas de impound.
- **LSA**: towing no es categoría de Local Services Ads.
- **Campaña por servicio**: $32.50/día no sostiene 3× CPL/día en ninguna división.

## Riesgos y supuestos
1. **Economía sin validar**: si el ticket promedio es ~$200, el CPL máximo es ~$21 y un objetivo de $25–35 no es rentable. **Ticket y margen son el primer bloqueante** antes de fijar el tCPA.
2. **La reputación (3.2★) limita la tasa de conversión** frente a pares de 4.5★. El plan de reseñas va en el roadmap como pista paralela; Ads no lo resuelve.
3. **Mercado chico**: ~2,000 búsquedas/mes de towing en el radio. Con 40% de cuota actual hay poco margen para crecer en volumen: la mejora tiene que venir del CPC y de la tasa de conversión.
4. **El horario 24/7 no está confirmado** (el sitio principal dice 7am–11pm). Pagar por clics de las 2am sin nadie que conteste es puro desperdicio.
5. **Volúmenes estimados** con KP a nivel estado × 25%: validar con las impresiones reales en el día 14.
6. **Las conversiones de llamada pueden caer** al exigir ≥60 s. Es esperado, y el CPL "real" será más alto que el reportado hoy.
7. **El ad group de emergencia y AG5 tienen volumen mínimo**: fusionarlos al día 30 si tienen <50 impresiones.
