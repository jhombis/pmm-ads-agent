---
cliente: Spillane's Towing & Recovery
slug: spillanes-towing
fase_actual: 0
actualizado: 2026-10-01
---
# Checklist — Spillane's Towing & Recovery

Base: `knowledge/checklists/setup-cuenta.md`, adaptada a una **cuenta ya activa** (822-393-5903).
- Eliminado: LSA (no aplica) y la sección completa de PMax (no realista con $989/mes; ver roadmap Fase 5).
- Agregado: corrección inmediata de la campaña viva, pendientes del brief y pistas de landing y reputación.

## Fase 0 — Fundación (bloqueante)
### A. Corrección sobre la campaña viva (no espera al cliente)
- [x] (PMM) Cuenta vinculada al MCC de PMM (822-393-5903)
- [x] (PMM) Facturación activa (la cuenta gasta; verificar el método en la UI)
- [ ] (PMM) Lista de negativas universal PMM aplicada a nivel de cuenta: **2026-10-02**
- [ ] (PMM) Bloque Towing + `data/negatives-nicho.txt` aplicados (marca, competidores, AAA/aseguradoras, impound, bajo ticket, fuera de área): **2026-10-02**
- [ ] (PMM) Pausar `roadside assistance` (BROAD) y `spillane's towing` (BROAD): **2026-10-02**
- [ ] (PMM) Conversión "Llamada desde anuncio" con duración mínima 60 s: **2026-10-02**
- [ ] (PMM) "Website Calls" con duración mínima 60 s; decidir cuáles son primarias: **2026-10-02**
- [ ] (PMM) Conversiones secundarias (vistas, clics de botón) marcadas como secundarias, NO primarias
- [ ] (PMM) Verificar ubicación: radio de 12 mi alrededor de 44.490450, -73.111263, **solo presencia**, resto de países excluidos
- [ ] (PMM) Verificar red: solo búsqueda (socios y Display apagados)
- [ ] (PMM) Aplicación automática de recomendaciones DESACTIVADA
- [ ] (PMM) Exportar Auction Insights de 30 días → completar `competitors.md`
- [ ] (PMM) Google Tag verificado con Tag Assistant en spillanestowingrecovery.com (un tag, reemplazo de número OK, sin doble conteo)
- [ ] (PMM) Conversión "Clic en teléfono" (móvil) en la landing creada o verificada
- [ ] (PMM) GA4 vinculado y audiencia "Todos los visitantes" (ambos dominios, 540 días) creada
- [ ] (PMM) Campos ocultos UTM + GCLID en el formulario

### B. Landing (bloqueantes de `audit-site.md`)
- [ ] (PMM) Quitar el link "Google" (share.google) de contacto y footer: **2026-10-02**
- [ ] (PMM) H1 con servicio + zona y flota en el hero: **2026-10-06**
- [ ] (PMM) Form de 3 campos arriba en móvil: **2026-10-06**
- [ ] (PMM) Página `/thank-you/` + "Form Fill" por page-view, probada con Tag Assistant: **2026-10-06**
- [ ] (PMM) PageSpeed móvil medido (configurar `PAGESPEED_API_KEY` o score manual); corregir si es <40: **2026-10-06**

### C. Cliente (vence 2026-10-12)
- [ ] (Cliente) **Ticket promedio y margen** por tipo de servicio → recalcular el CPL máximo en `brief.md`
- [ ] (Cliente) **Proceso de respuesta a leads**: quién contesta de 11pm a 7am y en cuánto tiempo (define 24/7 o 6:00–23:00)
- [ ] (Cliente) **Acceso de PMM al Google Business Profile**; GBP verificado y con categoría principal correcta
- [ ] (PMM) GBP vinculado a Google Ads (activo de ubicación), tras recibir el acceso
- [ ] (Cliente) Confirmar los claims: años en operación, 21 camiones / 16 flatbeds, taller propio, licencia y seguro
- [ ] (Cliente) Servicios a evitar: lockout, llantas, jump start, long distance, heavy-duty
- [ ] (Cliente) Confirmar que (802) 216-3105 desvía a la línea principal (call tracking aprobado)
- [ ] (Cliente) 8–10 fotos reales de la flota y la sede
- [ ] (Cliente) Unificar el horario publicado (el sitio principal dice 7am–11pm)
- [ ] (Cliente) Destino de los envíos del formulario

## Fase 1 — Relanzamiento Search (2026-10-13)
- [ ] (PMM) 6 ad groups creados en la campaña existente según `strategy.md` (vía `/build-campaign`)
- [ ] (PMM) Keywords en frase; exacta para los top términos; las 7 BROAD actuales pausadas
- [ ] (PMM) 3 RSA por ad group, H1 pinneado, 15H/4D (`data/ads-search.md`), fuerza "Buena" o superior; claims no confirmados retirados
- [ ] (PMM) Negativas cruzadas entre ad groups (accident / winch / stuck / flatbed)
- [ ] (PMM) Programación según la respuesta del cliente (24/7 o 6:00–23:00)
- [ ] (PMM) Puja: Maximizar conversiones (sin tCPA), presupuesto $32.50/día
- [ ] (PMM) Extensiones: 4 sitelinks, 8 callouts, snippet de servicios, llamada, ubicación, imágenes propias
- [ ] (PMM) URLs finales verificadas (200, https, sin redirect)
- [ ] (PMM) Anuncios aprobados por políticas (revisar 24 h después)
- [ ] (PMM) Primera conversión registrada con la regla de 60 s

## Fase 2 — Limpieza
- [ ] (PMM) D7 **2026-10-20**: search terms revisados, negativas agregadas; keywords sin impresiones identificadas (no pausar aún)
- [ ] (PMM) D14 **2026-10-27**: search terms revisados; keywords con >$35 de gasto y 0 conversiones marcadas para revisión
- [ ] (PMM) D30 **2026-11-12**: search terms revisados; keywords con 0 impresiones en 30 días pausadas
- [ ] (PMM) D30: RSA de peor rendimiento por grupo reemplazado
- [ ] (PMM) D30: decidir si se fusionan AG2 y AG5 (<50 impresiones) y si se prueba "road service near me" en F3
- [ ] (Cliente) D30: reporte de calidad de leads (fecha, origen, ¿trabajo pagado?) recibido

## Fase 3 — Optimización de puja (~2026-12-08)
- [ ] (PMM) ≥30 conversiones en 30 días confirmadas (llamada ≥60 s + formulario)
- [ ] (PMM) CPA real comparado con el CPL máximo del brief (requiere ticket)
- [ ] (PMM) tCPA configurado = CPA real observado +10% (no el deseado)
- [ ] (PMM) Presupuesto reajustado según CPA, cuota perdida por presupuesto y capacidad del cliente
- [ ] (PMM) Ajustes de puja por horario evaluados con datos (noche vs día)

## Fase 4 — Remarketing (reevaluar 2027-02)
- [ ] (PMM) Audiencia de visitantes ≥1,000 usuarios en 30 días (hoy no es alcanzable)
- [ ] (PMM) RLSA: audiencia agregada a Search en observación
- [ ] (PMM) Display remarketing opcional ($3–5/día) con exclusión de apps

## Pista Landing (mejoras)
- [ ] (PMM) `/towing/`: 2026-10-27
- [ ] (PMM) `/accident-recovery/`: **2026-11-10** (antes de la nieve)
- [ ] (PMM) `/flatbed-towing/`: 2026-11-24
- [ ] (PMM + Cliente) Oferta concreta en hero y anuncios (tras confirmación)
- [ ] (Cliente → PMM) 4–6 reseñas reales con ciudad + fotos de flota en la landing: 2026-11-12

## Pista Landing GHL (`landings/README.md`)
- [ ] (Jhombis) Confirmar el dominio de las landings GHL (propuesto: go.spillanestowingrecovery.com)
- [ ] (Cliente/PMM) CNAME del subdominio a GHL y SSL activo
- [ ] (PMM) Formulario GHL (≤4 campos + ocultos gclid/utm_source/utm_campaign/utm_term) → `ghl.form_id` en los 3 specs y regenerar — **bloqueante QA**
- [ ] (PMM) Conversión de formulario: GTM (`tracking.gtm_id`) o AW-ID + label → regenerar — **bloqueante QA**
- [ ] (PMM) Conversión por clic en llamada (`conversion_label_call` o GTM)
- [ ] (PMM) Montar towing, accident-towing-winch-out y flatbed-towing + sus páginas de gracias en GHL
- [ ] (PMM) Verificación §7 de setup-gohighlevel.md (gclid de prueba, Tag Assistant, PageSpeed ≥70)
- [ ] (PMM) Actualizar las URLs finales en strategy.md cuando estén publicadas

## Pista Reputación
- [ ] (Cliente) Pedido de reseña por SMS o QR a cada trabajo voluntario: desde 2026-10-13
- [ ] (PMM) Responder reseñas negativas en el GBP (requiere acceso)
- [ ] (Cliente) Decidir si se separa la operación de impound (perfil o número aparte)
- [ ] Hito 3.5★ (seller ratings) · Hito 3.8★ (condición de PMax)

## Fase 6 — Conversiones offline (futuro, requiere CRM)
- [ ] (Cliente) Exportar trabajos cerrados desde Towbook con GCLID
- [ ] (PMM) Importación de conversiones offline configurada

## Recurrente (semanal, `/weekly-review`)
- [ ] Search terms → negativas
- [ ] Gasto vs presupuesto mensual ($989)
- [ ] CPA vs objetivo ($35 F1 → $25 F2); tendencia 7d vs 28d
- [ ] CPC (meta ≤$7) y cuota perdida por ranking (meta <25%)
- [ ] Anuncios rechazados / limitados
- [ ] Cuota de impresiones perdida por presupuesto (en tormentas)
- [ ] Calidad de leads reportada por el cliente
- [ ] Rating del GBP
- [ ] Log escrito en `log/YYYY-MM-DD.md`
