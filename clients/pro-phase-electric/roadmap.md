---
cliente: Pro Phase Electric
slug: pro-phase-electric
D0: 2026-09-23
actualizado: 2026-09-23
fase_actual: 0
---

# Roadmap — Pro Phase Electric

> Las fechas son proyección; **la condición de paso es la que manda**. /weekly-review solo avanza de fase cuando se cumple la condición. Si no se cumple, anota el bloqueo y reprograma.
> Contexto: la cuenta **ya está activa** (desde 01-sep, Max. clics, broad). Por eso la Fase 0 incluye **contener el gasto** en la campaña actual mientras se prepara la nueva.
> Equivalencia con `strategy.md`: la "F2 — Paneles + EV" de strategy está aquí dentro de la Fase 2 y de la pista Landing.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Fundación + contención | 23-sep → 30-sep (o 07-oct si el sitio lo edita el cliente) | 🔄 en curso |
| 1 — Lanzamiento Search NWA | 01-oct → 08-oct | ⏳ |
| 2 — Limpieza (D7 · D14 · D30) + Paneles/EV | 08-oct · 15-oct · 31-oct | ⏳ |
| 3 — tCPA | **No alcanzable con $825/mes.** Con aumento a $1,500–1,800: ~05-ene-2027 | ⛔ por presupuesto |
| 4 — Remarketing | No realista (audiencia < 1,000) | ⛔ |
| 5 — Performance Max | No califica en el horizonte visible | ⛔ |
| 6 — Conversiones offline | Fuera de alcance (sin CRM) | ⏸ |
| Pista Landing | Paneles + EV listas ~14-oct (si edita PMM) | 🔄 |
| Pista LSA | En espera: el cliente dijo "No" por ahora | ⏸ |

## Fase 0 — Fundación + contención
- **Fecha estimada**: 23-sep → 30-sep, si PMM edita el sitio (+3 días por los bloqueantes de audit). Se corre a **07-oct** si lo edita el cliente (+7–14). Quién edita está PENDIENTE en el brief.
- **Condición de paso**: todos los ítems bloqueantes de Fase 0 en `checklist.md` en ✅, en especial **llamadas del sitio + formulario probados con Tag Assistant** (≥1 conversión de prueba en cada acción).
- **Tareas**:
  - *Contención en la campaña actual (esta semana, PMM):*
    - Importar `data/2026-09-22-negatives-editor.csv` (103 negativas).
    - Pausar las keywords broad "home electrical", "electrical services", "electrical contractors" y "home electrical services".
    - Poner techo de CPC de $12.
    - Apagar socios de búsqueda y Display.
    - Revisar que la ubicación sea "Presencia".
    - Poner la programación L–D de 5:00 a 16:00.
  - *Tracking (PMM, necesita acceso al Tag y al sitio):*
    - Conversión de formulario con página de gracias o evento.
    - "Website calls" con número de reenvío de Google.
    - Clic en `tel:`.
    - "Calls from Ads" con duración mínima de 60 s.
    - Probar todo con Tag Assistant.
    - GCLID/UTM en campos ocultos del formulario.
  - *Cliente:*
    - Acceso de gestor al GBP para PMM.
    - Decir quién contesta el teléfono de 5 a 16, en cuánto tiempo, y qué pasa con el buzón.
    - Aceptar el número de reenvío.
    - Ticket y margen de un cambio de panel y de una instalación EV.
    - Confirmar si cubren Siloam Springs y Gentry, y si instalan generadores.
    - Decir quién edita el sitio.
  - *PMM:* aplicación automática de recomendaciones apagada. Lista "PMM Universal" y lista de nicho (hoy van como negativas de campaña vía CSV; se pasan a listas cuando haya API).
- **Riesgos**:
  - Si el sitio lo edita el cliente o su agencia (crédito en el footer), el tracking del formulario puede tardar 1–2 semanas.
  - **Sin un proceso de respuesta definido** (quién contesta, en cuánto tiempo) es bloqueante: una llamada perdida cuesta ~$50.
  - La campaña actual sigue gastando mientras tanto; la contención reduce el daño, no lo elimina.

## Fase 1 — Lanzamiento Search NWA
- **Fecha estimada**: lanzamiento **01-oct** (o 08-oct), paso a Fase 2 el **08-oct**.
- **Condición de paso**: campaña activa 7 días, anuncios aprobados, ≥1 conversión registrada **del sitio** (no solo de la extensión de llamada).
- **Qué se lanza**:
  - "Pro Phase Electric - Search NWA - $1500/mo. - [fecha]" con **$27/día** y Max. conversiones sin tCPA.
  - 6 ad groups activos: General, Fayetteville, Rogers, Springdale, Bentonville y Repair. Paneles y EV se crean **pausados**.
  - 18 RSA, extensiones de `data/ads-search-nwa.md` y negativas universal + nicho.
  - Se pausa la campaña actual el mismo día.
  - La construye `/build-campaign`, en pausa. Jhombis revisa y activa.
- **Riesgos**:
  - Presupuesto menor a 3× CPL/día: el aprendizaje va a ser lento y ruidoso. No se juzga antes de 30 días; en semanas 1–3 se tolera un CPL de hasta $80.
  - Advertencia de operación: si el cliente no contesta en el horario de 5 a 16, Max. conversiones aprende de llamadas perdidas.
  - Sin el GBP vinculado no hay activo de ubicación.

## Fase 2 — Limpieza (D7 · D14 · D30) + Paneles y EV
- **Fechas** (si el lanzamiento es el 01-oct): **D7 = 08-oct · D14 = 15-oct · D30 = 31-oct**.
- **Condición de paso**: las tres revisiones hechas, negativas aplicadas, keywords sin impresiones pausadas en D30, RSA más débil de cada grupo reemplazado y ≥10 conversiones en 30 días.
- **Qué se revisa**: search terms → negativas (sobre todo utilities, competidores y DIY que se escapen), gasto sin conversión por keyword (>2× CPL sin conversión → revisar), RSA más débil por grupo, IS perdida por presupuesto contra ranking, y **QS y experiencia de landing de los grupos de ciudad**.
- **Paneles y EV**: se activan **después de D14** si ya pasaron por /audit-landing (pista Landing). Se agregan sus sitelinks.
- **Pedido al cliente en D30**: que marque qué llamadas se volvieron trabajo (hoja simple). Es la única forma de validar el CPL sin CRM.

## Fase 3 — Optimización de puja (tCPA)
- **Fecha estimada**: **no alcanzable con $825/mes.**
  - *Supuesto*: $27/día ÷ CPL de $50 = 0.54 conv./día → ~16 conv. por ventana de 30 días. La condición pide 30 en 30 días, y a este ritmo **nunca se llega**. Juntar 30 conversiones acumuladas tomaría 56 días, pero eso no es lo mismo que la condición.
  - *Con el aumento propuesto en strategy* ($1,500–1,800 de pauta ≈ $55/día → ~1.1 conv./día), aprobado hacia el **15-nov**: la ventana llega a 30 conv. ~30 días después, más 2 semanas por presupuesto < 3× CPL → **~05-ene-2027**.
- **Condición de paso**: ≥30 conversiones en una ventana de 30 días con tracking verificado.
- **Acción**: tCPA = CPA real observado (no el deseado); reajustar presupuesto según capacidad.
- **Si no se cumple en fecha**: revisar la tasa de conversión de la landing (<5% → landing), el presupuesto y la mezcla de keywords. **No forzar tCPA con menos datos.** Mientras tanto se sigue con Max. conversiones; en F3 se presenta la propuesta de presupuesto.

## Fase 4 — Remarketing
- **Fecha estimada**: no realista en el horizonte visible.
- **Condición de paso**: audiencia ≥1,000 usuarios en 30 días.
- **Por qué no**: ~80 clics pagados al mes y ~3 visitas orgánicas al mes (Semrush). La lista no llega a 1,000.
- **Acción si cambia**: RLSA en observación, luego ajuste de puja.

## Fase 5 — Performance Max
- **Fecha estimada**: **no califica**. No hay fecha realista con el presupuesto actual.
- **Condiciones que fallan** (`knowledge/estrategias/pmax-cuando-y-como.md`):
  1. Search con tCPA estable 4 semanas: depende de F3, que no se alcanza.
  2. ≥30 conv./mes: proyección de 12–20.
  3. Presupuesto ≥3× CPA/día (~$150/día): hay $27.
  4. Formulario con anti-spam moderno: hoy es un captcha matemático.
  5. Video corto: no hay.
- **Qué haría falta**: aumentar la pauta a ≥$4,500/mes y cumplir F3. Alternativa realista: **quedarse en Search** (el remarketing tampoco califica; ver F4).

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance (sin CRM). Paso intermedio sin costo: la hoja mensual de "llamadas que se volvieron trabajo" (F2, D30). Se reevalúa si el cliente empieza a registrar leads con GCLID (el campo oculto ya queda en F0).

## Pista paralela — Landing
| Ajuste | Tipo | Responsable | Fecha objetivo |
|---|---|---|---|
| Conversión del formulario (página de gracias o evento) + clic en `tel:` | **Bloqueante F0** | PMM | 30-sep |
| Score de PageSpeed móvil (si es <40, bloqueante F1) | **Bloqueante F0** (verificar) | PMM | 26-sep |
| Captura móvil de la home: ¿se ve el formulario o el botón de llamada sin scroll? | Verificar F0 | Jhombis | 26-sep |
| Landing `/electrical-panel-upgrade/` | **Bloqueante del ad group Paneles** | PMM o cliente | 14-oct (PMM) / 21-oct (cliente) |
| Landing `/ev-charger-installation/` | **Bloqueante del ad group EV** | PMM o cliente | 14-oct (PMM) / 21-oct (cliente) |
| H1 de la home → "Licensed Electrician in Northwest Arkansas…" | Mejora (QS) | PMM o cliente | 08-oct |
| Horario "Open 7 days · 5 AM–4 PM" en el sitio y el GBP | Mejora | Cliente | 08-oct |
| Número de licencia de Arkansas junto al badge | Mejora | Cliente | 15-oct |
| Captcha matemático → reCAPTCHA v3 o honeypot | Mejora | PMM o cliente | 31-oct |
| Email propio en lugar de Gmail | Mejora | Cliente | 31-oct |
| `/electrical-repair/` y landings por ciudad | Mejora F3 (según QS) | — | después de D30 |

## Pista paralela — LSA
- **Estado**: ⏸ en espera. Electricista califica en US, pero el cliente dijo "No" por ahora (GBP y requisitos).
- **Si el cliente acepta**: D+0 iniciar la solicitud (licencia, seguro, background check, GBP), D+14–28 verificación, después presupuesto semanal y gestión de reseñas. Con ~33 reseñas contra ~2,480 de Mister Sparky, **el volumen de reseñas decide el ranking en LSA**: hay que arrancar un pedido sistemático de reseñas antes de invertir.

## Estacionalidad y ventanas
- Electricista residencial en NWA: demanda bastante estable.
- **Tormentas de hielo o viento (dic–feb)** disparan búsquedas de "power outage" y reparación. Las de cortes van a las cooperativas; la negativa `outage` queda. Las de reparación sí son del cliente, así que conviene subir el presupuesto esos días si hay capacidad.
- **Nov–dic**: iluminación navideña (ticket bajo; no se puja).
- **Primavera–verano**: más paneles (cargas de AC) y EV. Es buen momento para que Paneles y EV ya tengan historia; otra razón para no retrasar sus landings.

## Historial de cambios
- 2026-09-23: creado (D0 = 2026-09-23). Cuenta ya activa desde 01-sep; F0 incluye contención.
