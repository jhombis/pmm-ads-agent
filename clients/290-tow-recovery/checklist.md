---
cliente: 290 Tow and Recovery
slug: 290-tow-recovery
fase_actual: 1
actualizado: 2026-10-06
---
# Checklist — 290 Tow and Recovery

Base: `knowledge/checklists/setup-cuenta.md`, ajustada al cliente.
- **(B)** = bloqueante para pasar de fase.
- Responsable entre paréntesis.
- /weekly-review lo actualiza.

**Contexto (2026-10-06):** la cuenta está activa desde el 17/09 con la plantilla PLL. En 18 días gastó $530.14, CPL $88.36, con 45.8% de desperdicio rastreable. El 06-oct se aplicaron las negativas y la reestructura (F1, adelantada con OK de Jhombis); la medición de F0 sigue sin verificar. Fechas en `roadmap.md`.

## Fase 0 — Medición + negativas (2026-10-06 → 2026-10-08)
### Cuenta
- [x] (PMM) Cuenta vinculada al MCC de PMM: 213-019-5545, visible en Windsor
- [x] (PMM) Red: solo Búsqueda; socios y Display apagados (confirmado por Windsor el 10-06: 100% SEARCH)
- [x] (PMM) Diagnóstico de 18 días (`log/2026-10-06-diagnose.md`)
- [ ] (PMM) Facturación verificada (está gastando; confirmar el método de pago y quién paga, PLL)
- [ ] **(B)** (PMM) Aplicación automática de recomendaciones DESACTIVADA
- [x] **(B)** (PMM) Lista universal PMM aplicada (06-oct, a nivel campaña vía Windsor: 138 términos sin choques)
- [x] **(B)** (PMM) Lista de nicho v3 aplicada (06-oct: 95 términos, sin "cheap")
- [x] **(B)** (PMM) Negativas nuevas del diagnóstico aplicadas (06-oct: 52; resto ya cubierto o en pausa). Total cargado 285, verificado
- [x] **(B)** (PMM) Negativas viejas que bloqueaban el plan quitadas (06-oct, con OK): `kerrville towing` [exacta], `city`, `Towed`, `Get car towed`, `Shop`, `shops`. Quedan 609 negativas
- [ ] (PMM) Quitar marcas de lujo y exactas de llantas cuando el cliente confirme exotic y roadside (ver log/2026-10-06.md)
- [ ] (PMM) D7 de negativas y reestructura (13-oct): desperdicio sobre lo rastreable contra 45.8%
- [ ] (PMM) Revisar el historial de cambios en la UI: quién renombró "Ad group 1 - Towing General", quitó "emergency roadside" y creó AG2

### Medición
- [x] (PMM) Google Tag en todas las páginas: GTM-WBX4RZ9K y AW-18397446767 en el HTML; GA4 G-KH9SFWZK66 vía GTM
- [ ] **(B)** (PMM) Revisar en Detalles de llamadas las 8 llamadas (25-sep, 28-sep, 29-sep, 2-oct, 4-oct): duración, código de área y hora
- [ ] **(B)** (PMM) "Calls from Ads" con duración mínima de **60 s**, verificada en la UI
- [ ] **(B)** (PMM) Confirmar que AW-18397446767 corresponde a la cuenta 213-019-5545
- [ ] **(B)** (PMM) "Website Calls" (clic en `tel:` desde móvil) probada con Tag Assistant
- [ ] **(B)** (PMM) "Form Fill" probada con GTM Preview y Tag Assistant: dispara 1 vez por envío válido, ninguna con el captcha fallido, sin trigger nativo de Form Submission duplicado y con recuento "Una". Sale del script `submit_success` → `gtm.formSubmit`; no hay `/thank-you/` por decisión de Jhombis. Hasta probarla, queda como secundaria
- [ ] (PMM) Verificar que la misma llamada no cuenta doble (Calls from Ads + Website Calls)
- [ ] (PMM) GA4 vinculado a Ads y audiencia "Todos los visitantes" importada
- [ ] (PMM) Campos ocultos UTM + GCLID en el formulario Elementor

### Landing (ver audit-site.md v3)
- [x] (PMM) CTA "Get A Free Quote" + "Call Now" en `/exotic-vehicle-towing/`: verificados en el HTML el 10-06; el bloque vacío era un error de captura
- [x] Sin `/thank-you/`: no se crea (06-oct, decisión de Jhombis); la conversión sale del script de validación del captcha
- [ ] (PMM) Popup "Your Booking Is Not Yet Confirmed": cambiar el texto a una confirmación ("We got your request — we'll call you right back"). Hoy pide llamar, y puede contar 2 conversiones por persona (Form Fill + Website Call). Mejora, no bloqueante
- [ ] (PMM) H1 de texto en el home (hoy no hay `<h1>`; el hero es imagen): "24/7 Towing & Tow Truck Service in Fredericksburg, TX"
- [ ] (PMM) Validar el volumen local en Keyword Planner (40 mi de 78624) y actualizar `data/keywords.csv`

### Cliente
- [ ] **(B)** (Cliente) Cruzar las 8 llamadas: ¿clientes o gente que buscaba a otra grúa ("comal towing", "mission towing", "junk cars")?
- [ ] **(B)** (Cliente) Proceso de respuesta a leads: quién contesta de noche y en fin de semana, en cuánto tiempo
- [x] (Cliente) Call tracking aprobado (número de reenvío de Google)
- [ ] (Cliente) Ticket promedio y margen por servicio → CPL máximo real (referencias: cohorte nueva $51–63; maduras $15–16)
- [ ] (Cliente) ¿Atiende Fair Oaks Ranch / Bulverde / Spring Branch? ($120.84 = 22.9% del gasto, 1 conversión de un competidor)
- [x] (Web) Flatbed confirmado: "rollback and wrecker trucks" (/about-us/)
- [ ] (Cliente) ¿Remolca RV, motos o trailers? ¿Qué roadside hace (jump, lockout, llanta, gasolina)?
- [ ] (Cliente) Número de licencia TDLR + seguro (copy y LSA). ¿Atiende en español?
- [ ] (Cliente) Ofertas sostenibles: ¿confirma "upfront price on the phone"?
- [ ] (Jhombis) Avisar al cliente que la proyección realista es ~14–24 llamadas/mes en el mes 2, no 35–55

## Fase 1 — Reestructura Search (aplicada 2026-10-06 · condición 2026-10-13)
- [x] (PMM) AG1 "Ad group 1 - Towing General": 29 keywords en frase y exacta (near me, wrecker, 24 h, ciudades sin sufijo de estado); 47 amplias eliminadas (06-oct)
- [x] (PMM) "roadside assistance" en amplia eliminada ($140.05, 26% del gasto)
- [x] (PMM) AG2 "Ad group 2 - Exotic Car & Long Distance towing": 11 keywords nuevas; 6 fuera (genérico "long distance towing", "best…", "…companies" ×2, rv, trailer) (06-oct)
- [ ] (PMM) AG2: URL final `/exotic-vehicle-towing/` por keyword en exotic, luxury, classic, flatbed y rollback (en la UI; Windsor no lo permite)
- [x] (PMM) AG3 "Ad group 3 - Roadside" (200527954469) creado el 06-oct, solo exacta: [roadside assistance near me], [roadside service near me], [jump start near me], [flat tire change near me]
- [x] (PMM) Radio de 40 mi recentrado en 30.2752, -98.8720 (06-oct); exclusiones del borde de San Antonio solo si el cliente lo confirma
- [ ] (PMM) Confirmar en la UI "Presencia" solamente (Windsor no expone la opción)
- [ ] (PMM) Programación 24/7; verificar la zona horaria de la cuenta en la UI
- [x] (PMM) Puja: Maximizar clics con tope de CPC de $6.50, $27/día (06-oct)
- [x] (PMM) 1 RSA por ad group, 15H/4D (`data/ads-search-towing.md` v3), activos; los RSA viejos con "Battery Jumpstarts"/"Tire Change" en pausa (06-oct)
- [ ] (PMM) Fijar el H1 de los 3 RSA en la UI (Windsor no pinnea) y revisar la fuerza del anuncio ("Buena" o superior)
- [x] (PMM) Assets: 4 sitelinks, 8 callouts y snippet "Service catalog" a nivel campaña (06-oct)
- [ ] (PMM) Verificar en la UI el call asset (830) 463-8318 con número de reenvío. Ubicación cuando exista el GBP
- [x] (PMM) URLs finales verificadas (200, https, sin redirect): home, long-distance, roadside, exotic, light-medium (06-oct)
- [x] (PMM) Negativas por ad group (06-oct): AG1 5, AG2 4, AG3 3
- [x] (PMM) Cambios aplicados registrados con fecha en `log/2026-10-06.md`
- [ ] (PMM) Anuncios y assets aprobados por políticas (revisar el 07-oct)
- [ ] **(B)** (PMM) Primera conversión registrada después de la reestructura y cruzada con una llamada real del cliente

## Fase 2 — Limpieza
- [ ] (PMM) D7 (2026-10-13): search terms → negativas; gasto <70% del presupuesto → keywords de ciudad + AG3 a frase
- [ ] (PMM) D14 (2026-10-20): search terms → negativas; AG2 con más de $100 y 0 llamadas → pausar; AG3 >20% del gasto → pausar
- [ ] (PMM) D30 (2026-11-05): search terms → negativas; keywords con 0 impresiones pausadas; desperdicio <15% del rastreable
- [ ] (Cliente) D30: calidad de las llamadas reportada (hoja compartida: llamada → trabajo sí/no → ticket)

## Fase 3 — Optimización de puja (Max conv por resultados desde el D14, 10-20 · tCPA ~2027-01)
- [ ] (PMM) Max. conversiones en la primera revisión que cumpla: medición F0 cerrada + (≥10 conversiones verificadas en los primeros 14 días **o** ≥15 acumuladas desde el 06-oct) + desperdicio <25% en 7 días. Mismo presupuesto, sin tCPA
- [ ] (PMM) 14 días después del cambio: revertir a Max. clics con tope de $6.50 si conversiones/día caen >30%, CPL > $63 o CPC > $12 sin más conversiones
- [ ] (PMM) ≥30 conversiones en 30 días → tCPA = CPL real de 30 días × 1.1 (no el deseado)
- [ ] (PMM) Prueba de grupo en español ("grua cerca de mi", "servicio de grua") si el cliente atiende en español
- [ ] (PMM) Presupuesto revisado según CPL y capacidad del cliente

## Fase 4 — Remarketing (no califica por volumen)
- [ ] (PMM) Audiencia de visitantes ≥1,000 en 30 días. Revisar mensualmente en GA4

## Fase 5 — Performance Max
**Bloqueada hasta ≥2027-03:** faltan 6 meses de Search estable, 30+ conversiones/mes verificadas, assets propios y GBP, y el presupuesto es de $27/día contra ~$44 de mínimo.
- [ ] (Cliente) Fotos reales de las grúas y del equipo (5+) y un video corto: sirven para PMax y para el sitio
- [ ] (Jhombis/PLL) Evaluar si el fee permite ≥$1,300/mes de pauta

## Fase 6 — Conversiones offline (futuro, requiere CRM)
- [ ] (Cliente) Registro de trabajos con fecha, hora y teléfono para cruzar con las llamadas

## Pista Landing (mejoras)
- [ ] (PMM) Velocidad del home: móvil 43, LCP 6.7 s, TBT 1,170 ms → LCP <3 s (WebP, caché, JS de Elementor)
- [ ] (PMM) Navy Veteran, 10% Senior Discount y radio en texto, no solo en la imagen
- [ ] (PMM) Meta description + JSON-LD LocalBusiness/TowingService + `alt` en las imágenes
- [ ] (PMM) Formulario de emergencia de 3 campos (Name, Phone, Location)

## Pista GBP + LSA
- [ ] **(B para Maps/LSA)** (Cliente) Crear y verificar el GBP (área de servicio, categoría "Towing service"). Objetivo: ~2026-10-27
- [ ] (PMM) Vincular el GBP a Ads y activar el activo de ubicación
- [ ] (Cliente) Proceso de reseñas después de cada servicio (los competidores tienen 70–157)
- [ ] (PMM) Solicitud LSA (licencia TDLR, seguro, background check). Objetivo: ~2026-10-27
- [ ] (PMM) LSA verificado y con presupuesto semanal definido. Objetivo: ~2026-11-24

## Recurrente (semanal, /weekly-review)
- [ ] Search terms → negativas
- [ ] Gasto contra los $825 mensuales (tope $820.80)
- [ ] CPL contra el objetivo (meses 1–2: $30–60; meses 3–6: $21–38); tendencia 7 d contra 28 d
- [ ] % de gasto de AG3 roadside y de AG2 exotic/long-distance
- [ ] Anuncios rechazados o limitados
- [ ] Impression share perdido por presupuesto y por ranking
- [ ] Calidad de las llamadas reportada por el cliente
- [ ] Log en `log/YYYY-MM-DD.md`
