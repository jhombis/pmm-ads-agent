---
cliente: Precision Towing
slug: precision-towing
pais: US
idioma: EN
nicho: towing
mcc_customer_id: 753-255-2245
actualizado: 2026-10-06
estado: brief-completo
---

# Brief — Precision Towing

> Brief cerrado el 2026-09-29 con Jhombis; historial de la cuenta actualizado el 2026-10-06 con datos de Windsor hasta el 2026-10-05 (ver `log/2026-10-06-diagnose.md`). Fuentes: entrevista, fetch de precisiontowingca.com, Windsor.ai (cuenta 753-255-2245) y búsqueda web. Lo marcado PENDIENTE requiere respuesta del cliente; los bloqueantes están en Pendientes al final.

## Negocio
- URL: https://precisiontowingca.com/
- Razón social / nombre real: **Precision Automotive, Paint & Collision & Towing** (Precision Automotive Inc.). "Precision Towing" es la marca usada en Ads. **El sitio para Ads es precisiontowingca.com** (confirmado por Jhombis). El cliente tiene además precisionautomotiveus.com para el taller; no se usa como landing y solo sirvió como fuente de datos (dominio bloqueado desde esta sesión).
- Dirección física: 5212 Lake Isabella Blvd, Lake Isabella, CA 93240 (Kern County). Taller de 17 bahías + towing bajo el mismo techo.
- Comunidades que declara atender (sitio principal): Lake Isabella, Kernville, Weldon, Bodfish, Wofford Heights, Mountain Mesa, Walker Basin, Twin Oaks. Coincide con el radio de 21 mi.
- Base y área de servicio (según Jhombis, geotargets a replicar en Google Ads):
  - Radio 21 mi alrededor de Lake Isabella, CA (5212 Lake Isabella Blvd)
  - Radio 8 mi en punto custom 35.674769, -118.033108 (zona Lake Isabella / Kern River Valley)
  - Radio 8 mi en punto custom 35.739446, -118.936733 (punto rural ~40 km al norte de Bakersfield, zona Woody/Glennville sobre la Hwy 155, la vía de acceso al lago desde el oeste)
  - Mercado rural, muy poco denso. Esperar volumen bajo: agrupar por tema, no forzar SKAG.
- Servicios (por prioridad del cliente):
  1. Light & Medium-Duty Towing (estrella)
  2. 5th Wheel Towing
  3. Travel Trailer Towing
  4. Roadside Assistance
  5. Auto Repair & Collision Service
- Servicio estrella: Light & Medium-Duty Towing.
- Servicio a evitar: ninguno declarado explícitamente por el cliente. Auto Repair & Collision queda último en prioridad; por defecto no se le asigna campaña propia en fase 1.
- Diferenciadores (del sitio): 33 años en Lake Isabella; despacho directo por el propio equipo, sin call center ni dispatch de terceros; taller de 17 bahías y colisión en el mismo lugar; "After-Hours Emergency Towing"; conocimiento local de las carreteras (Kern River, Hwy 178/155).
- Sellos verificables (sitio principal y directorios): **AAA Approved Auto Repair Facility**, **NAPA AutoCare Center**, **California Gold Seal Smog Check Station**. El sitio principal promete "towing 24 hours a day / 7 days a week". Ninguno de estos sellos aparece en la landing precisiontowingca.com: sumarlos a callouts, snippets y landing.
- Ofertas sostenibles: "Get A Free Quote" (cotización gratis) es lo único visible en el sitio. Confirmar con el cliente otras (bloque 4).
- Búsqueda de marca: PENDIENTE (bloque 4). Nota: reseñas mencionan "Precision automotive", posible nombre alterno del taller.
- Idioma del mercado: inglés (US). Sin contenido en español en el sitio.

## Objetivo y economía
- Objetivo primario: **llamadas**. El formulario de /schedule-a-tow/ queda como conversión secundaria (hoy solo genera 7 de 36 conversiones).
- Presupuesto mensual: **$825 USD** de pauta. Margen para escalar: PENDIENTE. Nota: la cuenta en el MCC se llama "Premium Local Listings 004040 ($1500 Precision Towing)" y las campañas dicen "$1500/mo"; confirmar si $1500 es el fee total del cliente y $825 la pauta neta.
- Ticket promedio / margen: PENDIENTE (Jhombis no lo tiene; pedir al cliente ticket de light-duty tow local, 5th wheel y travel trailer).
- Capacidad (leads o trabajos/mes): PENDIENTE (preguntar al cliente cuántos camiones y conductores tiene).
- **CPL máximo aceptable**: PENDIENTE hasta tener ticket y margen. Referencia provisional: CPL observado de $37 en Search (ver abajo). Fórmula al tener datos: margen por trabajo × tasa de cierre × 0.3.
- Historial Google Ads (cuenta 753-255-2245; Windsor.ai, 2026-08-14 → 2026-10-05; exports en `data/history-*.csv` y diagnóstico en `log/2026-10-06-diagnose.md`):
  - Cuenta nueva: primera campaña activa el **14/08/2026**. 53 días de datos.
  - Gasto total $1.484 (Search $1.332 + PMax $152) ≈ $28/día ≈ $850/mes. **Presupuesto diario configurado $32** (tope mensual $973), por encima de los $825 pactados.

  | Campaña | Tipo | Puja | Estado | Gasto | Clics | Impr. | Conv. | CPC | CPL | IS Search |
  |---|---|---|---|---|---|---|---|---|---|---|
  | ENHPRM Radius (14/08) | Search | Max. conversiones, sin tCPA | Activa, $32/día | $1.332 | 87 | ~690 | 31 | $15,31 | **$43,0** | 35% últ. 7 d (50% acumulado) |
  | P. Max (04/09) | PMax | Max. conversiones | Pausada, $5/día; gastó $25 entre 09-22 y 10-05 | $152 | 77 | 3.382 | 9 | $1,97 | $16,9 | — |

  - Search: CVR 35,6% (llamadas). **Tendencia**: CPC $5–8 del 31/08 al 20/09; $24,14 del 22/09 al 05/10 (últimos 7 días: $283, 11 clics, 3 conv, CPL $94). Es Max. conversiones sin tope en una subasta de 70 impresiones por semana.
  - Conversiones primarias: "Calls from Ads" 32 + "Website Calls" 7 (tag AW-18347302928) + **"Form Fill" 1 (acción creada entre el 29/09 y el 05/10, origen por verificar; el sitio sigue sin página de gracias)**. Secundarias: Clicks to call 10, acciones locales 16. Total primarias 40 → ~23/mes.
  - Estructura actual: 1 campaña Search con 2 ad groups y **107 keywords, todas en amplia** (no 22: el export por rendimiento solo mostraba las que imprimieron). Incluye `b&d towing` y `b&m towing` como keywords positivas (viola el estándar 5), `towing 24 hours near me`, 7 variantes de boat towing, motorhome, toy hauler y cargo trailer. ~400 negativas de campaña ya cargadas, entre ellas **la marca propia** (`precision`, `precision automotive`, [precision towing], [precision automotive lake isabella]) y `[flat tire service]` en exacta. Sin programación de anuncios (sirve 24/7 aunque el cliente atiende 7–22). Dispositivos: 97% móvil.
  - Keywords que rinden (53 d): "tow truck" ($402, 10,5 conv), "kernville towing" ($128, 6), "towing near me" ($292, 5), "towing lake isabella" ($108, 4), "car towing" ($95, 2,5). "lake isabella towing" en amplia: $136, 0 conv.
  - Desperdicio en search terms (sobre $476 rastreables de $1.332): competidores $144 (30%), taller $72 (15%: "starter and alternator repair near me" $65), 24 h $16, compra RV $15, precio $6. Neto 53%. Marca propia $67 con 2 conv (no es desperdicio; va a su grupo).
  - PMax se lanzó a los 20 días de vida (contra el estándar 9) y está pausada; no borrarla.
  - Competidor principal detectado por búsquedas: **B&D Towing (Lake Isabella)**, 6+ variantes del nombre en search terms; nueva esta semana: "gomez towing near me".

## Operación
- Horario / 24-7: **Lunes a domingo 7:00 AM – 10:00 PM** (dato de Jhombis, coincide con formato de Google Business Profile). El sitio dice 8 AM – 8 PM (sin cambios al 2026-10-06) y "After-Hours Emergency Towing Available": inconsistencia a corregir. La campaña actual **no tiene programación** (sirve 24/7). Propuesta: 6:30–22:30 todos los días **en la zona horaria de la cuenta** (`customer.time_zone`, PENDIENTE verificar en la UI; Windsor no la expone). Fuera de esa franja PENDIENTE confirmar si alguien contesta.
- Respuesta a leads (quién, tiempo): PENDIENTE con el cliente. El sitio afirma que atiende el propio equipo (nombres en reseñas: Wes/West Miller, Carolyn en recepción, conductores Matthew y Leroy).
- Teléfono / call tracking: **sí tiene call tracking**. El (760) 606-4160 de la landing es el número de reenvío; el número real del negocio es **(760) 379-6222** (sitio principal, GBP y directorios). En Ads usar siempre el de tracking; en el activo de ubicación se verá el del GBP.
- CRM (solo referencia): PENDIENTE con el cliente
- GBP: perfil "Precision Automotive, Paint & Collision & Towing", **4,8 estrellas con ~850 reseñas** según búsqueda web (verificar en Maps). Acceso de PMM y vinculación a Ads: PENDIENTE. Ojo: el horario publicado en directorios es L–V 7:30 AM–5 PM (horario del taller) mientras Jhombis reporta 7 AM–10 PM diario; unificar en GBP antes de activar el activo de ubicación.

## Competencia
| Competidor | URL | Nota |
|---|---|---|
| B&D Towing | yelp.com/biz/b-and-d-towing-lake-isabella-3 | Principal. 4112 Perdue Ave, Lake Isabella, 24 h, desde 2012, 4x4 off-road recovery. 6 variantes de su nombre en search terms de la cuenta. |
| Lake Isabella Towing | https://www.lakeisabellatowing.us/ | Sitio de dominio genérico "24/7", (760) 474-6825. Probable lead-gen. |
| Nitro Towing | PENDIENTE | Aparece en search terms con 1 clic. |
| B&M Towing | PENDIENTE | Aparece en search terms con 1 clic. |
| A&A Towing and Service | PENDIENTE | Listado en directorios de Lake Isabella. |
| Kern Valley Auto Body & Towing | PENDIENTE | Listado en directorios; también compite en colisión. |
| Ibarra's Towing | PENDIENTE | Aparece en search terms sin clic. |

Lista confirmada por el cliente: PENDIENTE (no la conoce Jhombis). /competitors debe validar URLs y descartar los que no anuncian.

## Web y tracking
- Plataforma / quién edita: WordPress + Elementor en precisiontowingca.com. Propietario y quién edita: PENDIENTE con el cliente (no es de PMM según Jhombis). **Alternativa sin depender del cliente (2026-10-06)**: PMM puede montar landings propias por servicio con `/landing-ghl` (GoHighLevel) o en Leadpages (cuenta de PMM conectada, plan Grow, 2 páginas de otro cliente ya publicadas), con formulario corto, página de gracias y conversión propias. Es la vía recomendada si el acceso no llega en la semana del 2026-10-06.
- Tag/GA4: GTM-NWQH4MVX instalado (contenedor GTM) y gtag de Google Ads AW-18347302928 (propio de la cuenta 753-255-2245). GA4 no visible en el HTML de la home (puede estar dentro de GTM). Acceso a GTM: PENDIENTE con el cliente.
- Formulario → destino: en la cuenta de Ads apareció la acción "Form Fill" (1 conv entre el 29/09 y el 05/10) sin que exista página de gracias ni redirect: PENDIENTE verificar sobre qué evento dispara. Formulario Elementor en /schedule-a-tow/ con campos Name, Phone, Email, Vehicle Year/Make/Model, Service Needed, Pick Up Location, Drop Off Location, Desired Date/Time, Comments (9 campos, largo para una emergencia). Destino probable: amirepair22@gmail.com (email visible en la página). PENDIENTE confirmar con el cliente. Tras enviar aparece popup "Your Booking Is Not Yet Confirmed — Please give us a call": el formulario no cierra la venta solo, el teléfono es la conversión principal.
- Home sin formulario: la home solo tiene CTA "Get A Free Quote" → /schedule-a-tow/ y "Call Now". Sin meta description. Candidato a bloqueante en /audit-landing: landing de towing de emergencia sin formulario corto arriba del pliegue.
- Requisitos de política: towing en California opera bajo permiso de CHP (motor carrier permit / CHP tow rotation). No es restricción de política de Google Ads, pero conviene mostrar licencia y seguro en la landing. Licencia y rotación CHP: PENDIENTE con el cliente. Sellos AAA/NAPA/Gold Seal sí son usables ya.

## LSA (solo US)
- Aplica: PENDIENTE — towing es categoría elegible en LSA en US y el cliente está en California, pero no se sabe si tiene licencia, seguro y disposición al background check. Se documenta como fase futura en el roadmap; no bloquea Search.

## Pendientes

**Bloqueantes para lanzar la cuenta reestructurada** (sin esto no se pasa de Fase 0):
- [ ] Acceso de edición a precisiontowingca.com y a GTM-NWQH4MVX, o confirmación de quién aplica cambios de landing
- [ ] Confirmar destino del formulario y crear conversión de formulario (hoy no existe)
- [ ] Ticket promedio y margen por servicio para fijar el CPL máximo (hoy referencia provisional $37)

**Resto:**
- [x] Bloque 1 — Identidad (URL, geo, servicios, idioma)
- [x] Bloque 2 — Objetivo y dinero (ticket, margen y capacidad quedan PENDIENTE con el cliente)
- [x] Bloque 3 — Operación (horario y call tracking confirmados; respuesta a leads, CRM y acceso a GBP quedan PENDIENTE con el cliente)
- [x] Bloque 4 — Competencia y diferenciación (competidores desde búsqueda web y search terms; lista del cliente, licencia CHP y ofertas quedan PENDIENTE con el cliente)
- [x] Bloque 5 — Web y tracking (sitio confirmado; acceso de edición, GTM y destino del formulario PENDIENTE con el cliente)
- [x] Bloque 6 — LSA (PENDIENTE con el cliente, fase futura)
- [x] AW-18347302928 es propio de la cuenta 753-255-2245 (confirmado por Jhombis)
- [ ] Confirmar destino real de los envíos del formulario y el origen de la conversión "Form Fill"
- [ ] Verificar `customer.time_zone` de la cuenta antes de programar anuncios o escribir horas en el copy
- [ ] Confirmar presupuesto diario correcto ($27 = $825/30,4; hoy $32)
- [ ] Unificar horario en la landing (sitio 8–8 vs real 7–10 vs GBP L–V 7:30–5) y aclarar si hay atención fuera de horario
- [ ] Pedir al cliente: quién responde leads y en cuánto tiempo, CRM, acceso a GBP y vínculo con Ads, licencia CHP / motor carrier, ofertas sostenibles, lista de competidores que reconoce
- [ ] Agregar sellos AAA / NAPA / Gold Seal Smog a la landing y a las extensiones
- [ ] Pedir al cliente: ticket promedio y margen por servicio, capacidad (camiones/conductores), margen para escalar presupuesto
- [ ] Confirmar si $1500 es fee total y $825 pauta neta
- [ ] Crear conversión de formulario (hoy no existe) y pasar keywords a concordancia de frase (hoy todo amplia)
