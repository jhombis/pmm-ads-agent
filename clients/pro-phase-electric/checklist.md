---
cliente: Pro Phase Electric
slug: pro-phase-electric
fase_actual: 1
actualizado: 2026-09-23
---
# Checklist — Pro Phase Electric

Generado por /roadmap desde `knowledge/checklists/setup-cuenta.md`. **B** = bloqueante de la fase. /weekly-review lo mantiene.
Cuenta 758-301-1023 · campaña actual 24208591381 (Max. clics, se pausa en F1).

## Fase 0 — Medición + contención (bloqueante para lanzar Search NWA)
### Cuenta
- [x] (PMM) Cuenta en el MCC de PMM — visible como "Premium Local Listings 004049 ($1500 Pro Phase Electric)"
- [x] (PMM) Facturación activa — la cuenta gasta desde el 11-sep
- [x] (PMM) Aplicación automática de recomendaciones DESACTIVADA — verificado vía API 23-sep (0 suscripciones)
- [x] (PMM) Acceso a la API (`google-ads.yaml`) — OK 23-sep. Pasar a variables de entorno para sesiones futuras

### Contención en la campaña actual
- [x] (PMM) Quitadas 15 negativas heredadas que bloqueaban servicios o el área (vista, car, estimate, free…) — 22-sep, ver log
- [x] (PMM) 134 negativas aplicadas a nivel campaña vía API — 23-sep
- [x] (PMM) Pausadas las 4 keywords broad genéricas — 23-sep
- [x] (PMM) Techo de CPC de $12 (Max. clics) — 23-sep
- [x] (PMM) Socios de búsqueda y Display apagados; ubicación = Presencia — verificado vía API 23-sep
- [x] (PMM) Programación verificada: L–D 5:00–16:00 hora de la cuenta (Pacífico) = 7:00–18:00 Central, según la orden de pedido — 23-sep (se había movido a 3–14 por error y se revirtió el mismo día)

### Tracking
- [ ] **B** (PMM) Google Tag verificado en todas las páginas (el cliente dice que está; confirmar el ID y el acceso)
- [ ] **B** (PMM) Conversión "Formulario" (Get a Free Quote: home + /contact-us/) con página de gracias o evento, probada con Tag Assistant
- [ ] **B** (PMM) Conversión "Llamadas desde el sitio" (número de reenvío de Google) creada y probada
- [ ] (PMM) Conversión "Clic en teléfono" (`tel:`) en móvil
- [~] (PMM) Conversiones existen: Form Fill (primaria), Calls from Ads (30 s), Website Calls (20 s). Form Fill y Website Calls con 0 en 90 días: probar en el sitio. Duración mínima no cambiada (decisión 23-sep)
- [ ] (PMM) Conversiones secundarias como secundarias (no primarias)
- [ ] (PMM) GA4 vinculado (Windsor no tiene una propiedad de este dominio conectada)
- [ ] (PMM) Campos ocultos UTM + GCLID en el formulario
- [ ] **B** (PMM/Cliente) Un solo teléfono en todo el sitio = número de reenvío (hoy (479) 287-3650 en barra, header y hero) — playbook §7
- [ ] **B** (PMM) Formulario de prueba: mensaje de gracias + llegada del correo + conversión registrada en 24–48 h
- [ ] (PMM) Recurso de llamada aprobado (no en revisión), filtro de duración 60 s
- [ ] (PMM) Popups y "After Submit" revisados si el sitio usa Elementor
- [ ] (PMM) Fecha de cada arreglo de medición anotada en el log

### Negativas
- [ ] (PMM) Lista "PMM Universal" a nivel cuenta (hoy como negativas de campaña vía CSV; pasar a lista cuando haya API)
- [ ] (PMM) Lista "pro-phase-electric nicho" (`data/negatives-nicho.txt`) aplicada a Search NWA
- [ ] (PMM) Limpiar la plantilla heredada de la campaña actual (palabras sueltas en broad, nombres de Grand Junction). No aplica si se pausa en F1

### Landing
- [ ] **B** (PMM) Score de PageSpeed móvil (si es <40, bloqueante)
- [ ] **B** (Jhombis) Captura móvil de la home: formulario y botón de llamada visibles
- [ ] (PMM/Cliente) Decir quién edita el sitio (PENDIENTE en el brief)
- [ ] (PMM) Verificar que `/residential-electrical-service/` hable de reparaciones (landing del grupo Repair en F1)

### Cliente
- [ ] **B** (Cliente) Proceso de respuesta: quién contesta de 7 a 18 Central, tiempo de respuesta, qué pasa con el buzón
- [ ] **B** (Cliente) Aceptar el número de reenvío de Google (call tracking)
- [ ] (Cliente) Acceso de gestor al GBP para PMM (el perfil existe: widget 4.9 ★ en el sitio)
- [ ] (PMM) GBP vinculado a Google Ads (activo de ubicación), después del acceso
- [ ] (Cliente) Horario del GBP y los directorios = L–D 7:00–18:00 (hoy publican L–V 8–17)
- [ ] (Cliente) Ticket y margen de un cambio de panel y de una instalación EV → CPL máximo (antes de Fase 2)
- [ ] (Cliente) Confirmar el área: ¿Siloam Springs, Gentry y el oeste de Benton? ¿Madison completo o solo Huntsville?
- [ ] (Cliente) Confirmar si instala generadores (hoy es negativa)
- [ ] (Cliente) Número de licencia de Arkansas
- [ ] (PMM) LSA: **en espera** (el cliente dijo "No"). Reabrir si cambia

## Fase 1 — Lanzamiento Search NWA (lanzada 23-sep con Fase 0 incompleta, por decisión de Jhombis — ver log/2026-09-23-build.md)
- [x] (PMM) Campaña Search NWA creada: ID 24273708366, 4 ad groups **activos**, todas las URLs a la home — 23-sep
- [x] (PMM) Red: solo Búsqueda; socios y Display apagados
- [x] (PMM) Ubicación: Presencia; condados de Benton y Washington + Huntsville
- [x] (PMM) Programación L–D 5:00–16:00 en hora de la cuenta (= 7:00–18:00 Central)
- [x] (PMM) Puja: Max. clics con tope de CPC $12; $27/día
- [x] (PMM) 83 keywords (64 frase + 19 exacta); ninguna broad
- [x] (PMM) 1 RSA por ad group, H1 pinneado, 15H/4D. Headline con teléfono reemplazado (política PHONE_NUMBER_IN_AD_TEXT)
- [ ] (PMM) Fuerza del anuncio "Buena" o superior (revisar en la UI)
- [x] (PMM) Extensiones: 5 sitelinks, 8 callouts, snippet, llamada (aprobada)
- [ ] (PMM) Imágenes propias; ubicación cuando haya GBP
- [x] (PMM) Negativas de enrutamiento por ad group (15) + listas compartidas PMM Universal (167) y nicho (97)
- [ ] (PMM) URLs finales verificadas (200, https): no se pudo con HEAD desde el entorno; confirmar en la aprobación
- [x] (Jhombis) Activación decidida; campaña anterior 24208591381 pausada — 23-sep
- [ ] (PMM) Anuncios aprobados (en revisión el 23-sep; revisar el 24-sep)
- [ ] (PMM) D7 (30-sep): CTR y QS de Paneles y EV apuntando a la home; si no convierten, pausar hasta tener landing
- [ ] **B** (PMM) Primera conversión **del sitio** registrada

## Fase 2 — Limpieza (D7 30-sep · D14 07-oct · D30 23-oct)
- [ ] D7: search terms revisados, negativas agregadas
- [ ] D7: keywords sin impresiones identificadas (no pausar aún)
- [ ] D14: search terms revisados, negativas agregadas
- [ ] D14: keywords con >$100 de gasto (2× CPL) y 0 conversiones marcadas para revisión
- [ ] D14+: landings de Paneles y EV auditadas → activar esos ad groups y sus sitelinks
- [ ] D30: search terms revisados, negativas agregadas
- [ ] D30: keywords con 0 impresiones en 30 días pausadas
- [ ] D30: activos del RSA de cada grupo revisados (1 RSA por grupo: no hay A/B)
- [ ] D30: clics por ciudad en el grupo NWA (solo se separa una ciudad con ≥50 clics y diferencias claras)
- [ ] D30: hoja de "llamadas → trabajos" recibida del cliente
- [ ] D30: ≥8 conversiones y CPL ≤ $100 → presentar la matemática y la propuesta de presupuesto ($1,500–1,800)
- [ ] 15+ conversiones en 30 días, estables y con medición limpia → pasar a Max. conversiones (anotar fecha)

## Fase 3 — Decisión de presupuesto, cambio de puja y tCPA
- [ ] Decisión de presupuesto del cliente (~1–15-nov)
- [ ] ≥30 conversiones en 30 días confirmadas (a CPL $85 pide ~$2,550/mes; a $55, ~$1,650)
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
- [ ] CPL contra objetivo (≤$85 provisional; aspiracional $40–60); tendencia 7d contra 28d
- [ ] Anuncios rechazados o limitados
- [ ] IS perdida por presupuesto y por ranking
- [ ] Calidad de leads reportada por el cliente
- [ ] Log escrito en `log/YYYY-MM-DD.md`
