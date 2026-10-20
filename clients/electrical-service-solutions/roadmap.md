---
cliente: Electrical Service Solutions
slug: electrical-service-solutions
pais: US
D0: 2026-10-20
actualizado: 2026-10-20
fase_actual: 0
plan_es: https://claude.ai/artifact/DDF3D2rBbjUM1vFLbG26eP
plan_en: https://claude.ai/artifact/1mULJUUTdeY8nYccq25HJU
---

# Roadmap — Electrical Service Solutions

> Las fechas son proyección; **la condición de paso es la que manda**. /weekly-review solo avanza de fase cuando se cumple la condición. Si no se cumple, anota el bloqueo y reprograma.
>
> D0 = 20-oct-2026 (hoy; Jhombis no indicó otra fecha). Insumos: `brief.md` (69%), `audit-site.md` (10/22), `competitors.md`, `benchmark.md` y `strategy.md` v1.1. Supuestos que siguen abiertos: ticket del cliente y volumen por ZIP.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Fundación: medición, web y cuenta | 20-oct → 23-oct | 🔄 en curso |
| 1 — Lanzamiento Search Paneles | Campaña **creada en pausa el 20-oct** (ID 24380613328). Activación estimada **27-oct** → paso a F2 el 03-nov | 🔄 creada en pausa |
| 2 — Limpieza (D7 · D14 · D30) | **03-nov · 10-nov · 27-nov** (D30 cae el 26-nov, Thanksgiving: la revisión va el 27) | ⏳ |
| 3 — Max. conversiones → tCPA | Max. conversiones: no antes del **04-ene-2027**, y solo en el escenario optimista. tCPA: **sin fecha** con esta pauta | ⛔ por presupuesto |
| 4 — Remarketing | No realista (~108 clics/mes; la audiencia no llega a 1,000) | ⛔ |
| 5 — Performance Max | No califica en el horizonte visible | ⛔ |
| 6 — Conversiones offline | Fuera de alcance (sin CRM) | ⛔ |
| Pista Landing | Bloqueantes 21–23-oct · mejoras 30-oct → 27-nov | 🔄 |
| Pista LSA | Inicio cuando haya GBP + licencia + aprobación del cliente; verificación 2–4 semanas | ⏳ |

## Fase 0 — Fundación
- **Fecha estimada**: 20-oct → 23-oct. Son D0+3 porque los bloqueantes de la web los edita PMM (factor del skill). Si el cliente tiene que aprobar los cambios de la web, se va a +7 días.
- **Condición de paso**: todas las tareas bloqueantes de Fase 0 del checklist en ✅, y en particular **Calls from ads y formulario probados con Tag Assistant** (estándar 7: sin tracking no se lanza).
- **Tareas**:
  | Tarea | Responsable | Bloquea |
  |---|---|---|
  | ~~Google Tag en todo el sitio~~ ✅ 20-oct: AW-18460546953 + GTM-58K232MX | Jhombis | — |
  | Conversiones: formulario (primaria), Calls from ads ≥60 s (primaria), clic en tel: (secundaria) | PMM | Sí |
  | ~~/thank-you/~~ ya no hace falta (formulario por evento gtm.formSubmit). Envío de prueba avisando al cliente, con Tag Assistant | PMM | Sí |
  | Formulario de 4 campos (o botón "Get A Free Quote") debajo del H1 en las páginas residencial y comercial | PMM | Sí |
  | Facturación de la cuenta 384-080-6970 configurada y verificada (sin dato: la cuenta nunca gastó) | PMM | Sí |
  | Lista universal PMM (sin "free") + 123 negativas de nicho, con /negatives y tu aprobación | PMM | Sí |
  | Recomendaciones automáticas desactivadas | PMM | Sí |
  | Volumen de los 4 ZIP + Monroeville en Keyword Planner (desde la interfaz: no hay API) | PMM | Sí: define si el tope de $15 y la pauta se pueden gastar |
  | Zona horaria de la cuenta (para convertir la programación) | PMM | No |
  | Campos ocultos GCLID/UTM en el formulario de Elementor | PMM | No |
  | Ticket, margen y tasa de cierre → CPL máximo | Cliente | No para lanzar: sí para la decisión de D30 |
  | Monto mínimo y tasa o promoción del financiamiento | Cliente | No: los anuncios dicen "Financing Available" |
  | Quién contesta fuera de horario y en cuánto tiempo | Cliente | No: las emergencias quedan cerradas en la programación |
  | Acceso de gestor al GBP | Cliente | No: sin él no hay activo de ubicación ni LSA |
- **Riesgos**:
  - Que Keyword Planner muestre un volumen tan chico que la pauta no se gaste. En ese caso se le propone al cliente sumar ZIP vecinos **antes** de lanzar.
  - Que el envío de prueba del formulario no llegue a chris@.

## Fase 1 — Lanzamiento Search
- **Fecha estimada**: **27-oct** (martes). Se arma con /build-campaign el 24-oct, en pausa; tu revisión el fin de semana; activación el lunes 26 y 24 h de revisión de políticas. Paso a F2 el **03-nov**.
- **Condición de paso**: campaña activa 7 días, anuncios aprobados, ≥1 conversión registrada (formulario o Calls from ads) y CallFire con al menos 1 llamada real (no de prueba).
- **Qué se lanza** (strategy.md):
  - ESS · Search · Paneles, con $42.56/día.
  - Max. clics con tope de CPC de $15.
  - 4 grupos (Panel Upgrade, Service Upgrade, Fuse Box, Commercial Panel), 42 keywords en frase + exacta.
  - 1 RSA por grupo y las extensiones (llamada al CTN, sitelinks y callouts).
  - Presencia en los ZIP 15102, 15241, 15228 y 15237 + Monroeville.
  - Horario L–V 9–21 y S–D 9–17, hora del Este.
- **Riesgos**:
  - Con ~3.5 clics/día, una semana son ~25 clics: no se concluye nada de tasas.
  - Si no se sabe quién contesta, las llamadas fuera de horario se pierden. Por eso la programación cierra a las 21:00 y a las 17:00.
  - El sitelink de Financing queda fuera hasta que exista /financing/.

## Fase 2 — Limpieza (D7 · D14 · D30)
- **Fechas**: **D7 = 03-nov · D14 = 10-nov · D30 = 27-nov** (el 26 es Thanksgiving).
- **Condición de paso**: tres revisiones hechas con log, negativas aplicadas, keywords sin impresiones identificadas y pausadas a los 30 días, y reporte de calidad de leads del cliente recibido.
- **Qué se revisa**:
  - **D3 (30-oct, extra)**: search terms de "panel" ambiguo (solar, garage, wall) y de precio. Con $42.56/día un mal término se lleva un tercio del día.
  - **D7**: search terms → negativas. Cuota perdida por ranking y gasto contra presupuesto, para decidir el tope (si se pierde >60% por ranking y se gasta <60%, el tope sube a $18).
  - **D14**: lo mismo, más keywords con gasto y 0 conversiones. Si el gasto está por debajo del 60% con cuota >80%, se le propone al cliente ampliar la geo.
  - **D30**: search terms, pausa de keywords con 0 impresiones, llamadas calificadas en CallFire contra conversiones de Ads, CPL observado contra $100–150 (o contra el CPL máximo si ya llegó el ticket) y decisión sobre la prueba de [commercial electrician near me] si el grupo comercial tiene <50 impresiones.
  - **No** se reemplaza el RSA a D30: con 1 RSA por grupo y <50 clics por grupo, el A/B es ruido (playbook §9).

## Fase 3 — Optimización de puja (Max. conversiones → tCPA)
- **Cálculo** (skill): conversiones/día = presupuesto diario ÷ CPL de benchmark.
  - Al CPL base de $150: $42.56 ÷ $150 = 0.28 conv./día → 30 conversiones acumuladas en ~106 días.
  - A la mediana de $83.95: 0.51/día → ~59 días.
  - La pauta diaria ($42.56) es menor que 3× el CPL ($252–450): aprendizaje lento, +2 semanas.
- **Paso 1, Max. conversiones**: 15+ conversiones/mes durante 2 meses seguidos con medición limpia (calificadas en CallFire). En el escenario base (~8.6/mes) no llega. En el optimista (~15.5/mes) se cumpliría con los meses completos de nov y dic → **no antes del 04-ene-2027**.
- **Paso 2, tCPA**: ≥30 conversiones en una ventana de 30 días, con tCPA = CPA observado. Con esta pauta no se alcanza: pediría $3,000–4,500/mes al CPL objetivo (benchmark.md). **Sin fecha.**
- **Si no se cumple en fecha**: revisar la landing (si la conversión es <5% con el formulario ya arriba), el volumen por ZIP y la calidad de las llamadas en CallFire. **No** forzar Max. conversiones ni tCPA con menos datos. La salida es una decisión de presupuesto con el cliente, con el CPL máximo en la mano.

## Fase 4 — Remarketing
- **Fecha estimada**: no realista. Con ~108 clics/mes, la lista de visitantes no llega a 1,000 usuarios en 30 días.
- **Condición de paso**: audiencia ≥1,000 en 30 días.
- **Acción si algún día se cumple**: RLSA en observación y luego ajuste de puja. No hay Display.

## Fase 5 — Performance Max
- **No califica**. Fallan casi todas las condiciones de `knowledge/estrategias/pmax-cuando-y-como.md`:
  - No hay tCPA activo.
  - No hay 30+ conversiones/mes (se esperan ~9).
  - La pauta diaria es menor que 3× el CPA.
  - Faltan assets propios: hay fotos de paneles en la web, pero no video.
  - La landing todavía no está medida.
- **Qué haría falta**: subir la pauta a ≥$3,000/mes y tener 4 semanas de Search estable con tCPA. Mientras tanto: Search + LSA.

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance (no hay CRM; los leads llegan por llamada y por correo a chris@). Se reevalúa cuando el cliente registre los leads con GCLID (el campo oculto ya va en Fase 0).

## Pista paralela — Landing
De `audit-site.md` (10/22):

| Ajuste | Fecha | Responsable | Tipo |
|---|---|---|---|
| Google Tag + conversiones (formulario, clic en tel:) | ✅ 20-oct (Jhombis); prueba con Tag Assistant 21-oct | PMM | Bloqueante F0 (la prueba) |
| /thank-you/ | No hace falta: formulario por evento | — | — |
| Formulario de 4 campos debajo del H1 (residencial y comercial); contacto con 4 campos | 22-oct | PMM | Bloqueante F0 |
| Verificar que `www.` redirija al dominio | 22-oct | PMM | F0 (no bloquea) |
| Página /financing/ en el dominio (destino del sitelink) | 30-oct | PMM | Mejora F2: activa el sitelink |
| Llamada sticky en móvil | 30-oct | PMM | Mejora F2 |
| Zonas (Bethel Park, Upper St. Clair, Mt. Lebanon, McCandless, Monroeville) en el texto | 30-oct | PMM | Mejora F2 |
| Hero de la home en WebP + preload, logo en WebP o SVG (LCP ~8.8 s) | 10-nov | PMM | Mejora F2 |
| H1 en la home, meta descriptions y JSON-LD Electrician | 27-nov | PMM | Mejora F3 |
| Reseñas de Google (widget o bloque) | cuando haya acceso al GBP | PMM / Cliente | Mejora |
| Número de licencia y "Licensed & Insured" | cuando el cliente los confirme | Cliente → PMM | Mejora |

## Pista paralela — LSA
- **Aplica**: US y la categoría Electrician califica. Va como pista aparte, con presupuesto propio y **aprobación del cliente** (no sale de los $1,293.75 sin acuerdo).
- **Requisitos**: GBP verificado con acceso, número de licencia y seguro, background check del dueño o los técnicos, y reseñas.
- **Fechas** (si arranca al tener el GBP): solicitud en D0+14 (~03-nov), verificación 2–4 semanas (~17-nov → 01-dic) y luego presupuesto semanal y gestión de reseñas.
- **Ojo**: hay que confirmar qué tipos de trabajo de panel permite elegir LSA para electricista; si no se puede restringir a paneles, llegarían leads de otros servicios.

## Estacionalidad y ventanas
- Semrush (12 meses, US): "electrical panel upgrade" está en su **máximo de los últimos 12 meses** (los 3 meses más recientes en 1.00, contra 0.54–0.66 de hace 7–12 meses); "electrical panel replacement" sigue la misma línea (`data/semrush-trend-2026-10-20.csv`). Con un año de datos no se separa estacionalidad de tendencia, pero no hay razón para esperar: **conviene lanzar ya**.
- Thanksgiving (26-nov) y fin de año: el cliente trabaja 7 días, pero el horario de feriados está PENDIENTE. La revisión D30 se corre al 27-nov.
- Comercial: los change-outs se programan con el negocio cerrado (la web lo dice). Sin datos de estacionalidad propia.

## Historial de cambios
- 2026-10-20: campaña 24380613328 creada en pausa por Windsor, por decisión de Jhombis con la Fase 0 incompleta. Antes de activar faltan, en la interfaz: ubicaciones con Presencia, socios apagados y el pin del H1 (log/2026-10-20-build.md).
- 2026-10-20: Jhombis instaló el Google Tag y las conversiones. La web pasa a 13/22; el formulario arriba es el único bloqueante de la web que queda, más la prueba de las conversiones. Fechas sin cambio.
- 2026-10-20: creado (D0 = 20-oct). Fechas: F0 → 23-oct, lanzamiento 27-oct, D7 03-nov, D14 10-nov, D30 27-nov. F3 a F5 sin fecha por presupuesto.
