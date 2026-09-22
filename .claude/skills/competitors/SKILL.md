---
name: competitors
description: Analiza competidores de un cliente en búsqueda pagada (keywords, copies, landings, ofertas) usando Semrush y búsqueda web. Escribe competitors.md. Usar tras /onboard o cuando se pida "competencia", "qué hacen los competidores".
---

# /competitors — Qué están pagando y prometiendo los competidores

## Requisitos
Lee `clients/<slug>/brief.md`: competidores declarados, nicho, ciudad, país, idioma.

## Pasos
1. **Descubrir competidores en pagado** (no solo los que el cliente nombró):
   - Semrush `competitors_research` → reporte de competidores en paid search para el dominio del cliente (si tiene historial) o para el competidor principal.
   - Semrush `paid_search_research` → keywords pagadas, posiciones, copies de anuncios por dominio competidor. `database`: `us` o `co`.
   - Búsqueda web `"<servicio> <ciudad>"` para ver quién aparece hoy en anuncios y LSA (anotar 3 capturas de texto de anuncios).
2. Para cada competidor (máx. 6): dominio, keywords pagadas estimadas, gasto estimado, top 10 keywords, 3 copies de anuncio, landing a la que envían, oferta visible, prueba social, teléfono/formulario, reseñas GBP (búsqueda web).
3. **Gap de keywords**: términos que 2+ competidores pagan y el cliente no cubre en brief. Clasificar por intención (comercial / descartar).
4. **Gap de oferta**: qué prometen (same-day, free estimate, financing, garantía) vs lo que el cliente puede sostener según brief.

## Salida: `clients/<slug>/competitors.md`
```markdown
---
cliente:
slug:
actualizado:
fuente: semrush + web
---

# Competencia — <cliente>

## Mapa
| Competidor | Dominio | KW pagadas | Gasto est./mes | Reseñas GBP | Oferta principal |

## Qué pagan (top keywords compartidas)
| Keyword | Vol. | CPC | # competidores | Intención | ¿Cubrir? |

## Cómo anuncian
Por competidor: 2–3 headlines/descripciones reales, ángulo (precio, rapidez, confianza), extensiones vistas.

## A dónde envían
Landing por competidor: tipo (home / servicio / ciudad), formulario, teléfono, oferta.

## Oportunidades para <cliente>
- Ángulos que nadie usa
- Keywords con intención sin competencia fuerte
- Ofertas que el cliente puede igualar o superar (según brief)

## Amenazas
- Competidores con mucho más presupuesto o reseñas
- Términos donde el CPC será alto

## Keywords a NO pujar
Marcas de competidores y términos que solo ellos pueden sostener.
```

Guarda los datos crudos en `clients/<slug>/data/competitors-keywords.csv`.

## Al terminar
Resume 3 oportunidades y 2 amenazas. Siguiente: `/strategy` (cuando audit y benchmark estén listos).
