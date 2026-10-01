---
cliente: Jump Towing LLC
slug: jump-towing
nicho: towing
pais: US
cuentas_comparables: 25
periodo: 90d
actualizado: 2026-10-01
---

# Benchmark interno — Jump Towing LLC

Fuente: Windsor.ai (`google_ads`, MCC PMM), 2026-07-03 → 2026-09-30. Esta sesión no tiene credenciales de la Google Ads API.
Muestra: 25 cuentas de towing/roadside en US con 30 días o más de gasto en la ventana. Quedan fuera las cuentas con menos de 30 días (5 cuentas), las de nicho no-towing (hauling, junk cars) y la propia cuenta de Jump. Las cuentas van anonimizadas como A–Y, ordenadas de menor a mayor CPL.

## Rangos esperados para este nicho/país

Nivel cuenta (Search + PMax cuando existe). Conv./mes y gasto/mes están normalizados por los días activos de cada cuenta.

| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $4.10 | $5.12 | $6.60 |
| CTR | 4.9% | 6.7% | 7.9% |
| Tasa conv. | 17.7% | 26.0% | 37.9% |
| CPL | $12.90 | $16.04 | $33.38 |
| Conv./mes | 18 | 31 | 57 |
| Gasto real/mes | $426 | $698 | $939 |
| Search IS (campañas Search) | 19% | 26% | 31% |

Jump va a arrancar solo con Search, así que también miré el nivel campaña. **Las campañas Search del nicho** (24 campañas) tienen un CPL de **P25 $13.63 / mediana $25.98 / P75 $41.51**. El CPL agregado es $19.30 en Search contra $13.43 en PMax.

**CPL objetivo inicial sugerido**:
- Con la mediana de cuenta ($16.04 ±20%) sale **$12.83–$19.25**. Ese rango sirve solo como referencia de una cuenta madura con PMax.
- **Para Jump en la Fase 1 (solo Search) uso $21–$31**, que es la mediana de Search ($25.98) ±20%. Es el número que debería ir a `strategy.md`.

**Con un presupuesto de $825/mes** (está por encima de la mediana de gasto real del nicho, que es $698):
- A CPL de Search mediano ($26): **unas 32 conversiones al mes**.
- A P75 ($41.5): unas 20 al mes.
- A P25 ($13.6): unas 60 al mes.
- Al CPL real que ha tenido la cuenta actual de Jump ($65.6, ver abajo): unas 13 al mes.

**¿Se llega a tCPA (~30 conv/30 días)?** Solo en el escenario de la mediana o mejor, y apenas. Para Jump **no conviene planificarlo antes de 60–90 días**, por cuatro razones:
1. El horario no es 24/7: sin noches ni domingos se pierde una parte grande de la demanda de towing.
2. El área es de solo 10 mi.
3. Las "conversiones" del benchmark son llamadas sin calificar (ver Advertencias). Si medimos llamadas de 60 s o más, el volumen baja.
4. La cuenta actual de Jump va en unas 13 al mes.

Recomendación: Maximizar conversiones sin tCPA, y revisar el día 60 si hay 30 o más conversiones calificadas en 30 días.

## Lo que hacen las cuentas que mejor rinden (cuartil superior: A–G, CPL $8–$13)
- **Puja**: las 7 usan **Maximizar conversiones**. Ninguna cuenta del cuartil superior usa Maximizar clics (TARGET_SPEND). Las dos cuentas con Maximizar clics que entran en la muestra están en el cuartil inferior (X: CPL $69, Y: CPL $70). Otras dos cuentas recientes con Maximizar clics (290 Tow y la de Jump) tienen menos de 30 días y no entran en el cálculo.
- **Estructura**: casi todas tienen una sola campaña Search por cuenta, llamada "Radius", con 1–2 ad groups. Además, 5 de las 7 tienen una campaña PMax madura, de entre 4 y 18 meses. C y F, con solo Search y presupuesto de $10–$23/día, tienen CPL de $9.7 y $12. Con eso se ve que se puede conseguir un buen CPL sin PMax.
- **Geo**: Presencia en todas las campañas Search del cuartil superior. Las únicas campañas con "Presencia o interés" son de cuentas con un componente heavy-duty o PMax.
- **Match types**: broad domina en el MCC. "towing near me" en broad concentra la mayoría de las conversiones atribuidas a keyword. Hay poca phrase o exacta, salvo la marca en exacta (cuenta E). **No se copia esto**: el estándar PMM es phrase. Las cuentas con broad también son las que más gasto se llevan en términos de competidores y de otras ciudades (ver negativas).
- **Presupuesto e IS**: el cuartil superior gasta entre $300 y $1,500 al mes, con un Search IS del 10–30% y pérdidas por presupuesto de entre el 23% y el 80%. Ninguna cuenta del nicho satura la demanda. Con $825 al mes, Jump va a estar limitado por presupuesto, y eso es normal en el nicho.
- **Ad group en español**: varias cuentas lo tienen. Funciona en mercados hispanos (TX, CA, FL). En las cuentas no hispanas aparece "gruas cerca de mi" con $92 gastados y 0 conversiones.

## Keywords que más convierten en el nicho (agregado, conv. atribuidas a keyword)
| Keyword | Gasto | Conv. | CPL aprox. |
|---|---|---|---|
| towing near me | $4,045 | 450 | $9 |
| tow truck near me | $262 | 55 | $5 |
| roadside assistance | $192 | 28 | $7 |
| towing company near me | $104 | 17 | $6 |
| [marca del cliente] (exacta) | $254 | 36 | $7 |
| rv towing | $97 | 14.5 | $7 |
| tow truck service / towing service / tow service | $97 | 24 | $4 |
| tow truck + [ciudad] | variable | 2–8 c/u | — |
| gruas cerca de mi (solo mercados hispanos) | $93 | 9 | $10 |

Las keywords suman solo una parte de las conversiones de cuenta. El resto son llamadas desde el activo de llamada y PMax, que no se atribuyen a keyword.

Para Jump, la base en phrase sería: "towing near me", "tow truck near me", "towing company", "towing service", "tow truck [ciudad]" con Brooklyn Park, Maple Grove, Plymouth, Minneapolis…, "roadside assistance", "jump start", "car lockout" y la marca en exacta.

## Negativas frecuentes del nicho (términos con gasto y 0 conv. en 90d)
- **Competidores por nombre** (es el mayor desperdicio recurrente): "northside towing", "jb towing", "b&b towing", "kwik tow", "a&m towing", "ballor towing", "al towing", "r&r towing phone number", "chinos towing", "joe's towing", "toolbox towing", "crow tow".
- **Fuera del área** (broad + radio): nombres de otras ciudades y estados ("towing arizona", "towing wichita falls", "des moines", "sioux falls", "i29 towing"). En MN hay que excluir explícitamente "st paul" si queda fuera del radio, más otras ciudades grandes.
- **Precio extremo**: "$50 tow truck", "cheapest $40 towing", "cheapest tow". "cheap tow" tiene resultados mixtos: no se excluye entero, solo la variante con "$".
- **Servicios que no son grúa**: "car battery change/replacement", "tire place", "tire repair", "roadside tire service", "junkyard", "car hauler trailers", "used car haulers", "flatbed equipment", "car delivery service", "auto transportation".
- **Larga distancia y vehículos no atendidos**: "long distance towing", "motorcycle towing", "rv", modelos de RV, y para Jump también "heavy duty", "semi", "18 wheeler", "box truck", "bus".
- **Asistencia de aseguradoras o del gobierno**: "statefarm roadside", "caltrans", "freeway assistance", "road ranger", "aaa".
- **Informacionales**: "average tow cost", "tow service price", "tow truck backing up".
- **Idioma**: términos en coreano y otros idiomas, y "en español" cuando no hay ad group en español.
- **Ojo**: "emergency gas for car", "ran out of gas", "i need a jump" y "car battery jump service" tuvieron 0 conversiones en otras cuentas, pero **sí son servicios de Jump** (pendiente confirmar la lista de roadside). No se excluyen; van a un ad group de roadside con su propio copy.

## Historial propio del cliente
**Encontrado en el MCC**: la cuenta 220-410-9619, "Premium Local Listings 004042 ($1500 Jump Towing LLC)". **No es una cuenta antigua: está activa ahora mismo.**

| | Jump (2026-09-14 → 09-30, ~17 días) | Benchmark Search mediana |
|---|---|---|
| Gasto | $458.97 | — |
| Clics / Impr. | 70 / 1,036 | — |
| CPC | $6.56 | $5.12 (cuenta) |
| CTR | 6.8% | 6.7% |
| Tasa conv. | 10.0% | 26% |
| CPL | **$65.57** | $25.98 |
| Conv. | 7 (~13/mes) | ~32/mes con $825 |
| Search IS | 17% (52% perdido por presupuesto, 31% por ranking) | 26% |

**Configuración actual**:
- Una campaña Search: "Jump Towing LLC - ENHPRM Radius - $2500/mo. - 08/11/2026". El nombre dice $2,500 y la cuenta dice $1,500, pero el presupuesto real es **$27/día**, coherente con el brief.
- Estado ENABLED, Presencia, puja **Maximizar clics (TARGET_SPEND)**.
- Ad groups: "Ad group 1 - English" y "Ad group 2 - Spanish". **Todas las keywords están en broad.**
- No hay datos en los 24 meses anteriores a sep-2026 bajo este ID. La cuenta que tuvo el cliente antes de PMM **no está en el MCC** y sigue PENDIENTE: hace falta su ID.

**Diagnóstico**:
- En 17 días su CPL es unas 2.5 veces la mediana de Search del nicho. Coincide con el patrón de las demás cuentas con Maximizar clics + broad del MCC (X e Y, con CPL de $69–$70).
- Search terms con desperdicio:
  - Competidores: "crow tow des moines iowa", "joe's towing", "toolbox towing", "xpress auto transportation".
  - Fuera de MN: "cheapest towing sioux falls", "i29 towing". Esto sugiere que el radio o la geo no están en las 10 mi del brief y hay que verificarlo.
  - Informacionales: "average tow cost for 50 miles", "tow truck backing up".
  - Otros servicios: "car hauler trailers", "used car haulers", "private car delivery service", "statefarm com roadside assistance".
- El ad group en español no tiene sentido en Brooklyn Park, donde la población hispana es baja y el brief indica idioma EN. Gastó unos $55 en 17 días con 1 conversión.
- **Conflicto con el brief y el estándar #7**: la cuenta está gastando mientras el brief marca como bloqueantes el tracking de llamadas, el teléfono y la auditoría de la landing. Jhombis tiene que decidir si **la pausa** hasta cerrar la Fase 0 o si la corrige en caliente: pasar a Maximizar conversiones, phrase, quitar el ad group en español, aplicar negativas y verificar la geo.

## Advertencias
- **Datos de Windsor.ai, no de la API.** No hay etiquetas `nicho:*`/`pais:*` en el MCC. Las cuentas se identificaron por nombre ("towing", "tow", "roadside", "recovery"); conviene etiquetarlas. Asumo que todas son de US (no hay campo de país; los nombres de ciudad son de US).
- **Las "conversiones" son llamadas sin calificar.** Cerca del 85% son "Calls from ads" del activo de llamada, con duración mínima desconocida. Algunas cuentas cuentan "Website Calls (20')", es decir, llamadas de 20 s. Por eso la tasa de conversión (26%) y el CPL ($16) del benchmark son optimistas frente a un **lead calificado**. Para Jump, la conversión principal debería ser una llamada de 60 s o más, y entonces hay que esperar un CPL mayor que el del benchmark.
- 5 de las 25 cuentas tienen entre 31 y 45 días activos en la ventana (normalizadas a 30 días).
- El CPL de PMax es más bajo, pero incluye llamadas de Maps/GBP. No es comparable con Search puro, y además PMax no se lanza al inicio (estándar #9).
- La tasa de conversión a nivel keyword a veces supera el 100%: las llamadas desde el activo se atribuyen sin clic. Las métricas de keyword se usan solo para ordenar, no como CPL real.
- Falta el campo de programación horaria y el de extensiones en esta extracción. No se pudo comparar 24/7 contra horario comercial.

**Siguiente**: `/strategy`. Antes, Jhombis tiene que decidir qué se hace con la campaña activa de Jump (220-410-9619).
