---
cliente: Hemet Affordable Burial and Cremation
slug: hemet-affordable-burial-cremation
fase_actual: 0
actualizado: 2026-10-01
---
# Checklist — Hemet Affordable Burial and Cremation

Base: `knowledge/checklists/setup-cuenta.md`, adaptado a una **cuenta ya activa** (751-429-2721). Se eliminaron Display remarketing (el Display ya probó 0 conversiones) y la configuración de PMax (no califica; ver roadmap Fase 5). LSA queda solo como verificación.
Responsables: PMM · Cliente · Jhombis (decisión).

## Fase 0 — Fundación / limpieza (bloqueante para Fase 1) · meta 2026-10-12
### Quick wins (día 1–2)
- [ ] (PMM) **CRÍTICO: instalar el Google Tag (AW-) en todo el sitio** (WordPress). Hoy no hay ninguno (audit-site.md)
- [ ] (PMM) Snippet de número de reenvío (Website Calls) funcionando con gclid
- [ ] (PMM) Formulario de Elementor → redirección a /thank-you/ con la conversión Form Fill
- [ ] (PMM) Pausar "Responsive Display - $300/mo" (0 conv en 90 días)
- [ ] (PMM) Lista "PMM Universal" aplicada a nivel de cuenta **sin** `cheapest`, `county` ni `rental`
- [ ] (PMM) Lista de nicho "Funeral - Hemet" (`data/negatives-nicho.txt`) aplicada a nivel de cuenta
- [ ] (PMM) Geo de la campaña actual revisada: solo presencia, ciudades del brief, resto de países excluido
### Cuenta y configuración
- [x] (PMM) Cuenta vinculada al MCC de PMM (Windsor la ve: "Premium Local Listings 004029")
- [x] (PMM) Facturación activa (la cuenta gasta)
- [ ] (PMM) Aplicación automática de recomendaciones DESACTIVADA (confirmar)
- [ ] (PMM) Socios de búsqueda y Display apagados en la campaña Search (confirmar)
### Tracking
- [ ] (PMM) "Calls from Ads" con duración mínima **90 s** (hoy son el 70% de las conversiones)
- [ ] (PMM) "Form Fill" probado con Tag Assistant; dispara solo en la página de gracias
- [ ] (PMM) "Website Calls" (número de reenvío en el sitio) verificado en todas las páginas
- [ ] (PMM) "Clicks to call" y las acciones locales confirmadas como **secundarias**
- [ ] (PMM) Google Tag en todas las páginas del sitio (confirmar en /audit-landing)
- [ ] (PMM) GA4 vinculado y audiencia "Todos los visitantes" creada (acumula para Fase 4)
- [ ] (PMM) Campos ocultos UTM + GCLID en el formulario (si la plataforma lo permite)
### GBP
- [ ] (Cliente) GBP **nuevo** verificado, con categoría principal "Funeral home"
- [ ] (Cliente) Acceso de PMM al GBP nuevo
- [ ] (PMM) GBP nuevo vinculado como activo de ubicación; ficha de Inland Memorial desvinculada
- [ ] (Cliente) Ficha de Inland Memorial cerrada o diferenciada correctamente (evitar duplicado en la misma dirección)
### Landing (ver pista Landing del roadmap)
- [x] (PMM) `/audit-landing` corrido (2026-10-01, 11/22)
- [ ] (PMM) Bloqueantes de audit-site.md resueltos (tag, página de gracias, reenvío, sin tráfico a la home)
- [x] (Cliente) GPL publicado online (PDF 2026-03-25); los precios de los anuncios coinciden
- [ ] (PMM) Score PageSpeed móvil real (la API devolvió 429 por cuota agotada)
### Operación y negocio
- [ ] (Cliente) Quién contesta de noche (director vs answering service) y tiempo de respuesta a formularios
- [x] (Cliente) Precios de servicios completos publicados en /pricing ($2,495–$2,995)
- [ ] (Cliente) Margen por caso por tipo de servicio → CPL máximo real (hoy supuesto $60)
- [ ] (Jhombis) Confirmar relación con Sunflower Crematory / cuentas Sunflower del MCC (posible competencia en la misma subasta)
- [ ] (Cliente) Capacidad de casos/mes
- [ ] (Jhombis) Presupuesto confirmado: $1,500 de pauta vs "$2800" del nombre de la cuenta
- [ ] (Jhombis) Aprobar agregar Valle Vista, East Hemet y Homeland a la geo
- [ ] (Cliente) Hoja mensual de leads → casos (fecha, teléfono, cerró sí/no, tipo de servicio)
### Pistas paralelas
- [ ] (PMM) LSA: verificar si "funeral home" está disponible en Riverside County (2026-10-03); cerrar pista si no
- [ ] (Cliente) ¿Personal hispanohablante 24/7? Decide la pista Español

## Fase 1 — Reestructura Search · publicar 2026-10-13
- [ ] Campaña "Search | Funeral & Cremation | Hemet Valley" creada (4 ad groups) según `strategy.md`
- [ ] Campaña "Search | Brand" creada; términos de marca como negativa en la genérica
- [ ] Negativas cruzadas entre ad groups aplicadas (ver strategy.md)
- [ ] Red: solo Búsqueda; socios y Display apagados
- [ ] Ubicación: presencia; ciudades del brief (+ zonas no incorporadas si se aprueba); resto de países excluido
- [ ] Programación 24/7 (contestan 24/7 con una persona)
- [ ] Puja: genérica Maximizar conversiones (sin tCPA); marca Maximizar clics con CPC máx. $3
- [ ] Keywords en frase; exacta para los top términos; **cero amplia**
- [ ] 3 RSA por ad group, H1 pinneado, 15H/4D (`data/ads-search.md`), fuerza "Buena" o superior
- [ ] Precios de los anuncios verificados contra el GPL
- [ ] Extensiones: 6 sitelinks, 8 callouts, snippet "Services", llamada, ubicación (GBP nuevo)
- [ ] URLs finales verificadas (200, https, sin redirect)
- [ ] Presupuestos: genérica $44/día, marca $5/día
- [ ] Campaña antigua "ENHPRM Radius" pausada (no borrada)
- [ ] Anuncios aprobados por políticas (revisar 24 h después)
- [ ] Primera conversión registrada con la configuración nueva

## Fase 2 — Limpieza (D7 2026-10-20 · D14 2026-10-27 · D30 2026-11-12)
- [ ] D7: search terms revisados, negativas agregadas
- [ ] D7: keywords sin impresiones identificadas (no pausar aún)
- [ ] D14: search terms revisados, negativas agregadas
- [ ] D14: keywords con >$100 de gasto y 0 conversiones marcadas para revisión
- [ ] D30: search terms revisados, negativas agregadas
- [ ] D30: keywords con 0 impresiones en 30 días pausadas
- [ ] D30: RSA con peor rendimiento por grupo reemplazado
- [ ] D30: hoja de leads → casos del cliente recibida (calidad y mezcla directo vs completo)
- [ ] D30: meta F1 evaluada: ≥12 conv/mes, CPA ≤ $100, desperdicio <10%

## Fase 3 — Optimización de puja (checkpoint 2027-01-15; requiere ~$2,500/mes o más conversión)
- [ ] ≥30 conversiones en 30 días confirmadas
- [ ] tCPA configurado = CPA real observado (no el deseado)
- [ ] Presupuesto reajustado según CPA y capacidad del cliente
- [ ] Ajustes de puja por horario/dispositivo evaluados con datos

## Fase 4 — Remarketing (bloqueada por volumen de tráfico)
- [ ] Audiencia de visitantes ≥1,000 usuarios en 30 días
- [ ] RLSA: audiencia agregada a Search en observación

## Fase 5 — Performance Max (no califica; reevaluar 2027-01-15)
- [ ] Condiciones de entrada de `pmax-cuando-y-como.md` verificadas (hoy fallan 4 de 6)

## Fase 6 — Conversiones offline (futuro, requiere CRM)
- [ ] Cliente comparte leads cerrados con GCLID
- [ ] Importación de conversiones offline configurada

## Pistas paralelas
- [ ] (Cliente / PMM) Landing de servicios completos con precio "desde" y fotos reales · 2026-11-12
- [ ] (Cliente / PMM) /cremation y /burial: H1 con ciudad, precios arriba, formulario arriba, email opcional · 2026-11-12
- [ ] (Cliente) Testimonios en las páginas de servicio · 2026-11-12
- [ ] (Cliente / PMM) Landing /veterans/ (paquetes de $1,250 / $2,500 / $4,000) · F2–F3
- [ ] (Cliente) 10 reseñas en el GBP nuevo · 2026-12-31
- [ ] (Cliente) Fotos reales de capilla e instalaciones (para extensiones de imagen y una futura PMax)
- [ ] (PMM) Ad group en español "Funeraria" · desde 2026-11-12, solo si hay personal hispanohablante

## Recurrente (semanal, /weekly-review)
- [ ] Search terms → negativas (vigilar competidores nuevos y fuera de área)
- [ ] Gasto vs presupuesto mensual ($1,500)
- [ ] CPA vs objetivo ($100 en F1 → $73 ±20%); tendencia 7d vs 28d
- [ ] Anuncios rechazados o limitados (ojo con políticas de precios)
- [ ] Impression share perdido por presupuesto y por ranking
- [ ] Calidad de leads reportada por el cliente
- [ ] Log escrito en `log/YYYY-MM-DD.md`
