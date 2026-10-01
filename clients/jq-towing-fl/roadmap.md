---
cliente: JQ Towing
slug: jq-towing-fl
D0: 2026-10-01
actualizado: 2026-10-01
fase_actual: 0
plan_es: https://claude.ai/artifact/48Lm7JkvRJCd57bqFy4B6Y
plan_en: https://claude.ai/artifact/4FBZLakgJxvFVybD57csmC
---

# Roadmap — JQ Towing (Belleview / Ocala, FL)

## Resumen
| Fase | Fecha estimada | Estado |
|---|---|---|
| 0 — Fundación | 2026-10-01 → 2026-10-15 | 🔄 en curso (bloqueada por inputs del cliente) |
| 1 — Lanzamiento Search | 2026-10-15 → 2026-10-22 | ⏳ |
| 2 — Limpieza D7 · D14 · D30 | 2026-10-22 · 2026-10-29 · 2026-11-14 | ⏳ |
| 3 — tCPA | ~2026-12-01 (rango 12-01 → 12-29) | ⏳ |
| 4 — Remarketing | No realista con el presupuesto actual | ⛔ (ver condición) |
| 5 — PMax | No califica con $879/mes | ⛔ |
| 6 — Conversiones offline | Fuera de alcance (sin CRM) | — |
| Pista Landing | 2026-10-01 → 2026-10-13 | 🔄 |
| Pista LSA | Solicitud 2026-10-01 → activa ~2026-10-29 | ⏳ (PENDIENTE requisitos) |

## Fase 0 — Fundación
- **Fecha estimada**: 2026-10-01 → 2026-10-15 (D0+14). Base de +3 días porque PMM crea las landings, más ~7–10 días porque depende de respuestas e insumos del cliente.
- **Condición de paso**: todas las tareas bloqueantes de Fase 0 en `checklist.md` ✅.
- **Tareas**:
  1. (Cliente) Ticket promedio, margen y tasa de cierre → CPL máximo. Si el CPL máximo queda por debajo de $25, se replantea la estrategia antes de construir.
  2. (Cliente) Aprobar call tracking (número de desvío de Google en anuncios y sitio).
  3. (Cliente) Confirmar la lista de servicios (lockout, jump, llanta, fuel, flatbed, golf cart, heavy duty) y los claims marcados con `*` en el copy.
  4. (Cliente) GBP: verificado, reseñas y acceso de administrador para PMM.
  5. (PMM) Conectar 986-810-9972 a Windsor o configurar la API, y leer historial, conversiones existentes y Auction Insights. Decide la puja inicial.
  6. (PMM) Permitir jqtowingfl.com en el entorno y re-correr `/audit-landing`.
  7. (PMM) Landings `/towing`, `/roadside-assistance` y `/thank-you` (ver pista Landing).
  8. (PMM) Conversiones: llamada desde anuncio ≥ 60 s, llamada al número de desvío del sitio ≥ 60 s y formulario como primarias; clic en `tel:` como secundaria. Probar con Tag Assistant.
  9. (PMM) Negativas: lista universal + `data/negatives-nicho.txt` (ajustar según los servicios confirmados).
  10. (PMM) Apagar la aplicación automática de recomendaciones; revisar facturación y acceso en la cuenta existente.
- **Riesgos**:
  - El cliente tarda en responder: es el factor que más mueve la fecha.
  - La cuenta previa puede tener conversiones mal configuradas (llamadas de 20 s, duplicadas) que haya que limpiar antes de lanzar.
  - Si el CPL máximo resulta < $25, la estrategia cambia.

## Fase 1 — Lanzamiento Search
- **Fecha estimada**: lanzamiento 2026-10-15; condición evaluable 2026-10-22.
- **Condición de paso**: campaña activa 7 días, anuncios aprobados y ≥ 1 conversión real registrada (llamada ≥ 60 s o formulario).
- **Qué se lanza**: `JQ | Search | Towing & Roadside | 15mi` a $29/día. Lleva 4 ad groups (golf cart solo si se confirma), radio de 15 mi en Presencia y horario 24/7.
- **Puja**: Maximizar conversiones si la cuenta previa trae conversiones; si no, Maximizar clics con CPC máx. $9 hasta ~10 conversiones (≤ 3 semanas).
- **Riesgos**:
  - **Aprendizaje lento**: el presupuesto de $29/día está por debajo de 3× CPL ($96).
  - **Volumen**: con CPC de ~$7 son ~4 clics/día.
  - **Speed to lead**: si de noche nadie contesta, se pierden las llamadas y el CPL se dispara. Se verifica con las llamadas perdidas en la revisión D7.

## Fase 2 — Limpieza
- **Fechas**: D7 2026-10-22 · D14 2026-10-29 · D30 2026-11-14.
- **Condición de paso**:
  - las tres revisiones hechas;
  - negativas aplicadas;
  - keywords con 0 impresiones en 30 días pausadas;
  - el peor RSA de cada grupo reemplazado;
  - reporte de calidad de leads del cliente recibido (D30).
- **Qué se revisa**:
  - search terms, con foco en motor clubs, impound, competidores locales, ciudades fuera del radio y "cheap/$50";
  - gasto sin conversión por ad group;
  - CPC real vs. el supuesto de $7;
  - llamadas perdidas o cortas.

## Fase 3 — Optimización de puja (tCPA)
- **Fecha estimada**: ~2026-12-01. **Supuesto**: $29/día ÷ CPL $32 = 0.9 conversiones/día → 33 días hasta 30 conversiones, +14 días porque el presupuesto queda por debajo de 3× CPL; lanzamiento 2026-10-15 + 47 días. Con el CPL de cuenta nueva ($59): 0.49 conversiones/día → 61 + 14 días → **2026-12-29**.
- **Condición de paso**: ≥ 30 conversiones en 30 días, con tracking verificado (llamadas ≥ 60 s).
- **Acción**: tCPA = CPA real de los últimos 30 días (×1.0–1.1). Si el impression share perdido por presupuesto supera el 30% y el CPA ≤ objetivo, proponer subir a ~$1,200/mes según la capacidad del cliente.
- **Si no se cumple en fecha**:
  - landing con conversión < 5% → corregir la landing;
  - CPC real > $9 → revisar keywords y presupuesto.
  - No forzar tCPA con menos datos.

## Fase 4 — Remarketing
- **Fecha estimada**: no realista con el presupuesto actual.
- **Condición de paso**: audiencia ≥ 1,000 usuarios en 30 días.
- **Por qué no se cumple**: ~125 clics de pago al mes y un sitio sin tráfico orgánico (no indexado) no llegan a 1,000. Además, en towing la compra es inmediata y casi no hay "visitante que vuelve".
- **Qué lo desbloquea**: más presupuesto (≥ ~$2,500/mes) o tráfico orgánico/GBP. Se reevalúa en D30 con el tamaño real de la audiencia.

## Fase 5 — Performance Max
- **Fecha estimada**: no califica.
- **Condiciones que fallan**:
  - **Presupuesto**: PMax necesita ≥ 3× CPA/día (~$96/día ≈ $2,900/mes solo para PMax) y su presupuesto es el 20–30% de Search.
  - **Conversiones**: ≥ 30/mes sostenidas con tCPA estable 4 semanas, como pronto en enero de 2027.
  - **Assets propios**: fotos, logo y video. Hoy son PENDIENTE.
- **Qué hacer**: quedarse en Search (+ LSA). Reevaluar solo si el presupuesto pasa de ~$3,500/mes.

## Fase 6 — Conversiones offline
- **Estado**: fuera de alcance (sin CRM). Mientras tanto, una hoja compartida donde el cliente marca qué leads cerraron (fecha, teléfono, servicio, monto) sirve para calidad de lead en D30.

## Pista paralela — Landing
| Tarea | Fecha | Responsable | Tipo |
|---|---|---|---|
| Habilitar acceso a jqtowingfl.com y re-auditar | 2026-10-02 | PMM (configuración de red del entorno) | Bloqueante |
| Decidir dónde viven las landings: sitio del cliente vs Leadpages (PMM) | 2026-10-05 | PMM + cliente | Bloqueante |
| `/towing`: H1 "24/7 Towing in Ocala & Belleview, FL", `tel:` sticky, formulario ≤ 4 campos, reseñas, área de servicio | 2026-10-09 | PMM | Bloqueante |
| `/roadside-assistance` (o sección dentro de /towing con H1 propio) | 2026-10-09 | PMM | Bloqueante |
| `/thank-you` con URL propia ("Keep your phone close — we'll call you in under 2 min") | 2026-10-09 | PMM | Bloqueante |
| Número de desvío en las landings + Google Tag + Tag Assistant | 2026-10-13 | PMM | Bloqueante |
| Fotos reales de las grúas y del equipo | 2026-10-13 | Cliente | Mejora (F2) |
| Indexar el sitio (revisar noindex/robots) para SEO/GBP a futuro | 2026-10-31 | Cliente / quien edite el sitio | Mejora (F2–3) |

## Pista paralela — LSA
- **2026-10-01**: confirmar licencia y seguro de grúa en FL, GBP verificado y disposición al background check (PENDIENTE).
- **2026-10-05**: iniciar la solicitud de Local Services (categoría Towing).
- **2026-10-15 → 2026-10-29**: verificación (2–4 semanas).
- **Luego**:
  - presupuesto semanal aparte (por definir con el cliente);
  - responder el 100% de los leads LSA (el ranking depende de la tasa de respuesta);
  - plan de reseñas para competir con Muggsuggs (+150).

## Estacionalidad y ventanas
- Florida no tiene estacionalidad de nieve. Picos esperados:
  - temporada de *snowbirds* (nov–abr), con más población en The Villages y Ocala;
  - verano (calor → baterías y sobrecalentamiento);
  - tormentas de la temporada de huracanes (hasta el 30 nov).
- Lanzar a mediados de octubre deja el aprendizaje hecho antes del pico de *snowbirds*. Es una hipótesis que hay que validar con el histórico de la cuenta 986-810-9972.

## Historial de cambios
- 2026-10-01: creado.
- 2026-10-01: plan ES/EN publicado (/informe).
