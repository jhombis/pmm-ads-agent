---
cliente: A's Unasa Towing
slug: as-unasa-towing
url: https://asunasatowing.com
actualizado: 2026-10-21
veredicto: REQUIERE AJUSTES ANTES DE LANZAR
score: 10/22
---

# Auditoría de landing — A's Unasa Towing

## Veredicto
**No está lista para recibir tráfico pago.** Hay 3 bloqueantes:
1. El sitio no tiene Google tag. Site Kit está instalado pero sin conectar.
2. El formulario no está arriba del pliegue en ninguna página. El home no tiene formulario.
3. El formulario no tiene página de gracias medible.

Aparte de los bloqueantes:
- El header muestra el **placeholder "Logo."** de Elementor.
- No hay **ninguna prueba social**.
- La base es buena: oferta clara arriba ("Tows Starting At $79.99!"), botón de llamada arriba del pliegue, una página por servicio y una foto real de la grúa roja.

## Bloqueantes (resolver en Fase 0)
- [ ] **Google tag + conversiones.**
  - Conectar Site Kit (ya instalado, v1.189.0) o instalar GTM.
  - Crear 3 conversiones:
    - llamada desde el anuncio (≥60 s)
    - llamada desde el sitio, con número de reenvío de Google
    - envío de formulario
  - Probar con Tag Assistant.
  - Responsable: PMM, con acceso a WordPress del cliente. Esfuerzo: 2 h.
- [ ] **Página de gracias con URL propia** (`/thank-you/`).
  - Hoy el envío probablemente abre el popup 1704 (sin triggers propios), que dice "Your Booking Is Not Yet Confirmed — call to confirm". La acción "After Submit" no se puede ver desde fuera; hay que confirmarla en Elementor → Form → Actions After Submit.
  - Cambiarla por un redirect a `/thank-you/`. La conversión de formulario se dispara ahí.
  - Responsable: PMM. Esfuerzo: 1 h.
- [ ] **Formulario corto arriba del pliegue en móvil.**
  - Home: no tiene formulario.
  - Páginas de servicio: hay un formulario de 4 campos que en móvil empieza a ~2,370 px (Accident Recovery).
  - Schedule A Tow: 9 campos.
  - Arreglo: 3 campos (nombre, teléfono, ubicación) en el hero o justo debajo, con `type="tel"`.
  - Responsable: PMM. Esfuerzo: 2 h.

## Mejoras (Fase 2–3)
- [ ] **Logo real en el header.** Hoy se ve "Logo." (`elementor-pro/.../logo-placeholder.png`) en todas las páginas. Es lo primero que ve el usuario del anuncio y resta confianza. Hay 4 conceptos en `logo/`. Responsable: Cliente (elige), PMM (sube). Esfuerzo: 0.5 h.
- [ ] **Prueba social.** No hay reseñas, estrellas ni testimonios en ninguna página. Agregar el widget del GBP (cuando exista) o 3 reseñas reales con nombre. Responsable: Cliente + PMM. Esfuerzo: 1 h.
- [ ] **Headline por búsqueda.**
  - El home no tiene H1; el hero dice "From Flat Tires to Flatbeds".
  - Las páginas de servicio sí tienen H1 por servicio, pero todo dice "Salt Lake City" y nada dice West Valley, Kearns o Sandy, que es el área de la campaña.
  - Responsable: PMM. Esfuerzo: 1 h.
- [ ] **Horario coherente.**
  - El footer dice "Monday–Saturday 24 Hours · Closed Sunday".
  - El footer también dice "around-the-clock crew".
  - La grúa de la foto del home tiene rotulado "24/7 SERVICE".
  - Hay que alinearlo con lo que confirme el cliente (brief: pendiente bloqueante). Responsable: Cliente → PMM. Esfuerzo: 0.5 h.
- [ ] **Header sticky en móvil.** Hoy es sticky solo en desktop (`sticky_on: desktop`); en móvil, al bajar, desaparecen el header y su ícono de llamada. Agregar sticky en móvil o una barra inferior "Call Now". Responsable: PMM. Esfuerzo: 0.5 h.
- [ ] **Confianza.** Faltan "Licensed & Insured" y el USDOT 4229473 (registro público, web: LoadWrap), y no hay fotos propias en las páginas de servicio. Accident Recovery usa una foto de stock de dos autos chocados. "Police rotation" y "nearly a decade" ya están. Responsable: Cliente (confirma seguro), PMM. Esfuerzo: 0.5 h.
- [ ] **Formulario de Schedule A Tow mal etiquetado.**
  - El campo con id `email` tiene la etiqueta "Desired Date/Time".
  - El email real es `field_3adf8e2`, de tipo `text`.
  - Si la acción de email de Elementor usa `[field id="email"]` como Reply-To, el correo llega con la fecha en lugar del email.
  - Arreglo: corregir los ids y usar los tipos `email`/`tel`.
  - Responsable: PMM. Esfuerzo: 0.5 h.
- [ ] **Dirección y email en el footer.** Hoy solo aparecen en Schedule A Tow (y el email en Privacy Policy). El cliente pidió la dirección visible. Antes de publicarla hay que confirmar si 721 S 5500 W recibe clientes: si es una dirección postal, no se muestra y el GBP va como área de servicio. Responsable: Cliente → PMM. Esfuerzo: 0.25 h.
- [ ] **SEO básico.** Ninguna página tiene meta description. No hay JSON-LD `TowingService`/`LocalBusiness`. Las 11 imágenes del home tienen `alt=""`. Responsable: PMM. Esfuerzo: 1.5 h.
- [ ] **Peso.** Home de ~1.5 MB en ~50 requests. Los fondos del header pesan 222 KB (desktop) y 110 KB (móvil); además hay `texture.webp` de 118 KB y 2 fotos de ~190 KB. Comprimir y bajar el header a <80 KB en móvil. Responsable: PMM. Esfuerzo: 1 h.

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| / | **ninguno** (hero: "From Flat Tires to Flatbeds") | "Click here to call" arriba del pliegue, "Get A Free Quote" (→ /schedule-a-tow/), "Call Now" ×2 | **no** | (385) 473-9820, 6 enlaces `tel:` | no | Oferta "$79.99" arriba. Foto real de la grúa roja. 581 palabras |
| /about-us/ | About Us | Get A Free Quote, Call Now | 4 campos (name, phone, email, message) | (385) 473-9820 | no | 521 palabras |
| /light-medium-duty-towing/ | Light & Medium-Duty Towing | ídem | 4 campos | ídem | no | 463 palabras |
| /exotic-classic-vehicle-transport/ | Exotic & Classic Vehicle Transport | ídem | 4 campos | ídem | no | 508 palabras |
| /accident-recovery/ | Accident Recovery | ídem | 4 campos, a ~2,370 px en móvil | ídem | no | Foto de stock. Menciona la rotación policial. 557 palabras |
| /roadside-assistance/ | Roadside Assistance | ídem | 4 campos | ídem | no | 552 palabras |
| /schedule-a-tow/ | Schedule A Tow | Submit | **9 campos** (3 obligatorios), con ids mal etiquetados | ídem | no | Única página con dirección y email |
| /privacy-policy/ | Privacy Policy | — | no | ídem | — | — |

No hay páginas por ciudad. Los "Learn More" del home enlazan a las 4 páginas de servicio. El menú tiene 7 ítems y no hay enlaces externos (salvo gmpg.org en el `<head>`). El popup 1704 está en todas las páginas, sin triggers de tiempo ni de scroll, así que no es intrusivo.

## Tracking encontrado
- **Nada.** Las 8 páginas no tienen `gtag(`, `G-`, `AW-`, `GTM-` ni `fbq(`.
- **Site Kit by Google 1.189.0** está instalado (meta generator) pero no imprime ningún tag: no está conectado a GA4 ni a Ads. Es el camino más rápido para el Google tag, sin tocar el tema.
- **Teléfono**: un solo número en todo el sitio, **(385) 473-9820** (CallFire → (801) 906-1114). Cumple "un solo teléfono" (playbook §7). Falta la conversión de llamada desde el sitio. Recomendación: número de reenvío de Google en el sitio que desvíe a (385) 473-9820, para que CallFire siga registrando todas las llamadas y Ads pueda separar las suyas.
- **Formulario**: Elementor Pro (AJAX, `action` vacío). El destino del email está PENDIENTE (brief).
- Stack: WordPress 7.1.3, Elementor 4.3.5 + Elementor Pro 4.2.3.

## Velocidad
- **PageSpeed: sin dato** (no hay `PAGESPEED_API_KEY`). Score PENDIENTE: pedir a Jhombis el score móvil de pagespeed.web.dev o configurar la clave.
- **Estimación de laboratorio** (Chromium headless, 390 px, sin throttling de red ni CPU, así que es optimista frente a PageSpeed móvil):

  | Página | LCP | Evento `load` |
  |---|---|---|
  | Home | 3.1 s | 5.0 s |
  | Accident Recovery | 2.0 s | 4.4 s |

- **Peso del home**: HTML de 104 KB + 50 recursos (~1.04 MB) + fondos de header y textura (~0.45 MB) ≈ **1.5 MB**. Las causas principales son imágenes sin comprimir (fondos del header de 222/110 KB, 2 fotos webp de ~190 KB), jQuery (88 KB) y 26 hojas CSS de Elementor.
- El TTFB del HTML ronda 1.2–2.6 s (curl). El hosting es lento o no tiene caché de página.
- **Score de la rúbrica: 1 (estimado)**. Con throttling móvil, el LCP probablemente pasa de 2.5 s. No es bloqueante mientras no haya un score real < 40.

## Landings que la estrategia va a necesitar
Con ~$540/mes y 1 campaña de 1–3 ad groups (benchmark.md), no hacen falta páginas por ciudad × servicio. Hacen falta 3 páginas, con la plantilla corregida (formulario corto arriba, llamada sticky, reseñas, logo):
1. **Towing West Valley City & Kearns** (grupo principal: "towing near me", "tow truck", "west valley towing", "kearns towing"). H1 con West Valley/Kearns, oferta, formulario de 3 campos y llamada. Puede ser una página nueva en el WordPress del cliente o una `/landing` en performancemediamarketing.com/as-unasa-towing/ si no se consigue el acceso a WordPress.
2. **Accident Recovery**: adaptar la página existente. Formulario arriba, foto real y la rotación policial como prueba (confirmar antes la vigencia en West Valley City, ver competitors.md).
3. **Exotic & Classic Transport**: la página existente, para sitelink o grupo chico. Formulario arriba y una foto real de un exótico o clásico cargado en la flatbed, si el cliente la tiene.

Sandy (84092) entra en la página 1 con inserción de ciudad, si el cliente confirma que lo cubre. Las landings las define `/strategy`, y se construyen con `/landing` o `/landing-ghl`.

## Qué ya rankea orgánico (Semrush)
- **Sin datos.** `domain_rank` de asunasatowing.com en la base `us` da no_data. El dominio es nuevo (copyright ©2026, imágenes subidas en 2026-10). No tiene relevancia orgánica previa sobre la cual apoyarse.
- Los términos locales los dominan competidores con décadas de antigüedad (competitors.md).
