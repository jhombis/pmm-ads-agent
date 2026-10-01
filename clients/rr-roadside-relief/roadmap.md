---
cliente: RR Roadside Relief
slug: rr-roadside-relief
D0: 2026-10-01
actualizado: 2026-10-01
fase_actual: 0
---

# Roadmap — RR Roadside Relief

> Caso especial: la cuenta **ya está activa** desde el 15-sep (ENHPRM, en amplia, un solo ad group). La Fase 0 se hace **con la campaña corriendo**: primero se corta el desperdicio (negativas) y después se reestructura. No se pausa: 7 de 8 conversiones son llamadas y la llamada funciona.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Fundación / correcciones | 2026-10-01 → 2026-10-08 (→ 10-15 si el cliente edita la web) | 🔄 en curso |
| 1 — Relanzamiento Search (estructura nueva) | 2026-10-08 → 2026-10-15 | ⏳ |
| 2 — Limpieza D7 · D14 · D30 | 2026-10-15 · 2026-10-22 · 2026-11-07 | ⏳ |
| 3 — tCPA | ~2026-11-16 (rango 11-05 → 11-23) | ⏳ |
| 4 — Remarketing (RLSA) | no antes de 2027-Q1; con el tráfico actual no llega a 1,000 usuarios/30 d | ⛔ probable bloqueo por volumen |
| 5 — Performance Max | no califica con el presupuesto actual; reevaluar en ene-2027 | ⛔ bloqueada (presupuesto + assets) |
| 6 — Conversiones offline | fuera de alcance (sin CRM) | — |
| Pista Landing | 2026-10-01 → 2026-10-08 (bloqueantes) · → 2026-10-31 (mejoras) | 🔄 |
| Pista LSA | 2026-10-01 → verificación 10-15/10-29 (requiere GBP primero) | ⏳ |

## Fase 0 — Fundación
- **Fecha estimada**: 2026-10-01 → 2026-10-08. Hay bloqueantes de landing: +3 días si edita PMM, +7–14 si edita el cliente (quién edita la web: PENDIENTE). Si edita el cliente, la fecha pasa a **2026-10-15**.
- **Condición de paso**: todos los ítems bloqueantes de Fase 0 del checklist en ✅.
- **Tareas**:
  - Día 1–2, sobre la campaña actual (cortar desperdicio ya):
    - (Jhombis) OK para aplicar `data/2026-10-01-negatives.txt` (238 términos) + `data/negatives-nicho.txt` §A–C.
    - (PMM) Quitar las negativas existentes que bloquean llantas, `mobile`, `quick` y `budget` (`data/negatives-nicho.txt` §F).
    - (PMM) Ajustar "Calls from Ads" a ≥60 s y verificar que sea la única conversión de llamada primaria.
    - (PMM) Tag Assistant: confirmar que `AW-18397439627` pertenece a la cuenta 425-405-2574 y que "Form Fill" no se cuenta doble (Site Kit + GTM).
  - Confirmaciones del cliente (vía Jhombis):
    - Presupuesto real de pauta.
    - Área de servicio (radio).
    - Si contestan 24/7 de verdad.
    - Quién responde los leads y en cuánto tiempo.
    - Tarifas u oferta sostenible.
    - Si atienden en español.
    - Licencia y seguro.
    - Ticket promedio.
  - Landing (ver pista Landing): formulario de 4 campos arriba en la home, /light-medium-duty-towing/ y /roadside-assistance/; H1 nuevos; logo e imágenes comprimidos + caché; medir PageSpeed móvil.
  - (Cliente) Crear/verificar Google Business Profile y dar acceso a PMM. No se encontró en búsqueda web y es requisito para el activo de ubicación, Maps y LSA.
- **Riesgos**:
  - El cliente tarda en confirmar el presupuesto o el área. Mitigación: se relanza con los supuestos de `strategy.md` y se ajusta después.
  - Nadie contesta de noche: se pierden leads pagados. Mitigación: programar el horario real.
  - Si la web la edita un tercero del cliente, la fase se extiende hasta 10-15.

## Fase 1 — Relanzamiento Search
- **Fecha estimada**: 2026-10-08 (lanzamiento de la estructura nueva) → 2026-10-15 (condición).
- **Condición de paso**: estructura nueva activa 7 días, anuncios aprobados y ≥1 conversión registrada **con llamada ≥60 s**.
- **Qué se lanza**: la estructura de `strategy.md` dentro de la campaña existente, vía `/build-campaign`.
  - 9 ad groups EN. AG10 en español solo si se confirma el idioma **y** existe su landing.
  - Keywords en frase/exacta.
  - 3 RSA por grupo (sin los headlines ⚠ no confirmados).
  - Extensiones.
  - "Ad group 1" (amplia) en pausa.
  - Presupuesto: **$43/día** (~$1,300/mes) ⚠ hasta confirmar la pauta real.
  - Maximizar conversiones; Presencia con radio de 25 mi.
- **Riesgos**:
  - El cambio de keywords reinicia parte del aprendizaje: 1–2 semanas de CPL alto.
  - Sin GBP no hay activo de ubicación.
  - Presupuesto < 3× CPL benchmark por día ($43 contra $45): aprendizaje lento.

## Fase 2 — Limpieza (D7 · D14 · D30)
- **Fechas** (desde el relanzamiento del 10-08): **2026-10-15 · 2026-10-22 · 2026-11-07**.
- **Condición de paso**: las tres revisiones hechas (`/weekly-review`), negativas aplicadas, keywords sin impresiones en 30 días pausadas y RSA peor de cada grupo reemplazado.
- **Qué se revisa**:
  - search terms → negativas (foco en planes de aseguradoras, tiendas de llantas y competidores);
  - gasto sin conversión por ad group (umbral: >2× CPL objetivo = $90);
  - tasa de conversión por grupo;
  - IS perdido por ranking (meta < 40% al D30);
  - calidad de llamadas reportada por el cliente;
  - llamadas nocturnas no contestadas.

## Fase 3 — Optimización de puja (tCPA)
- **Fecha estimada**: **~2026-11-16** (rango 11-05 → 11-23).
- **Supuesto del cálculo**: $43/día ÷ CPL de cuenta nueva ≈ $35 (benchmark de cuentas nuevas, mejorado por la limpieza) ≈ 1.2 conv/día → 30 conversiones en ~25 días desde el 10-08 (≈ 11-02). Se suman **+2 semanas** porque el presupuesto queda por debajo de 3× el CPL del benchmark → ~11-16. Si el CPL baja a ~$20, la fecha se adelanta a ~11-05 (mínimo 21 días).
- **Condición de paso**: ≥30 conversiones en 30 días con tracking verificado (llamada ≥60 s, formulario sin doble conteo) **y** el cliente confirma que ≥70% son leads reales.
- **Acción**: tCPA = CPA real de 30 días (no el deseado). Reajustar el presupuesto según CPA y capacidad (3 flatbeds).
- **Si no se cumple en fecha**:
  - conversión por clic < 5% → revisar la landing (formulario, velocidad);
  - IS perdido por ranking > 50% → revisar QS y copy;
  - pocas búsquedas → ampliar keywords o radio.
  - **No** forzar tCPA con menos datos.

## Fase 4 — Remarketing
- **Fecha estimada**: no antes de 2027-Q1.
- **Condición de paso**: audiencia ≥1,000 usuarios en 30 días.
- **Realidad**: con ~$1,300/mes y CPC ~$5 son ~250–300 clics/mes. Más el orgánico (sitio nuevo, sin ranking), la lista no llega a 1,000. Solo es viable si sube el presupuesto o crece el tráfico orgánico/GBP.
- **Acción cuando califique**: RLSA en observación → ajuste de puja. Display remarketing opcional con exclusión de apps.

## Fase 5 — Performance Max
- **Fecha estimada**: no califica con las condiciones actuales; reevaluar en **enero 2027**.
- **Condiciones de `pmax-cuando-y-como.md` que fallan hoy**:
  1. **Presupuesto**: PMax necesita ≥3× CPA por día. Con un CPA de ~$25 son ~$75/día solo para PMax; hoy la cuenta entera tiene $43/día.
  2. **Search estable con tCPA**: llega como pronto a mediados de nov, más 4 semanas estable → mediados de dic.
  3. **Assets propios**: no hay 5+ fotos reales validadas, ni video, ni reseñas.
  4. **Landing**: sin anti-spam en el formulario y conversión por clic actual de 8.5% (hay que confirmar ≥5% tras los cambios).
- **Qué hacer para cumplirlas**:
  - subir la pauta a ≥$120/día en total;
  - sesión de fotos y video corto de los 3 flatbeds;
  - honeypot/reCAPTCHA v3 en Elementor;
  - sostener el tCPA 4 semanas.
- **Mientras tanto**: Search + LSA.

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance (sin CRM; leads por email a rraysautorecovery@gmail.com). Se reevalúa cuando el cliente registre los leads con GCLID (campos ocultos en el formulario, incluidos en el checklist como preparación).

## Pista paralela — Landing
| Ajuste (de `audit-site.md`) | Tipo | Responsable | Fecha |
|---|---|---|---|
| Formulario de 4 campos arriba en home, /light-medium-duty-towing/ y /roadside-assistance/ | **Bloqueante F0** | PMM (o quien edite la web ⚠) | 10-08 |
| PageSpeed móvil medido; logo 676 KB → <30 KB; headers → <100 KB; caché de página | **Bloqueante F0** (duro si score < 40) | PMM | 10-08 |
| H1 en home ("24/7 Towing & Roadside Assistance in Oklahoma City") y H1 de servicio con OKC | Mejora (necesaria para QS) | PMM | 10-08 |
| Botón de llamar fijo en móvil | Mejora | PMM | 10-08 |
| /thank-you/ con URL propia | Mejora | PMM | 10-15 |
| Páginas nuevas: /flat-tire-change/, /car-lockout/, /jump-start/, /flatbed-motorcycle-towing/ | Mejora F2 | PMM | 10-31 |
| /es/servicio-de-grua/ | Condicional (AG10) | PMM + cliente | 10-31 si se confirma el español |
| Reseñas GBP embebidas + fotos reales de las grúas | Mejora F2–3 | Cliente + PMM | 10-31 |
| "Licensed & Insured" con datos | Mejora | Cliente | 10-15 |
| Anti-spam en el formulario (honeypot/reCAPTCHA v3) | Requisito F5 | PMM | 11-30 |

## Pista paralela — LSA
- **Aplica**: US + towing es categoría elegible en OKC (`competitors.md`).
- **Prerrequisito**: GBP verificado (hoy no encontrado).
- **D0 → 10-08**: el cliente crea/verifica el GBP y PMM inicia la solicitud LSA (licencia, seguro, background check del dueño y los conductores).
- **10-15 → 10-29**: verificación (2–4 semanas desde la solicitud; si el GBP tarda, se corre).
- **Luego**: presupuesto semanal LSA separado de Search, respuesta a leads <1 h (afecta ranking LSA) y campaña de reseñas (meta: 20–30 en 60 días).

## Estacionalidad y ventanas
- Towing en OKC tiene **pico en invierno** (dic–feb: tormentas de hielo, baterías muertas, llantas) y picos puntuales con clima severo en primavera.
- Relanzar en octubre es buen momento: la meta es tener **tCPA estable antes de diciembre** para escalar presupuesto en las heladas.
- En eventos de hielo, subir el presupuesto diario 50–100% (si hay capacidad de grúas) y tener listo un RSA de "Ice Storm Towing / Stuck in Ditch".

## Historial de cambios
- 2026-10-01: creado (D0 = 2026-10-01; cuenta activa desde el 2026-09-15).
