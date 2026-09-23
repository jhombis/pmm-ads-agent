---
name: audit-landing
description: Audita la URL/landing de un cliente para Google Ads (velocidad, oferta, formulario, llamada, prueba social, tracking) y decide si está lista para lanzar. Escribe audit-site.md. Usar tras /onboard o cuando se pida "revisar la página", "auditar landing".
---

# /audit-landing — ¿La página está lista para recibir tráfico pagado?

## Requisitos
Lee `clients/<slug>/brief.md` (URL, servicios, objetivo, quién edita la web).

## Qué hacer
1. **Fetch** de la home y de cada página de servicio que exista (WebFetch). Anota título, H1, CTA visibles, teléfono, formulario, prueba social, y si hay páginas por servicio o por ciudad.
2. **Velocidad**: `python scripts/pagespeed.py <url> --strategy mobile` (requiere `PAGESPEED_API_KEY`, opcional). Si no hay clave, usar WebFetch de `https://pagespeed.web.dev/` no funciona; en ese caso pide a Jhombis el score o estima con tamaño de página.
3. **Semrush `site_audit`** si el dominio está en un proyecto; si no, `domain_overview` para tráfico orgánico y keywords que ya rankea (sirve para la estrategia).
4. **Tracking**: buscar en el HTML `gtag`, `googletagmanager`, `G-`, `AW-`, `fbq`. Anotar qué hay.
5. **Formulario**: cuántos campos, si está above the fold en móvil, a dónde envía, si tiene página de gracias propia (URL) o solo mensaje inline (afecta conversión de Ads).
6. **Móvil**: clic para llamar (`tel:`) visible sin scroll; WhatsApp si es Colombia.
7. **Medición (playbook §7)**, antes que cualquier otra cosa: un solo teléfono en todo el sitio y que sea el número de reenvío de la conversión; formulario de prueba (mensaje de gracias, llegada del correo, conversión registrada en 24–48 h); acciones de conversión activas y si son leads reales o vistas y clics; recursos de llamada no en revisión ni rechazados; filtro de duración de llamada razonable; horario de atención contra programación de anuncios; en Elementor, Templates → Popups y acciones "After Submit" (popups heredados de otro cliente o con otro teléfono). Registrar la fecha de cada arreglo.

## Rúbrica (puntuar cada ítem 0/1/2)
| Ítem | 2 = bien | Bloqueante si 0 |
|---|---|---|
| Headline refleja el servicio buscado | Sí, por página de servicio | Sí |
| Formulario corto visible arriba (móvil) | ≤4 campos, sin scroll | Sí |
| Clic para llamar en móvil | Botón sticky o header | Sí |
| Oferta clara | Una oferta concreta visible | No |
| Prueba social | Reseñas con número + estrellas, logos, fotos reales | No |
| Confianza | Licencia, seguro, años, garantía | No (sí en nichos regulados) |
| Velocidad móvil | LCP < 2.5s / score ≥ 70 | Sí si score < 40 |
| Google Tag presente | Sí | Sí |
| Página de gracias medible | URL propia | Sí |
| Páginas por servicio | Una por servicio principal | No (recomendación fuerte) |
| Sin fugas | Sin menú gigante, links externos, pop-ups agresivos | No |

## Salida: `clients/<slug>/audit-site.md`
```markdown
---
cliente:
slug:
url:
actualizado:
veredicto: LISTA | LISTA CON MEJORAS | REQUIERE AJUSTES ANTES DE LANZAR
score: NN/22
---

# Auditoría de landing — <cliente>

## Veredicto
Una frase. Si hay bloqueantes, listarlos primero.

## Bloqueantes (resolver en Fase 0)
- [ ] ítem — qué hacer — responsable (PMM/Cliente) — esfuerzo (h)

## Mejoras (Fase 2–3)
- [ ] ...

## Detalle por página
| URL | H1 | CTA | Form | Tel | Prueba social | Nota |

## Tracking encontrado

## Velocidad
Score móvil, LCP, CLS, peso. Causas principales.

## Landings que la estrategia va a necesitar
Lista de páginas de servicio (o servicio×ciudad) que hay que crear, según brief. Esto alimenta /strategy.

## Qué ya rankea orgánico (Semrush)
Top keywords orgánicas: ayudan a saber qué términos ya tienen relevancia.
```

## Al terminar
Resume veredicto, bloqueantes y cuántas landings faltan. Siguiente: `/competitors` y `/benchmark-interno` si no corrieron; luego `/strategy`.
