---
name: strategy
description: Cruza brief, auditoría, competencia y benchmark para definir tipo de campaña, estructura de campañas/ad groups, keywords, match types, presupuesto por fase y negativas. Escribe strategy.md. Usar cuando se pida "estrategia", "cómo estructuro la cuenta", "qué campañas hago".
---

# /strategy — Qué campañas, cómo divididas y con cuánto

## Requisitos
Lee `brief.md`, `audit-site.md`, `competitors.md`, `benchmark.md`. Si falta alguno, puedes continuar pero marca en el archivo qué supuestos hiciste por falta de ese input.

## Pasos
1. **Keyword research** por servicio del brief:
   - Keyword Planner vía API (`scripts/keyword_ideas.py --geo <ciudad>`) o Semrush `keyword_research` (`database` us/co, filtro por ciudad en la keyword).
   - Une con `data/competitors-keywords.csv`.
   - Clasifica cada término: **comercial** (pujar), **informacional/laboral/producto** (negativa), **competidor** (negativa), **marca propia** (campaña de marca aparte si el brief dice que lo buscan).
   - Guarda `data/keywords.csv`: keyword, volumen, CPC est., intención, servicio, ciudad, match sugerido.
2. **Decidir tipo de campaña** con esta lógica:
   - Siempre: **Search** por servicio.
   - **Marca**: solo si hay búsquedas de marca o competidores pujan por ella.
   - **LSA**: si US y categoría califica (pista paralela).
   - **Remarketing / RLSA**: fase 4, no ahora.
   - **PMax**: fase 5 condicionada; escribir explícitamente por qué no ahora.
   - **Display, Video, Demand Gen**: no para servicios locales salvo pedido expreso.
3. **Estructura**:
   - Campaña por servicio (o familia) con presupuesto propio: así el servicio estrella no compite por presupuesto con el que menos interesa.
   - Ad group por tema (STAG). Servicio × ciudad solo si esa combinación tiene ≥100 búsquedas/mes; si no, un grupo por servicio con inserción de ubicación.
   - Prioridad de presupuesto según "servicio estrella" y "servicio a evitar" del brief.
   - Un ad group "Emergencia/24-7" separado si el nicho lo tiene: intención y CPC distintos.
4. **Match types**: frase por defecto; exacta para los top 3–5 términos de cada grupo; amplia no.
5. **Presupuesto por fase** con el benchmark:
   - Fase 1: presupuesto del brief repartido por campaña (% según prioridad), con CPL objetivo = mediana del benchmark.
   - Regla de aprendizaje: cada campaña necesita ≥3× CPL/día; si no alcanza, consolidar campañas (menos campañas, más ad groups).
   - Fase 3+: reasignación según CPA real.
6. **Copy**: por ad group, 15 headlines + 4 descripciones en el idioma del mercado, H1 pinneado = término del grupo, usando los diferenciadores y ofertas del brief y los gaps de competitors.md. Extensiones: sitelinks (otros servicios), callouts (diferenciadores), snippets (servicios), llamada, ubicación.
7. **Landings**: mapear cada ad group a su URL. Si la landing no existe, listarla como requerida (alimenta roadmap pista Landing).
8. **Negativas**: universal + nicho + competidores + lo descartado en el research → `data/negatives-nicho.txt`.

## Salida: `clients/<slug>/strategy.md`
```markdown
---
cliente:
slug:
actualizado:
version: 1
supuestos: [lista de inputs faltantes]
---

# Estrategia Google Ads — <cliente>

## Resumen ejecutivo (5 líneas)
Tipo de campañas, cuántas, presupuesto, CPL objetivo, cuándo se espera tCPA.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |

## Estructura por campaña
### Campaña: <nombre>
| Ad group | Keywords (match) | Vol. est. | Landing | H1 pinneado |
Negativas específicas del grupo:

## Keywords descartadas y por qué
Tabla resumida (detalle en data/keywords.csv).

## Copy
Por ad group: headlines, descripciones, extensiones. (Puede ir en `data/ads-<campaña>.md` si es largo.)

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |

## Por qué NO (todavía) 
- PMax: ...
- Amplia: ...
- Display: ...

## Riesgos y supuestos
```

## Al terminar
Resume: N campañas, N ad groups, presupuesto por campaña, CPL objetivo, landings faltantes. Siguiente: `/roadmap`.
