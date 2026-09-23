# Playbook de analítica y optimización de Google Ads

Base de conocimiento para un agente de Ads. Recoge el método de diagnóstico, los umbrales de decisión, los patrones de desperdicio recurrentes y las reglas del portafolio, extraídos de casos reales.

Última actualización: 22 de septiembre de 2026.

> **Cómo lo usa el agente.** Complemento de análisis para **todas** las cuentas del MCC, con o sin carpeta en `clients/`. Lo aplican `/diagnose`, `/weekly-review`, `/strategy`, `/audit-landing`, `/negatives` y `/benchmark-interno`. Si algo aquí choca con los estándares de `CLAUDE.md`, se aplica la resolución de la sección "Reconciliación con los estándares PMM" al final de este archivo. `/weekly-review` y `/diagnose` agregan filas al **Registro de casos** (sección 11) cuando encuentran un hallazgo nuevo.

---

## 1. Alcance

Portafolio de ~15 cuentas de servicios locales en EE. UU. (plomería, grúas, electricistas, pavimentación, funeraria, transmisiones, abogados). Presupuestos declarados entre $799 y $2,500 mensuales. Todas operan con campañas de búsqueda por radio geográfico, algunas con Display o Performance Max de apoyo.

El agente debe asumir que son cuentas **de bajo volumen**: entre 3 y 15 clics diarios. Casi todos los marcos de optimización publicados están escritos para cuentas con cien veces ese volumen y no aplican tal cual.

---

## 2. Acceso a los datos: Windsor.ai

Conector `google_ads`. Los IDs de cuenta se pasan con guiones, tal como aparecen en `get_connectors` (ej. `758-301-1023`).

### Campos útiles

| Propósito | Campos |
|---|---|
| Rendimiento | `spend`, `clicks`, `impressions`, `conversions`, `all_conversions`, `phone_calls`, `cpc`, `ctr`, `cost_per_conversion` |
| Competitividad | `search_impression_share`, `search_budget_lost_impression_share`, `search_rank_lost_impression_share` |
| Configuración | `campaign_status`, `campaign_primary_status`, `campaign_primary_status_reasons`, `budget_amount`, `target_cpa`, `bidding_strategy_type`, `campaign_type` |
| Desglose | `date`, `month`, `campaign`, `search_term`, `keyword_text`, `conversion_action_name`, `device` |

### Limitaciones aprendidas

- **`keyword` no sirve**: devuelve ideas del Keyword Planner y es incompatible con los campos de rendimiento. Usar siempre **`keyword_text`**.
- Google Ads no permite mezclar campos de reportes distintos en una misma consulta. El error lo dice explícitamente; la solución es partir en dos llamadas.
- **`budget_amount` y `target_cpa` reflejan el valor vigente**, no el histórico. Si un mes gastó más de lo que permite el presupuesto actual, el presupuesto se cambió después: hay que confirmar la fecha en el historial de cambios de Google Ads, que Windsor no expone.
- El informe de términos de búsqueda **solo cubre una parte del gasto** (en Pro Phase, $212.89 de $352.88). Al calcular porcentajes de desperdicio, decir siempre "sobre el gasto rastreable".
- Los días sin filas en una serie diaria suelen indicar programación de anuncios, no falta de datos. Verificar antes de alarmarse.

---

## 3. Rutina de diagnóstico

Orden fijo. Cada paso puede cerrar el caso.

1. **Serie mensual** de los últimos 3–4 meses: gasto, clics, conversiones, CPC, cuota de impresiones. Sirve para separar una caída real de una comparación contra un mes pico.
2. **`campaign_primary_status` + `budget_amount` + `target_cpa`** por campaña. Detecta limitaciones por presupuesto y configuraciones de puja incoherentes con el historial.
3. **Serie diaria** del mes en curso. Localiza la fecha exacta del quiebre.
4. **`conversion_action_name` por mes.** Si una acción concreta se va a cero mientras las demás siguen, el problema es de medición, no de demanda.
5. **Términos de búsqueda** con clics > 0, últimos 30–60 días. Clasificar por categoría de desperdicio (sección 6).
6. **`keyword_text`** con impresiones > 0. Revela la concentración de gasto y las palabras de alta intención que no reciben tráfico.
7. **Landing page** (sección 7).

### Señales de lectura rápida

- **Alta pérdida por presupuesto + gasto bajo**: el presupuesto diario se agota temprano en tráfico equivocado. No es falta de dinero, es falta de filtros.
- **Cuota de impresiones baja con CPC alto**: problema de relevancia y de nivel de calidad.
- **Palabra de alta intención con impresiones y cero clics** mientras una genérica consume el presupuesto: la puja por clics está comprando lo barato. Síntoma clásico de `TARGET_SPEND` sin tope.
- **Tasa de conversión por debajo del 2% en servicios locales**: revisar medición antes que campaña. Lo sano está entre 5% y 10%.

---

## 4. Matemáticas de presupuesto

Fórmulas que el agente debe aplicar antes de proponer cualquier estructura.

- **Tope mensual real = presupuesto diario × 30.4.** Google puede gastar hasta el doble del diario en un día, pero nunca supera ese tope mensual. Si una campaña gasta rápido al inicio del mes, se frena al final: no es un fallo, es el tope. Caso Ridge Electric: $2/día → tope de $60.80; gastó $59.04 al día 18 y se apagó de hecho.
- **Clics diarios = presupuesto diario ÷ CPC.** Con $50/día y CPC $13.57 son 4 clics. Este número manda sobre cualquier ambición de estructura.
- **Prospectos mensuales esperados = clics mensuales × tasa de conversión.** Con 140 clics y 5–8%, son 7–11 prospectos. Decirlo antes de que el cliente lo descubra.
- **Presupuesto declarado ≠ inversión en medios.** En algunas cuentas solo ~40% del presupuesto que ve el cliente se ejecuta como inversión real (el resto es margen). Consultar siempre la tabla interna de gasto máximo por cuenta antes de juzgar el pacing. El monto que aparece en el nombre de la campaña puede estar desactualizado (caso C And P Paving).

### Límite de fragmentación

Una campaña necesita volumen para salir de aprendizaje. Regla práctica:

| Inversión real mensual | Estructura máxima sensata |
|---|---|
| < $600 | 1 campaña, 2–3 grupos |
| $600 – $1,500 | 1 campaña, 3–5 grupos |
| $1,500 – $4,000 | 2–3 campañas por línea de servicio |
| > $4,000 | Separación completa por servicio, marca y geografía |

Ocho campañas con $50 diarios equivalen a medio clic por campaña al día: ninguna acumula datos nunca.

---

## 5. Estrategia de puja

| Situación | Estrategia | Razón |
|---|---|---|
| Cuenta nueva o < 15 conversiones/mes | Maximizar clics **con tope de CPC** | La puja automática sin historial puja a ciegas y compra lo genérico |
| 15+ conversiones/mes estables | Maximizar conversiones, con CPA objetivo si ya se conoce el costo sostenible | Hay con qué aprender |
| Conversiones sucias (rellenos, clics, vistas) | Limpiar primero las acciones de conversión | Optimizar hacia una métrica falsa es peor que no optimizar |

Referencias reales:
- **Integrity Plumbing**: pasó de CPA objetivo a Maximizar clics con tope de $10 el 12 ago 2026, con $22/día. El dueño reportó aumento de llamadas en los días siguientes.
- **Ridge Electric**: Maximizar conversiones con CPA objetivo de $20 y ~24 conversiones mensuales. Funciona porque tiene historial.
- **Noah's Tow Truck**: cuenta nueva con Smart Bidding, sobregasto inmediato y cero conversiones.

Nunca fijar un CPA objetivo arbitrario: debe salir del CPA histórico observado, no de una expectativa.

---

## 6. Categorías de desperdicio

Estas cinco categorías han aparecido en todas las cuentas revisadas. La lista maestra de negativas debe cubrirlas, y tres de ellas suelen faltar en los marcos genéricos.

### 6.1 Empresas de energía y servicios públicos *(específica del oficio eléctrico)*

La más cara y la más fácil de pasar por alto, porque cambia con cada mercado. Quien busca a su empresa de luz quiere pagar el recibo.

Arkansas: `carroll electric`, `ozarks electric`, `swepco`, `entergy`.
San Diego: `sdge`.
Genéricas: `cooperative`, `utility`, `pay bill`, `outage`, `power company`, `+ciudad+ electric` cuando la ciudad tiene cooperativa propia.

> En Pro Phase, "carroll electric" se llevó $50.46 de $212.89 rastreables en 18 días.

### 6.2 Marcas de producto

El usuario quiere comprar el aparato, no contratar la instalación. "Suministros" como categoría es demasiado vaga: hay que nombrar marcas.

Eléctrico: `tesla`, `wall connector`, `supercharger`, `ccs`, `adapter`, `generac`, `leviton`, `lutron`, `harbor breeze`, `minka`, `casablanca`, `siemens`, `eaton`, `intermatic`, `zinsco`, `sylvania`.
Retail: `lowes`, `home depot`, `amazon`, `menards`.

> En Ideal Electric, las palabras de cargadores EV gastaron ~$430 con 1 conversión, alimentadas por búsquedas como "tesla home charger" y "best home ev charger 2026".

### 6.3 Bricolaje e informativas

`how to`, `diy`, `wiring`, `wire size`, `gauge`, `diagram`, `troubleshooting`, `not working`, `replace`, `what size`, `why does`, `reset`.

### 6.4 Marcas de la competencia

Se recogen del informe de términos y se añaden en frase. En Integrity Plumbing se aplicaron 43 negativas y en Leading Edge Towing 52, en ambos casos a nivel campaña y en concordancia de frase.

### 6.5 Precio de referencia y empleo

`hourly rate`, `cost per hour`, `average cost`, `how much does`, `price list`, `salary`, `jobs`, `hiring`, `apprentice`, `school`, `certification`, `license requirements`.

Excepción: si el cliente ofrece cotización o diagnóstico gratuito, **no** bloquear `free`.

### 6.6 Específicas por vertical

- **Grúas**: programas de asistencia en carretera ajenos (AAA, seguros), geografía fuera de zona.
- **Servicios locales en general**: nombres de ciudades fuera del radio. Verificar siempre la cobertura real con el cliente; suele ser más estrecha que la configurada.

---

## 7. Auditoría de medición y landing page

**Ningún resultado es interpretable si la medición está rota.** Este paso va antes de cualquier ajuste de puja. Casos reales encontrados:

| Hallazgo | Cuenta | Efecto |
|---|---|---|
| Popup heredado de otro cliente que decía "su solicitud no está confirmada, llame a (915)…" — número de otro estado | Ideal Electric | Desviaba los prospectos del formulario; tasa de conversión al 0.8% |
| Dos teléfonos distintos entre la página de inicio y la de contacto | Ideal Electric | Las llamadas al número no rastreado no se contaban |
| "Website Calls" a cero mientras "Calls from ads" seguía normal | Ridge Electric | Fallo del rastreo de llamadas del sitio |
| Recurso de llamada en revisión | Noah's Tow Truck | Cero conversiones registradas |
| Filtro de duración de llamada por encima del umbral razonable | Noah's Tow Truck | Llamadas válidas descartadas como conversión |

### Checklist

1. Un solo teléfono en todo el sitio, y que sea el número de reenvío configurado en la acción de conversión.
2. Enviar un formulario de prueba: verificar el mensaje de gracias, la llegada del correo y el registro de la conversión en 24–48 h.
3. Revisar qué acciones de conversión están activas y si son prospectos reales o vistas y clics.
4. Estado de los recursos de llamada (no en revisión, no rechazados).
5. Horario de atención contra programación de anuncios, **en la zona horaria de la cuenta** (`customer.time_zone`), que puede no ser la del cliente. Un negocio que cierra a las 4 p.m. y anuncia hasta medianoche paga llamadas que nadie contesta.
6. Si el sitio usa Elementor, revisar Templates → Popups y las acciones "After Submit" del formulario. Al borrar un popup, la acción del formulario puede quedar apuntando a algo inexistente.
7. Registrar la **fecha del arreglo** para poder comparar el antes y el después.

---

## 8. Estructura de campaña recomendada

Para un oficio local con presupuesto medio, una campaña con grupos por intención:

1. **Servicio principal + "near me" + ciudades** — el núcleo.
2. **Reparación y urgencias** — alta intención, buena tasa de llamada. Solo si el cliente atiende de verdad fuera de horario.
3. **Trabajo de ticket alto** (panel eléctrico, reemplazo de línea, instalación mayor).
4. **Servicio emergente** (cargadores EV, generadores) — solo si el cliente lo presta.

Reglas:
- Exacta y frase al arrancar. La amplia y AI Max solo después de ~50 conversiones limpias acumuladas.
- Un RSA por grupo, con el término de servicio fijado en un titular.
- Cada grupo a su página de servicio, nunca todo al inicio del sitio.
- Marca en campaña aparte solo cuando exista volumen de búsqueda de marca. En un negocio nuevo, no lo hay.
- Segmentación geográfica por **presencia**, nunca por presencia o interés.
- Socios de búsqueda desactivados al lanzar en cuentas de bajo presupuesto: mezclan tráfico de calidad distinta y contaminan la lectura.

---

## 9. Qué no se puede concluir con bajo volumen

El agente debe declarar los límites antes de que alguien saque conclusiones equivocadas.

- Con 4 clics diarios, un test A/B de anuncios da ~60 clics por variante en 90 días. Cualquier diferencia es ruido. Los tests de creatividad se hacen en las cuentas con volumen.
- Las audiencias en observación no dan señal estadística útil en un trimestre a este nivel de tráfico.
- Un mes con el doble de conversiones que el promedio es normalmente un pico, no una nueva base. Antes de declarar una "caída", comparar contra la mediana de 3–4 meses, no contra el mejor mes. Caso Ridge Electric: agosto con 36 conversiones contra un promedio de 25–27; septiembre parecía un desplome y la campaña de búsqueda estaba en su nivel normal.
- Una tasa de conversión del 35% sobre 32 clics no es una tasa, es azar.

---

## 10. Reglas del portafolio

- **Nunca pausar campañas de Display.** Sostienen la visibilidad del perfil de Google Business y su valor no se mide por conversiones en Ads. Si gastan de más, se les baja el presupuesto.
- Las cuentas que son de compañeros (ayuda puntual) **no entran en los informes propios**.
- El pie de página de informes y checklists dice **"PMM"**.
- Formato de informe habitual: HTML gerencial en lenguaje sencillo — KPIs, destacados positivos, tabla por cuenta con barra de pacing, cambios de presupuesto y plan de acción al cierre.
- Las acciones de escritura sobre Google Ads desde el chat están habilitadas en Windsor (Settings → API Access). **Nada se aplica sin aprobación explícita previa**, con la lista de cambios a la vista.
- Antes de analizar una cuenta, confirmar que está vinculada al conector. Si no lo está, no es legible ni operable.

---

## 11. Registro de casos

| Fecha | Cuenta | Hallazgo | Acción |
|---|---|---|---|
| Ago 2026 | Integrity Plumbing | CPA objetivo asfixiaba el volumen | Maximizar clics con tope $10; más llamadas |
| Ago 2026 | Integrity Plumbing | Competencia e investigación | 43 negativas en frase |
| Ago 2026 | Leading Edge Towing | Competencia, asistencia ajena, precio, geografía | 52 negativas en frase |
| Sep 2026 | Pro Phase Electric | 95% del gasto rastreable en cooperativas de energía, genéricas, competencia y bricolaje | Propuesta de reestructura y negativas |
| Sep 2026 | Ideal Electric | Popup de otro cliente con teléfono de otro estado; dos números en el sitio | Popup eliminado el 21 sep 2026 |
| Sep 2026 | Ridge Electric | PMax con $2/día alcanzó su tope mensual; "Website Calls" a cero | Pendiente: historial de cambios y revisión del rastreo |
| Sep 2026 | Pro Phase Electric | Cuenta en zona horaria del Pacífico con cliente en Arkansas (Central): la programación "5–16" corría 7–18 hora local, fuera del horario de atención | Programación a 3–14 hora de la cuenta el 23 sep 2026. **Verificar siempre `customer.time_zone` contra la zona del cliente** |

---

## 12. Cómo debe responder el agente

- Empezar por el dato, no por la recomendación. Mostrar la serie temporal antes de diagnosticar.
- Distinguir siempre entre **caída real** y **comparación contra un pico**.
- Cuantificar el desperdicio en dinero, no en adjetivos: "$50.46 de $212.89" convence, "mucho tráfico irrelevante" no.
- Nombrar lo que no puede saber: presupuestos históricos, el historial de cambios, qué servicios presta realmente el cliente, si la cobertura configurada coincide con la real.
- Proponer el orden de ejecución, no una lista suelta: medición → negativas → estructura → puja → creatividad.
- No aplicar cambios sin aprobación, y dejar registrada la fecha de cada cambio para poder medirlo después.

---

## Reconciliación con los estándares PMM (decidido por Jhombis, 23-sep-2026)

| Tema | Playbook | Estándar anterior | Queda |
|---|---|---|---|
| Puja inicial | <15 conv/mes o cuenta nueva → Max. clics con tope | Max. conversiones desde el inicio | **Playbook**: Max. clics con tope de CPC hasta 15+ conv/mes estables con medición limpia; luego Max. conversiones; tCPA con ~30/30d desde el CPA histórico |
| RSA por grupo | 1 | mínimo 3 | **Por volumen**: <$1,500/mes de pauta → 1 (máx. 2); más volumen → 3 |
| Amplia / AI Max | tras ~50 conversiones limpias | con tCPA maduro | Ambas condiciones + aprobación de Jhombis |
| Estructura | tabla de fragmentación por inversión | STAG, ciudad con ≥100 búsquedas | La tabla manda; ciudades dentro del grupo del servicio con inserción de keyword |
| Negativas genéricas vs. servicios vendidos | `tesla`, `wall connector`, `wiring`, `troubleshooting`, `replace` sueltas | "nunca negar una keyword activa" | No se usan sueltas si chocan: se quitan las keywords de producto/DIY (p. ej. las de Tesla) o se usan negativas combinadas ("tesla home charger", "wiring diagram") |
| Marcas de paneles (`zinsco`, `siemens`, `eaton`) | negativas de producto | — | **No** negar en cuentas con grupo de paneles: "zinsco panel replacement" es un lead de ticket alto |
