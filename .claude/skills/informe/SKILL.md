---
name: informe
description: Genera o actualiza el artefacto del cliente (plan en HTML, español + inglés) con el estilo PMM, a partir de sus archivos (brief, auditoría, competencia, benchmark, estrategia, roadmap, checklist, logs), y lo publica o republica en sus mismas URLs. Es el último paso de TODOS los skills; también usarlo cuando se pida "el artefacto", "el plan", "el informe", "la página", "el HTML" o "actualiza el plan" de un cliente o de un diagnóstico.
---

# /informe — Artefacto del cliente (ES + EN, estilo PMM)

Último paso del flujo: **todo skill que corra sobre un cliente o una cuenta termina aquí**. Jhombis siempre pide la página; no se pregunta si se quiere, se entrega.

## Requisitos
- Cliente con carpeta `clients/<slug>/` (o diagnóstico en `diagnostics/<cuenta>/`). Leer `brief.md` y `checklist.md` si existen.
- Estilo: `knowledge/estilo-informes/README.md`. Plantilla y validador: `scripts/informe_html.py`.

## Archivos y URLs
| Caso | Archivos | Dónde se guardan las URLs |
|---|---|---|
| Cliente | `clients/<slug>/plan-es.html` + `plan-en.html` | front matter de `roadmap.md` (`plan_es`, `plan_en`); si todavía no hay roadmap, en `brief.md` (al crear el roadmap se pasan allá) |
| Diagnóstico sin cliente | `diagnostics/<cuenta>/diagnostico-es.html` + `-en.html` | front matter del `.md` del diagnóstico (`informe_es`, `informe_en`) |

**Una pareja de URLs por cliente para siempre.** Si ya existen URLs, se republica en ellas (Artifact con `url`) y nunca se crea un artefacto nuevo. Si hay que empezar de cero, primero se busca con `Artifact action=list` para no duplicar.

## Pasos
1. **Inventario**: qué archivos del cliente existen y cuáles cambiaron desde la última publicación (el `actualizado` del plan contra el de cada archivo).
2. **Base**:
   - Si no existe el plan: `python scripts/informe_html.py new <es> <en>`.
   - Si existe: se edita el que hay y se conserva el diseño; solo cambia el contenido.
3. **Contenido**: una sección por cada archivo que exista, en este orden. Las que no tengan fuente no se incluyen ni se rellenan con supuestos.
   | Sección | Fuente |
   |---|---|
   | Resumen (4 KPIs, estado de la cuenta con el desperdicio en $, la decisión en ≤5 líneas, matemática de presupuesto) | brief, strategy, diagnose/log |
   | Próximos pasos (responsable, B si bloquea) | checklist, último log |
   | Fechas y fases (línea de tiempo + tarjetas con condición de paso) | roadmap |
   | Estrategia (`cfg`: puja, horario en hora del cliente y de la cuenta, geo, match; tabla de ad groups; presupuesto por fase) | strategy, build log |
   | Anuncios (vistas previas `.serp`, H1 por grupo, pool de headlines y descripciones, extensiones) | `data/ads-*.md` |
   | Negativas (barras por categoría) | `data/*negatives*` |
   | Landing (rúbrica) | audit-site |
   | Competencia | competitors |
   | Benchmark | benchmark |
   | Checklist completo (filtros por responsable y estado) | checklist |
   | Preguntas para el cliente (con botón de copiar, en inglés si el cliente es US) | pendientes del cliente |
   | Historial (fecha y cambio aplicado en la cuenta) | logs |

   Las cifras son exactas y salen de los archivos; nada inventado. El dinero se expresa sobre el gasto rastreable.
4. **Versión en inglés**: mismo contenido y diseño, traducido completo (textos, datos del script, etiquetas y `lang="en"`). Los anuncios y las keywords quedan tal cual.
5. **Enlace cruzado**:
   - ES con "English version →" a la URL EN.
   - EN con "Versión en español →" a la URL ES.
   - En la primera publicación: publicar las dos, poner los enlaces y republicar.
6. **Validar**: `python scripts/informe_html.py check <es> <en>` tiene que dar OK. Si hay JavaScript, además `node --check` del script.
7. **Publicar** las dos con `Artifact`:
   - Con `url` si ya existen.
   - Si es la primera vez, `icon: "chart"` y una `description` de una línea.
   - `label` corto con lo que cambió (p. ej. "D7 review", "Horario 7–18 Central").
8. **Guardar** las URLs en el front matter que corresponda y actualizar `actualizado`. Hacer commit junto con los cambios del skill que lo disparó.

## Al terminar
Entrega los dos enlaces (ES y EN) y en una línea qué cambió en esta versión. Recuerda que el artefacto es privado: para que el cliente lo vea, Jhombis lo comparte desde el menú Share.
