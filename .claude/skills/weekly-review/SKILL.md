---
name: weekly-review
description: Revisión periódica de una cuenta: search terms → negativas, gasto sin conversión, CPA vs objetivo, avance de fases del roadmap y actualización del checklist. Escribe log/YYYY-MM-DD.md. Usar en las revisiones día 7/14/30 y semanales, o cuando se pida "revisar la cuenta", "cómo va X".
---

# /weekly-review — Seguimiento y avance de fase

## Requisitos
Lee `brief.md`, `strategy.md`, `roadmap.md`, `checklist.md` y el último `log/*.md`. Datos: Google Ads API (`scripts/gaql.py`) o Windsor.ai; exports a `data/YYYY-MM-DD-*.csv`.

## Método (knowledge/playbook-analitica.md)
Sigue la rutina de diagnóstico del playbook (§3) y sus reglas de respuesta (§12): dato antes que recomendación, desperdicio en dinero y **sobre el gasto rastreable**, caída real contra comparación con un pico (mediana de 3–4 meses), límites de bajo volumen (§9) y orden de ejecución medición → negativas → estructura → puja → creatividad. Si una acción de conversión cae a cero mientras otras siguen, es medición y va primero.

## Pasos
1. **Datos del período** (últimos 7d y 28d, por campaña y ad group): costo, clics, impresiones, conv., CPA, CTR, tasa conv., impression share (presupuesto / ranking), estado de anuncios.
2. **Search terms** (desde última revisión): clasificar cada término con gasto → relevante / negativa / nueva keyword, y agrupar las negativas por categoría de desperdicio del playbook (§6: utilities, marcas de producto, DIY, competencia, precio/empleo, geografía) con su $. Escribir propuesta de negativas en `data/YYYY-MM-DD-negatives.txt` (aplicar solo tras confirmación de Jhombis, vía `/negatives`).
3. **Desperdicio**: keywords con gasto > 2× CPL objetivo y 0 conversiones → proponer pausar o bajar. Keywords con 0 impresiones en 30d → pausar.
4. **Anuncios**: rechazados/limitados; RSA con fuerza baja; peor RSA por grupo (CTR y conv.) → reemplazar.
4b. **Medición**: `conversion_action_name` por semana; estado de los recursos de llamada; que el horario de anuncios coincida con el de atención.
5. **Calidad de leads**: preguntar a Jhombis si el cliente reportó (hasta que haya CRM). Anotar spam.
6. **Roadmap**: comparar la condición de paso de la fase actual contra los datos. Si se cumple → avanzar `fase_actual`, marcar ✅, poner fecha de la siguiente. Si no → ⛔ con la razón concreta y nueva fecha estimada. Nunca avanzar por calendario.
7. **Presupuesto**: gasto acumulado del mes vs presupuesto; proyección; impression share perdido por presupuesto en campañas rentables → propuesta de reasignación.
8. **Checklist**: marcar lo hecho, agregar tareas nuevas con responsable.
9. **Registro de casos**: si hubo un hallazgo nuevo o útil para otras cuentas, agregar una fila al §11 del playbook. Anotar la **fecha de cada cambio** aplicado para medir antes/después.

## Salida: `clients/<slug>/log/YYYY-MM-DD.md`
```markdown
---
cliente:
fecha:
periodo: 7d / 28d
fase_antes: N
fase_despues: N
---

# Revisión <fecha> — <cliente>

## Estado en una línea
CPA $X vs objetivo $Y (tendencia ↑↓), N conv. en 7d, gasto Z% del presupuesto.

## Acciones tomadas
- ...

## Acciones propuestas (requieren OK)
- [ ] Negativas: N términos (ver data/...)
- [ ] Pausar keywords: ...
- [ ] Reemplazar RSA: ...
- [ ] Presupuesto: ...

## Avance de fase
Fase actual, condición, cumple/no, razón, próxima fecha.

## Métricas
| Campaña | Costo | Conv. | CPA | CTR | IS presup. | IS rank |

## Para el cliente
2–3 líneas en lenguaje no técnico que Jhombis puede reenviar.

## Próxima revisión
Fecha y qué mirar.
```

Actualiza `roadmap.md` (estado de fases, historial) y `checklist.md`.


## Al terminar
Resume estado, acciones propuestas que necesitan OK, y si la fase avanzó.

**Último paso obligatorio: `/informe`**: actualizar y republicar el artefacto del cliente (ES + EN, estilo PMM) en sus mismas URLs y entregar los dos enlaces.
