---
cliente: Colton Sunflower Burial and Cremation
slug: colton-sunflower
nicho: funeraria / cremación
pais: US
cuentas_comparables: 5
periodo: 90d (2026-07-03 → 2026-09-30)
actualizado: 2026-10-01
---

# Benchmark interno — Colton Sunflower

Cuentas comparables (MCC PMM, sin etiquetas `nicho:*`, filtradas por nombre): Sunflower Cremation Services (Riverside), Hemet Affordable B&C, Murrieta Valley FH, Inland Memorial, Swan B&C (Tucson, AZ: otro mercado, se incluye por nicho). Métricas **solo de Search**, salvo donde se indica.

## Rangos esperados para este nicho/país (Search, 90d)
| Métrica | P25 | Mediana | P75 | **Colton** |
|---|---|---|---|---|
| CPC | $5.94 | $8.64 | $9.41 | $5.94 |
| CTR | 4.3% | 8.1% | 9.2% | 7.8% |
| **Tasa conv.** | **8.3%** | **9.7%** | **11.9%** | **1.5%** |
| CPL | $58 | $73 | $133 | **$394** |
| Conv./mes | 7 | 10 | 15 | 3.7 |
| Gasto Search/mes | $889 | $1,029 | $1,145 | $1,450 |

CPL de la cuenta completa (Search + PMax + Display): P25 $42 · mediana $56 · P75 $108.

**El problema de Colton no es el CPC ni el CTR, que están en rango. Es la tasa de conversión: 1.5% contra 8–12%.** Coincide con lo que encontramos antes:
- Tráfico basura por amplia + Max clics (≈80% del gasto visible).
- La home, que es URL final, no tiene formulario.
- El formulario no se mide.

**CPL objetivo inicial sugerido**: mediana ±20% → **$58–$87 (punto medio $73)**.
**Con $1,490/mes**: ~20 conversiones/mes a $73. Para tCPA hacen falta 30 en 30 días, lo que exige un CPA de ~$50 (nivel P25). **El presupuesto es suficiente para salir de aprendizaje**: las hermanas logran 7–20 conv/mes gastando $900–1,150/mes en Search. **No alcanza para tCPA** salvo que Colton llegue a P25.

## Lo que hacen las cuentas que mejor rinden
- **Sunflower Riverside (CPL $50) y Swan ($58)**:
  - 1 campaña Search con **1 solo ad group** genérico.
  - Keywords **amplias** con **Maximizar conversiones** (sin tCPA); la mejor es "cremation cost" (amplia): 23 conv, $44 CPA en 90d.
  - Más una PMax madura (29–49 conv/90d).
  - IS perdido por presupuesto: 26–75%, es decir, limitadas por presupuesto con buen CPA.
- **Hemet ($133)**: 3 ad groups (General / Cremation / Burial), frase y amplia, Max conv; CPC alto ($13) pero 9.7% de conversión.
- **Común a todas**:
  - Max conversiones.
  - Conversiones de **Form Fill + Calls from ads + Website calls**.
  - Geo con presencia.
  - Reciben mucha **búsqueda de marca** que convierte barato (swan funeral home, murrieta valley mortuary, inland memorial funeral care, sunflower cremation).
- **Lectura para Colton**: la amplia funciona en este nicho **solo con Max conversiones y tracking completo**. Colton tiene amplia con Max clics y sin formulario medido, la peor combinación. Se mantiene la estrategia (frase/exacta + Max conv en F1) y se prueba "cremation cost" en amplia en F2, con aprobación de Jhombis.

## Keywords que más convierten en el nicho (agregado, 90d)
- **Marca propia** (la mayor parte de las conversiones baratas): "<marca> funeral home", "<marca> mortuary", "<marca> cremation".
- **Precio**: "cremation cost" (amplia), "low cost cremation <county>", "cheapest mortuary near me", "average cost of cremation in california" (convirtió en una cuenta pese a ser informacional).
- **Ciudad + servicio**: "mortuary <ciudad>", "funeral homes in <ciudad> ca", "<ciudad> cremation", "direct cremation in san bernardino".
- **Near me**: "funeral homes near me", "mortuaries near me", "cremations near me", "cremation services near me".
- **Español** (convirtió en Hemet): "funeraria cerca de mi", "cuanto cuesta cremar una persona en eeuu". **Esto valida activar el grupo E de negativas solo si el cliente NO atiende en español, y considerar un ad group ES si sí atiende.**
- **Preneed**: "pre need funeral plans" convirtió en Hemet. Refuerza no negativizar "prepaid".

## Negativas frecuentes del nicho
No se extrajeron las listas de las otras cuentas en esta corrida (pendiente para la próxima). La lista de Colton (542 términos) ya cubre obituarios, productos, mascotas, empleo, informacionales y competidores; ver `data/negatives-nicho.txt`.

## Historial propio del cliente
| | Colton (57 días) | Mediana nicho |
|---|---|---|
| Puja | Max clics | Max conversiones |
| Match | ~70% amplia | mixto, con Max conv |
| Conversiones medidas | solo llamadas | formulario + llamadas |
| Tasa conv. | 1.5% | 9.7% |
| CPL | $394 | $73 |

Diagnóstico: **la estructura no es el problema principal; lo es la combinación de puja, tracking y landing.** Con Max clics, Google compra los clics más baratos dentro de la amplia (obituarios, Costco, mascotas). Sin formulario medido, ni siquiera Max conv tendría señal suficiente.

## Advertencias
- Solo 5 cuentas comparables; una es de otro mercado (Tucson) y otra tiene poco gasto en Search (Inland, $170/mes). Los percentiles son orientativos.
- Datos de Windsor.ai, no de la API (no hay google-ads.yaml en la sesión).
- Las cuentas del MCC no tienen etiquetas `nicho:funeral` / `pais:US`. **Propuesta: etiquetarlas** para que /benchmark-interno las encuentre sin filtrar por nombre.
- **Solape**: Sunflower Riverside e Inland Memorial convierten con términos de San Bernardino, que es la zona de Colton. El benchmark de Colton puede empeorar si las tres cuentas compiten en la misma subasta.
