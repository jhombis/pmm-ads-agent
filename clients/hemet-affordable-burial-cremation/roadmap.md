---
cliente: Hemet Affordable Burial and Cremation
slug: hemet-affordable-burial-cremation
D0: 2026-10-01
actualizado: 2026-10-01
fase_actual: 0
---

# Roadmap — Hemet Affordable Burial and Cremation

> **Cuenta activa** (751-429-2721, desde el 07/05/2026). No hay "lanzamiento" desde cero: Fase 0 limpia y verifica sobre la cuenta en vivo **sin pausarla**, y Fase 1 publica la reestructura de `strategy.md`.
> Inputs faltantes: `audit-site.md` (sitio no auditado) y `benchmark.md` formal. Las fechas de Fase 0 asumen que **el cliente edita el sitio** (+7 días) hasta que /audit-landing diga lo contrario.
> **Aviso de presupuesto**: $49/día < 3× CPL benchmark ($73 × 3 = $219/día, `benchmark.md`). El aprendizaje será lento, tCPA no es alcanzable con este presupuesto y PMax no califica.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Fundación / limpieza | 2026-10-01 → 2026-10-12 | 🔄 en curso |
| 1 — Reestructura Search publicada | 2026-10-13 → 2026-10-20 | ⏳ |
| 2 — Limpieza D7 · D14 · D30 | 2026-10-20 · 2026-10-27 · 2026-11-12 | ⏳ |
| 3 — tCPA | ⛔ no alcanzable con $1,500/mes (detalle abajo); próximo checkpoint 2027-01-15 | ⏳ |
| 4 — Remarketing (RLSA) | ⛔ la audiencia no llega a 1,000 usuarios en 30 días con el tráfico actual | ⏳ |
| 5 — Performance Max | ⛔ no califica (fallan 4 de 6 condiciones) | ⏳ |
| 6 — Conversiones offline | Fuera de alcance (sin CRM) | — |
| Pista Landing | 2026-10-02 → 2026-10-12 (bloqueantes) | ⏳ |
| Pista GBP / reseñas | 2026-10-01 → continuo | ⏳ |
| Pista Español (condicional) | Desde 2026-11-12 si se confirma personal hispanohablante | ⏳ |
| Pista LSA | Verificación única 2026-10-03; probablemente no aplica | ⏳ |

## Fase 0 — Fundación / limpieza (sobre cuenta en vivo)
- **Fecha estimada**: 2026-10-01 → 2026-10-12 (D0+11; +7 días si el cliente tarda en el sitio o el GBP → 2026-10-19)
- **Condición de paso**: todas las tareas bloqueantes de Fase 0 en `checklist.md` ✅
- **Tarea crítica (día 1)**: `audit-site.md` encontró que **el sitio no tiene Google Tag**. Form Fill y Website Calls no registran desde mediados de septiembre, y la puja automática solo ve las llamadas desde el anuncio. Instalar el tag, el número de reenvío y la página de gracias (PMM, ~3 h con acceso a WordPress).
- **Tareas — quick wins (aplicar ya, PMM, día 1–2)**. Cortan unos $230/mes de desperdicio sin esperar al resto:
  1. (PMM) Pausar "Responsive Display" ($31/mes, 0 conv).
  2. (PMM) Aplicar la lista "PMM Universal" **sin** `cheapest`, `county` ni `rental` (ver `data/negatives-nicho.txt`) más la lista de nicho "Funeral - Hemet" a nivel de cuenta.
  3. (PMM) Agregar la marca como negativa en la campaña genérica actual. Hasta que exista la de marca, se puede dejar; se aplica junto con la Fase 1.
  4. (PMM) Revisar la geo actual ("Radius"): pasarla a presencia y a las ciudades del brief. Hay search terms de Palm Springs, Lake Elsinore y Menifee.
- **Tareas — verificación (bloqueantes)**:
  5. (PMM) "Calls from Ads": subir la duración mínima a **90 s** (hoy 21 de las 30 conversiones vienen de aquí; validar calidad).
  6. (PMM) "Form Fill": envío de prueba con Tag Assistant y confirmar que dispara solo en la página de gracias.
  7. (PMM) "Website Calls" existe (5 conv en 90 días), así que hay número de reenvío en el sitio: confirmar que funciona en todas las páginas y que el cliente lo conoce.
  8. (PMM) "Clicks to call" y las acciones locales quedan como secundarias (ya lo están). Verificar que no entren en "Conversiones".
  9. (PMM) Recomendaciones automáticas: confirmar que están apagadas. Socios de búsqueda y Display en la campaña Search: apagados.
  10. (Cliente → PMM) Verificar el GBP nuevo y dar acceso a PMM; vincularlo como activo de ubicación. **Desvincular la ficha de Inland Memorial** si estuviera ligada.
  11. (Cliente) Margen por caso y precio del paquete de servicios completos, para fijar el CPL máximo real. Hoy el supuesto es $60 y el benchmark $73.
  12. (Cliente) Confirmar quién contesta de noche y el tiempo de respuesta a formularios.
  13. (Jhombis) Confirmar el presupuesto ($1,500 de pauta vs "$2800" del nombre de la cuenta) y aprobar sumar Valle Vista, East Hemet y Homeland a la geo.
  14. ✅ `/audit-landing` corrido el 2026-10-01 (11/22). Pendiente: acceso a WordPress para resolver sus bloqueantes.
- **Riesgos**:
  - El GBP nuevo comparte dirección con la ficha de Inland Memorial: riesgo de suspensión o de duplicado. Si se suspende, Fase 1 sale sin activo de ubicación.
  - Subir la duración mínima de llamada va a "bajar" las conversiones reportadas. Es esperado: corrige la señal, no empeora la cuenta.

## Fase 1 — Reestructura Search publicada
- **Fecha estimada**: publicar el 2026-10-13; condición evaluada el 2026-10-20
- **Condición de paso**: campañas nuevas activas 7 días, anuncios aprobados, ≥1 conversión registrada con la configuración nueva
- **Qué se lanza** (según `strategy.md`, Fase 1):
  - "Search | Funeral & Cremation | Hemet Valley": 4 ad groups (Funeral Home, Cremation, Affordable, Burial), solo frase y exacta, $44/día, Maximizar conversiones sin tCPA, 24/7.
  - "Search | Brand": $5/día, Maximizar clics con CPC máx. $3.
  - Campaña actual "ENHPRM Radius": se pausa el mismo día. **No se borra**, para conservar el histórico.
  - 3 RSA por grupo (`data/ads-search.md`), extensiones y activo de ubicación del GBP nuevo.
- **Riesgos**:
  - Campaña nueva implica aprendizaje. Esperar 1–2 semanas con un CPA peor antes de juzgar.
  - Al quitar la amplia baja el volumen de clics. Si el gasto queda debajo del 70% del presupuesto, ampliar variantes en frase (no volver a la amplia).
  - Si las landings de servicio no están listas, los grupos apuntan a la home de forma temporal (no bloquea).

## Fase 2 — Limpieza (D7 · D14 · D30 desde publicación)
- **Fechas**: 2026-10-20 · 2026-10-27 · 2026-11-12
- **Condición de paso**: tres revisiones hechas con `/weekly-review`, negativas aplicadas, keywords con 0 impresiones en 30 días pausadas
- **Qué se revisa**:
  - Search terms: competidores nuevos, fuera de área, informacional.
  - Gasto sin conversión: más de $100 sin conversión en una keyword se marca para revisión.
  - RSA peor por grupo, reemplazado el D30.
  - Feedback del cliente sobre calidad de llamadas: ¿cuántas se volvieron casos y de qué tipo (directo vs completo)?
- **Meta de salida de Fase 2 / F1 de strategy**: ≥12 conv/mes, CPA ≤ $100 y desperdicio en search terms <10%.

## Fase 3 — Optimización de puja (tCPA)
- **Fecha estimada**: **no alcanzable con el presupuesto actual.** Checkpoint de reevaluación: **2027-01-15**.
  - Supuesto: $49/día ÷ CPL benchmark $73 = **0.67 conv/día ≈ 20 conv en 30 días**. El histórico real fue de 7–18.5 conv/mes. Para llegar a 30 en una ventana de 30 días hace falta ~1 conv/día, es decir **~$2,200/mes** a CPA $73.
  - Estacionalidad a favor: la mortalidad sube entre diciembre y febrero (temporada de gripe), así que el volumen de conversiones puede subir en esa ventana sin aumentar presupuesto. Por eso el checkpoint es a mediados de enero.
- **Condición de paso**: ≥30 conversiones (llamada ≥90 s + formulario verificado) en ventana de 30 días
- **Acción**: tCPA = CPA real observado de los últimos 30 días; reajustar presupuesto
- **Si no se cumple**: seguir con Maximizar conversiones sin tCPA. No forzar tCPA con menos datos. Opciones para Jhombis y el cliente:
  1. subir el presupuesto a ~$2,500/mes;
  2. mejorar la conversión de la landing (si es <5%, ese es el cuello de botella);
  3. aceptar Maximizar conversiones como estrategia estable, que en esta escala es razonable.

## Fase 4 — Remarketing (RLSA)
- **Fecha estimada**: ⛔ no proyectable. Search trae ~110 clics al mes y el orgánico es mínimo (Semrush ~8 visitas/mes). La lista no llega a 1,000 usuarios en 30 días, que es el mínimo de Google para usar audiencias en Search.
- **Condición de paso**: audiencia de visitantes ≥1,000 en 30 días
- **Acción**: crear la audiencia desde la Fase 0 para que vaya acumulando. Si algún día califica, RLSA en observación y luego ajuste de puja. **Nada de Display remarketing**: el Display actual mostró 0 conversiones.

## Fase 5 — Performance Max
- **Fecha estimada**: ⛔ no califica en el horizonte visible. Se reevalúa junto con Fase 3 (2027-01-15).
- **Condiciones** (`knowledge/estrategias/pmax-cuando-y-como.md`):
  | Condición | Estado | Qué haría falta |
  |---|---|---|
  | Search ≥4 semanas estable con tCPA | ❌ | Fase 3 (presupuesto) |
  | ≥30 conv/mes con tracking verificado | ❌ (~12) | Presupuesto ~$2,500 o mejor conversión |
  | Un ciclo de limpieza D30 completo | ⏳ | 2026-11-12 |
  | Assets propios (5+ fotos reales, logo, video) | ❓ | Pedir fotos de capilla e instalaciones al cliente |
  | Landing ≥5% de conversión + antispam | ❓ | /audit-landing |
  | ≥3× CPA/día de presupuesto | ❌ ($49 vs $219) | — |
- **Nota**: las otras funerarias del MCC tienen PMax con CPA de $21–57. Antes de usarlo como argumento, `/benchmark-interno` debe auditar qué conversiones cuentan.
- **Si no califica**: quedarse en Search + negativas + mejora de landing. Es lo correcto para esta escala.

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance (sin CRM). Mientras tanto, pedir al cliente una hoja mensual simple con fecha, teléfono del lead, si se convirtió en caso y de qué tipo. Así se puede medir el costo por caso a mano.

## Pista paralela — Landing
- **Bloqueantes (Fase 0, fecha 2026-10-12)**:
  - ✅ GPL publicado (PDF 2026-03-25).
  - (PMM) **Google Tag** en todo el sitio, número de reenvío y página de gracias con la conversión verificada (audit-site.md).
  - (PMM) Sacar la home de las URLs finales de los grupos genéricos.
- **Mejoras (Fase 2–3, objetivo 2026-11-12)**:
  - (Cliente / PMM) Landing de **servicios completos** con precio "desde", fotos reales de la capilla, sala de velación y salón de recepción. Es el servicio estrella y hoy no tiene página dedicada confirmada.
  - (Cliente / PMM) Landings /cremation y /burial con el término en el H1.
  - (Cliente) Reseñas visibles en el sitio en cuanto el GBP nuevo las tenga.

## Pista paralela — GBP y reseñas
- 2026-10-01: verificar el GBP nuevo y dar acceso a PMM (cliente).
- 2026-10-12: vincularlo al activo de ubicación (PMM).
- Continuo: el cliente pide reseña a cada familia atendida, después del servicio y con tacto. Meta: **10 reseñas para 2026-12-31**. Sin reseñas, el anuncio en Maps y el CTR quedan débiles frente a Miller-Jones o Hemet Valley Mortuary.

## Pista paralela — Español (condicional)
- Condición: el cliente confirma personal hispanohablante que conteste 24/7.
- Desde 2026-11-12 (después del D30): ad group "Funeraria" con `funerarias cerca de mi` (1,900/mes nacional; ya convirtió 1 vez), copy en español e idioma ES agregado a la campaña. Sale del mismo presupuesto, sin aumento.

## Pista paralela — LSA
- 2026-10-03: verificación única de si "funeral home" está disponible en LSA para Riverside County. Lo más probable es que no aplique: no es una categoría habitual. Si no aplica, se cierra la pista.

## Estacionalidad y ventanas
- **Dic–feb**: pico estacional de mortalidad en EE.UU. Conviene que la reestructura esté estable antes del 2026-12-01 (Fase 2 D30 = 2026-11-12 ✅). Si el cliente tiene capacidad, es la ventana para proponer un aumento temporal de presupuesto.
- Feriados (Thanksgiving, Navidad): las llamadas siguen entrando, porque el cliente contesta 24/7. No pausar.

## Historial de cambios
- 2026-10-01: creado (D0 = 2026-10-01).
- 2026-10-01: /audit-landing → Google Tag ausente pasa a tarea crítica del día 1; GPL ✅; landings mapeadas.
