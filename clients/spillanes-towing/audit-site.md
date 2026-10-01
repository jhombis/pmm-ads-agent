---
cliente: Spillane's Towing & Recovery
slug: spillanes-towing
url: https://spillanestowingrecovery.com/
actualizado: 2026-10-01
veredicto: REQUIERE AJUSTES ANTES DE LANZAR
score: 10/22
---

# Auditoría de landing — Spillane's Towing & Recovery

> Método: el proxy de la sesión bloquea el dominio. El contenido se leyó con Leadpages `analyze_url` (fetch remoto), el tráfico de Ads con Windsor (cuenta 822-393-5903, last_90d) y el orgánico con Semrush. **PageSpeed devolvió 429 (sin `PAGESPEED_API_KEY`)** y el HTML crudo (scripts) no fue accesible, así que velocidad y tags son inferidos o pendientes.

## Veredicto
La landing de Ads (one-page en WordPress/Elementor, creada en 08/2026) sirve para llamadas, pero no para formulario ni relevancia: sin H1 con el servicio, formulario de 6 campos al fondo y sin página de gracias. **La campaña ya está activa: no se pausa.** Los bloqueantes se corrigen en la Fase 0 de la reestructuración, antes de subir presupuesto o separar ad groups.

Contexto: el 99% de los clics son móviles (78 de 79) y 13 de 14 conversiones son llamadas. El formulario pesa poco hoy, pero el estándar 7 exige medirlo bien.

## Bloqueantes (resolver en Fase 0)
- [ ] **H1 con el servicio + zona**: hoy el hero no tiene heading; "Stranded on the road?" es texto suelto. Poner H1 tipo "24/7 Towing in Burlington & South Burlington, VT" y subtítulo con el tiempo de llegada si el cliente lo sostiene. Responsable: PMM · 0.5 h
- [ ] **Formulario corto arriba en móvil**: hoy tiene 6 campos (Name, Phone, Email, Service Needed, Vehicle Location, Details) y está al final (#contact). Pasar a 3 campos en el hero móvil (Name, Phone, Vehicle Location) y dejar el largo abajo. PMM · 1.5 h
- [ ] **Página de gracias con URL propia** (`/thank-you/`). Hoy el envío parece inline (los clics a `#contact` no muestran URL de destino). Cambiar la conversión "Form Fill" a page-view de `/thank-you/` o verificar el evento. PMM · 1 h
- [ ] **Velocidad móvil sin medir**: correr PageSpeed con API key o a mano en pagespeed.web.dev. Hay 3 headers duplicados en el DOM, un hero de 1920×760 más su versión móvil y 4 familias de fuentes; sospecha de LCP alto. PMM · 0.5 h medir + lo que salga
- [ ] **Verificar tracking con Tag Assistant**: "Website Calls" (5 conv.) y "Form Fill" (1) registran, así que el tag existe, pero no se pudo leer el HTML. Confirmar que hay un solo Google Tag, que el reemplazo del número funciona y que no hay doble conteo con "Calls from Ads". PMM · 0.5 h

## Mejoras (Fase 2–3)
- [ ] **Quitar el link "Google" (share.google) del contacto y del footer**: lleva al GBP de 3.2★ y es una fuga directa hacia la peor prueba social del cliente. PMM · 5 min
- [ ] **Oferta concreta** en lugar de "Get A Free Quote" (en towing nadie pide cotización): "Avg. arrival 30 min", "Flat local rate" o similar, según lo que confirme el cliente (brief: ofertas PENDIENTE).
- [ ] **Bajar Lockouts y Roadside Assistance del bloque de servicios** o moverlos abajo: son tickets bajos y hoy atraen gasto ("roadside assistance" broad = 72% del presupuesto). Subir Accident Recovery y Winch-out.
- [ ] **Prueba social**: hay 2 testimonios de 5★ más la imagen "Review us on Google". Agregar 4–6 reseñas reales con nombre y ciudad (Essex, Colchester, Williston) y fotos de la flota propia. No mostrar el conteo de Google mientras siga en 3.2★.
- [ ] **Confianza**: el dato de flota ("1 wrecker, 16 flatbeds, 4 light service trucks") es el mejor diferenciador; subirlo al hero. Agregar "Licensed & Insured" si aplica y el logo AAA (una reseña menciona que atienden llamadas de AAA). Confirmar con el cliente.
- [ ] **Páginas por servicio**: hoy todos los anuncios van a la home (24 URLs distintas en Ads, todas `/?gad_source=…`). Ver la lista abajo.
- [ ] **Consistencia de horario y teléfono entre sitios**: el sitio principal dice "Monday – Sunday (7am – 11pm)" en el footer y la landing dice 24/7. Si de 11pm a 7am no contesta nadie, los anuncios no deben correr 24h (brief: PENDIENTE quién contesta de noche).

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| spillanestowingrecovery.com/ (landing Ads) | **Ninguno** (hero sin heading; H2: Services, About Us, Why Choose Us…) | "Get A Free Quote" (#contact) + "Call Now (802) 216-3105" en header y en cada servicio | 6 campos, al fondo, envío inline (no confirmado) | `tel:(802)2163105` en header (3 variantes de header, probablemente sticky; verificar en móvil) | 2 testimonios 5★ + imagen "Review us on Google" | One-page, sin menú (bien). Link saliente al GBP. Servicios: Light-Duty, Accident Recovery, Roadside, Lockouts |
| spillanestowingrecovery.com/privacy-policy/ | — | — | — | — | — | Única página adicional |
| spillanestowingandrecovery.com/ (sitio principal, no Ads) | "Stranded on the Road? We're Here to Help!" | "Submit Tow Request" → **public.towbook.com** (externo) | Externo (Towbook) | `tel:+18028637900` | 5 testimonios sin estrellas | Contadores rotos ("0+ Years", "0 Min"), footer "7am–11pm", "Reading Location". Menú: Services, Gallery, About, Location, /pick-up-and-delivery/, /specialized-transport/ |

**Teléfonos**: la landing usa **(802) 216-3105** y el sitio principal (802) 863-7900. Confirmar si el 216-3105 es una línea de tracking que desvía a la principal y quién contesta. PENDIENTE

## Tracking encontrado
No se pudo leer el HTML (`gtag`, `GTM-`, `AW-`, `G-`). Por los datos de conversión de la cuenta:
| Acción | Categoría | Conv. 90d | Lectura |
|---|---|---|---|
| Calls from Ads | PHONE_CALL_LEAD | 8 | Activo de llamada: no depende del sitio |
| Website Calls | PHONE_CALL_LEAD | 5 | Hay Google Tag con reemplazo de número en la landing, y funciona |
| Form Fill | SUBMIT_LEAD_FORM | 1 | Hay evento de formulario; método (thank-you vs. evento) sin confirmar |

GA4/GTM: PMM tiene acceso (brief). Verificar con Tag Assistant y GTM Preview.

## Velocidad
**PENDIENTE**: PageSpeed API devolvió 429 (sin clave). Indicadores de riesgo: header duplicado 3× en el DOM, imágenes PNG sin `alt` (logo 598×272 repetido ×7, iconos 150×150 PNG), hero de 1920 px y 4 familias de fuentes (Roboto, Bai Jamjuree, Days One y las globales de Elementor). Acción: configurar `PAGESPEED_API_KEY` o pasar el score manual.

## Landings que la estrategia va a necesitar
Con mercado chico y presupuesto de $989, no hace falta servicio×ciudad. Basta una página por familia de servicio, todas en el mismo dominio de Ads y con la misma plantilla:
1. `/towing/`: Emergency Towing 24/7 Burlington VT (servicio estrella)
2. `/accident-recovery/`: Accident & Collision Towing (ticket más alto; ligar con taller si aplica)
3. `/winch-out-recovery/`: Winch-out / Stuck Vehicle Recovery
4. `/flatbed-towing/`: opcional, si /strategy separa el ad group de flatbed (tienen 16 flatbeds)
5. `/thank-you/`: obligatoria

Lockout, cambio de llanta y long distance: **sin landing** hasta que el cliente confirme que le interesan (brief: servicios a evitar PENDIENTE).

## Qué ya rankea orgánico (Semrush)
La landing de Ads no rankea (2 keywords). El sitio principal (`spillanestowingandrecovery.com`):
| Keyword | Pos. | Vol. | Nota |
|---|---|---|---|
| spillane's service center | 1 | 210 | Marca del taller: el 44% del tráfico orgánico |
| spillane's towing | 1 | 140 | Marca: confirma que no hace falta pagar por ella |
| spillanes towing | 1 | 30 | Marca |
| towing in burlington | 4 | 70 | Genérico local |
| vt towing service | 5 | 40 | Genérico |
| recovery service near me | 9 | 170 | CPC $12.15 |
| handys towing | 22 | 210 | Competidor |
| sheehan's towing | 35 | 480 | Competidor |
| long distance towing near me | 38–45 | 480 | Servicio a confirmar |

La marca ya ocupa el #1 orgánico, lo que refuerza no pagar por ella. Los $170 en marca de los últimos 90 días van mayormente a recuperar clics que llegarían gratis.
