---
cliente: Jerry's Auto Body Solutions & Towing Service
slug: jerrys-towing-wesley-chapel
actualizado: 2026-10-01
version: 1.1
supuestos:
  - Ticket promedio, margen y tasa de cierre desconocidos → CPL objetivo tomado del benchmark (Fishhawk + MCC), no de la economía del cliente
  - Radio real de servicio desconocido → se propone 20 mi desde 3645 New River Rd
  - No se sabe si contestan en español → el ad group ES queda condicional
  - No se sabe si atienden de noche con alguien que conteste → se propone 24/7 condicionado
  - Medium-duty y carrocería no confirmados → fuera de la Fase 1
  - GBP no encontrado → sin activo de ubicación hasta confirmarlo
  - Keyword Planner no disponible (sin google-ads.yaml) → volúmenes nacionales de Semrush + datos reales de la cuenta
---

# Estrategia Google Ads — Jerry's Auto Body Solutions & Towing Service

> La cuenta ya está activa desde el 22/08/2026 (plantilla ENHPRM). Esta estrategia **reestructura dentro de la campaña existente**: no se crea una campaña nueva, para no perder el historial de 21 conversiones ni reiniciar el aprendizaje desde cero.

## Resumen ejecutivo
- **1 campaña Search** (la actual, renombrada) con **4 ad groups activos + 1 condicional** (Grúa ES). Sin marca, sin PMax, sin Display.
- **Presupuesto: $25/día (~$760/mes)**, que es el del paquete de $1,500. No alcanza para más de una campaña (regla de 3× CPL/día = $115/día por campaña).
- **CPL objetivo: $30–40** en la Fase 1 (actual: $38.50 en 28 días; Fishhawk Search: ~$31). Meta de la Fase 2: **≤ $30**.
- Puja: **Maximizar conversiones** sin tCPA, **condicionado a la medición** (CLAUDE.md #6): si al verificar las conversiones quedan <15 conv./mes reales (p. ej. si "Website Calls" es un clic en `tel:`), se pasa a **Maximizar clics con tope de CPC de $10** hasta volver a 15+. **tCPA no es alcanzable** con este presupuesto (~20 conv./mes a $38). Para 30 conv./mes con CPL de $30 hace falta **~$30/día en medios**.
- RSA: **1 por ad group (máx. 2)** (CLAUDE.md #4: <$1,500/mes de pauta; con ~90 clics/mes un A/B es ruido).
- Match: **frase por defecto + exacta en los 3–4 términos top**. Se migran las 13 keywords en broad.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| Towing - Search - Radius (renombrar la actual "…ENHPRM Radius…") | Llamadas ≥60 s + formularios | $25 | 100% | Maximizar conversiones (se mantiene) | **Presencia**, radio de 20 mi desde 3645 New River Rd; excluir el resto de países | 24/7 **si** alguien contesta de noche; si no, 6:00–23:00 |
| LSA (pista paralela) | Leads verificados | presupuesto propio LSA | — | por lead | Pasco + N. Hillsborough | 24/7 |

**Por qué 24/7 condicionado:** entre 0 y 5 h se gastó el 19% ($192) con un CPL de $48, contra ~$27 entre 17 y 23 h y ~$61 entre 7 y 16 h. La muestra es chica (21 conv.), así que por ahora no se recortan horas. Las 5 h ($102, 16 clics, 1 conv.) son una anomalía: vigilar clics inválidos.
**Dispositivos:** el 93% del gasto es móvil. No se ajusta nada (Maximizar conversiones ignora los ajustes de puja salvo -100%).
**Red:** solo búsqueda (confirmado). Sin socios de búsqueda ni Display.

## Estructura por campaña
### Campaña: Towing - Search - Radius

| Ad group | Keywords (match) | Vol. US* | Landing | H1 pinneado (RSA A / B / C) |
|---|---|---|---|---|
| **Towing Near Me** | "towing near me", "tow truck near me", "towing company near me", "tow company near me", "tow service near me", "towing service near me", "car towing near me", "local towing company near me", "24 hour towing near me", "emergency towing near me", "flatbed towing near me", "accident towing near me" (frase) · [tow truck near me], [towing near me], [towing company near me], [tow company near me] (exacta) | ~390k | Home (con H1 nuevo) | Towing Near You 24/7 / Tow Truck Near You / Local Towing Company |
| **Cheap Towing** | "cheap towing near me", "cheap tow truck near me", "cheapest towing near me", "affordable towing near me", "flat rate towing near me", "tow truck cost near me", "towing cost near me" (frase) · [cheap towing near me] (exacta) | ~24k | Home → sección de precios/cotización | Affordable Towing Near You / Low-Cost Local Towing / Upfront Towing Prices |
| **Roadside Assistance** | "roadside assistance near me", "jump start service near me", "jump start near me", "flat tire service near me", "flat tire change near me", "fuel delivery near me", "gas delivery near me", "winch out service near me" (frase) | ~41k | `/roadside-assistance/` (crear; mientras tanto `/#roadside`) | Roadside Assistance 24/7 / Jump Starts & Tire Changes / Out of Gas? We Deliver |
| **Wesley Chapel Towing** | [towing wesley chapel], [tow truck wesley chapel], [wesley chapel towing] (exacta) + mismas en frase, "pasco county towing", "towing lutz" (frase) | ~130 local | Home | Towing in Wesley Chapel / Wesley Chapel Tow Truck / Pasco County Towing |
| **Grúa ES** *(condicional)* | "grua cerca de mi", "gruas cerca de mi", "servicio de grua cerca de mi", "servicio de grua", "servicio de gruas cerca de mi" (frase) · [servicio de grua cerca de mi] (exacta) | ~12k | `/es/` (crear) | Grúa Cerca de Usted 24/7 / Servicio de Grúa Local / Grúa en Wesley Chapel |

*Volumen nacional de Semrush (no hay Keyword Planner por ciudad). El volumen dentro del radio es una fracción mínima; lo que manda son los datos de la cuenta.

**Por qué 4 ad groups y no más:** con ~90 clics/mes, cada grupo adicional divide los datos. "Towing Near Me" concentra el 80% de la demanda y 15 de las 18 conversiones en inglés. "Cheap" va aparte porque su copy (precio) es distinto y convierte (CPL de $23.50). "Roadside" va aparte porque la intención y el ticket son distintos. "Wesley Chapel" existe porque es el término local con mayor intención y ya convirtió con CPC de ~$10.

**Grúa ES — regla de activación:** solo si (1) el cliente confirma que contesta en español y (2) existe `/es/` o un bloque en español arriba de la home. Si no se cumplen las dos, **pausar el ad group**: hoy gasta el 30% con un CPL de $103.

**Negativas específicas por grupo (a nivel ad group, para que no se crucen los grupos):**
- Towing Near Me: "cheap", "cheapest", "affordable", "cost", "price", "jump", "tire", "fuel", "gas", "wesley chapel", "pasco", "lutz"
- Cheap Towing: "wesley chapel", "pasco", "lutz"
- Roadside Assistance: "tow", "towing", "tow truck"
- Grúa ES: ninguna adicional

**Cambios concretos sobre la cuenta actual (orden de ejecución):**
1. Aplicar negativas de cuenta (`data/negatives-nicho.txt`) → `/negatives`.
2. Pausar: `Towing Service` (broad), `tow company` (frase), `tow truck company` (frase), `servicio de grua cerca de mi en español` (broad), `servicio de grua near me` (broad).
3. Renombrar "Ad group 1 - English" → **Towing Near Me** (conserva su historial). Agregar en frase y exacta las que hoy están en broad, en el mismo momento **pausar la versión broad** (no dejar duplicados compitiendo).
4. Crear los ad groups **Cheap Towing**, **Roadside Assistance** y **Wesley Chapel Towing**. Mover `cheap towing near me` y `roadside assistance near me` a sus grupos (pausar en el grupo 1).
5. Renombrar "Ad group 2 - Spanish" → **Grúa ES**, migrar a frase y pausar según la regla de activación.
6. RSA: **1 por ad group** (la variante A de `data/ads-search.md`). Towing Near Me conserva además su RSA actual (fuerza GOOD), máx. 2; Grúa ES conserva el suyo (EXCELLENT). Las variantes B y C quedan de reserva para cuando el volumen permita comparar.
7. Geo: verificar Presencia y radio de 20 mi. Idioma: inglés + español (el grupo ES lo necesita).

## Keywords descartadas y por qué
| Término | Por qué |
|---|---|
| towing zephyrhills / dade city / land o lakes | ~0 búsquedas; el radio + "near me" las cubre |
| Towing Service, tow company, tow truck company (sin "near me") | Genéricas: gastaron $99.68 sin conversiones y atraen búsquedas de marcas ajenas |
| car lockout near me | El sitio no ofrece lockout (PENDIENTE) |
| box truck / medium duty towing | Ticket alto, pero sin confirmar capacidad → Fase 3 |
| auto body / collision repair wesley chapel | No se sabe si hacen carrocería → Fase 3 |
| Competidores (≈50 nombres) | Estándar #5: el clic llega, la venta no |
| road ranger, aaa, aseguradoras | Buscan un servicio gratis o a su proveedor |
Detalle en `data/keywords.csv`.

## Copy
En `data/ads-search.md`: 3 variantes por ad group (ángulos rapidez / precio / confianza), 15 headlines + 4 descripciones cada una, límites validados por script. **Se activa 1 por grupo (la A); máx. 2** (CLAUDE.md #4). Grúa ES en español.
Extensiones: 4 sitelinks, 8 callouts, snippet de Servicios (7), llamada (813) 381-0435, logo y nombre del negocio. **Ubicación: bloqueada hasta tener el GBP.**
No se usan "licensed & insured", ETA, reseñas ni años de experiencia hasta que el cliente los confirme.

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| `/` con H1 "24/7 Towing in Wesley Chapel, FL", formulario de 3 campos y bloque de reseñas | Parcial | PMM (edición) + Cliente (reseñas) | H1: no · reseñas: no |
| `/thank-you/` (redirect del formulario + conversión) | No | PMM | **Sí** (medición) |
| `/roadside-assistance/` | No | PMM | No (usar ancla mientras tanto) |
| `/es/` (o bloque ES arriba de la home) | No | PMM + Cliente (confirmar que contestan en ES) | **Sí para Grúa ES** |
| `/medium-duty-towing/` | No | PMM | Fase 3, condicional |
| `/collision-repair/` | No | PMM | Fase 3, condicional |

## Presupuesto por fase
| Fase | Total/mes (medios) | Por campaña | Condición para pasar |
|---|---|---|---|
| **F0 – Saneamiento** (ahora → ~10/10) | $760 ($25/día) | 1 campaña | Conversiones verificadas (Website Calls, Form Fill, Calls ≥60 s), negativas aplicadas, broad migrado, geo en Presencia |
| **F1 – Estabilizar** (~10/10 → ~10/11) | $760 | 1 campaña | 4 semanas seguidas con CPL ≤ $40 **y** el cliente confirma que ≥50% de los leads son reales |
| **F2 – Optimizar** (~10/11 → ~10/12) | $760 | 1 campaña; reasignar entre ad groups pausando los de peor CPL | CPL ≤ $30 por 4 semanas; IS perdido por presupuesto > 20% |
| **F3 – Escalar** (desde ~12/2026) | $900–1,050 ($30–35/día) → requiere subir el paquete | 1 campaña + ad groups Medium-Duty / Collision si se confirman | ~30 conv./30 d → evaluar tCPA a CPL real +10% |
| **F4 – Remarketing / RLSA** | +10% del presupuesto | Audiencia de visitantes en observación | Lista ≥1,000 usuarios (con este tráfico, >6 meses) |
| **F5 – PMax** | — | — | Ver "Por qué NO" |

## Por qué NO (todavía)
- **PMax:** exige 30+ conv./mes con tracking confiable, Search estable, exclusión de marca y assets propios. Hoy hay 18 conv./mes, tracking sin verificar, sin GBP y sin fotos reales. Fishhawk corre PMax, pero con otro presupuesto e historial.
- **Amplia:** la cuenta ya muestra el costo: búsquedas de NY, OH y AZ, Road Rangers, aseguradoras y ~40 competidores. `tow truck near me` rinde mejor en frase (CPL de $13.77) que en broad ($41.74).
- **Display / Demand Gen / Video:** servicio de urgencia; nadie contrata una grúa desde un banner.
- **Campaña de marca:** 1–3 impresiones de "jerrys towing" en 38 días. No hay demanda de marca.
- **Más campañas:** $25/día no sostiene ni una campaña a 3× CPL; dividirla dejaría a cada una sin datos.
- **tCPA:** ~20 conv./mes como techo con el presupuesto actual.

## Riesgos y supuestos
- **Negativas universales con excepciones:** "cheapest", "insurance claim", "phone number" suelto y "county" (bloquearía "pasco county towing") no se aplican en esta cuenta; detalle en `data/negatives-nicho.txt`.
- **Economía del cliente:** con un ticket supuesto de $125 y margen del 50%, el CPL "cómodo" es de ~$11 y el de equilibrio ~$37. **Un CPL de $30–40 puede no ser rentable** si el cliente cobra tows locales baratos. Conseguir ticket y tasa de cierre es la prioridad comercial.
- **Tracking:** si "Website Calls" resulta ser un clic en el teléfono, el CPL real es peor que $38.50 y Maximizar conversiones está optimizando hacia clics.
- **Sin GBP ni reseñas:** peor CTR en Maps y en la landing, y sin LSA. El 52% de IS perdido por ranking no se resuelve solo con pujas.
- **CPC de Tampa ~$8–10:** con $25/día son ~3 clics por día; la varianza semanal va a ser alta. No reaccionar a una semana mala.
- **LSA:** verificar si "Towing" es una categoría habilitada en su código postal; si lo es, puede dar leads más baratos que Search. Requiere GBP, licencia y seguro.
