---
cliente: 290 Tow and Recovery
slug: 290-tow-recovery
fase_actual: 0
actualizado: 2026-09-24
---
# Checklist — 290 Tow and Recovery

Base: `knowledge/checklists/setup-cuenta.md`, ajustada al cliente. **(B)** = bloqueante para pasar de fase. Responsable entre paréntesis. /weekly-review lo actualiza.
**Contexto:** la cuenta ya está activa desde el 17/09 con la configuración PLL. La Fase 1 = reestructurar según `strategy.md`.

## Fase 0 — Fundación (D0 2026-09-24 → 2026-09-29)
### Cuenta
- [x] (PMM) Cuenta vinculada al MCC de PMM: 213-019-5545, visible en Windsor
- [ ] (PMM) Facturación verificada. Está gastando, así que es probable que esté activa; confirmar el método de pago y quién paga (PLL)
- [ ] **(B)** (PMM) Aplicación automática de recomendaciones DESACTIVADA
- [x] (PMM) Red: solo Búsqueda; socios y Display apagados. Ya está así: mantenerlo
- [ ] **(B)** (PMM) Lista universal PMM aplicada a nivel de cuenta (sin excluir "tow truck" ni "towing")
- [ ] **(B)** (PMM) Lista de nicho + cliente aplicada (`data/negatives-nicho.txt`)
- [ ] (Jhombis) Decidir qué hacer con la campaña actual durante la F0: dejarla, pausarla o cargar solo las negativas

### Tracking
- [x] (PMM) Google Tag en todas las páginas: GTM-WBX4RZ9K, G-KH9SFWZK66, AW-18397446767 (auditoría del 2026-09-23)
- [ ] **(B)** (PMM) Confirmar que AW-18397446767 corresponde a la cuenta 213-019-5545
- [ ] **(B)** (PMM) "Calls from Ads" con duración mínima de **60 s**, verificada en la UI
- [ ] **(B)** (PMM) "Website Calls" (clic en `tel:` desde móvil) probada con Tag Assistant
- [ ] **(B)** (PMM) "Form Fill" probada con Tag Assistant, disparando en `/thank-you/`
- [ ] **(B)** (PMM) Verificar que la misma llamada no cuenta doble (Calls from Ads + Website Calls)
- [ ] (PMM) Conversiones secundarias (vistas, scroll, direcciones) marcadas como secundarias
- [ ] (PMM) GA4 vinculado a Ads y audiencia "Todos los visitantes" importada
- [ ] (PMM) Campos ocultos UTM + GCLID en el formulario Elementor

### Landing (ver audit-site.md)
- [ ] **(B)** (PMM) CTA "Get a Free Quote" + "Call Now" en `/exotic-vehicle-towing/`. Sin esto, AG5 queda en pausa
- [ ] **(B)** (PMM) `/thank-you/` + redirect del formulario
- [ ] (PMM) H1 del home: "24/7 Towing & Tow Truck Service in Fredericksburg, TX"; "45-minute radius" → 40 mi
- [ ] (PMM) Validar el volumen local en Keyword Planner (40 mi de 78624) y actualizar `data/keywords.csv`

### Cliente
- [ ] **(B)** (Cliente) Proceso de respuesta a leads: quién contesta de noche y en fin de semana, en cuánto tiempo, qué pasa si no contesta (buzón o desvío)
- [x] (Cliente) Call tracking aprobado (número de reenvío de Google). Confirmado en /onboard
- [ ] (Cliente) Ticket promedio y margen por servicio → recalcular el CPL máximo (hoy ~$14 provisional; benchmark $14.57)
- [ ] (Cliente) Servicio estrella y servicio a evitar
- [ ] (Cliente) ¿Atiende Boerne / Fair Oaks Ranch / Bulverde? (decide las exclusiones geo)
- [ ] (Cliente) ¿Tiene flatbed? ¿Remolca RV y motos? (activa keywords de AG5 y F2)
- [ ] (Cliente) Número de licencia TDLR + seguro (copy y LSA)
- [ ] (Cliente) Ofertas sostenibles: ¿confirma "upfront price on the phone"?
- [x] (PMM) Historial de la cuenta leído (2026-09-23, Windsor): 6 días, $165.57, 0 conversiones, 43% de desperdicio

## Fase 1 — Reestructuración Search (2026-09-30 → 2026-10-07)
- [ ] (PMM) Campaña reestructurada según `strategy.md`: 7 ad groups, AG5 en pausa hasta arreglar su landing
- [ ] (PMM) 10 keywords en amplia de la plantilla PLL eliminadas
- [ ] (PMM) Ubicación: presencia solamente; radio de 40 mi recentrado en 30.2752, -98.8720; exclusiones de San Antonio según la respuesta del cliente
- [ ] (PMM) Programación 24/7 (zona horaria de la cuenta: LA)
- [ ] (PMM) Puja: Maximizar clics con tope de CPC de $6.50, $27/día
- [ ] (PMM) Keywords en frase + exacta para los términos principales, sin amplia
- [ ] (PMM) 3 RSA por ad group, H1 pinneado, 15H/4D, fuerza "Buena" o superior (`data/ads-search-towing.md`)
- [ ] (PMM) Assets: 4 sitelinks, 8 callouts, snippet de servicios, llamada con número de reenvío. Ubicación cuando exista el GBP
- [ ] (PMM) URLs finales verificadas (200, https, sin redirect)
- [ ] (PMM) Negativas por ad group (ver strategy.md)
- [ ] (PMM) Anuncios aprobados por políticas (revisar 24 h después)
- [ ] **(B)** (PMM) Primera conversión registrada y cruzada con una llamada real del cliente

## Fase 2 — Limpieza
- [ ] (PMM) D7 (2026-10-07): search terms → negativas; keywords sin impresiones identificadas; gasto <70% del presupuesto → abrir AG7 a frase
- [ ] (PMM) D14 (2026-10-14): search terms → negativas; AG5/AG6 con más de $100 y 0 llamadas → pausar; AG7 >20% del gasto → pausar
- [ ] (PMM) D14: evaluar el paso a Maximizar conversiones (≥15 conversiones o 14 días con tracking OK y CPC ≤ $7)
- [ ] (PMM) D30 (2026-10-30): search terms → negativas; keywords con 0 impresiones pausadas; RSA peor por grupo reemplazado
- [ ] (Cliente) D30: calidad de las llamadas reportada (hoja compartida: llamada → trabajo sí/no → ticket)

## Fase 3 — Optimización de puja (tCPA ~2026-11-11)
- [ ] (PMM) ≥30 conversiones en 30 días confirmadas
- [ ] (PMM) tCPA = CPL real de 30 días × 1.1 (no el deseado)
- [ ] (PMM) Presupuesto revisado según CPL y capacidad del cliente
- [ ] (PMM) Ajustes por dispositivo evaluados con datos

## Fase 4 — Remarketing (probablemente no califica por volumen)
- [ ] (PMM) Audiencia de visitantes ≥1,000 en 30 días. Revisar mensualmente en GA4

## Fase 5 — Performance Max
**Bloqueada:** $27/día < ~$44/día de mínimo; sin assets propios; sin GBP. Se reevalúa el 2026-12-29 o si sube el presupuesto.
- [ ] (Cliente) Fotos reales de las grúas y del equipo (5+) y un video corto: sirven para PMax y para el sitio
- [ ] (Jhombis/PLL) Evaluar si el fee permite ≥$1,300/mes de pauta

## Fase 6 — Conversiones offline (futuro, requiere CRM)
- [ ] (Cliente) Registro de trabajos con fecha, hora y teléfono para cruzar con las llamadas

## Pista GBP + LSA
- [ ] **(B para Maps/LSA)** (Cliente) Crear y verificar el GBP (área de servicio, categoría "Towing service"). Objetivo: ~2026-10-15
- [ ] (PMM) Vincular el GBP a Ads y activar el activo de ubicación
- [ ] (Cliente) Proceso de reseñas después de cada servicio (los competidores tienen 70–157)
- [ ] (PMM) Solicitud LSA (licencia TDLR, seguro, background check). Objetivo: ~2026-10-15
- [ ] (PMM) LSA verificado y con presupuesto semanal definido. Objetivo: ~2026-11-12

## Recurrente (semanal, /weekly-review)
- [ ] Search terms → negativas
- [ ] Gasto contra los $825 mensuales
- [ ] CPL contra el objetivo ($14.57; rango $11.70–$17.50); tendencia 7 d contra 28 d
- [ ] % de gasto de AG7 roadside y de AG5/AG6
- [ ] Anuncios rechazados o limitados
- [ ] Impression share perdido por presupuesto y por ranking
- [ ] Calidad de las llamadas reportada por el cliente
- [ ] Log en `log/YYYY-MM-DD.md`
