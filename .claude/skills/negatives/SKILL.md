---
name: negatives
description: Gestiona negativas: aplica la lista universal PMM y la del nicho a una cuenta nueva, o aplica las negativas propuestas por /weekly-review tras confirmación. Usar cuando se pida "negativas", "aplicar lista universal", "excluir términos".
---

# /negatives — Listas de negativas

## Modos
- `/negatives init <slug>`: crea/vincula la lista compartida "PMM Universal" (desde `knowledge/negativas-universales.md`) a nivel de cuenta y una lista "<slug> nicho" con la sección del nicho + `data/negatives-nicho.txt`. Antes de aplicar, muestra los términos que podrían chocar con los servicios del brief (ej. "parts" si vende repuestos) y pide confirmación para excluirlos de la lista.
- `/negatives apply <slug> <archivo>`: aplica `data/YYYY-MM-DD-negatives.txt` (formato: `término | match | nivel(campaña/adgroup/cuenta)`) tras confirmación de Jhombis.
- `/negatives suggest <slug>`: solo propone, sin aplicar, a partir de search terms de los últimos N días.

## Reglas
- Nivel cuenta: solo términos universales (empleo, educación, gratis…).
- Nivel campaña: términos de otros servicios que esa campaña no cubre (para que no se canibalicen).
- Nivel ad group: refinamientos entre grupos del mismo servicio.
- Match: frase por defecto; exacta para términos cortos que podrían bloquear demasiado (ej. `free` en exacta si el cliente ofrece "free estimate").
- Nunca agregues una negativa que coincida con una keyword activa del mismo nivel; el script lo valida.
- Cada aplicación se registra en `log/YYYY-MM-DD.md`.
- Cubrir siempre las categorías de desperdicio del playbook (`knowledge/playbook-analitica.md` §6): utilities (cambian por mercado; buscar la cooperativa local), marcas de producto, DIY/informativas, competencia (en frase, a nivel campaña), precio de referencia y empleo, y geografía fuera de zona.
- Términos genéricos de esas listas que chocan con servicios que el cliente sí vende (p. ej. `wiring`, `troubleshooting`, `replace`, `tesla`, `wall connector` en un electricista con grupos de reparación o EV) no van sueltos: se usan combinados con el modificador de producto o DIY (`wiring diagram`, `tesla home charger`) o en exacta, y el conflicto se muestra antes de aplicar.
- Si el cliente ofrece cotización o diagnóstico gratis, **no** bloquear `free`.

## Herramientas
`scripts/negatives.py` (API) o export CSV para Google Ads Editor.

## Al terminar
Resume cuántos términos se aplicaron por nivel y cuáles se descartaron por conflicto.
