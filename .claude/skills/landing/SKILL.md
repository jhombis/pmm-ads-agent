---
name: landing
description: Crea la landing de una campaña y la publica en https://performancemediamarketing.com/<cliente>/ (Plesk, sin GoHighLevel como hosting) con su página /gracias, conversión, SEO, schema y formulario con gclid/UTM. Escribe clients/<slug>/landings/<pagina>/ y sube solo publicar/. Usar cuando se pida "landing", "landing para la campaña", "crear landing page", "publicar la landing", "landing en performancemediamarketing.com". Para montar en GoHighLevel o en el dominio del cliente usar /landing-ghl.
---

# /landing — Landing de campaña en performancemediamarketing.com

## Entrada
`/landing <slug> [servicio|todos] [ciudad]`. Por defecto hace **una landing por cada campaña o servicio de `strategy.md`** (o por cada servicio principal del brief si aún no hay estrategia).

## URLs
| Caso | Landing | Gracias |
|---|---|---|
| Una landing por cliente | `https://performancemediamarketing.com/<cliente>/` | `…/<cliente>/gracias/` |
| Varias (una por servicio) | `https://performancemediamarketing.com/<cliente>/<servicio>/` | `…/<cliente>/<servicio>/gracias/` |

`<cliente>` es el slug corto del negocio, sin ciudad salvo que haga falta distinguirlo (`jq-towing`, `jump-towing`). Va en `spec.json → hosting: {"tipo": "plesk", "ruta": "<cliente>[/<servicio>]"}`. El generador fija la URL final, el canonical y la redirección a `/gracias/`; no se escriben a mano. La página sale con **noindex** por defecto (ver por qué en `docs/publicar-plesk.md`).

## Reglas y contenido
Sigue `knowledge/landings/reglas.md`: fuentes, reglas 1–8 y pasos comunes 1–5 (inventario, spec, generar y validar, revisión visual, índice).

## Pasos
1. **Antes de escribir**: revisa `clients/informes.json` y los briefs. Si otro cliente del **mismo nicho y zona** ya tiene landing en este dominio, avisa: Google muestra un solo anuncio por dominio en cada subasta y se quitarían impresiones entre sí. En ese caso propone `/landing-ghl` con el dominio del cliente.
2. **Pasos comunes 1–4** de `knowledge/landings/reglas.md`, con `hosting.tipo = "plesk"` y la `ruta` de la tabla de arriba.
3. **Publicar** solo si el QA está en 0 bloqueantes. Procedimiento completo en `docs/publicar-plesk.md` (conector `Plesk_PMM`):
   1. Ruta libre: 404 desde el servidor, o carpeta del mismo cliente si es una actualización.
   2. `mkdir -p` de `<ruta>/gracias`.
   3. `write_file` de **solo** `publicar/index.html` y `publicar/gracias/index.html`, a las rutas de `publicar/MANIFIESTO.txt`.
   4. `chown` al usuario de la suscripción y permisos 755 / 644.
   5. Verificación: 200 y el H1 esperado en `/<ruta>/` y `/<ruta>/gracias/` (curl con `--resolve` desde el servidor).

   Nunca subas `spec.json`, `qa.md`, `ghl-*` ni `preview.html`. Nunca borres nada en el servidor: para despublicar, renombra la carpeta y solo con el OK de Jhombis.
4. **Paso común 5** (índice `landings/README.md`) con estado `publicada` y fecha. En `checklist.md`, deja la tarea de probar con Tag Assistant: el formulario de prueba llega a GHL con `gclid` y la conversión dispara una vez en `/gracias/`.

## Al terminar
Resume en 3–5 líneas:
- URLs publicadas (o qué bloqueó la publicación y quién lo resuelve)
- teléfono usado (tracking o principal)
- indexación

Siguiente paso: probar con Tag Assistant y actualizar las URLs finales en `strategy.md` antes de `/build-campaign`. Cambiar las URLs en una campaña activa requiere el OK de Jhombis. Termina con `/informe`.
