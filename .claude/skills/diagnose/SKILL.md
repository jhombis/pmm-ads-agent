---
name: diagnose
description: Diagnóstico de cualquier cuenta de Google Ads del MCC (con o sin carpeta en clients/) usando la rutina del playbook de analítica: serie mensual, estado de campañas, serie diaria, acciones de conversión, search terms por categoría de desperdicio, keywords, medición y landing. Cuantifica el desperdicio en dinero y propone el orden de ejecución. Usar cuando se pida "diagnosticar", "qué le pasa a la cuenta X", "por qué bajaron las llamadas", "revisa la cuenta X" en una cuenta sin onboarding, o antes de /strategy en una cuenta que ya gasta.
---

# /diagnose — Diagnóstico de una cuenta (playbook de analítica)

Fuente: `knowledge/playbook-analitica.md`. Léelo antes de empezar; este skill es su rutina ejecutable.

## Requisitos
- ID de la cuenta (con guiones, como en `get_connectors` de Windsor) o nombre.
- **Confirmar que la cuenta está en el conector** (Windsor `get_connectors` o `scripts/mcc_accounts.py`). Si no está, no es legible: dilo y detente.
- Si existe `clients/<slug>/`, lee `brief.md`, `checklist.md` y el último `log/`. Si no, trabaja solo con datos y marca como **desconocido** lo que solo sabría el cliente.
- Pregunta o busca el **gasto máximo real** de la cuenta: el monto del nombre de la campaña es el contrato y puede estar desactualizado; la inversión en medios suele ser ~40–60% de ese monto.

## Rutina (orden fijo; cada paso puede cerrar el caso)
Datos por Windsor (`google_ads`) o API (`scripts/gaql.py`). Si Windsor da error de campos incompatibles, divide la consulta. Usa `keyword_text`, nunca `keyword`.

1. **Serie mensual (3–4 meses)**: gasto, clics, conversiones, CPC, IS. Compara contra la **mediana**, no contra el mejor mes. Un mes con el doble del promedio es un pico, no una base.
2. **Estado por campaña**: `campaign_primary_status`, `campaign_primary_status_reasons`, `budget_amount`, `target_cpa`, `bidding_strategy_type`. `budget_amount` y `target_cpa` son valores **vigentes**: si el gasto histórico no cuadra con el presupuesto actual, alguien lo cambió. Pide el historial de cambios; Windsor no lo expone.
3. **Serie diaria del mes**: fecha exacta del quiebre. Los días sin filas suelen ser programación de anuncios o tope mensual (presupuesto diario × 30.4), no falta de datos.
4. **`conversion_action_name` por mes**: si una acción cae a cero y las demás siguen, el problema es de **medición**, no de demanda.
5. **Search terms** con clics > 0 (30–60 días). Clasifica en las categorías de desperdicio del playbook (§6): utilities, marcas de producto, DIY/informativas, competencia, precio/empleo, vertical/geografía fuera de zona. Reporta cada categoría en **$ y % sobre el gasto rastreable** (el informe de términos no cubre todo el gasto; di cuánto cubre).
6. **`keyword_text`** con impresiones > 0: concentración del gasto, keywords de alta intención con impresiones y 0 clics (síntoma de Max. clics sin tope comprando lo barato).
7. **Medición y landing** (checklist del playbook §7): un solo teléfono en todo el sitio y que sea el de reenvío, formulario de prueba, acciones de conversión reales (no vistas ni clics), estado de los recursos de llamada, filtro de duración de llamada, horario de atención contra programación, popups y "After Submit" si es Elementor.

## Lectura rápida
- Mucha IS perdida por presupuesto + gasto bajo → el presupuesto se agota en tráfico equivocado: faltan filtros, no dinero.
- IS baja + CPC alto → relevancia y Quality Score.
- Tasa de conversión <2% en servicios locales → revisar medición antes que campaña (lo sano es 5–10%).
- Matemática de presupuesto: clics/día = presupuesto diario ÷ CPC; prospectos/mes = clics/mes × tasa de conversión. Dilo antes de que el cliente lo descubra.
- Límite de fragmentación: con <$600 de pauta, 1 campaña y 2–3 grupos; con $600–1,500, 1 campaña y 3–5 grupos (tabla del playbook §4).

## Qué NO concluir con bajo volumen (playbook §9)
No declares ganadores de A/B de anuncios, ni señales de audiencias en observación, ni tasas de conversión sobre <50 clics. Nómbralo explícitamente en el informe.

## Salida
- Si hay carpeta de cliente: `clients/<slug>/log/YYYY-MM-DD-diagnose.md`.
- Si no: `diagnostics/<nombre-cuenta-en-slug>/YYYY-MM-DD.md`, con front matter `cuenta`, `account_id`, `fecha`, `periodo`.

```markdown
# Diagnóstico <fecha> — <cuenta>

## En una línea
El problema principal, con el número que lo prueba.

## Datos (antes del diagnóstico)
Serie mensual y, si aplica, la diaria. Mediana de referencia.

## Hallazgos (ordenados por dinero)
| # | Hallazgo | Evidencia ($ / datos) | Categoría (medición / desperdicio / estructura / puja / creatividad) |

## Desperdicio por categoría (sobre $X rastreables de $Y totales)
| Categoría | $ | % | Términos ejemplo |

## Lo que no se puede saber desde los datos
Presupuestos históricos, historial de cambios, servicios que presta realmente, cobertura real, calidad de los leads.

## Plan en orden de ejecución
1. Medición → 2. Negativas → 3. Estructura → 4. Puja → 5. Creatividad. Cada acción con "requiere OK" y la fecha en que se aplicaría (para medir antes/después).
```

Propuestas de negativas en `data/YYYY-MM-DD-negatives.txt` (o `diagnostics/<cuenta>/`), para aplicar solo con `/negatives` tras OK.
Si el hallazgo es nuevo o útil para otras cuentas, agrega una fila al **Registro de casos** del playbook (§11): fecha, cuenta, hallazgo, acción.

## Reglas
- Empieza por el dato, no por la recomendación. Cuantifica en dinero ("$50.46 de $212.89"), nunca en adjetivos.
- Distingue **caída real** de **comparación contra un pico**.
- Nada se aplica sin aprobación explícita, con la lista de cambios a la vista. Toda escritura queda con fecha en el log.
- **Nunca propongas pausar campañas de Display** existentes: sostienen la visibilidad del GBP. Si gastan de más, se baja su presupuesto.
- Las cuentas de compañeros (ayuda puntual) no entran en informes propios.

## Al terminar
Resume en 3–5 líneas: problema principal con su número, $ desperdiciado sobre el rastreable, primera acción del plan, qué hay que preguntarle al cliente. Siguiente: `/negatives` para lo propuesto; `/onboard` + `/strategy` si la cuenta necesita reestructura.
