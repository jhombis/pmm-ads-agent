---
cliente: Jump Towing LLC
slug: jump-towing
actualizado: 2026-10-01
version: 1
supuestos:
  - audit-site.md no existe (jumptowing.com bloqueado por el proxy de la sesión). Las landings se asumen PENDIENTES.
  - Ticket promedio y margen PENDIENTES. CPL máximo sin calcular; se usa el CPL del benchmark como objetivo.
  - Volumen local "near me" estimado como nacional × ~0.18% (población del radio). Keyword Planner geolocalizado no corrido (sin credenciales de API en la sesión).
  - Lista exacta de roadside PENDIENTE. R2 (lockout) y R3 (tire & fuel) son condicionales.
  - Flatbed, licencia/seguro, precio base y tiempos de llegada sin confirmar. El copy los marca [C].
  - GBP PENDIENTE. Sin activo de ubicación ni LSA hasta tener acceso.
  - Competidores sin datos de pago en Semrush (copies y gasto s/d).
---

# Estrategia Google Ads — Jump Towing LLC

## Resumen ejecutivo
- **1 campaña Search** ("Towing & Roadside") con **7 ad groups**: 4 de towing y 3 de roadside, 2 de ellos condicionales. Se construye **dentro de la cuenta existente 220-410-9619** para conservar el historial. La campaña actual (Maximizar clics + broad + ad group en español) se pausa el día del lanzamiento.
- **Presupuesto**: $825/mes → **$31/día**, con anuncios solo lun–sáb en horario del cliente (≈26.5 días activos/mes).
- **Puja**: Maximizar conversiones sin tCPA. La conversión principal es la **llamada de ≥60 s** (activo de llamada + número de reenvío en la web).
- **CPL objetivo F1**: **$21–$31**, que es la mediana de Search del benchmark ($25.98) ±20%. Se esperan ~20–32 llamadas calificadas/mes. Es un objetivo provisional hasta tener el CPL máximo del cliente.
- **tCPA**: no antes del **día 60–90**, y solo con ≥30 conversiones calificadas en 30 días. Lo más probable con este presupuesto y horario es que no se alcance (ver Riesgos).

## Campañas
| Campaña | Objetivo | Presupuesto/día F1 | % | Puja inicial | Geo | Horario |
|---|---|---|---|---|---|---|
| Search \| Towing & Roadside \| 10mi \| v1 | Llamadas ≥60 s | $31 | 100% | Maximizar conversiones (sin tCPA) | **Presencia**, radio 10 mi en (45.093312, -93.343931). Excluir resto de países | Lun–vie 6:00–18:00, sáb 6:00–15:30, dom off (America/Chicago) |
| ~~Marca~~ | — | — | — | — | — | No en F1: "jump towing" (20/mes) se confunde con el genérico "jump start towing" y nadie puja por la marca (s/d) |
| LSA (pista paralela) | Llamadas | Presupuesto aparte, a definir | — | — | 10 mi | Igual al horario |

**Por qué una sola campaña:** la regla de aprendizaje pide ≥3× CPL/día por campaña, es decir $78/día. Con $31/día no alcanza ni para una campaña, así que se consolida todo en una y la prioridad entre towing y roadside se maneja por ad group, no por presupuesto. El brief pide "ambos por igual", así que no hace falta proteger presupuesto entre servicios. El cuartil superior del benchmark (CPL $8–$13) usa exactamente esta estructura: una campaña "Radius" con Maximizar conversiones y Presencia.

**Por qué el horario no lleva margen:** el estándar es horario comercial + margen, pero nadie contesta fuera de horario (brief). Una llamada pagada que no se atiende es desperdicio puro. Solo se amplía si el cliente pone a alguien a contestar noches o domingo (pendiente en brief).

**Configuración fija (estándares PMM):**
- Solo red de Búsqueda: sin socios, sin Display.
- Recomendaciones automáticas apagadas. Rotación optimizada.
- Sin exclusiones de audiencia. Idioma inglés.
- Todos los dispositivos. Ajuste de puja en móvil: ninguno, Maximizar conversiones lo gestiona.

## Estructura por campaña
### Campaña: Search | Towing & Roadside | 10mi | v1
Volúmenes: Semrush US (ciudad) o estimación near-me × 0.18%. Detalle en `data/keywords.csv`.

| Ad group | Keywords (match) | Vol. est./mes | Landing | H1 pinneado |
|---|---|---|---|---|
| **T1 Towing Near Me** | [towing near me], [tow truck near me], [towing company near me], "towing near me", "tow truck near me", "towing company near me", "towing service near me", "emergency towing near me", "towing service", "tow truck service", "towing company", "car towing", "tow service", "flatbed towing near me" [C] | ~560 (est.) | /towing (PENDIENTE) | Tow Truck Near You / Towing Service Near You |
| **T2 Towing Brooklyn Park** | [towing brooklyn park mn], [tow truck brooklyn park], "towing brooklyn park", "tow truck brooklyn park" | ~80 | /towing-brooklyn-park (ideal) o /towing | Towing in Brooklyn Park, MN / Brooklyn Park Tow Truck |
| **T3 Towing Minneapolis** | [towing minneapolis], [tow truck minneapolis], "towing minneapolis", "tow truck minneapolis", "car towing minneapolis", "flatbed towing minneapolis" [C], "cheap towing minneapolis", "24 hour towing minneapolis" | ~800 (solo una parte cae en el radio) | /towing | Towing in Minneapolis, MN / Minneapolis Tow Truck |
| **T4 Towing Ciudades NW** | "towing maple grove", "towing plymouth", "towing coon rapids", "towing crystal", "towing brooklyn center", "towing fridley", "towing new hope", "towing robbinsdale", "towing champlin", "towing osseo" (+ variante "tow truck <ciudad>") | ~140 | /towing (+ bloque de área de servicio) | Towing in the NW Metro |
| **R1 Jump Start** | [jump start service near me], "jump start service near me", "car jump start", "jump start minneapolis", "battery jump service", "i need a jump", "roadside assistance minneapolis" | ~30 | /jump-start (PENDIENTE) | Car Jump Start Service / Dead Battery? Get a Jump |
| **R2 Lockout** [condicional] | [car lockout service near me], "car lockout service near me", "locked out of car", "car lockout minneapolis", "car unlock service" | ~30 | /car-lockout (PENDIENTE) | Car Lockout Service / Locked Out of Your Car? |
| **R3 Tire & Fuel** [condicional] | "flat tire service near me", "roadside tire change near me", "gas delivery near me", "ran out of gas" | ~30 | /flat-tire-fuel (PENDIENTE) | Flat Tire Help Near You / Out of Gas? We Bring Fuel |

Por qué T3 va separado: "towing/tow truck minneapolis" suman 530/mes, más de los 100/mes que pide un grupo propio por ciudad, y necesitan H1 con "Minneapolis". Con Presencia a 10 mi solo entra el norte de la ciudad.

Por qué T4 va agrupado: todas las ciudades tienen <100/mes (0–30). No se fuerza SKAG.

Por qué no hay ad group "Emergency/24-7": el cliente no es 24/7. "emergency towing" entra en T1 con copy de horario real; un grupo propio prometería algo que no se cumple.

Negativas específicas por grupo (cruzadas, para que cada búsqueda caiga en su grupo):
- **T1**: brooklyn park, minneapolis, maple grove, plymouth, coon rapids, crystal, fridley, brooklyn center, new hope, robbinsdale, champlin, osseo, jump, lockout, locked, tire, gas, fuel.
- **T2 / T3 / T4**: jump, lockout, tire, gas, fuel. Además T3 excluye las ciudades de T2/T4 y T4 excluye brooklyn park y minneapolis.
- **R1–R3**: towing, tow truck, tow, más los términos de los otros R (R1 excluye lockout/tire/gas, etc.).

## Keywords descartadas y por qué
| Keyword | Vol. | Motivo |
|---|---|---|
| minneapolis impound / impound lot minneapolis | 590 / 260 | Navegacional: lote municipal |
| heavy duty / semi truck towing (near me, minneapolis) | 1,900 / 1,300 nac. | No ofrece heavy-duty |
| cash for junk cars / junk car removal minneapolis | 40 / 10 | Otro servicio |
| motorcycle towing minneapolis | 20 | PENDIENTE confirmar servicio |
| roadside assistance near me | 33,100 nac. | Mezcla membresías y aseguradoras (AAA, State Farm). Solo entra la versión con ciudad, en R1 y con negativas |
| jump towing | 20 | Ambiguo marca/genérico; sin campaña de marca en F1 |
| marcas de competidores | — | Regla PMM: no pujar salvo prueba controlada |
| cualquier término en español (grúa, grúas) | — | El ad group en español actual gastó ~$55 con 1 conversión y no hay mercado hispano relevante en el radio |

Lista completa: `data/negatives-nicho.txt`, con la universal PMM a nivel de cuenta más ~140 términos de nicho, área y competidores.

## Copy
En `data/ads-search-towing-roadside.md`: 15 headlines por ad group (3–5 propios pinneados en H1 + pool común), 6 descripciones (4 por grupo), 3 RSA por grupo (ángulos local, rapidez y precio) y las extensiones.
- Ángulos tomados del gap de competencia:
  - **Operador local real**: "Based in Brooklyn Park, MN", frente a los sitios lead-gen sin dirección.
  - **Solo vehículos livianos**: "Cars, SUVs & Light Trucks".
  - **Precio claro** [C]: "Local Tows From $XX". Ningún competidor publica precio.
  - **Horario real visible**: "Open Mon-Sat From 6 AM". Anunciarlo filtra a quien busca a medianoche.
- Prohibido: "24/7", número de reseñas o años, tiempos de llegada concretos (hasta que se confirmen).

## Landings requeridas
| URL | Existe | Responsable | Bloqueante |
|---|---|---|---|
| jumptowing.com (home) | Sí (sin auditar) | PMM (tiene acceso) | **Sí**: correr /audit-landing desde un entorno con acceso |
| /towing (T1, T3, T4) con H1 "Towing in Brooklyn Park & the NW Metro", clic para llamar arriba, área de servicio y horario | PENDIENTE | PMM | **Sí** |
| /towing-brooklyn-park (T2) | PENDIENTE | PMM | No (T2 puede ir a /towing en F1) |
| /jump-start (R1) | PENDIENTE | PMM | Sí para activar R1 |
| /car-lockout (R2) | PENDIENTE | PMM | Sí para activar R2 (y confirmar servicio) |
| /flat-tire-fuel (R3) | PENDIENTE | PMM | Sí para activar R3 (y confirmar servicio) |

Requisitos mínimos por landing (estándar 11):
- Botón de llamada fijo en móvil, con el número de reenvío de Google.
- Formulario corto como secundario.
- Horario visible.
- Prueba social: reseñas de GBP cuando existan.
- Carga en móvil <3 s.

## Presupuesto por fase
| Fase | Total/mes | Por campaña | Condición para pasar |
|---|---|---|---|
| **F0 — Saneamiento y tracking** (ya) | Decisión Jhombis: pausar la campaña actual o corregirla en caliente | — | Conversión de llamada ≥60 s probada con Tag Assistant; teléfono de reenvío; landing /towing aprobada en audit; negativas universales + nicho aplicadas |
| **F1 — Lanzamiento** (días 1–30) | $825 | $31/día (100%). R2/R3 pausados si no están confirmados | ≥14 días y ≥10 conversiones; search terms revisados día 7 y 14 |
| **F2 — Optimización** (días 31–60) | $825 | Igual. Pausar ad groups con gasto ≥2× CPL objetivo ($62) y 0 conversiones | CPL ≤ $31 sostenido 30 días |
| **F3 — Escala o tCPA** (días 61–90) | $825 → propuesta $1,100–1,200 si el IS perdido por presupuesto es >40% y CPL ≤ objetivo | tCPA = CPL real 30d ×1.1 **solo** si hay ≥30 conversiones/30d | ≥30 conv/30d con tracking confiable |
| **F4 — RLSA** | — | Baja prioridad: en towing la compra es urgente y no se repite. Solo como ajuste de observación | Listas ≥1,000 usuarios |
| **F5 — PMax** | — | Ver "Por qué NO" | Condiciones de `knowledge/estrategias/pmax-cuando-y-como.md` |
| **LSA** (paralelo desde F0) | Aparte del $825, a definir | — | GBP verificado + seguro + background check (2–4 semanas) |

Nota sobre el presupuesto diario: con $31/día y solo ~26.5 días activos, el gasto esperado es ~$820/mes. Google puede gastar hasta 2× en un día, pero respeta el tope mensual de 30.4× el diario ($942). Hay que vigilar la semana 1 para que no se pase de $825.

## Por qué NO (todavía)
- **PMax**: requiere Search estable, 30+ conversiones/mes con tracking confiable, assets propios y exclusión de marca. Hoy no hay ni tracking verificado ni GBP. En el benchmark, 5 de las 7 cuentas del cuartil superior tienen PMax, pero madura (4–18 meses). Se reevalúa en F5.
- **Amplia**: domina en el MCC, pero es justamente lo que tiene la cuenta actual de Jump: CPL $65.57 y search terms de Iowa, Dakota del Sur y competidores. Phrase + exacta hasta tener tCPA maduro y la aprobación de Jhombis.
- **Display / Video / Demand Gen**: el remolque es una necesidad inmediata y no se crea demanda.
- **Campaña de marca**: no hay búsquedas de marca medibles. Se agrega en exacta si aparece "jump towing llc" o similar en search terms.
- **Ad group en español**: no hay mercado. Se elimina.
- **Maximizar clics**: las 4 cuentas del MCC que lo usan tienen CPL de $65–$78. Solo se usaría como fallback si la conversión de llamada no estuviera verificada, y en ese caso no se lanza (estándar 7).

## Riesgos y supuestos
1. **El horario recorta la demanda.** Los 6 competidores son 24/7. Jump renuncia a noches y domingos, donde se concentra buena parte del remolque de emergencia. Esto limita las conversiones/mes y hace improbable llegar a tCPA con $825. Es el mayor techo de la cuenta y una decisión del cliente.
2. **El CPL real será mayor que el benchmark.** El benchmark cuenta llamadas sin calificar (algunas de 20 s). Medir llamadas ≥60 s es más honesto y sube el CPL. Si F1 sale en $35–45 con llamadas que sí cierran, puede seguir siendo rentable; depende del ticket (PENDIENTE).
3. **CPL máximo sin calcular.** Ejemplo ilustrativo, no cifra del cliente: ticket de $125, margen del 50% y cierre del 60% dan un CPL máximo ≈ $11 (con el factor 0.3 del brief). Con ese margen el objetivo de $21–31 sería **no rentable**, así que esto es bloqueante para validar el objetivo.
4. **CPC real 2–3× Semrush.** El CPC real de Jump ya es $6.56 frente a $3–4 en Semrush. Con $31/día salen ~4–5 clics/día.
5. **Sin GBP**: sin activo de ubicación, sin Maps, sin LSA, sin prueba social. Los competidores tienen 153–387 reseñas.
6. **Landing sin auditar**: si jumptowing.com no cumple el estándar 11, F1 no arranca.
7. **Campaña actual gastando** con broad, Maximizar clics y geo dudosa. Cada semana que siga así es desperdicio medible: ~$190/semana a CPL $65.
