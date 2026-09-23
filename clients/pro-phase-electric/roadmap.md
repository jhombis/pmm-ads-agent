---
cliente: Pro Phase Electric
slug: pro-phase-electric
D0: 2026-09-23
actualizado: 2026-09-23
fase_actual: 1
plan_es: https://claude.ai/artifact/B6JRbhCt3HNMFq29UeJv36
plan_en: https://claude.ai/artifact/3KhWsGyQmP8QY9ZLm1zZgk
---

# Roadmap — Pro Phase Electric

> Las fechas son proyección; **la condición de paso es la que manda**. /weekly-review solo avanza de fase cuando se cumple la condición. Si no se cumple, anota el bloqueo y reprograma.
> Contexto: la cuenta **ya está activa** (desde 01-sep, Max. clics, broad). Por eso la Fase 0 incluye **contener el gasto** en la campaña actual mientras se prepara la nueva.
> Equivalencia con `strategy.md`: la "F2 — Paneles + EV" de strategy está aquí dentro de la Fase 2 y de la pista Landing.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Medición + contención | Contención ✅. Medición del sitio pendiente (en paralelo, por Jhombis) | 🔄 en curso |
| 1 — Lanzamiento Search NWA | **Lanzada 23-sep** (ID 24273708366; F0 incompleta por decisión de Jhombis) → paso a F2 el 30-sep | 🔄 en curso |
| 2 — Limpieza (D7 · D14 · D30) | **30-sep · 07-oct · 23-oct** | ⏳ |
| 3 — Decisión de presupuesto → cambio de puja → tCPA | Decisión ~1–15-nov. Max. conversiones: con 15+ conv/mes (pide ~$1,275/mes a CPL $85). tCPA: sin fecha en el escenario base; ~05-ene-2027 solo con aumento y CPL ≤$55 | ⛔ por presupuesto |
| 4 — Remarketing | No realista (audiencia < 1,000) | ⛔ |
| 5 — Performance Max | No califica en el horizonte visible | ⛔ |
| 6 — Conversiones offline | Fuera de alcance (sin CRM) | ⏸ |
| Pista Landing | Paneles + EV listas ~14-oct (si edita PMM) | 🔄 |
| Pista LSA | En espera: el cliente dijo "No" por ahora | ⏸ |

## Fase 0 — Medición + contención
- **Fecha estimada**: 23-sep → 30-sep, si PMM edita el sitio (+3 días por los bloqueantes de audit). Se corre a **07-oct** si lo edita el cliente (+7–14). Quién edita está PENDIENTE en el brief.
- **Condición de paso**: todos los ítems bloqueantes de Fase 0 en `checklist.md` en ✅, en especial **llamadas del sitio + formulario probados con Tag Assistant** (≥1 conversión de prueba en cada acción).
- **Tareas**:
  - *Contención en la campaña actual (esta semana, PMM):*
    - Importar `data/2026-09-22-negatives-editor.csv` (103 negativas).
    - Pausar las keywords broad "home electrical", "electrical services", "electrical contractors" y "home electrical services".
    - Poner techo de CPC de $12.
    - Apagar socios de búsqueda y Display.
    - Revisar que la ubicación sea "Presencia".
    - Programación L–D 7:00–18:00 Central = 5:00–16:00 en la cuenta (Pacífico), según la orden de pedido. ✅ 23-sep.
  - *Tracking (PMM, necesita acceso al Tag y al sitio):*
    - Conversión de formulario con página de gracias o evento.
    - "Website calls" con número de reenvío de Google.
    - Clic en `tel:`.
    - "Calls from Ads" con duración mínima de 60 s.
    - Probar todo con Tag Assistant.
    - GCLID/UTM en campos ocultos del formulario.
    - Medición del playbook §7: **un solo teléfono** en todo el sitio (el de reenvío; hoy (479) 287-3650 en barra, header y hero), formulario de prueba con llegada del correo y conversión registrada en 24–48 h, recurso de llamada aprobado con filtro de 60 s, popups/"After Submit" si es Elementor. Anotar la fecha de cada arreglo.
  - *Cliente:*
    - Acceso de gestor al GBP para PMM.
    - Decir quién contesta el teléfono de 7 a 18 Central, en cuánto tiempo, y qué pasa con el buzón.
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
  - "Pro Phase Electric - Search NWA - $1500/mo. - [fecha]" con **$27/día** y **Max. clics con tope de CPC $12** (playbook §5: <15 conv/mes).
  - 2 ad groups activos: **Electrician - NWA** (near me + todas las ciudades, H1 con inserción de keyword) y **Electrical Repair**. Paneles y EV se crean **pausados**.
  - 1 RSA por ad group (2 activos), extensiones de `data/ads-search-nwa.md` y negativas universal + nicho.
  - Se pausa la campaña actual el mismo día.
  - La construye `/build-campaign`, en pausa. Jhombis revisa y activa.
- **Riesgos**:
  - Presupuesto menor a 3× CPL/día: el aprendizaje va a ser lento y ruidoso. No se juzga antes de 30 días; en semanas 1–3 se tolera un CPL de hasta $80.
  - Advertencia de operación: si el cliente no contesta en el horario de 7 a 18, se pagan llamadas que nadie atiende (y cuando pase a Max. conversiones, aprenderá de llamadas perdidas).
  - Sin el GBP vinculado no hay activo de ubicación.

## Fase 2 — Limpieza (D7 · D14 · D30) + Paneles y EV
- **Fechas** (lanzada el 23-sep): **D7 = 30-sep · D14 = 07-oct · D30 = 23-oct**.
- **Condición de paso**: las tres revisiones hechas, negativas aplicadas, keywords sin impresiones pausadas en D30, y **≥8 conversiones en 30 días con CPL ≤ $100** y tendencia a la baja (escenario base de strategy v4: ~8–13 prospectos/mes, CPL ~$65–100). Con 1 RSA por grupo no hay "RSA más débil" que reemplazar: se revisan los activos del RSA.
- **Qué se revisa**: search terms → negativas (sobre todo utilities, competidores y DIY que se escapen), gasto sin conversión por keyword (>2× CPL sin conversión → revisar), RSA más débil por grupo, IS perdida por presupuesto contra ranking, y clics por ciudad dentro del grupo NWA (una ciudad solo se separa en F3 si acumula **≥50 clics** con diferencias claras; antes es ruido, playbook §9).
- **Cambio de puja**: con **15+ conversiones en 30 días**, estables y con medición limpia (sin vistas ni clics como conversión) → Max. conversiones sin tCPA. Con $825 y el escenario base (~8–13/mes) **no se espera**; solo en el optimista. Anotar la fecha si ocurre.
- **Paneles y EV**: se activan **después de D14** si ya pasaron por /audit-landing (pista Landing). Se agregan sus sitelinks.
- **Pedido al cliente en D30**: que marque qué llamadas se volvieron trabajo (hoja simple). Es la única forma de validar el CPL sin CRM.

## Fase 3 — Decisión de presupuesto, cambio de puja y tCPA
- **Decisión de presupuesto (~1–15-nov)**: con 30 días de datos, presentar al cliente la matemática real (playbook §4): con $825 el techo es ~8–13 prospectos/mes. Propuesta $1,500–1,800 de pauta.
- **Cambio a Max. conversiones**: condición 15+ conv/30 días estables con medición limpia. A CPL ~$85 eso requiere ~$1,275/mes de pauta: alcanzable solo con el aumento (o si el CPL real resulta optimista).
- **tCPA**: condición ≥30 conversiones en 30 días. A CPL $85 requiere ~$2,550/mes; a $55, ~$1,650. Por eso **no tiene fecha en el escenario base**. Si el aumento se aprueba hacia el 15-nov **y** el CPL baja a ≤$55: ventana de 30 conversiones ~30 días después + 2 semanas de margen → **~05-ene-2027**.
- **Acción**: tCPA = CPA histórico observado +10–20% (nunca el deseado); reajustar presupuesto según capacidad del cliente.
- **Si no se cumple**: revisar la medición primero, luego la tasa de conversión de las landings (<5% → landing), el presupuesto y la mezcla de keywords. **No forzar tCPA con menos datos.** Max. clics con tope no es la estrategia final: si en F3 no hay aumento, se documenta que la cuenta queda limitada por presupuesto.

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
| Horario "Open 7 days · 7 AM–6 PM" en el sitio y el GBP | Mejora | Cliente | 08-oct |
| Número de licencia de Arkansas junto al badge | Mejora | Cliente | 15-oct |
| Captcha matemático → reCAPTCHA v3 o honeypot | Mejora | PMM o cliente | 31-oct |
| Email propio en lugar de Gmail | Mejora | Cliente | 31-oct |
| Verificar que `/residential-electrical-service/` hable de reparaciones (landing del grupo Repair en F1) | Verificar F0 | PMM | 30-sep |
| Landing `/electrical-repair/` (playbook §8: cada grupo a su página) | Recomendada | PMM o cliente | 21-oct |
| Landings por ciudad | Solo si en F3 se separan ciudades | — | después de F3 |

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
- 2026-09-23: **Search NWA lanzada** (24273708366) con los 4 ad groups activos y todas las URLs a la home; campaña anterior pausada. Fase 0 de medición sigue abierta por decisión de Jhombis. Revisiones D7/D14/D30 → 30-sep, 07-oct, 23-oct.
- 2026-09-23: estrategia v4 regenerada con el playbook como base: CPC real $9.80 → ~84 clics/mes; proyección por escenarios (base 8–13 prospectos, CPL ~$65–100, objetivo provisional ≤$85); F2 pide ≥8 conv y CPL ≤$100; F3 pasa a ser decisión de presupuesto; tCPA sin fecha en el escenario base; Repair a /residential-electrical-service/; medición §7 en F0; separar ciudades solo con ≥50 clics.
- 2026-09-23: estrategia v3 (playbook de analítica integrado): puja Max. clics con tope $12 hasta 15+ conv/mes; 1 RSA por grupo; sin keywords Tesla ni "electrical troubleshooting"; +31 negativas del playbook.
- 2026-09-23: estrategia v2. De 8 a 4 ad groups (2 activos en F1): las ciudades se integran en "Electrician - NWA" con inserción de keyword; con ~80 clics/mes, 6 grupos fragmentaban los datos. Separar ciudades pasa a ser decisión de F3.
