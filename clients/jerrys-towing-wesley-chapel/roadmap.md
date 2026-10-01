---
cliente: Jerry's Auto Body Solutions & Towing Service
slug: jerrys-towing-wesley-chapel
D0: 2026-10-01
actualizado: 2026-10-01
fase_actual: 0
plan_es: https://claude.ai/artifact/4BPtSrAmvJSYaeFhXCKvBE
plan_en: https://claude.ai/artifact/7SLqmrgbKmMYWC8AaPtjDC
---

# Roadmap — Jerry's Auto Body Solutions & Towing Service

> **Contexto:** la cuenta ya sirve desde el 22/08/2026 con la plantilla ENHPRM ($25/día, CPL de $38.50 en septiembre). Este roadmap **no pausa la campaña**: la Fase 0 sanea la medición y la configuración con la campaña corriendo, y la Fase 1 es el **relanzamiento con la estructura de `strategy.md`**, no un lanzamiento desde cero. Se pausaría solo si la verificación muestra que "Website Calls" y "Form Fill" no miden leads reales.
>
> **D0 = 2026-10-01** (hoy; Jhombis no indicó otra fecha).

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Fundación / saneamiento | 10/01 → 10/06 (PMM) · 10/15 (pendientes del cliente) | 🔄 en curso |
| 1 — Relanzamiento Search reestructurado | 10/06 → 10/13 | ⏳ |
| 2 — Limpieza (D7 · D14 · D30) | 10/13 · 10/20 · 11/05 | ⏳ |
| 3 — tCPA | **⛔ no alcanzable a $25/día.** Si se sube a $35/día el 12/01 → ~2027-01-15 | ⛔ bloqueada por presupuesto |
| 4 — Remarketing | No realista con el tráfico actual (~90 clics/mes) | ⛔ |
| 5 — Performance Max | No califica (ver razones) | ⛔ |
| 6 — Conversiones offline | Fuera de alcance (sin CRM) | — |
| Pista Landing | 10/01 → 10/10 (bloqueantes) · 10/31 (mejoras) | 🔄 |
| Pista LSA | Verificar elegibilidad 10/03 · verificación 10/15–10/29 (si hay GBP) | ⏳ bloqueada por GBP |

## Fase 0 — Fundación / saneamiento
- **Fecha estimada**: 2026-10-01 → **2026-10-06** para las tareas de PMM (los bloqueantes de landing los edita PMM: +3 días). Los pendientes del cliente llegan hasta el **2026-10-15** (+7–14 días), pero solo bloquean partes concretas (ver abajo), no el relanzamiento entero.
- **Condición de paso**: todos los ítems marcados **[B]** en `checklist.md` (Fase 0) en ✅.
- **Tareas**:
  - [B] (PMM) Verificar con Tag Assistant las 3 conversiones: **Website Calls** (¿desvío de Google o clic en `tel:`?), **Form Fill** (¿qué la dispara sin página de gracias?) y **Calls from Ads** (duración ≥60 s). Lo que no sea un lead real pasa a secundaria.
  - [B] (PMM) Crear `/thank-you/`, redirigir ahí el formulario de Elementor y mover la conversión Form Fill a la carga de esa página.
  - [B] (PMM) Verificar que la ubicación esté en **Presencia** y el radio en **20 mi** desde 3645 New River Rd.
  - [B] (PMM) Aplicar negativas de cuenta (`data/negatives-nicho.txt`, que incluye la universal con excepciones) vía `/negatives`. **Requiere OK de Jhombis.**
  - [B] (PMM) Verificar que la aplicación automática de recomendaciones esté **desactivada** (la plantilla ENHPRM puede tenerla activa).
  - (PMM) Campos ocultos UTM + GCLID en el formulario.
  - (Cliente, vía Jhombis) Ticket promedio, margen y tasa de cierre → recalcular el CPL máximo. **No bloquea el relanzamiento, pero sí la Fase 3** (no se escala sin saber si un CPL de $30–40 es rentable).
  - (Cliente) ¿Contestan en español? → **bloquea solo el ad group Grúa ES**. Si para el 10/06 no hay respuesta, el grupo se relanza en pausa.
  - (Cliente) ¿Alguien contesta entre 0 y 6 h? → define 24/7 o 6:00–23:00.
  - (Cliente) ¿GBP existe y está verificado? ¿PMM tiene acceso? → bloquea el activo de ubicación y la pista LSA.
  - (Cliente) Radio real, ¿medium-duty?, ¿carrocería?, ¿lockout? → solo afecta la Fase 3.
  - (Cliente) Proceso de respuesta: quién contesta, en cuánto tiempo, qué pasa con los formularios (hoy llegan a un Gmail).
- **Riesgos**:
  - Si "Website Calls" es un clic en `tel:`, las 9 conversiones de esa acción no son leads: el CPL real sería >$60 y Maximizar conversiones estaría aprendiendo de la señal equivocada. En ese caso el relanzamiento arranca con aprendizaje casi nuevo.
  - El cliente no tiene historial de responder rápido (no hay datos) → riesgo de que el CPL sea "bueno" y las ventas no.

## Fase 1 — Relanzamiento Search reestructurado
- **Fecha estimada**: **2026-10-06** (cambios aplicados) → **2026-10-13** (7 días de datos).
- **Condición de paso**: los cambios de `strategy.md` (pasos 2–7) aplicados, con 7 días corriendo, anuncios nuevos aprobados, **≥1 conversión verificada** en la estructura nueva y ninguna conversión primaria que sea un clic.
- **Qué se lanza** (sobre la campaña existente, sin crear otra):
  - Campaña renombrada a *Towing - Search - Radius*, $25/día, Maximizar conversiones, solo búsqueda, Presencia + 20 mi.
  - Ad groups: Towing Near Me (el actual "Ad group 1", renombrado), Cheap Towing, Roadside Assistance y Wesley Chapel Towing. Grúa ES queda activa solo si se cumple la regla.
  - Broad → frase + exacta. Pausar 5 keywords genéricas. 1 RSA nueva por grupo (variante A de `data/ads-search.md`; máx. 2 con la actual), según CLAUDE.md #4.
  - Extensiones: sitelinks, callouts, snippet, llamada. Ubicación solo si hay GBP.
- **Riesgos**:
  - Mover keywords entre grupos y cambiar match type hace que Maximizar conversiones vuelva a aprender: esperar 1–2 semanas de CPL inestable. No reaccionar antes del D14.
  - Con ~3 clics/día, una semana sin conversiones es varianza normal.

## Fase 2 — Limpieza (D7 · D14 · D30 desde el relanzamiento)
- **Fechas**: **D7 = 2026-10-13 · D14 = 2026-10-20 · D30 = 2026-11-05**
- **Condición de paso**:
  - las tres revisiones hechas (`/weekly-review`), negativas nuevas aplicadas y keywords sin impresiones en 30 días pausadas;
  - **CPL ≤ $40 durante 4 semanas seguidas**;
  - el cliente confirma que **≥50% de los leads son reales** (llamadas y formularios con intención de servicio).
- **Qué se revisa**:
  - search terms (sobre todo de los nuevos grupos frase/exacta);
  - gasto sin conversión mayor a $80 (2× el CPL objetivo);
  - el peor RSA por grupo en D30;
  - si la hora 5 sigue con clics sin conversión (posibles clics inválidos);
  - si el gasto baja a menos de $20/día por limitación de ranking.
- **Meta de salida hacia la Fase 3**: CPL ≤ $30 por 4 semanas (fecha optimista: **~2026-12-01**).

## Fase 3 — Optimización de puja (tCPA)
- **Fecha estimada**: **no alcanzable con el presupuesto actual.**
  - Cálculo: $25/día ÷ $38.50 de CPL = 0.65 conv./día → **máximo ~19–20 conv. en 30 días**, por debajo de 30.
  - Presupuesto < 3× CPL/día ($115): aprendizaje lento, y la Fase 3 se corre al menos 2 semanas.
  - **Escenario con upgrade**: si el **2026-12-01** el paquete sube a ~$35/día en medios y el CPL está en ~$30 → ~35 conv./30 d. Con la regla de 30 días con datos + 2 semanas de margen, **tCPA alrededor del 2027-01-15**.
- **Condición de paso**: ≥30 conversiones en una ventana de 30 días, con tracking verificado y calidad de lead confirmada.
- **Acción**: tCPA = CPA real observado (no el deseado), presupuesto ajustado a la capacidad del cliente.
- **Si no se cumple**: quedarse en Maximizar conversiones (o en Maximizar clics con tope de $10 si la medición limpia deja <15 conv./mes). **No forzar tCPA con 20 conv./mes.** Si la conversión de la landing está por debajo del 5% (hoy está en ~21%, así que no es el problema), revisar landing; si no, el limitante es el presupuesto → propuesta comercial de upgrade con datos de la Fase 2.

## Fase 4 — Remarketing
- **Fecha estimada**: **no realista a corto plazo.** El tráfico pagado es de ~90 clics/mes y el orgánico del dominio es nuevo (08/2026), así que la audiencia de visitantes no llega a 1,000 en 30 días. Además, en towing el remarketing aporta poco: la necesidad es inmediata y no se reconsidera.
- **Condición de paso**: audiencia ≥1,000 usuarios en 30 días.
- **Acción**: importar la audiencia de GA4 "todos los visitantes" desde ya (no cuesta nada) y agregarla en **observación** a Search cuando alcance el tamaño mínimo. Display remarketing: no.

## Fase 5 — Performance Max
- **Fecha estimada**: **no califica.** Fallan 5 de las 6 condiciones de `knowledge/estrategias/pmax-cuando-y-como.md`:
  1. ❌ Search ≥4 semanas estable **con tCPA** → no hay tCPA (Fase 3 bloqueada).
  2. ❌ ≥30 conv./mes con tracking verificado → ~18–20/mes, sin verificar.
  3. ⏳ Ciclo de limpieza D30 → el 11/05 como pronto.
  4. ❌ Assets propios (5+ fotos reales, video) → no hay fotos del negocio en el sitio.
  5. ⚠️ Landing con conversión ≥5% y anti-spam → la conversión cumple (~21%); no hay honeypot ni reCAPTCHA.
  6. ❌ Presupuesto ≥3× CPA/día ($115) → hay $25.
- **Qué haría falta**: el upgrade de la Fase 3 **y** 4 semanas con tCPA estable **y** fotos y video reales **y** un presupuesto adicional de ~$100/día. Para un paquete de $1,500 eso **no es realista**: quedarse en Search (+ LSA si califica).

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance (sin CRM; los formularios llegan a un Gmail). Se reevalúa si el cliente empieza a registrar leads con GCLID. El paso intermedio es que el cliente marque en una hoja compartida qué llamadas o formularios terminaron en servicio (alimenta la condición de la Fase 2).

## Pista paralela — Landing
| Ajuste | Tipo | Fecha | Responsable |
|---|---|---|---|
| `/thank-you/` + redirect del formulario + conversión | **Bloqueante F0** | 10/06 | PMM |
| Revisar los disparadores de conversión en GTM | **Bloqueante F0** | 10/06 | PMM |
| H1 "24/7 Towing in Wesley Chapel, FL" | Mejora (impacto alto en Quality Score) | 10/06 | PMM |
| Formulario de 6 → 3 campos | Mejora | 10/10 | PMM |
| `tel:+18133810435` normalizado + botón de llamada fijo en móvil | Mejora | 10/06 | PMM |
| PageSpeed móvil (correr con API key) y optimizar si el score es menor a 70 | Mejora | 10/10 | PMM |
| Reseñas de GBP o testimonios reales visibles | Mejora (bloqueada por GBP) | 10/31 | Cliente → PMM |
| "Licensed & Insured", años de experiencia, fotos reales | Mejora | 10/31 | Cliente → PMM |
| `/roadside-assistance/` | Mejora (Fase 2) | 10/20 | PMM |
| `/es/` o bloque en español | Condicional (Grúa ES) | 10/10 si confirman español | PMM |
| Honeypot / reCAPTCHA v3 en el formulario | Mejora | 10/20 | PMM |
| `/medium-duty-towing/`, `/collision-repair/` | Fase 3, condicional | — | PMM |

## Pista paralela — LSA
- **10/03**: verificar en ads.google.com/local-services-ads si la categoría Towing está habilitada para 33543. **PENDIENTE de verificar; no se asume.**
- **Requisito previo: GBP verificado** (hoy no encontrado) + licencia/registro de wrecker en FL + seguro + background check.
- Si califica y hay GBP: solicitud el 10/06 → verificación del **10/20 al 11/03** (2–4 semanas) → presupuesto semanal propio, aparte del paquete Search (conversación comercial).
- Ranking LSA = reseñas (cantidad, promedio, velocidad) × tasa de respuesta × fotos: el cliente necesita un plan de reseñas desde el día 1.

## Estacionalidad y ventanas
- **Temporada de huracanes (hasta el 30/11)**: picos de demanda (accidentes, vehículos inundados, recuperaciones) después de tormentas. Con $25/día el presupuesto se agota temprano esos días: tener lista una subida temporal de presupuesto con OK del cliente.
- **Snowbirds (nov–abr)**: Zephyrhills y Dade City tienen mucha población estacional y parques de RV → más demanda de nov a abr. **Revisar en noviembre** las negativas "rv towing" / "motor home" si el cliente puede remolcar RV clase C (hoy excluidas).
- **Fiestas (Thanksgiving, Navidad)**: más tráfico en la I-75 → más llamadas de roadside y towing.

## Historial de cambios
- 2026-10-01: plan HTML ES + EN publicado con /informe (URLs en el front matter).
- 2026-10-01: RSA a 1 por grupo (máx. 2) y puja condicionada a la medición, por las reglas nuevas de CLAUDE.md (#4, #6).
- 2026-10-01: creado (D0 = 2026-10-01). Cuenta activa desde el 22/08; la Fase 0 corre con la campaña en vivo.
