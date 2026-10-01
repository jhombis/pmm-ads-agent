---
cliente: Precision Towing
slug: precision-towing
D0: 2026-09-29
actualizado: 2026-09-29
fase_actual: 0
---

# Roadmap — Precision Towing

> Fechas = proyección desde D0 2026-09-29. Condiciones = verdad. /weekly-review avanza la fase solo cuando la condición se cumple. Factores aplicados: la web la edita el cliente (Fase 0 +14 días), presupuesto $27/día < 3× CPL benchmark ($78) (Fase 3 +2 semanas, PMax probablemente nunca califica), país US con categoría LSA (pista paralela pendiente de licencia), proceso de respuesta a leads no definido (bloqueante en Fase 0), nicho estacional (pico mayo–septiembre, lanzamos en temporada baja).

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 · Fundación | 2026-09-29 → 2026-10-13 | 🔄 en curso |
| 1 · Lanzamiento Search (estructura nueva) | 2026-10-14 → 2026-10-21 | ⏳ pendiente |
| 2 · Limpieza D7 · D14 · D30 | 2026-10-21 · 2026-10-28 · 2026-11-13 | ⏳ pendiente |
| 3 · tCPA | 2026-11-26 (rango 2026-11-13 → 2026-12-09) | ⏳ pendiente |
| 4 · Remarketing | 2027-01-15 (revisión) | ⛔ probable bloqueo: audiencia < 1.000 con este tráfico |
| 5 · Performance Max | 2027-03-30 como muy pronto | ⛔ no califica con $825/mes (ver fase) |
| 6 · Conversiones offline | fuera de alcance | ⏳ sin CRM |
| Paralela · Landing | 2026-09-29 → 2026-11-13 | 🔄 en curso |
| Paralela · LSA | depende de licencia (respuesta antes del 2026-10-06) | ⏳ PENDIENTE cliente |

La cuenta ya está gastando ($825/mes en la campaña "ENHPRM Radius"). Fase 0 no detiene el gasto: aplica las mejoras que no dependen del cliente (negativas, frase) sobre la campaña actual mientras se resuelven los bloqueantes.

## Fase 0 — Fundación
- **Fecha estimada**: 2026-09-29 → 2026-10-13 (14 días porque la web y el GTM los edita el cliente o un tercero; si PMM consigue acceso directo en la primera semana, se acorta a 2026-10-06)
- **Condición de paso**: todas las tareas bloqueantes de Fase 0 en checklist ✅ (acceso web+GTM, conversión de formulario probada, Tag Assistant OK, horario unificado, negativas aplicadas, proceso de respuesta a leads definido, estructura nueva creada en pausa)
- **Tareas**:
  - Esta semana, sin esperar al cliente (PMM): aplicar lista universal + `data/negatives-nicho.txt` a la cuenta actual con `/negatives`; pasar las 22 keywords amplias de "ENHPRM Radius" a frase (misma campaña, sin tocar puja) para frenar el 13,5% de desperdicio; poner duración mínima 30 s en "Calls from Ads"; marcar "Clicks to call" y acciones locales como secundarias; desactivar aplicación automática de recomendaciones; confirmar en la UI que la geo es "Presencia" y que socios de búsqueda y Display están apagados (Windsor no lo muestra).
  - Cliente (vía Jhombis, esta semana): acceso de edición a precisiontowingca.com (WordPress/Elementor) y a GTM-NWQH4MVX, o nombre y contacto de quien publica cambios. **Bloqueante raíz.**
  - Cliente: definir quién contesta el (760) 606-4160 en horario, quién fuera de horario, y en cuánto tiempo devuelven un formulario. Sin esto, un CPL bueno no se convierte en dinero.
  - Cliente/quien edite: crear `/thank-you/` (noindex, teléfono grande, "we call you back in 5 minutes") y poner Redirect en los 7 formularios Elementor; corregir footer a "Monday – Sunday 7 AM – 10 PM"; corregir IDs del formulario de /schedule-a-tow/ (campo fecha con name=email).
  - PMM: crear conversión "Form - Thank You" (URL de destino) en AW-18347302928 y, si hay acceso a GTM, trigger `submit_success` como respaldo; verificar con Tag Assistant llamada y formulario; documentar capturas en `log/`.
  - PMM: vincular GBP "Precision Automotive, Paint & Collision & Towing" a Ads (activo de ubicación) y unificar el horario del perfil a 7–22 (hoy directorios muestran L–V 7:30–17).
  - PMM: confirmar con el cliente los 5 claims condicionados (after-hours, flatbed, medium duty, winch/4x4, nombre Miller's) y el ticket promedio para recalcular el CPL máximo.
  - PMM: `/build-campaign` crea "Search - Towing KRV" y "Search - Marca" en pausa según `strategy.md` y `data/ads-search.md`.
  - PMM: pedir a Jhombis PageSpeed móvil de la home y de /light-medium-duty-towing/ (o `PAGESPEED_API_KEY`).
- **Riesgos**: si al 2026-10-13 no hay acceso a la web, se lanza igual la estructura nueva (la landing actual convierte al 37%) pero sin conversión de formulario y con el horario mal; se anota como bloqueo de Fase 2 y se escala a Jhombis. Si el cliente no define respuesta a leads, Fase 1 arranca con advertencia y se pide reporte de calidad de leads en el D30.

## Fase 1 — Lanzamiento Search
- **Fecha estimada**: activar 2026-10-14; condición evaluable 2026-10-21
- **Condición de paso**: campañas activas 7 días, RSA aprobados con fuerza ≥ "Buena", ≥1 conversión registrada en cada tipo (llamada desde anuncio y llamada web; formulario si ya existe)
- **Qué se lanza**: "Search - Towing KRV" $24/día (AG1 Tow Truck Near Me, AG2 Towing Lake Isabella & KRV, AG3 Roadside Assistance, AG4 RV & Trailer Towing) y "Search - Marca" $3/día; Maximizar conversiones sin tCPA; frase + exacta; presencia en radio 21 mi + 2 puntos de 8 mi; programación 6:30–22:30; el mismo día se pausa "ENHPRM Radius". PMax sigue pausada.
- **Riesgos**: caída de impresiones al salir de amplia (mercado rural). Si el gasto queda por debajo de $18/día en la primera semana, ampliar con variantes en frase ("tow truck", "towing service") antes de considerar amplia. Golden Empire (sede a 5 mi) puede aparecer en Auction Insights: revisar en D7.

## Fase 2 — Limpieza (D7 · D14 · D30)
- **Fechas**: 2026-10-21 · 2026-10-28 · 2026-11-13
- **Condición de paso**: tres revisiones hechas con `/weekly-review`, negativas aplicadas, keywords sin impresiones en 30 días pausadas, RSA peor por grupo reemplazado, reporte de calidad de leads del cliente recibido
- **Qué se revisa**: search terms → negativas (marcas de competidores nuevas, compra de trailers, aseguradoras); gasto sin conversión por keyword (umbral: $47 = P75 del benchmark, sobre todo "tow truck" y "roadside assistance" en frase); CPL por ad group contra el objetivo $21–31; IS de AG1/AG2 (meta 70–80%); Auction Insights; en D30, decisión sobre AG4 (si 0 conv, pausar hasta mayo) y sobre "24 hour" si el cliente confirmó cobertura nocturna. Landing estrella reescrita debe estar publicada antes del D30.

## Fase 3 — Optimización de puja (tCPA)
- **Fecha estimada**: **2026-11-26**. Cálculo: $27/día ÷ CPL benchmark $26 = 1,04 conv/día → 30 conv en ~29 días desde el lanzamiento (2026-11-12); +14 días porque el presupuesto está por debajo de 3× CPL/día (aprendizaje lento) → 2026-11-26. Con el CPL histórico de la cuenta ($37,5): 0,72 conv/día → 42 días → 2026-11-25 sin ajuste, 2026-12-09 con él. Rango realista: 2026-11-13 → 2026-12-09.
- **Condición de paso**: ≥30 conversiones en ventana de 30 días con tracking verificado (llamadas ≥30 s + formulario), CPL ≤ $47
- **Acción**: tCPA en "Search - Towing KRV" = CPA real observado (esperado $30–35), no el deseado; bajar 10% cada 2 semanas si se sostiene hasta $26; Marca se queda en Max. conversiones. Reajustar reparto por ad group según CPA. Evaluar ajustes por horario y dispositivo con datos de 60 días.
- **Si no se cumple en fecha**: revisar en este orden: (1) tasa de conversión de la landing (< 25% de llamadas por clic indica problema de landing o de respuesta del cliente), (2) IS perdido por presupuesto vs por ranking, (3) keywords que consumen sin convertir. NO forzar tCPA con menos de 30 conversiones. El histórico de la campaña vieja no cuenta para la ventana.

## Fase 4 — Remarketing
- **Fecha estimada**: revisión 2027-01-15
- **Condición de paso**: audiencia de visitantes ≥1.000 usuarios en 30 días (mínimo de Google para RLSA en Search)
- **Acción**: RLSA en observación en ambas campañas; Display de remarketing con exclusión de apps solo si la audiencia supera 100 usuarios y hay creatividades propias.
- **Realidad**: con ~60–80 clics/mes y sin tráfico orgánico (Semrush: 0), la audiencia de 30 días será de 100–200 usuarios. RLSA en Search **no va a habilitarse** con este presupuesto; Display de remarketing sí es posible con lista ≥100, pero con presupuesto residual ($1–2/día) y solo si el cliente entrega fotos. Se marca ⛔ hasta que el tráfico crezca (GA4 vinculado y audiencia creada desde Fase 0 para acumular desde ya).

## Fase 5 — Performance Max
- **Fecha estimada**: 2027-03-30 como muy pronto (mes 6 de la cuenta)
- **Condición de paso**: TODAS las de `knowledge/estrategias/pmax-cuando-y-como.md`: tCPA estable ≥4 semanas dentro de objetivo; ≥30 conv/mes verificadas (formulario + llamada ≥60 s); ciclo de limpieza D30 completado; assets propios (5+ fotos, logo, 1 video); landing ≥5% conversión con anti-spam; presupuesto PMax ≥3× CPA/día
- **Si no califica** (es lo esperado): con $825/mes, PMax tendría 20–30% = $5,5–8/día contra un mínimo de ~$78/día (3× CPA $26). **No califica por presupuesto**, y además hoy fallan tracking de formulario y assets. Qué haría falta: pauta ≥ $2.000/mes o CPA ≤ $3 (imposible en el nicho). Decisión: quedarse en Search + remarketing Display; reevaluar solo si el cliente confirma margen para escalar (PENDIENTE en brief). La campaña PMax existente sigue pausada; no borrarla (conserva historial).

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance actual. El cliente no tiene CRM (PENDIENTE confirmar). Sustituto desde D0: hoja compartida donde marque cada llamada/formulario como calificado o no, con fecha y hora, para cruzar con Ads en D30. Se reevalúa cuando exista registro de leads con GCLID (campos ocultos UTM+GCLID se añaden al formulario en Fase 0 si hay acceso).

## Pista paralela — Landing
| Ajuste (audit-site.md) | Fase | Fecha | Responsable | Bloqueante |
|---|---|---|---|---|
| Acceso de edición web + GTM, o contacto de quien edita | 0 | 2026-10-06 | Cliente | Sí |
| `/thank-you/` + Redirect en 7 formularios; conversión de formulario | 0 | 2026-10-10 | Cliente edita / PMM configura | Sí |
| Tag Assistant: llamada web + formulario | 0 | 2026-10-13 | PMM | Sí |
| Footer: horario 7 AM–10 PM en las 9 páginas | 0 | 2026-10-10 | Cliente | Sí |
| Bug IDs formulario /schedule-a-tow/ | 0 | 2026-10-10 | Cliente | No |
| Reescritura landing estrella `/light-medium-duty-towing/` (H1 "Tow Truck in Lake Isabella & the Kern River Valley", teléfono + ETA arriba, form 3 campos, comunidades, sellos, agregado 4,8★, 4 reseñas de grúa) | 2 | PMM redacta 2026-10-17; publicada antes del 2026-11-13 | PMM / Cliente | No (sí para pasar Fase 2) |
| Botón de llamada sticky en móvil | 2 | 2026-10-24 | Cliente | No, prioridad alta |
| Sellos AAA / NAPA / Gold Seal + "licensed & insured" (cuando confirme CHP) | 2 | 2026-10-24 | Cliente | No |
| `/roadside-assistance/` con H2 por subservicio | 2 | 2026-10-31 | Cliente | No |
| `/5th-wheel-towing/` y `/travel-trailer-towing/` con frase "we tow, we don't sell hitches" | 2 | 2026-10-31 | Cliente | No |
| Home: H1, agregado de reseñas, horario | 2 | 2026-10-31 | Cliente | No |
| Velocidad: hero WebP ≤120 KB, un solo hero por breakpoint, fuentes a 2 pesos, caché/CDN | 3 | 2026-11-30 | Cliente / hosting | No (pendiente medir PSI) |
| Fugas: menú reducido en landings pagadas, sin Quick Links duplicados | 3 | 2026-11-30 | Cliente | No |

## Pista paralela — LSA
- Aplica en principio: US, towing es categoría elegible, GBP con 4,8★ y ~850 reseñas (ventaja fuerte de ranking). Falta confirmar licencia (CHP / motor carrier permit), seguro y disposición al background check: **PENDIENTE cliente, respuesta antes del 2026-10-06**.
- Si confirma: 2026-10-06 iniciar solicitud → verificación 2026-10-20 a 2026-11-03 → presupuesto semanal aparte de los $825 (proponer $50–75/semana) y gestión de reseñas y tasa de respuesta desde el primer día.
- Si no confirma: se documenta como fase futura y no bloquea nada.

## Estacionalidad y ventanas
- **Pico**: mayo–septiembre (turismo del Kern River, campgrounds: es cuando AG4 trailers tiene sentido). **Valle**: noviembre–marzo. Lanzamos el 2026-10-14, entrando en temporada baja: esperar menos impresiones que las 620 de agosto–septiembre y no leerlo como fallo de la estructura.
- Invierno: nieve y cierres en Hwy 155/178 generan demanda de winch-out y recovery (AG3) y accidentes; conviene tener AG3 vivo en enero–febrero aunque rinda poco en octubre.
- AG4 (5th wheel / travel trailer): si en D30 sigue en 0 conversiones, pausar y reactivar el 2027-04-15 antes del pico.
- Ventana de tCPA: la ventana de 30 conv puede alargarse por la temporada baja; el rango 2026-11-13 → 2026-12-09 ya lo contempla con el +14 días.

## Historial de cambios
- 2026-09-29: creado a partir de strategy.md v1, audit-site.md (12/22), benchmark.md (27 cuentas) y brief.md.
