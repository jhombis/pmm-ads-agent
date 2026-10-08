---
name: landing-ghl
description: Landing por servicio para montar en GoHighLevel o en el dominio del cliente (código para Custom Code + Head Tracking Code, SEO, schema, formulario GHL con gclid/UTM, página de gracias con conversión). Escribe clients/<slug>/landings/<pagina>/. Usar SOLO cuando se pida GoHighLevel/GHL o una landing en el dominio del cliente; para landings en performancemediamarketing.com usar /landing.
---

# /landing-ghl — Landing para GoHighLevel o el dominio del cliente

## Entrada
`/landing-ghl <slug> [servicio|todos] [ciudad]`. Por defecto hace una landing por cada campaña o servicio de `strategy.md`.

## Cuándo usarlo en vez de /landing
- El cliente quiere su propio dominio en el anuncio (`go.cliente.com`), o necesita SEO en su dominio.
- Otro cliente del mismo nicho y zona ya usa performancemediamarketing.com.
- Jhombis lo pide.

## Reglas y contenido
Sigue `knowledge/landings/reglas.md`: fuentes, reglas 1–8 y pasos comunes 1–5. En el spec: `hosting: {"tipo": "ghl"}` y `pagina.url_final` = la URL real en el dominio del cliente o de GHL.

## Montaje
`docs/setup-gohighlevel.md`: dominio, formulario con campos ocultos, Custom Code, Head Tracking Code, página de gracias, conversiones, workflow y verificación.

## Salida por página (`clients/<slug>/landings/<pagina>/`)
| Archivo | Dónde va en GHL |
|---|---|
| `spec.json` | fuente; editar aquí y regenerar, nunca en el HTML |
| `ghl-body.html` | página en blanco → elemento **Custom Code** a ancho completo |
| `ghl-head.html` | página → Settings → **Head Tracking Code** |
| `ghl-seo.md` | página → Settings → SEO Meta Data + path + redirección del formulario |
| `gracias-body.html` / `gracias-head.html` | página de gracias (dispara la conversión) |
| `preview.html` | revisión local |
| `qa.md` | checklist automático |

## Al terminar
Resume en 3–5 líneas:
- páginas creadas y cuáles se indexan
- bloqueantes de QA y quién los resuelve
- qué falta para montarlas en GHL

Siguiente paso: montar, probar con Tag Assistant y actualizar las URLs finales en `strategy.md` antes de `/build-campaign`. Termina con `/informe`.
