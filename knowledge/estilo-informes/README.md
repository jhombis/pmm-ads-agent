# Estilo de informes PMM

Todo informe, plan o resumen en HTML que salga del agente (planes de cliente, `/weekly-review`, `/diagnose`, reportes para el cliente) usa **este estilo**: logo PMM, paleta, tipografías y componentes de `plantilla.html`. La referencia viva es el plan de Pro Phase Electric (`clients/pro-phase-electric/plan-es.html`).

## Flujo
1. `python scripts/informe_html.py new clients/<slug>/<nombre>-es.html clients/<slug>/<nombre>-en.html`: copia la plantilla con el logo ya insertado.
2. Llenar los `{{MARCADORES}}` y borrar las secciones que no apliquen. Se pueden agregar secciones, siempre con los componentes de abajo. **No se edita el `<style>`**; si un informe necesita un componente nuevo, se agrega primero a la plantilla y a esta guía.
3. Publicar las dos versiones como artefactos, poner en cada una la URL de la otra y republicar. Guardar las URLs en el front matter (`plan_es`/`plan_en` en `roadmap.md` o el archivo que corresponda).
4. `python scripts/informe_html.py check <es> <en>` debe dar OK antes de la publicación final. Al actualizar, se republican las dos en sus mismas URLs.

## Marca
- **Logo**: `pmm-logo.webp` (Performance Media Marketing, formas de colores más texto negro). Va arriba a la izquierda del masthead, sobre una placa blanca (`--logo-plate`, también en modo oscuro), 46 px de alto y embebido en base64, porque el artefacto no carga archivos locales. No se recolorea, no se recorta ni se estira.
- **Pie**: siempre `Performance Media Marketing · <Cliente> · cuenta <ID>` más las fuentes o el periodo de datos.
- **Tono visual**: editorial y sobrio. Fondo blanco, tinta casi negra y una regla gruesa negra bajo el masthead. El color se reserva para datos y estados, nunca para decorar.

## Paleta (tokens en `:root`; el modo oscuro se redefine en la plantilla)
| Token | Claro | Uso |
|---|---|---|
| `--ink` / `--ink-2` / `--muted` | #121216 / #3A3B45 / #6A6C78 | Texto principal, secundario y apagado |
| `--ground` / `--surface` / `--surface-2` / `--line` | #FFFFFF / #F5F5F8 / #ECECF2 / #E2E2EA | Fondo, callouts, pistas de barras, bordes |
| `--red` | #E0452B | Fase 0, desperdicio, bloqueos |
| `--orange` | #F39A1E | Fase 1, competidores |
| `--yellow` | #F5C518 | Fase 2 |
| `--green` | #22A55B | Fase 3, lo que funciona |
| `--sky` | #4F8FD6 | Fase 4, genéricos, foco |
| `--purple` | #86479A | Fase 5, DIY o producto |
| `--blue` | #27409C | Enlaces, landings, titulares de anuncio |
| `--ok`/`--warn`/`--bad` (+ `-bg`) | verde / ámbar / rojo | Chips de estado |

Los colores de datos salen del logo (bola amarilla, cubo morado, cubo verde, bola naranja, bola roja, triángulo celeste, cubo azul). **El color de cada fase es fijo** en todos los informes: F0 rojo · F1 naranja · F2 amarillo · F3 verde · F4 celeste · F5 morado · F6 gris.

## Tipografía
- Títulos, eyebrows, chips y etiquetas: **Red Hat Display** (700/900).
- Texto: **Source Sans 3** (400/600/700).
- IDs de cuenta, fechas de fase y keywords: **JetBrains Mono**.
- Las tres se cargan de Google Fonts. Los números van con `.num` (cifras tabulares).

## Componentes (clases de la plantilla)
| Componente | Clase | Cuándo |
|---|---|---|
| Masthead | `header.mast` + `.logo` + `dl.meta` | Siempre: logo, cliente, subtítulo, enlace al otro idioma, cuenta, fase y fecha |
| Índice fijo | `nav.toc` | Siempre que haya 3+ secciones |
| Sección | `section` + `.sec-head` (h2 + una línea de contexto) | Cada bloque |
| KPIs | `.kpis` > `.kpi` (4, o 2 en móvil) | Las cifras que deciden: pauta, CPL, prospectos, hito |
| Estado + decisión | `.two` con texto, `.bar-spend` + `.legend` y `.callout` | Resumen: el desperdicio en dinero y la decisión en ≤5 líneas |
| Pasos | `.steps` > `.step` (nº, texto, `.who`, chip, `.b-flag` si bloquea) | Próximos pasos con responsable (PMM / Cliente) |
| Configuración | `dl.cfg` | Ajustes de campaña: puja, horario, geo, match |
| Tabla | `.tbl` > `table` (`.r` para números, `.kw` para keywords) | Datos, ad groups, search terms |
| Fases | `.phases` > `.phase` con `--c`, `.when` y `.cond` (condición de paso) | Roadmap; toda fase lleva fecha y condición |
| Línea de tiempo | `.tl-*` (ver `plan-es.html`) | Roadmap con fechas |
| Checklist | `.cl-phase` > `.cl-item` con `.box` / `.box.done` / `.box.part` | Checklist por fase |
| Anuncio | `.serp` (`.spon`, `.url`, `.hl`, `.ds`) | Vista previa de RSA |
| Barras | `.negbars` / `.negbar` | Conteos por categoría |
| Chips | `.chip` + `st-done`/`st-run`/`st-todo`/`st-block`/`st-pause` | Estado: Hecho, En curso, Pendiente, Bloqueado, Pausado |

## Reglas
- **Bilingüe siempre** (CLAUDE.md): `-es.html` y `-en.html`, con el mismo contenido y diseño, y cada una enlazada a la otra.
- Responsivo hasta 390 px, sin scroll horizontal de página (las tablas y la línea de tiempo hacen scroll dentro de su caja).
- Modo claro y oscuro con los tokens de la plantilla; nada de colores sueltos fuera de `:root`.
- Cifras en dinero y sobre el gasto rastreable ("$50.46 de $212.89"), como en el playbook; nada de adjetivos.
- Sin datos sensibles: no poner credenciales, tokens ni teléfonos personales. El ID de la cuenta y el del MCC sí van.
- `localStorage` solo para comodidades (filtros), dentro de `try/catch`.
