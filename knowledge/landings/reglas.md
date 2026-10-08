# Landings PMM — reglas de contenido y pasos comunes

Las usan `/landing` (publica en performancemediamarketing.com vía Plesk) y `/landing-ghl` (GoHighLevel o dominio del cliente). Lo único que cambia entre los dos es `hosting` en el `spec.json` y dónde se publica. El generador es el mismo: `scripts/landing_build.py`. La plantilla del spec es `knowledge/landings/spec-ejemplo.json`.

## Fuentes
- `clients/<slug>/brief.md` (obligatorio).
- Si existen, léelos:
  - `strategy.md`: servicios, ad groups, keywords y ofertas
  - `audit-site.md`
  - `competitors.md`: qué ofertas no repetir y cómo diferenciarse
  - `data/site-scan.json`: logo, colores, teléfono, reseñas, licencia
  - `data/account-profile.json`: search terms y anuncios que convierten
- **Teléfono**: si el brief tiene `tracking_number` (call tracking), la landing muestra **ese** número y no el principal. Así las llamadas desde la landing se miden.

## Reglas
1. **Una página = un servicio** (+ ciudad si la estrategia separa por ciudad). El H1 contiene la keyword principal del ad group, porque así sube el Quality Score y la tasa de conversión. No mezcles servicios en una misma landing.
2. **Idioma del mercado**: inglés para US y español para CO, con el tono del cliente. Los archivos de trabajo y el diálogo, en español.
3. **Nada inventado.**
   - Reseñas, rating, licencia, años, garantía, tiempos de respuesta y ofertas salen del brief, del site-scan o del GBP, y cada reseña lleva su `fuente`.
   - Si un dato no existe, la sección se omite: deja el campo vacío; no escribas "PENDIENTE" en un texto visible.
   - Una oferta que el cliente no confirmó no se publica.
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
8. **Formulario**: formulario nativo de GHL (`ghl.form_id`), embebido en la página, esté donde esté hospedada. Lleva campos ocultos `gclid`, `utm_source`, `utm_campaign` y `utm_term`; el código pasa los parámetros de la URL al iframe. Si la cuenta usa un dominio white-label para los formularios, pega su código de inserción en `ghl.form_embed_html`. Al enviarse, el formulario redirige a la URL de gracias que indica `ghl-seo.md`.

## Pasos comunes
1. **Inventario**: lista `servicio → keyword principal → slug → URL final → ¿indexar?` en 1 tabla antes de escribir. Si Jhombis no corrige, sigue.
2. **Spec por página**: copia `knowledge/landings/spec-ejemplo.json` a `clients/<slug>/landings/<slug-pagina>/spec.json`, borra `_nota`, ajusta `hosting` (lo indica cada comando) y completa todo. Copy:
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
5. **Índice**: `clients/<slug>/landings/README.md` con una tabla `página | URL final | hosting | keyword | indexar | QA bloqueantes | estado (borrador / publicada / montada en GHL) | fecha`.
