---
cliente: AAMCO Transmissions & Total Car Care — 103rd St (Jacksonville)
slug: aamco-jacksonville-103rd
nicho: taller (transmisiones / auto repair)
pais: US
cuentas_comparables: 7 campañas Search AAMCO (misma cuenta) + 2 cuentas de taller afines (solo referencia)
periodo: 90d (2026-06-25 → 2026-09-22)
actualizado: 2026-09-23
---

# Benchmark interno — AAMCO 103rd St

> **Cómo se armó**: el MCC no tiene etiquetas `nicho:*` / `pais:*` (Windsor muestra 62 cuentas sin etiquetar). Las comparables se eligieron por nombre:
> - **Principal**: las 7 campañas Search "ZETA Radius" de AAMCO Ad Pool (468-970-4116): St. Augustine, Biscayne, 103rd, San Jose, Atlantic, Orange Park, St. Marys. Mismo nicho, marca, mercado (NE Florida / SE Georgia), plantilla y tracking.
> - **Afín, excluida de los percentiles**: Beacon Automotive (328-153-9215) y Beachaven Auto Care & Towing (742-239-3943). Son solo PMax, miden solo "Calls from ads" y tienen $250–420/mes: no son comparables con Search.
> - Datos de Windsor.ai (no API directa). Se sugiere etiquetar las cuentas del MCC con `nicho:auto-repair` y `pais:US`.

## ⚠️ Advertencia principal
**Las 7 campañas AAMCO comparten la misma medición inflada**: "Calls from ads", CallRail y "Phone Call" como primarias a la vez (ver `evaluacion-search-2026-09-23.md`, P1). Por eso el benchmark se da en dos bases:
- **Reportado**: todas las conversiones primarias, como las ve Google.
- **Solo CallRail**: una sola fuente de llamada. Es la estimación menos inflada disponible, pero tampoco filtra llamadas repetidas o cortas.

Ninguna de las dos es CPL de lead calificado. Sirven para comparar sedes entre sí, no para fijar un tCPA.

## Rangos esperados (7 campañas Search AAMCO, 90 días)
| Métrica | P25 | Mediana | P75 | 103rd |
|---|---|---|---|---|
| CPC | $6.19 | $6.41 | $7.22 | $6.25 |
| CTR | 6.2% | 6.5% | 6.75% | **5.5%** (el más bajo) |
| Tasa conv. (reportada) | 31.7% | 34.1% | 39.3% | 38.9% |
| CPL (reportado) | $16.85 | $19.50 | $21.70 | $16.08 |
| Tasa conv. (solo CallRail) | 20.4% | 21.5% | 22.6% | 23.1% |
| **CPL (solo CallRail)** | $28.69 | **$32.09** | $35.44 | $27.06 |
| Conv./mes (reportadas) | 49.6 | 63.8 | 82.9 | 78.0 |
| Gasto/mes | $1,057 | $1,245 | $1,439 | $1,254 |
| Search IS | 20.7% | 23.6% | 25.6% | 20.3% |
| IS perdida por presupuesto | 42% | 48% | 53% | 53% |

Detalle por campaña (90 días):
| Sede | Gasto/mes | CPC | CTR | CPL rep. | CPL CallRail | Conv/mes rep. | IS | Perdida presup. |
|---|---|---|---|---|---|---|---|---|
| Biscayne | $1,439 | $6.41 | 6.6% | $15.97 | $23.87 | 90 | 24% | 47% |
| 103rd | $1,254 | $6.25 | 5.5% | $16.08 | $27.06 | 78 | 20% | 53% |
| Atlantic | $1,546 | $5.97 | 6.3% | $17.63 | $30.32 | 88 | 21% | 58% |
| San Jose | $1,245 | $7.72 | 6.5% | $19.50 | $34.98 | 64 | 24% | 42% |
| St. Augustine | $917 | $6.12 | 6.9% | $20.80 | $43.12 | 44 | 22% | 48% |
| St. Marys | $1,057 | $7.71 | 8.6% | $22.59 | $35.89 | 47 | 28% | 53% |
| Orange Park | $1,205 | $6.74 | 6.1% | $23.02 | $32.09 | 52 | 26% | 35% |

**CPL objetivo inicial sugerido** (base solo CallRail, mediana ±20%): **$26–38 por llamada CallRail**. No es CPL calificado. Cuando CallRail filtre primera llamada ≥ 60 s, el CPL calificado probable es de $45–65, que es contra lo que hay que comparar el CPL máximo del brief (PENDIENTE del cliente).

**Con el presupuesto actual (~$1,600/mes en Search 103rd, hoy gasta ~$1,250)**:
- Reportado: ~80 conv./mes. Supera de sobra el umbral de 30/mes para tCPA, pero es una señal inflada.
- Solo CallRail: ~46–50 llamadas/mes.
- Estimación calificada (supuesto: 50–60% de las llamadas de CallRail son leads nuevos): **~25–30/mes**. Justo en el umbral de tCPA. **Recomendación**: no poner tCPA hasta tener 30 días de conversión limpia; seguir con Max Conversions sin tCPA.
- El presupuesto alcanza para salir de aprendizaje con una sola conversión primaria.

## Lo que hacen las cuentas que mejor rinden
**No hay variación estructural para aprender**. Las 7 campañas usan **la misma plantilla**:
| Rasgo | Las 7 campañas |
|---|---|
| Ad groups | **1** ("Grupo de anuncios 1" / "Ad group 1") |
| Keywords | 28–54, mitad amplia y mitad frase |
| Gasto en concordancia amplia | **98–100%**: las keywords en frase casi no reciben impresiones |
| Keyword #1 en gasto | **"oil change near me" (amplia)** en las 7 |
| Puja | Max Conversions sin tCPA |
| Geo | Radio de 4–5 mi, Presencia |
| Red | Solo Búsqueda |

Lo que explica que Biscayne y 103rd tengan el mejor CPL (reportado y CallRail) **no es la estructura**. Son la **densidad del mercado** (Jacksonville urbano frente a St. Augustine y St. Marys) y la **mayor proporción de marca** en conversiones (103rd: 40% de las conversiones vienen de keywords "aamco"; St. Augustine: 49%, pero con menos volumen total).

Conclusión: el benchmark interno fija un **piso de rendimiento con la plantilla actual**. No es un techo. La reestructura propuesta (STAG por servicio, frase por defecto) no tiene precedente en esta cuenta, así que hay que tratarla como **prueba controlada** en 103rd antes de replicarla en las otras 6 sedes.

## Keywords que más convierten en el nicho (agregado 7 campañas, 90 días, conversiones reportadas)
| Keyword (concordancia) | Conv. | Gasto | CPA rep. | Campañas | Nota |
|---|---|---|---|---|---|
| oil change near me (amplia) | 484 | $10,182 | $21.04 | 7 | **38% del gasto total**. Funciona como comodín genérico, no por cambio de aceite |
| auto repair (amplia) | 235 | $5,024 | $21.35 | 5 | 103rd **no la tiene**; 5 sedes sí |
| aamco (amplia) | 201 | $2,178 | $10.82 | 7 | Marca |
| aamco transmission (amplia) | 153 | $1,836 | $12.04 | 6 | Marca |
| aamco near me (amplia) | 68 | $507 | $7.51 | 7 | Marca |
| mechanic near me (amplia) | 58 | $1,441 | $24.76 | 7 | |
| transmission shop near me (amplia) | 42 | $869 | $20.89 | 7 | **Mejor keyword de transmisión no-marca** |
| engine repair (amplia) | 22 | $574 | $25.68 | 5 | |
| auto shop near me (amplia) | 21 | $808 | $38.41 | 7 | CPA alto |
| car ac repair near me (amplia) | 5 | $172 | $34.36 | 7 | |
| transmission repair near me (amplia) | 2 | $52 | $25.99 | 6 | Casi sin volumen con la plantilla actual |

Lectura: con la plantilla actual, la transmisión no-marca apenas recibe tráfico en ninguna sede. "transmission shop near me" es la única keyword de transmisión con volumen, y su CPA ($20.89) es igual al de las genéricas. Si el ticket de transmisión es 5–10× el de mantenimiento, esa keyword está subinvertida en toda la cuenta.

## Negativas frecuentes del nicho
Las campañas de Jacksonville tienen 67–578 negativas (103rd: 359). Las que aparecen en 3 o más campañas:
- **Otras sedes AAMCO** (negativas cruzadas): 103rd, biscayne, san jose, atlantic, orange park, blanding, aamco dunn ave.
- **Carrocería y vidrio**: body shop, collision, dent(s), bumper, frame, autobody, maaco, gerber, auto glass, glass; y en español carrocería, hojalatería, latonería, abolladura, choque, enderezado.
- **Repuestos**: auto parts, car parts, parts, oem parts, aftermarket, autozone, advance auto, o'reilly (y 10 variantes mal escritas), napa, lkq, junkyard, deshuesadero, salvage.
- **Competidores y cadenas**: firestone, goodyear, midas, mavis, jiffy lube, grease monkey, take 5, valvoline, brakes 4 less, mr transmission, american transmission(s), mitchell transmission, jasper.
- **Concesionarios**: dealer, dealership, autonation, carmax, coggin, hanania, beaver toyota, bozard.
- **Cerrajería y llantas**: locksmith, cerrajero, key replacement, flat tire, llantera, gomero.
- **Informacional**: how, how to, diy, free.

⚠️ La negativa "**duval**" en 103rd bloquea "duval county transmission" (competidor, correcto), pero también búsquedas como "transmission repair duval county". Revisar si es intencional.
⚠️ La negativa "**aaa**" (común en varias campañas) bloquea "aaa approved auto repair", que es intención comercial. Revisar.

## Historial propio del cliente
103rd **es** parte del benchmark. Frente a sus pares:
- **Mejor que la mediana** en CPL (reportado $16.08 contra $19.50; CallRail $27.06 contra $32.09) y en volumen (78 conv./mes contra 64).
- **Peor** en CTR (5.5%, el más bajo) y en cuota de impresiones (20%, cerca del P25). El CTR bajo encaja con el RSA de fuerza "POOR" y los titulares genéricos.
- **Más limitada por presupuesto** que la mediana (53% contra 48%).
- Serie de 12 meses: el CPA reportado bajó de ~$32 (oct–dic 2025) a ~$16 (jun–ago 2026). La bajada coincide con el cambio de medición de abr-2026, no con cambios de estructura (ver evaluación).

Diagnóstico: 103rd rinde bien **dentro de una plantilla débil que comparten las 7 sedes**. Los problemas de fondo son de la cuenta, no de la sede: medición duplicada, 1 ad group, amplia en todo, "oil change near me" como comodín y marca pagada por 4 sedes. Arreglarlos en 103rd como piloto da un aprendizaje que se puede replicar en ~$8,600/mes de gasto Search.

## Advertencias
- Todas las comparables son de **una sola cuenta y una sola franquicia**. No hay otro taller de transmisión con Search en el MCC.
- Datos de **Windsor.ai**, no de la API directa (sin acceso a `google-ads.yaml` en esta sesión).
- La **tasa de conversión reportada** (29–40%) no es realista para un taller. Úsese solo en términos relativos.
- Beacon y Beachaven (PMax, "Calls from ads" únicamente) muestran CPL de $7.6–8.1. No son comparables: otra medición y otro tipo de campaña.
