---
name: onboard
description: Entrevista de onboarding de un cliente nuevo de Google Ads. Crea clients/<slug>/ y escribe brief.md. Usar cuando llega un cliente nuevo o cuando se dice "onboard", "nuevo cliente", "dar de alta".
---

# /onboard — Alta de cliente nuevo

## Objetivo
Recoger en una sola conversación todo lo que los demás skills necesitan, y dejarlo en `clients/<slug>/brief.md`. Sin brief no corre nada más.

## Reglas
- Pregunta en bloques de 4–6 preguntas, no una por una ni las 25 de golpe. Usa AskUserQuestion cuando las opciones sean cerradas.
- Si Jhombis pega un texto, correo o propuesta del cliente, extrae primero lo que ya responde y pregunta solo lo que falta.
- Lo que no se sepa se marca `PENDIENTE`, no se inventa. Los pendientes bloqueantes van al checklist.
- Cuando tengas la URL, haz un WebFetch rápido de la home para confirmar nicho, servicios y ciudades antes de preguntar (ahorra la mitad de las preguntas).
- Slug: minúsculas, guiones, sin tildes: `aamco-jacksonville`, `towing-miami-rapid`.

## Bloque 1 — Identidad
1. Nombre del negocio y URL principal
2. País y ciudad base; **área de servicio real** (radio en km/millas o lista de ciudades/condados)
3. Nicho (towing, plomería, electricista, HVAC, taller, abogado, dental, otro)
4. Servicios que ofrece, en orden de rentabilidad para el cliente (los 3–5 principales)
5. Servicio que **más quiere vender** y el que **menos** le interesa (aunque tenga demanda)
6. Idioma del mercado (EN / ES / ambos)

## Bloque 2 — Objetivo y dinero
7. Objetivo primario: llamadas, formularios, WhatsApp, reservas, visitas al local
8. Presupuesto mensual de pauta (sin fee) y si hay margen para escalar
9. Ticket promedio y margen aproximado por trabajo (para calcular CPL máximo aceptable)
10. Cuántos leads/trabajos al mes puede atender (capacidad)
11. ¿Tiene historial en Google Ads? Si sí: ID de cuenta, hace cuánto, qué pasó (para /benchmark-interno leer su histórico)

## Bloque 3 — Operación (los eslabones que no controlamos)
12. Horario de atención real y si hay servicio 24/7 con alguien que conteste
13. ¿Quién responde los leads y en cuánto tiempo? ¿Tienen recepcionista, IA, buzón?
14. Teléfono principal y si aceptan call tracking (número de reenvío)
15. ¿Tienen CRM o dónde registran los leads? (solo documentar, no integrar)
16. Google Business Profile: ¿verificado? ¿cuántas reseñas y promedio? ¿acceso para PMM?

## Bloque 4 — Competencia y diferenciación
17. 3–5 competidores que el cliente reconoce (nombre o URL)
18. ¿Por qué un cliente lo elige a él? (licencias, años, garantía, precio, rapidez, financiación)
19. Ofertas o promociones que puede sostener (cotización gratis, sin cargo por visita, descuento)
20. Marca: ¿la gente lo busca por nombre? (decide campaña de marca)

## Bloque 5 — Web y tracking
21. ¿La landing/sitio es de PMM o del cliente? ¿Quién puede editarla? (WordPress/Elementor, otro)
22. ¿Hay Google Tag / GA4 instalado? ¿Acceso?
23. ¿Hay formulario en la web? ¿A dónde llegan los envíos?
24. Restricciones de políticas: ¿el nicho tiene requisitos (licencias visibles, certificaciones, garantías)?

## Bloque 6 — Solo si país = US
25. ¿La categoría está en Local Services Ads? ¿Tiene licencia, seguro y disposición al background check?

## Salida: `clients/<slug>/brief.md`
```markdown
---
cliente: <nombre>
slug: <slug>
pais: US|CO
idioma: EN|ES
nicho: <nicho>
actualizado: YYYY-MM-DD
estado: onboarding
---

# Brief — <cliente>

## Negocio
- URL:
- Base y área de servicio:
- Servicios (por prioridad):
- Servicio estrella / servicio a evitar:
- Diferenciadores:
- Ofertas sostenibles:
- Búsqueda de marca: sí/no/PENDIENTE

## Objetivo y economía
- Objetivo primario:
- Presupuesto mensual:
- Ticket promedio / margen:
- Capacidad (leads o trabajos/mes):
- **CPL máximo aceptable**: <calculado: margen por trabajo × tasa de cierre estimada × 0.3; anota el supuesto>
- Historial Google Ads:

## Operación
- Horario / 24-7:
- Respuesta a leads (quién, tiempo):
- Teléfono / call tracking:
- CRM (solo referencia):
- GBP: verificado sí/no, reseñas N (promedio X), acceso sí/no

## Competencia
| Competidor | URL | Nota |
|---|---|---|

## Web y tracking
- Plataforma / quién edita:
- Tag/GA4:
- Formulario → destino:
- Requisitos de política:

## LSA (solo US)
- Aplica: sí/no/PENDIENTE — motivo

## Pendientes
- [ ] ...
```

## Al terminar
1. Crea la carpeta desde `clients/_template/` (copia `checklist.md` vacío, `log/`, `data/`).
2. Resume en 5 líneas: nicho, geo, presupuesto, CPL máximo, pendientes bloqueantes.
3. Indica el siguiente paso: correr `/audit-landing`, `/competitors` y `/benchmark-interno` (pueden correr en paralelo con subagentes).
