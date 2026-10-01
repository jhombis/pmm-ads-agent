---
cliente: Pro Phase Electric
slug: pro-phase-electric
nicho: electricista
pais: US
cuentas_comparables: 4
periodo: 90d (2026-06-24 → 2026-09-21)
actualizado: 2026-09-22
---

# Benchmark interno — Pro Phase Electric

Fuente: Windsor.ai (`google_ads`), sin la API. No hay etiquetas `nicho:*` en el MCC; las cuentas se filtraron por nombre ("Electric"). Solo campañas Search. CPC de mercado de Semrush (`us`, sept-2026).

| Cuenta | Mercado | Puja | Gasto 90d | Clics | CPC | CTR | Tasa conv. | Conv. | CPL | Conv./mes |
|---|---|---|---|---|---|---|---|---|---|---|
| A | Grand Junction, CO (mercado chico) | Max. conversiones, tCPA $20 | $971.69 | 187 | $5.20 | 5.3% | 28.7% | 53.6 | **$18.11** | 17.9 |
| B | Rocky Mount, NC (mercado chico) | Max. conversiones | $461.08 | 128 | $3.60 | 6.4% | 30.5% | 39.0 | **$11.82** | 13.0 |
| C | Irvine, CA (mercado caro) | Max. clics | $580.76 | 108 | $5.38 | 3.2% | 2.8% | 3 | $193.59 | 1.0 |
| D | San Diego North County, CA (caro; desde 20-jul) | Max. clics | $2,754.52 | 323 | $8.53 | 4.1% | 1.9% | 6 | $459.09 | 2.8 |
| **Pro Phase** | NWA, AR (desde 01-sep, gasto desde 11-sep) | Max. clics | $442.75 | 35 | **$12.65** | 3.4% | 2.9% | 1 | **$442.75** | — |

## Rangos esperados para este nicho/país
| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $4.80 | $5.29 | $6.17 |
| CTR | 3.9% | 4.7% | 5.6% |
| Tasa conv. | 2.5% | 15.7% | 29.1% |
| CPL | $16.54 | $105.85 | $260.47 |
| Conv./mes | 2.4 | 7.9 | 14.2 |

**Los datos son bimodales y la mediana no sirve como objetivo.** Hay dos grupos sin nada en medio:
- **Max. conversiones** (A, B): tasa de conversión ~30%, CPL $12–18 (sin marca: A ≈ $20, B ≈ $14).
- **Max. clics** (C, D y Pro Phase): tasa de conversión ~2–3%, CPL $190–460.

Por eso no aplico la regla "mediana ±20%" ($85–127). La propuesta sale del grupo que funciona, ajustado al CPC de NWA:

- CPC en NWA: Semrush da pujas de parte superior de $14–28 para "electrician + ciudad" (Fayetteville $28.27, Rogers $22.24, Springdale $17.68, Bentonville $13.61). El CPC real en el MCC suele quedar entre 40% y 60% de ese número, así que estimo **$8–12**. Es mercado más caro que A y B, y parecido a D.
- **CPL objetivo inicial sugerido: $40–60** por llamada. Supone CPC ~$10 y tasa de conversión de 17–25%, que es menos que A y B porque en NWA el CPC es más alto y parte del volumen será genérico. Hay que validarlo contra el CPL máximo cuando tengamos ticket y margen.
- **Con $825/mes** esperamos ~70–100 clics y **~12–20 llamadas por mes**. Eso nunca llega a 30 conversiones en 30 días, así que **tCPA no es alcanzable con este presupuesto**. Hay que quedarse en Max. conversiones sin tCPA, o con un tCPA suelto como el de A si el CPL se estabiliza. Para 30 conv/mes al CPL objetivo harían falta ~$1,500–1,800 de pauta.
- El volumen local es chico: las keywords "electrician + ciudad" de NWA suman ~450 búsquedas/mes (Semrush), y "electrician lowell ar" tiene 10. El presupuesto de $27/día **no** está limitado por falta de demanda.

## Lo que hacen las cuentas que mejor rinden (A y B)
- **Puja**: Max. conversiones desde el inicio; A agregó tCPA $20 después. Las dos que pujan a clics (C y D) tienen un CPL 10–25 veces más alto.
- **Conversiones**: "Calls from ads" más "Website Calls / Calls from Website". Las llamadas del sitio suman 11 conv. en A y 7 en B. Pro Phase solo mide "Calls from Ads".
- **Estructura**: 1 campaña Search Radius y 1–4 ad groups. Las keywords son genéricas de intención ("electrician(s)", "electrician near me", "electrical companies") más **ciudad** y **marca propia**. La marca aporta ~20% de las conversiones (A: ~16 de 54; B: 6 de 39).
- **Match types**: casi todo broad en las dos, pero en mercados chicos y con Max. conversiones, que filtra por intención. Esto **choca con el estándar PMM (phrase)**; no lo tomo como modelo.
- **Geo**: radio. Presencia vs interés no se puede leer desde Windsor; revisarlo en la cuenta.
- A tiene además PMax ($362, 22 conv., CPL $16) con $2/día. Eso no cumple las condiciones PMM para PMax; se anota como dato, no como modelo.

## Keywords que más convierten en el nicho (agregado)
| Keyword | Match | Conv. | Gasto | CPL |
|---|---|---|---|---|
| electricians | broad | 31.7 | $646.83 | $20.42 |
| electrician near me | broad/phrase | 10 | $218.60 | $21.86 |
| marca propia (A y B) | broad | 16 | $95.21 | $5.95 |
| wiring electrician | broad | 8 | $57.08 | $7.14 |
| a licensed electrician | broad | 4 | $20.94 | $5.24 |
| electric electric company / electrical companies | broad | 7 | $122.67 | $17.52 |
| electrician + ciudad (varias) | phrase/broad | ~5 | ~$110 | ~$22 |
| electrical repair | broad | 2.7 | $36.62 | $13.73 |

Keywords de servicio en D (Max. clics) con **0 conversiones**: "home electrical" ($945), "electrical services" ($692), "ev charger installation near me" (1 conv. / $276), "home ev charger installer" ($172), "electrician ceiling fan installation" ($99), "electrical repairs" ($118), "emergency electrician" ($53).

## Negativas frecuentes del nicho
Salen de los search terms de A, B y Pro Phase y de la lista PMM:
- **Empresas de energía y cooperativas**: `carroll electric`, `ozarks electric`, `bentonville electric`, "electric company" como servicio público, `swepco`, `electric bill`, `pay bill`, `power outage`. En NWA "electric" suele ser la cooperativa.
- **Competidores por nombre**: axis, epic, hills, abs electrical, arnold & blevins, triway, etc. Excluir como keyword objetivo (estándar 5); ver /competitors.
- **Producto / DIY**: `nema 14 50 outlet`, `dc charger for home`, `level 2 ev charger for home` (sin "install"), `junction box`, `old time wiring`, `replacing ceiling fan`.
- Otros: `handyman`, `low cost`, `motor repair`, `ac unit repair`, `electrical supply`.

## Historial propio del cliente (758-301-1023)
Campaña "ENHPRM Radius", creada el 01-sep-2026. Imprime desde el 09-sep y gasta desde el 11-sep. Budget $27/día, **Max. clics**, 1 ad group con broad match.

| | Pro Phase | Grupo que funciona (A/B) |
|---|---|---|
| CPC | **$12.65** | $3.60–5.20 |
| Tasa conv. | 2.9% | 29–31% |
| CPL | **$442.75** (1 conv.) | $12–18 |
| IS perdida por presupuesto / ranking | 47% / 31% | 16–41% / 37–41% |

**Diagnóstico** (11 días con gasto; poca muestra, pero el patrón es claro):
1. **Pujar a clics con broad compra tráfico basura caro.** De $290.74 en search terms visibles, **~$219 (75%) no tenía intención**: $68.58 fueron cooperativas o empresas de energía, $68.90 competidores y $81.12 producto, DIY o información. Otros $72 fueron términos genéricos ("electrical", "electrical companies" a **$23/clic**). ~$152 no aparecen por umbral de privacidad.
2. **Es la misma plantilla de D** ("home electrical", "electrical services" en broad), que en D quemó $1,637 con 5 conversiones. No hay keywords de ciudad ni de marca.
3. **Tracking incompleto**: solo "Calls from Ads". No se miden llamadas desde el sitio ni formularios, así que Max. conversiones tendría menos señal de la que puede tener.
4. Del 11 al 15-sep gastó ~$54/día, el doble del budget (sobreentrega diaria permitida). Después bajó a $11–35.

**Qué cambiar** (lo decide /strategy):
1. Pasar a **Max. conversiones**.
2. Usar phrase: "electrician" + ciudades de NWA, "electrician near me", marca propia, y paneles y EV como ad groups separados.
3. Aplicar negativas de utilities, competidores y DIY desde hoy.
4. Agregar las conversiones de llamadas desde el sitio y del formulario, y probarlas con Tag Assistant.

## Advertencias
- Solo 4 cuentas comparables, con 2 grupos de puja muy distintos; los percentiles son orientativos.
- Ninguna comparable está en Arkansas. A y B son mercados chicos y baratos; C y D son California. El CPC de NWA sale de Semrush y del propio Pro Phase, no de una comparable.
- "Conversión" = llamada desde anuncio o sitio con la duración mínima de la cuenta (probablemente 60 s por defecto). **No es lead calificado.** El CPL real por trabajo es más alto.
- Los datos vienen de Windsor.ai y no de la API. Sin la API no pude leer presencia vs interés, extensiones ni programación. Revisar a mano o cuando esté `google-ads.yaml`.
- El historial de Pro Phase son 11 días con gasto; es un diagnóstico de configuración, no de rendimiento.
- Proponer etiquetas `nicho:electrician` y `pais:US` en el MCC para las cuentas 334-048-0032, 324-020-3548, 436-679-0497, 684-092-9740 y 758-301-1023.
