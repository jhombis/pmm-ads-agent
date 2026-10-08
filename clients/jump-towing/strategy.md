---
cliente: Jump Towing LLC
slug: jump-towing
actualizado: 2026-10-08
version: 2
supuestos:
  - audit-site.md no existe (jumptowing.com bloqueado por el proxy de la sesión). Las landings se asumen PENDIENTES.
  - Ticket promedio y margen PENDIENTES. CPL máximo sin calcular; el objetivo sale del benchmark.
  - Volumen local "near me" estimado como nacional × ~0.18% (población del radio). Falta Keyword Planner geolocalizado.
  - Lista exacta de roadside PENDIENTE. Las keywords de lockout, llanta y combustible de G4 se activan solo si se confirman.
  - Flatbed, licencia/seguro, precio base y tiempos de llegada sin confirmar. El copy los marca [C].
  - GBP PENDIENTE. Sin activo de ubicación ni LSA.
  - CallFire mide todas las llamadas al (612) 665-6274. No se sabe si el número está solo en la extensión de llamada o también en la web/GBP.
  - Gasto de Ads de oct s/d (Windsor sin autorizar en la sesión).
cambios_v2:
  - "Puja: Maximizar clics con tope de CPC $8 (playbook §5, estándar 6 de CLAUDE.md al 08-oct) en lugar de Maximizar conversiones."
  - "Estructura: 4 ad groups en lugar de 7, por el límite de fragmentación ($600–1,500 → 3–5 grupos)."
  - "RSA: 1 por ad group (máx. 2) en lugar de 3: con <$1,500/mes un A/B es ruido."
  - "Datos reales de CallFire: costo por llamada calificada ≥60 s en sep = $76.50."
---

# Estrategia Google Ads — Jump Towing LLC (v2)

## Resumen ejecutivo
- **1 campaña Search** ("Towing & Roadside") con **4 ad groups**, dentro de la cuenta 220-410-9619. La campaña actual ("ENHPRM Radius") se pausa el día del lanzamiento.
- **Presupuesto**: $825/mes, es decir **$31/día**, con anuncios solo lun–sáb en horario del cliente (~26.5 días activos/mes).
- **Puja**: **Maximizar clics con tope de CPC de $8**.
  - Se pasa a Maximizar conversiones cuando haya **≥15 llamadas calificadas/mes estables** y la conversión de Ads tenga umbral de 60 s.
  - tCPA solo con ~30 en 30 días, fijado desde el CPA observado.
- **Línea base real (CallFire)**: en septiembre, $458.97 de gasto dieron 6 llamadas calificadas ≥60 s, o sea **$76.50 por llamada calificada**. Entre el 14-sep y el 08-oct hubo 12 calificadas, unas 14 por mes: estamos cerca del umbral de 15.
- **Objetivo**:
  - F2: bajar a **≤ $41.51 por llamada calificada** (P75 de CPL Search del benchmark).
  - Referencia de largo plazo: $21–31 (mediana Search ±20%), sujeta al CPL máximo del cliente.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| Search \| Towing & Roadside \| 10mi \| v1 | Llamadas ≥60 s | $31 | 100% | Maximizar clics, tope CPC $8 | **Presencia**, radio 10 mi en (45.093312, -93.343931). Excluir resto de países | Lun–vie 6:00–18:00, sáb 6:00–15:30, dom off (America/Chicago) |
| ~~Marca~~ | — | — | — | — | — | No en F1: "jump towing" tiene 20/mes y se confunde con el genérico "jump start towing" |
| LSA (pista paralela) | Llamadas | Aparte, a definir | — | — | 10 mi | Igual al horario |

**Por qué una campaña y 4 grupos:** el límite de fragmentación del playbook para $600–1,500/mes es 1 campaña y 3–5 grupos. Con ~4.7 clics/día, más grupos no acumulan datos.

**Por qué Maximizar clics con tope:** la cuenta tiene <15 conversiones/mes. El problema de la campaña actual no es Maximizar clics en sí, sino que corre **sin tope, en broad y con geo dudosa**: eso compra lo genérico y barato (Sioux Falls, I-29, competidores). El tope de $8 queda por encima del CPC real ($6.56) y del P75 del nicho ($6.60), para no perder las subastas de alta intención.

**Por qué el horario no lleva margen:** nadie confirmó cobertura fuera de horario. Pero CallFire muestra 2 llamadas contestadas después del cierre (vie 18:08, sáb 16:15). Si el cliente confirma que contesta hasta las 19:00, se amplía.

**Configuración fija (estándares PMM):**
- Solo red de Búsqueda: sin socios, sin Display.
- Recomendaciones automáticas apagadas. Rotación optimizada.
- Sin exclusiones de audiencia. Idioma inglés. Todos los dispositivos.

## Estructura
### Campaña: Search | Towing & Roadside | 10mi | v1
Volúmenes: Semrush US (ciudad) o estimación near-me × 0.18%. Detalle en `data/keywords.csv`.

| Ad group | Keywords (match) | Vol. est./mes | Landing | H1 pinneado |
|---|---|---|---|---|
| **G1 Towing Near Me** | [towing near me], [tow truck near me], [towing company near me], "towing service near me", "emergency towing near me", "towing service", "tow truck service", "towing company", "car towing", "tow service", "flatbed towing near me" [C] | ~560 | /jump-towing/towing/ | Tow Truck Near You |
| **G2 Towing Brooklyn Park & NW** | [towing brooklyn park mn], [tow truck brooklyn park], "towing brooklyn park" + "towing <ciudad>" y "tow truck <ciudad>" para Maple Grove, Plymouth, Coon Rapids, Crystal, Brooklyn Center, Fridley, New Hope, Robbinsdale, Champlin, Osseo | ~220 | /jump-towing/towing/ | {KeyWord:Towing in Brooklyn Park} |
| **G3 Towing Minneapolis** | [towing minneapolis], [tow truck minneapolis], "car towing minneapolis", "flatbed towing minneapolis" [C], "cheap towing minneapolis", "24 hour towing minneapolis" | ~800 (solo el norte cae en el radio) | /jump-towing/towing/ | Towing in Minneapolis, MN |
| **G4 Roadside** | [jump start service near me], "car jump start", "jump start minneapolis", "battery jump service", "i need a jump", "roadside assistance minneapolis". Con confirmación: "car lockout service near me", "locked out of car", "flat tire service near me", "gas delivery near me", "ran out of gas" | ~90 | /jump-towing/roadside/ | {KeyWord:Roadside Help Near You} |

- **G2** junta Brooklyn Park con las ciudades del radio porque cada una tiene <100/mes. La inserción de keyword pone la ciudad en el H1.
- **G3** va aparte porque "towing/tow truck minneapolis" suman 530/mes y piden el H1 con Minneapolis.
- **G4** junta todo el roadside en un grupo con una landing por secciones. Las keywords sin confirmar se cargan en pausa.
- No hay ad group de "Emergency/24-7": el cliente no es 24/7. "emergency towing" entra en G1 con el horario real en el copy.

Negativas cruzadas entre grupos:
- **G1**: brooklyn park, minneapolis, y las ciudades de G2; jump, lockout, locked, tire, gas, fuel.
- **G2**: minneapolis; jump, lockout, tire, gas, fuel.
- **G3**: brooklyn park y las ciudades de G2; jump, lockout, tire, gas, fuel.
- **G4**: towing, tow truck, tow.

## Keywords descartadas y por qué
| Keyword | Vol. | Motivo |
|---|---|---|
| minneapolis impound / impound lot minneapolis | 590 / 260 | Navegacional: lote municipal |
| heavy duty / semi truck towing | 1,900 / 1,300 nac. | No ofrece heavy-duty |
| cash for junk cars / junk car removal minneapolis | 40 / 10 | Otro servicio |
| motorcycle towing minneapolis | 20 | PENDIENTE confirmar servicio |
| roadside assistance near me | 33,100 nac. | Mezcla membresías y aseguradoras. Solo entra la versión con ciudad, en G4 |
| jump towing | 20 | Ambiguo marca/genérico |
| marcas de competidores | — | No pujar salvo prueba controlada |
| términos en español | — | El ad group en español gastó ~$55 con 1 conversión |

Lista completa: `data/negatives-nicho.txt` (124 del nicho) + universal PMM a nivel de cuenta.

## Copy
En `data/ads-search-towing-roadside.md`: **1 RSA por ad group** (máx. 2), cada uno con 15 headlines (H1 pinneado + pool común) y 4 descripciones.
- Ángulos del gap de competencia:
  - "Based in Brooklyn Park, MN".
  - "Cars, SUVs & Light Trucks".
  - "Local Tows From $XX" [C].
  - "Open Mon-Sat From 6 AM".
- Prohibido: "24/7", número de reseñas o años, tiempos de llegada concretos.

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| jumptowing.com (home) | Sí (sin auditar) | PMM | **Sí**: /audit-landing desde un entorno con acceso |
| https://performancemediamarketing.com/jump-towing/towing/ (G1–G3) | **Publicada el 08-oct** (solo llamada, excepción aprobada; GTM-T9JFQNTC; privacidad del cliente) | PMM | No (falta Tag Assistant) |
| https://performancemediamarketing.com/jump-towing/roadside/ (G4) | **Publicada el 08-oct** (solo llamada; jump start + remolque; lockout/llanta/combustible al confirmarse) | PMM | No |

En las landings, **un solo teléfono**: el número de seguimiento que corresponda (Google forwarding o CallFire), nunca el directo (612) 616-0723.

## Presupuesto por fase
| Fase | Total/mes | Qué pasa | Condición para pasar |
|---|---|---|---|
| **F0** Saneamiento | Decisión de Jhombis sobre la campaña actual | Tope de CPC, phrase, sin ad group en español, negativas, geo | Llamada ≥60 s medida, dónde va el número de CallFire, /towing aprobada, negativas aplicadas |
| **F1** Lanzamiento (días 1–30) | $825 | $31/día, Max. clics con tope de $8, G1–G4 | ≥14 días y ≥10 calificadas; search terms revisados D7 y D14 |
| **F2** Optimización (31–60) | $825 | Pausar keywords con ≥$62 y 0 conversiones; ajustar el tope según IS perdido por ranking | Costo por calificada ≤ $41.51 sostenido |
| **F3** Puja (61–90) | $825 → propuesta $1,100–1,200 si el IS perdido por presupuesto es >40% | **Max. conversiones** con ≥15 calificadas/mes estables; tCPA solo con ~30/30d, desde el CPA observado | Medición limpia (60 s) y volumen |
| **LSA** (paralelo) | Aparte, a definir | Solicitud y verificación | GBP verificado + seguro + background check |

Nota: el tope mensual real de Google es $31 × 30.4 = $942. Con solo ~26.5 días activos, el gasto esperado es ~$820. Hay que vigilar la semana 1.

## Por qué NO (todavía)
- **PMax**: requiere ≥3× CPA/día (≈ $78/día solo para PMax), tCPA estable 4 semanas, 30+ conv./mes, GBP y assets propios. No se cumple ninguna.
- **Amplia / AI Max**: requiere tCPA maduro, ~50 conversiones limpias y aprobación de Jhombis. La cuenta actual en broad compró Iowa, Dakota del Sur y competidores.
- **Maximizar conversiones desde el día 1**: con <15 conversiones/mes la puja automática puja a ciegas (playbook §5).
- **Display / Video / Demand Gen**: el remolque es una necesidad inmediata.
- **Campaña de marca**: no hay búsquedas de marca medibles.
- **Ad group en español**: no hay mercado.
- **3 RSA por grupo**: con ~4.7 clics/día un A/B da ~60 clics por variante en 90 días. Es ruido.

## Riesgos y supuestos
1. **El horario recorta la demanda.** Los 6 competidores son 24/7. CallFire muestra que el sábado es el día con más llamadas (7 de 28) aunque cierra a las 15:30, y que hubo llamadas después del cierre.
2. **El costo real por calificada es $76.50**, unas 3 veces la mediana Search del benchmark. El benchmark cuenta llamadas sin calificar; la meta de F2 ($41.51) ya es exigente.
3. **CPL máximo sin calcular.** Ejemplo ilustrativo: ticket $125 × margen 50% × cierre 60% × 0.3 ≈ $11. Con un margen así, ni siquiera $21–31 es rentable. Es bloqueante.
4. **Atribución:** si el número de CallFire también está en la web o el GBP, el costo por calificada mezcla llamadas orgánicas.
5. **Llamadas perdidas:** 2 en horario en una semana (06 y 07-oct), ≈ $66 de pauta si venían de Ads.
6. **Hueco del 26-sep al 02-oct**: 0 llamadas. Sin explicar hasta revisar la cuenta.
7. **Sin GBP**: no hay activo de ubicación, Maps ni LSA. Los competidores tienen 153–387 reseñas.
