---
cliente: AAMCO Transmissions & Total Car Care — 103rd St (Jacksonville)
slug: aamco-jacksonville-103rd
D0: 2026-09-23
actualizado: 2026-09-23
fase_actual: 0
modo: cuenta existente, reestructura. Nada se ejecuta en Ads sin aprobación de Jhombis
---

# Roadmap — AAMCO 103rd St

> Cuenta activa (no es un lanzamiento desde cero). "Fase 1" = salida de la estructura nueva de `strategy.md`, que reemplaza a la campaña "ZETA Radius" y al PMax 103rd. Mientras tanto, la estructura actual sigue corriendo sin cambios de presupuesto.
> D0 = fecha de hoy (no se indicó otra). Si Jhombis fija otra D0, se corren todas las fechas.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Fundación (medición, landing, decisiones del cliente) | 2026-09-23 → 2026-10-09 | 🔄 en curso (diagnóstico hecho) |
| 1 — Salida de la estructura nueva | 2026-10-12 → 2026-10-19 | ⏳ pendiente |
| 2 — Limpieza D7 · D14 · D30 | 2026-10-19 · 2026-10-26 · 2026-11-11 | ⏳ pendiente |
| 3 — tCPA en no-marca | ~2026-11-30 (supuesto abajo) | ⏳ pendiente |
| 4 — Remarketing (RLSA) | ~2026-12-14, si la audiencia llega a 1,000 | ⏳ pendiente, dudosa |
| 5 — Performance Max | **No califica con el presupuesto actual**; reevaluar 2027-02 | ⛔ bloqueada (presupuesto) |
| 6 — Conversiones offline | Fuera de alcance | ⏳ futuro |
| Pista Landing | F0 (bloqueantes) → F3 (mejoras) | 🔄 |
| Pista LSA | Elegibilidad al 2026-10-07; verificación ~2026-11-04 → 11-18 | ⏳ |

## Fase 0 — Fundación
- **Fecha estimada**: 2026-09-23 → 2026-10-09 (D0+16). Base de 3 días + bloqueantes de landing que **edita el cliente o la franquicia** (+7–14 días, según `audit-site.md`). Puede llegar al 2026-10-16 si el sitio lo edita la franquicia.
- **Condición de paso**: todos los ítems bloqueantes de Fase 0 en `checklist.md` ✅. En concreto: 1 conversión primaria de llamada probada, form con `/thank-you/` registrando, CPL máximo definido y ofertas confirmadas.
- **Tareas**:
  - **Semana 1 (09-23 → 09-30)**
    - (PMM) Acceso a CallRail. Medir en los últimos 60 días: % de primera vez, % ≥ 60 s y % de clientes actuales. Da el **factor de inflación** y el CPL real.
    - (PMM) Identificar qué es "Phone Call" (DEFAULT) y de dónde viene.
    - (PMM, **requiere aprobación**) Dejar como única primaria de llamada **CallRail con primera llamada ≥ 60 s**. "Calls from ads" y "Phone Call" pasan a secundarias. Se aplica **en la campaña actual ya en semana 1**, para tener **2 semanas de línea base limpia** (09-28 → 10-11) antes de la estructura nueva y poder comparar lo viejo con lo nuevo con la misma vara.
    - (Cliente) Ticket y margen por tipo de trabajo, tasa de cierre, capacidad semanal → CPL máximo.
    - (Cliente) Quién contesta el teléfono y en cuánto tiempo; qué pasa con las llamadas fuera de horario.
    - (Cliente) Confirmar garantía por tipo de trabajo, financiamiento en esta sede, "Free Transmission Check" vigente y remolque gratis (sí/no).
    - (Cliente) Decisión sobre el oil change: producto de entrada o se excluye.
  - **Semana 2 (10-01 → 10-09)**
    - (PMM + quien edite el sitio) Crear `/thank-you/`, redirigir el form y crear la conversión por URL. Probar con Tag Assistant.
    - (PMM) Enviar un lead de prueba desde el form del subdominio 103rd en móvil (0 envíos en 90 días).
    - (PMM) Eventos clave en GA4: form_submit / page_view de `/thank-you/`, click_tel.
    - (PMM) Keyword Planner (radio 5 mi) para confirmar los volúmenes de los ad groups A y E.
    - (PMM) Revisar la concordancia de negativas existentes ("take 5", "aamco dunn ave") y las negativas "aaa" y "duval".
    - (PMM) Confirmar exclusión de marca en PMax 103rd (se pausa en F1 igual).
    - (PMM) `/build-campaign`: crear MARCA 103rd y NO-MARCA 103rd **en pausa**, con anuncios, extensiones y negativas. Revisión de políticas antes de activar.
- **Riesgos**:
  - La franquicia no permite editar el sitio → sin `/thank-you/` hay que medir el form por evento (menos confiable). Si pasa el 2026-10-09 sin avance, se lanza F1 midiendo **solo llamadas CallRail** y el form queda como mejora de F2. No se bloquea todo por el form: aporta ~2% de las conversiones.
  - Sin acceso a CallRail no se puede filtrar por primera llamada / duración → **bloqueo total**: no se lanza la estructura nueva sobre la señal inflada.
  - Cambiar la conversión primaria en la campaña actual la mete en re-aprendizaje ~1 semana. El CPA reportado va a subir: es esperado, hay que avisar al cliente antes.

## Fase 1 — Salida de la estructura nueva
- **Fecha estimada**: lunes 2026-10-12 → 2026-10-19. Se lanza en lunes porque el taller solo atiende L–V.
- **Condición de paso**: las 2 campañas activas 7 días, anuncios aprobados, ≥1 conversión CallRail (≥ 60 s) registrada en no-marca y la campaña vieja + PMax pausados sin solaparse.
- **Qué se lanza** (de `strategy.md`, fase 1):
  - MARCA 103rd: $8/día, cuota de impresiones 90% arriba, CPC máx. $4.
  - NO-MARCA 103rd: $60/día, Max Conversions sin tCPA, ad groups A, B, C, E y F.
  - Pausar: "AAMCO Transmissions (103 RD JACKSONVILLE FL) - ZETA Radius…" y "103 RD Jacksonville - PMAX - 01/02/25" **el mismo día** que se activan las nuevas.
  - Total: ~$68/día, igual que hoy.
- **Riesgos**:
  - **Presupuesto < 3× CPL/día** en no-marca ($60 frente a ~$96 con CPL de $32, y ~$165 con CPL calificado de ~$55): el aprendizaje será lento, de ahí la holgura en F3.
  - Caída de clics al pasar de amplia a frase: esperada. El umbral de alarma es −40% de clics no-marca a los 14 días (ver `strategy.md`, riesgo 1).
  - Proceso de respuesta del cliente sin confirmar: si no contestan en horario, las llamadas perdidas no convierten y el CPL sube por causas ajenas a Ads.

## Fase 2 — Limpieza (D7 · D14 · D30)
- **Fechas**: D7 = 2026-10-19 · D14 = 2026-10-26 · D30 = 2026-11-11.
- **Condición de paso**: las tres revisiones hechas (log en `log/`), negativas aplicadas, keywords con 0 impresiones en 30 días pausadas y el peor RSA de cada grupo reemplazado.
- **Qué se revisa**:
  - Search terms → negativas (meta: <5% del gasto irrelevante).
  - Reparto dentro de no-marca: si E pasa del 45% del gasto con peor CPL que transmisión, se ajusta (`strategy.md`).
  - Anuncio de solo llamada frente a RSA con activo de llamada: seguir o no.
  - Llamadas CallRail: % de primera vez y % ≥ 60 s. **Reporte de calidad del cliente al D30.**
  - D14: arrancar la prueba de incrementalidad de [aamco] (bajar puja 2–4 semanas y medir las llamadas totales de CallRail, incluidas las de GBP).

## Fase 3 — Optimización de puja (tCPA)
- **Fecha estimada**: **2026-11-30** (lunes después de Thanksgiving).
- **Cálculo**:
  - Supuesto: CPL calificado ~$55 (CallRail primera llamada ≥ 60 s; benchmark CallRail $32 × ~1.7 de filtro).
  - Conversiones/día = $60 ÷ $55 ≈ 1.1 → 30 conversiones en ~27 días desde el 10-12 = ~11-08.
  - +2 semanas porque el presupuesto es < 3× CPL → ~11-22.
  - Se evita cambiar la puja en la semana de Thanksgiving (11-26) → **11-30**.
  - Si el CPL real sale ~$35, la fecha se adelanta a ~11-16.
- **Condición de paso**: ≥30 conversiones limpias en no-marca en una ventana de 30 días, tracking verificado y sin cambios de estructura en los últimos 14 días.
- **Acción**:
  - tCPA = CPA real observado (no el deseado).
  - Marca sigue con cuota de impresiones.
  - Si el CPL no-marca ≤ CPL máximo, primer paso de escala: +20% de presupuesto, 2 semanas entre pasos.
  - Separar Transmisión en campaña propia cuando pueda tener ≥ 3× CPL/día.
  - Ajustes por horario y dispositivo con datos.
- **Si no se cumple en fecha**: revisar en este orden:
  1. Landing (conv. < 5% de clics en no-marca → pista Landing).
  2. Volumen (si la frase dejó < 200 clics/mes → reabrir "mechanic near me" / "auto shop near me" en frase).
  3. Presupuesto.
  **No forzar tCPA con menos datos.**

## Fase 4 — Remarketing
- **Fecha estimada**: ~2026-12-14 (D30 de F1 + 4 semanas de F3), **condicionada**.
- **Condición de paso**: audiencia de visitantes ≥1,000 usuarios en 30 días, apta para Search. GA4 103rd registra ~650 sesiones/mes reales (sin el tráfico bot directo). Probablemente **no llega** solo con la sede. Opción: audiencia del sitio compartido `aamco-jacksonvillefl.com` (todas las sedes de Jax), limitada por geo de la campaña.
- **Acción**: RLSA en observación en no-marca → ajuste de puja (+20–30%) si convierte mejor. Display remarketing: no (ver `strategy.md`).

## Fase 5 — Performance Max
- **Estado**: ⛔ **no califica** con el presupuesto actual. Reevaluar en 2027-02.
- **Condiciones** (`knowledge/estrategias/pmax-cuando-y-como.md`):
  | Condición | Estado previsto | Qué falta |
  |---|---|---|
  | Search ≥4 semanas estable con tCPA en objetivo | Posible desde ~2026-12-28 | Llegar a F3 |
  | ≥30 conv./mes con tracking verificado | Ajustado (~30–33/mes estimado) | Medición limpia en F0 |
  | Ciclo de limpieza D30 completado | 2026-11-11 | — |
  | Assets propios (5+ fotos reales, logo, video) | N/V | Fotos del taller 103rd |
  | Landing ≥5% de conversión + anti-spam en el form | N/V | Pista Landing |
  | **Presupuesto ≥3× CPA/día** (~$165/día con CPA $55) | ❌ PMax tendría ~$15–20/día (20–30% de Search) | **Esta es la que falla** |
- **Si no califica**: quedarse en Search + RLSA. Con el presupuesto de franquicia actual, PMax 103rd no es realista. Solo se reabre si el ad pool asigna a la sede ≥ $150/día en total, y aun así con exclusión de marca y solo las conversiones primarias limpias.

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance (sin CRM integrado).
- **Nota**: la franquicia usa un sistema de órdenes de reparación, y CallRail puede etiquetar llamadas como "cita agendada". Si el cliente acepta marcar resultados en CallRail, sería el primer paso barato hacia optimizar por trabajos, sin CRM. Se reevalúa después de F3.

## Pista paralela — Landing
| Ajuste (de `audit-site.md`) | Fase | Fecha | Responsable | Bloqueante |
|---|---|---|---|---|
| `/thank-you/` + redirect del form + conversión por URL | F0 | 2026-10-09 | PMM + quien edite el sitio | **Sí** (degradable: ver riesgos de F0) |
| Form del subdominio 103rd enviando (0 envíos en 90 días) | F0 | 2026-10-02 | PMM | **Sí** |
| Eventos clave GA4 (form, click_tel) | F0 | 2026-10-02 | PMM | Sí |
| Número CallRail visible como `tel:` en el header móvil | F0 | 2026-10-02 | PMM | Sí |
| PageSpeed móvil (N/V) | F0 | 2026-10-02 | PMM (API key o manual) | Solo si score < 40 |
| Quitar `/test/` y `/test-2/`; redirigir URLs legacy `/Sites/US/...` | F2 | 2026-10-26 | Quien edite el sitio | No |
| Dominio canónico único (anuncio, subdominio, GBP) | F2 | 2026-11-11 | Cliente/franquicia | No |
| Versión 103rd de `/service/automatic-transmissions/` (H1 por servicio, CallRail, form arriba, reseñas) | F2 | 2026-11-11 | Cliente/franquicia | No |
| Versión 103rd de `/auto-service/` y `/service/check-engine-light-service/` | F3 | 2026-12-01 | Cliente/franquicia | No |
| Nueva página rebuild + financiamiento 103rd | F3 | 2026-12-01 | Cliente/franquicia | No |
| Anti-spam en el form (reCAPTCHA v3 / honeypot) | F3 | 2026-12-01 | Quien edite el sitio | No (sí para F5) |

## Pista paralela — LSA
- **2026-09-23 → 10-07**: verificar si "auto repair" / transmisiones está habilitado en LSA para Jacksonville, FL y si la franquicia AAMCO lo permite (algunas franquicias lo manejan de forma centralizada).
- Si aplica: solicitud ~10-07 → verificación (licencia, seguro, background check) ~11-04 → 11-18 → presupuesto semanal chico (~$100–150) → gestión de reseñas (LSA pondera reseñas: 4.4★ es una desventaja frente a los independientes de 4.9★).
- Si no aplica: se cierra la pista y se documenta.

## Estacionalidad y ventanas
- **Nov–Dic**: menor demanda de reparaciones grandes (gasto navideño) y Thanksgiving (11-26). No cambiar la puja esa semana. Es buena ventana para limpiar y medir.
- **Feb–Abr 2027 (devoluciones de impuestos)**: pico de reparaciones grandes (rebuild/reemplazo). **Ventana para escalar transmisión** si F3 está estable: tener el ad group B y la landing de rebuild listos antes del 2027-02-01.
- **Abr–Sep (calor)**: A/C y sobrecalentamiento; en Florida también fallas de transmisión por temperatura. Ad group G (A/C) en F3 para abril 2027.
- ⚠️ **Feb–Mar 2026 la campaña casi no gastó** (causa PENDIENTE). Confirmar facturación y presupuesto del ad pool antes de feb-2027 para no perder la ventana de impuestos.

## Historial de cambios
- 2026-09-23: creado (D0 = 2026-09-23), a partir de brief, evaluación, audit-site, competitors, benchmark y strategy v1.
