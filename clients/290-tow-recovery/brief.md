---
cliente: 290 Tow and Recovery
slug: 290-tow-recovery
pais: US
idioma: EN
nicho: towing
customer_id: 213-019-5545
actualizado: 2026-10-06
estado: activa sin reestructurar (Fase 0)
origen: onboard (2026-09-23) + reanálisis 2026-10-06
---

# Brief — 290 Tow and Recovery

Fuentes:
- (cliente): respuesta de Jhombis en /onboard
- (web): site-scan del 2026-10-06
- (Windsor): cuenta 213-019-5545
- (Semrush)
- (benchmark): `knowledge/benchmarks/towing-us.md`

## Negocio
- **URL**: https://290towrecovery.com/ — WordPress + Elementor Pro, sitio de PMM (web).
- **Base y área de servicio**:
  - Fredericksburg, TX 78624, radio de **40 mi** (cliente).
  - La web dice "Fredericksburg and surrounding areas within a 45-minute radius" (web, imagen del hero).
  - Gasto real por ciudad: Kerrville 20.2%, Fair Oaks Ranch 17.1%, Fredericksburg 13.9% (Windsor).
  - PENDIENTE si atiende Fair Oaks Ranch, Bulverde y Spring Branch, el borde de San Antonio.
- **Servicios**:
  1. Light & Medium-Duty Towing
  2. Local & Long-Distance Towing
  3. Exotic Vehicle Towing
  4. Roadside Assistance: battery jumpstarts, tire changes, lockout (web)

  Equipo: "rollback and wrecker trucks", o sea **flatbed confirmado** (web, /about-us/). Página "Schedule A Tow" para tows programados (web).
- **Servicio estrella / a evitar**: PENDIENTE.
  - En la cuenta, "towing near me" lleva el 55.7% del gasto y 4 de 6 conversiones (Windsor).
  - "roadside assistance" en amplia lleva el 26% del gasto y trajo casi todo el desperdicio (Windsor).
- **Diferenciadores**:
  - Respuesta rápida 24/7 y precio claro (cliente).
  - "Navy Veteran Owned & Operated", "Available 24/7", "Fast & Efficient" (web).
- **Ofertas sostenibles**:
  - "Get A Free Quote" y "10% Senior Discount" (web, en imagen).
  - "Precio antes de enganchar": PENDIENTE confirmar.
- **Búsqueda de marca**: no. Hay 0 búsquedas de "290 tow" en los search terms del 09-17 al 10-06 (Windsor).

## Objetivo y economía
- **Objetivo primario**: llamadas, 24/7 (cliente).
- **Presupuesto mensual**: el cliente paga $1,500/mes; **$825/mes de pauta**, $27/día, tope mensual $820.80 (cliente + Windsor).
- **Ticket promedio / margen**: PENDIENTE.
- **Capacidad**: PENDIENTE.
- **CPL máximo aceptable**: PENDIENTE hasta tener ticket y margen.
  - Referencias rotuladas:
    - CPL observado: $88.36 (6 conversiones sin verificar, 09-17 → 10-05) (Windsor)
    - cohorte nueva del MCC, meses 1–2: mediana $51–63 (benchmark)
    - cuentas maduras: $15–16 (benchmark)
  - La cifra de ~$14 del onboarding salía de un ticket supuesto de $175 y queda **descartada** como objetivo.
- **Historial Google Ads** (Windsor):
  - Cuenta: "Premium Local Listings 004046 ($1500 290 Tow and Recovery)", ID 213-019-5545, revendedor PLL. Activa desde el 2026-09-17.
  - Configuración:
    - 1 campaña Search "ENHPRM Radius", Maximizar clics, $27/día
    - presencia en radio de 40 mi, solo Búsqueda
    - "Ad group 1 - Towing General" con 12 keywords en amplia
    - "Ad group 2 - Exotic Car & Long Distance towing" vacío
  - **18 días: $530.14, 53 clics, CPC $10.00, 6 conversiones** (4 Calls from Ads, 1 Website Calls, 1 Form Fill), CPL $88.36.
  - 45.8% del gasto rastreable en desperdicio.
  - Detalle en `log/2026-10-06-diagnose.md`.

## Operación
- **Horario**: 24/7 con alguien que contesta (cliente). "Hours: Available 24/7" (web). Sin programación de anuncios (Windsor).
- **Respuesta a leads**: PENDIENTE (quién contesta de noche y en cuánto tiempo).
- **Teléfono / call tracking**:
  - (830) 463-8318, el único en todo el sitio (web).
  - Número de reenvío de Google en la extensión de llamada (Windsor: 8 llamadas, 4 contadas como conversión).
- **Email**: 290towandrecovery@gmail.com (web, privacy policy).
- **CRM**: PENDIENTE.
- **GBP**: no tiene / PENDIENTE (cliente). No está conectado en Windsor.

## Competencia
| Competidor | URL | Nota |
|---|---|---|
| Douglas Towing (Fredericksburg) | FB | 4.8★ / 157 (competitors.md) |
| Tic Tac Towing (Fredericksburg) | FB | 4.9★ / 70 · aparece en search terms (Windsor) |
| Integrity Towing (Kerrville) | integritytowing.net | 4.8★ / 89 · aparece en search terms |
| Comal Towing, Mission Towing, Five Star / KW Towing (Boerne), Barbee Wrecker, RST Towing | — | aparecen en search terms del 09-17 al 10-06 (Windsor); 2 conversiones salieron de "comal towing" y "mission towing" |

## Web y tracking
- **Plataforma**: WordPress + Elementor Pro (tema Hello Elementor, Google Site Kit). La edita PMM (web).
- **Tag**: GTM-WBX4RZ9K y AW-18397446767 en el HTML; GA4 G-KH9SFWZK66 vía GTM (web).
- **Conversiones** (Windsor), las tres primarias, "una por clic":
  - Calls from Ads
  - Website Calls
  - Form Fill
- **Formulario**:
  - "Contact Us" de 4 campos en cada página y "Schedule A Tow" de 9.
  - Al enviar, popup "Your Booking Is Not Yet Confirmed – Please give us a call to confirm".
  - **No hay página de gracias** (`/thank-you/` da 404) (web).
- **Requisitos de política**: licencia TDLR de Texas. No es visible en el sitio; PENDIENTE.

## LSA (solo US)
- Aplica: towing califica.
- Bloqueado por: falta de GBP, licencia TDLR y seguro sin confirmar, background check PENDIENTE.

## Fuentes consultadas
| Fuente | Estado | Archivo |
|---|---|---|
| Google Ads API | sin credenciales en el entorno | — |
| Windsor (google_ads) | ok, 2026-09-17 → 2026-10-06 | data/2026-10-06-*.csv, data/hist-*.csv |
| Web (9 páginas) | ok (2026-10-06) | data/site-scan.json (no versionado) |
| PageSpeed | ok (home 43, light-medium 55, exotic 62) | data/pagespeed.json (no versionado) |
| Semrush | ok el 2026-09-23 (sin datos de pago locales) | data/competitors-keywords.csv |
| GBP | no existe / no conectado | — |

## Hallazgos que ya importan para la estrategia
- **Amplia sin negativas**: $126.66 de $276.32 rastreables (45.8%) son desperdicio claro. "roadside assistance" en amplia se lleva el 26% del gasto.
- **Las conversiones no prueban leads**: 3 de 6 vienen de búsquedas de competidores o "junk cars". 8 llamadas → 4 conversiones de Calls from Ads.
- **CPC de $10.00**: 2× la mediana de las maduras y +32% sobre la cohorte nueva. Maximizar clics sin tope visible.
- **Borde de San Antonio**: 22.9% del gasto ($120.84) con 1 conversión, que salió de un competidor.
- **El RSA del grupo de towing** usa titulares de roadside ("Battery Jumpstarts", "Tire Change").
- **Form Fill** dispara sin página de gracias y el formulario muestra un popup que pide volver a llamar.

## Preguntas para el cliente (solo lo que no se pudo investigar)
1. **(B)** De las llamadas del 25-sep, 28-sep, 29-sep, 2-oct y 4-oct, ¿cuáles fueron clientes y cuáles se convirtieron en trabajo?
2. **(B)** ¿Quién contesta de noche y fines de semana, y en cuánto tiempo?
3. **(B)** Ticket promedio y margen por servicio: tow local, long-distance, exotic, roadside.
4. ¿Atiende Fair Oaks Ranch, Bulverde y Spring Branch, o solo hasta Boerne/Comfort?
5. ¿Qué roadside hace: jump start, lockout, cambio de llanta, gasolina? ¿Remolca RV, motos o trailers?
6. ¿Cotiza el precio por teléfono antes de enganchar? Si sí, se usa en los anuncios.
7. Número de licencia TDLR y seguro. ¿Atiende en español?
8. ¿Ya creó el Google Business Profile?

## Pendientes
- [ ] **(bloqueante)** Verificar las 8 llamadas y la medición (Tag Assistant, umbral de 60 s, `/thank-you/`).
- [ ] **(bloqueante)** Respuesta a leads (quién y en cuánto tiempo).
- [ ] **(bloqueante para F2)** Ticket y margen → CPL máximo real.
- [x] Historial de la cuenta leído: 09-23 (6 días) y 10-06 (18 días).
- [ ] Área real (borde de San Antonio), servicios de roadside, RV, motos.
- [ ] Crear y verificar el GBP (activo de ubicación, LSA, reseñas).
- [ ] Licencia TDLR y seguro visibles en el sitio.
- [ ] Oferta "precio antes de enganchar" confirmada.
