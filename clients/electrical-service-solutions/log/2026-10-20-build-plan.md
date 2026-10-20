---
cliente: Electrical Service Solutions
slug: electrical-service-solutions
fecha: 2026-10-20
skill: /build-campaign (solo plan; no se ejecutó)
---

# Plan de operaciones — /build-campaign (preparado, sin ejecutar)

**No se escribió nada en Google Ads.** La Fase 0 no está completa: faltan el Google Tag, las conversiones, /thank-you/, el formulario arriba, la facturación y el volumen por ZIP, además de tu aprobación de strategy.md v1.1. Este archivo y los CSV quedan listos para cuando se cierre.

## Qué se va a crear (todo en PAUSA)
| Elemento | Cantidad | Detalle |
|---|---|---|
| Presupuesto | 1 | $42.56/día, estándar |
| Campaña | 1 | `ESS · Search · Paneles · South Hills/North Hills/Monroeville`, Search, **pausada** |
| Red | — | Solo Búsqueda de Google: sin socios ni Display |
| Puja | — | Maximizar clics con tope de CPC de $15.00 |
| Ubicación | 5 | ZIP 15102, 15241, 15228, 15237 + Monroeville, PA · **Presencia** (inclusión y exclusión) |
| Idioma | 1 | Inglés |
| Programación | 7 franjas | L–V 09:00–21:00 · S–D 09:00–17:00, **hora del Este** (convertir si la cuenta está en otra zona) |
| Rotación | — | Optimizar |
| Ad groups | 4 | Panel Upgrade, Service Upgrade, Fuse Box y Commercial Panel (habilitados dentro de la campaña pausada) |
| Keywords | 51 | 42 términos; 9 en exacta + frase (Panel Upgrade 27 · Service Upgrade 12 · Fuse Box 7 · Commercial Panel 5) |
| RSA | 4 | 1 por grupo, H1 pinneado en la posición 1, 15 headlines y 4 descripciones |
| Negativas de campaña | 303 | 167 de "PMM Universal" + 136 de nicho (`data/2026-10-20-negatives.txt`) |
| Negativas de ad group | 8 | Reparto entre grupos |
| Sitelinks | 4 | Residential Panels, Commercial Panels, Get A Free Quote y About Us; Financing cuando exista /financing/ |
| Callouts | 8 | 40+ Years Experience · Financing Available · Free Quotes · Permits & Inspection · Open 7 Days · Residential & Commercial · Panel Specialists · Service Change-Outs |
| Snippet | 1 | Services: Panel Upgrades, Panel Replacement, Service Upgrades, Fuse Box Replacement, Meter Base Replacement, Commercial Panels |
| Llamada | 1 | (412) 666-9290 (CTN de CallFire), US |

URLs finales verificadas el 20-oct (HEAD → 200, sin redirección): /residential-electric-service-panel-upgrades-replacements/, /commercial-electric-service-panel-upgrades-replacements/, /contact-us/ y /about-us/.

## Vía 1 (recomendada): Google Ads Editor
Archivos:
- `data/import-google-ads-editor.csv` (376 filas): campaña, ubicaciones, ad groups, keywords, negativas de grupo, RSA y negativas de campaña.
- `data/import-google-ads-editor-assets.csv` (14 filas): sitelinks, callouts, snippet y llamada.

Pasos:
1. Editor → cuenta 384-080-6970 → Account → Import → From file → `import-google-ads-editor.csv`. Revisar la vista previa: tienen que salir 1 campaña, 5 ubicaciones, 4 grupos, 51 keywords, 311 negativas y 4 anuncios, sin errores.
2. Importar `import-google-ads-editor-assets.csv`. Si Editor lo pide, importar por tipo.
3. **Verificar a mano antes de publicar** (son las columnas que Editor puede no mapear):
   - Ubicaciones resueltas a los ZIP y a Monroeville, **PA**.
   - "Location of presence" en la opción de segmentación.
   - Tope de CPC de $15 en Maximizar clics.
   - Programación en la zona horaria de la cuenta.
4. Crear la lista compartida "PMM Universal" (Shared library → Negative keyword lists), mover ahí las 167 universales y vincularla a la campaña.
5. Post → campaña **pausada**. Activa Jhombis.

## Vía 2: Windsor (la que se eligió para las negativas)
Secuencia: `create_campaign` (pausada, target_spend, 42,560,000 micros) → `set_cpc_bid_ceiling` (15,000,000) → `set_campaign_geo_targeting` → `set_campaign_language_targeting` (en) → `set_ad_schedule` → 4× `create_ad_group` → 4× `push_keywords` → `push_negative_keywords` (campaña, 303) y 4× (grupo) → 4× `create_responsive_search_ad` → 14× `create_ad_asset`.

**Límites de Windsor (verificados en `list_actions`)**:
- No configura la red ni el tipo de segmentación geográfica. Después de crear la campaña hay que poner **Presencia** y apagar los **socios de búsqueda** en la interfaz (estándares 1 y 8).
- No crea listas compartidas: las 167 universales van a nivel de campaña.
- `set_campaign_geo_targeting` pide los IDs numéricos de los ZIP y de Monroeville. No se pudieron sacar desde el entorno (la tabla de geo-targets de Google está bloqueada): hay que buscarlos en la interfaz o en el CSV de geo-targets.
- El RSA de Windsor no tiene parámetro de pin: hay que confirmar si acepta pinned_field o pinnear el H1 en la interfaz.

## Antes de ejecutar (cualquiera de las dos vías)
- [ ] Fase 0 cerrada en checklist.md (tag, conversiones probadas, /thank-you/, formulario arriba, facturación, volumen por ZIP)
- [ ] strategy.md v1.1 aprobada por Jhombis
- [ ] Zona horaria de la cuenta: si no es la del Este, convertir la programación
- [ ] Recurso de llamada: confirmar que el informe de llamadas (call reporting) está activo para que "Calls from ads" cuente

## Verificación después de crear (playbook, 9 ajustes)
1. Solo red de Búsqueda (sin socios ni Display)
2. Presencia en inclusión y exclusión
3. 5 ubicaciones correctas en PA; resto del mundo sin segmentar
4. Maximizar clics con tope de $15
5. Programación L–V 9–21 y S–D 9–17 (hora del Este)
6. Rotación optimizada; recomendaciones automáticas apagadas
7. 51 keywords en frase o exacta, sin amplia
8. 4 RSA con el H1 pinneado y fuerza "Buena" o más
9. Negativas (311) y extensiones (llamada, 4 sitelinks, 8 callouts, snippet) vinculadas

El resultado de la verificación va a `log/YYYY-MM-DD-build.md` cuando se ejecute.
