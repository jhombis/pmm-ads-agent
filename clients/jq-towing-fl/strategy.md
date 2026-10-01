---
cliente: JQ Towing
slug: jq-towing-fl
actualizado: 2026-10-01
version: 1
supuestos:
  - "CPL máximo sin calcular: falta ticket, margen y tasa de cierre. Se usa CPL objetivo del benchmark ($25–38) como referencia, no como techo de rentabilidad."
  - "Landing sin auditar (jqtowingfl.com bloqueado por red). URLs por ad group = PENDIENTE; se asume que hay que crear 2 landings + thank-you."
  - "Historial de la cuenta 986-810-9972 sin leer (no conectada a Windsor, sin API). Puja inicial depende de si tiene conversiones recientes."
  - "Volumen 'near me' es nacional (Semrush); el volumen real del radio de 15 mi requiere Keyword Planner geo."
  - "Lista exacta de servicios sin confirmar: lockout, jump, llanta, fuel, flatbed, golf cart, heavy duty."
  - "Claims de copy marcados con * (licensed & insured, upfront quote, no hidden fees, flatbed, base en Belleview) sin confirmar."
---

# Estrategia Google Ads — JQ Towing (Belleview / Ocala, FL)

## Resumen ejecutivo
- **1 campaña Search** (towing + roadside) con 4 ad groups por tema; golf cart como 5.º grupo condicional. Sin marca, sin PMax, sin Display.
- **$879/mes ≈ $29/día**, todo en la misma campaña: ni una sola campaña llega a la regla de 3× CPL/día (~$96), así que dividir el presupuesto rompería el aprendizaje.
- **CPL objetivo inicial: $25–38** (mediana de cuentas Search towing del MCC ±20%; FL agregado $37.8). El CPL máximo de rentabilidad queda PENDIENTE.
- **Expectativa:** 15–27 conversiones/mes (mes 1 en el extremo bajo); con llamadas ≥ 60 s como conversión, menos que el benchmark, pero más reales.
- **tCPA:** realista en el mes 2–3, al llegar a ~30 conversiones en 30 días. **LSA** como pista paralela si el cliente tiene licencia, seguro y acepta el background check.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| `JQ \| Search \| Towing & Roadside \| 15mi` | Llamadas ≥ 60 s + formulario | $29 | 100% | Maximizar conversiones sin tCPA (ver nota) | Radio 15 mi desde 29.045014, -82.037279 · **Presencia** · excluir resto de países | 24/7 (el cliente contesta 24/7 real) |
| LSA (pista paralela) | Leads pagados por lead | Aparte (PENDIENTE) | — | Max leads | Marion County dentro del radio | 24/7 |

**Nota de puja:** si la cuenta 986-810-9972 registró conversiones en los últimos 30–60 días, va Maximizar conversiones desde el día 1. Si no tiene historial, Maximizar clics con CPC máx. $9 solo hasta acumular ~10 conversiones (≤ 3 semanas) y después Maximizar conversiones. Max clics no es estrategia final: las 4 cuentas del MCC que lo usan están en el cuartil inferior.

**Conversiones (Fase 0):**
- Primarias: llamadas desde anuncios ≥ 60 s, llamadas al número de desvío en el sitio ≥ 60 s, y envío de formulario (thank-you con URL propia).
- Secundaria (no se optimiza): clic en `tel:`.
- El benchmark muestra cuentas que cuentan llamadas de 20 s o 3 acciones primarias a la vez; aquí no.

**Configuración:**
- Solo red de Búsqueda: sin socios de búsqueda ni Display.
- Rotación: optimizar.
- Recomendaciones automáticas: apagadas.
- Audiencias: sin exclusiones.
- Idioma: inglés.

## Estructura por campaña
### Campaña: JQ | Search | Towing & Roadside | 15mi
| Ad group | Keywords (match) | Vol. est. | Landing | H1 pinneado |
|---|---|---|---|---|
| Towing - Near Me | [tow truck near me], [towing near me]; "tow truck near me", "towing near me", "towing company near me", "tow company near me", "towing service near me", "wrecker service near me", "tow truck", "towing service", "towing company", "car towing", "wrecker service" · *"flatbed tow truck near me", "flatbed towing" en pausa hasta confirmar flatbed* | Mayor volumen; local desconocido (US: 110–135k/mes) | /towing (crear) | Tow Truck Near Me |
| Towing - Ocala & Belleview | [ocala towing], [towing ocala fl], [tow truck ocala fl]; "towing ocala", "tow truck ocala", "towing service ocala", "towing company ocala", "wrecker service ocala", "towing belleview", "tow truck belleview", "towing summerfield", "towing lady lake", "towing the villages", "tow truck the villages", "towing silver springs" | ~870/mes | /towing (crear; H1 dinámico o variante Ocala) | Towing in Ocala, FL |
| Towing - Emergency 24/7 | "24 hour towing", "24 hour tow truck", "emergency towing", "emergency tow truck", "towing open now", "accident towing", "car accident towing", "i 75 towing", "roadside towing" | Bajo, alta intención | /towing | 24/7 Emergency Towing |
| Roadside Assistance | [roadside assistance near me]; "roadside assistance", "car lockout service", "locked keys in car", "jump start service", "car jump start", "flat tire change", "flat tire service", "fuel delivery service", "ran out of gas", "winch out service", "car stuck in ditch" | Medio (US: 33k + servicios) | /roadside-assistance (crear) | Roadside Assistance 24/7 |
| Golf Cart Towing *(condicional)* | "golf cart towing", "golf cart tow", "golf cart towing the villages" | 20–70/mes | /towing o sección | Golf Cart Towing |

Por qué Ocala & Belleview va como ad group aparte aunque ninguna combinación pase de 100/mes: es el único bloque con volumen local medible (~870/mes), sin anunciantes visibles, y lleva el H1 con la ciudad. Las demás ciudades van dentro del mismo grupo, sin servicio × ciudad.

**Negativas específicas por grupo (cross-negatives para evitar canibalización):**
- *Towing - Near Me*: "ocala", "belleview", "summerfield", "lady lake", "the villages", "emergency", "24 hour", "lockout", "jump start", "flat tire".
- *Towing - Ocala & Belleview*: "near me", "emergency", "24 hour".
- *Towing - Emergency 24/7*: "near me" no (la intención de emergencia suele llevar "near me"; se deja competir).
- *Roadside Assistance*: "tow truck", "towing".

**Negativas de cuenta:** universal PMM + `data/negatives-nicho.txt` (133 líneas: nicho towing, motor clubs/seguros, impound, renta/talleres, precio irreal, servicios no confirmados, competidores locales, ciudades fuera del radio).

## Keywords descartadas y por qué
| Keyword / grupo | Motivo |
|---|---|
| "$50 towing", "free towing" | Precio irreal: en FL el remolque local cuesta $85–160; atrae llamadas que no cierran |
| aaa tow, motor clubs, seguros | Navegacional; el usuario ya tiene proveedor |
| tow yards, impound, city tow, towed car | Busca su auto incautado, no un servicio |
| junk car removal ($7.44) | Otro modelo de negocio; solo si el cliente compra chatarra |
| heavy duty ($7.37), semi, RV, box truck | Equipo no confirmado; un clic se come ¼ del día |
| motorcycle towing | Servicio no confirmado |
| cheap towing | No se puja; se evalúa en search terms (puede entrar por frase) |
| Marcas de competidores (Muggsuggs, Carter's, Dave's, J&D, K&J, Matos…) | Estándar PMM: no pujar salvo prueba controlada |
| Marca propia "jq towing" | Sin volumen medible en FL ni competidores pujando; se revisa en el día 30 |

Detalle completo en `data/keywords.csv` (63 filas).

## Copy
En `data/ads-search-towing-roadside.md`:
- 4 ad groups × 15 headlines + 4 descripciones, con límites de caracteres validados.
- 3 RSA por grupo: A sin pin en posición 2, B con ángulo precio, C con ángulo local.
- Sitelinks, callouts, snippets, llamada y ubicación.

**Ángulos (de competitors.md):**
- "Real person answers 24/7": verdadero según el brief.
- Base local en Belleview junto a la salida 341 de la I-75; nadie más lo usa.
- "Upfront quote / no hidden fees": ataca las quejas por cargos de almacenaje de Dave's y Carter's.
- Corredor I-75.

**Claims sin confirmar (`*`):** licensed & insured, upfront quote, no hidden fees, flatbed, cars/trucks/SUVs, long-distance y base en Belleview. No se publican sin confirmación del cliente.
**Tiempo de llegada:** no se promete ningún ETA en minutos hasta tener el dato real del cliente; es el ángulo que usan los agregadores ("30–45 min").

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| /towing — "24/7 Towing in Ocala & Belleview, FL" (grupos Near Me, Ocala y Emergency) | PENDIENTE (sitio sin auditar) | PMM (Leadpages disponible) o quien edite el sitio | Sí |
| /roadside-assistance — lockout, jump, llanta, fuel, winch-out | PENDIENTE | PMM / cliente | Sí (o enviar a /towing con sección roadside y H1 adaptado) |
| /thank-you con URL propia | PENDIENTE | PMM | Sí: conversión de formulario |
| Número de desvío (call tracking) visible en ambas | PENDIENTE aceptación | Cliente | Sí |

**Mínimo de cada landing:**
- H1 que refleje el término buscado.
- Botón `tel:` fijo en móvil.
- Formulario de ≤ 4 campos (nombre, teléfono, ubicación del vehículo, servicio).
- Reseñas reales (GBP) y área de servicio.
- Sin menú que saque al usuario de la página.

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |
|---|---|---|---|
| F0 — Setup | $0 | — | Tracking verificado con Tag Assistant (llamada ≥ 60 s + form), landings con 200, claims confirmados, negativas aplicadas |
| F1 — Lanzamiento (días 1–30) | $879 | Search 100% ($29/día) | ≥ 15 conversiones en 30 días y CPL ≤ $45; search terms limpios en las revisiones de los días 7, 14 y 30 |
| F2 — Optimización (días 31–60) | $879 | Reasignar con ajustes por ad group (pausar el que tenga CPL > 2× la media) | ~30 conversiones en 30 días |
| F3 — tCPA (mes 2–3) | $879 → propuesta $1,200 si IS perdido por presupuesto > 30% y CPL ≤ objetivo | tCPA = CPL real de 30 días ×1.0–1.1 | CPL estable 2 semanas; cliente confirma capacidad |
| F4 — Remarketing / RLSA | +10% | Observación → ajuste de oferta | Audiencia de ≥ 1,000 usuarios |
| F5 — PMax | Ver condición | — | Ver "Por qué NO" |

## Por qué NO (todavía)
- **PMax:** requiere más de 30 conversiones al mes con tracking confiable, Search estable, exclusión de marca y assets propios. Hoy no existe nada de eso. Además, en el MCC su CPL "bajo" viene mezclado con marca y acciones locales.
- **Amplia:** en el MCC rinde algo mejor que frase (CPL $21 contra $25), pero en cuentas maduras con conversiones infladas por llamadas cortas. Para una cuenta nueva con $29/día, amplia gasta en búsquedas ajenas. Se reevalúa con tCPA maduro y aprobación de Jhombis.
- **Campaña de marca:** "jq towing" no tiene volumen medible en FL y nadie puja por el nombre.
- **Separar towing y roadside en campañas:** con $29/día ninguna llega al mínimo de aprendizaje. Se separan cuando el presupuesto pase de ~$100/día o roadside muestre un CPL muy distinto.
- **Display / Video / Demand Gen:** no aplican a una urgencia local.
- **Heavy duty / junk car:** CPC de más de $7 y equipo sin confirmar.

## Riesgos y supuestos
- **CPL máximo desconocido.** Si el margen por servicio ronda $60–80, un CPL de $38 puede no ser rentable. Es lo primero a resolver con el cliente.
- **CPC real probablemente por encima de Semrush ($3–4):** el benchmark del MCC da ~$7 en Search, lo que deja unos 125 clics al mes. Si el CPC real pasa de $9, el volumen cae a menos de 100 clics y la salida de aprendizaje se demora.
- **Volumen local de "near me" desconocido:** si el radio de 15 mi no da más de ~1,500 búsquedas al mes, el techo es la demanda y no el presupuesto.
- **Muggsuggs (más de 150 reseñas)** puede dominar Maps y LSA. Sin GBP verificado y con reseñas no hay activo de ubicación ni LSA competitivo.
- **Speed to lead:** el brief dice que contesta 24/7. Si de noche no contesta, conviene restringir el horario. Se verifica en la revisión del día 14 con la tasa de llamadas perdidas.
- **Historial de la cuenta 986-810-9972 sin leer:** puede haber conversiones mal configuradas o negativas útiles. Conectar a Windsor antes de construir.
