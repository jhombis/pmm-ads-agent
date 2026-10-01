---
cliente: AAMCO Transmissions & Total Car Care — 103rd St (Jacksonville)
slug: aamco-jacksonville-103rd
fase_actual: 0
actualizado: 2026-09-23
---
# Checklist — AAMCO 103rd St

Generado por /roadmap a partir de `knowledge/checklists/setup-cuenta.md`, adaptado a una cuenta existente en reestructura. /weekly-review lo actualiza. ✅ = verificado con datos; (N/V) = no verificado todavía.

## Diagnóstico (hecho)
- [x] (PMM) /onboard + evaluación de la campaña actual (2026-09-23)
- [x] (PMM) /audit-landing parcial (2026-09-23)
- [x] (PMM) /competitors (2026-09-23)
- [x] (PMM) /benchmark-interno (2026-09-23)
- [x] (PMM) /strategy v1 (2026-09-23)
- [x] (PMM) /roadmap (2026-09-23)

## Fase 0 — Fundación (bloqueante para la estructura nueva)
### Cuenta (ya existe)
- [x] (PMM) Cuenta en el MCC de PMM (AAMCO Ad Pool 468-970-4116)
- [x] (PMM) Facturación activa (la cuenta gasta)
- [x] (Cliente) GBP verificado, categoría "Transmission shop" (507 reseñas, 4.4★)
- [ ] (PMM) GBP vinculado a Google Ads como activo de ubicación, filtrado a la sede 103rd (N/V)
- [x] (PMM) Google Tag instalado (GA4 recibe hits; la conversión de form registra)
- [x] (PMM) Auto-tagging activo
- [ ] (PMM) Aplicación automática de recomendaciones DESACTIVADA (N/V)
### Medición — **bloqueante**
- [ ] (PMM) Acceso a CallRail
- [ ] (PMM) Medir en CallRail (60 días): % de primera vez, % ≥ 60 s, % de clientes actuales
- [ ] (PMM) Identificar la conversión "Phone Call" (DEFAULT)
- [ ] (PMM, requiere aprobación) Única primaria de llamada: CallRail primera llamada ≥ 60 s; "Calls from ads" y "Phone Call" a secundarias
- [ ] (PMM) Línea base limpia de 2 semanas en la campaña actual (09-28 → 10-11)
- [ ] (PMM) Conversión "Formulario" por URL `/thank-you/`, probada con Tag Assistant
- [ ] (PMM) Form del subdominio 103rd probado en móvil (hoy 0 envíos)
- [ ] (PMM) Eventos clave en GA4: form_submit / thank-you, click_tel
- [ ] (PMM) Número CallRail visible como `tel:` en el header móvil
- [x] (PMM) Conversiones secundarias (direcciones, store visits, local actions) como secundarias
- [ ] (PMM) Campos ocultos UTM + GCLID en el form (N/V)
### Negocio — **bloqueante**
- [ ] (Cliente) Ticket y margen por tipo de trabajo, tasa de cierre, capacidad → CPL máximo
- [ ] (Cliente) Proceso de respuesta: quién contesta, en cuánto tiempo, qué pasa fuera de horario
- [ ] (Cliente) Confirmar garantía por tipo de trabajo, financiamiento en la sede, "Free Transmission Check", remolque gratis
- [ ] (Cliente) Decisión sobre el oil change (producto de entrada o se excluye)
### Negativas y build
- [ ] (PMM) Lista universal PMM (ajustada: sin "free" ni "reviews") como lista compartida — `data/negatives-nicho.txt`
- [ ] (PMM) Lista de nicho + competidores + cruzadas por sede
- [ ] (PMM) Revisar la concordancia de las negativas existentes ("take 5", "aamco dunn ave") y quitar o ajustar "aaa" y "duval"
- [ ] (PMM) Keyword Planner (radio 5 mi) para confirmar los volúmenes de A y E
- [ ] (PMM) Confirmar exclusión de marca en PMax 103rd
- [ ] (PMM) /build-campaign: MARCA y NO-MARCA creadas **en pausa**
- [ ] (PMM) PageSpeed móvil de las landings (N/V; bloqueante solo si score < 40)

## Fase 1 — Salida de la estructura nueva (objetivo: lunes 2026-10-12)
- [ ] Campañas: MARCA 103rd ($8/d) y NO-MARCA 103rd ($60/d) según `strategy.md`
- [ ] Red: solo Búsqueda; socios y Display apagados
- [ ] Ubicación: radio 5 mi en 7532 103rd St, solo Presencia
- [ ] Programación: L–V 8:00–18:00 ET (5–15 PT)
- [ ] Puja: MARCA con cuota de impresiones 90% arriba y CPC máx. $4; NO-MARCA con Max Conversions sin tCPA
- [ ] Keywords en frase + exacta en los top términos; **sin amplia**
- [ ] 3 RSA por ad group, H1 pinneado, 15 titulares / 4 descripciones, fuerza "Buena" o superior (`data/ads-search-103rd.md`)
- [ ] Anuncio de solo llamada en MARCA y en A
- [ ] Extensiones: sitelinks (6), callouts (8), snippets, llamada (CallRail), ubicación (solo 103rd), imágenes reales
- [ ] URLs finales verificadas (200, https, sin redirect)
- [ ] Campaña "ZETA Radius" 103rd y PMax 103rd pausadas **el mismo día**
- [ ] Anuncios aprobados (revisar 24 h después)
- [ ] Primera conversión CallRail ≥ 60 s registrada en no-marca
- [ ] Aviso al cliente: el CPA reportado sube por el cambio de medición, no por la estructura

## Fase 2 — Limpieza (D7 2026-10-19 · D14 10-26 · D30 11-11)
- [ ] D7: search terms → negativas
- [ ] D7: keywords sin impresiones identificadas (no pausar aún)
- [ ] D7: reparto de gasto E frente a transmisión revisado
- [ ] D14: search terms → negativas
- [ ] D14: keywords con gasto > $60 y 0 conversiones marcadas para revisión
- [ ] D14: alarma de volumen (clics no-marca −40% frente a la línea base) evaluada
- [ ] D14: prueba de incrementalidad de [aamco] iniciada
- [ ] D30: search terms → negativas
- [ ] D30: keywords con 0 impresiones en 30 días pausadas
- [ ] D30: peor RSA de cada grupo reemplazado
- [ ] D30: anuncio de solo llamada frente a RSA: decisión
- [ ] D30: reporte de calidad de leads del cliente (CallRail etiquetado)

## Fase 3 — Optimización de puja (~2026-11-30)
- [ ] ≥30 conversiones limpias en no-marca en 30 días confirmadas
- [ ] tCPA = CPA real observado
- [ ] Presupuesto reajustado según CPA frente a CPL máximo y capacidad (+20% por paso)
- [ ] Evaluar separar Transmisión en campaña propia (≥ 3× CPL/día)
- [ ] Ajustes por horario y dispositivo evaluados con datos
- [ ] Resultado de la prueba de incrementalidad de marca aplicado

## Fase 4 — Remarketing (~2026-12-14, condicionada)
- [ ] Audiencia de visitantes ≥1,000 en 30 días (evaluar la audiencia del sitio compartido de Jax)
- [ ] RLSA en observación en no-marca

## Fase 5 — Performance Max ⛔ (no califica con el presupuesto actual; reevaluar 2027-02)
- [ ] Presupuesto de la sede ≥ $150/día total (condición que hoy falla)
- [ ] Resto de condiciones de `pmax-cuando-y-como.md`

## Fase 6 — Conversiones offline (futuro)
- [ ] (Cliente) Etiquetar en CallRail las llamadas que terminan en cita o trabajo

## Pista Landing
- [ ] `/thank-you/` (F0, 2026-10-09)
- [ ] Quitar `/test/`, `/test-2/`; redirigir URLs legacy (F2, 2026-10-26)
- [ ] (Cliente) Dominio canónico único para la sede (F2, 2026-11-11)
- [ ] (Cliente) Versión 103rd de la página de transmisiones (F2, 2026-11-11)
- [ ] (Cliente) Versiones 103rd de auto-service y check engine (F3, 2026-12-01)
- [ ] (Cliente) Página rebuild + financiamiento (F3, 2026-12-01; lista antes de la ventana de impuestos 2027-02)
- [ ] Anti-spam en el form (F3)

## Pista LSA
- [ ] (PMM) Elegibilidad de auto repair en Jacksonville + permiso de la franquicia (2026-10-07)
- [ ] (Cliente) Solicitud y verificación (~2026-11-04 → 11-18), si aplica

## Cuenta (fuera del alcance de la sede, pero afecta)
- [ ] (Cuenta) Acordar entre sedes quién puja por [aamco] genérico
- [ ] (Cliente) Plan de reseñas (4.4★ frente a 4.9★ de los independientes)
- [ ] (PMM) Métricas de Auction Insights desde la interfaz
- [ ] (PMM) Etiquetar las cuentas del MCC con nicho:* / pais:*
- [ ] (PMM) Causa del bajo gasto en feb–mar 2026; asegurar presupuesto del ad pool para feb-2027

## Recurrente (semanal, /weekly-review)
- [ ] Search terms → negativas
- [ ] Gasto frente a presupuesto mensual
- [ ] CPA frente a objetivo; tendencia 7d frente a 28d
- [ ] Anuncios rechazados o limitados
- [ ] Cuota de impresiones perdida por presupuesto y por ranking
- [ ] Calidad de leads (CallRail)
- [ ] Log en `log/YYYY-MM-DD.md`
