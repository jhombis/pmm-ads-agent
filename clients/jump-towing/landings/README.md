# Landings — Jump Towing LLC

Generadas con `/landing` (Plesk, `scripts/landing_build.py`) el 2026-10-08. Copy solo con datos del brief: sin reseñas, licencia, años, ofertas ni tiempos de llegada, porque ninguno está confirmado. Teléfono: el de tracking de CallFire **(612) 665-6274**.

| Página | URL final | Hosting | Keyword | Indexar | QA bloqueantes | Estado | Fecha |
|---|---|---|---|---|---|---|---|
| towing-brooklyn-park | https://performancemediamarketing.com/jump-towing/towing/ | plesk | towing brooklyn park | no | 3 | borrador | 2026-10-08 |
| roadside-help-brooklyn-park | https://performancemediamarketing.com/jump-towing/roadside/ | plesk | roadside help brooklyn park | no | 3 | borrador | 2026-10-08 |

- Ruta libre en Plesk: `/jump-towing/`, `/jump-towing/towing/` y `/jump-towing/roadside/` dan 404 (verificado el 08-oct desde el servidor). No hay otro cliente de towing en MN en este dominio.
- **Bloqueantes iguales en las dos** (no se publica hasta cerrarlos):
  1. `ghl.form_id`: formulario GHL de Jump Towing con campos ocultos gclid/UTM y redirección a `/gracias/` (PMM).
  2. `legal.privacidad_url`: política de privacidad (la de jumptowing.com si existe, o una de PMM para el cliente) (PMM / Jhombis).
  3. Conversión: `tracking.google_ads_id` + `conversion_label_form` (y `conversion_label_call`) de la cuenta 220-410-9619, o el GTM del cliente. No los dos (PMM).
- **Avisos**:
  - Sin prueba social ni oferta en el hero: faltan GBP y reseñas, y oferta confirmada.
  - Roadside solo menciona jump starts y remolque. Lockout, llanta y combustible se agregan cuando el cliente los confirme.
- **Decisión de dominio**: el anuncio va a mostrar `performancemediamarketing.com`, no `jumptowing.com`. Si se prefiere el dominio del cliente (PMM tiene acceso a la web), la alternativa es `/landing-ghl` con el mismo spec y `hosting.tipo = "ghl"`.
