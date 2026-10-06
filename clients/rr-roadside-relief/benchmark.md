---
cliente: RR Roadside Relief
slug: rr-roadside-relief
nicho: towing
pais: US
cuentas_comparables: 30 (20 maduras con 3 meses completos + 10 nuevas)
periodo: 90d (jul–sep 2026)
actualizado: 2026-10-01
---

# Benchmark interno — RR Roadside Relief

Fuente: Windsor.ai (conector google_ads) sobre las cuentas de towing del MCC, todas con la plantilla ENHPRM ("Premium Local Listings"). Datos crudos: `knowledge/benchmarks/raw/towing-us-2026-q3-monthly.csv`.

## Rangos esperados para este nicho/país
Cuentas maduras (n=20, con jul, ago y sep completos):

| Métrica | P25 | Mediana | P75 |
|---|---|---|---|
| CPC | $4.08 | $4.91 | $6.01 |
| CTR | 5.1% | 6.9% | 8.1% |
| Tasa conv. | 23.5% | 28.2% | 38.5% |
| CPL | $11.87 | $14.66 | $23.41 |
| Conv./mes | 23 | 43 | 62 |
| Gasto real/mes | $420 | $728 | $1,094 |

Cuentas nuevas (n=10, primeros 1–2 meses): CPL de $31 a $78 (mediana ≈ $63) y CPC de $2.5 a $11.9 (mediana ≈ $7.6). Las cuentas tardan unos 2–3 meses en bajar al rango maduro.

**CPL objetivo inicial sugerido**:
- Mes 1–2 (aprendizaje): ≤ $45 por conversión.
- Mes 3+: mediana ±20% → **$12–$18**. Hasta $23 (P75) es aceptable.

**Con el gasto real esperado**: el "$2,250/mo" del nombre es el precio del paquete, no el gasto en pauta.
- En las 20 cuentas maduras, el gasto real es entre el 23% y el 70% del monto del nombre (mediana ≈ 44%). RR gasta hoy ≈ $43/día, o sea ~$1,300/mes (58%), dentro del rango normal. **Confirmar con Jhombis el presupuesto de pauta real.**
- Con ~$1,300/mes:
  - Mes 1–2: ~20–35 conversiones/mes.
  - Mes 3+ con CPL de $15–23: ~55–85 conversiones/mes. Como referencia, una cuenta comparable con $1,129/mes saca 88/mes.
- Se llega a 30 conversiones/30 días (umbral para tCPA) en ~6–8 semanas si se corrigen el desperdicio y el ranking.

## Lo que hacen las cuentas que mejor rinden
Cuartil superior por CPL ($8–13): 7 cuentas con 31–153 conv./mes.
- **Puja**: todas en Maximizar conversiones sin tCPA. Las peores (CPL $41–70) incluyen 2 de las 4 cuentas que usan Maximizar clics (TARGET_SPEND).
- **Geo**: Presencia en las campañas Search de todas. Excepciones con "Presencia o interés" solo en algunas PMax o campañas heavy duty.
- **Red**: Search sin partners ni Display. Una cuenta del P75 sí tiene partners en Search.
- **IS perdido por ranking**: las mejores pierden 9–30%. RR pierde **62%**: el problema de RR es ranking (QS/puja/landing), no presupuesto.
- **IS perdido por presupuesto**: las mejores pierden 35–78%. Muchas cuentas buenas están limitadas por presupuesto con CPL bajo, una señal de que vale la pena subir el gasto cuando el CPL está en rango.
- **PMax**: 5 de las 7 mejores tienen PMax además de Search. PMax reporta CPL muy bajo (p. ej. $6 por conversión) pero sin validar la calidad de esas conversiones. Según el estándar PMM #9, no se lanza al inicio.
- **Match types**: la plantilla ENHPRM usa casi todo en **amplia** con ~450 negativas de campaña, y aun así las cuentas maduras dan buen CPL. Eso contradice el estándar PMM #2. Para RR se mantiene frase/exacta: la cuenta es nueva, el tracking no está validado y el 54% del gasto visible en search terms fue desperdicio.
- **Keywords de ciudad**: las cuentas que convierten bien tienen variantes "tow truck <ciudad>" y "towing <ciudad> <estado>" con CPL bajo. RR no tiene ninguna keyword con OKC salvo "roadside assistance okc".

## Keywords que más convierten en el nicho (agregado, 20 cuentas maduras, 90 d)
| Tema | Conv. | Gasto | CPL aprox. | Nota |
|---|---|---|---|---|
| towing near me | ~790 | ~$8,700 | ~$11 | Motor del nicho, en 16 de 20 cuentas |
| tow truck near me / tow trucks near me | ~155 | ~$1,400 | ~$9 | |
| Español (grúa/grúas cerca de mí, servicio de grúa, asistencia en carretera, auxilio vial) | ~110 | ~$1,150 | ~$10.5 | **Convierte igual que inglés**; en 5 cuentas |
| roadside assistance (+ near me) | ~75 | ~$800 | ~$11 | Una cuenta saca 47 conv. a $7 |
| tow truck / towing + ciudad | ~90 | ~$700 | ~$8 | Muy eficiente |
| Marca propia | ~95 | ~$800 | ~$8.5 | Solo cuentas con marca conocida |
| cheap towing / cheap tow truck near me | ~36 | ~$300 | ~$8 | **No negativizar "cheap"** |
| jump start / lockout (ES: "sacar llaves", "abrir carro") / tire | ~15 | ~$110 | ~$7 | Bajo volumen pero barato |

## Negativas frecuentes del nicho
Todas las cuentas ENHPRM comparten una plantilla de ~450 negativas de campaña en amplia: aseguradoras y motor clubs (AAA, Geico, State Farm, Allstate, USAA, Progressive), marcas de autos, impound/repo/"my car was towed", tow yard/lot, rentals (U-Haul, Penske, Ryder), empleo, DIY/how to, tiendas de llantas y autopartes. RR ya la tiene (ver `log/2026-10-01.md`). El riesgo de la plantilla son las negativas amplias de una sola palabra (quick, budget, discount, new, mobile), que bloquean búsquedas comerciales.

## Historial propio del cliente
Cuenta 425-405-2574, 16 días (15-sep → 1-oct):

| Métrica | RR | Benchmark nuevas | Benchmark maduras (mediana) | Diagnóstico |
|---|---|---|---|---|
| CPC | $6.90 | ~$7.6 | $4.91 | En línea con cuentas nuevas; por encima del P75 maduro |
| CTR | 5.6% | — | 6.9% | P25: anuncios genéricos, un solo ad group |
| Tasa conv. | 8.5% | — | 28.2% | **Muy baja**: landing sin formulario arriba y tráfico irrelevante (54% de desperdicio) |
| CPL | $81 | ~$63 | $14.66 | Peor que las nuevas, y 2 de 8 conversiones son sospechosas |
| IS perdido por ranking | 62% | — | 9–30% en top | Ranking es el freno principal |
| IS perdido por presupuesto | 19% | — | — | Secundario |

Diagnóstico: es pronto para juzgar (16 días), pero el patrón apunta a problemas de calidad, no de presupuesto:
- keywords en amplia sin estructura;
- landing genérica y lenta;
- conversión baja por clic.

Lo que corrigen `/negatives` + la reestructura de `/strategy` + los bloqueantes de `audit-site.md` es exactamente lo que separa a RR de las cuentas del cuartil superior.

## Advertencias
- Datos de Windsor, no de la API: no se pudo leer extensiones, programación, tCPA ni negativas por cuenta. La tasa de conversión del 28% sugiere que "Calls from Ads" cuenta llamadas cortas; el CPL real de leads calificados en el nicho probablemente es más alto. Verificar el umbral de duración de llamada en la plantilla ENHPRM.
- Las 20 cuentas maduras son de mercados distintos (IN, VA, KY, CA, GA, NY, MI, CO, TX…). No hay ninguna en Oklahoma.
- Las conversiones de PMax incluidas en los agregados de cuenta bajan el CPL del benchmark frente a una cuenta solo Search.
- 5 cuentas de towing del MCC no tuvieron gasto en 90 días y se excluyeron.
