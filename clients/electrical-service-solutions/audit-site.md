---
cliente: Electrical Service Solutions
slug: electrical-service-solutions
url: https://electricalservicesolutionspa.com/
actualizado: 2026-10-20
veredicto: REQUIERE AJUSTES ANTES DE LANZAR
score: 10/22
---

# Auditoría de landing — Electrical Service Solutions

## Veredicto
El mensaje está bien: especialista en paneles, residencial y comercial, 40+ años, financiamiento y "Free Quote", con una página por servicio y un solo teléfono, el CTN. **Pero no se puede lanzar** porque:
1. No hay ningún Google Tag.
2. El formulario no tiene página de gracias medible.
3. En móvil el formulario queda a ~3 pantallas de scroll en las landings de servicio.

Son 4–5 horas de trabajo de PMM en Elementor. No dependen del cliente.

Fuentes: `data/site-scan.json` (6 páginas), HTML bajado por curl y Playwright en móvil (390×844, red de ~1.6 Mbps con 150 ms de latencia y CPU 4× más lenta, parecido a Lighthouse móvil). No hay `PAGESPEED_API_KEY`, así que **la velocidad es una medición propia, no el score de PageSpeed**. Solo abre el dominio sin `www` (`www.` no resuelve desde el entorno; verificar que redirija).

## Bloqueantes (resolver en Fase 0)
- [ ] **Google Tag**: Site Kit by Google 1.189.0 está instalado pero sin conectar. En el HTML solo aparece un `dns-prefetch` a googletagmanager.com, sin ningún ID G-, AW- ni GTM-. Hay que conectar el tag de Google Ads de la cuenta 384-080-6970, ya sea con Site Kit o con GTM, en todas las páginas. — PMM — 1 h
- [ ] **Conversiones en la web**: (a) envío del formulario por la página de gracias y (b) clic en `tel:4126669290`. Las dos se prueban con Tag Assistant, y la del formulario se registra como primaria. — PMM — 1 h
- [ ] **Página de gracias**: el formulario es de Elementor Pro (`elementor-form`, sin `action`) y no hay redirección visible. Hay que crear `/thank-you/` con noindex y, en Elementor → Form → Actions After Submit, poner **Redirect** a esa página, sin quitar la acción Email a chris@electrical-service-solutions.com. Después, hacer un envío de prueba (con aviso al cliente) para confirmar que llega el correo. — PMM — 1 h
- [ ] **Formulario corto arriba en móvil**: la home no tiene formulario, porque "Get A Free Quote" lleva a /contact-us/. En las páginas residencial y comercial el formulario (Name, Phone, Email, Message + reCAPTCHA) empieza a **2,821 px** y **2,622 px**, con un fold de 844 px. Hay que subirlo justo debajo del H1, o poner un botón "Get A Free Quote" debajo del H1 que salte al formulario. Además, /contact-us/ pide 6 campos, con Property Address obligatorio: se baja a 4 o se deja la dirección opcional. — PMM — 1.5 h

## Mejoras (Fase 2–3)
- [ ] **Página /financing/ en el dominio**: hoy el menú "Financing" sale directo a `offers.purefinancegroup.com`, sin `target="_blank"` en el menú. Eso es una fuga, y el sitelink de financiamiento tiene que ser del mismo dominio. La página va con el texto que ya existe (on approved credit, 7–20 años) y un CTA al enlace de Pure Finance Group en pestaña nueva. — PMM — 1 h
- [ ] **Llamada sticky en móvil**: el ícono de teléfono del header y "Click Here To Call" se ven sin scroll, pero al bajar el header no queda fijo en móvil. Falta una barra o botón flotante con el CTN. — PMM — 0.5 h
- [ ] **Prueba social**: no hay reseñas, estrellas ni testimonios, solo un enlace "Google" al GBP. Hay que agregar un widget o bloque de reseñas de Google con estrellas y número en cuanto haya acceso al GBP. — PMM/Cliente
- [ ] **Confianza**: no aparecen licencia ni seguro. Hay que agregar el número de licencia y "Licensed & Insured" cuando el cliente los confirme (pendiente del brief). — Cliente
- [ ] **Velocidad de la home**: LCP de ~8.8 s en la medición, con 1.27 MB, de los que 974 KB son imágenes. El elemento LCP es el fondo del hero móvil (`electrical-service-solutions-header-mobile-bg.jpg`, 217 KB), que además entra con el lazy-load de fondos de Elementor. El logo es un PNG de 151 KB. Arreglos: hero en WebP de ~60 KB con preload, sin lazy-load en el primer fondo, y logo en WebP o SVG. Los anuncios no van a la home, así que no bloquea. — PMM — 1 h
- [ ] **Zonas en el texto**: la web dice "Greater Pittsburgh". Hay que nombrar Bethel Park, Upper St. Clair, Mt. Lebanon, McCandless/North Hills y Monroeville en las landings, para que coincidan con los headlines y con la geo. — PMM — 0.5 h
- [ ] **SEO básico**: la home no tiene H1 (el hero usa H2) y ninguna página tiene meta description. Falta JSON-LD `Electrician` con `areaServed` (sin dirección) y horario. — PMM — 1 h
- [ ] **`www`**: verificar que `www.electricalservicesolutionspa.com` redirija al dominio sin www, porque desde el entorno no resuelve. — PMM — 0.2 h
- [ ] **Financiamiento en anuncios**: la web publica plazos ("seven to twenty years"). En un anuncio, mencionar plazos o cuotas puede obligar a divulgar APR y condiciones. En los anuncios se usa "Financing Available" / "On Approved Credit", y los plazos solo con el texto de divulgación del financiador. — PMM

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| / | — (hero en H2: "Service Panel Upgrades & Panel Replacements" / "Your Panel Upgrade Specialists") | Click Here To Call · Get A Free Quote → /contact-us/ · View Financing Options → Pure Finance | No | CTN en header (sin scroll) y en CTAs | No (enlace "Google") | LCP ~8.8 s; 1.27 MB |
| /residential-electric-service-panel-upgrades-replacements/ | Residential Electric Service Panel Upgrades & Replacements | Get A Free Quote · Call Now · View Financing Options | 4 campos + reCAPTCHA, a 2,821 px | CTN | No | Cubre panel upgrade, **service change-out**, fusibles, paneles con fallas de seguridad, permisos e inspección, "usually a single working day"; LCP ~3.3 s, 623 KB |
| /commercial-electric-service-panel-upgrades-replacements/ | Commercial Electric Service Panel Upgrades & Replacements | Get A Free Quote · Call Now · View Financing Options | 4 campos + reCAPTCHA, a 2,622 px | CTN | No | Verticales (retail, restaurantes, oficinas, dental/médico, supermercados, industrial), trabajo de noche y fines de semana, permisos y coordinación con la empresa de luz; LCP ~3.3 s, 590 KB |
| /contact-us/ | Contact Us | Submit | 6 campos (Property Address obligatorio) + reCAPTCHA, a 431 px | CTN | No | Horario L–V 9–21, S–D 9–17 y "Emergency & Late-Night Services Available"; LCP ~6.4 s |
| /about-us/ | About Us | Get A Free Quote · Call Now | 4 campos | CTN | No | 40+ años, financiamiento 7–20 años, "the number we give you is the number you pay" |
| /privacy-policy/ | Privacy Policy | — | No | CTN | — | Única página con el email chris@electrical-service-solutions.com |

**Medición (playbook §7)**:
- Un solo teléfono en todo el sitio: el CTN (412) 666-9290 (`tel:4126669290`) ✓.
- No hay popups (`hasPopUps:false`) ✓.
- No hay acciones de conversión que revisar porque no hay tag.
- La duración de llamada y el recurso de llamada se configuran en Ads (pendiente).
- El horario de la web coincide con el del brief ✓.

## Tracking encontrado
| Elemento | Estado |
|---|---|
| Google Tag (G-/AW-) | **No hay** |
| GTM | No hay |
| Site Kit by Google 1.189.0 | Instalado, sin conectar (solo `dns-prefetch`) |
| Meta Pixel, CallRail, Clarity, Hotjar | No hay |
| reCAPTCHA | Sí, en todos los formularios |
| Plataforma | WordPress 7.1.3 + Elementor 4.3.4 + Elementor Pro, tema Hello Elementor |

## Velocidad
Medición propia en móvil (Playwright con red y CPU limitadas). No es el score de PageSpeed: hay que confirmarlo con PageSpeed Insights.

| Página | LCP | CLS | Peso | Requests |
|---|---|---|---|---|
| Home | ~8.8 s | 0.015 | 1.27 MB (974 KB en imágenes) | 49 |
| Residencial | ~3.3 s | 0.001 | 623 KB | 48 |
| Comercial | ~3.3 s | 0.013 | 590 KB | 48 |
| Contacto | ~6.4 s | 0.002 | 722 KB | 47 |

Causas en la home:
- El fondo del hero móvil es un JPG de 217 KB, cargado con lazy-load de fondos (elemento LCP).
- `image1.webp` pesa 189 KB y `texture.webp` 176 KB.
- El logo es un PNG de 151 KB.
- Dos fuentes Inter suman ~99 KB.

Las landings de servicio están cerca del umbral (LCP <2.5 s): con el formulario arriba y las imágenes optimizadas deberían pasarlo.

## Landings que la estrategia va a necesitar
No hace falta crear landings nuevas para lanzar. El mapa de grupos a páginas queda así:

| Ad group | URL final |
|---|---|
| Panel Upgrade | /residential-electric-service-panel-upgrades-replacements/ |
| Service Upgrade | /residential-electric-service-panel-upgrades-replacements/ (tiene la sección "Panel Upgrade or Service Change-Out?") |
| Fuse Box | /residential-electric-service-panel-upgrades-replacements/ (menciona "Fuses instead of breakers") |
| Commercial Panel | /commercial-electric-service-panel-upgrades-replacements/ |
| Sitelink Financing | /financing/ (**crear**) |

Opcional en F2: página propia de "Service Change-Out / 200 Amp Upgrade" si ese grupo junta volumen.

## Qué ya rankea orgánico (Semrush)
Nada todavía: Semrush no tiene datos de `electricalservicesolutionspa.com` (dominio nuevo; consultado el 19 y el 20-oct). Tampoco del dominio anterior, `electrical-service-solutions.com`.
