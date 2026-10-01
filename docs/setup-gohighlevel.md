# Setup: montar en GoHighLevel las landings de /landing-ghl

Los nombres de los menús pueden variar un poco entre versiones de GHL o de cuentas white-label. Cuando un valor depende de la cuenta (registros DNS, dominio de los formularios), usa el que muestra GHL en pantalla.

## 0. Websites o Funnels
- **Websites**: para páginas que deben **posicionar en SEO**. Genera sitemap, tiene páginas hermanas y un menú común.
- **Funnels**: para páginas **solo para Ads** (`indexar: false`). Cada página es un paso, y el siguiente paso es la página de gracias.

Las dos aceptan los mismos bloques (Custom Code + Head Tracking Code + SEO Meta Data).

## 1. Dominio (una vez por cliente)
1. GHL → Settings → **Domains** → Add domain. Usa un subdominio, p. ej. `go.cliente.com` u `ofertas.cliente.com`, para no tocar la web principal.
2. Crea en el DNS del cliente el registro **CNAME** que indica GHL en esa pantalla y espera a que el SSL quede activo.
3. Asigna el dominio al Website o Funnel. La URL final de cada página es `https://<dominio>/<slug>`, la misma que va en `spec.json → pagina.url_final`.

## 2. Formulario (uno por servicio, o uno común con un campo "Servicio" oculto)
1. Sites → **Forms** → Builder. Máximo 4 campos visibles: nombre, teléfono, (email), qué necesita.
2. Añade **campos ocultos** y ponle a cada uno su *Query Key*: `gclid`, `utm_source`, `utm_campaign`, `utm_term` (y `service` si el formulario es común). La landing pasa los parámetros de la URL al formulario.
3. En Options → **On submit: Open URL** pon la página de gracias que indica `ghl-seo.md`.
4. Copia el **Form ID** (está en la URL del builder o en el código de inserción) en `spec.json → ghl.form_id` y regenera. Si la cuenta usa un dominio white-label para los formularios, pega su código de inserción completo en `ghl.form_embed_html`.
5. Activa el consentimiento SMS/TCPA si el cliente envía SMS. En US es obligatorio para hacer follow-up por texto.

## 3. Página de la landing
1. Crea una página o paso en blanco con el path igual al `slug`.
2. Arrastra **una sección a ancho completo → una fila de 1 columna → el elemento "Custom Code"** y quítale el padding a la sección, la fila y la columna.
3. Pega `ghl-body.html` en el elemento.
4. En **Settings** de la página:
   - Head Tracking Code → pega `ghl-head.html`.
   - SEO Meta Data → title, description e imagen social de `ghl-seo.md`.
5. Si el Website o Funnel ya tiene GTM o gtag en su head global, **no** lo repitas. En ese caso borra del `spec.json` el ID duplicado y regenera.

## 4. Página de gracias
Igual que el paso 3, con `gracias-body.html` y `gracias-head.html`. Esta página queda en noindex y dispara la conversión del formulario.

## 5. Conversiones en Google Ads
- **Formulario**: crea una acción de conversión de tipo *Website*, categoría *Submit lead form*, y copia el ID `AW-…` y la *label* en `spec.json → tracking`. Con GTM, en su lugar, crea un activador *Custom Event* `pmm_lead_form` → etiqueta de conversión de Google Ads.
- **Clic en teléfono**: otra acción *Website* (clicks on phone number) → `conversion_label_call`.
- **Llamadas reales**: si el cliente usa un número de seguimiento de GHL (LC Phone), muestra ese número en `negocio.telefono`. Las llamadas desde los anuncios se miden con el call asset de Google. La importación offline de GHL a Google Ads es una fase futura (fuera de alcance, ver CLAUDE.md).

## 6. Workflow de GHL (aviso del lead)
Automation → Workflow → trigger **Form Submitted** (el formulario de esta landing):
1. Crear o actualizar el contacto, con el tag `ads-<servicio>`.
2. Notificar al cliente por SMS y email con nombre, teléfono, servicio y `utm_term`.
3. Opcional: SMS automático al lead ("Recibimos tu solicitud…").
4. Crear la oportunidad en el pipeline del cliente.

## 7. Verificación antes de mandar tráfico (bloqueante, estándar PMM n.º 7)
- [ ] Abrir `https://<dominio>/<slug>?gclid=TEST123&utm_source=google`, enviar el formulario y confirmar que el contacto en GHL tiene `gclid=TEST123`.
- [ ] Tag Assistant: la conversión dispara **solo** en la página de gracias y **una vez**.
- [ ] El clic en el teléfono dispara la conversión de llamada (si se configuró).
- [ ] PageSpeed móvil ≥ 70: `python scripts/pagespeed.py https://<dominio>/<slug>`.
- [ ] Rich Results Test sin errores en el schema.
- [ ] Páginas indexables enviadas en Search Console. Las `indexar: false` deben devolver noindex.
- [ ] Enlace a la política de privacidad funcionando.
