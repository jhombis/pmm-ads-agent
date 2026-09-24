---
cliente: 290 Tow and Recovery
slug: 290-tow-recovery
D0: 2026-09-24
actualizado: 2026-09-24
fase_actual: 0
---

# Roadmap — 290 Tow and Recovery

> **Contexto:** la cuenta 213-019-5545 **ya está activa desde el 17/09** con la plantilla PLL: amplia, Maximizar clics y sin negativas. En 6 días gastó $165.57 con 0 conversiones y un 43% de desperdicio claro. Por eso la Fase 1 no es un lanzamiento desde cero: es la **reestructuración** de esa campaña según `strategy.md`. Mientras dure la Fase 0, la campaña actual sigue gastando unos $27/día, salvo que Jhombis decida pausarla o cargar solo las negativas.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Fundación | 2026-09-24 → 2026-09-29 | 🔄 en curso |
| 1 — Reestructuración Search | 2026-09-30 → 2026-10-07 | ⏳ pendiente |
| 2 — Limpieza D7 · D14 · D30 | 2026-10-07 · 2026-10-14 · 2026-10-30 | ⏳ pendiente |
| 3 — Maximizar conversiones → tCPA | Max Conv ~2026-10-14 · tCPA ~2026-11-11 | ⏳ pendiente |
| 4 — Remarketing (RLSA) | No antes de 2027-Q1 | ⛔ probablemente no califica (volumen) |
| 5 — Performance Max | No realista con $27/día | ⛔ bloqueada (presupuesto y assets) |
| 6 — Conversiones offline | Fuera de alcance | ⏳ futuro |
| Pista Landing | 2026-09-24 → 2026-10-14 | 🔄 en curso |
| Pista GBP + LSA | GBP ~2026-10-15 · LSA ~2026-11-12 | ⏳ pendiente (cliente) |

## Fase 0 — Fundación
- **Fecha estimada**: 2026-09-24 → 2026-09-29 (D0+5). Son 3 días por los ajustes bloqueantes del sitio (los hace PMM) y 2 de margen para las respuestas del cliente.
- **Condición de paso**: todos los ítems bloqueantes de Fase 0 en `checklist.md` ✅. El mínimo es tracking verificado, CTA de exotic arreglado, página de gracias, negativas cargadas, geo recentrada y proceso de respuesta confirmado.
- **Tareas**:
  - **PMM**:
    - Probar con Tag Assistant las 3 conversiones: Calls from Ads con umbral de **60 s**, Website Calls (clic en `tel:`) y Form Fill.
    - Confirmar que AW-18397446767 es de la cuenta 213-019-5545 y que una misma llamada no se cuenta dos veces.
  - **PMM**: crear `/thank-you/` y configurar el redirect del formulario Elementor, o usar un disparador de GTM sobre `submit_success`. Agregar campos ocultos UTM/GCLID.
  - **PMM**: arreglar los CTA faltantes en `/exotic-vehicle-towing/`.
  - **PMM**: validar el volumen local en Keyword Planner (UI, 40 mi de 78624) para las keywords de `data/keywords.csv`.
  - **PMM**: aplicar a nivel de cuenta la lista universal PMM + `data/negatives-nicho.txt` (vía `/negatives`, con aprobación de Jhombis).
  - **PMM**: desactivar la aplicación automática de recomendaciones. Verificar que sigan apagados los socios de búsqueda y Display.
  - **Cliente**:
    - Confirmar ticket y margen por servicio, y el servicio estrella.
    - Confirmar quién contesta de noche y en cuánto tiempo.
    - Confirmar si atiende Boerne y Fair Oaks Ranch.
    - Confirmar la capacidad de flatbed, RV y moto.
    - Dar el número de licencia TDLR y el seguro.
  - **Jhombis**: decidir qué pasa con la campaña actual mientras dura la Fase 0: dejarla, pausarla o cargar solo las negativas.
- **Riesgos**:
  - Si el cliente tarda en responder, el ticket y la geo quedan como supuestos. Se lanza igual (no bloquean la reestructuración), pero el CPL objetivo sigue siendo provisional.
  - Cada día de Fase 0 con la configuración actual cuesta ~$27, con alrededor de 40% de desperdicio.

## Fase 1 — Reestructuración Search
- **Fecha estimada**: se aplica el 2026-09-30 y pasa la condición el 2026-10-07.
- **Condición de paso**: la campaña reestructurada lleva 7 días activa, los anuncios están aprobados y hay **≥1 conversión registrada y verificada** (una llamada real que llegó al cliente).
- **Qué se lanza** (`/build-campaign`, según `strategy.md` F1):
  - La campaña actual reestructurada: 7 ad groups en frase y exacta, AG5 exotic en pausa hasta arreglar su landing, 3 RSA por grupo y los assets de `data/ads-search-towing.md`.
  - Puja: Maximizar clics con **tope de CPC de $6.50**, **$27/día**, 24/7.
  - Geo: presencia, radio de 40 mi recentrado en Fredericksburg, con exclusiones del borde de San Antonio.
  - Se eliminan las 10 keywords en amplia.
- **Riesgos**:
  - **Volumen**: tras quitar la amplia y recentrar, la campaña puede no gastar $27/día. Si en el D7 gasta menos del 70%, se abre AG7 a frase o se agrega "motorcycle towing". No se vuelve a la amplia.
  - La respuesta a leads todavía no está confirmada: una llamada no atendida de noche es un lead perdido.

## Fase 2 — Limpieza (D7 · D14 · D30)
- **Fechas**: **2026-10-07** (D7) · **2026-10-14** (D14) · **2026-10-30** (D30), contadas desde el 2026-09-30.
- **Condición de paso**: las tres revisiones hechas con `/weekly-review`, negativas aplicadas y keywords sin impresiones en 30 días pausadas.
- **Qué se revisa**:
  - Search terms: vigilar Virginia, San Antonio, equipo, jump starters, transporte y competidores.
  - Gasto sin conversión por ad group. Regla: pausar AG5 o AG6 si superan $100 sin llamadas.
  - Porcentaje de AG7 roadside sobre el gasto (tope 20%).
  - CPC real contra el tope.
  - RSA con peor rendimiento por grupo en el D30.
  - Calidad de las llamadas reportada por el cliente en el D30.

## Fase 3 — Optimización de puja
- **Paso A: Maximizar conversiones (sin tCPA)**
  - **Fecha estimada**: ~2026-10-14.
  - **Condición**: ≥15 conversiones verificadas **o** 14 días con tracking comprobado y CPC ≤ $7.
- **Paso B: tCPA**
  - **Fecha estimada**: **~2026-11-11** (6 semanas desde el lanzamiento).
  - **Supuesto**: $27/día ÷ CPL benchmark de $14.57 = 1.85 conversiones/día, así que harían falta ~16 días para llegar a 30. Se usa el mínimo de 21 días y se suman **+2 semanas** porque el presupuesto ($27/día) queda por debajo de 3× CPL ($44/día). Además, las primeras 2 semanas corren con Max clics.
- **Condición de paso**: **≥30 conversiones en una ventana de 30 días** con tracking verificado y umbral de llamada de 60 s.
- **Acción**: tCPA = CPL real de 30 días × 1.1, nunca el CPL deseado. Presupuesto sin cambios salvo que el cliente amplíe el fee.
- **Si no se cumple en fecha**:
  - Si la conversión clic→llamada es menor al 15%: revisar la landing (H1, CTA arriba, velocidad).
  - Si el CPC es mayor a $7: revisar keywords y subasta.
  - Si el volumen no alcanza: aceptar Max conversiones sin tCPA como estado estable. **No forzar tCPA con menos datos.**

## Fase 4 — Remarketing
- **Fecha estimada**: no antes de 2027-Q1.
- **Condición de paso**: audiencia de visitantes ≥1,000 usuarios en 30 días. Es el mínimo de Google para RLSA en Search.
- **Realidad**:
  - Con ~125–165 clics pagados al mes y tráfico orgánico ≈ 0 (Semrush), el sitio **no llega a 1,000 visitantes/mes**.
  - Además, towing es compra de emergencia: el remarketing aporta poco.
- **Acción si califica**: RLSA en observación y ajuste de puja después. Display remarketing no.

## Fase 5 — Performance Max
- **Fecha estimada**: **no realista con el presupuesto actual.**
- **Condiciones que fallan** (`knowledge/estrategias/pmax-cuando-y-como.md`):
  1. **Presupuesto**: PMax necesita ≥3× CPA/día (~$44/día) solo para PMax, además de Search. El total de la cuenta es $27/día.
  2. **Assets propios**: el sitio usa fotos de stock. No hay imágenes reales, video ni reseñas.
  3. **GBP**: no existe todavía.
  4. **Condiciones de datos**: falta ≥4 semanas de tCPA estable con ≥30 conversiones al mes, que se estiman para diciembre de 2026 en el mejor caso.
- **Qué haría falta**:
  - Que el fee suba lo suficiente para ≥$1,300/mes de pauta.
  - Fotos reales de las grúas y del equipo, más un video corto.
  - GBP con reseñas.
  - Se reevalúa a 90 días (~2026-12-29). En el MCC, PMax sí baja el CPL de towing (a $5.9–6.5), pero solo en cuentas con historial y más presupuesto.
- **Mientras tanto**: solo Search.

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance. El cliente no tiene CRM (PENDIENTE confirmar dónde registra los trabajos). Se reevalúa cuando haya un registro de leads con GCLID, o como mínimo una hoja compartida de llamadas y trabajos cerrados para la calidad de lead en el D30.

## Pista paralela — Landing
Los ajustes salen de `audit-site.md`. Responsable: PMM.

| Ajuste | Tipo | Fecha |
|---|---|---|
| CTA faltantes en `/exotic-vehicle-towing/` | **Bloqueante F0** (AG5) | 2026-09-26 |
| `/thank-you/` + redirect del formulario + campos UTM/GCLID | **Bloqueante F0** | 2026-09-26 |
| H1 del home: "24/7 Towing & Tow Truck Service in Fredericksburg, TX", y "45-minute radius" → 40 mi | Mejora (landing de AG1/AG3/AG4) | 2026-09-29 |
| CTA de llamar/cotizar arriba del texto en las páginas de servicio | Mejora | 2026-10-07 |
| "Upfront price before we tow / no hidden fees" en el hero y los callouts | Mejora | 2026-10-07 |
| TDLR # + "Licensed & Insured" visibles (cuando el cliente dé los datos) | Mejora | Al recibir el dato |
| Velocidad móvil: WebP, caché, CSS/JS de Elementor sin usar (LCP de 5.7–6.9 s → <3 s) | Mejora F2 | 2026-10-14 |
| Formulario de 3 campos (Name, Phone, Location) | Mejora F2–3 | 2026-10-14 |
| Testimonios y fotos reales de las grúas | Mejora F3 (depende del cliente) | Cuando el cliente las envíe |

## Pista paralela — GBP + LSA (US, towing califica)
- **2026-09-24 → ~2026-10-15**: el cliente crea el **Google Business Profile** como área de servicio, sin dirección visible si opera desde casa. Categoría principal "Towing service" y verificación por video. PMM da la guía.
  - En cuanto se verifica, PMM vincula el GBP a Ads (activo de ubicación y Maps).
  - Arranca la **campaña de reseñas**: pedirlas después de cada servicio. Los competidores tienen 70–157 reseñas.
- **~2026-10-15**: solicitud LSA con licencia TDLR, seguro y background check.
- **~2026-10-29 → 2026-11-12**: verificación LSA (2–4 semanas).
- **Después**: presupuesto semanal de LSA separado (pay-per-lead) o tomado de los $825. **Decisión del cliente y de Jhombis.** En servicios locales, el LSA suele salir a ~50% del CPL de Search.
- **Bloqueante**: sin GBP verificado no avanza nada de esta pista.

## Estacionalidad y ventanas
- **Fredericksburg Oktoberfest (primer fin de semana de octubre) y temporada de vinerías y turismo de otoño**: más tráfico de visitantes en la Hwy 290 y posibles picos de llamadas de fin de semana. La presencia capta a los turistas varados.
- **Luces de fin de año (noviembre y diciembre)** y **Spring Break / wildflowers (marzo y abril)**: más turismo, así que más demanda de towing.
- **Heladas de invierno** (ejemplo: febrero de 2021): pocas pero intensas, con picos de accidentes y jump starts. Si hay alerta de helada, revisar el tope de CPC y la capacidad del cliente.
- **Verano (junio–agosto)**: el calor provoca averías y sube la demanda de roadside. Vigilar el tope de AG7.
- Conclusión: **no hay razón para retrasar la reestructuración**. Octubre es buena ventana para lanzar.

## Historial de cambios
- 2026-09-24: creado. D0 = hoy. Cuenta activa desde el 2026-09-17 con la configuración PLL.
