# Checklist base: setup de cuenta nueva

Copiado a `clients/<slug>/checklist.md` por /roadmap. Cada ítem tiene responsable (PMM | Cliente) y fase. /weekly-review lo actualiza.

## Fase 0 — Fundación (bloqueante para lanzar)
- [ ] (PMM) Cuenta vinculada al MCC de PMM, acceso admin
- [ ] (PMM) Facturación configurada y verificada
- [ ] (Cliente) Google Business Profile verificado y con categoría principal correcta
- [ ] (PMM) GBP vinculado a Google Ads (activo de ubicación)
- [ ] (PMM) Google Tag instalado en todas las páginas de la landing/sitio
- [ ] (PMM) Conversión "Formulario" creada y probada con Tag Assistant
- [ ] (PMM) Conversión "Llamada desde anuncio" creada (duración mínima 60s)
- [ ] (PMM) Conversión "Clic en teléfono" en landing (móvil) creada
- [ ] (PMM) Conversiones secundarias (vistas, scroll) marcadas como secundarias, NO primarias
- [ ] (PMM) GA4 vinculado y audiencia "Todos los visitantes" importada
- [ ] (PMM) Campos ocultos UTM + GCLID en el formulario
- [ ] (PMM) Lista de negativas universal PMM aplicada a nivel de cuenta
- [ ] (PMM) Lista de negativas del nicho aplicada
- [ ] (PMM) Aplicación automática de recomendaciones DESACTIVADA
- [ ] (PMM) Landing aprobada por /audit-landing (o ajustes bloqueantes resueltos)
- [ ] (Cliente) Proceso de respuesta a leads definido: quién contesta, en cuánto tiempo, horario
- [ ] (Cliente) Número de teléfono de seguimiento / call tracking aprobado
- [ ] (PMM) Si US y categoría LSA: solicitud LSA iniciada (proceso paralelo)

## Fase 1 — Lanzamiento Search
- [ ] Campañas creadas por servicio según `strategy.md`
- [ ] Red: solo Búsqueda, socios y Display apagados
- [ ] Ubicación: Presencia solamente; países restantes excluidos
- [ ] Programación de anuncios según horario del cliente
- [ ] Puja: Max. clics con tope de CPC si es cuenta nueva o <15 conv/mes; Max. conversiones con 15+ estables (playbook §5)
- [ ] Keywords en frase; exacta para los top términos
- [ ] RSA por ad group según volumen (1–2 si pauta <$1,500/mes; 3 si mayor), H1 pinneado, 15H/4D, fuerza "Buena" o superior
- [ ] Extensiones: sitelinks (4+), callouts (6+), snippets, llamada, ubicación
- [ ] URLs finales verificadas (200, https, sin redirect)
- [ ] Presupuesto diario configurado según fase 1 de `strategy.md`
- [ ] Anuncios aprobados por políticas de Google (revisar 24h después)
- [ ] Primera conversión registrada (confirma tracking en producción)

## Fase 2 — Limpieza (días 7, 14, 30)
- [ ] Día 7: search terms revisados, negativas agregadas
- [ ] Día 7: keywords sin impresiones identificadas (no pausar aún)
- [ ] Día 14: search terms revisados, negativas agregadas
- [ ] Día 14: keywords con >$X gasto y 0 conversiones marcadas para revisión
- [ ] Día 30: search terms revisados, negativas agregadas
- [ ] Día 30: keywords con 0 impresiones en 30 días pausadas
- [ ] Día 30: RSA con peor rendimiento por grupo reemplazado
- [ ] Día 30: reporte de calidad de leads del cliente recibido

## Fase 3 — Optimización de puja
- [ ] ≥30 conversiones en 30 días confirmadas
- [ ] tCPA configurado = CPA real observado (no el deseado)
- [ ] Presupuesto reajustado según CPA y capacidad del cliente
- [ ] Ajustes de puja por horario/dispositivo evaluados con datos

## Fase 4 — Remarketing
- [ ] Audiencia de visitantes ≥1000 usuarios en 30 días
- [ ] RLSA: audiencia de visitantes agregada a Search en observación
- [ ] Campaña Display remarketing (opcional) con exclusión de apps

## Fase 5 — Performance Max (solo si califica; ver pmax-cuando-y-como.md)
- [ ] Condiciones de entrada verificadas
- [ ] Exclusión de marca configurada
- [ ] Asset groups por servicio con assets propios
- [ ] Presupuesto 20–30% de Search; tCPA +10–20%
- [ ] Evaluación a las 4 semanas

## Fase 6 — Conversiones offline (futuro, requiere CRM)
- [ ] Cliente comparte lista de leads cerrados con GCLID
- [ ] Importación de conversiones offline configurada
- [ ] Optimización cambiada a valor de conversión

## Recurrente (semanal, /weekly-review)
- [ ] Search terms → negativas
- [ ] Gasto vs presupuesto mensual
- [ ] CPA vs objetivo; tendencia 7d vs 28d
- [ ] Anuncios rechazados / limitados
- [ ] Impression share perdido por presupuesto y por ranking
- [ ] Calidad de leads reportada por el cliente
- [ ] Log escrito en `log/YYYY-MM-DD.md`
