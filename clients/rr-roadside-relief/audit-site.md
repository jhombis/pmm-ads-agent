---
cliente: RR Roadside Relief
slug: rr-roadside-relief
url: https://rrroadsiderelief.com/
actualizado: 2026-10-01
veredicto: REQUIERE AJUSTES ANTES DE LANZAR
score: 10/22
---

# Auditoría de landing — RR Roadside Relief

## Veredicto
La cuenta ya está gastando y todo el tráfico cae en una home genérica. No tiene H1, ni formulario arriba, ni reseñas, y es lenta en móvil. La llamada funciona y el tag está instalado, pero hay que corregir 2 bloqueantes antes de escalar presupuesto. Como la cuenta ya está activa, no la pausaría: con 7 de 8 conversiones por llamada, el canal principal funciona.

## Bloqueantes (resolver en Fase 0)
- [ ] **Formulario corto arriba en móvil** — la home no tiene formulario. "Get A Free Quote" lleva a /schedule-a-tow/, con 9 campos (Name, Phone, Email, Vehicle, Service, Pick Up, Drop Off, Date/Time, Comments). Hay que poner en el hero de la home y de cada página de servicio un formulario de 4 campos: Nombre, Teléfono, Ubicación, Servicio. Dejar /schedule-a-tow/ para tows programados. — PMM — 2 h
- [ ] **Velocidad móvil sin verificar y probablemente mala**:
  - TTFB de 1.2 a 2.2 s en caché caliente y 6.5 s en la primera carga.
  - `logo.jpg` pesa 676 KB, el header de escritorio 493 KB y el de móvil 325 KB.
  - La página carga 28 scripts y 21 CSS (Elementor).
  - Acciones: medir con PageSpeed (la API agotó su cuota hoy), comprimir el logo a menos de 30 KB y pasarlo a WebP/SVG, comprimir los headers a menos de 100 KB, y activar caché de página (LiteSpeed/WP Rocket) o mejorar el hosting.
  - Si el score móvil sale por debajo de 40, es bloqueante duro.
  - PMM — 2–3 h

## Mejoras (Fase 2–3)
- [ ] **H1 por intención**: la home no tiene H1. Propuesta: "24/7 Towing & Roadside Assistance in Oklahoma City". Las páginas de servicio usan H1 genéricos ("Roadside Assistance"); conviene añadir ciudad y "24/7". — PMM — 0.5 h
- [ ] **Botón de llamar sticky en móvil**: el header sticky está configurado solo para escritorio (`sticky_on: desktop`). En móvil, el `tel:` desaparece al hacer scroll. Agregar una barra inferior fija "Call Now (405) 536-9093". — PMM — 0.5 h
- [ ] **Prueba social**: no hay reseñas, estrellas ni fotos reales del equipo o las grúas. Hay que embeber las reseñas de Google Business Profile (y conseguirlas si no las hay) y usar fotos de los 3 flatbeds. — Cliente + PMM — 1 h
- [ ] **Oferta concreta**: hoy solo hay "Get A Free Quote". El search term "$50 towing" convirtió. Proponer al cliente una oferta sostenible, por ejemplo "Jumpstart/Lockout desde $X" o "llegada en ≤30 min en OKC". — Cliente — —
- [ ] **Confianza**: dice "10 years combined experience", "24/7" y "3 flatbeds", pero no muestra licencia, seguro ni USDOT. Agregar "Licensed & Insured" con datos verificables. — Cliente — 0.5 h
- [ ] **Página de gracias con URL propia**: hoy el envío muestra un mensaje inline. El popup "Your Booking Is Not Yet Confirmed — call (405) 536-9093" es buena idea porque empuja a llamar, pero no tiene URL. Redirigir a /thank-you/ con ese mismo mensaje para medir sin depender del evento JS. — PMM — 0.5 h
- [ ] **Doble tag**: la web carga a la vez Site Kit (`GT-PHCMTZJ8` + `AW-18397439627`) y GTM (`GTM-TS99RXK7`). Hay que verificar con Tag Assistant que "Form Fill" no se cuente dos veces y que `AW-18397439627` pertenezca a la cuenta 425-405-2574. — PMM — 0.5 h

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| `/` (final URL actual de los anuncios) | **ninguno** (H2: "Oklahoma City's Trusted Roadside Team") | Get A Free Quote → /schedule-a-tow/ · Call Now ×3 | No | Sí, header + 3 botones; sticky solo escritorio | No | Menciona OKC, flatbeds, lowered cars, motocicletas, 24/7 |
| `/light-medium-duty-towing/` | Light & Medium-Duty Towing | Quote + Call | 4 campos, al pie | Sí | No | Buen texto (lowered cars, motos), sin ciudad en H1 |
| `/roadside-assistance/` | Roadside Assistance | Quote + Call | 4 campos, al pie | Sí | No | Lista: tire changes, lockout, fuel delivery, jumpstarts, winch outs |
| `/schedule-a-tow/` | Schedule A Tow | Submit | **9 campos** | Sí | No | Email: rraysautorecovery@gmail.com |
| `/about-us/` | About Us | Quote + Call | 4 campos, al pie | Sí | No | 3 flatbeds, 10 años de experiencia combinada |

Sin fugas: menú de 5 ítems, sin links externos ni pop-ups agresivos (2/2).

## Tracking encontrado
- **Site Kit by Google 1.187.0** → `gtag config GT-PHCMTZJ8` (GA4/Google tag) + `gtag config AW-18397439627` (Google Ads).
- **GTM** `GTM-TS99RXK7` (no se pudo leer el contenedor: el proxy bloquea googletagmanager.com).
- Listener propio: en `submit_success` de formularios Elementor empuja `gtm.formSubmit` al dataLayer. Probablemente es lo que dispara la conversión "Form Fill".
- Sin Meta pixel ni call tracking dinámico. Las llamadas se miden solo como "Calls from Ads" (call asset), no como llamadas desde la web.
- Plataforma: WordPress 7.1.2 + Elementor 4.2.4 (Pro: formularios, sticky).

## Velocidad
| Métrica | Valor |
|---|---|
| Score móvil PSI | **PENDIENTE** (cuota de API agotada; pedir a Jhombis o reintentar con `PAGESPEED_API_KEY`) |
| TTFB | 6.5 s la primera vez · 1.2–2.2 s después |
| HTML home | 105 KB · 28 `<script>` · 21 hojas CSS |
| Imágenes pesadas | logo.jpg 676 KB · header escritorio 493 KB · header móvil 325 KB (posible LCP) · image1.webp 219 KB |

Causas probables: hosting sin caché de página, imágenes sin optimizar (sobre todo el logo) y la carga de Elementor. Score provisional del ítem: 0 (estimado, hay que confirmarlo con medición).

## Landings que la estrategia va a necesitar
Los anuncios apuntan hoy todos a `/`. Con la estructura propuesta en el brief (Towing · Roadside · Tire):
1. **24/7 Towing OKC**: rehacer `/light-medium-duty-towing/` con H1 + formulario de 4 campos arriba. Absorbe "tow truck near me", "towing service" y "wrecker".
2. **Roadside Assistance OKC**: rehacer `/roadside-assistance/` con H1 + formulario arriba.
3. **Flat Tire Change OKC** (nueva): el sitio confirma que hacen cambio de llanta y la cuenta puja por "tire change near me".
4. **Car Lockout OKC** (nueva): servicio ofrecido sin keywords todavía.
5. **Jump Start / Dead Battery OKC** (nueva).
6. **Fuel Delivery OKC** (nueva, bajo volumen; puede ir como sección de Roadside).
7. **Motorcycle & Lowered Car Towing** (nueva, diferenciador: flatbeds).
8. **Servicio de Grúa en Español OKC** (nueva, solo si atienden en español: "servicio de grúa en español" convirtió).

En total: 2 a rehacer y 5–6 nuevas. Las páginas por ciudad (Norman, Moore, Edmond, Yukon) quedan para Fase 3 si el volumen lo justifica.

## Qué ya rankea orgánico (Semrush)
Nada. Semrush no tiene datos de `rrroadsiderelief.com` en la base US: es un dominio nuevo, con contenido subido en sep-2026. Sin relevancia orgánica previa, la calidad de la landing pesa más en el Quality Score.

## Puntaje
| Ítem | Pts |
|---|---|
| Headline refleja el servicio | 1 |
| Formulario corto arriba (móvil) | 0 ⛔ |
| Clic para llamar en móvil | 1 |
| Oferta clara | 1 |
| Prueba social | 0 |
| Confianza | 1 |
| Velocidad móvil | 0 (estimado) ⛔? |
| Google Tag presente | 2 |
| Página de gracias medible | 1 |
| Páginas por servicio | 1 |
| Sin fugas | 2 |
| **Total** | **10/22** |
