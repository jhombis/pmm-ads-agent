---
name: build-campaign
description: Crea en Google Ads (vía API) las campañas, ad groups, keywords, negativas, RSA y extensiones definidas en strategy.md, en pausa, y verifica la configuración. Usar cuando Fase 0 esté completa y se pida "crear las campañas", "montar la cuenta".
---

# /build-campaign — Ejecutar strategy.md en la cuenta

## Requisitos
- `strategy.md` versión aprobada por Jhombis.
- `checklist.md` con Fase 0 completa (tracking verificado, negativas universales, landing aprobada). Si no, detente y lista qué falta.
- `docs/setup-google-ads-api.md` configurado; `customer_id` del cliente en `brief.md`.

## Reglas de seguridad
- Todo se crea en **PAUSA**. Jhombis activa manualmente o pide `/build-campaign --enable`.
- Antes de escribir, imprime el plan de operaciones (N campañas, N grupos, N keywords, N anuncios) y pide confirmación.
- Usa `validate_only=true` primero; si pasa, ejecuta.
- Nunca modifiques campañas existentes con este skill; solo crea. Para cambios usa `/weekly-review`.

## Pasos (scripts/build_campaign.py)
1. Lista de negativas compartida "PMM Universal" a nivel de cuenta (crear si no existe) + lista del nicho.
2. Por campaña de `strategy.md`:
   - Tipo Search; red: solo búsqueda; sin socios; sin Display.
   - Presupuesto diario de Fase 1.
   - Puja según estándar 6 / playbook §5: MAXIMIZE_CLICKS con `cpc_bid_ceiling` si la cuenta es nueva o tiene <15 conv/mes; MAXIMIZE_CONVERSIONS sin target con 15+ estables.
   - Geo: ubicaciones del brief con `positive_geo_target_type = PRESENCE`; excluir países no objetivo.
   - Idioma; programación de anuncios **en la zona horaria de la cuenta** (leer `customer.time_zone` y convertir el horario del cliente); rotación OPTIMIZE.
   - Ad groups con keywords y match types de `data/keywords.csv`.
   - RSA desde `data/ads-*.md`, H1 pinneado: 1 por grupo (máx. 2) si la pauta es <$1,500/mes; 3 si es mayor.
   - Extensiones: sitelinks, callouts, snippets, llamada, ubicación (vinculación GBP).
3. Verificación post-creación (GAQL): leer cada campaña y confirmar los 9 ajustes del playbook. Escribir resultado en `log/YYYY-MM-DD-build.md`.
4. Verificar URLs finales con HEAD request (200, sin redirect).

## Alternativa sin API
Genera `data/import-google-ads-editor.csv` con el formato de Google Ads Editor (campaña, ad group, keyword, match, anuncios, extensiones) para importar manualmente. Indícalo claramente.

## Al terminar
Resume qué se creó, en qué estado, y las verificaciones que pasaron/fallaron. Actualiza `checklist.md` Fase 1. Siguiente: activar campañas, revisar aprobación de anuncios en 24h, `/weekly-review` a los 7 días.
