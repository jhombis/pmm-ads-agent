---
cliente: Murrieta Valley Funeral Home
slug: murrieta-valley-funeral-home
fase_actual: 0
actualizado: 2026-10-07
---
# Checklist — Murrieta Valley Funeral Home

Provisional: lo crea /investigar-cliente con los pendientes bloqueantes del brief. /roadmap lo reemplaza por el checklist completo (`knowledge/checklists/setup-cuenta.md`) adaptado a una **cuenta ya activa** (769-956-1619).
Responsables: PMM · Cliente · Jhombis (decisión).

## Fase 0 — Fundación / onboarding (bloqueante para Fase 1)
### Datos de la cuenta
- [x] (PMM) Brief investigado sin entrevista (2026-10-07, completitud 56%)
- [ ] (PMM) **Bloqueante**: credenciales de la API de Google Ads o Windsor autorizado → `account_profile.py --customer 7699561619` (estructura, conversiones, search terms, geo) y `/diagnose`
- [ ] (PMM) Auditar qué conversiones cuenta la PMax (CPA $57) antes de usarla como referencia
### Economía
- [ ] (Cliente) **Bloqueante**: margen por tipo de servicio (cremación directa vs servicio completo), mezcla y capacidad de casos/mes → CPL máximo
- [ ] (Cliente) Servicio que más quiere vender y ofertas sostenibles (planes de pago, pre-need)
### Tracking
- [x] (PMM) Google Tag presente: GTM-MRZ2HJMT + AW-16758859270 en todas las páginas (audit-site.md 2026-10-07)
- [ ] (PMM) **Bloqueante**: confirmar que AW-16758859270 es el de 769-956-1619 y qué etiquetas dispara el GTM (llamadas, formulario, reenvío)
- [ ] (PMM/Cliente) **Bloqueante**: crear /thank-you/ (noindex) y poner el formulario de Elementor en Redirect; Form Fill por URL probado con Tag Assistant
- [ ] (PMM/Cliente) **Bloqueante**: llamadas con duración mínima (≥60–90 s) y número de reenvío; un solo teléfono por landing (hoy la home muestra 696-0626 y 296-0890)
- [ ] (Cliente) Acceso al WordPress para instalar o confirmar el tag
### GBP y grupo
- [ ] (Cliente) GBP de Murrieta (y Temecula / Lake Elsinore): verificación, conteo de reseñas en Google y acceso de PMM
- [ ] (PMM) GBP vinculado como activo de ubicación
- [ ] (Cliente) Confirmar dueño actual (Shreves vs Hamilton) y si Colton Sunflower, Temecula Cremation & Burial y Options son del mismo grupo
- [ ] (Jhombis) Coordinar geos y negativas de marca entre 769-956-1619, Colton Sunflower (151-776-2744) e Inland Memorial Murrieta (934-241-5137, pausada)
### Landing (audit-site.md 2026-10-07: 11/22)
- [ ] (PMM/Cliente) **Bloqueante**: landing /cremation/ con H1 de servicio, paquetes con precio del GPL, formulario arriba y llamada fija
- [ ] (PMM/Cliente) **Bloqueante**: landing /funeral-services/ (paquetes A/B/C, direct burial $1,995, capilla)
- [ ] (Cliente) Home: H1, una línea de precio/oferta bajo el hero, un solo teléfono
- [ ] (Cliente) /veteran-services/: formulario y llamada arriba
- [ ] (Cliente) Caché de página (TTFB 1.8–2.2 s) y preload del hero móvil
- [ ] (PMM/Cliente) Reseñas de Google con número y nota en todas las landings
### Operación
- [ ] (Cliente) Quién contesta de noche y fines de semana; tiempo de respuesta a formularios
- [ ] (Cliente) ¿Atienden en español? (define ad group ES o negativas del grupo E)
### Siguientes skills
- [x] (PMM) `/audit-landing` corrido 2026-10-07 (11/22, requiere ajustes)
- [ ] (PMM) `/competitors` y `/benchmark-interno` en paralelo
- [ ] (PMM) `/strategy` → `/roadmap` (crea el checklist completo)
