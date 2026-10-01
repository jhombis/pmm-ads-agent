---
cliente: Jerry's Auto Body Solutions & Towing Service
slug: jerrys-towing-wesley-chapel
fase_actual: 0
actualizado: 2026-10-01
---

# Checklist — Jerry's Auto Body Solutions & Towing Service

Base: `knowledge/checklists/setup-cuenta.md`, adaptada a una cuenta **que ya está activa desde el 22/08/2026**.
Leyenda: ✅ hecho · 🔄 en curso / parcial · ⬜ pendiente · **[B]** bloqueante de fase · *(evidencia)* de dónde sale el estado.
Fase 5 (PMax) eliminada: no califica con este presupuesto (ver `roadmap.md`).

## Fase 0 — Fundación / saneamiento
### Cuenta
- ✅ (PMM) Cuenta 523-801-4243 visible en el MCC de PMM *(Windsor: "Premium Local Listings 004043")*
- ✅ (PMM) Facturación activa *(gasta desde el 22/08)*
- ⬜ **[B]** (PMM) Aplicación automática de recomendaciones DESACTIVADA (revisar en la UI)
- ⬜ **[B]** (PMM) Ubicación = **Presencia**; radio de 20 mi desde 3645 New River Rd; resto de países excluidos *(search terms de NY/OH/AZ sugieren que no)*
- ✅ (PMM) Red: solo Búsqueda *(ad_network_type = SEARCH)*

### Medición
- ✅ (PMM) Google Tag en el sitio *(AW-18347420212, GTM-5VX6B6KS, GT-5DDGBBK6; sitio de una sola página)*
- 🔄 **[B]** (PMM) Conversión "Formulario" probada con Tag Assistant *(existe "Form Fill": 6 conv.; sin página de gracias, disparador sin verificar)*
- ⬜ **[B]** (PMM) Crear `/thank-you/` y redirigir el formulario de Elementor ahí; mover Form Fill a esa página
- 🔄 **[B]** (PMM) Conversión "Llamada desde anuncio" con duración mínima de 60 s *(existe "Calls from Ads": 6 conv.; duración sin verificar)*
- 🔄 **[B]** (PMM) Conversión "Clic en teléfono" en landing → **debe ser secundaria** si es un clic *(existe "Website Calls": 9 conv., primaria; tipo sin verificar)*
- ⬜ (PMM) Conversiones secundarias marcadas como secundarias, NO primarias
- ⬜ (PMM) GA4 vinculado y audiencia "Todos los visitantes" importada
- ⬜ (PMM) Campos ocultos UTM + GCLID en el formulario

### Negativas
- ⬜ **[B]** (PMM) Lista universal PMM aplicada a nivel de cuenta, **con las excepciones** de este cliente (cheapest, insurance claim, "phone number" suelto, county) → `data/negatives-nicho.txt` · *requiere OK de Jhombis*
- ⬜ **[B]** (PMM) Lista del nicho + competidores + fuera de área aplicada (mismo archivo) · *requiere OK*
- ⬜ (PMM) Negativas a nivel de ad group para que los grupos no se crucen (`strategy.md`)

### Landing
- 🔄 (PMM) Landing aprobada por /audit-landing: **11/22, requiere ajustes**. El bloqueante es la página de gracias (arriba).
- ⬜ (PMM) H1 "24/7 Towing in Wesley Chapel, FL"
- ⬜ (PMM) `tel:+18133810435` normalizado + botón de llamada fijo en móvil
- ⬜ (PMM) Formulario de 3 campos (Nombre, Teléfono, Ubicación del vehículo)
- ⬜ (PMM) PageSpeed móvil medido (falta `PAGESPEED_API_KEY`)

### Cliente (vía Jhombis)
- ⬜ (Cliente) Ticket promedio, margen y tasa de cierre → recalcular el CPL máximo *(bloquea la Fase 3, no la 1)*
- ⬜ (Cliente) Proceso de respuesta a leads: quién contesta, en cuánto tiempo, formularios → ¿a quién llegan? (hoy a un Gmail)
- ⬜ (Cliente) ¿Alguien contesta entre 0 y 6 h? → horario 24/7 o 6:00–23:00
- ⬜ (Cliente) ¿Contestan en español? → activa o pausa Grúa ES *(bloquea solo ese ad group)*
- ⬜ (Cliente) Google Business Profile: ¿existe, verificado, categoría "Towing service", acceso para PMM? *(no encontrado en búsqueda)*
- ⬜ (PMM) GBP vinculado a Google Ads (activo de ubicación) *(depende del anterior)*
- ⬜ (Cliente) Radio real de servicio (¿incluye Tampa ciudad, Brandon, Plant City?)
- ⬜ (Cliente) ¿Medium-duty (box trucks)? ¿Carrocería? ¿Lockout? ¿Remolque de RV?
- ⬜ (Cliente) "Licensed & insured", años en el negocio, fotos reales de las grúas
- ⬜ (Cliente) Número de seguimiento / call tracking aprobado

### LSA (pista paralela)
- ⬜ (PMM) Verificar si la categoría Towing está habilitada en LSA para 33543 *(10/03)*
- ⬜ (PMM) Si aplica y hay GBP: iniciar solicitud LSA *(10/06)*

## Fase 1 — Relanzamiento Search reestructurado
- ✅ Campaña Search creada *(plantilla ENHPRM; se reestructura, no se recrea)*
- ⬜ Renombrar campaña → *Towing - Search - Radius*
- ⬜ Pausar: `Towing Service` (B), `tow company` (F), `tow truck company` (F), `servicio de grua cerca de mi en español` (B), `servicio de grua near me` (B)
- ⬜ Renombrar "Ad group 1 - English" → **Towing Near Me**; broad → frase + exacta (pausar las broad al mismo tiempo)
- ⬜ Crear ad groups **Cheap Towing**, **Roadside Assistance**, **Wesley Chapel Towing**
- ⬜ Renombrar "Ad group 2 - Spanish" → **Grúa ES**; frase; activar o pausar según la regla
- ⬜ Programación de anuncios según la respuesta del cliente (24/7 o 6:00–23:00)
- ✅ Puja: Maximizar conversiones (sin tCPA) *(confirmado)*
- ⬜ Si la medición limpia deja <15 conv./mes → Maximizar clics con tope de CPC de $10 (CLAUDE.md #6)
- ⬜ 1 RSA por ad group (máx. 2, CLAUDE.md #4), H1 pinneado, 15H/4D, fuerza "Buena" o superior (variante A de `data/ads-search.md`) *(hoy: 1 RSA por grupo, GOOD / EXCELLENT)*
- ⬜ Extensiones: 4 sitelinks, 8 callouts, snippet de Servicios, llamada, ubicación (si hay GBP)
- ⬜ URLs finales verificadas (200, https, sin redirect)
- ✅ Presupuesto diario $25 *(confirmado)*
- ✅ Anuncios actuales aprobados *(APPROVED)*
- ⬜ Anuncios nuevos aprobados (revisar 24 h después)
- ✅ Primera conversión registrada *(25/08)*
- ⬜ **[B]** ≥1 conversión **verificada** en la estructura nueva

## Fase 2 — Limpieza (D7 10/13 · D14 10/20 · D30 11/05)
- ✅ Revisión inicial (día ~38 de la cuenta) hecha: `log/2026-09-29.md`, negativas propuestas
- ⬜ D7: search terms revisados, negativas agregadas
- ⬜ D7: keywords sin impresiones identificadas (no pausar aún)
- ⬜ D14: search terms revisados, negativas agregadas
- ⬜ D14: keywords con gasto mayor a $80 y 0 conversiones marcadas para revisión
- ⬜ D30: search terms revisados, negativas agregadas
- ⬜ D30: keywords con 0 impresiones en 30 días pausadas
- ⬜ D30: en Towing Near Me, pausar el peor de los 2 RSA solo si la diferencia es clara (con <50 clics es ruido)
- ⬜ D30: reporte de calidad de leads del cliente recibido (≥50% reales)
- ⬜ Vigilar la hora 5 (clics sin conversión) y el gasto diario menor a $20

## Fase 3 — Optimización de puja (⛔ bloqueada por presupuesto)
- ⬜ Propuesta comercial de upgrade a ~$35/día en medios con datos de la Fase 2 *(Jhombis)*
- ⬜ ≥30 conversiones en 30 días confirmadas
- ⬜ tCPA configurado = CPA real observado (no el deseado)
- ⬜ Presupuesto reajustado según CPA y capacidad del cliente
- ⬜ Ajustes de puja por horario evaluados con datos (≥60 conv.)
- ⬜ Ad groups Medium-Duty / Collision si el cliente los confirmó

## Fase 4 — Remarketing (no realista a corto plazo)
- ⬜ Audiencia GA4 "todos los visitantes" importada (desde ya)
- ⬜ Audiencia de visitantes ≥1,000 usuarios en 30 días
- ⬜ RLSA en observación en Search

## Fase 6 — Conversiones offline (futuro, requiere CRM)
- ⬜ Paso intermedio: hoja compartida donde el cliente marca qué leads terminaron en servicio
- ⬜ Cliente comparte lista de leads cerrados con GCLID
- ⬜ Importación de conversiones offline configurada

## Recurrente (semanal, /weekly-review)
- ⬜ Search terms → negativas
- ⬜ Gasto vs presupuesto mensual (~$760)
- ⬜ CPA vs objetivo ($30–40); tendencia 7d vs 28d
- ⬜ Anuncios rechazados / limitados
- ⬜ Impression share perdido por presupuesto y por ranking *(baseline: 25.5% / 51.9%)*
- ⬜ Calidad de leads reportada por el cliente
- ⬜ Log escrito en `log/YYYY-MM-DD.md`
- ⬜ Temporada de huracanes (hasta el 30/11): subir el presupuesto temporalmente después de tormentas, con OK
