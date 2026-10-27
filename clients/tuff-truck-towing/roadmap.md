---
cliente: Tuff Truck Towing
slug: tuff-truck-towing
D0: 2026-10-27
actualizado: 2026-10-27
fase_actual: 0
plan_es: https://claude.ai/artifact/EtXuJ1EMrY3pVwjNiwcTvE
plan_en: https://claude.ai/artifact/SXJzd5AN6xtkuqCGKqeAY7
---

# Roadmap — Tuff Truck Towing

> Las fechas son una proyección; la condición de paso es la que manda. `/weekly-review` avanza de fase solo cuando se cumple la condición.
>
> Inputs: brief.md, audit-site.md (7/22, requiere ajustes), competitors.md, benchmark.md y strategy.md v1. Cuenta 727-278-3398. Pauta estimada en ~$700/mes, de un paquete de $1,400.

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Fundación | 2026-10-27 → 2026-11-09 | 🔄 en curso, con bloqueantes del cliente y de Bree |
| 1 — Lanzamiento Search (T1 + T2) | 2026-11-10 → 2026-11-17 | ⏳ |
| 2 — Limpieza D7 · D14 · D30 (+ E1) | 2026-11-17 · 2026-11-24 · 2026-12-10 | ⏳ |
| Hito: Max. clics → Max. conversiones | ~2027-01-11 (día 60), con 15+ conv/mes estables | ⏳ |
| 3 — tCPA | primer chequeo 2027-03-10 (mes 4) | ⏳, probablemente ⛔ con $700/mes (ver supuesto) |
| 4 — Remarketing | no antes de 2027-T2 | ⛔ no califica por tráfico (<1,000 usuarios/30 días) |
| 5 — PMax | no realista con ~$700/mes | ⛔ por presupuesto y volumen |
| 6 — Conversiones offline | fuera de alcance | — |
| Pista Landing | /towing 2026-10-27 → 2026-11-07 · /equipment → 2026-11-24 | 🔄 |
| Pista LSA | 2026-11-03 → 2026-12-01 | ⏳ (depende del GBP) |

## Fase 0 — Fundación
- **Fecha estimada**: 2026-10-27 → 2026-11-09 (D0+13).
  - Base de 3 días + 7–14 porque el sitio lo edita el cliente (Wix, audit-site.md).
  - Si PMM publica /towing con `/landing` en performancemediamarketing.com, puede bajar a ~D0+7, siempre que lleguen a tiempo los límites de Tulsa y el monto de medios.
- **Condición de paso**: todos los ítems bloqueantes de la Fase 0 del checklist en ✅. Lo crítico:
  - conversiones de llamada probadas con Tag Assistant;
  - /towing publicada;
  - ZIP de Tulsa confirmados;
  - negativas aplicadas;
  - monto de medios confirmado.
- **Tareas** (responsable):
  - (Jhombis) Confirmar el monto de medios del paquete de $1,400 (~$700 estimado). Si queda por debajo de $600, E1 sale de la estrategia.
  - (Jhombis) Mandar las preguntas del brief al cliente: ticket y margen, peso máximo, fines de semana, acceso al Wix y al GBP, dueño del tag AW-1004387232, heavy/RV/motos, [C] del copy.
  - (Jhombis + Bree) ZIP y pines al este de Memorial Dr sobre el mapa; límites norte y sur; Claremore sí o no.
  - (PMM) Conectar 727-278-3398 a Windsor o a la API, y revisar si ya tiene campañas, conversiones o recomendaciones automáticas.
  - (PMM) Facturación, recomendaciones automáticas apagadas, lista universal PMM (sin "equipment" ni "cheapest") + `data/negatives-nicho.txt`.
  - (PMM) Google tag de 727-278-3398 en /towing y en la web, más estas conversiones:
    - "Llamadas desde anuncios" ≥60 s;
    - "Llamada desde la web" con número de reenvío de Google sobre (918) 320-7595, ≥60 s;
    - "Formulario" en /thank-you;
    - "Clic en teléfono", como secundaria.
  - (Jhombis/Cliente) Decidir qué se hace con el tag AW-1004387232: vincular su cuenta, quitarla o dejarla sin conversiones primarias.
  - (Cliente) Quitar el `tel:` del fax; (918) 894-0368 solo en /hauling.
  - (Cliente) Quién contesta las llamadas y en qué horario (lun–vie 7–21 o más).
- **Riesgos**:
  - El cliente tarda con el acceso al Wix → plan B: `/landing` de PMM.
  - Bree no confirma la geo → no se lanza con "Tulsa" completa.
  - La cuenta trae configuración heredada → se revisa antes de `/build-campaign`.

## Fase 1 — Lanzamiento Search
- **Fecha estimada**: 2026-11-10 (lunes) → 2026-11-17.
- **Condición de paso**: campaña activa 7 días, anuncios aprobados y ≥1 conversión de llamada ≥60 s registrada (confirma el tracking en producción). CallFire debe mostrar las mismas llamadas, separadas de las orgánicas.
- **Qué se lanza** (strategy.md, F1):
  - "Search | Towing & Hauling | BA-East Tulsa | v1" a $32/día, solo lun–vie 7:00–21:00 Central.
  - T1 Towing Near Me + T2 Towing Ciudades.
  - Max. clics con tope de $9, frase + exacta, Presencia.
  - 1 RSA por grupo y las extensiones.
  - E1 creado **en pausa**.
- **Riesgos**:
  - CPC de más de $9 → poco volumen (se revisa el tope, no se quita).
  - El gasto de la semana 1 se pasa de ~$160 por el tope mensual de Google ($973): hay que vigilarlo.
  - Llamadas fuera de horario sin contestar.

## Fase 2 — Limpieza (D7 · D14 · D30)
- **Fechas**: D7 = 2026-11-17 · D14 = 2026-11-24 · D30 = 2026-12-10.
- **Condición de paso**: las tres revisiones hechas, negativas aplicadas, keywords sin impresiones identificadas (y pausadas en D30). **E1 activado** si /equipment está publicada (objetivo 2026-11-24).
- **Qué se revisa**:
  - search terms: ciudades fuera del área, brokers, compra o alquiler de equipos, heavy-duty;
  - gasto sin conversión (keywords con ≥$100 y 0 conversiones);
  - llamadas en CallFire: contestadas, ≥60 s, fuera de horario, fuera del estado;
  - IS perdido por presupuesto y por ranking.
  - No hay A/B: con ~84 clics/mes es ruido (1 RSA por grupo).
- **Ventana**: Thanksgiving (2026-11-26) cae entre D14 y D30. La semana del 23-nov tendrá menos días hábiles y menos llamadas B2B; no hay que leerla como caída.

## Hito — Max. clics → Max. conversiones
- **Fecha estimada**: ~2027-01-11 (día 60).
- **Condición**: 15+ conversiones de llamada calificadas (≥60 s) en 30 días, con la medición limpia.
- **Supuesto**: ~13 conversiones/mes en los meses 1–2 a ~$700 (benchmark: cohorte nueva, CPL ~$51). Con eso, el umbral de 15 aparece hacia el día 45–60.
- Las cuentas del MCC que se quedan en Max. clics tienen CPL de $70–83, así que el cambio no se pospone si la condición se cumple antes.

## Fase 3 — Optimización de puja (tCPA)
- **Fecha estimada**: primer chequeo el **2027-03-10 (mes 4)**; lo realista es que **no califique** con ~$700/mes.
- **Supuesto explícito**:
  - Conversiones por día esperadas = presupuesto diario promedio ($23) ÷ CPL del benchmark. A $51 (meses 1–2) da 0.45/día; a $26–33 (mes 3+) da 0.7–0.9/día.
  - Hacen falta 30 en una **ventana de 30 días** (1/día). A $700 se llega solo con un CPL de ≤$23, por debajo de la mediana de Search.
  - Además, el presupuesto ($32/día activo) es menor que 3× el CPL ($153): el aprendizaje es lento (+2 semanas).
  - El horario lun–vie y la geo recortada restan volumen.
- **Condición de paso**: ≥30 conversiones calificadas en 30 días con tracking verificado.
- **Acción**: tCPA = CPA real observado ×1.1 y presupuesto reajustado.
- **Si no se cumple en fecha**: seguir en Max. conversiones **sin tCPA** (es lo que hace el cuartil superior del MCC). Revisar la tasa de conversión de la landing (<5% → la landing), el IS perdido por presupuesto (>40% con CPL en objetivo → proponer más pauta) y los search terms. **No se fuerza tCPA con menos datos.**

## Fase 4 — Remarketing
- **Fecha estimada**: no antes de 2027-T2.
- **Condición de paso**: audiencia ≥1,000 usuarios en 30 días.
- **Por qué no califica**: ~84 clics/mes de Ads más ~136 visitas orgánicas/mes (Semrush) dan ~220 usuarios/mes.
- **Si cambia el volumen**: RLSA en observación para E1 (hauling B2B: contratistas que vuelven). Display de remarketing no aplica.

## Fase 5 — Performance Max
- **Fecha estimada**: no realista con ~$700/mes.
- **Condiciones que fallan** (pmax-cuando-y-como.md):
  1. ≥30 conversiones/mes (ver Fase 3);
  2. tCPA activo 4 semanas;
  3. presupuesto ≥3× el CPA por día (~$150/día contra $23);
  4. assets propios: 5+ imágenes reales y un video (hoy hay pocas fotos y ningún video);
  5. landing con ≥5% de conversión y anti-spam (no existe).
- **Qué hacer para cumplirlas**: subir la pauta a ≥$1,500/mes, sostener un CPL de ≤$25 y conseguir fotos y video.
- **Mientras tanto**: Search + LSA.

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance; no hay CRM. Se reevalúa cuando el cliente registre leads con GCLID (formulario /thank-you con campos ocultos).

## Pista paralela — Landing
| Ajuste (audit-site.md) | Tipo | Fecha | Responsable |
|---|---|---|---|
| /towing: H1 de servicio + ciudad, llamada fija en móvil, formulario de 4 campos → /thank-you, horario real, DPS/MC/DOT, área de servicio, bloque medium-duty | **Bloqueante F0** | 2026-11-07 | PMM (/landing) o Cliente (Wix) |
| Google tag 727-278-3398 + llamada desde la web (reenvío de Google) | **Bloqueante F0** | 2026-11-07 | PMM |
| Un solo teléfono de servicio (fuera el `tel:` del fax; 894-0368 solo en /hauling) | **Bloqueante F0** | 2026-11-07 | Cliente |
| Tag AW-1004387232: decidir | **Bloqueante F0** | 2026-11-07 | Jhombis/Cliente |
| /equipment: formulario de cotización (qué, origen, destino, fecha), peso máximo, forklifts/skid steers/contenedores | Bloqueante de E1 (F2) | 2026-11-24 | PMM o Cliente |
| "24/7" fuera de la home si no es real | Mejora F2 | 2026-11-24 | Cliente |
| Reseñas (widget del GBP), confianza en la home, oferta | Mejora F2–3 | 2026-12-10 | Cliente |
| "Experienced Driver? Apply Now!" fuera del primer pantallazo | Mejora F2 | 2026-11-24 | Cliente |
| PageSpeed móvil con clave | Mejora F2 | 2026-11-17 | PMM |

## Pista paralela — LSA
- **2026-11-03**: verificar en el panel de LSA que Towing esté disponible en Broken Arrow / Tulsa e iniciar la solicitud (requiere GBP verificado con acceso de PMM).
- **2026-11-17 → 2026-12-01**: background check, licencia (DPS 53342-W) y seguro (2–4 semanas).
- **Luego**: presupuesto semanal aparte del de Search; gestionar reseñas (hoy no hay ninguna visible).
- **Bloqueo**: sin acceso al GBP no arranca.

## Estacionalidad y ventanas
- **Invierno en Oklahoma** (dic–feb): las tormentas de hielo disparan la demanda de remolque. Lanzar en noviembre deja D30 limpio antes de la temporada. Con horario lun–vie se pierde la demanda de los fines de semana con hielo: conviene preguntarle al cliente si atiende esos días.
- **Hauling B2B** (equipment/contenedores): probablemente baja en diciembre por fiestas y obra más lenta (inferido, sin datos). Activar E1 el 24-nov y evaluarlo en el primer trimestre de 2027, a los 50 clics.
- **Thanksgiving 2026-11-26 y fiestas de fin de año**: semanas cortas; se comparan contra la mediana, no contra la semana anterior.

## Historial de cambios
- 2026-10-27: creado (D0 = 2026-10-27). Inputs: brief, audit-site, competitors, benchmark, strategy v1. URLs del plan pasadas desde brief.md.
