---
cliente: Tuff Truck Towing
slug: tuff-truck-towing
url: https://www.tufftrucktowing.com/
actualizado: 2026-10-27
veredicto: REQUIERE AJUSTES ANTES DE LANZAR
score: 7/22 (velocidad sin dato: 7 de 20 medibles)
---

# Auditoría de landing — Tuff Truck Towing

**Cómo se leyó el sitio.** El proxy de la sesión bloquea el dominio, así que el contenido se sacó por dos vías:
- Leadpages `analyze_url`: estructura, textos y enlaces.
- `curl` de solo lectura desde el servidor Plesk de PMM: HTML crudo, tags, `tel:` y JSON-LD.

Se revisaron 3 páginas: `/`, `/hauling` y `/photo-gallery`. PageSpeed no corrió: no hay `PAGESPEED_API_KEY` y la API sin clave devolvió 429 (cuota diaria agotada).

## Veredicto
**Requiere ajustes antes de lanzar.** Hoy el sitio es una home genérica de grúa en Wix, y tiene cuatro problemas:
- No tiene formulario ni página de gracias.
- No tiene ninguna página para los servicios que se quieren pautar (equipment hauling, forklifts, contenedores).
- Muestra 4 números `tel:` distintos.
- El único tag de Google Ads es de una cuenta que no está en el MCC (AW-1004387232) y no registra ninguna conversión.

Además, el número de tracking ya está publicado en la web. Eso explica las llamadas que entran desde el 20-oct sin campaña.

## Bloqueantes (resolver en Fase 0)
- [ ] **Medición de llamadas.** Instalar el Google tag de la cuenta nueva de PMM (Wix → Marketing Integrations / Custom Code, en `<head>` de todas las páginas) y crear dos conversiones de llamada:
  - "llamada desde la web": número de reenvío de Google sobre el (918) 320-7595, que lo cambia solo a quien llega por un anuncio;
  - "llamadas desde anuncios": recurso de llamada, ≥60 s.

  Sin esto, Ads no se distingue de las ~6 llamadas/día que ya trae el sitio orgánico. Responsable: PMM, con acceso al Wix del cliente. 1.5 h.
- [ ] **Tag AW-1004387232.** Averiguar de quién es la cuenta. Si es del cliente o de una agencia anterior, pedir acceso o vincularla al MCC (puede traer historial). Si no se usa, quitarla para no medir doble. Responsable: Jhombis/Cliente. 0.5 h.
- [ ] **Formulario corto + página de gracias.** Formulario de ≤4 campos (nombre, teléfono, servicio, ubicación del vehículo o equipo) arriba en móvil, con redirección a `/thank-you` donde dispara la conversión. Hoy solo hay `mailto:`. Responsable: Cliente (Wix) o PMM con acceso. 2 h.
- [ ] **Un solo número de servicio.**
  - Hoy hay 4: (918) 320-7595 en header, cuerpo y pie; (918) 894-0368 en /hauling, 5 veces; (918) 638-6348 en el schema; y el fax (918) 994-7053 enlazado como `tel:`.
  - Hay que quitar el `tel:` del fax. El número de /hauling puede quedarse solo si esa página no se pauta.
  - Responsable: Cliente. 0.5 h.
- [ ] **Página por servicio pautado.** No existe ninguna página de equipment hauling, maquinaria, forklifts, skid steers, contenedores ni madera. `/hauling` es volteo de tierra, roca y asfalto por carga, otro servicio que el brief no menciona. Además está huérfana: no aparece en el menú. Se necesitan al menos 2 landings (ver abajo). Responsable: PMM (/landing) o Cliente (Wix). 4–6 h.

## Mejoras (Fase 2–3)
- [ ] **"24/7 SERVICE!" es el H1 de la home, pero el cliente dijo lun–vie 7:00–21:00.** Confirmar con el cliente. Si no es 24/7, corregir la web, y los anuncios no lo prometen. CallFire muestra llamadas contestadas un sábado.
- [ ] **Prueba social.** No hay reseñas ni estrellas en ninguna página. Agregar un widget del GBP con el número de reseñas y el promedio. Las fotos reales de grúa ya están: se conservan.
- [ ] **Confianza en la home.** "Family owned and operated · insured and permitted · DOT #3161444" solo aparece en /hauling. Hay que subirlo a la home junto a DPS #53342-W y MC #14954.
- [ ] **Oferta.** No hay ninguna; solo los medios de pago. Proponer una que el cliente sostenga (p. ej. "free quote for equipment hauling" o tarifa plana local).
- [ ] **Fugas.** "Experienced Driver? Apply Now!" está arriba del H1 y trae buscadores de empleo. Va al pie o a otra página. Los enlaces `mailto:` usan tres correos distintos (drbtruck@yahoo.com, drbtruck@gmail.com, dbothell1963@gmail.com), ninguno es el del brief (ar.tufftrucktowing@gmail.com), y eso es mala señal para la respuesta a leads.
- [ ] **Áreas de servicio del sitio.** La web lista Tulsa completa, Broken Arrow, Wagoner, Bixby, Coweta, Catoosa y Owasso. No menciona Claremore, e incluye Owasso y Wagoner, que no están en el brief. Las landings deben mostrar solo el área real.
- [ ] **Velocidad.** Correr PageSpeed móvil con clave. El HTML pesa 419 KB en la home y 589 KB en la galería, típico de Wix. Sin score no se puede juzgar.

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |
|---|---|---|---|---|---|---|
| `/` | "Tuff Truck Towing - 24/7 SERVICE! FAST, COURTEOUS, PROFESSIONAL & CLEAN!" | "Call Now! 918-320-7595" (barra superior) + "Call for Service Now!" | No (solo mailto) | 320-7595 ×4 · fax 994-7053 como tel | Fotos reales de grúa; sin reseñas | Servicios: light & medium-duty, flatbed, equipment hauling (una línea) y roadside (fuel, lockout, jumpstart, tires). DPS #53342-W, MC #14954. "Experienced Driver? Apply Now!" arriba |
| `/hauling` | "Tuff Truck Towing now also offers Hauling Services!..." | "Call Now! 918-894-0368" | No | 894-0368 ×5 · 320-7595 ×3 · fax | Foto del camión de volteo | Volteo de tierra, roca y asfalto por carga, con descuento por volumen. Family owned, insured, DOT #3161444. Fuera del menú |
| `/photo-gallery` | 3 H1 | Barra "Call Now!" | No | 320-7595 ×4 · fax | Galería de fotos | 589 KB de HTML |

Plataforma: **Wix** (`static.wixstatic.com`, metaSiteId, revisión 332), con selector EN/ES. Quién edita: el cliente; PMM no tiene acceso (PENDIENTE).

## Tracking encontrado
| Qué | Estado |
|---|---|
| Google Ads tag | **AW-1004387232** en las 3 páginas, solo `gtag('config')`. No hay eventos de conversión en el HTML. La cuenta no está en el MCC de PMM (Windsor). |
| GA4 (G-) / GTM | No hay |
| Meta Pixel | No hay |
| CallRail / DNI | No hay. El número de CallFire (918) 320-7595 está fijo en la web. |
| JSON-LD | LocalBusiness "Tuff Truck Sales & Towing", 5577 South 193rd East Avenue, Broken Arrow, OK 74014, telephone +1 918-638-6348. Sin `openingHours` ni `aggregateRating`. |
| Formulario | No hay |

**Origen de las llamadas al CTN:** el (918) 320-7595 es el teléfono principal de la web (barra, cuerpo, pie y meta description). Las 42 llamadas del 20 al 26-oct vienen, al menos en parte, del sitio orgánico (el sitio está #1 en "tuff truck towing" y "towing broken arrow" según Semrush). Falta saber si el GBP también lo usa.

## Velocidad
Sin dato. PageSpeed no corrió (sin clave; la API pública devolvió 429). Referencias de peso: HTML de 419 KB en `/`, 419 KB en `/hauling` y 589 KB en `/photo-gallery`; el servidor respondió en 0.13–1.7 s. Hay que pedirle el score a Jhombis o correr `scripts/pagespeed.py` con clave.

## Landings que la estrategia va a necesitar
Con el presupuesto aún pendiente y el límite de fragmentación, propongo 2 (o 3):
1. **Towing — Broken Arrow & East Tulsa** (light + medium-duty)
   - H1: "Light & Medium-Duty Towing in Broken Arrow & East Tulsa"
   - Llamada arriba, formulario de 4 campos, horario real, DPS/MC/seguro, reseñas, área real (BA, Bixby, Coweta, Catoosa, Tulsa al este de Memorial).
2. **Equipment & Container Hauling** (forklifts, skid steers, maquinaria, contenedores de 20 ft, madera)
   - H1: "Equipment, Forklift & Container Hauling — Broken Arrow / Tulsa"
   - Es intención planificada y B2B: formulario de cotización (qué se mueve, origen, destino, fecha) más llamada.
3. *(Si Claremore entra)* Towing Claremore, o la ciudad dentro de la landing 1 con inserción de keyword.

Dónde: en el Wix del cliente (él lo pidió: "we will be running ads to that site"), o con `/landing` en performancemediamarketing.com/tuff-truck-towing/ si el cliente no da acceso o no puede editar a tiempo. La decisión es de Jhombis.

## Qué ya rankea orgánico (Semrush, 26-oct)
52 keywords; ~136 visitas/mes.
- **Marca**: "tuff truck towing" en la posición 1 (90/mes).
- **Broken Arrow**: "towing broken arrow" 1 (50), "towing broken arrow ok" 2 (50), "tow truck broken arrow" 2 (30), "tow truck services in broken arrow ok" 4 (70).
- **Tulsa** (posiciones 16–23, sin tráfico): "tow truck tulsa" 17 (260), "towing service tulsa" 20 (390), "tow trucks in tulsa oklahoma" 16 (210).
- **Nada en equipment hauling, forklift ni containers**: hoy no hay relevancia para esos términos, y por eso hacen falta landings propias.
