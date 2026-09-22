# Playbook: Google Ads para servicios locales

Fuente: destilado de la masterclass "Automate Google Ads with Claude Code" (Jono, 2026) + criterio PMM. Lo que está aquí es lo que aplica a nuestra cartera; lo descartado se anota al final.

## 1. El embudo completo (los 5 eslabones)
Google Ads solo funciona si los cinco eslabones funcionan. Un fallo en cualquiera anula los demás:

1. **Anuncio** relevante al término buscado.
2. **Landing page** que refleja el término y convierte (formulario/llamada).
3. **Speed to lead**: contacto en <60 segundos en horario comercial. Llamar en el primer minuto multiplica ~4x el cierre (Velocify). Doble marcación.
4. **Venta**: script probado; llamadas más largas correlacionan con más cierre.
5. **Analítica** que conecta gasto → lead → venta.

PMM controla directamente 1, 2 y 5, pero el onboarding **debe preguntar** por 3 y 4 y dejarlos en el checklist como responsabilidad del cliente. Si el cliente no responde leads rápido, un CPL "bueno" no se convierte en dinero y la cuenta parece fallar.

## 2. Los tres lugares donde aparece un anuncio local
| Tipo | Dónde | Notas |
|---|---|---|
| Local Services Ads (LSA) | Bloque superior con badge "Google Guaranteed/Screened" | Solo ~70 categorías, principalmente US/CA. CPL ≈ mitad que Search. Requiere GBP, licencia, seguro, background check; verificación 2–4 semanas. No aplica en Colombia. |
| Search | Resultados con enlace a landing | El núcleo de lo que hacemos. |
| Google Maps | Anuncio en el pack de mapas | No es campaña aparte: Search + activo de ubicación vinculado a GBP. Siempre activarlo. |

**Regla LSA**: /onboard pregunta país y categoría. Si país=US y la categoría califica, el roadmap incluye "LSA setup" en paralelo a Search (proceso largo, arrancar día 1). Ranking LSA = gasto × tasa de respuesta × reseñas (cantidad, promedio, velocidad) × fotos.

## 3. Keyword research: intención o nada
Patrones de intención comercial para servicios locales:
- `[servicio] near me`, `[servicio] in/en [ciudad]`, `emergency [servicio]`, `24/7 [servicio]`, `same day`, `[servicio] open now`, `affordable/cheap [servicio]`, `[servicio] cost/price/quote`, `[problema específico] repair`.

Descartar: empleo (jobs, salary, apprenticeship, careers), educación (course, school, how to, DIY, tutorial), productos/equipos (parts, supplies, tool), gratis, y **nombres de competidores** (el clic llega, la venta no; el usuario ya tiene referido).

Proceso: Keyword Planner vía API con la ciudad del cliente (nunca país completo) + Semrush `keyword_research` y `paid_search_research` de competidores. Guardar en `clients/<slug>/data/keywords.csv` con volumen, CPC estimado y clasificación intención/descartar.

## 4. Match types
- **Amplia**: no por defecto. Google arrastra búsquedas ajenas. Solo con tCPA maduro y aprobación.
- **Frase**: default PMM. Captura variantes de la intención sin perder control.
- **Exacta**: para los 3–5 términos de mayor volumen e intención de cada grupo, en el mismo ad group o en uno espejo con puja mayor.

## 5. Estructura: SKAG → STAG
Principio: **el término buscado debe aparecer en el anuncio y en la landing**. Estructura:
- Campaña por **servicio** (Emergency Plumbing, Drain Cleaning…).
- Ad group por **servicio × ciudad** cuando cada combinación tiene volumen (>~100 búsquedas/mes). Si no, ad group por servicio con la ciudad en el copy vía inserción de ubicación o un grupo por región.
- Landing por servicio (mínimo) o por servicio × ciudad (ideal, generadas en lote).
- Saltar combinaciones con ~0 búsquedas: no vale la pena mantenerlas.

## 6. Configuración de campaña (los 9 ajustes)
1. Red: solo Búsqueda. Sin socios de búsqueda ni Display.
2. Puja: Maximizar conversiones → tCPA al madurar. El objetivo final es cliente pagado, no "conversiones".
3. Programación: horario comercial + 1h de margen. 24/7 solo si el cliente responde 24/7 (o tiene recepcionista IA). Leads nocturnos son más baratos pero cierran menos si nadie contesta.
4. Ubicación: **Presencia** solamente, radio real de servicio (~50 km o ciudades explícitas). Excluir los demás países.
5. Dispositivos: todos.
6. Audiencias: sin exclusiones en Search.
7. Recomendaciones automáticas: apagadas.
8. Rotación de anuncios: optimizar.
9. Idioma: el del mercado.

## 7. Anuncios (RSA)
- 3 RSA por ad group como mínimo para split test.
- Headline 1 **pinneado** = término del grupo (ej. "Emergency Plumber Toronto").
- Headlines 2–15: oferta, urgencia, confianza (licensed & insured, X reviews, same-day, free quote, no call-out fee).
- 4 descripciones con CTA.
- Nombre de negocio y logo.
- Extensiones: sitelinks a otros servicios, callouts de beneficios, snippets estructurados, llamada, ubicación. Apiladas pueden dar +20–25% de CTR.
- Imágenes solo si son del negocio y de calidad. Stock genérico puede bajar conversión.
- URL final debe responder 200 antes de publicar o el anuncio será rechazado.

## 8. Negativas
Lista universal a nivel de cuenta desde día 1 (`knowledge/negativas-universales.md`) + lista por nicho + revisión de search terms días 7, 14, 30 y luego semanal.

## 9. Landing page: los golpes más fuertes
En orden de impacto observado por el autor (CPL de $200 → $30):
1. Video testimonios de clientes.
2. Formulario visible arriba, corto.
3. Video del fundador (+33% leads en su caso).
4. Headline = término de búsqueda.
5. Oferta clara y diferenciada.
6. Prueba social: reseñas, logos, cantidad de trabajos.
7. Clic para llamar en móvil.
8. Página de gracias que prepara la llamada: "Ten tu teléfono listo, te llamamos en 75 segundos".
Meta: 15–20% de conversión landing→lead está en el percentil alto.

## 10. Tracking y remarketing
- Google Tag en toda la landing; conversión de formulario y de llamada. Verificar con Tag Assistant simulando envío.
- UTMs + GCLID en campos ocultos del formulario para trazar keyword → lead → venta.
- Audiencia de visitantes del sitio: ~90% del gasto a frío, ~10% a remarketing. Un visitante recurrente convierte hasta 3x más.
- Conversiones offline (subir GCLIDs de clientes pagados) enseñan a Google qué es un cliente rentable. Fase futura en PMM (sin CRM por ahora); documentar en roadmap.

## 11. Performance Max y Display
El autor gastó ~$10k/mes en PMax y recibió spam y clics accidentales. Para servicios locales: PMax solo con conversiones sólidas (30+/mes), Search estable, exclusión de marca, ubicaciones excluidas y assets propios. Display puro: no. Ver `pmax-cuando-y-como.md`.

## 12. Analítica que sí importa
Cruzar leads (por teléfono/GCLID) con cierres para saber: tipo de trabajo que más cierra, ciudad, canal (llamada vs formulario vs mensaje), día y hora. Con eso se recortan servicios que no cierran y se reasigna presupuesto. Windsor.ai + exports de la API alimentan el dashboard.

## Descartado o adaptado del video
- Blueprints pagos del autor (CRO, GoHighLevel): reemplazados por `knowledge/` propio de PMM.
- Flujo de reseñas con Next.js + Make.com: fuera del alcance Google Ads; se anota como recomendación al cliente.
- LSA: solo aplica a parte de la cartera US.
- Escala de presupuesto del autor: nuestros clientes locales operan con presupuestos menores; ajustar umbrales de conversiones a la realidad de cada cuenta.
