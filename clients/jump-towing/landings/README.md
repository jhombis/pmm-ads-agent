# Landings — Jump Towing LLC

Generadas y publicadas con `/landing` (Plesk, `scripts/landing_build.py`) el 2026-10-08. Copy solo con datos del brief: sin reseñas, licencia, años, ofertas ni tiempos de llegada, porque ninguno está confirmado. Teléfono: el de tracking de CallFire **(612) 665-6274**.

| Página | URL final | Hosting | Keyword | Indexar | QA bloqueantes | Estado | Fecha |
|---|---|---|---|---|---|---|---|
| towing-brooklyn-park | https://performancemediamarketing.com/jump-towing/towing/ | plesk | towing brooklyn park | no | 0 (excepción: solo llamada) | **publicada** | 2026-10-08 |
| roadside-help-brooklyn-park | https://performancemediamarketing.com/jump-towing/roadside/ | plesk | roadside help brooklyn park | no | 0 (excepción: solo llamada) | **publicada** | 2026-10-08 |

- Ruta libre en Plesk: `/jump-towing/`, `/jump-towing/towing/` y `/jump-towing/roadside/` dan 404 (verificado el 08-oct desde el servidor). No hay otro cliente de towing en MN en este dominio.
- **Publicadas el 08-oct** en Plesk (`httpdocs/jump-towing/{towing,roadside}/` + `gracias/`). sha256 verificado, dueño de la suscripción, 755/644. 200 y H1 correctos desde el servidor. La carpeta raíz `/jump-towing/` da 403 (sin index), como se espera.
- **Privacidad**: https://jumptowing.com/privacy-policy/ (del cliente).
- **Conversión**: GTM del cliente `GTM-T9JFQNTC`, el mismo de jumptowing.com. Trae la etiqueta de Google Ads `AW-18347375568`:
  - "llamadas desde la web" (`__awcc`), que reemplaza el (612) 665-6274 por el número de reenvío de Google
  - una conversión por clic (`__awct`, disparadores de clic en enlace "612" y envío de formulario)

  Falta probar con Tag Assistant que la llamada y el clic disparen en la landing. El evento `pmm_lead_form` de la página de gracias no tiene disparador en ese GTM, pero hoy no hay formulario, así que no aplica.
- **Excepción aprobada por Jhombis (08-oct): solo llamada.** No hay formulario GHL (`ghl.solo_llamada: true`): en su lugar va una tarjeta de llamada con horario. Va contra el estándar 11 (formulario corto). Cuando exista el formulario: poner `ghl.form_id`, quitar `solo_llamada`, regenerar y republicar.
- **Avisos**:
  - Sin prueba social ni oferta en el hero: faltan GBP y reseñas, y oferta confirmada.
  - Roadside solo menciona jump starts y remolque. Lockout, llanta y combustible se agregan cuando el cliente los confirme.
- **Decisión de dominio**: el anuncio va a mostrar `performancemediamarketing.com`, no `jumptowing.com`. Si se prefiere el dominio del cliente (PMM tiene acceso a la web), la alternativa es `/landing-ghl` con el mismo spec y `hosting.tipo = "ghl"`.
