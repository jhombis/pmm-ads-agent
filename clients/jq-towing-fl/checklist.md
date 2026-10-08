---
cliente: JQ Towing
slug: jq-towing-fl
fase_actual: 0
actualizado: 2026-10-08
---

# Checklist — JQ Towing

Basado en `knowledge/checklists/setup-cuenta.md`. Fase 5 (PMax) eliminada porque no califica con $879/mes (ver roadmap). /weekly-review lo actualiza.

## Pendientes de onboarding (bloqueantes de Fase 0)
- [x] (Cliente) ID de la cuenta previa: 986-810-9972
- [ ] (Cliente) Ticket promedio, margen y tasa de cierre → CPL máximo
- [x] (Cliente) Call tracking: CallFire (352) 645-5030 → (352) 282-2512, conectado al MCP (2026-10-08)
- [ ] (Cliente) Decir dónde está publicado hoy (352) 645-5030 (web, GBP, directorios)
- [ ] (Cliente) Subir la tasa de contestadas del 75% al ≥ 80% (CallFire 14-sep → 08-oct: 4 de 18 llamantes nunca hablaron)
- [ ] (Cliente) Confirmar servicios: lockout, jump, llanta, fuel, flatbed, golf cart, heavy duty, junk car
- [ ] (Cliente) Confirmar claims del copy marcados con `*` (licensed & insured, upfront quote, no hidden fees, flatbed, base en Belleview, long-distance)
- [ ] (PMM) Conectar 986-810-9972 a Windsor o configurar API; leer historial, conversiones y Auction Insights → decidir puja inicial
- [ ] (PMM) Permitir jqtowingfl.com en el entorno y re-correr /audit-landing

## Fase 0 — Fundación (bloqueante para lanzar)
- [ ] (PMM) Cuenta 986-810-9972 vinculada al MCC con acceso admin (confirmar nivel de acceso)
- [ ] (PMM) Facturación configurada y verificada
- [ ] (Cliente) Google Business Profile verificado, categoría principal "Towing service"
- [ ] (PMM) GBP vinculado a Google Ads (activo de ubicación)
- [ ] (PMM) Google Tag instalado en todas las landings (/towing, /roadside-assistance, /thank-you)
- [ ] (PMM) Conversión "Formulario" (thank-you con URL propia) creada y probada con Tag Assistant
- [ ] (PMM) Conversión "Llamada desde anuncio" ≥ 60 s
- [ ] (PMM) Conversión "Llamada al número de desvío en el sitio" ≥ 60 s (Google reemplaza (352) 645-5030 en el sitio)
- [ ] (PMM) Activo de llamada con (352) 645-5030 e informes de llamadas activados
- [ ] (PMM) Conversión "Clic en teléfono" en móvil como SECUNDARIA
- [ ] (PMM) Revisar y limpiar conversiones heredadas de la cuenta previa (sin llamadas de 20 s ni primarias duplicadas)
- [ ] (PMM) GA4 vinculado y audiencia "Todos los visitantes" importada
- [ ] (PMM) Campos ocultos UTM + GCLID en el formulario
- [ ] (PMM) Lista de negativas universal PMM aplicada a nivel de cuenta
- [ ] (PMM) `data/negatives-nicho.txt` aplicada (ajustada a los servicios confirmados)
- [ ] (PMM) Aplicación automática de recomendaciones DESACTIVADA
- [ ] (PMM) Landings `/towing`, `/roadside-assistance` y `/thank-you` publicadas (200, https) y aprobadas por /audit-landing
- [x] (Cliente) 24/7 real: CallFire muestra llamadas contestadas a las 00:30, 01:07, 03:00 y 03:06 (2026-10-08)
- [ ] (Cliente) Quién contesta y en cuánto tiempo
- [ ] (Cliente) Hoja compartida de leads cerrados (fecha, teléfono, servicio, monto) para calidad de lead
- [ ] (Cliente) Licencia, seguro y background check confirmados → (PMM) solicitud LSA iniciada

## Fase 1 — Lanzamiento Search (objetivo 2026-10-15)
- [ ] Campaña `JQ | Search | Towing & Roadside | 15mi` creada según `strategy.md`
- [ ] Red: solo Búsqueda; socios y Display apagados
- [ ] Ubicación: radio de 15 mi desde 29.045014, -82.037279, solo Presencia; resto de países excluidos
- [ ] Programación 24/7
- [ ] Puja: Maximizar clics con CPC máx. $9 (Max. conversiones si el historial trae 15+ conversiones/mes limpias)
- [ ] Keywords en frase; exacta para los top términos (ver `data/keywords.csv`)
- [ ] Cross-negatives entre ad groups aplicadas
- [ ] 1 RSA por ad group (< $1,500/mes), H1 pinneado, 15H/4D, fuerza "Buena" o superior; claims `*` no confirmados eliminados
- [ ] Extensiones: 4 sitelinks, 6+ callouts, snippet de servicios, llamada, ubicación
- [ ] URLs finales verificadas (200, https, sin redirect)
- [ ] Presupuesto diario $29
- [ ] Anuncios aprobados (revisar 24 h después)
- [ ] Primera conversión real registrada

## Fase 2 — Limpieza
- [ ] D7 (2026-10-22): search terms → negativas; CallFire (contestadas, calificadas, horario) vs conversiones de llamada de Ads
- [ ] D7: keywords sin impresiones identificadas (no pausar aún)
- [ ] D14 (2026-10-29): search terms → negativas
- [ ] D14: keywords con gasto > $40 y 0 conversiones marcadas para revisión
- [ ] D14: CPC real vs supuesto de $7
- [ ] D30 (2026-11-14): search terms → negativas
- [ ] D30: keywords con 0 impresiones en 30 días pausadas
- [ ] D30: peor RSA por grupo reemplazado
- [ ] D30: reporte de calidad de leads del cliente recibido
- [ ] D30: reevaluar campaña de marca y tamaño de la audiencia de remarketing

## Fase 3 — Optimización de puja (~2026-12-01)
- [ ] 15+ conversiones/mes limpias → Maximizar conversiones
- [ ] ≥ 30 conversiones en 30 días confirmadas
- [ ] tCPA = CPA real observado (no el deseado)
- [ ] Presupuesto reajustado según CPA, IS perdido por presupuesto y capacidad del cliente
- [ ] Ajustes de puja por horario y dispositivo evaluados con datos (noche vs día)

## Fase 4 — Remarketing (bloqueada: audiencia < 1,000)
- [ ] Audiencia de visitantes ≥ 1,000 usuarios en 30 días
- [ ] RLSA: audiencia de visitantes en Search en observación

## Fase 6 — Conversiones offline (futuro, requiere CRM)
- [ ] Cliente comparte leads cerrados con GCLID
- [ ] Importación de conversiones offline configurada

## Recurrente (semanal, /weekly-review)
- [ ] Search terms → negativas
- [ ] Gasto vs presupuesto mensual ($879)
- [ ] CPA vs objetivo ($25–38); tendencia 7 d vs 28 d
- [ ] Anuncios rechazados o limitados
- [ ] Impression share perdido por presupuesto y por ranking
- [ ] Calidad de leads reportada por el cliente
- [ ] Log escrito en `log/YYYY-MM-DD.md`
