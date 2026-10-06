from build_common import NEGC, NEG_TOTAL, UNI, KW_ACTIVE

BODY = r'''<div class="wrap">
  <header class="mast">
    <div>
      <span class="logo"><img src="@@LOGO@@" alt="Performance Media Marketing"></span>
      <h1>Jerry's Auto Body Solutions &amp; Towing Service</h1>
      <p class="sub">Plan de Google Ads: diagnóstico de la cuenta activa, reestructura, fechas y checklist para pasar de un CPL de $38.50 con medición sin verificar a ≤ $30 con leads confirmados.</p>
      <p style="margin-top:8px; font-size:.88rem"><a href="@@URL_OTHER@@">English version →</a></p>
    </div>
    <dl class="meta">
      <dt>Cuenta</dt><dd class="mono">523-801-4243</dd>
      <dt>MCC</dt><dd class="mono">444-523-7672</dd>
      <dt>Mercado</dt><dd>Wesley Chapel, FL (Pasco) · radio 20 mi · EN (+ ES condicional)</dd>
      <dt>D0</dt><dd class="num">01-oct-2026</dd>
      <dt>Fase actual</dt><dd><span class="chip st-block">Fase 0 · bloqueada</span></dd>
      <dt>Actualizado</dt><dd class="num">06-oct-2026</dd>
    </dl>
  </header>

  <nav class="toc" aria-label="Secciones">
    <a href="#resumen">Resumen</a><a href="#evolucion">Evolución</a><a href="#pasos">Próximos pasos</a><a href="#fechas">Fechas</a><a href="#estrategia">Estrategia</a><a href="#anuncios">Anuncios</a><a href="#negativas">Negativas</a><a href="#landing">Landing</a><a href="#mercado">Mercado</a><a href="#checklist">Checklist</a><a href="#cliente">Cliente</a><a href="#porque">Por qué no</a>
  </nav>

  <section id="resumen">
    <div class="sec-head"><h2>Resumen</h2><p>Grúa local y familiar 24/7 en 3645 New River Rd, Wesley Chapel, FL: light y medium-duty towing, accidentes, recuperación y roadside. Objetivo: llamadas ≥60 s y formularios.</p></div>
    <div class="kpis">
      <div class="kpi"><b>$760</b><span>pauta/mes del plan · $25/día (contrato $1,500); desde el 01-oct: Search $22 + PMax $5</span></div>
      <div class="kpi"><b>$30–40</b><span>CPL objetivo F1 · Search de Fishhawk (Tampa) ~$31 · meta F2 ≤ $30</span></div>
      <div class="kpi"><b>~15–22</b><span>prospectos/mes, escenario base (~94 clics a $8.06)</span></div>
      <div class="kpi"><b>13-oct</b><span>relanzamiento con la estructura nueva (reprogramado: Fase 0 bloqueada)</span></div>
    </div>

    <div class="two">
      <div>
        <p class="eyebrow">Estado de la cuenta hoy</p>
        <h3 style="margin:6px 0 10px">$1,214.89 gastados, 169 clics, 27 conversiones (22-ago → 05-oct)</h3>
        <p>Septiembre cerró con 18 conversiones y CPL de $38.50 (agosto: $108.28); la semana del 29-sep, 6 conversiones a $32.84. Pero <b>Form Fill no registra nada desde el 14-sep</b> y el 01-oct se creó una <b>PMax de $5/día</b> fuera del plan. Las 3 acciones de conversión son primarias y ninguna está verificada: si "Website Calls" (9 de 21) es un clic en <span class="mono">tel:</span>, el CPL real pasa de $60. El ad group en español gastó $308.09 (30%) con 3 conversiones. 13 de 21 keywords están en broad. De los search terms visibles, <b>$87.08 de $629.42</b> fueron a competidores, servicios públicos, aseguradoras, fuera de área o servicios que no ofrece.</p>
        <div class="bar-spend" role="img" aria-label="Distribución de $629.42 en search terms visibles">
          <i style="width:85.4%; background:var(--green)"></i><i style="width:6.1%; background:var(--orange)"></i><i style="width:5.3%; background:var(--red)"></i><i style="width:2.4%; background:var(--purple)"></i><i style="width:0.8%; background:var(--sky)"></i>
        </div>
        <div class="legend">
          <span style="--c:var(--green)">Intención de servicio $537.40 (16 conv.)</span>
          <span style="--c:var(--orange)">Competidores $38.26</span>
          <span style="--c:var(--red)">Road Rangers / aseguradoras $33.25</span>
          <span style="--c:var(--purple)">Fuera de área / servicio no ofrecido $15.57</span>
          <span style="--c:var(--sky)">Marca propia $4.95</span>
        </div>
        <p class="muted" style="font-size:.85rem; margin-top:6px">Search terms del 22-ago al 28-sep. Visible: $629.42 de $1,017.83 (62%); el resto Google lo oculta por privacidad. "Fuera de área" = Farmingdale NY ($5.85); "no ofrecido" = RV transport ($9.72).</p>
      </div>
      <div class="callout">
        <h3>La decisión en cinco líneas</h3>
        <ul>
          <li><b>Campañas</b> 1 Search: se reestructura la actual, no se crea otra, para conservar las 21 conversiones y el aprendizaje.</li>
          <li><b>Ad groups</b> 4 + Grúa ES condicional (límite de fragmentación: $600–1,500/mes → 1 campaña, 3–5 grupos).</li>
          <li><b>Puja y match</b> Max. conversiones si la medición se confirma (si quedan &lt;15 conv./mes reales, Max. clics con tope de $10); frase + exacta; Presencia, radio 20 mi; 24/7 si alguien contesta de noche.</li>
          <li><b>El techo con este presupuesto</b> ~15–22 conv./mes; tCPA pide 30 → solo con ~$35/día (decisión después de la Fase 2, ~01-dic).</li>
          <li><b>Qué no se hace</b> PMax (la creada el 01-oct no cumple condiciones: recomendación, pausarla), Display, remarketing, marca. LSA solo si hay GBP y la categoría califica.</li>
        </ul>
      </div>
    </div>
    <div style="margin-top:24px">
      <p class="eyebrow">Matemática de presupuesto (playbook §4)</p>
      <h3 style="margin:6px 0 10px">$25/día ÷ CPC $8.06 ≈ 3.1 clics/día → ~94 clics/mes</h3>
      <div class="tbl"><table>
        <thead><tr><th>Escenario</th><th class="r">Tasa conv.</th><th class="r">Prospectos/mes</th><th class="r">CPL</th><th>Referencia</th></tr></thead>
        <tbody>
          <tr><td>Conservador</td><td class="r">12%</td><td class="r">~11</td><td class="r">~$69</td><td>Si "Website Calls" resulta ser clics y se descuentan</td></tr>
          <tr><td><b>Base</b></td><td class="r"><b>16–24%</b></td><td class="r"><b>~15–22</b></td><td class="r"><b>~$35–51</b></td><td>Septiembre: 20.9% y CPL $38.50</td></tr>
          <tr><td>Optimista</td><td class="r">32%</td><td class="r">~30</td><td class="r">~$25</td><td>Search de Fishhawk Towing (Tampa) en 90 días</td></tr>
        </tbody>
      </table></div>
      <p class="muted" style="font-size:.86rem; margin-top:8px">Max. conversiones pide 15+ conv./mes limpias (se cumple solo si la medición se confirma). tCPA pide ~30 en 30 días: ~$1,050/mes ($35/día) a CPL $35, o ~$900 a $30.</p>
    </div>
  </section>

  <section id="evolucion">
    <div class="sec-head"><h2>Evolución · semana 7 (29-sep → 05-oct)</h2><p>Search "ENHPRM Radius" y la PMax creada el 01-oct. ¿Avanzó la Fase 0 y qué cambió en la cuenta?</p></div>
    <div class="kpis">
      <div class="kpi"><b>$197.06</b><span>gasto en 7 días · Search $174.54 + PMax $22.51 · octubre a ritmo de ~$885</span></div>
      <div class="kpi"><b>39</b><span>clics · Search 23 (CTR 10.3%) · PMax 16 (CTR 1.4%)</span></div>
      <div class="kpi"><b>$7.59</b><span>CPC de Search ($9.05 la semana anterior) · PMax $1.41</span></div>
      <div class="kpi"><b>6</b><span>conversiones · CPL $32.84 · 3 Calls from Ads, 3 Website Calls (1 de PMax), 0 formularios</span></div>
    </div>
    <div class="two">
      <div style="min-width:0">
        <p class="eyebrow">La causa</p>
        <h3 style="margin:6px 0 10px">Form Fill lleva 22 días en cero mientras las llamadas siguen: es medición, no demanda</h3>
        <div class="bar-spend" role="img" aria-label="Visible vs oculto"><i style="width:65.1%; background:var(--sky)"></i><i style="width:34.9%; background:var(--surface-2)"></i></div>
        <div class="legend"><span style="--c:var(--sky)">Visible en search terms $113.63</span><span style="--c:var(--surface-2)">Oculto por privacidad $60.91</span></div>
        <div class="tbl" style="margin-top:14px"><table>
          <thead><tr><th>Día</th><th class="r">Impr.</th><th class="r">Clics</th><th class="r">Costo</th><th class="r">CPC</th><th class="r">IS</th><th class="r">Perdido ranking</th><th class="r">Perdido presup.</th></tr></thead>
          <tbody>
            @@DAILY@@
          </tbody>
        </table></div>
        <div class="tbl" style="margin-top:14px"><table>
          <thead><tr><th>Ad group</th><th class="r">Impr.</th><th class="r">Clics</th><th class="r">CTR</th><th class="r">Costo</th><th class="r">% gasto</th></tr></thead>
          <tbody>
            <tr><td>Ad group 1 - English (3 conv., CPL $28.49)</td><td class="r">168</td><td class="r">10</td><td class="r">6.0%</td><td class="r">$85.46</td><td class="r">43%</td></tr>
            <tr><td>Ad group 2 - Spanish (2 conv., CPL $44.54)</td><td class="r">55</td><td class="r">13</td><td class="r">23.6%</td><td class="r">$89.09</td><td class="r">45%</td></tr>
            <tr><td>P. Max (1 conv. Website Calls)</td><td class="r">1,143</td><td class="r">16</td><td class="r">1.4%</td><td class="r">$22.51</td><td class="r">11%</td></tr>
          </tbody>
        </table></div>
        <p class="muted" style="font-size:.86rem; margin-top:8px">Formularios por período: 6 del 22-ago al 14-sep; 0 del 15-sep al 05-oct (con 14 conversiones de llamada). Search terms visibles: desperdicio claro "road ranger" $6.15; dudoso "costo de una grua para auto" $7.00. La PMax gastó en tablet y connected TV.</p>
      </div>
      <div class="callout" style="min-width:0">
        <h3>Diagnóstico</h3>
        <ul>
          <li><b>Medición:</b> Form Fill en cero desde el 14-sep (antes, 1 cada ~3 días). La única conversión de la PMax es Website Calls, la acción sin verificar.</li>
          <li><b>Volumen:</b> 23 clics de Search en la semana: el CPL de $34.91 es ruido semana a semana; el de 28 días ($33.74) sí sirve de referencia.</li>
          <li><b>Cambios fuera del plan:</b> PMax de $5/día y Search de $25 → $22 el 01-oct; "gruero cerca de mi" agregada en broad. Las negativas no se aplicaron ("road ranger" volvió a gastar).</li>
          <li><b>Puja/CPC:</b> no se toca. IS perdido por ranking 45%: la palanca es la landing y las reseñas, no la puja.</li>
          <li><b>Qué hacer:</b> 1) revisar el disparador del formulario en GTM; 2) decidir la PMax; 3) negativas; 4) reestructura el 13-oct.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="pasos">
    <div class="sec-head"><h2>Próximos pasos</h2><p>Lo que falta para cerrar la Fase 0 y relanzar el 06-oct. Los que dicen B bloquean.</p></div>
    <div class="steps" id="steps"></div>
  </section>

  <section id="fechas">
    <div class="sec-head"><h2>Fechas y fases</h2><p>La fecha es proyección; la condición de paso manda. Nunca se avanza "porque ya es la fecha".</p></div>
    <div class="tl-wrap"><div class="tl" id="timeline"></div></div>
    <div class="phases" id="phases"></div>
  </section>

  <section id="estrategia">
    <div class="sec-head"><h2>Estrategia</h2><p>Una campaña con 4 grupos por intención, porque $25/día no sostiene más y "near me" es casi toda la demanda (las ciudades tienen ~0 búsquedas).</p></div>
    <dl class="cfg">
      <div><dt>Campaña</dt><dd>Towing - Search - Radius (la actual, renombrada)</dd></div>
      <div><dt>Tipo</dt><dd>Search · solo red de Búsqueda (confirmado)</dd></div>
      <div><dt>Presupuesto</dt><dd class="num">$25/día (~$760/mes) en el plan · hoy Search $22 + PMax $5</dd></div>
      <div><dt>Puja</dt><dd>Max. conversiones → si la medición limpia deja &lt;15 conv./mes, Max. clics con tope $10 → tCPA con ≥30 conv./30 días</dd></div>
      <div><dt>Conversiones</dt><dd>Calls from Ads ≥60 s + formulario en /thank-you/; Website Calls solo si es desvío de Google (si es clic en tel:, secundaria)</dd></div>
      <div><dt>Match</dt><dd>Frase + exacta en los términos top · sin broad (13 keywords migran)</dd></div>
      <div><dt>Ubicación</dt><dd>Presencia · radio 20 mi desde 3645 New River Rd · resto de países excluidos</dd></div>
      <div><dt>Horario</dt><dd>24/7 si alguien contesta de noche; si no, 6:00–23:00 (hora del Este, igual que la cuenta)</dd></div>
      <div><dt>Apagado</dt><dd>Socios de búsqueda, Display, recomendaciones automáticas</dd></div>
    </dl>
    <div class="tbl"><table>
      <thead><tr><th>Ad group</th><th>Fase</th><th>Keywords principales</th><th class="r">Vol. US/mes*</th><th>Landing</th></tr></thead>
      <tbody id="agrows"></tbody>
    </table></div>
    <p class="muted" style="font-size:.88rem; margin-top:10px">* Volumen nacional de Semrush (no hay Keyword Planner por ciudad); dentro del radio es una fracción mínima. Zephyrhills, Dade City y Land O' Lakes tienen ~0 búsquedas: se cubren con radio + "near me", sin grupos por ciudad. Grúa ES se activa solo si contestan en español y existe una página en español.</p>

    <h3 style="margin-top:28px; margin-bottom:10px">Presupuesto por fase</h3>
    <div class="tbl"><table>
      <thead><tr><th>Fase</th><th>Total/mes</th><th>Qué pasa</th><th>Condición para pasar</th></tr></thead>
      <tbody>
        <tr><td><b>F0</b> Saneamiento</td><td class="num">$760</td><td>Medición, negativas, geo con la campaña corriendo</td><td>Conversiones verificadas, negativas, Presencia</td></tr>
        <tr><td><b>F1</b> Estabilizar</td><td class="num">$760</td><td>Estructura nueva, 1 RSA por grupo</td><td>4 semanas con CPL ≤ $40 y ≥50% de leads reales</td></tr>
        <tr><td><b>F2</b> Optimizar</td><td class="num">$760</td><td>Pausar los grupos de peor CPL</td><td>CPL ≤ $30 por 4 semanas; IS perdido por presupuesto &gt; 20%</td></tr>
        <tr><td><b>F3</b> Escalar</td><td class="num">$900–1,050</td><td>$30–35/día (requiere subir el paquete) + Medium-Duty / Collision si se confirman</td><td>~30 conv./30 días → tCPA a CPL real +10%</td></tr>
        <tr><td><b>F4</b> Remarketing</td><td class="num">+10%</td><td>Audiencia de visitantes en observación</td><td>Lista ≥1,000 usuarios (con este tráfico, &gt;6 meses)</td></tr>
        <tr><td><b>F5</b> PMax</td><td class="num">—</td><td>No califica</td><td>Ver "Por qué no"</td></tr>
      </tbody>
    </table></div>
  </section>

  <section id="anuncios">
    <div class="sec-head"><h2>Anuncios</h2><p>1 RSA por ad group (máx. 2): con ~94 clics/mes un A/B es ruido (CLAUDE.md #4). H1 pinneado a la keyword del grupo; se escribieron 3 variantes (rapidez, precio, confianza) y se activa la de rapidez.</p></div>
    <div class="adgrid">
@@SERP@@
    </div>
    <div class="two" style="margin-top:22px">
      <div>
        <h3 style="margin-bottom:8px">H1 pinneado por ad group</h3>
        <div class="tbl"><table><tbody id="h1rows"></tbody></table></div>
      </div>
      <div>
        <h3 style="margin-bottom:8px">Headlines compartidas</h3>
        <ul class="pool" id="pool"></ul>
        <h3 style="margin:16px 0 8px">Descripciones (Towing Near Me; cada grupo tiene sus 4)</h3>
        <ul style="margin:0; padding-left:1.1em; font-size:.93rem" id="descs"></ul>
      </div>
    </div>
    <div class="callout" style="margin-top:22px">
      <h3>Extensiones</h3>
      <ul>
        <li><b>Llamada</b> (813) 381-0435, número de desvío de Google, 24/7 o según el horario que confirme el cliente</li>
        <li><b>Sitelinks</b>: Towing Near You, Roadside Assistance, Get a Free Quote, Accident Towing</li>
        <li><b>Callouts</b>: Available 24/7, Family-Owned, Free Quotes, Upfront Pricing, No Hidden Fees, Local to Wesley Chapel, Light &amp; Medium-Duty, You Choose Destination</li>
        <li><b>Snippet</b>: Servicios: Towing, Accident Towing, Vehicle Recovery, Jump Starts, Flat Tire Change, Fuel Delivery, Medium-Duty Towing</li>
        <li><b>Ubicación / imágenes</b>: ubicación bloqueada hasta tener GBP; imágenes solo con fotos reales de las grúas (sin stock)</li>
        <li><b>No se promete</b>: licensed &amp; insured, tiempo de llegada, cantidad de reseñas ni años de experiencia, hasta que el cliente los confirme</li>
      </ul>
    </div>
  </section>

  <section id="negativas">
    <div class="sec-head"><h2>Negativas</h2><p>Propuestas, sin aplicar: esperan el OK de Jhombis (vía /negatives). Nada se escribe en la cuenta sin aprobación.</p></div>
    <div class="two" style="margin-top:0">
      <div>
        <h3 style="margin-bottom:12px">@@NEGTOTAL@@ de nicho + @@UNI@@ universales (pendiente de OK)</h3>
        <div class="negbars" id="negbars"></div>
        <p class="muted" style="font-size:.86rem; margin-top:12px">Validadas contra las @@KW@@ keywords que quedan activas: 0 choques. Archivos:</p>
        <p class="muted" style="font-size:.86rem"><span class="mono">data/negatives-nicho.txt</span> · <span class="mono">data/2026-09-29-negatives.txt</span></p>
      </div>
      <div class="callout">
        <h3>Choques evitados</h3>
        <p style="margin-top:8px"><span class="kw">county</span> <span class="kw">cheapest</span> <span class="kw">insurance claim</span> <span class="kw">phone number</span></p>
        <p style="font-size:.9rem; color:var(--ink-2); margin-top:8px">Universales que NO se aplican en esta cuenta: "county" bloquearía "pasco county towing" (grupo Wesley Chapel); "cheapest" bloquearía "cheapest towing near me", que convirtió; "insurance claim" puede ser un accidente; "phone number" suelto bloquearía "towing service phone number". Tampoco se niega "jerry"/"jerrys" (marca propia).</p>
      </div>
    </div>
  </section>

  <section id="landing">
    <div class="sec-head"><h2>Landing</h2><p>11/22 · requiere ajustes antes del relanzamiento. Bloquea la página de gracias; la prueba social en 0 es mejora, no bloqueo (rúbrica de /audit-landing).</p></div>
    <div class="two" style="margin-top:0">
      <div>
        <div class="rub" id="rubric"></div>
        <p class="muted" style="font-size:.86rem; margin-top:8px">jerrystowingservice.com: una sola página (WordPress + Elementor, 08-2026), sin H1, formulario de 6 campos al final, 16 enlaces tel: y header fijo. Velocidad sin medir (PageSpeed sin clave).</p>
      </div>
      <div>
        <h3 style="margin-bottom:8px">Landings que se necesitan</h3>
        <div class="tbl"><table>
          <thead><tr><th>URL</th><th>Estado</th><th>Para</th></tr></thead>
          <tbody>
            <tr><td class="mono">/thank-you/</td><td><span class="chip st-block">Crear · B</span></td><td>Medición del formulario (F0)</td></tr>
            <tr><td class="mono">/</td><td><span class="chip st-todo">Mejora</span></td><td>H1, formulario de 3 campos, reseñas · Towing Near Me, Cheap, Wesley Chapel</td></tr>
            <tr><td class="mono">/roadside-assistance/</td><td><span class="chip st-todo">Crear</span></td><td>Roadside Assistance (mientras tanto /#roadside)</td></tr>
            <tr><td class="mono">/es/</td><td><span class="chip st-block">Crear si contestan ES</span></td><td>Grúa ES</td></tr>
            <tr><td class="mono">/medium-duty-towing/</td><td><span class="chip st-pause">Condicional</span></td><td>F3, si lo confirman</td></tr>
            <tr><td class="mono">/collision-repair/</td><td><span class="chip st-pause">Condicional</span></td><td>F3, si hacen carrocería</td></tr>
          </tbody>
        </table></div>
      </div>
    </div>
  </section>

  <section id="mercado">
    <div class="sec-head"><h2>Benchmark y competencia</h2><p>28 cuentas de towing US del MCC, 90 días (Windsor). Tampa es mercado caro: Jerry's paga $8 por clic contra la mediana de $4.87, y su CPL está en línea con el comparable de la zona.</p></div>
    <div class="tbl"><table>
      <thead><tr><th>Cuenta</th><th>Mercado</th><th>Puja</th><th class="r">CPC</th><th class="r">Tasa conv.</th><th class="r">CPL</th><th class="r">Conv./mes</th></tr></thead>
      <tbody>
        <tr><td>A (anonimizada)</td><td>Tampa, FL · paquete ENHPRM</td><td>Max. conv. + PMax</td><td class="r">$5.94</td><td class="r">17.8%</td><td class="r"><b>$33.29</b></td><td class="r">24</td></tr>
        <tr><td>B (anonimizada)</td><td>US · paquete $2,500</td><td>Max. conv. + PMax</td><td class="r">$3.72</td><td class="r">38.6%</td><td class="r"><b>$9.64</b></td><td class="r">151</td></tr>
        <tr><td>C (anonimizada)</td><td>US · paquete $1,399</td><td>Max. conv.</td><td class="r">$4.51</td><td class="r">37.2%</td><td class="r"><b>$12.13</b></td><td class="r">56</td></tr>
        <tr><td>D (anonimizada)</td><td>US · paquete $1,600</td><td>Max. conv. + PMax</td><td class="r">$4.46</td><td class="r">24.9%</td><td class="r"><b>$17.88</b></td><td class="r">38</td></tr>
        <tr><td>E (anonimizada)</td><td>US · paquete $1,500</td><td>Max. conv.</td><td class="r">$6.80</td><td class="r">16.4%</td><td class="r"><b>$41.39</b></td><td class="r">19</td></tr>
        <tr><td>F (anonimizada)</td><td>US · paquete $1,500</td><td>Max. conv.</td><td class="r">$11.22</td><td class="r">25.8%</td><td class="r"><b>$43.56</b></td><td class="r">17</td></tr>
        <tr><td>Mediana MCC (20 cuentas maduras)</td><td>US</td><td>—</td><td class="r">$4.87</td><td class="r">28.1%</td><td class="r"><b>$14.59</b></td><td class="r">42</td></tr>
        <tr><td><b>JERRY'S (sep)</b></td><td>Wesley Chapel, FL</td><td>Max. conv.</td><td class="r"><b>$8.06</b></td><td class="r">20.9%</td><td class="r"><b>$38.50</b></td><td class="r">18</td></tr>
      </tbody>
    </table></div>
    <p class="muted" style="font-size:.86rem; margin-top:8px">Tasas de 38–50% en el MCC probablemente cuentan clics en el teléfono como conversión: el CPL del MCC está subestimado. En A, las keywords "near me" en Search cuestan ~$10 por clic; el promedio lo baja PMax.</p>

    <div class="two">
      <div>
        <h3 style="margin-bottom:8px">Competidores en Wesley Chapel / Pasco</h3>
        <div class="tbl"><table>
          <thead><tr><th>Competidor</th><th>Tipo</th><th>Ángulo</th></tr></thead>
          <tbody>
            <tr><td>B&amp;D Towing &amp; Recovery</td><td>Local, Tampa</td><td>"Fast and affordable 24/7"; página por ciudad</td></tr>
            <tr><td>Pasco Towing Inc</td><td>Local, Pasco</td><td>"Fast and affordable 24/7"; página por ciudad</td></tr>
            <tr><td>towingwesleychapel.com</td><td>Dominio con la keyword</td><td>Probable lead-gen</td></tr>
            <tr><td>dependabletowwesleychapel.com</td><td>Dominio con la keyword</td><td>Probable lead-gen, 24/7</td></tr>
            <tr><td>DRIVE Roadside · True Towing · 24hr-towing</td><td>Agregadores nacionales</td><td>24/7, red nacional; pujan fuerte en "near me"</td></tr>
          </tbody>
        </table></div>
        <p class="muted" style="font-size:.86rem; margin-top:8px">Semrush no tiene anuncios locales de estos dominios; reseñas sin relevar.</p>
      </div>
      <div class="callout">
        <h3>Oportunidades</h3>
        <ul>
          <li><b>Español</b> en A, "servicio de grua" y "grua cerca de mi" convierten a $19–25, con una página en español.</li>
          <li><b>Medium-duty</b> box trucks y flotas: ticket alto y pocos agregadores.</li>
          <li><b>Local y familiar</b> contra redes nacionales que subcontratan, si se respalda con reseñas.</li>
        </ul>
        <h3 style="margin-top:14px">Amenazas</h3>
        <ul>
          <li>Agregadores en "near me": CPC real ~$10, 2.5–3× lo que muestra Semrush.</li>
          <li>Sin GBP ni reseñas: sin map pack, sin activo de ubicación y sin LSA.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="checklist">
    <div class="sec-head"><h2>Checklist</h2><p>Espejo de <span class="mono">clients/jerrys-towing-wesley-chapel/checklist.md</span> al 01-oct. /weekly-review lo mantiene al día.</p></div>
    <div class="filters" role="group" aria-label="Filtros">
      <div class="grp"><span class="lab">Responsable</span><span id="f-who"></span></div>
      <div class="grp"><span class="lab">Estado</span><span id="f-st"></span></div>
    </div>
    <div id="cl"></div>
  </section>

  <section id="cliente">
    <div class="sec-head"><h2>Pendientes del cliente</h2><p>Lo que hay que pedirle a Jerry's. Los marcados con B bloquean una parte del plan.</p></div>
    <div class="two" style="margin-top:0">
      <ol class="qlist" id="qlist"></ol>
      <div class="callout">
        <h3>Mensaje listo para enviar (EN)</h3>
        <p style="font-size:.9rem; color:var(--ink-2)">Para mandarle al cliente por email o texto.</p>
        <textarea class="copyarea" id="clientmsg" readonly aria-label="Mensaje para el cliente"></textarea>
        <div style="display:flex; gap:10px; align-items:center; margin-top:8px"><button class="copybtn" id="copybtn" type="button">Copiar mensaje</button><span id="copystate" class="muted" style="font-size:.85rem" aria-live="polite"></span></div>
      </div>
    </div>
  </section>

  <section id="porque">
    <div class="sec-head"><h2>Por qué no (todavía)</h2></div>
    <div class="why">
      <div><h4>Performance Max</h4><p>Se creó una de $5/día el 01-oct, fuera del plan (5 días: $22.51, 16 clics, 1 conv. Website Calls); recomendación: pausarla. Falla 5 de 6 condiciones: sin tCPA estable, ~18 conv./mes sin verificar, sin fotos ni video propios, sin anti-spam y $25/día contra ~$115 que pide.</p></div>
      <div><h4>Broad</h4><p>Ya se ve su costo: búsquedas de NY, OH y AZ, Road Rangers, aseguradoras y competidores. "tow truck near me" en frase: CPL $13.77; en broad: $41.74.</p></div>
      <div><h4>Display / Demand Gen</h4><p>Servicio de urgencia: nadie contrata una grúa desde un banner.</p></div>
      <div><h4>Campaña de marca</h4><p>"jerrys towing": 1–3 impresiones en 38 días. No hay demanda de marca.</p></div>
      <div><h4>Remarketing</h4><p>~94 clics/mes y dominio nuevo: la audiencia no llega a 1,000 en 30 días. En towing la necesidad es inmediata.</p></div>
      <div><h4>Grupos por ciudad</h4><p>Zephyrhills, Dade City y Land O' Lakes tienen ~0 búsquedas; "towing wesley chapel" ~30/mes. Radio + "near me" cubre la demanda.</p></div>
    </div>
    <div class="callout" style="margin-top:22px">
      <h3>Riesgos y supuestos</h3>
      <ul>
        <li><b>Economía:</b> con un tow supuesto de $125 y margen del 50%, el CPL "cómodo" es ~$11 y el de equilibrio ~$37. Un CPL de $30–40 puede no ser rentable.</li>
        <li><b>Medición:</b> si "Website Calls" es un clic, el CPL real pasa de $60 y Max. conversiones aprende de la señal equivocada.</li>
        <li><b>Varianza:</b> ~3 clics/día: una semana sin conversiones es normal; no reaccionar antes del D14.</li>
        <li><b>Huracanes (hasta 30-nov) y snowbirds (nov–abr):</b> picos de demanda; tener lista una subida temporal de presupuesto con OK del cliente.</li>
        <li><b>Supuestos:</b> radio de 20 mi, atención 24/7 y servicios del sitio, sin confirmar con el cliente.</li>
      </ul>
    </div>
  </section>

  <footer>
    <span>Performance Media Marketing · Jerry's Auto Body Solutions &amp; Towing Service · cuenta 523-801-4243</span>
    <span>Fuentes: brief, audit-site, benchmark, competitors, strategy, roadmap, checklist y logs 2026-09-29 y 2026-10-06 · Windsor 22-ago → 05-oct-2026 · Semrush US</span>
  </footer>
</div>'''

DATA = {
 'steps': [
  ['Form Fill en cero desde el 14-sep', 'Revisar el disparador del formulario en GTM y Tag Assistant; preguntarle al cliente si recibió formularios por email. Las llamadas siguen registrando: es medición.', 'PMM', True],
  ['Decidir la PMax creada el 01-oct', 'Recomendación: pausarla y volver Search a $25/día. Si se mantiene: negativas a nivel de cuenta, exclusión de marca, URL expansion apagada, exclusión de apps.', 'Jhombis', True],
  ['Verificar las 3 conversiones con Tag Assistant', 'Website Calls (¿desvío de Google o clic en tel:?), Form Fill y Calls from Ads (≥60 s). Lo que no sea un lead real pasa a secundaria.', 'PMM', True],
  ['Crear /thank-you/ y mover Form Fill ahí', 'Redirigir el formulario de Elementor a la página de gracias y disparar la conversión en su carga.', 'PMM', True],
  ['Ubicación en Presencia, radio 20 mi', 'Revisar en la interfaz (Windsor no lo muestra): hubo clics de NY, OH y AZ.', 'PMM', True],
  ['Aprobar y aplicar las negativas', f'{NEG_TOTAL} de nicho + universal con 4 excepciones + 3 nuevas en español, vía /negatives. "road ranger" volvió a gastar $6.15.', 'Jhombis', True],
  ['Apagar recomendaciones automáticas', 'La plantilla ENHPRM puede tenerlas activas.', 'PMM', True],
  ['Reestructura el 13-oct', '4 ad groups + Grúa ES condicional, broad → frase + exacta (incluida "gruero cerca de mi"), pausar 5 keywords, 1 RSA por grupo.', 'PMM', False],
  ['Preguntas al cliente', 'Formularios recibidos desde el 14-sep, ticket y cierre, español, atención nocturna, GBP, radio y servicios.', 'Cliente', False],
  ['✓ Hecho 06-oct: revisión semanal', 'log/2026-10-06: Form Fill a cero, PMax fuera del plan, 3 negativas nuevas; fases reprogramadas.', 'PMM', False],
  ['✓ Hecho 01-oct: estrategia, roadmap y checklist', 'Ajustados a las reglas de CLAUDE.md: 1 RSA por grupo y puja según medición.', 'PMM', False],
 ],
 'mname': {'2026-10-01': 'oct', '2026-11-01': 'nov', '2026-12-01': 'dic', '2027-01-01': 'ene 2027'},
 'rows': [
  {'k': 'F0', 'label': 'F0 Saneamiento', 'bars': [{'a': '2026-10-01', 'b': '2026-10-12', 't': 'B'}, {'a': '2026-10-12', 'b': '2026-10-15', 't': '', 'ghost': True}]},
  {'k': 'F1', 'label': 'F1 Relanzamiento', 'bars': [{'a': '2026-10-13', 'b': '2026-10-20', 't': '7 días'}]},
  {'k': 'F2', 'label': 'F2 Limpieza', 'bars': [{'a': '2026-10-20', 'b': '2026-11-12', 't': 'D7 · D14 · D30'}, {'a': '2026-11-12', 'b': '2026-12-08', 't': 'meta CPL ≤ $30', 'ghost': True}]},
  {'k': 'F3', 'label': 'F3 tCPA', 'bars': [{'a': '2026-12-08', 'b': '2027-01-20', 't': 'solo con $35/día', 'ghost': True}]},
  {'k': 'LAND', 'label': 'Landing', 'bars': [{'a': '2026-10-01', 'b': '2026-10-10', 't': 'B'}, {'a': '2026-10-10', 'b': '2026-10-31', 't': 'mejoras', 'ghost': True}]},
  {'k': 'LSA', 'label': 'LSA', 'bars': [{'a': '2026-10-20', 'b': '2026-11-03', 't': 'si hay GBP', 'ghost': True}]},
  {'k': 'F4', 'label': 'F4 Remarketing', 'bars': [], 'note': 'Sin fecha: audiencia < 1,000'},
  {'k': 'F5', 'label': 'F5 PMax', 'bars': [], 'note': 'No califica · creada el 01-oct: decidir'},
 ],
 'phases': [
  {'k': 'F0', 't': 'Saneamiento', 'w': '01-oct → 12-oct (reprogramada el 06-oct)', 's': ['block', 'Bloqueada'],
   'c': 'Los ítems B de Fase 0 en ✅: conversiones verificadas, /thank-you/, Presencia + 20 mi, negativas, recomendaciones apagadas.',
   'i': ['Nuevo: Form Fill en cero desde el 14-sep; PMax creada el 01-oct fuera del plan', 'Verificar Website Calls, Form Fill y Calls from Ads con Tag Assistant', 'Página de gracias y conversión del formulario', f'{NEG_TOTAL} negativas de nicho + universal, con OK de Jhombis', 'Cliente: ticket, español, horario nocturno, GBP']},
  {'k': 'F1', 't': 'Relanzamiento Search', 'w': '13-oct → 20-oct (reprogramada)', 's': ['todo', 'Pendiente'],
   'c': '7 días con la estructura nueva, anuncios aprobados y ≥1 conversión verificada.',
   'i': ['Misma campaña, $25/día, Max. conversiones', '4 ad groups + Grúa ES condicional; broad → frase + exacta', '1 RSA por grupo (máx. 2); pausar 5 keywords genéricas']},
  {'k': 'F2', 't': 'Limpieza D7 · D14 · D30', 'w': '20-oct · 27-oct · 12-nov (reprogramada)', 's': ['todo', 'Pendiente'],
   'c': '3 revisiones hechas, 4 semanas con CPL ≤ $40 y el cliente confirma ≥50% de leads reales.',
   'i': ['Search terms → negativas', 'Gasto > $80 sin conversión a revisión', 'Vigilar la hora 5 y los días con gasto < $20', 'Meta para salir hacia F3: CPL ≤ $30 (~08-dic)']},
  {'k': 'F3', 't': 'tCPA', 'w': '~20-ene-2027, solo con $35/día', 's': ['block', 'Bloqueada'],
   'c': '≥30 conversiones en 30 días con medición verificada.',
   'i': ['A $25/día el techo es ~20 conv./mes', 'Con $35/día y CPL $30 → ~35 conv./mes', 'tCPA = CPA real observado, no el deseado']},
  {'k': 'F4', 't': 'Remarketing', 'w': 'Sin fecha', 's': ['block', 'Bloqueada'],
   'c': 'Audiencia ≥1,000 usuarios en 30 días.', 'i': ['~94 clics/mes y dominio nuevo: no llega', 'Importar ya la audiencia de GA4 (sin costo)']},
  {'k': 'F5', 't': 'Performance Max', 'w': 'No califica', 's': ['block', 'Bloqueada'],
   'c': 'Todas las condiciones de pmax-cuando-y-como.md.', 'i': ['Falla: tCPA estable, 30+ conv./mes verificadas, fotos y video propios, anti-spam, presupuesto ≥ $115/día', 'Se creó una de $5/día el 01-oct (5 días: $22.51, 1 conv. Website Calls): decisión de Jhombis']},
  {'k': 'F6', 't': 'Conversiones offline', 'w': 'Fuera de alcance', 's': ['pause', 'Pausada'],
   'c': 'Registro de leads con GCLID (CRM u hoja).', 'i': ['Paso intermedio: hoja donde el cliente marca qué leads fueron servicio']},
 ],
 'ags': [
  ['Towing Near Me', 'F1', ['towing near me', 'tow truck near me', 'towing company near me', 'tow company near me', '24 hour towing near me', 'emergency towing near me'], '~390k', '/'],
  ['Cheap Towing', 'F1', ['cheap towing near me', 'cheap tow truck near me', 'cheapest towing near me', 'affordable towing near me'], '~24k', '/'],
  ['Roadside Assistance', 'F1', ['roadside assistance near me', 'jump start service near me', 'flat tire service near me', 'fuel delivery near me'], '~41k', '/roadside-assistance/'],
  ['Wesley Chapel Towing', 'F1', ['towing wesley chapel', 'tow truck wesley chapel', 'wesley chapel towing', 'pasco county towing'], '~130', '/'],
  ['Grúa ES', 'Condicional', ['grua cerca de mi', 'gruas cerca de mi', 'servicio de grua cerca de mi', 'servicio de grua'], '~12k', '/es/'],
 ],
 'h1': [[g] + p for g, p in [
  ('Towing Near Me', ['Towing Near You 24/7', 'Tow Truck Near You', 'Local Towing Company']),
  ('Cheap Towing', ['Affordable Towing Near You', 'Low-Cost Local Towing', 'Upfront Towing Prices']),
  ('Roadside Assistance', ['Roadside Assistance 24/7', 'Jump Starts & Tire Changes', 'Out of Gas? We Deliver']),
  ('Wesley Chapel Towing', ['Towing in Wesley Chapel', 'Wesley Chapel Tow Truck', 'Pasco County Towing']),
  ('Grúa ES', ['Grúa Cerca de Usted 24/7', 'Servicio de Grúa Local', 'Grúa en Wesley Chapel'])]],
 'negs': [['Competidores y terceros', NEGC['comp'], 'var(--orange)'], ['Servicios que no ofrece', NEGC['nosvc'], 'var(--purple)'],
          ['Compra / empleo / equipo', NEGC['compra'], 'var(--ink-2)'], ['Road Rangers / aseguradoras / clubes', NEGC['publico'], 'var(--red)'],
          ['Fuera de área', NEGC['area'], 'var(--muted)'], ['Impound / remolque de terceros', NEGC['impound'], 'var(--blue)']],
 'rub': [['Headline refleja el servicio', 1], ['Formulario corto arriba (móvil)', 1], ['Clic para llamar', 2], ['Oferta clara', 1], ['Prueba social', 0],
         ['Confianza (licencia, años)', 1], ['Velocidad móvil', None], ['Google Tag presente', 2], ['Página de gracias medible', 0], ['Páginas por servicio', 1], ['Sin fugas', 1]],
 'CL': [
  ['F0', 'Decisión sobre la PMax creada el 01-oct (recomendación: pausarla)', 'Jhombis', 'todo', True],
  ['F0', 'Presupuesto: Search $25 → $22 el 01-oct; con PMax $27/día (~$837/mes vs $760)', 'Jhombis', 'todo', False],
  ['F0', 'Cuenta 523-801-4243 visible en el MCC de PMM', 'PMM', 'done', False],
  ['F0', 'Facturación activa (gasta desde el 22-ago)', 'PMM', 'done', False],
  ['F0', 'Aplicación automática de recomendaciones desactivada', 'PMM', 'todo', True],
  ['F0', 'Ubicación = Presencia; radio 20 mi desde 3645 New River Rd; resto de países excluidos', 'PMM', 'todo', True],
  ['F0', 'Red: solo Búsqueda', 'PMM', 'done', False],
  ['F0', 'Google Tag en el sitio (AW-18347420212, GTM-5VX6B6KS, GT-5DDGBBK6)', 'PMM', 'done', False],
  ['F0', 'Form Fill sin conversiones desde el 14-sep: revisar disparador en GTM y preguntar al cliente', 'PMM', 'todo', True],
  ['F0', 'Form Fill probada con Tag Assistant (6 conv.; disparador sin verificar)', 'PMM', 'part', True],
  ['F0', 'Crear /thank-you/ y redirigir el formulario de Elementor ahí', 'PMM', 'todo', True],
  ['F0', 'Calls from Ads con duración mínima de 60 s (6 conv.; sin verificar)', 'PMM', 'part', True],
  ['F0', 'Website Calls → secundaria si es clic en tel: (9 conv., primaria)', 'PMM', 'part', True],
  ['F0', 'Conversiones secundarias marcadas como secundarias', 'PMM', 'todo', False],
  ['F0', 'GA4 vinculado y audiencia "Todos los visitantes" importada', 'PMM', 'todo', False],
  ['F0', 'Campos ocultos UTM + GCLID en el formulario', 'PMM', 'todo', False],
  ['F0', 'Lista universal PMM con excepciones (cheapest, insurance claim, "phone number" suelto, county) · OK de Jhombis', 'PMM', 'todo', True],
  ['F0', 'Lista de nicho + competidores + fuera de área (data/negatives-nicho.txt) · OK de Jhombis', 'PMM', 'todo', True],
  ['F0', 'Negativas a nivel de ad group para que los grupos no se crucen', 'PMM', 'todo', False],
  ['F0', 'Landing aprobada por /audit-landing (11/22, requiere ajustes)', 'PMM', 'part', False],
  ['F0', 'H1 "24/7 Towing in Wesley Chapel, FL"', 'PMM', 'todo', False],
  ['F0', 'tel:+18133810435 normalizado + botón de llamada fijo en móvil', 'PMM', 'todo', False],
  ['F0', 'Formulario de 3 campos (nombre, teléfono, ubicación del vehículo)', 'PMM', 'todo', False],
  ['F0', 'PageSpeed móvil medido', 'PMM', 'todo', False],
  ['F0', 'Ticket promedio, margen y tasa de cierre', 'Cliente', 'todo', False],
  ['F0', 'Proceso de respuesta a leads: quién contesta, en cuánto tiempo, a dónde llegan los formularios', 'Cliente', 'todo', False],
  ['F0', '¿Alguien contesta entre 0 y 6 h? (24/7 o 6:00–23:00)', 'Cliente', 'todo', False],
  ['F0', '¿Contestan en español? (activa o pausa Grúa ES)', 'Cliente', 'todo', False],
  ['F0', 'Google Business Profile: ¿existe, verificado, acceso para PMM?', 'Cliente', 'todo', False],
  ['F0', 'GBP vinculado a Google Ads (activo de ubicación)', 'PMM', 'todo', False],
  ['F0', 'Radio real de servicio (¿Tampa, Brandon, Plant City?)', 'Cliente', 'todo', False],
  ['F0', '¿Medium-duty, carrocería, lockout, remolque de RV?', 'Cliente', 'todo', False],
  ['F0', 'Licensed & insured, años en el negocio, fotos reales de las grúas', 'Cliente', 'todo', False],
  ['F0', 'Número de seguimiento / call tracking aprobado', 'Cliente', 'todo', False],
  ['F0', 'LSA: verificar si Towing está habilitada para 33543 (03-oct)', 'PMM', 'todo', False],
  ['F0', 'LSA: si aplica y hay GBP, iniciar solicitud (06-oct)', 'PMM', 'todo', False],
  ['F1', 'Campaña Search creada (plantilla ENHPRM; se reestructura, no se recrea)', 'PMM', 'done', False],
  ['F1', 'Renombrar campaña → Towing - Search - Radius', 'PMM', 'todo', False],
  ['F1', 'Pausar Towing Service (B), tow company, tow truck company y 2 keywords en español', 'PMM', 'todo', False],
  ['F1', 'Ad group 1 → Towing Near Me; broad → frase + exacta (pausar las broad al mismo tiempo)', 'PMM', 'todo', False],
  ['F1', 'Crear Cheap Towing, Roadside Assistance y Wesley Chapel Towing', 'PMM', 'todo', False],
  ['F1', 'Ad group 2 → Grúa ES; frase; activar o pausar según la regla', 'PMM', 'todo', False],
  ['F1', 'Programación según la respuesta del cliente (24/7 o 6:00–23:00)', 'PMM', 'todo', False],
  ['F1', 'Puja: Maximizar conversiones (sin tCPA)', 'PMM', 'done', False],
  ['F1', 'Si la medición limpia deja <15 conv./mes → Max. clics con tope de CPC de $10', 'PMM', 'todo', False],
  ['F1', '1 RSA por ad group (máx. 2), H1 pinneado, 15H/4D, fuerza Buena o superior', 'PMM', 'todo', False],
  ['F1', 'Extensiones: 4 sitelinks, 8 callouts, snippet, llamada, ubicación (si hay GBP)', 'PMM', 'todo', False],
  ['F1', 'URLs finales verificadas (200, https, sin redirect)', 'PMM', 'todo', False],
  ['F1', 'Presupuesto diario: era $25; desde el 01-oct Search $22 + PMax $5', 'PMM', 'part', False],
  ['F1', 'Anuncios actuales aprobados', 'PMM', 'done', False],
  ['F1', 'Anuncios nuevos aprobados (revisar 24 h después)', 'PMM', 'todo', False],
  ['F1', 'Primera conversión registrada (25-ago)', 'PMM', 'done', False],
  ['F1', '≥1 conversión verificada en la estructura nueva', 'PMM', 'todo', True],
  ['F2', 'Revisión inicial (día ~38): log 2026-09-29, negativas propuestas', 'PMM', 'done', False],
  ['F2', 'Revisión semanal 06-oct: log 2026-10-06, 3 negativas nuevas', 'PMM', 'done', False],
  ['F2', 'Pasar "gruero cerca de mi" (agregada en broad) y "servicio de grua" a frase', 'PMM', 'todo', False],
  ['F2', 'D7: search terms → negativas; keywords sin impresiones identificadas', 'PMM', 'todo', False],
  ['F2', 'D14: search terms → negativas; gasto > $80 sin conversión a revisión', 'PMM', 'todo', False],
  ['F2', 'D30: search terms; keywords con 0 impresiones en 30 días pausadas', 'PMM', 'todo', False],
  ['F2', 'D30: en Towing Near Me, pausar el peor de los 2 RSA solo si la diferencia es clara', 'PMM', 'todo', False],
  ['F2', 'D30: reporte de calidad de leads del cliente (≥50% reales)', 'Cliente', 'todo', False],
  ['F2', 'Vigilar la hora 5 (clics sin conversión) y el gasto diario menor a $20', 'PMM', 'todo', False],
  ['F3', 'Propuesta de upgrade a ~$35/día con datos de la Fase 2', 'Jhombis', 'todo', False],
  ['F3', '≥30 conversiones en 30 días confirmadas', 'PMM', 'todo', False],
  ['F3', 'tCPA = CPA real observado (no el deseado)', 'PMM', 'todo', False],
  ['F3', 'Presupuesto según CPA y capacidad del cliente', 'PMM', 'todo', False],
  ['F3', 'Ajustes de puja por horario con ≥60 conversiones', 'PMM', 'todo', False],
  ['F3', 'Ad groups Medium-Duty / Collision si el cliente los confirma', 'PMM', 'todo', False],
  ['F4', 'Audiencia GA4 "todos los visitantes" importada (desde ya)', 'PMM', 'todo', False],
  ['F4', 'Audiencia de visitantes ≥1,000 usuarios en 30 días', 'PMM', 'todo', False],
  ['F4', 'RLSA en observación en Search', 'PMM', 'todo', False],
  ['F6', 'Hoja compartida donde el cliente marca qué leads fueron servicio', 'Cliente', 'todo', False],
  ['F6', 'Lista de leads cerrados con GCLID', 'Cliente', 'todo', False],
  ['F6', 'Importación de conversiones offline configurada', 'PMM', 'todo', False],
 ],
 'PHT': {'F0': 'Fundación / saneamiento', 'F1': 'Relanzamiento Search', 'F2': 'Limpieza D7 · D14 · D30', 'F3': 'Optimización de puja (bloqueada)', 'F4': 'Remarketing', 'F6': 'Conversiones offline'},
 'qs': [
  ['<b>¿Le llegaron formularios del sitio por email después del 14-sep?</b> El sistema no registra ninguno desde esa fecha.', True],
  ['<b>¿Cuántos de los 18 contactos de septiembre fueron trabajos?</b> Sin esto el CPL de $38.50 no se traduce a rentabilidad.', False],
  ['<b>Ticket y margen:</b> cuánto cobra en promedio por un tow local y por medium-duty.', False],
  ['<b>¿Atienden en español?</b> Si no, se pausa el grupo en español (hoy: $308.09 y 3 conversiones).', True],
  ['<b>¿Alguien contesta entre medianoche y las 6 am?</b> Define 24/7 o 6:00–23:00.', False],
  ['<b>Google Business Profile:</b> ¿existe y está verificado? Acceso para PMM. Sin él no hay ubicación en los anuncios, Maps ni LSA.', True],
  ['<b>Radio real de servicio:</b> ¿incluye Tampa ciudad, Brandon, Plant City?', False],
  ['<b>Servicios:</b> ¿medium-duty (box trucks), carrocería, lockout, remolque de RV?', False],
  ['<b>Confianza:</b> ¿licensed &amp; insured? Años en el negocio y fotos reales de las grúas.', False],
 ],
 'msg': """Hi! Quick update on your Google Ads and a few questions so we can keep improving it.

In September the campaign brought in 18 contacts (calls and form fills) with $693 in ad spend, about $38 per contact, down from ~$108 in August. Next week we're cleaning up which searches trigger your ads and checking that every call is tracked correctly.

To fine-tune it we need:
1. Have you received any website form requests by email since September 14? Our system hasn't logged any since then.
2. How many of those 18 contacts turned into actual jobs?
3. What do you charge on average for a local tow? And for a box truck / medium-duty tow?
4. Can your team take calls in Spanish?
5. Does someone answer the phone between midnight and 6 am?
6. Do you have a Google Business Profile? If so, please give us manager access.
7. How far do you go? (Does it include Tampa, Brandon or Plant City?)
8. Besides towing and roadside, do you do body work, lockouts or RV towing?
9. Are you licensed and insured, and how many years have you been in business? Any real photos of your trucks are a big help.

Thanks!""",
}
ES = {'title': "Jerry's Towing · Plan Google Ads (ES)", 'body': BODY.replace('@@NEGTOTAL@@', str(NEG_TOTAL)).replace('@@UNI@@', str(len(UNI))).replace('@@KW@@', str(KW_ACTIVE)), 'data': DATA}
