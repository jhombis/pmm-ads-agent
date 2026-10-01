---
nicho: towing
pais: US
cuentas: 25
periodo: últimos 90 días (2026-07-03 → 2026-09-30)
fuente: Windsor.ai (google_ads, MCC PMM)
actualizado: 2026-10-01
---

Nivel cuenta: Search + PMax cuando existe. Conv./mes y gasto/mes están normalizados por los días activos. Las conversiones son en un ~85% "Calls from ads" (llamadas sin calificar).

| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $4.10 | $5.12 | $6.60 |
| CTR | 4.9% | 6.7% | 7.9% |
| Tasa conv. | 17.7% | 26.0% | 37.9% |
| CPL | $12.90 | $16.04 | $33.38 |
| Conv./mes | 18 | 31 | 57 |
| Presupuesto/mes (gasto real) | $426 | $698 | $939 |
| Search IS (campañas Search) | 19% | 26% | 31% |

**Solo campañas Search** (24 campañas): CPL P25 $13.63, mediana $25.98, P75 $41.51. El agregado es $19.30 en Search contra $13.43 en PMax (15 campañas).
Para cuentas nuevas que arrancan solo con Search, se usa la mediana de Search ($26 ±20%) como CPL objetivo inicial, no la de cuenta.

## Estructura que mejor funciona
Cuartil superior: 7 cuentas con CPL de $8–$13.
- Las 7 pujan con **Maximizar conversiones**. Las cuentas con Maximizar clics (TARGET_SPEND) caen todas en el cuartil inferior o tienen CPL de $65–$78 (incluye 2 cuentas recientes, de menos de 30 días).
- Una campaña Search "Radius" con 1–2 ad groups y Presencia. Con presupuestos de $10–$25/día ya se consigue un CPL bajo de $13.
- 5 de las 7 suman una campaña PMax madura (4–18 meses) con assets propios. PMax baja el CPL de la cuenta, pero incluye llamadas de Maps/GBP. Solo se lanza con Search estable (ver `knowledge/estrategias/pmax-cuando-y-como.md`).
- Search IS del 10–30% y pérdida por presupuesto del 20–80%: ninguna cuenta satura la demanda. Más presupuesto escala casi linealmente hasta donde se puede observar.
- La marca en exacta convierte a ~$7 en las cuentas que tienen demanda de marca.
- Ad group en español: útil solo en mercados hispanos (TX, CA, FL). Fuera de ellos gasta sin convertir.

## Keywords top por conversiones (agregado)
| Keyword | Gasto | Conv. |
|---|---|---|
| towing near me | $4,045 | 450 |
| tow truck near me | $262 | 55 |
| [marca] exacta | $254 | 36 |
| roadside assistance | $192 | 28 |
| towing company near me | $104 | 17 |
| rv towing | $97 | 14.5 |
| tow truck service / towing service / tow service | $97 | 24 |
| tow truck + [ciudad] | — | 2–8 c/u |
| gruas cerca de mi (mercados hispanos) | $93 | 9 |

La mayoría de las conversiones no se atribuyen a keyword: vienen de llamadas desde el activo y de PMax.

## Negativas que más gasto ahorraron
Son los términos con más gasto y 0 conversiones en 90 días, todos candidatos a negativa de nicho:
- **Nombres de competidores**: es el desperdicio más recurrente, siempre por broad. Hay que revisar los search terms cada semana.
- **Ciudades o estados fuera del área**: "towing arizona", "towing wichita falls", ciudades vecinas fuera del radio.
- **Precio extremo**: "$50 tow truck", "$40 towing", "cheapest tow".
- **Servicios que no son grúa**: "car battery change/replacement", "tire place", "tire repair", "junkyard", "car hauler trailers", "used car haulers", "auto transportation", "car delivery service", "flatbed equipment".
- **Larga distancia y vehículos especiales**: "long distance towing", "motorcycle towing" y modelos de RV, si el cliente no los atiende.
- **Asistencia de aseguradoras o del gobierno**: "state farm roadside", "caltrans", "freeway assistance", "road ranger", "aaa".
- **Informacionales**: "average tow cost", "tow service price", "tow truck backing up".
- **Otros idiomas** (p. ej. coreano) y "en español" cuando no hay ad group en español.
- **No excluir por defecto**: "ran out of gas", "need a jump", "jump start" y "lockout". Tienen 0 conversiones en cuentas que no los ofrecen, pero son servicios válidos para clientes con roadside.

## Errores comunes vistos en cuentas del P25
- **Maximizar clics como estrategia final**: las 4 cuentas con TARGET_SPEND tienen CPL de $65–$78 y una tasa de conversión del 7–13%.
- **Keywords solo en broad** sin revisión de search terms: el gasto se va a competidores, otras ciudades y servicios que no se ofrecen.
- **Ad group en español** en mercados no hispanos.
- **CPC alto ($9–$11) con poco volumen**: suele indicar mal Ad Rank (IS perdido por ranking del 40–60%) más que falta de presupuesto.
- **PMax lanzado al poco tiempo** en cuentas nuevas (2 casos): poco gasto, 1–2 conversiones, y luego pausado.
- **Medición laxa**: se cuentan "Calls from ads" sin una duración mínima clara o llamadas web de 20 s. Infla la tasa de conversión e impide comparar con un lead calificado. El estándar recomendado es una llamada de 60 s o más como conversión principal.

## Notas de método
- Las cuentas se identificaron por nombre ("towing", "tow", "roadside", "recovery") porque el MCC no tiene etiquetas `nicho:*`/`pais:*`. Hay que etiquetarlas.
- Quedan fuera las cuentas con menos de 30 días de gasto en la ventana y las de hauling/junk cars.
