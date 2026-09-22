# PMM Ads Agent

Agente de Google Ads para Performance Media Marketing. Se usa con Claude Code (o Claude con este repo como carpeta de trabajo).

## Flujo por cliente nuevo
```
/onboard            → clients/<slug>/brief.md
/audit-landing  ┐
/competitors    ├─ en paralelo → audit-site.md, competitors.md, benchmark.md
/benchmark-interno ┘
/strategy           → strategy.md  (revisar y aprobar)
/roadmap            → roadmap.md + checklist.md
/build-campaign     → campañas en PAUSA vía API (o CSV para Ads Editor)
/weekly-review      → log/, avanza fases, propone negativas
/negatives          → aplica negativas
```

## Primeros pasos
1. `docs/setup-google-ads-api.md` → crear `google-ads.yaml`.
2. Etiquetar cuentas del MCC con `nicho:*` y `pais:*`.
3. Probar con un cliente real: `/onboard`.

## Dónde está cada cosa
- `CLAUDE.md`: reglas y estándares PMM. Léelo antes de cambiar cualquier skill.
- `knowledge/`: playbook (destilado del video + criterio PMM), PMax, negativas, checklist base, benchmarks.
- `.claude/skills/`: un skill por paso del flujo.
- `clients/`: una carpeta por cliente; `_template` es el molde.
- `scripts/`: API de Google Ads (GAQL, cuentas del MCC), PageSpeed.

## Agregar una estrategia nueva
Un archivo en `knowledge/estrategias/` con: cuándo aplica, condiciones de entrada, configuración y cómo evaluar. Luego referenciarla desde `/strategy` o `/roadmap`.
