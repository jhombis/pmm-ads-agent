---
name: landing-ghl
description: Diseña landing pages por servicio listas para GoHighLevel (código para pegar en Custom Code + Head Tracking Code, SEO, schema, formulario GHL con gclid/UTM, página de gracias con conversión). Escribe clients/<slug>/landings/<pagina>/. Usar cuando se pida "landing", "crear landing page", "una landing por servicio", "página para GHL/GoHighLevel".
---

# /landing-ghl — Una landing por servicio, lista para GoHighLevel

## Entrada
`/landing-ghl <slug> [servicio|todos] [ciudad]`. Por defecto crea **una landing por cada campaña/servicio de `strategy.md`**, o por cada servicio principal del brief si aún no hay estrategia.

## Requisitos
- `clients/<slug>/brief.md` (obligatorio).
- Si existen, léelos: `strategy.md` (servicios, ad groups, keywords y ofertas), `audit-site.md`, `competitors.md` (qué ofertas no repetir y cómo diferenciarse), `data/site-scan.json` (logo, colores, teléfono, reseñas, licencia) y `data/account-profile.json` (search terms y anuncios que convierten).
- Guía de montaje: `docs/setup-gohighlevel.md`. Plantilla del spec: `knowledge/landing-ghl/spec-ejemplo.json`.

## Reglas
1. **Una página = un servicio (+ ciudad si la estrategia separa por ciudad).**
   - El H1 contiene la keyword principal del ad group, porque así sube el Quality Score y la tasa de conversión.
   - No mezcles servicios en una misma landing.
2. **Idioma del mercado**: inglés para US y español para CO, con el tono del cliente. Los archivos de trabajo y este diálogo, en español.
3. **Nada inventado.** Reseñas, rating, licencia, años, garantía, tiempos de respuesta y ofertas salen del brief, del site-scan o del GBP, y cada reseña lleva su `fuente`. Si un dato no existe, la sección se omite: deja el campo vacío; no escribas "PENDIENTE" en un texto visible. Una oferta que el cliente no confirmó no se publica.
4. **Estándar PMM de landing** (CLAUDE.md, punto 11):
   - headline = término de búsqueda
   - formulario corto (≤4 campos) visible arriba
   - clic para llamar sticky en móvil
   - prueba social, oferta clara y página rápida (el generador no usa librerías y pesa ~12 KB)
5. **SEO**:
   - title de 30–60 caracteres y meta description de 70–160, las dos con la keyword
   - slug `servicio-ciudad`
   - H2 con variaciones semánticas (no repitas la keyword en todos)
   - FAQ con preguntas reales del nicho (search terms informativos de la cuenta, "People also ask")
   - ≥400 palabras únicas por página
6. **Contenido único por página.** Las páginas servicio × ciudad casi idénticas son *doorway pages* y Google las penaliza. Si solo cambia la ciudad, pon `"indexar": false` (sirven para Ads, pero no se indexan) o reescribe intro, FAQ y zona con detalles reales de esa ciudad.
7. **Tracking**:
   - Con GTM del cliente: `tracking.gtm_id`. El generador emite el evento `pmm_lead_form` en la página de gracias.
   - Sin GTM: `google_ads_id` + `conversion_label_form` (+ `conversion_label_call` para clics en `tel:`).
   - Nunca las dos cosas a la vez: se duplicarían las conversiones.
8. **Formulario**: siempre el formulario nativo de GHL (`ghl.form_id`), con campos ocultos `gclid`, `utm_source`, `utm_campaign` y `utm_term`. El código pasa los parámetros de la URL al iframe. Si el cliente usa un dominio white-label para los formularios, pega su código de inserción en `ghl.form_embed_html`.

## Pasos
1. **Inventario de páginas**: lista `servicio → keyword principal → slug → URL final → ¿indexar?` y muéstrala en 1 tabla antes de escribir. Si Jhombis no corrige, sigue.
2. **Spec por página**: copia `knowledge/landing-ghl/spec-ejemplo.json` a `clients/<slug>/landings/<slug-pagina>/spec.json`, borra `_nota` y completa todo. Copy:
   - **Hero**: H1 (keyword + beneficio o velocidad), subtítulo con los problemas concretos del servicio, oferta real y 3 bullets de confianza.
   - **incluye**: 3 sub-servicios o problemas que resuelve. Usa los search terms que convierten.
   - **por_que**: 3 diferenciadores del brief, contra lo que hacen los competidores.
   - **proceso**: 3 pasos.
   - **faq**: 4–6 preguntas que respondan objeciones (precio, tiempo, garantía, cobertura, licencia).
   - **zona**: ciudades reales del área de servicio. El `mapa_embed_url` del GBP va si existe.
   - **gracias**: confirmación, tiempo de respuesta real y teléfono.
   - **marca**: colores del sitio actual (site-scan) o los que indique el brief.
3. **Generar y validar**: `python scripts/landing_build.py clients/<slug>/landings`. Revisa cada `qa.md`:
   - Los bloqueantes sin datos (form_id, privacidad, IDs de conversión) quedan como tareas en `checklist.md`, con responsable.
   - Corrige los avisos que dependan del copy (title, description, palabras) y vuelve a generar.
4. **Revisión visual**: abre `preview.html` en móvil (390 px) y en escritorio con Playwright y haz captura. Chequea:
   - el hero y el CTA de llamada sin scroll en móvil
   - que no haya desbordes
   - que la barra sticky esté visible
5. **Índice**: escribe `clients/<slug>/landings/README.md` con una tabla `página | URL final | keyword | indexar | QA bloqueantes | estado (borrador/montada en GHL/publicada)`.

## Salida por página (`clients/<slug>/landings/<pagina>/`)
| Archivo | Dónde va en GHL |
|---|---|
| `spec.json` | fuente; editar aquí y regenerar, nunca en el HTML |
| `ghl-body.html` | página en blanco → elemento **Custom Code** a ancho completo |
| `ghl-head.html` | página → Settings → **Head Tracking Code** |
| `ghl-seo.md` | página → Settings → SEO Meta Data + path + redirección del formulario |
| `gracias-body.html` / `gracias-head.html` | paso o página de gracias (dispara la conversión) |
| `preview.html` | revisión local; también sirve para hospedar fuera de GHL |
| `qa.md` | checklist automático |

## Al terminar
Resume en 3–5 líneas:
- páginas creadas, cuáles se indexan y cuáles son solo para Ads
- bloqueantes de QA y quién los resuelve
- el siguiente paso: montarlas en GHL siguiendo `docs/setup-gohighlevel.md`, probar el envío con Tag Assistant y luego actualizar las URLs finales en `strategy.md` antes de `/build-campaign`
