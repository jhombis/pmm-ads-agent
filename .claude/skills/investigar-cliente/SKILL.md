---
name: investigar-cliente
description: Onboarding SIN preguntas. Recibe la URL del cliente y/o su cuenta en el MCC (ID o nombre) e investiga solo las preguntas del brief en la web, la cuenta de Google Ads, Semrush y Windsor. Escribe brief.md con la fuente de cada dato y deja PENDIENTE solo lo que no se puede averiguar. Usar cuando se diga "investiga el cliente", "investigar-cliente", "arma el brief sin preguntarme", "saca todo del MCC/la página".
---

# /investigar-cliente — Brief investigado, no entrevistado

Alternativa a `/onboard`: produce el **mismo `brief.md`** (mismas secciones, mismo formato) pero sin entrevistar a Jhombis. Cada dato lleva su fuente; lo que no aparece en ninguna fuente queda `PENDIENTE` y se lista al final en un solo bloque.

## Entrada
`/investigar-cliente <url> [cuenta]` donde cuenta es el Customer ID (con o sin guiones) o parte del nombre de la cuenta en el MCC. Basta con uno de los dos:
- Solo URL → buscar la cuenta en el MCC por dominio/nombre (paso 2).
- Solo cuenta → sacar la URL de las `final_urls` de sus anuncios.
- Si Jhombis pega además un texto/correo del cliente, úsalo como fuente `(cliente)`.

## Reglas
- **No hagas preguntas durante la investigación.** No uses AskUserQuestion. Si algo falta, se marca y se sigue.
- **Nunca inventes.** Cada dato lleva una etiqueta de fuente: `(web)`, `(MCC)`, `(Semrush)`, `(Windsor)`, `(GBP)`, `(cliente)`, o `(inferido: <razón en pocas palabras>)`. Lo que no tiene respaldo queda `PENDIENTE`.
- Un **inferido** debe salir de datos, no de suposiciones del nicho. Ejemplo válido: "servicio estrella: flatbed towing (inferido: 62% del gasto y 70% de las conversiones en 12 meses)". Ejemplo inválido: "ticket promedio $150 (inferido: típico de towing)". Eso último es PENDIENTE; el rango del nicho puede ir en una nota aparte, rotulado como referencia.
- Si una fuente no está disponible (sin `google-ads.yaml`, red bloqueada, Semrush sin autorizar), **dilo en el brief** en `## Fuentes consultadas` y sigue con las demás.
- Paraleliza: web, MCC y Semrush son independientes; lánzalos con subagentes o llamadas paralelas.
- Guarda los datos crudos en `clients/<slug>/data/` para que otros skills no tengan que volver a pedirlos.

## Pasos

### 1. Carpeta
Slug con la regla de `/onboard` (minúsculas, guiones, sin tildes). Si `clients/<slug>/` no existe, cópiala de `clients/_template/`. Si ya existe un `brief.md`, **no lo pises**: completa solo los campos PENDIENTE y anota la fecha.

### 2. MCC (Google Ads API; si no hay, Windsor)
1. Localizar la cuenta: `python scripts/mcc_accounts.py --buscar "<nombre o dominio sin TLD>"`. Si hay varias coincidencias, elegir la que tenga `final_urls` con el dominio del cliente; si sigue ambiguo, registrar las candidatas y usar la de más gasto.
2. Perfil completo: `python scripts/account_profile.py --customer <id> > clients/<slug>/data/account-profile.json`. Si la cuenta tiene poco historial, correr también `--dias 730`.
3. Sin API → Windsor (`google_ads`): gasto, clics y conversiones por mes y por campaña, keywords, search terms y landings de los últimos 12 meses. Guarda el resultado en `data/windsor-*.json`.
4. Sin cuenta en el MCC → "Historial Google Ads: no hay cuenta en el MCC de PMM", y los datos se sacan de la web y de Semrush.

Qué sale del MCC:
| Campo del brief | Dónde mirar en account-profile.json |
|---|---|
| Nombre, moneda, zona horaria | `cuenta` |
| País | moneda y zona horaria + `geo` |
| Área de servicio | `geo` (ubicaciones, radios, exclusiones). Anotar si usa Presencia o "Presencia o interés" (`positive_geo_target_type`) |
| Servicios y prioridad | gasto y conversiones por campaña, ad group y keyword (`campanas`, `keywords_top`) |
| Servicio estrella | el de mejor volumen de conversiones con CPL aceptable |
| Servicio a evitar | el de mucho gasto y 0 conversiones, o términos que el cliente ya negativizó. Siempre como inferido |
| Presupuesto mensual | promedio de `historial_mensual` de los últimos 3 meses + presupuestos diarios activos × 30.4 |
| Historial | `historial_mensual` + `campanas` (estado, puja, tCPA, redes) → qué pasó, en 3 líneas |
| CPL histórico | costo / conversiones, pero solo si las conversiones son confiables (ver `conversiones`) |
| Horario / 24-7 | `horarios` (sin programación = 24/7 en Ads, lo que no prueba que atiendan 24/7) |
| Teléfono / call tracking | `extensiones` CALL + `conversiones` de tipo llamada |
| Diferenciadores y ofertas | `extensiones` (callouts, snippets, sitelinks) + textos de `anuncios` |
| Tracking | `cuenta.conversion_tracking_status` + `conversiones` (cuáles son primarias y si registran algo) |
| Búsqueda de marca | `search_terms_top` con el nombre del negocio: impresiones y conversiones |
| Landings usadas | `landings` |
| Competidores | términos con nombres de competidores en `search_terms_top` |

### 3. Web del cliente
1. `python scripts/site_scan.py <url> --max 20 > clients/<slug>/data/site-scan.json`. Si falla por red, usar WebFetch en la home y en las páginas de servicios. Si ambos fallan, anotar "red bloqueada": el entorno necesita Network access en Full o el dominio en la lista permitida.
2. Qué sale de la web:
   - Servicios: H1/H2 y URLs de páginas de servicio.
   - Ciudades: páginas por ciudad, `areaServed` del JSON-LD, footer.
   - Teléfono, WhatsApp, email, dirección: `tel:`, `wa.me`, `mailto:`, JSON-LD.
   - Horario: `openingHours` del JSON-LD o el texto "24/7".
   - Diferenciadores y ofertas: `frases_confianza_oferta`.
   - Prueba social: `aggregateRating` y widgets de reseñas.
   - Formulario: cuántos campos tiene y su `action`. La plataforma (WordPress, Elementor, Wix…) se deduce de las rutas `wp-content` y de los meta generator.
   - Tracking: los IDs `G-`, `AW-`, `GTM-`, Meta Pixel y CallRail.
   - Idioma: `lang` del HTML y el idioma del texto.
   - Requisitos de política: licencia visible (número de licencia, "licensed & insured").
3. Si hay `PAGESPEED_API_KEY`: `python scripts/pagespeed.py <url> --strategy mobile` → guardar en `data/pagespeed.json` (lo reutiliza /audit-landing).

### 4. Semrush (si está autorizado)
- `domain_overview` del dominio: tráfico orgánico y de pago, y si ya se anuncia fuera del MCC.
- `keyword_research` del nombre de marca: volumen mensual → "búsqueda de marca sí/no".
- `competitors_research` (orgánico y pago) → 3–5 competidores con URL. Se marcan `(Semrush)`, no "reconocidos por el cliente".
- Keywords del nicho × ciudad principal: volumen y CPC como referencia del presupuesto.

### 5. Google Business Profile
Windsor `google_my_business` si la ficha está conectada. Si no, el JSON-LD o el widget de reseñas de la web. Datos a sacar: verificado, número de reseñas y promedio. El acceso de PMM a la ficha queda PENDIENTE salvo que Windsor lo confirme.

### 5b. Call tracking (CallFire / CallRail)
Busca el negocio en CallFire (`callfire_get` con path `/numbers/leases`, paginando con `offset`; la etiqueta es el nombre del negocio) y en CallRail (`callrail_list_companies` + `callrail_list_trackers`). Si aparece:
- Anota en el front matter `call_tracking`, `tracking_number` y el destino `(CallFire)`/`(CallRail)`.
- Exporta 90 días de llamadas a `data/` y corre `scripts/call_summary.py`. Con eso se responden con dato las preguntas de capacidad de respuesta (tasa de contestadas), horario real y volumen de llamadas (ver `knowledge/call-tracking.md`).

Si no aparece, la pregunta va al bloque de preguntas para el cliente.

### 6. LSA (solo US)
Decide si la categoría califica según el nicho. Licencia y seguro, desde la web. La disposición al background check queda siempre PENDIENTE.

### 7. Lo que casi nunca se puede investigar
Déjalo PENDIENTE salvo que haya fuente directa:
- ticket promedio y margen
- capacidad de atención
- quién responde los leads y en cuánto tiempo
- CRM
- el servicio que más quiere vender el dueño, si difiere de lo que ya convierte
- ofertas que puede sostener, si difieren de las publicadas
- presupuesto futuro y margen para escalar

**CPL máximo aceptable**: calcular solo si hay ticket y margen. Si no los hay, poner `PENDIENTE` y, como referencia rotulada, el CPL histórico de la cuenta y la mediana de `knowledge/benchmarks/<nicho>-<pais>.md` si existe.

## Salida: `clients/<slug>/brief.md`
Usa exactamente la plantilla de salida de `.claude/skills/onboard/SKILL.md`, con estos cambios:
- Front matter: añade `origen: investigar-cliente`, `customer_id: <id|ninguno>` y `completitud: NN%` (campos con dato / total de campos).
- Cada valor termina con su etiqueta de fuente.
- Añade al final:

```markdown
## Fuentes consultadas
| Fuente | Estado | Archivo |
|---|---|---|
| Google Ads API (cuenta <id>) | ok / sin credenciales / sin cuenta | data/account-profile.json |
| Web (N páginas) | ok / red bloqueada | data/site-scan.json |
| PageSpeed | ok / sin clave | data/pagespeed.json |
| Semrush | ok / sin autorizar | — |
| Windsor | ok / no usado | data/windsor-*.json |

## Hallazgos que ya importan para la estrategia
- 3–6 bullets: desperdicio visible en search terms, geo en "Presencia o interés", conversiones mal configuradas, landing sin tag, etc.

## Preguntas para el cliente (solo lo que no se pudo investigar)
Agrupadas y listas para copiar en un correo o WhatsApp, en el idioma de Jhombis. Máximo 8 y ordenadas por bloqueo: primero las que impiden calcular el CPL máximo o lanzar.
```

Los pendientes bloqueantes van también a `## Pendientes` del brief y a `checklist.md`.

## Al terminar
Resume en 5 líneas:
- nicho, geo y presupuesto (con su fuente)
- CPL histórico vs CPL máximo, o PENDIENTE
- % de completitud
- los 2–3 hallazgos más caros
- cuántas preguntas quedan para el cliente

Siguiente: `/audit-landing` (ya tiene site-scan y pagespeed en `data/`), `/competitors` y `/benchmark-interno` en paralelo.
