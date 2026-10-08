---
cliente: RR Roadside Relief
slug: rr-roadside-relief
actualizado: 2026-10-08
version: 1
supuestos:
  - Presupuesto de pauta real: el ritmo observado es ~$49/día (~$1,490/mes; corregido el 01-oct, antes se estimó en $43/día). El paquete de $2,250 no es todo pauta. PENDIENTE confirmar.
  - Área de servicio = OKC metro, radio de 25 mi. PENDIENTE confirmar (la web dice "anywhere in Oklahoma City").
  - Ticket promedio y tasa de cierre desconocidos. El CPL objetivo sale del benchmark interno, no de la economía del cliente.
  - 24/7 real: CONFIRMADO con CallFire (22 de 23 llamadas nocturnas contestadas, 16-sep → 08-oct).
  - Atención en español desconocida. AG10 queda condicionado.
  - Sin oferta de precio confirmada. Los headlines con precio llevan ⚠ y no se publican hasta confirmar.
  - Volúmenes OKC estimados como volumen nacional × 0.43% (población del metro), salvo keywords con ciudad (volumen real). Validar con Keyword Planner geo OKC cuando la API esté disponible.
---

# Estrategia Google Ads — RR Roadside Relief

## Resumen ejecutivo
1. **Una sola campaña Search**. Se reestructura la campaña existente (24255091376): 10 ad groups STAG (9 EN + 1 ES condicional), keywords en frase/exacta y "Ad group 1" pausado. El presupuesto (~$43/día) solo alcanza para una campaña con la regla de aprendizaje.
2. **Puja**: Maximizar conversiones (se mantiene). El conteo de llamadas debe pedir ≥60 s antes de confiar en la señal.
3. **CPL objetivo**: ≤ $45 en semanas 1–8 y $12–18 desde el mes 3 (mediana del benchmark ±20%; P75 = $23 aceptable).
4. **tCPA** con 30 conversiones en 30 días. Se espera hacia la semana 6–8 del relanzamiento si se corrigen el desperdicio (54%) y el IS perdido por ranking (62%).
5. **En paralelo**: LSA (towing elegible en OKC) y fix de landing (formulario arriba, velocidad, 5–6 páginas nuevas). PMax, RLSA y amplia no van ahora.

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| RR Roadside Relief - ENHPRM Radius (reestructurada) | Llamadas (principal) + formulario | $43 | 100% | Maximizar conversiones, sin tCPA | Presencia; radio 25 mi desde OKC centro ⚠; excluir resto de US | 24/7 ⚠ (revisar las llamadas nocturnas no contestadas en /weekly-review) |
| LSA: Towing (pista paralela) | Leads pagados por lead | Aparte (LSA cobra por lead) | — | Max leads | OKC + ciudades del radio | 24/7 |

Configuración de la campaña Search:
- **Red**: solo Search; sin partners ni Display (ya está así).
- **Idiomas**: inglés + español (para AG10).
- **Rotación**: optimizar.
- **Recomendaciones automáticas**: OFF.
- **Audiencias**: sin exclusiones.

## Estructura por campaña
### Campaña: RR Roadside Relief - ENHPRM Radius
Volumen OKC estimado por grupo (búsquedas/mes). Detalle en `data/keywords.csv`.

| Ad group | Keywords (match) | Vol. est. | Landing | H1 pinneado |
|---|---|---|---|---|
| AG1 Towing Near Me | [towing near me], [tow truck near me], [towing company near me] + frase: "tow service near me", "tow truck service near me", "car towing near me", "towing service near me", "wrecker service near me", "towing service", "car towing service", "tow truck service" | ~3,100 | /light-medium-duty-towing/ (rehacer) | Tow Truck Near Me - 24/7 |
| AG2 Towing OKC & Cities | [towing okc], [tow truck okc] + frase: towing/tow truck oklahoma city, okc towing, towing edmond/norman/moore/yukon/midwest city, tow truck norman/moore | ~1,100 (real por ciudad: 20–320) | /light-medium-duty-towing/ | Towing in Oklahoma City |
| AG3 24/7 Emergency Towing | [24 hour towing near me], [emergency towing near me] + frase: 24 hour towing, 24/7 towing, emergency towing, tow truck open now | ~40 | /light-medium-duty-towing/ | 24/7 Emergency Towing OKC |
| AG4 Affordable Towing | [cheap towing near me], [cheap tow truck near me] + frase: affordable towing, affordable towing near me | ~110 | /light-medium-duty-towing/ (+ bloque de precio ⚠) | Affordable Towing in OKC |
| AG5 Flatbed & Motorcycle Towing | [flatbed tow truck near me], [motorcycle towing near me] + frase: flatbed towing, flatbed tow truck, motorcycle towing, motorcycle tow, lowered car towing | ~80 | /flatbed-motorcycle-towing/ (NUEVA) | Flatbed Towing in OKC |
| AG6 Roadside Assistance | [roadside assistance near me], [roadside assistance okc] + frase: emergency roadside assistance, 24 hour roadside assistance, roadside assistance oklahoma city, winch out (service), car stuck in mud, gas delivery near me | ~320 | /roadside-assistance/ (rehacer) | Roadside Assistance OKC |
| AG7 Flat Tire Change | [flat tire change near me] + frase: tire change near me, flat tire change, mobile tire change, roadside tire change, flat tire help | ~75 | /flat-tire-change/ (NUEVA) | Flat Tire Change in OKC |
| AG8 Car Lockout | [car lockout service], [car lockout near me] + frase: car lockout, locked keys in car, locked out of car | ~70 | /car-lockout/ (NUEVA) | Car Lockout Service OKC |
| AG9 Jump Start | [jump start near me] + frase: jump start service, car jump start service, dead battery jump start | ~10–20 | /jump-start/ (NUEVA) | Jump Start Service in OKC |
| AG10 Grúa en Español ⚠ | [grua cerca de mi] + frase: servicio de grua, grua okc, asistencia en carretera, auxilio vial | bajo (estimación muy gruesa; en el MCC convierte a ~$10.5) | /es/servicio-de-grua/ (NUEVA) | Grúa en Oklahoma City 24/7 |

Por qué así:
- **Ad groups por tema, no SKAG**: ninguna combinación de servicio × ciudad pasa de 100 búsquedas/mes, así que las ciudades van juntas en AG2.
- **AG3 separado**: la urgencia pide un copy distinto.
- **AG4 separado**: en el MCC "cheap towing" convierte a ~$8 CPL, pero el copy necesita un ángulo de precio.
- **AG5 separado**: los flatbeds y el remolque de motos y autos bajos son el diferenciador que ningún competidor usa en sus anuncios.
- **AG6–AG9**: servicios que la web ofrece y hoy no tienen keywords, con baja competencia (winch out, lockout).

Negativas específicas de cada grupo (ruteo + intención mixta) en `data/negatives-nicho.txt` §D–E. Resumen:
- AG1 excluye en exacta los términos de AG3/AG4/AG5.
- AG6 excluye tire/lockout/jump/tow truck.
- AG7–AG9 excluyen "towing".
- AG8 y AG9 excluyen "how to".
- AG7 excluye tiendas de llantas.

## Keywords descartadas y por qué
| Keyword | Motivo |
|---|---|
| roadside assistance (sola) | 450k/mes nacional, dominada por planes AAA y aseguradoras. Ya generó llamadas mal dirigidas (Lincoln). Solo se usa con "near me" o ciudad. |
| jump start (sola) | Informacional/producto (CPC $1.07). |
| fuel delivery / gas delivery | B2B (fleet fueling), CPC $6.7–8. Solo "gas delivery near me" en frase con puja controlada. |
| tow truck (sola) | Mezcla compra de camión, empleo e info. |
| aaa roadside call, marcas de planes | Navegacional, no es cliente de RR. |
| Marcas de competidores (Puckett's, 5 Star, Bad Day, Tow Mate…) | Estándar #5: el clic llega pero la venta no. |
| heavy duty / semi / 18 wheeler | El cliente solo hace light & medium. |

## Copy
RSA completos y extensiones en `data/ads-rr-search.md`:
- 15 headlines y 4 descripciones por grupo, con H1 pinneado y 3 RSA por grupo (ángulos rapidez / confianza / oferta).
- Ángulos tomados de los huecos en `competitors.md`:
  - **Especialidad flatbed** (autos bajos, motos): nadie la usa.
  - **Atiende una persona real 24/7.**
  - **Cotización gratis por teléfono.**
  - **Precio visible** ⚠: solo si el cliente confirma tarifa.
  - **Español** ⚠.
- No prometemos ETA de 30 min (5-Star y Oklahoma Towing Service sí) mientras el cliente no confirme que puede sostenerlo con 3 grúas.

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| / (home): H1 + formulario de 4 campos arriba + botón de llamar fijo en móvil | Sí, requiere ajuste | PMM | **Sí** (hoy recibe todo el tráfico) |
| /light-medium-duty-towing/: H1 "24/7 Towing in Oklahoma City" + formulario arriba | Sí, rehacer | PMM | **Sí** para AG1–AG4 |
| /roadside-assistance/: H1 con OKC + formulario arriba | Sí, rehacer | PMM | **Sí** para AG6 |
| /flatbed-motorcycle-towing/ | No | PMM | No (AG5 usa /light-medium-duty-towing/ mientras tanto) |
| /flat-tire-change/ | No | PMM | No (AG7 usa /roadside-assistance/ mientras tanto) |
| /car-lockout/ | No | PMM | No (fallback /roadside-assistance/) |
| /jump-start/ | No | PMM | No (fallback /roadside-assistance/) |
| /es/servicio-de-grua/ | No | PMM + cliente (confirma español) | **Sí** para AG10 (no se lanza AG10 sin landing en español) |
| /thank-you/ con URL propia | No | PMM | No (la conversión por evento funciona; mejora la medición) |

Comunes a todas: comprimir el logo (676 KB) y los headers, caché de página, y reseñas de GBP embebidas.

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |
|---|---|---|---|
| F0 — Correcciones (sem 0–1) | gasto actual | Campaña actual | Negativas aplicadas + limpieza de negativas de llantas, keywords amplia→frase/exacta, ad groups nuevos y "Ad group 1" en pausa, llamadas ≥60 s verificadas, Tag Assistant OK, landings de towing y roadside con formulario arriba |
| F1 — Relanzamiento (sem 1–4) | ~$1,300 ($43/día) ⚠ | 100% Search | ≥ 20 conv. en 30 días y CPL ≤ $45 con ≥ 70% de llamadas reales (escucha/feedback del cliente) |
| F2 — Optimización (sem 5–8) | ~$1,300 | 100% Search; pausar ad groups con gasto > 2× CPL y 0 conv. | ≥ 30 conv. en 30 días → tCPA = CPL real de 30 días (no más bajo de entrada) |
| F3 — Escala (mes 3+) | $1,300–2,000 según el paquete real | Si pauta ≥ $90/día: dividir en **Towing (65%)** y **Roadside+Tire+Lockout+Jump (35%)**; ES como campaña propia si AG10 da ≥ 10 conv./mes | CPL ≤ $23 sostenido 4 semanas; IS perdido por ranking < 35% |
| F4 — Remarketing (mes 4+) | +10% | RLSA en observación sobre Search | Lista de visitantes ≥ 1,000 usuarios |
| F5 — PMax (condicional) | +20–30% | PMax con exclusión de marca y assets propios | Ver abajo |

Regla de aprendizaje: cada campaña necesita ≥ 3× CPL por día. Con un CPL maduro de $15 son $45/día por campaña, y hoy hay $43/día en total. Por eso va **una sola campaña** hasta F3.

## Por qué NO (todavía)
- **PMax**: el estándar #9 pide Search estable, 30+ conversiones/mes con tracking confiable, exclusión de marca y assets propios. RR tiene 8 conversiones en 16 días (2 sospechosas), sin reseñas ni fotos propias validadas, y la landing saca 10/22. En el MCC, PMax reporta CPL de ~$6 pero sin validar la calidad de esas conversiones. Primero hay que probar que las conversiones de Search son llamadas reales.
- **Amplia**: hoy toda la cuenta está en amplia y el 54% del gasto visible fue desperdicio. Las cuentas maduras del MCC corren amplia con ~450 negativas, pero tienen meses de datos. Se reevalúa solo con tCPA maduro, tracking validado y aprobación de Jhombis.
- **Display / Video / Demand Gen**: no aplica a towing de emergencia.
- **Campaña de marca**: 0 búsquedas de "RR Roadside Relief" en 30 días y ningún competidor puja por la marca.
- **Dividir en varias campañas ya**: el presupuesto no da para que cada una salga de aprendizaje.

## Riesgos y supuestos
- **Medición (actualizado 08-oct, CallFire)**: Ads subcuenta. Del 16-sep al 01-oct reporta 7 llamadas y CallFire registra 19 calificadas ≥60 s (~$36 por llamada calificada si todas vienen de Ads). La prioridad de F0 pasa de "evitar contar basura" a **"hacer que Ads vea las llamadas reales"**: conversión de llamadas desde la web + recurso de llamada ≥60 s. tCPA nunca se fija desde el CPA de Ads ($85) mientras subcuente.
- **Calidad de conversión**: si "Calls from Ads" cuenta llamadas cortas o mal dirigidas, Maximizar conversiones optimiza hacia basura. Es la acción F0 más importante después de las negativas.
- **Landing**: sin formulario arriba y con carga lenta, el IS perdido por ranking seguirá alto (QS bajo) y el CPC por encima de $6. El benchmark de mercado está en $3–4 (Semrush) y $4.91 en el MCC maduro.
- **Reputación**: 0 reseñas frente a las ~1,500 de 5-Star. Afecta CTR, LSA y conversión. Hay que conseguir las primeras 20–30 reseñas en GBP (cliente). Sin GBP no hay activo de ubicación ni Maps.
- **Presupuesto real desconocido**: si la pauta es menor a $43/día, se recortan AG5/AG9/AG10; si es mayor, F3 se adelanta.
- **24/7**: si nadie contesta de noche, hay que programar el horario real; los leads nocturnos sin respuesta se pierden.
- **Volúmenes estimados**: los volúmenes OKC son proyecciones. Validar con Keyword Planner y con los search terms de las primeras 2 semanas.
