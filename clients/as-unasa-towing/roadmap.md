---
cliente: A's Unasa Towing
slug: as-unasa-towing
D0: 2026-10-22
actualizado: 2026-10-22
fase_actual: 0
plan_es: https://claude.ai/artifact/RB9tc2syBAXv2GK9Y5d5mP
plan_en: https://claude.ai/artifact/CrPAZcEDg6j5hqZZMBC6ie
---

# Roadmap — A's Unasa Towing

> D0 = 2026-10-22 (Jhombis no indicó otra fecha). Cuenta nueva 730-795-5909, sin historial. Las fechas son proyección; manda la condición de paso.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Fundación | 2026-10-22 → 2026-11-05 (rango hasta 11-12; depende del cliente) | 🔄 en curso |
| 1 — Lanzamiento Search (1 campaña, 3 ad groups) | 2026-11-05 → 2026-11-12 | ⏳ pendiente |
| 2 — Limpieza D7 · D14 · D30 | 2026-11-12 · 2026-11-19 · 2026-12-05 | ⏳ pendiente |
| 2b — Max. clics → Max. conversiones | ~2027-02-05 (rango 2027-01-05 → 03-05) | ⏳ pendiente |
| 3 — tCPA | ~2027-05-19 (rango 2027-04 → no se alcanza con $396) | ⏳ pendiente |
| 4 — Remarketing (RLSA) | reevaluar 2027-05 con datos de GA4 | ⛔ probablemente no califica (audiencia <1,000/30d) |
| 5 — Performance Max | **no realista con $540/mes**; no antes de 2027-07 aunque suba el presupuesto | ⛔ bloqueada |
| 6 — Conversiones offline | fuera de alcance (sin CRM) | — |
| Pista Landing | bloqueantes 2026-10-22 → 11-02 · mejoras 11-05 → 12-05 | 🔄 en curso |
| Pista GBP y reseñas | ficha 2026-11-05 · verificación ~11-19 · 10 reseñas ~2027-01-15 | ⏳ pendiente |
| LSA | no aplica (towing no es categoría) | — |

## Fase 0 — Fundación
- **Fecha estimada**: 2026-10-22 → 2026-11-05. Los arreglos de landing que hace PMM toman D0+3 una vez que haya acceso a WordPress (+3 días). Varios bloqueantes dependen del cliente (ticket, horario, acceso, GBP): +7–14 días. Rango hasta 2026-11-12.
- **Condición de paso**: todas las tareas bloqueantes (B) de Fase 0 en `checklist.md` ✅.
- **Tareas**:
  1. **(Cliente) Ticket promedio y margen** por tipo de trabajo → CPL máximo. Si el ticket real está cerca de $79.99, la cuenta no es rentable hasta madurar (strategy.md): Jhombis decide si se lanza igual. **B**
  2. **(Jhombis) Gasto real en medios** del paquete de $1,200 (strategy.md usa $540). **B**
  3. **(Cliente) Horario real** y quién contesta de noche y el domingo. Define la programación. **B**
  4. **(Cliente) Proceso de respuesta a leads**: con 1 grúa y 1 conductor, quién atiende cuando el conductor está en un servicio (desvío, buzón con devolución en <15 min). CallFire ya muestra 1 abandonada de 3. **B**
  5. **(Cliente) Acceso a WordPress** para PMM. **B**
  6. **(PMM) Medición**: conectar Site Kit o GTM; conversiones "Calls from ads" ≥60 s, "Website calls" ≥60 s (número de reenvío de Google → (385) 473-9820) y formulario en /thank-you/; clic en teléfono como secundaria; probar con Tag Assistant. **B**
  7. **(PMM) Landing**: /towing-west-valley-kearns/ y /thank-you/, con formulario de 3 campos arriba en móvil (audit-site.md). **B**
  8. **(Cliente) GBP**: confirmar si existe. Si no, crearlo como área de servicio (la dirección puede ser virtual). Acceso de PMM. **B** para el activo de ubicación; no bloquea el lanzamiento de Search.
  9. **(Cliente) Área**: confirmar 84104, 84120 y Sandy.
  10. **(PMM) Cuenta**: facturación, recomendaciones automáticas apagadas, lista universal + `data/negatives-nicho.txt` (178), GA4 vinculado.
  11. **(Cliente) Logo**: elegir uno de los 4 conceptos (`logo/`) para reemplazar el placeholder "Logo." del header.
- **Riesgos**:
  - Cada semana de retraso pierde pico de invierno: en el MCC, diciembre y enero tienen 1.20–1.27× las conversiones del mes promedio, con el CPL más bajo del año ($11.48–12.02). Son 16 cuentas maduras de towing, mayormente de estados templados; en Utah, con nieve, el pico probablemente sea mayor (inferido, sin datos de Utah en el MCC).
  - Si el cliente no da acceso a WordPress, la landing se hace con `/landing` en performancemediamarketing.com/as-unasa-towing/ (+3–5 días).

## Fase 1 — Lanzamiento Search
- **Fecha estimada**: 2026-11-05 → 2026-11-12.
- **Condición de paso**: campaña activa 7 días, anuncios aprobados, ≥1 conversión registrada (llamada ≥60 s o formulario) y tasa de contestadas ≥80% en CallFire.
- **Qué se lanza** (strategy.md, F1):
  - Search | Towing | West Valley-Kearns | v1: AG1 Towing Near Me, AG2 Towing West Valley & SLC, AG3 Accident & Recovery.
  - $17.75/día si es 24/7 o $20.50/día con el domingo apagado. Max. clics con tope de CPC de $7.50. Frase + exacta. Presencia.
  - 1 RSA por grupo (`data/ads-search.md`), solo con los [C] que el cliente haya confirmado.
- **Riesgos**:
  - Con una geo de 4 ZIP (~152–184k habitantes) puede no gastarse el presupuesto: si el día 7 va por debajo del 70% con IS perdido por ranking <30%, se amplía la geo.
  - 1 conductor: una llamada pagada que no se contesta es desperdicio. Advertencia al cliente antes del lanzamiento (tarea 4 de F0).

## Fase 2 — Limpieza (D7 · D14 · D30)
- **Fechas**: D7 = 2026-11-12 · D14 = 2026-11-19 · D30 = 2026-12-05.
- **Condición de paso**: tres revisiones hechas (`log/`), negativas aplicadas y keywords sin impresiones en 30 días pausadas.
- **Qué se revisa**:
  - D7: search terms → negativas; gasto contra presupuesto (regla de geo); CPC promedio contra el tope de $7.50 (subir a $9 si choca y no se gasta); contestadas en CallFire.
  - D14: search terms; keywords con ≥$36 de gasto y 0 conversiones, marcadas para revisión.
  - D30: search terms; keywords sin impresiones pausadas; calidad de las llamadas con el cliente. **No** se reemplaza un RSA por "peor rendimiento": con ~75 clics por mes, la comparación es ruido (playbook §9).
- **2b — Paso a Maximizar conversiones**: con **15+ conversiones/mes limpias** (≥60 s), esperable en el mes 3–4 → **~2027-02-05** (rango 01-05 → 03-05). El pico de invierno puede adelantarlo.

## Fase 3 — Optimización de puja (tCPA)
- **Fecha estimada**: **~2027-05-19**.
- **Supuesto**:
  - conversiones/día = presupuesto diario ÷ CPL de benchmark: $17.75 ÷ $24–36 = 0.49–0.74/día. Eso da 15–22 conversiones/mes, que no llegan a 30 en 30 días.
  - 30 en 30 días exige ≥1/día, es decir, un CPL ≤ $17.75. Eso solo pasa con el CPL de una cuenta madura (mediana $13.52 → ~1.3/día), desde el mes 6.
  - Lanzamiento 2026-11-05 + 6 meses = 2027-05-05, +2 semanas por aprendizaje lento (presupuesto < 3× CPL de benchmark por día) = **2027-05-19**.
  - Con $396/mes de medios no se alcanza.
- **Condición de paso**: ≥30 conversiones en 30 días con tracking verificado.
- **Acción**: tCPA = CPA real observado de 30 días; reajustar presupuesto según CPA y capacidad (1 grúa).
- **Si no se cumple en fecha**: revisar la landing (conversión <5%), el presupuesto (propuesta de subir si IS perdido por presupuesto >40% con CPL ≤ $36) y las keywords. **No** forzar tCPA con menos datos: seguir en Max. conversiones.

## Fase 4 — Remarketing
- **Fecha estimada**: reevaluar 2027-05 con los datos de GA4.
- **Condición de paso**: audiencia ≥1,000 usuarios en 30 días.
- **Estado**: ⛔ probablemente no califica. Ads trae ~75 clics/mes y el dominio no tiene tráfico orgánico medible (Semrush sin datos). En towing la compra es urgente y no se repite, así que el valor es bajo incluso si califica.
- **Acción si califica**: RLSA en observación en Search; nada de Display remarketing con este presupuesto.

## Fase 5 — Performance Max
- **Fecha estimada**: no antes de 2027-07, y solo si sube el presupuesto.
- **Condición de paso**: todas las de `knowledge/estrategias/pmax-cuando-y-como.md`.
- **Si no califica** (hoy no califica, y es lo más probable también a 9 meses):
  - **Presupuesto**: PMax pide ≥3× el CPA objetivo por día, unos $40–54/día con CPA de $13.5–18. Hoy hay $17.75/día en total. Para cumplirlo hace falta ~$1,200–1,600/mes de medios, sin quitárselo a Search.
  - **tCPA**: requiere tCPA activo 4 semanas (Fase 3, ~2027-05).
  - **Assets**: faltan 5+ fotos reales, logo y video. Se arma desde ya: fotos de la grúa en servicio, el logo elegido y un video corto con fotos.
  - **Qué hacer**: quedarse en Search. La alternativa del playbook (Display remarketing) tampoco aplica con esta audiencia.

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance actual (sin CRM). Se reevalúa cuando el cliente tenga registro de trabajos con GCLID.

## Pista paralela — Landing (audit-site.md, 10/22)
| Ajuste | Tipo | Responsable | Fecha |
|---|---|---|---|
| Google tag + 3 conversiones (Site Kit o GTM) | Bloqueante F0 | PMM | 2026-11-02 (D+3 desde el acceso) |
| /thank-you/ + redirect del formulario | Bloqueante F0 | PMM | 2026-11-02 |
| /towing-west-valley-kearns/ con formulario de 3 campos arriba y llamada sticky | Bloqueante F0 | PMM | 2026-11-02 |
| Logo real en el header | Mejora (F1) | Cliente elige · PMM sube | 2026-11-05 |
| Horario coherente (footer, copy, grúa "24/7") | Mejora (F1) | Cliente confirma · PMM edita | 2026-11-05 |
| Header sticky en móvil | Mejora (F2) | PMM | 2026-11-12 |
| Formulario de Schedule A Tow: ids, tipos `email`/`tel` | Mejora (F2) | PMM | 2026-11-12 |
| Dirección y email en el footer (si la dirección recibe clientes) | Mejora (F2) | Cliente confirma · PMM | 2026-11-12 |
| /accident-recovery/: formulario arriba + foto real | Mejora (F2) | PMM + fotos del cliente | 2026-11-19 |
| Reseñas visibles (widget del GBP o 3 reseñas reales) | Mejora (F2) | Cliente + PMM | 2026-12-05 |
| Meta descriptions, schema, alt, compresión del header | Mejora (F2–3) | PMM | 2026-12-05 |

## Pista paralela — GBP y reseñas
- 2026-11-05: ficha existente identificada o creada como área de servicio; PMM con acceso.
- ~2026-11-19: verificación (los tiempos de Google varían; puede pedir video).
- Desde la verificación: vincular a Ads (activo de ubicación) y pedir reseña después de cada servicio. Meta orientativa: 10 reseñas hacia 2027-01-15. Stauffer's y 4 Wheel suman más de 1,000 (competitors.md).

## Pista paralela — LSA
- No aplica: towing no es categoría de Local Services Ads.

## Estacionalidad y ventanas
- En el MCC (16 cuentas de towing con conversiones los 12 meses, oct-2025 → sep-2026), el índice de conversiones es 1.20 en diciembre y 1.27 en enero, contra 0.76–0.83 en julio–septiembre. El CPL va de $11.48–12.02 en el pico a $15.09–15.95 en agosto–septiembre. Fuente: `knowledge/benchmarks/raw/towing-us-2026-10-21-monthly.csv`; los clics se mueven igual, así que parte del efecto puede ser presupuesto.
- **Conviene lanzar lo antes posible**: un lanzamiento el 5 de noviembre aprende en pleno pico. Si F0 se atrasa a diciembre, el aprendizaje cae en enero y las fases 2b–3 se corren en la misma medida.

## Historial de cambios
- 2026-10-22: creado (D0 = 2026-10-22).
