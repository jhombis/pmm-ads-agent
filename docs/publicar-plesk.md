# Publicar landings en performancemediamarketing.com (Plesk)

Lo usa `/landing` (`hosting.tipo = "plesk"`). Para GoHighLevel o el dominio del cliente está `/landing-ghl`. Cada landing vive en una carpeta estática dentro del WordPress de PMM:

```
https://performancemediamarketing.com/<cliente>/             → landing
https://performancemediamarketing.com/<cliente>/gracias/     → página de gracias (dispara la conversión)
https://performancemediamarketing.com/<cliente>/<servicio>/  → si el cliente tiene más de una landing
```

- Servidor: dominio `performancemediamarketing.com` en Plesk. Document root: `/var/www/vhosts/performancemediamarketing.com/httpdocs`.
- El `.htaccess` de WordPress solo reescribe lo que **no** existe como archivo o carpeta (`!-f`, `!-d`), así que una carpeta real se sirve tal cual y WordPress no la toca.
- `<cliente>` es el slug del cliente sin ciudad, salvo que haga falta distinguirlo (`jq-towing`, `jump-towing`, `pro-phase-electric`). Se fija en `spec.json → hosting.ruta`.

## Qué se sube
Solo lo que deja el generador en `clients/<slug>/landings/<pagina>/publicar/`:

| Local | Servidor |
|---|---|
| `publicar/index.html` | `httpdocs/<ruta>/index.html` |
| `publicar/gracias/index.html` | `httpdocs/<ruta>/gracias/index.html` |

Nunca se suben `spec.json`, `qa.md`, `ghl-*`, `preview.html` ni nada de `data/`: todo lo que está en `httpdocs` es público. `publicar/MANIFIESTO.txt` repite el destino exacto de cada archivo.

## Procedimiento (conector `Plesk_PMM`)
1. **QA en 0 bloqueantes**: `python scripts/landing_build.py clients/<slug>/landings/<pagina>/spec.json`. No se publica con bloqueantes; el formulario GHL, la privacidad y la conversión tienen que estar.
2. **La ruta está libre**: `ssh_command`:
   ```
   D=/var/www/vhosts/performancemediamarketing.com/httpdocs/<ruta>
   ls -la "$D" 2>/dev/null
   curl -sk -o /dev/null -w "%{http_code}" --resolve performancemediamarketing.com:443:172.31.93.65 https://performancemediamarketing.com/<ruta>/
   ```
   - Si la carpeta no existe, el código debe ser 404. Un 200 significa que hay una página de WordPress con ese slug: cambia la ruta.
   - Si la carpeta existe y es de este cliente (su `index.html` lleva el mismo H1), es una **actualización**. `write_file` deja un backup `.bak.<fecha>` del archivo anterior.
   - Si la carpeta es de otra cosa, detente y pregunta.
3. **Carpetas**: `ssh_command` → `mkdir -p "$D/gracias"`. `write_file` no crea carpetas.
4. **Archivos**: `write_file` con `path = $D/index.html` y el contenido de `publicar/index.html`. Lo mismo con `gracias/index.html`.
5. **Dueño y permisos**: el conector escribe como root. Hay que devolverle los archivos al usuario de la suscripción:
   ```
   O=$(stat -c '%U:%G' /var/www/vhosts/performancemediamarketing.com/httpdocs/index.php)
   chown -R "$O" "$D" && find "$D" -type d -exec chmod 755 {} + && find "$D" -type f -exec chmod 644 {} +
   ```
6. **Verificación**: `curl` con `--resolve` (como en el paso 2) a `/<ruta>/` y `/<ruta>/gracias/`. Las dos tienen que dar 200 y contener el H1 esperado (`grep`). Desde el entorno de Claude el dominio puede estar bloqueado por la política de red; por eso la verificación se hace desde el servidor.
7. **Registro**:
   - `landings/README.md`: URL y estado `publicada`, con fecha.
   - `checklist.md`: probar con Tag Assistant (conversión solo en gracias, una vez) y cambiar la URL final de los anuncios. El cambio en Ads requiere el OK de Jhombis.
8. **Despublicar**: no se borra nada sin la aprobación de Jhombis. Si la da: `mv "$D" "$D.off.<fecha>"` (devuelve 403 o 404 y se puede revertir) en lugar de `rm`.

## Decisiones que trae este dominio
- **Dominio visible en el anuncio**: Google Ads muestra el dominio de la URL final. El anuncio de un cliente aparece como `performancemediamarketing.com`, no con el dominio del cliente, y eso puede bajar el CTR frente a competidores con su propia marca. Para clientes con dominio propio y acceso, la alternativa es `/landing-ghl` (GHL o su propio dominio).
- **Un anuncio por dominio en cada subasta**: Google no muestra dos anuncios con el mismo dominio en una misma subasta. Dos clientes de PMM del mismo nicho y con áreas que se solapan (p. ej. dos towing en la misma ciudad) se excluirían entre sí. Antes de publicar, revisa en `clients/informes.json` y en los briefs que no haya otro cliente del mismo nicho en la misma zona usando este dominio.
- **SEO**: por defecto la landing se publica con `noindex`. Posicionarla en el dominio de PMM no le sirve al cliente, y muchas páginas de towing casi iguales en un mismo dominio cuentan como *doorway pages*. Si un cliente necesita SEO, la landing va en su propio dominio.
- **Caché**: LiteSpeed Cache solo cachea WordPress; los archivos estáticos se sirven directos. Si una actualización no se ve, la causa es el caché del navegador o el CDN, no el plugin.
