# Landings GoHighLevel — Spillane's Towing & Recovery

Generadas con `/landing-ghl` el 2026-10-01 (`python scripts/landing_build.py clients/spillanes-towing/landings`). Una página por servicio de `strategy.md`. Todas en inglés y **noindex** (solo Ads): el SEO lo hace el sitio principal, spillanestowingandrecovery.com.

| Página | URL final | Keyword | Indexar | QA bloqueantes | Estado |
|---|---|---|---|---|---|
| towing-burlington-vt | https://go.spillanestowingrecovery.com/towing-burlington-vt | towing near me (AG1–AG4) | no | 2: form_id, conversión de formulario | borrador |
| accident-towing-winch-out-burlington-vt | https://go.spillanestowingrecovery.com/accident-towing-winch-out-burlington-vt | accident towing (AG5) | no | 2: form_id, conversión de formulario | borrador |
| flatbed-towing-burlington-vt | https://go.spillanestowingrecovery.com/flatbed-towing-burlington-vt | flatbed towing (AG6) | no | 2: form_id, conversión de formulario | borrador |

## Estructura (layout v2, 01-oct-2026)
A pedido de Jhombis, las 3 páginas usan `"layout": "v2"`:
1. Barra fija de llamada
2. Header con navegación y "Request Service"
3. Hero con badge, H1, 3 íconos de confianza, 2 CTA y foto
4. Reseñas
5. 4 servicios con íconos
6. Por qué elegirnos (4)
7. Zona con mapa y ciudades
8. FAQ en 2 columnas
9. CTA final oscuro con el formulario
10. Footer

El formulario queda abajo (el botón del hero baja hasta él). Se aparta del estándar "formulario arriba", pero aquí 13 de 14 conversiones son llamadas.
- **Foto del hero**: `spillanes-header.jpg`, del WordPress del cliente. Hay que subirla a la galería de medios de GHL, cambiar `hero.imagen.src` y confirmar que es un camión propio.
- **Mapa**: embed de Google Maps del condado (Chittenden County, VT), no del GBP, para no mostrar las 3.2★.

## Decisiones y supuestos
- **Dominio**: subdominio `go.spillanestowingrecovery.com` en GHL, para no tocar el WordPress actual. Hay que confirmarlo (o usar otro) y crear el CNAME.
- **Teléfono**: (802) 216-3105, el mismo de la landing actual de Ads. Falta confirmar que desvía a la línea principal (863-7900).
- **Sin rating ni conteo de Google** (3.2★): la prueba social son 2 testimonios publicados en los sitios del cliente, con su fuente.
- **Sin oferta** en el hero: el cliente no confirmó tiempo de llegada ni tarifa. Hay un aviso en la QA.
- **Datos del sitio del cliente sin confirmar**: "Available 24/7" (el sitio principal dice 7am–11pm), "50+ years" y la flota (1 wrecker, 16 flatbeds, 4 service trucks). Si el cliente corrige algo, se edita el `spec.json` y se regenera.
- **Sin enlace al GBP** (decisión de la auditoría).

## Para montar (docs/setup-gohighlevel.md)
1. Dominio y CNAME. 2. Formulario GHL con campos ocultos `gclid`, `utm_source`, `utm_campaign`, `utm_term` → `ghl.form_id` en cada spec y regenerar. 3. Conversión: GTM (`tracking.gtm_id`) o AW-ID + label de formulario y de clic en llamada. 4. Pegar `ghl-body.html` / `ghl-head.html` y la página de gracias. 5. Verificación §7 con Tag Assistant antes de mandar tráfico.
