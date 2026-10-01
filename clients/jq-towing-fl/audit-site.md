---
cliente: JQ Towing
slug: jq-towing-fl
url: https://jqtowingfl.com/
actualizado: 2026-10-01
veredicto: SIN AUDITAR
score: —/22
---

# Auditoría de landing — JQ Towing

## Veredicto
**Sin auditar.** La política de red del entorno bloquea jqtowingfl.com (CONNECT 403) y PageSpeed API devolvió 429 (sin `PAGESPEED_API_KEY`). No se puntúa la rúbrica para no inventar. Re-correr `/audit-landing` cuando el dominio esté permitido o con el HTML/capturas pegados.

## Lo que sí se sabe
- **No indexado**: `site:jqtowingfl.com` no devuelve resultados; Semrush sin datos del dominio → sitio nuevo o bloqueado a buscadores. Cero relevancia orgánica de partida; el Quality Score dependerá 100% de la relevancia on-page.
- Cliente declara **Google Tag + formulario instalados** (sin verificar).
- Teléfono a mostrar: (352) 645-5030.

## Bloqueantes potenciales (verificar en Fase 0)
- [ ] Google Tag presente y disparando — Tag Assistant — PMM — 0.5 h
- [ ] Formulario: ≤4 campos, visible sin scroll en móvil, **página de gracias con URL propia** — PMM — 0.5 h revisar / 2 h si hay que crearla
- [ ] `tel:` sticky o en header móvil — PMM — 0.5 h
- [ ] Headline por servicio (towing / roadside) — depende de si hay páginas por servicio
- [ ] Velocidad móvil (score ≥ 40 mínimo, ideal ≥ 70) — PageSpeed — PMM — 0.25 h
- [ ] ¿Por qué no está indexado? (noindex, robots.txt, dominio nuevo) — no bloquea Ads, pero `noindex` sugiere sitio sin terminar

## Landings que la estrategia va a necesitar
Con $879/mes y una campaña Search (towing + roadside por tema), mínimo:
1. **Towing / Tow truck — Ocala & Belleview** (H1 con "Towing in Ocala, FL" / "24/7 Tow Truck")
2. **Roadside assistance** (lockout, jump start, flat tire, fuel delivery) — puede ser una sola página
3. Opcional si el cliente lo hace: **Golf cart towing — The Villages** (20 búsq./mes, comp. 0.93)
4. Página de gracias medible (compartida)

No hace falta servicio×ciudad: el volumen por ciudad fuera de Ocala es ~0.

## Qué ya rankea orgánico (Semrush)
Nada (dominio sin datos).

## Para completar esta auditoría
Una de estas:
- Permitir `jqtowingfl.com` en Network access del entorno y re-correr `/audit-landing`.
- Pegar el HTML de la home (view-source) + capturas móvil above the fold, y el score de pagespeed.web.dev.
