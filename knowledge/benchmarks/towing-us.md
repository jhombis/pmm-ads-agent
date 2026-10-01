---
nicho: towing
pais: US
cuentas: 21–31 por extracción (19–23 maduras)
periodo: últimos 90 días, extracciones del 2026-09-23 al 2026-10-01 (jun–oct 2026) + 12 meses de control
actualizado: 2026-10-01
fuente: Windsor.ai (google_ads). Consolidado de 7 extracciones hechas para 290 Tow, Precision Towing, Jerry's Towing, Spillane's, RR Roadside, JQ Towing y Jump Towing. Crudos en raw/. Cuentas identificadas por nombre (towing, tow, roadside, recovery) porque el MCC aún no tiene etiquetas nicho:/pais:
---
# Benchmark towing US — MCC PMM (consolidado)

Siete sesiones sacaron este benchmark por separado sobre casi las mismas cuentas, y los números coinciden. Por eso cada métrica se da como **rango entre extracciones** en lugar de recalcular percentiles. Qué columna usar para un cliente nuevo:
- **CPL objetivo inicial de una cuenta nueva solo Search**: la mediana de *Solo Search* ($26–32) ±20% → **$21–38**.
- **Mes 1**: espera la cohorte nueva (~$51–63).
- **Meta a 6 meses**: la mediana de las cuentas maduras ($15–16).

**Qué es "conversión" aquí**: el 70–100% son llamadas ("Calls from Ads" ≈ 86% del total, llamadas desde la web ≈ 9,5%, formularios ≈ 4,6%). El CPL es **costo por llamada**, no por lead calificado.

## Cuentas maduras (n = 20–23; ≥15–30 conv. en 90 días)
| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC (cuenta) | $3,78–4,08 | $4,84–5,05 | $5,94–6,33 |
| CTR | 4,7–5,1% | 6,6–7,1% | 7,8–8,4% |
| Tasa conv. | 21–24% | 27–28% | 38–40% |
| CPL | $11,52–12,45 | **$14,59–16,01** | $23,41–32,07 |
| Conv./mes | 17–23 | 35–43 | 54–70 |
| Gasto real en medios/mes | $357–420 | $680–728 | $918–1.094 |
| Impression share (Search) | 19–22% | 26–27% | 31–32% |

CPL en el P25 = el mejor cuartil (el más bajo).

**Solo Search** (24–30 cuentas): CPC $5,14–7,02 en la mediana · CVR 19,5% / 26% / 38,5% · **CPL $13,45–14,14 / $25,98–31,91 / $41,51–55,24**. El agregado da Search $19,23–19,30 contra PMax $13,22–13,43.

**Solo PMax** (13 cuentas): CPL $8,92 / $15,35 / $18,19. Incluye las llamadas de Maps/GBP.

**Impression share de Search**: mediana del 26%, con ~30% perdido por presupuesto y ~35% por ranking. Ninguna cuenta satura la demanda: en lo observado, más presupuesto escala casi linealmente.

**12 meses** (21 cuentas): CPC $4,03 / $4,44 / $5,49 · CVR 21% / 29% / 35% · CPL $10,43 / $15,13 / $28,63.

## Todas las cuentas, incluidas las nuevas (n = 27–30)
| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $4,23–4,51 | $5,12–5,41 | $6,78–7,28 |
| CPL | $12,67–13,15 | $17,88–25,15 | $42,48–47,66 |
| Conv./mes | 5,8–6,9 | 21,7–27,3 | 47,2–50,0 |

## Cohorte nueva (expectativa para un lanzamiento)
| Cohorte | CPL | CPC | CVR |
|---|---|---|---|
| Meses 1–2 (<60 días) | mediana ≈ $51–63 (P25 $35, P75 $68; rango $31–81) | $7,3–7,6 | 14–19% |
| Search con ≥6 meses | mediana $14,57 (P25 $12,80, P75 $27,87) | $5,96 | 36,7% |

Una cuenta nueva arranca con un CPL 3–4 veces el de una madura. La brecha está en la tasa de conversión, no en el CPC. Lo esperable:
- meses 1–2: $30–60
- meses 3–6: converge a $15–28

En los primeros 60 días, compara contra esta cohorte y no contra la madura.

## Presupuesto: monto del paquete vs gasto real
El "$X/mo" del nombre de la cuenta es el precio del paquete (incluye el fee). Lo que se gasta realmente en medios es una fracción de ese monto:

| Paquete | % del monto que va a medios | Gasto real/mes |
|---|---|---|
| Todos | 39–44% (mediana; rango 23–70%) | — |
| $799–1.200 | 33–45% | mediana $375 |
| $1.500 | ~50% | — |
| ENHPRM $1.399–1.800 | — | $675–790 |

## Por tipo de mercado (Search, 90 días)
| Mercado | CPC | CVR | CPL |
|---|---|---|---|
| Pueblos y ciudades pequeñas (PA, NC, VA, norte de CA, GA) | $4,48 | 34,9% | $12,84 |
| Paquete de $799–1.500 (12 cuentas) | $5,51 | 29,4% | $18,74 |
| Metro bilingüe de Texas (1 cuenta) | $3,32 | 26,8% | $12,38 |
| Metros caras (Phoenix, LA, Bay Area, Tampa, Colorado Springs) | $6,5–10,9 | 14–26% | $30–66 |
| Florida (3 cuentas, agregado) | $6,51 | 17% | $37,8 |

En Tampa/FL, el CPC de "near me" en Search ronda los $10. El promedio de la cuenta sale más bajo porque lo baja PMax.

## Estructura que mejor funciona (cuartil superior, CPL $8–13)
- **1 campaña Search de radio** ("ENHPRM Radius") con **1 ad group consolidado y 5–16 keywords**. Dos o tres términos hacen el 80% del volumen. Ninguna cuenta top usa SKAG.
- En mercados hispanos (TX, CA, FL), un ad group separado en español. Fuera de ellos gasta sin convertir.
- Con $10–25/día ya se logra un CPL de $13, siempre que la cuenta sea madura y use Maximizar conversiones.
- **Puja: Maximizar conversiones** en todas las cuentas top, sin tCPA en la mayoría (4 cuentas con tCPA de $12–15, todas en la mitad buena).
  - Maximizar clics: las 3 cuentas que lo usan tienen un CPL de $70–83.
  - Puja por impression share: CPL de $27,68.
- **Match type**: el MCC está casi todo en amplia, pero amplia no rinde mejor; solo gasta más.

  | Match | Cuentas | CPL | CVR |
  |---|---|---|---|
  | Amplia | 26 | $19,43 | 32,5% |
  | Frase | 7 | $17,36 | 32,1% |
  | Exacta | 2 | $18,36 | 40,8% |

  Otra extracción (31 cuentas) dio exacta $18,0 · amplia $21,2 · frase $24,9. **Las diferencias de CPL entre match types son chicas y cambian de signo según la extracción.** Lo que sí es consistente es el desperdicio en amplia: el 23% del gasto de Search del nicho ($5.166) se fue en términos con 0 conversiones, sobre todo competidores, otras ciudades y servicios no ofrecidos.

  La razón para usar **frase por defecto** en cuentas nuevas (estándar PMM n.º 2) es controlar ese desperdicio, no esperar un CPL más bajo. La marca propia en exacta convierte a ~$7–14.
- **Keywords de ciudad** ("tow truck / towing + ciudad + estado"): CPL ≈ $8.
- **PMax**: está en 4–5 de las 7–8 mejores cuentas, siempre después de 6–12 meses de Search estable.
  - Reporta un CPL de $6–14, pero incluye acciones de Maps y la calidad de esas conversiones no está validada.
  - Las 2 cuentas que lo lanzaron antes de los 3 meses fracasaron y lo pausaron.
- En las cuentas del P75, la pérdida de IS por ranking es de solo el 9–30%. Suelen estar limitadas por presupuesto con un CPL bajo, así que ahí lo que toca es escalar.
- Windsor no muestra geo (presencia vs interés), programación ni extensiones; verificar por API.

## Keywords top por conversiones (agregado de 27 cuentas, 90 días)
| Keyword | Conv. | CPL | CVR | Cuentas |
|---|---|---|---|---|
| towing near me | 775–790 | $11–17,66 | 36,7% | 17 |
| tow truck near me | 155–173 | $9–18 | 42,3% | 20 |
| Español (grúa(s) cerca de mí, servicio de grúa, asistencia en carretera, auxilio vial) | ~110 | ~$10,5–24 | 20–31% | 3+ |
| marca propia (exacta) | 95–107 | $8,5–14 | 37–62% | 3 |
| tow truck / towing + ciudad | ~90 | ~$8 | 52% | varias |
| roadside assistance (+ near me) | 75–76 | $11–28,60 | 22,8% | 9 |
| cheap towing / cheap tow truck near me | 25–36 | $8–18,5 | 34% | 8 |
| towing company near me | 25–40 | $13–16,5 | 42% | 7 |
| towing service | 23,5 | $34,58 | 21% | 9 |
| tow truck service / tow service | 13–19 | $4,6–11,3 | 38–70% | 2 |

**"roadside assistance" como keyword principal es riesgoso.** En el agregado convierte ($11–29), pero en las cuentas donde concentra el gasto en amplia sale a $67–154, porque compite con AAA, CAA y las aseguradoras. Úsalo en frase y con negativas de aseguradoras, o no lo uses.

**Search terms top** (26 cuentas):

| Término | Conv. | CPL |
|---|---|---|
| tow truck near me | 163,5 | $16,51 |
| towing near me | 65 | $17,71 |
| towing company near me | 40 | $16,48 |
| tow company near me | 28,5 | $16,01 |
| cheap towing near me | 26 | $13,66 |
| roadside assistance near me | 15 | $21,75 |

## Términos que NO hay que negativizar
- **cheap / cheapest / affordable**: CVR 34,5%, CPL $16,59 en 26 cuentas.
  - *Contradicción resuelta*: la extracción de 290 Tow lo listaba como negativa por términos sueltos con más de $15 y 0 conversiones. En el agregado convierte igual que el genérico.
  - Lo que sí se negativiza son los precios irreales ("$40 towing", "$50 tow").
- **price / cost / how much**: CPL $21,67, CVR 26%.
- **trailer** a secas, si el cliente remolca trailers. Lo mismo con **flat tire** o **tire change**, si hace roadside. Las negativas amplias de una palabra que bloquean servicios del cliente son un error del P25.

## Negativas que más gasto ahorran (por tema)
Windsor no expone las listas de negativas. Esto sale de términos con gasto y 0 conversiones (728 términos, $5.166). El desperdicio está atomizado (el término más caro gastó $54), así que conviene negativizar por tema:

| Tema | Ejemplos | Gasto | CPL / CVR | Sin conv. | Cuándo aplicar |
|---|---|---|---|---|---|
| Aseguradoras, motor clubs y planes de fabricante | aaa, geico, allstate, progressive, state farm, usaa, carvana, toyotacare, mopar, onstar, lincoln, bridgestone, carshield, bristol west, root, caa, road ranger, freeway assistance | $257 | $32 / 18% | $199 | siempre |
| "phone number" / "número de teléfono" | — | $347 | $43 / 13% | $250 | siempre |
| Batería y jump start como **producto** | car jumper, jump starter, jump box, battery pack, battery change/replacement | $406 | $45 / 14% | $336 | siempre |
| Gasolina, jump o lockout como **servicio** | ran out of gas, emergency gas, need a jump, jump start, lockout | $119 (gasolina) | $60 | $95 | **solo si el cliente no ofrece roadside**; si lo ofrece, son servicios válidos |
| Tiendas de llantas | tire shop, tire place, discount tire, big o tires | — | tema llantas $520, $27 | — | mantener "flat tire" si hay roadside |
| Compra o alquiler de trailers y RV | for sale, rental, hitch, dolly, hauler, toy hauler, cargo trailer, moving | $80 | $80 | — | siempre |
| Long distance towing | — | $46 | 1 conv. | — | salvo cobertura interestatal |
| Motorcycle towing | — | $68 | $23 | — | salvo que tenga el equipo |
| Junk, cash for cars, salvage, scrap, we buy | — | $51 | — | — | siempre |
| Impound, repo, "car was towed", tow yard / lot | find my towed car, police | — | — | — | siempre |
| Renta, equipo y transporte | u haul, penske, ryder, hertz, enterprise, jerr dan, copart, parts, car hauler, auto transportation, car delivery service, flatbed equipment | — | — | — | siempre |
| Talleres | mechanic, car repair, shop, pep boys, firestone | — | — | — | siempre |
| Marcas de auto y dealer | ford, chevy, toyota, honda, tesla, dealer, carmax | — | — | — | siempre (plantilla) |
| Ciudades o estados fuera del área | "towing arizona", ciudades vecinas fuera del radio | — | — | — | por cuenta |
| Empleo y DIY | — | — | — | — | siempre (lista universal) |
| Informacionales | "why won't my car start", "average tow cost", "tow truck backing up" | — | — | — | siempre |

- **Competidores locales por nombre**: es el desperdicio recurrente más grande y aparece en todas las cuentas con amplia. La lista se arma por cuenta.
- **Idiomas sin anuncio** (coreano; español si no hay ad group ES), en mercados metro.
- **Plantilla base del MCC**: ~190 términos a nivel campaña (presente en 28 de 31 cuentas); la versión ENHPRM tiene ~450 en amplia. Con esa lista aplicada, el desperdicio residual viene sobre todo de competidores locales, ciudades fuera del área y "grua" suelto.

## Errores comunes en las cuentas del P25
- **Maximizar clics o puja por IS** como estrategia sostenida: CPL de $70–83.
- **Cuentas de menos de 3 meses sin limpiar search terms**: CVR del 7–19%, contra 37% en las maduras.
- **"roadside assistance" amplia concentrando el gasto**, o genéricos de roadside ("emergency roadside", "car battery help"): CPL de $29–154.
- **PMax lanzado a las 2–3 semanas** de vida de la cuenta.
- **Metro cara con presupuesto de paquete bajo**: CPC de $7–11+, CPL de $38–66, menos de 10 llamadas al mes y la cuenta no sale de aprendizaje. Si el CPC supera $9 en los primeros meses, agregar keywords de ciudad.
- **IS perdido por ranking mayor al 40%**: la landing o el Quality Score son débiles.
- **Display prendido en Search**: miles de clics basura.
- **1 ad group en amplia con 50–100 keywords** sin historial de conversiones.
- **Ad group en español fuera de mercados hispanos.**
- **Geo filtrando fuera del país**: gasto en México o Canadá en cuentas de US. Usar "Presencia".
- **Marca propia mezclada con genéricos** en el mismo ad group: infla la CVR aparente y esconde el CPL real de los genéricos. Pujar por competidores sin control es otro gasto con 0 conversiones.
- **Fuga geográfica**: búsquedas de ciudades a más de 100 millas. Revisar "Presencia" y amplia.
- **Conteo de conversiones inflado**: con más conversiones que clics, o una CVR de Search ≥ 40–50%, probablemente se cuentan como primarias las llamadas repetidas o cortas, o los clics en el teléfono. Antes de usar el CPL para decidir:
  - verificar que el umbral de duración sea de 60–90 s; hay cuentas con llamadas web de 20 s
  - verificar qué acciones son primarias; algunas cuentas tienen llamada y formulario como primarias a la vez

  La CVR baja (<10%) apunta a lo contrario: tracking de llamadas roto o tráfico de ticket bajo (lockout, llantas).

## Cómo se actualiza
Cuando `/benchmark-interno` vuelva a correr para towing US, **actualiza este archivo**; no crees `towing.md` ni otra variante. Agrega la extracción nueva a los rangos (o reemplaza las de más de 90 días) y guarda el crudo en `raw/towing-us-<fecha>.*`.
