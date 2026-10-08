---
cliente: Rio Roadside Assistance
slug: rio-roadside-assistance
nicho: towing / roadside assistance
pais: US
cuentas_comparables: 29 (9 con paquete ≤ $1,200; 2 con "roadside" o "lockouts" en el nombre)
periodo: 90d (jul–sep 2026, Windsor; serie mensual en knowledge/benchmarks/raw/towing-us-2026-q3-monthly.csv)
actualizado: 2026-10-07
fuente: knowledge/benchmarks/towing-us.md (consolidado de 7 extracciones) + recálculo sobre el crudo Q3. Sin extracción nueva: Windsor pide volver a autorizar y no hay credenciales de la API.
---

# Benchmark interno — Rio Roadside Assistance

No se pudo hacer una extracción nueva del MCC (Windsor desconectado, API sin credenciales). Este benchmark recalcula el crudo de jul–sep 2026 que ya estaba en `knowledge/benchmarks/raw/` (31 cuentas de towing/roadside, 29 con ≥30 clics) y toma la lectura cualitativa del consolidado `knowledge/benchmarks/towing-us.md`. Las cuentas se identifican por el nombre del paquete; el MCC sigue sin etiquetas `nicho:` / `pais:`.

## Rangos esperados para este nicho/país
Todas las cuentas de towing/roadside del MCC, 90 días (n = 29):

| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $4.31 | $5.16 | $7.13 |
| CTR | 4.7–5.1% | 6.6–7.1% | 7.8–8.4% (consolidado) |
| Tasa conv. | 16.2% | 25.0% | 37.9% |
| CPL | $12.87 | **$21.82** | $46.64 |
| Conv./mes | 13 | 24 | 51 |
| Gasto real en medios/mes | $384 | $625 | $873 |

Paquetes de $799–1,200, como el de Rio (n = 9):

| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $2.92 | $4.12 | $5.96 |
| Tasa conv. | 12.1% | 26.0% | 42.0% |
| CPL | $9.11 | **$13.45** | $46.20 |
| Conv./mes | 9 | 19 | 42 |
| Gasto real/mes | $285 | $365 | $413 |

Las dos cuentas con "roadside" o "lockouts" en el nombre:

| Cuenta | Gasto/mes | CPC | CVR | CPL | Conv./mes |
|---|---|---|---|---|---|
| A (lockouts, paquete $1,200, madura) | $469 | $3.36 | 26.0% | $12.91 | 36 |
| B (towing & roadside, paquete $1,500) | $799 | $6.83 | 16.5% | $41.32 | 19 |

Cohorte nueva (consolidado, cuentas con <60 días): CPL mediana $51–63 (P25 $35, P75 $68), CPC $7.3–7.6, CVR 14–19%. **En los primeros 60 días Rio se compara contra esta cohorte, no contra las maduras.**

**CPL objetivo inicial sugerido**: mediana de las cuentas de paquete ≤ $1,200 ±20% → **$11–16 a los 6 meses**; en meses 1–2, **$30–60** es lo normal.
**Con presupuesto de $608/mes ($20/día)**: $608 ÷ CPC $4.37 actual ≈ 139 clics/mes → con la CVR de la cohorte nueva (14–19%) ≈ 19–26 conversiones/mes; con la CVR mediana madura (25%) ≈ 35. Eso cruza el umbral de 15+ conversiones/mes de Maximizar conversiones en el mes 1–2 **si la medición registra las llamadas**; tCPA (~30 en 30 días) sería alcanzable hacia el mes 2–3. Hoy la cuenta reporta 0 conversiones en 24 clics, así que ninguna de las dos pujas se puede activar hasta que Tag Assistant confirme la medición. Rio gasta el 51% del paquete, por encima del 33–45% típico en paquetes de $799–1,200: no está limitada por dinero sino por relevancia (IS 12%, 58% perdido por ranking).

## Lo que hacen las cuentas que mejor rinden (cuartil superior, CPL $8–13)
- **1 campaña Search de radio con 1 ad group consolidado y 5–16 keywords**; dos o tres términos hacen el 80% del volumen. Nadie usa SKAG. Para Rio, con $608/mes, el límite de fragmentación del playbook da 1 campaña y 3–5 grupos: roadside genérico · flat tire · jump start · lockout/fuel.
- **Puja: Maximizar conversiones** en todas las top; las 3 cuentas que sostienen Maximizar clics tienen CPL de $70–83. Rio está en Maximizar clics sin tope: punto de partida, no destino.
- **Match**: el MCC está casi todo en amplia y amplia no rinde mejor, solo gasta más: el 23% del gasto de Search del nicho se fue en términos con 0 conversiones. Frase por defecto (estándar PMM #2) para controlar ese desperdicio, que en Rio ya es el 69% del rastreable.
- **Keywords de ciudad** ("towing / roadside + ciudad"): CPL ≈ $8. Para Rio: Boston, Cambridge, Somerville, Medford, Malden, Everett.
- **Ad group en español** solo en mercados hispanos (TX, CA, FL). El norte de Boston tiene demanda en portugués y español en los search terms (`gruas cerca de mi`, `borracheiro near me`); se prueba solo si el cliente atiende en ese idioma.
- **PMax** en 4–5 de las 8 mejores, siempre tras 6–12 meses de Search estable; las 2 que lo lanzaron antes de 3 meses lo pausaron.
- En las cuentas del P75 la pérdida de IS por ranking es del 9–30%; Rio pierde 58%: problema de relevancia/QS, no de presupuesto.

## Keywords que más convierten en el nicho (agregado de 27 cuentas, 90 días)
| Keyword | Conv. | CPL | CVR |
|---|---|---|---|
| towing near me | 775–790 | $11–18 | 37% |
| tow truck near me | 155–173 | $9–18 | 42% |
| español (grúa cerca de mí, asistencia en carretera) | ~110 | $10–24 | 20–31% |
| marca propia (exacta) | 95–107 | $8.5–14 | 37–62% |
| towing + ciudad | ~90 | ~$8 | 52% |
| roadside assistance (+ near me) | 75–76 | $11–29 | 23% |
| cheap towing / cheap tow truck near me | 25–36 | $8–18.5 | 34% |

**"roadside assistance" como keyword principal es riesgoso**: en el agregado convierte a $11–29, pero en las cuentas donde concentra el gasto en amplia sale a $67–154 porque compite con AAA y las aseguradoras. Rio tiene exactamente ese patrón: 61% del gasto en `roadside assistance` amplia, con clics de Plymouth Rock y "roadside assistance number". Usarla en frase con negativas de aseguradoras, y mover el peso a términos de servicio (flat tire, jump start, lockout) y de ciudad.

## Negativas frecuentes del nicho (aplican a Rio desde el día 1)
- Aseguradoras, motor clubs y planes de fabricante: aaa, geico, allstate, progressive, state farm, usaa, plymouth rock, liberty, vw/volkswagen, benz/mercedes, turo, carshield ($32 CPL / 18% CVR en el agregado; en Rio ya gastó $10.33 sin conversión).
- "phone number" / "número de teléfono": $43 CPL, 13% CVR.
- Batería y jump start como **producto**: jumper, jump starter, jump box, battery charger, battery pack (en Rio: 9 impresiones).
- Tiendas y compra de llantas: tire shop, tire store, used tire, mavis, town fair, sullivan, discount tire, medidas (235 60 r17, 245 75r16, 33 12.50 r20), walmart, autozone, bj's (en Rio: $17.95, el mayor desperdicio).
- Talleres: mechanic, auto repair, jiffy lube, pep boys, firestone, alternator, abs, brake light.
- Informacionales y DIY: how to, what to do, why, average, cost (ojo: "cost / how much" convierte a $21.67 en el agregado; negativizar solo "average tow truck charge" y similares).
- **No negativizar** si Rio ofrece el servicio: flat tire, tire change, jump start, lockout, ran out of gas, fuel. Tampoco cheap / affordable (CVR 34.5%, CPL $16.59).

## Historial propio del cliente
Cuenta 185-043-8400, 12 días (25-sep → 7-oct 2026): $104.81, 24 clics, CPC $4.37, CTR 5.2%, 0 conversiones, IS 12.3% (58% perdido por ranking, 20% por presupuesto). Contra el benchmark:
- CPC $4.37 vs $7.3–7.6 de la cohorte nueva: está comprando lo barato y genérico (Maximizar clics sin tope en amplia), no es una ventaja.
- 0 conversiones vs 14–19% de CVR esperada (3–4 conversiones en 24 clics): la medición es sospechosa antes que el tráfico. Hasta no verificarla con Tag Assistant, el CPL no existe.
- Patrón de error del P25 que ya cumple: "roadside assistance" amplia concentrando el gasto, Maximizar clics, cuenta nueva sin limpiar search terms, IS perdido por ranking > 40%.

## Advertencias
- Sin extracción nueva: los datos son los de jul–sep 2026 ya guardados; `knowledge/benchmarks/towing-us.md` no se modifica porque no hay cuentas ni periodo nuevos.
- No hay ninguna cuenta del MCC en Massachusetts ni en una metro del noreste; las metros caras del consolidado (Phoenix, LA, Bay Area, Tampa) dan CPC $6.5–10.9 y CPL $30–66, y Boston debería parecerse más a eso que a los pueblos (CPL $12.84).
- Solo 2 cuentas tienen "roadside" en el nombre y una es de lockouts; el resto es towing puro, con ticket más alto. El CPL de roadside (ticket de $50–150 por servicio) tiene que ser más bajo que el de towing para ser rentable; de ahí que el ticket y la tasa de cierre del cliente sigan siendo el pendiente que manda.
- Tasas de conversión sobre <50 clics (Rio hoy) son ruido; `budget_amount` es el vigente, no el histórico.
