---
name: roadmap
description: Convierte strategy.md en un roadmap con fechas estimadas y condiciones de paso por fase, y crea checklist.md del cliente. Usar después de /strategy o cuando se pida "roadmap", "cronograma", "cuándo lanzo PMax", "plan de fechas".
---

# /roadmap — Plan por fases con fechas y condiciones

## Requisitos
Lee `clients/<slug>/brief.md`, `strategy.md`, `audit-site.md` y (si existe) `benchmark.md`. Si falta `strategy.md`, detente y pide correr `/strategy`.

## Principio
Cada fase tiene **fecha estimada** y **condición de paso**. La fecha es una proyección; la condición es la verdad. `/weekly-review` avanza el estado solo cuando la condición se cumple, y si no, escribe el bloqueo y reprograma. Nunca se avanza "porque ya es la fecha".

## Cómo calcular las fechas
Toma como `D0` la fecha que Jhombis indique (o hoy). Ajusta con estos factores:

| Factor | Efecto |
|---|---|
| `audit-site.md` marca bloqueantes | Fase 0 se extiende: +3 días si edita PMM, +7–14 si edita el cliente |
| Sin historial de conversiones | Fase 3 (tCPA) se estima con `conversiones/día esperadas = presupuesto diario ÷ CPL benchmark`; días hasta 30 conv. = 30 ÷ eso, mínimo 21 días |
| Presupuesto < 3× CPL benchmark por día | Advertir: aprendizaje lento; fase 3 +2 semanas; PMax probablemente nunca califica |
| País = US y LSA aplica | Añadir pista paralela "LSA" con verificación 2–4 semanas desde D0 |
| Cliente responde leads >1h o sin proceso | Añadir bloqueante en Fase 0 y advertencia en Fase 1 |
| Nicho estacional (HVAC, towing en invierno, etc.) | Anotar ventana y si conviene adelantar/retrasar lanzamiento |

## Salida: `clients/<slug>/roadmap.md`
```markdown
---
cliente:
slug:
D0: YYYY-MM-DD
actualizado: YYYY-MM-DD
fase_actual: 0
---

# Roadmap — <cliente>

## Resumen
Una línea por fase con fecha estimada y estado (⏳ pendiente · 🔄 en curso · ✅ hecha · ⛔ bloqueada).

## Fase 0 — Fundación
- **Fecha estimada**: D0 → D0+N
- **Condición de paso**: todas las tareas bloqueantes de Fase 0 en checklist ✅
- **Tareas**: (lista concreta para ESTE cliente, con responsable)
- **Riesgos**:

## Fase 1 — Lanzamiento Search
- **Fecha estimada**:
- **Condición de paso**: campañas activas 7 días, anuncios aprobados, ≥1 conversión registrada
- **Qué se lanza**: campañas y presupuesto diario de strategy.md, fase 1
- **Riesgos**:

## Fase 2 — Limpieza (D7 · D14 · D30)
- **Fechas**: tres fechas concretas
- **Condición de paso**: tres revisiones hechas, negativas aplicadas, keywords sin impresiones pausadas
- **Qué se revisa**: search terms, gasto sin conversión, RSA peor por grupo

## Fase 3 — Optimización de puja (tCPA)
- **Fecha estimada**: (calculada, con el supuesto explícito)
- **Condición de paso**: ≥30 conversiones en ventana de 30 días con tracking verificado
- **Acción**: tCPA = CPA real observado; reajustar presupuesto
- **Si no se cumple en fecha**: revisar landing (conv. <5%), presupuesto, o keywords; NO forzar tCPA con menos datos

## Fase 4 — Remarketing
- **Fecha estimada**:
- **Condición de paso**: audiencia ≥1000 en 30 días
- **Acción**: RLSA en observación → ajuste de puja; Display remarketing opcional

## Fase 5 — Performance Max
- **Fecha estimada**: típicamente semana 6–10; escribir la real según fase 3
- **Condición de paso**: TODAS las de `knowledge/estrategias/pmax-cuando-y-como.md`
- **Acción**: configuración PMM para PMax
- **Si no califica**: explicar cuál condición falla y qué hacer para cumplirla (o quedarse en Search + remarketing)

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance actual (sin CRM). Se reevalúa cuando el cliente tenga registro de leads con GCLID.

## Pista paralela — Landing
- Ajustes recomendados por audit-site.md, con fecha y responsable
- Cuáles son bloqueantes (fase 0) y cuáles mejoras (fase 2–3)

## Pista paralela — LSA (solo si aplica)
- D0: iniciar solicitud · D0+14–28: verificación · luego: presupuesto semanal y gestión de reseñas

## Estacionalidad y ventanas
- (si aplica)

## Historial de cambios
- YYYY-MM-DD: creado
```

## Salida 2: `clients/<slug>/checklist.md`
Copia `knowledge/checklists/setup-cuenta.md`, elimina lo que no aplica (LSA si no es US, PMax si el presupuesto no lo permitirá), agrega las tareas específicas de este cliente (ajustes de landing, pendientes del brief) y pone responsable a cada ítem. Front matter con `fase_actual: 0`.

Si se entrega el plan en HTML (`plan-es.html` / `plan-en.html`), se arma con el estilo PMM: `python scripts/informe_html.py new …`, componentes de `knowledge/estilo-informes/README.md` (fases con color fijo, línea de tiempo, checklist) y `check` antes de publicar.

## Al terminar
Resume: D0, fecha estimada de lanzamiento, fecha estimada de tCPA (con el supuesto), si PMax es realista o no y por qué, y los 3 bloqueantes más importantes. Siguiente paso: resolver bloqueantes de Fase 0 y correr `/build-campaign`.
