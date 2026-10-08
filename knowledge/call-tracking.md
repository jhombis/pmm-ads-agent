# Call tracking — CallFire y CallRail

Las llamadas son la conversión principal de casi todo el portafolio (towing ≈ 86% de las conversiones). Google Ads solo ve las **llamadas desde el anuncio** y cuenta como conversión las que superan su umbral de duración. El call tracking ve **todas las llamadas al número**: duración real, si alguien contestó, si el llamante repite, el horario y la grabación. Por eso es la fuente para juzgar la calidad del lead y si el cliente contesta.

## Conectores (MCP, solo lectura)
| Proveedor | Herramientas | Qué cubre hoy |
|---|---|---|
| **CallFire** (`mcp__CallFire__*`) | `callfire_get` path `/numbers/leases` (números y su etiqueta = cliente) · `callfire_list_calls` (`toNumber`, `intervalBegin`/`intervalEnd` en ms epoch, `limit` ≤1000) · `callfire_get_call` | La mayoría de los clientes: un número de reenvío por negocio, etiquetado con su nombre. `callfire_list_numbers` devuelve 404: usar `callfire_get /numbers/leases`. |
| **CallRail** (`mcp__CallRail_PMM__*`) | `callrail_list_companies` · `callrail_list_trackers` (números por fuente) · `callrail_list_calls` (`company_id`, `start_date`/`end_date`, `fields`) · `callrail_get_call` (`fields=transcription,call_summary,lead_status`) · `callrail_list_form_submissions` | Hoy solo la cuenta AAMCO: 6 talleres de Jacksonville, cada uno con número de **anuncio (Ad Ext)**, **GMB** y **pool de la web (DNI)**. |

No hace falta configurar nada más: los conectores ya están en la sesión. Si no aparecen, revisar en claude.ai → Settings → Connectors que estén conectados y habilitados para Claude Code.

## Cómo encontrar el número de un cliente
1. Front matter del `brief.md`: `call_tracking`, `tracking_number`, `tracking_destino`.
2. Si no está: CallFire `/numbers/leases` (paginar con `offset`; ~270 números) y buscar la etiqueta con el nombre del negocio; CallRail `callrail_list_companies` + `callrail_list_trackers`.
3. Si no aparece en ninguno, es una pregunta para el cliente (`/onboard`, bloque 3) o un pendiente (`/investigar-cliente`).
4. Anotar en el brief **dónde se usa el número** (extensión de llamada, sitio web, GBP, todos). Con CallFire hay un número por negocio: si el mismo número está en la web y en el GBP, las llamadas no se pueden atribuir a Ads solo con CallFire.

## Exportar y resumir
1. Traer las llamadas del periodo con el conector y guardar la respuesta tal cual en `clients/<slug>/data/calls-<proveedor>-<desde>_<hasta>.json` (si hay varias páginas, una lista de respuestas).
   - CallFire: `callfire_list_calls` con `toNumber` = número de tracking (formato `1XXXXXXXXXX`), `intervalBegin` en ms, `limit` 1000.
   - CallRail: `callrail_list_calls` con `company_id`, `start_date`, `end_date`, `per_page` 250, `fields=source_name,tracking_phone_number,lead_status,first_call`.
2. `python scripts/call_summary.py <archivo> --tz <zona del cliente> --gasto <gasto Ads del periodo> --ads-conv <conv. de llamada en Ads>`.

## Definiciones (las usa todo el repo)
| Métrica | Definición |
|---|---|
| Llamada | Toda llamada entrante al número de tracking. |
| Contestada | CallFire: existe el tramo `XFER_LEG` con duración > 0 (el negocio atendió). CallRail: `answered = true`. |
| No contestada | CallFire: `ABANDONED` u otro resultado sin `XFER_LEG`. CallRail: `answered = false` o buzón. |
| **Calificada** | Llamante único con al menos una llamada contestada de **≥60 s de conversación** (umbral PMM, igual que la conversión de Google Ads). Los números ocultos cuentan por llamada. |
| Repetida | Segunda o siguiente llamada del mismo número en el periodo. |
| Costo por llamada calificada | Gasto de Google Ads ÷ calificadas. Es el CPL real del nicho de llamadas, más fiel que el que reporta Ads. |

## Qué mirar (en este orden)
1. **Tasa de contestadas.** <80% en horario de atención es un problema del cliente y no de la campaña: se reporta con $ ("de 28 llamadas, 6 sin contestar = ~$90 de pauta perdida") y va a `Para el cliente`.
2. **Calificadas vs conversiones de Google Ads.** Si Ads reporta muchas más, la conversión de llamada cuenta llamadas cortas o repetidas (ver playbook §7). Si reporta muchas menos, faltan llamadas desde la web o el GBP, o falta el recurso de llamada.
3. **Llamadas cortas (<30 s) y repetidas.** Muchas cortas = número equivocado, spam o el cliente no contesta. Muchas repetidas = no contestan a la primera.
4. **Horario.** Llamadas fuera del horario de atención (`por_hora`, zona del cliente) contra la programación de anuncios. Si llegan llamadas fuera de horario y nadie contesta, ajustar la programación o pedir desvío.
5. **Fuente** (solo CallRail): Ad Ext vs GMB vs web. Es la única forma de separar lo que trae Ads de lo que trae el GBP.
6. **Contenido** (solo CallRail, con `transcription`/`call_summary`): el motivo real de la llamada (cotización, empleo, proveedor, spam). Las grabaciones de CallFire son mp3: el agente no las transcribe; se listan las URL de las 3–5 llamadas más largas para que alguien las escuche si hace falta.

## Privacidad
Los números de los llamantes y las grabaciones son datos personales: van solo en `data/` del cliente. En el informe (`/informe`) se muestran solo los agregados, nunca números ni enlaces a grabaciones.

## Clientes con número identificado (2026-10-08)
| Cliente | Proveedor | Número de tracking | Notas |
|---|---|---|---|
| JQ Towing | CallFire | (352) 645-5030 | Reenvía a (352) 282-2512 |
| RR Roadside Relief | CallFire | (405) 536-9093 | |
| Jump Towing | CallFire | (612) 665-6274 | Reenvía a (612) 616-0723. 28 llamadas, 12 calificadas (14-sep → 08-oct) |
| 290 Tow & Recovery | CallFire | (830) 463-8318 | |
| Spillane's Towing | CallFire | (802) 216-3105 | |
| Precision Towing | CallFire | (760) 606-4160 | Confirmar que es este negocio (la etiqueta coincide; prefijo de Victorville) |
| AAMCO 103rd St | CallRail + CallFire | CallRail: Ad Ext (904) 569-5501 · GMB (904) 664-1215 · pool web "103rd St. - Jax Ad Pool" · CallFire: (904) 203-5211 | CallRail separa por fuente |
| Pro Phase Electric · Jerry's Towing · Colton Sunflower · Hemet Affordable | — | No encontrado | Preguntar. Jerry's: existe "Fishhawk Towing" (813) 565-3206 en CallFire; confirmar si es suyo |
