# Performance Max: cuándo sí y cómo

## Por qué no al inicio
PMax optimiza contra la señal de conversión que tenga. Sin historial, aprende de lo que Google considere "conversión" (spam de formularios, clics accidentales en Display, llamadas de 3 segundos). El resultado típico en servicios locales es volumen alto de leads basura y un CPA que parece bueno hasta que se cruza con ventas.

## Condiciones de entrada (todas deben cumplirse)
- [ ] Search lleva ≥4 semanas estable con tCPA activo y CPA dentro del objetivo.
- [ ] ≥30 conversiones/mes en la cuenta con tracking verificado (formulario + llamada ≥60s).
- [ ] Al menos un ciclo de limpieza de search terms completado (día 30).
- [ ] Assets propios disponibles: 5+ imágenes reales del negocio, logo, 1 video corto (aunque sea de fotos), 5 headlines y 5 descripciones probados en Search.
- [ ] Landing con conversión ≥5% y filtro anti-spam en formulario (honeypot/reCAPTCHA v3).
- [ ] Presupuesto: PMax necesita ≥3× el CPA objetivo por día para salir de aprendizaje en 2–3 semanas.

Si cualquiera falla, la fase queda bloqueada en `roadmap.md` con la razón.

## Configuración PMM para PMax en servicios locales
1. **Objetivo de conversión**: solo las conversiones primarias (formulario calificado, llamada ≥60s). Excluir vistas de página y clics de botón.
2. **Exclusión de marca**: lista de marca del cliente excluida para que PMax no canibalice tráfico de marca barato.
3. **Ubicación**: presencia solamente, misma geo que Search.
4. **URL expansion**: apagada, o limitada a las landings de servicio. Sin esto PMax manda tráfico a páginas de blog/carrera.
5. **Audience signals**: visitantes del sitio, convertidores, y custom segment con las keywords de intención de Search.
6. **Asset groups**: uno por servicio (misma lógica que las campañas de Search).
7. **Negativas**: pedir a Google Ads Rep la lista de negativas a nivel de cuenta aplicada a PMax (o usar las exclusiones de marca + placement exclusions). Excluir apps (mobileappcategory::69500) y placements de bajo valor.
8. **tCPA inicial**: 10–20% por encima del CPA real de Search. Ajustar semanalmente.
9. **Presupuesto inicial**: 20–30% del presupuesto de Search. Solo escalar si el CPA cruzado con calidad de lead se sostiene 2 semanas.

## Cómo evaluar si funcionó (semana 4 de PMax)
- CPA de PMax vs Search.
- % de leads calificados (el cliente los marca; sin CRM se hace con una hoja compartida).
- Insights de PMax: si >40% del gasto va a Display/YouTube y esos canales no traen leads calificados, apagar o bajar presupuesto.
- Si Search perdió impresiones de marca, la exclusión no está funcionando.

## Alternativa cuando no califica
Search + campaña de remarketing en Display (audiencia de visitantes, presupuesto pequeño, exclusión de apps). Da gran parte del beneficio con control total.
