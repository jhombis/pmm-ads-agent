---
cliente: Precision Towing
slug: precision-towing
D0: 2026-10-06
actualizado: 2026-10-06
fase_actual: 0
version: 2
plan_es: 
plan_en: 
---

# Roadmap — Precision Towing (v2)

> Re-baseline el 2026-10-06: el D0 anterior (2026-09-29) no avanzó porque ninguna tarea de Fase 0 se ejecutó (faltó confirmación para escribir en la cuenta y el cliente no entregó accesos). Fechas = proyección desde el nuevo D0; condiciones = verdad. Factores aplicados: web la edita el cliente o se monta landing propia (Fase 0 +11 días), presupuesto $27/día < 3× CPL ($78) (Fase 3 +2 semanas, PMax no califica), US con categoría LSA (pista paralela pendiente de licencia), respuesta a leads sin definir (bloqueante en Fase 0), temporada baja de noviembre a marzo.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 · Fundación | 2026-10-06 → 2026-10-17 | 🔄 en curso (acciones de cuenta esta semana; landing vía A o B decidida el 2026-10-10) |
| 1 · Relanzamiento (estructura nueva, Max. clics con tope) | 2026-10-20 → 2026-10-27 | ⏳ pendiente |
| 2 · Limpieza D7 · D14 · D30 y paso a Max. conversiones | 2026-10-27 · 2026-11-03 · 2026-11-19 | ⏳ pendiente |
| 3 · tCPA | 2026-12-03 (rango 2026-11-19 → 2026-12-17) | ⏳ pendiente |
| 4 · Remarketing | 2027-01-20 (revisión) | ⛔ probable bloqueo: audiencia < 1.000 |
| 5 · Performance Max | 2027-04-06 como muy pronto | ⛔ no califica con $825/mes |
| 6 · Conversiones offline | fuera de alcance | ⏳ sin CRM |
| Paralela · Landing | 2026-10-06 → 2026-11-19 | 🔄 en curso |
| Paralela · LSA | depende de licencia (respuesta antes del 2026-10-10) | ⏳ PENDIENTE cliente |

La cuenta sigue gastando ($32/día en la campaña actual, CPC $24 en las dos últimas semanas). Fase 0 arranca por lo que no depende del cliente y frena la sangría: presupuesto a $27, negativas, amplias a frase, programación.

## Fase 0 — Fundación
- **Fecha estimada**: 2026-10-06 → 2026-10-17 (11 días: 2 de acciones en cuenta con OK de Jhombis + hasta el 2026-10-10 para el acceso web + 5 días hábiles para montar la landing vía B si no llega)
- **Condición de paso**: bloqueantes ⚠ de Fase 0 en checklist ✅: medición verificada (llamada ≥30 s y formulario real con Tag Assistant), landing publicada (vía A o B), negativas y eliminaciones aplicadas, presupuesto $27, proceso de respuesta a leads definido, estructura nueva creada en pausa.
- **Tareas**:
  - 2026-10-07 (PMM, con OK de Jhombis, vía Windsor): presupuesto $32 → $27; eliminar 14 keywords (`data/2026-10-06-keyword-removals.txt`); aplicar negativas de campaña (`data/2026-10-06-negatives.txt`); pasar las 93 keywords restantes a frase; programación 6:30–22:30 tras leer `customer.time_zone` en la UI; "Calls from Ads" ≥30 s; secundarias las de clic y locales; recomendaciones automáticas apagadas; confirmar socios de búsqueda y Display apagados y geo en "Presencia".
  - 2026-10-07 (PMM, UI): verificar qué dispara "Form Fill"; si es un evento de clic, pasarla a secundaria.
  - Hasta 2026-10-10 (Cliente vía Jhombis): acceso a WordPress/Elementor y GTM, o contacto de quien edita; quién contesta 7–22 y fuera de horario; licencia CHP/seguro para LSA; los 5 claims (after-hours, flatbed, medium duty, winch, nombre Miller's); ticket promedio; confirmación de $825 como pauta; CNAME `go.precisiontowingca.com` si se va por vía B.
  - 2026-10-10 (PMM): decisión vía A (editar WordPress) o vía B (`/landing-ghl precision-towing todos` o Leadpages: 3 landings + gracias).
  - 2026-10-13 → 2026-10-17 (PMM): landing publicada, conversión de formulario creada, Tag Assistant en móvil, GBP vinculado (si hay acceso), `/build-campaign` con la estructura v2 en pausa, URLs finales actualizadas en `data/keywords.csv`.
- **Riesgos**: si Jhombis no confirma las escrituras el 2026-10-07, cada día cuesta ~$40 de CPC inflado; si el cliente no define quién contesta, se lanza con advertencia y se exige la hoja de leads en D30.

## Fase 1 — Lanzamiento Search
- **Fecha estimada**: activar 2026-10-20; condición evaluable 2026-10-27
- **Condición de paso**: campaña activa 7 días, RSA aprobados (fuerza ≥ "Buena"), ≥1 conversión de llamada y ≥1 de formulario registradas, gasto ≥ $18/día
- **Qué se lanza**: "Search - Precision Towing KRV" $27/día, 4 grupos (AG1 Tow Truck & Towing KRV, AG2 Roadside, AG3 RV & Trailer, AG4 Marca), 87 keywords frase/exacta, Max. clics con tope $9, presencia 21 mi + 2 × 8 mi, programación 6:30–22:30 hora de la cuenta; la campaña ENHPRM Radius se pausa el mismo día; PMax sigue pausada.
- **Riesgos**: menos impresiones al salir de amplia; si el gasto no llega a $18/día en D7, tope a $11. Golden Empire en Auction Insights.

## Fase 2 — Limpieza (D7 · D14 · D30) y paso a Max. conversiones
- **Fechas**: 2026-10-27 · 2026-11-03 · 2026-11-19
- **Condición de paso**: tres revisiones con `/weekly-review`, negativas aplicadas, keywords sin impresiones pausadas, hoja de calidad de leads recibida, **≥15 conversiones limpias en 30 días y CPL ≤ $47 → cambio a Max. conversiones** (sin tCPA)
- **Qué se revisa**: search terms (competidores nuevos, taller, compra de trailers); gasto > $47 sin conversión por keyword ("tow truck", "roadside assistance" primero); CPL por grupo contra $21–38; IS y pérdida por presupuesto vs ranking; CPC medio contra el tope; Auction Insights; dispositivo (desktop −50% si sigue en 0); en D30 decisión sobre AG3 trailers y "24 hour".

## Fase 3 — Optimización de puja (tCPA)
- **Fecha estimada**: **2026-12-03**. Cálculo: $27/día ÷ CPL benchmark $26 = 1,04 conv/día → 30 conv en ~29 días desde el lanzamiento (2026-11-18); +14 días por presupuesto < 3× CPL/día → 2026-12-03. Con el CPL histórico de la cuenta ($43): 0,63/día → 48 días → 2026-12-07; +14 → 2026-12-21. Rango realista: 2026-11-19 → 2026-12-17.
- **Condición de paso**: ≥30 conversiones en 30 días con tracking verificado (llamadas ≥30 s + formulario real), CPL ≤ $47, ya en Max. conversiones ≥2 semanas
- **Acción**: tCPA = CPA observado en esas 30 conversiones (no $26 por deseo); −10% cada 2 semanas si se sostiene; reparto por grupo según CPA; ajustes de horario y dispositivo con 60 días.
- **Si no se cumple en fecha**: revisar (1) CVR de landing (< 25% de llamadas por clic), (2) IS perdido por presupuesto vs ranking, (3) keywords que consumen sin convertir. No forzar tCPA; no volver a Max. conversiones sin tope si el CPC vuelve a dispararse.

## Fase 4 — Remarketing
- **Fecha estimada**: revisión 2027-01-20
- **Condición de paso**: audiencia ≥1.000 usuarios en 30 días para RLSA (Search)
- **Realidad**: con 60–90 clics/mes y 0 tráfico orgánico la lista será de 100–200: RLSA no se habilita; Display de remarketing sí con lista ≥100, presupuesto residual y fotos propias. GA4 y la audiencia se crean en Fase 0 para acumular desde ya.

## Fase 5 — Performance Max
- **Fecha estimada**: 2027-04-06 como muy pronto
- **Condición de paso**: todas las de `knowledge/estrategias/pmax-cuando-y-como.md` (tCPA estable 4 semanas, 30+ conv/mes verificadas, D30 cumplido, assets propios, landing ≥5% con anti-spam, presupuesto ≥3× CPA/día)
- **Si no califica** (esperado): con $825/mes PMax tendría $5–8/día contra ~$78 necesarios. Solo califica con pauta ≥ $2.000/mes. La PMax existente sigue pausada; no borrarla.

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance (sin CRM). Sustituto: hoja compartida de calidad de leads desde Fase 0; campos ocultos gclid/UTM en el formulario (nativos en la vía B).

## Pista paralela — Landing
| Ajuste | Fase | Fecha | Responsable | Bloqueante |
|---|---|---|---|---|
| Acceso web + GTM o contacto de quien edita (vía A) | 0 | 2026-10-10 | Cliente | Sí (define vía) |
| Vía B: 3 landings GHL/Leadpages (towing, roadside, trailer) + gracias, formulario 3 campos, conversión propia, dominio | 0 | 2026-10-13 → 2026-10-17 | PMM (CNAME: Cliente) | Sí hasta Tag Assistant OK |
| Vía A: `/thank-you/` + redirect en 7 formularios; footer 7–22; bug IDs del formulario | 0 | 2026-10-17 | Cliente | Sí |
| Verificar origen de "Form Fill"; conversión de formulario real | 0 | 2026-10-07 / 2026-10-17 | PMM | Sí |
| Tag Assistant: llamada web + formulario, en móvil | 0 | 2026-10-17 | PMM | Sí |
| Landing estrella reescrita (vía A) o copy final GHL (vía B): H1 "Tow Truck in Lake Isabella & the Kern River Valley", teléfono + ETA, form 3 campos, comunidades, sellos, 4,8★ | 1–2 | antes de 2026-11-19 | PMM redacta / Cliente o PMM publica | No (sí para pasar Fase 2) |
| Sticky móvil; sellos AAA/NAPA/Gold Seal; agregado 4,8★ en páginas de servicio | 2 | 2026-10-30 | Cliente (vía A) / nativo en vía B | No |
| `/roadside-assistance/`, `/5th-wheel-towing/`, `/travel-trailer-towing/` ajustes; home con H1 (AG4) | 2 | 2026-11-06 | Cliente | No |
| Velocidad (hero WebP, fuentes, caché) y fugas de menú | 3 | 2026-12-05 | Cliente / hosting | No (PSI pendiente de medir) |

## Pista paralela — LSA
- Towing es elegible en US; GBP 4,8★ / ~850 reseñas es una ventaja fuerte. Falta licencia (CHP / motor carrier), seguro y disposición al background check: **PENDIENTE cliente, respuesta antes del 2026-10-10**.
- Si confirma: 2026-10-13 iniciar solicitud → verificación 2026-10-27 → 2026-11-10 → presupuesto semanal aparte ($50–75) y gestión de reseñas y tasa de respuesta.
- Si no: fase futura, no bloquea.

## Estacionalidad y ventanas
- Pico mayo–septiembre (Kern River, campgrounds): AG3 trailers tiene sentido ahí. Valle noviembre–marzo: lanzamos el 2026-10-20 entrando en temporada baja; esperar menos impresiones que en agosto–septiembre y no leerlo como fallo de la estructura.
- Invierno: nieve y cierres en Hwy 155/178 traen winch-out y recovery (AG2): mantener AG2 vivo en enero–febrero.
- AG3: si en D30 sigue en 0 conv, pausar y reactivar el 2027-04-15.
- La ventana de 30 conv puede alargarse por temporada baja; el rango de Fase 3 ya lo contempla.

## Historial de cambios
- 2026-09-29: creado (v1) a partir de strategy.md v1, audit-site.md (12/22), benchmark.md (27 cuentas) y brief.md.
- 2026-10-06: v2. Re-baseline D0 por Fase 0 sin ejecutar; estrategia v2 (1 campaña, 4 grupos, Max. clics con tope); landing vía B (GHL/Leadpages) como alternativa al acceso web; diagnóstico `log/2026-10-06-diagnose.md` (CPC $24, CPL $94 en 7 días).
