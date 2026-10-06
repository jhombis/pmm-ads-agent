---
name: informe
description: Genera o actualiza el artefacto del cliente (plan en HTML, español + inglés) con el estilo PMM, a partir de sus archivos (brief, auditoría, competencia, benchmark, estrategia, roadmap, checklist, logs), y lo publica o republica en sus mismas URLs. Es el último paso de TODOS los skills; también usarlo cuando se pida "el artefacto", "el plan", "el informe", "la página", "el HTML" o "actualiza el plan" de un cliente o de un diagnóstico.
---

# /informe — Artefacto del cliente (ES + EN, estilo PMM)

Último paso del flujo: **todo skill que corra sobre un cliente o una cuenta termina aquí**. Jhombis siempre pide la página; no se pregunta si se quiere, se entrega.

## Requisitos
- Cliente con carpeta `clients/<slug>/` (o diagnóstico en `diagnostics/<cuenta>/`). Leer `brief.md` y `checklist.md` si existen.
- Estilo: `knowledge/estilo-informes/README.md`. Plantilla y validador: `scripts/informe_html.py`.
- **Referencia obligatoria**: `knowledge/estilo-informes/ejemplo-pro-phase-es.html` y `-en.html`, el plan de Pro Phase Electric que aprobó Jhombis. **Todo informe tiene que verse como ese**: mismas secciones, en el mismo orden, mismos componentes y la misma densidad de datos. Ábrelo antes de escribir y úsalo para ver cómo queda cada sección llena. Nunca copies de ahí datos, textos ni IDs: el validador lo detecta.

## Archivos y URLs
| Caso | Archivos | Dónde se guardan las URLs |
|---|---|---|
| Cliente | `clients/<slug>/plan-es.html` + `plan-en.html` | front matter de `roadmap.md` (`plan_es`, `plan_en`); si todavía no hay roadmap, en `brief.md` (al crear el roadmap se pasan allá) |
| Diagnóstico sin cliente | `diagnostics/<cuenta>/diagnostico-es.html` + `-en.html` | front matter del `.md` del diagnóstico (`informe_es`, `informe_en`) |

**Una pareja de URLs por cliente para siempre.** Si ya existen URLs, se republica en ellas (Artifact con `url`) y nunca se crea un artefacto nuevo. Si hay que empezar de cero, primero se busca con `Artifact action=list` para no duplicar.

## Pasos
1. **Inventario**: qué archivos del cliente existen y cuáles cambiaron desde la última publicación (el `actualizado` del plan contra el de cada archivo).
2. **Base**:
   - Si no existe el plan: `python scripts/informe_html.py new <es> <en>`. La plantilla ya trae las 12 secciones del ejemplo, el índice y el `<script>` con los renderizadores (pasos, línea de tiempo, fases, ad groups, H1, headlines, negativas, rúbrica, checklist con filtros, preguntas con botón de copiar). Solo se cambian los datos: el HTML de cada sección y los arrays del `<script>`. Los renderizadores no se tocan.
   - Si existe: se edita el que hay y se conserva el diseño; solo cambia el contenido.
   - Si un plan viejo no sigue esta estructura (p. ej. un `plan.html` de una sola versión), se rehace desde la plantilla, conservando sus URLs.
3. **Contenido**: una sección por cada archivo que exista, en este orden. Las que no tengan fuente no se incluyen ni se rellenan con supuestos.
   | # | `id` | Sección | Qué lleva (como en el ejemplo) | Fuente |
   |---|---|---|---|---|
   | 1 | `resumen` | Resumen | 4 KPIs · estado de la cuenta en $ con barra de gasto por categoría · la decisión en 5 líneas · matemática de presupuesto con 3 escenarios | brief, strategy, diagnose/log |
   | 2 | `evolucion` | Evolución · semana N | 4 KPIs del periodo · causa con barra visible/oculto · tabla diaria (IS, perdido por ranking y por presupuesto) · tabla por ad group · diagnóstico en 5 puntos | último log de /weekly-review o /diagnose |
   | 3 | `pasos` | Próximos pasos | número, título, detalle, responsable, B si bloquea; lo hecho como "✓ Hecho DD-mmm: …" | checklist, último log |
   | 4 | `fechas` | Fechas y fases | línea de tiempo con "hoy" + tarjetas por fase con fecha, chip de estado y condición de paso | roadmap |
   | 5 | `estrategia` | Estrategia | `cfg` (campaña, tipo, presupuesto, puja, conversiones, match, ubicación, horario del cliente y de la cuenta, apagado) · tabla de ad groups · presupuesto por fase | strategy, build log |
   | 6 | `anuncios` | Anuncios | vistas previas `.serp` · H1 por grupo con largo · pool de headlines y descripciones con largo · extensiones · qué no se promete | `data/ads-*.md` |
   | 7 | `negativas` | Negativas | barras por categoría · validación · quitadas o choques evitados | `data/*negatives*` |
   | 8 | `landing` | Landing | rúbrica 0/1/2 con B · landings que se necesitan · landings GHL con QA | audit-site, `landings/README.md` |
   | 9 | `mercado` | Benchmark y competencia | tabla de cuentas comparables (anonimizadas) + la del cliente · competidores · oportunidades y amenazas | benchmark, competitors |
   | 10 | `checklist` | Checklist | espejo completo de checklist.md con filtros por responsable y estado | checklist |
   | 11 | `cliente` | Pendientes del cliente | preguntas con B + mensaje listo para copiar en el idioma del cliente | pendientes del brief/checklist |
   | 12 | `porque` | Por qué no (todavía) | PMax, broad, Display, marca, remarketing y otro descarte del nicho, cada uno con su condición · riesgos y supuestos | strategy |

   Resumen, Próximos pasos y Checklist son obligatorias. Las demás se omiten **solo** si no existe su archivo fuente: se borran completas, junto con su enlace del índice y su bloque del `<script>`. No se cambia el orden ni se inventan secciones nuevas (si hace falta una, primero se agrega a la plantilla y a `SECTIONS` en `scripts/informe_html.py`).

   Las cifras son exactas y salen de los archivos; nada inventado. El dinero se expresa sobre el gasto rastreable.
4. **Versión en inglés**: mismo contenido y diseño, traducido completo (textos, datos del script, etiquetas y `lang="en"`). Los anuncios y las keywords quedan tal cual.
5. **Enlace cruzado**:
   - ES con "English version →" a la URL EN.
   - EN con "Versión en español →" a la URL ES.
   - En la primera publicación: publicar las dos, poner los enlaces y republicar.
6. **Validar**:
   - `python scripts/informe_html.py check <es> <en>` tiene que dar OK. Revisa logo, estilo, marcadores, orden de secciones, que ES y EN sean iguales y que no queden datos del ejemplo.
   - `node --check` del último `<script>`.
   - Captura con Playwright a 390 px y a 1280 px: ninguna sección vacía y sin scroll horizontal.
7. **Publicar** las dos con `Artifact`:
   - Con `url` si ya existen.
   - Si es la primera vez, `icon: "chart"` y una `description` de una línea.
   - `label` corto con lo que cambió (p. ej. "D7 review", "Horario 7–18 Central").
8. **Guardar** las URLs en el front matter que corresponda y actualizar `actualizado`.
9. **Índice del equipo**:
   - Registra o actualiza las URLs del cliente en `clients/informes.json` (`clientes.<slug>.informes`: título, idioma, url; `mercado` y `cuenta` si faltan). Marca `"anterior": true` en los que quedan reemplazados.
   - Corre `python scripts/indice_informes.py` y republica `clients/indice-informes.html` en la URL de `indice_url` (Artifact con `url`). Nunca crees un índice nuevo.
   - Haz commit de todo junto con los cambios del skill que lo disparó.

## Al terminar
Entrega los dos enlaces (ES y EN) y en una línea qué cambió en esta versión. Menciona que el índice del equipo quedó actualizado. Recuerda que el artefacto es privado: para que el cliente lo vea, Jhombis lo comparte desde el menú Share.
