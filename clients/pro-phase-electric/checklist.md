---
cliente: Pro Phase Electric
slug: pro-phase-electric
fase_actual: 0
actualizado: 2026-09-23
---
# Checklist — Pro Phase Electric

Generado por /roadmap desde `knowledge/checklists/setup-cuenta.md`. **B** = bloqueante de la fase. /weekly-review lo mantiene.
Cuenta 758-301-1023 · campaña actual 24208591381 (Max. clics, se pausa en F1).

## Fase 0 — Fundación + contención (bloqueante para lanzar Search NWA)
### Cuenta
- [x] (PMM) Cuenta en el MCC de PMM — visible como "Premium Local Listings 004049 ($1500 Pro Phase Electric)"
- [x] (PMM) Facturación activa — la cuenta gasta desde el 11-sep
- [ ] **B** (PMM) Aplicación automática de recomendaciones DESACTIVADA (verificar)
- [x] (PMM) Acceso a la API (`google-ads.yaml`) — OK 23-sep. Pasar a variables de entorno para sesiones futuras

### Contención en la campaña actual
- [x] (PMM) Quitadas 15 negativas heredadas que bloqueaban servicios o el área (vista, car, estimate, free…) — 22-sep, ver log
- [ ] **B** (PMM) Importar `data/2026-09-22-negatives-editor.csv` (103 negativas: utilities, competidores, DIY, universal)
- [ ] (PMM) Pausar las keywords broad "home electrical", "electrical services", "electrical contractors" y "home electrical services"
- [ ] (PMM) Techo de CPC de $12 (Max. clics)
- [x] (PMM) Socios de búsqueda y Display apagados; ubicación = Presencia — verificado vía API 23-sep
- [ ] (PMM) Programación L–D 5:00–16:00 en la campaña actual

### Tracking
- [ ] **B** (PMM) Google Tag verificado en todas las páginas (el cliente dice que está; confirmar el ID y el acceso)
- [ ] **B** (PMM) Conversión "Formulario" (Get a Free Quote: home + /contact-us/) con página de gracias o evento, probada con Tag Assistant
- [ ] **B** (PMM) Conversión "Llamadas desde el sitio" (número de reenvío de Google) creada y probada
- [ ] (PMM) Conversión "Clic en teléfono" (`tel:`) en móvil
- [~] (PMM) "Calls from Ads" existe; **verificar duración mínima de 60 s**
- [ ] (PMM) Conversiones secundarias como secundarias (no primarias)
- [ ] (PMM) GA4 vinculado (Windsor no tiene una propiedad de este dominio conectada)
- [ ] (PMM) Campos ocultos UTM + GCLID en el formulario

### Negativas
- [ ] (PMM) Lista "PMM Universal" a nivel cuenta (hoy como negativas de campaña vía CSV; pasar a lista cuando haya API)
- [ ] (PMM) Lista "pro-phase-electric nicho" (`data/negatives-nicho.txt`) aplicada a Search NWA
- [ ] (PMM) Limpiar la plantilla heredada de la campaña actual (palabras sueltas en broad, nombres de Grand Junction). No aplica si se pausa en F1

### Landing
- [ ] **B** (PMM) Score de PageSpeed móvil (si es <40, bloqueante)
- [ ] **B** (Jhombis) Captura móvil de la home: formulario y botón de llamada visibles
- [ ] (PMM/Cliente) Decir quién edita el sitio (PENDIENTE en el brief)

### Cliente
- [ ] **B** (Cliente) Proceso de respuesta: quién contesta de 5 a 16, tiempo de respuesta, qué pasa con el buzón
- [ ] **B** (Cliente) Aceptar el número de reenvío de Google (call tracking)
- [ ] (Cliente) Acceso de gestor al GBP para PMM (el perfil existe: widget 4.9 ★ en el sitio)
- [ ] (PMM) GBP vinculado a Google Ads (activo de ubicación), después del acceso
- [ ] (Cliente) Horario del GBP y los directorios = L–D 5:00–16:00 (hoy publican L–V 8–17)
- [ ] (Cliente) Ticket y margen de un cambio de panel y de una instalación EV → CPL máximo (antes de Fase 2)
- [ ] (Cliente) Confirmar el área: ¿Siloam Springs, Gentry y el oeste de Benton? ¿Madison completo o solo Huntsville?
- [ ] (Cliente) Confirmar si instala generadores (hoy es negativa)
- [ ] (Cliente) Número de licencia de Arkansas
- [ ] (PMM) LSA: **en espera** (el cliente dijo "No"). Reabrir si cambia

## Fase 1 — Lanzamiento Search NWA
- [ ] (PMM) /build-campaign: "Search NWA" con 8 ad groups (6 activos + Paneles y EV pausados) según `strategy.md`, creada en pausa
- [ ] (PMM) Red: solo Búsqueda; socios y Display apagados
- [ ] (PMM) Ubicación: Presencia; condados de Benton y Washington + Huntsville; resto excluido
- [ ] (PMM) Programación L–D 5:00–16:00
- [ ] (PMM) Puja: Max. conversiones sin tCPA; $27/día
- [ ] (PMM) Keywords en frase + exacta (101); ninguna broad
- [ ] (PMM) 3 RSA por ad group, H1 pinneado, 15 headlines y 4 descripciones (`data/ads-search-nwa.md`), fuerza "Buena" o superior
- [ ] (PMM) Extensiones: 5 sitelinks, 8 callouts, snippet, llamada (5–16), imágenes propias; ubicación cuando haya GBP
- [ ] (PMM) Negativas de enrutamiento por ad group (General, Repair)
- [ ] (PMM) URLs finales verificadas (200, https, sin redirect)
- [ ] **B** (Jhombis) Revisión y activación; pausar la campaña actual el mismo día
- [ ] (PMM) Anuncios aprobados (revisar a las 24 h)
- [ ] **B** (PMM) Primera conversión **del sitio** registrada

## Fase 2 — Limpieza (D7 08-oct · D14 15-oct · D30 31-oct) + Paneles/EV
- [ ] D7: search terms revisados, negativas agregadas
- [ ] D7: keywords sin impresiones identificadas (no pausar aún)
- [ ] D14: search terms revisados, negativas agregadas
- [ ] D14: keywords con >$100 de gasto (2× CPL) y 0 conversiones marcadas para revisión
- [ ] D14+: landings de Paneles y EV auditadas → activar esos ad groups y sus sitelinks
- [ ] D30: search terms revisados, negativas agregadas
- [ ] D30: keywords con 0 impresiones en 30 días pausadas
- [ ] D30: RSA más débil de cada grupo reemplazado
- [ ] D30: QS y experiencia de landing de los grupos de ciudad revisados (¿hacen falta landings por ciudad?)
- [ ] D30: hoja de "llamadas → trabajos" recibida del cliente
- [ ] D30: ≥10 conversiones y CPL ≤ $60 → presentar la propuesta de presupuesto ($1,500–1,800)

## Fase 3 — Optimización de puja (bloqueada con $825/mes)
- [ ] ≥30 conversiones en 30 días confirmadas (requiere el aumento de presupuesto)
- [ ] tCPA = CPA real observado (no el deseado)
- [ ] Presupuesto reajustado según CPA y capacidad del cliente
- [ ] Ajustes de puja por horario y dispositivo evaluados con datos

## Fase 4 — Remarketing (no realista hoy)
- [ ] Audiencia de visitantes ≥1,000 usuarios en 30 días
- [ ] RLSA en observación

## Fase 5 — Performance Max
No aplica con el presupuesto actual (requiere ~$150/día, tCPA estable y 30+ conv./mes). Ver `roadmap.md`.

## Fase 6 — Conversiones offline (futuro, requiere CRM)
- [ ] El cliente registra leads cerrados con GCLID
- [ ] Importación de conversiones offline configurada

## Recurrente (semanal, /weekly-review)
- [ ] Search terms → negativas
- [ ] Gasto contra presupuesto mensual ($825)
- [ ] CPL contra objetivo ($40–60); tendencia 7d contra 28d
- [ ] Anuncios rechazados o limitados
- [ ] IS perdida por presupuesto y por ranking
- [ ] Calidad de leads reportada por el cliente
- [ ] Log escrito en `log/YYYY-MM-DD.md`
