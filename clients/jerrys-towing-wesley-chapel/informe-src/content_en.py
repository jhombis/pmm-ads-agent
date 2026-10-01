from build_common import NEGC, NEG_TOTAL, UNI, KW_ACTIVE
from content_es import DATA as DES

BODY = r'''<div class="wrap">
  <header class="mast">
    <div>
      <span class="logo"><img src="@@LOGO@@" alt="Performance Media Marketing"></span>
      <h1>Jerry's Auto Body Solutions &amp; Towing Service</h1>
      <p class="sub">Google Ads plan: diagnosis of the live account, restructure, dates and checklist to go from a $38.50 CPL with unverified tracking to ≤ $30 with confirmed leads.</p>
      <p style="margin-top:8px; font-size:.88rem"><a href="@@URL_OTHER@@">Versión en español →</a></p>
    </div>
    <dl class="meta">
      <dt>Account</dt><dd class="mono">523-801-4243</dd>
      <dt>MCC</dt><dd class="mono">444-523-7672</dd>
      <dt>Market</dt><dd>Wesley Chapel, FL (Pasco) · 20 mi radius · EN (+ ES conditional)</dd>
      <dt>D0</dt><dd class="num">Oct 1, 2026</dd>
      <dt>Current phase</dt><dd><span class="chip st-run">Phase 0 · in progress</span></dd>
      <dt>Updated</dt><dd class="num">Oct 1, 2026</dd>
    </dl>
  </header>

  <nav class="toc" aria-label="Sections">
    <a href="#resumen">Summary</a><a href="#evolucion">Performance</a><a href="#pasos">Next steps</a><a href="#fechas">Timeline</a><a href="#estrategia">Strategy</a><a href="#anuncios">Ads</a><a href="#negativas">Negatives</a><a href="#landing">Landing page</a><a href="#mercado">Benchmark &amp; competitors</a><a href="#checklist">Checklist</a><a href="#cliente">Client to-dos</a><a href="#porque">Why not yet</a>
  </nav>

  <section id="resumen">
    <div class="sec-head"><h2>Summary</h2><p>Local, family-owned 24/7 towing at 3645 New River Rd, Wesley Chapel, FL: light and medium-duty towing, accidents, recovery and roadside. Goal: calls ≥60 s and form fills.</p></div>
    <div class="kpis">
      <div class="kpi"><b>$760</b><span>ad spend/month · $25/day ($1,500 ENHPRM contract)</span></div>
      <div class="kpi"><b>$30–40</b><span>P1 target CPL · Fishhawk (Tampa) Search ~$31 · P2 goal ≤ $30</span></div>
      <div class="kpi"><b>~15–22</b><span>leads/month, base case (~94 clicks at $8.06)</span></div>
      <div class="kpi"><b>Oct 6</b><span>relaunch with the new structure</span></div>
    </div>

    <div class="two">
      <div>
        <p class="eyebrow">Account status today</p>
        <h3 style="margin:6px 0 10px">$1,017.83 spent, 130 clicks, 21 conversions (Aug 22 → Sep 28)</h3>
        <p>September closed with 18 conversions at a $38.50 CPL (August: $108.28). But all 3 conversion actions are primary and none is verified: if "Website Calls" (9 of 21) is a <span class="mono">tel:</span> click, the real CPL is above $60. The Spanish ad group spent $308.09 (30%) for 3 conversions. 13 of 21 keywords are broad. Of the visible search terms, <b>$87.08 of $629.42</b> went to competitors, public services, insurers, out-of-area searches or services Jerry's doesn't offer.</p>
        <div class="bar-spend" role="img" aria-label="Breakdown of $629.42 in visible search terms">
          <i style="width:85.4%; background:var(--green)"></i><i style="width:6.1%; background:var(--orange)"></i><i style="width:5.3%; background:var(--red)"></i><i style="width:2.4%; background:var(--purple)"></i><i style="width:0.8%; background:var(--sky)"></i>
        </div>
        <div class="legend">
          <span style="--c:var(--green)">Service intent $537.40 (16 conv.)</span>
          <span style="--c:var(--orange)">Competitors $38.26</span>
          <span style="--c:var(--red)">Road Rangers / insurers $33.25</span>
          <span style="--c:var(--purple)">Out of area / service not offered $15.57</span>
          <span style="--c:var(--sky)">Own brand $4.95</span>
        </div>
        <p class="muted" style="font-size:.85rem; margin-top:6px">Visible: $629.42 of $1,017.83 (62%); Google hides the rest for privacy. "Out of area" = Farmingdale NY ($5.85); "not offered" = RV transport ($9.72).</p>
      </div>
      <div class="callout">
        <h3>The decision in five lines</h3>
        <ul>
          <li><b>Campaigns</b> 1 Search: the current one is restructured, not replaced, to keep its 21 conversions and learning.</li>
          <li><b>Ad groups</b> 4 + conditional Grúa ES (fragmentation limit: $600–1,500/month → 1 campaign, 3–5 groups).</li>
          <li><b>Bidding and match</b> Max. Conversions if tracking checks out (if &lt;15 real conv./month remain, Max. Clicks with a $10 cap); phrase + exact; Presence, 20 mi radius; 24/7 if someone answers at night.</li>
          <li><b>The ceiling at this budget</b> ~15–22 conv./month; tCPA needs 30 → only at ~$35/day (decided after Phase 2, ~Dec 1).</li>
          <li><b>Not doing</b> PMax, Display, remarketing, brand. LSA only with a Business Profile and an eligible category.</li>
        </ul>
      </div>
    </div>
    <div style="margin-top:24px">
      <p class="eyebrow">Budget math (playbook §4)</p>
      <h3 style="margin:6px 0 10px">$25/day ÷ $8.06 CPC ≈ 3.1 clicks/day → ~94 clicks/month</h3>
      <div class="tbl"><table>
        <thead><tr><th>Scenario</th><th class="r">Conv. rate</th><th class="r">Leads/month</th><th class="r">CPL</th><th>Reference</th></tr></thead>
        <tbody>
          <tr><td>Conservative</td><td class="r">12%</td><td class="r">~11</td><td class="r">~$69</td><td>If "Website Calls" turn out to be clicks and are removed</td></tr>
          <tr><td><b>Base</b></td><td class="r"><b>16–24%</b></td><td class="r"><b>~15–22</b></td><td class="r"><b>~$35–51</b></td><td>September: 20.9% and $38.50 CPL</td></tr>
          <tr><td>Optimistic</td><td class="r">32%</td><td class="r">~30</td><td class="r">~$25</td><td>Fishhawk Towing (Tampa) Search, 90 days</td></tr>
        </tbody>
      </table></div>
      <p class="muted" style="font-size:.86rem; margin-top:8px">Max. Conversions needs 15+ clean conv./month (met only if tracking is confirmed). tCPA needs ~30 in 30 days: ~$1,050/month ($35/day) at a $35 CPL, or ~$900 at $30.</p>
    </div>
  </section>

  <section id="evolucion">
    <div class="sec-head"><h2>Performance · day 38 (September)</h2><p>Campaign "Jerry's … ENHPRM Radius", Sep 1 → Sep 28. Is the template working, and where does the money go?</p></div>
    <div class="kpis">
      <div class="kpi"><b>$693.01</b><span>spend in 28 days · 99% of $700</span></div>
      <div class="kpi"><b>86</b><span>clicks · 822 impr. · 10.5% CTR</span></div>
      <div class="kpi"><b>$8.06</b><span>avg. CPC · $9.05 over the last 7 days</span></div>
      <div class="kpi"><b>18</b><span>conversions · $38.50 CPL · since launch: 9 Website Calls, 6 Form Fill, 6 Calls from Ads</span></div>
    </div>
    <div class="two">
      <div style="min-width:0">
        <p class="eyebrow">The cause</p>
        <h3 style="margin:6px 0 10px">The ad attracts clicks (10.5% CTR, above the MCC P75); it loses 52% of impressions to rank, and Spanish spends without converting</h3>
        <div class="bar-spend" role="img" aria-label="Visible vs hidden"><i style="width:61.8%; background:var(--sky)"></i><i style="width:38.2%; background:var(--surface-2)"></i></div>
        <div class="legend"><span style="--c:var(--sky)">Visible in search terms $629.42</span><span style="--c:var(--surface-2)">Hidden for privacy $388.41</span></div>
        <div class="tbl" style="margin-top:14px"><table>
          <thead><tr><th>Day</th><th class="r">Impr.</th><th class="r">Clicks</th><th class="r">Cost</th><th class="r">CPC</th><th class="r">IS</th><th class="r">Lost (rank)</th><th class="r">Lost (budget)</th></tr></thead>
          <tbody>
            @@DAILY@@
          </tbody>
        </table></div>
        <div class="tbl" style="margin-top:14px"><table>
          <thead><tr><th>Ad group</th><th class="r">Impr.</th><th class="r">Clicks</th><th class="r">CTR</th><th class="r">Cost</th><th class="r">% spend</th></tr></thead>
          <tbody>
            <tr><td>Ad group 1 - English (18 conv., $39.43 CPL)</td><td class="r">1,018</td><td class="r">81</td><td class="r">8.0%</td><td class="r">$709.74</td><td class="r">70%</td></tr>
            <tr><td>Ad group 2 - Spanish (3 conv., $102.70 CPL)</td><td class="r">300</td><td class="r">49</td><td class="r">16.3%</td><td class="r">$308.09</td><td class="r">30%</td></tr>
          </tbody>
        </table></div>
        <p class="muted" style="font-size:.86rem; margin-top:8px">Ad groups: Aug 22 → Sep 28. Lost IS (rank and budget) is only available as a September aggregate. 93% of spend on mobile. Sep 24–28 spent $7–21/day on a $25 budget.</p>
      </div>
      <div class="callout">
        <h3>Diagnosis</h3>
        <ul>
          <li><b>Tracking:</b> Website Calls (9), Form Fill (6) and Calls from Ads (6), all three primary and unverified; the form has no thank-you page.</li>
          <li><b>Volume:</b> 86 clicks in the month: enough to see spend trends, not to compare ads or hours.</li>
          <li><b>Traffic:</b> 85% of visible spend is service intent; the waste is competitors, Road Rangers, insurers and searches from NY, OH and AZ (broad + possibly "Presence or interest").</li>
          <li><b>Bidding/CPC:</b> leave it until tracking is verified; an $8 CPC is the Tampa market rate.</li>
          <li><b>What to do:</b> 1) verify conversions and build /thank-you/; 2) negatives + Presence; 3) restructure on Oct 6 (phrase + exact, 4 groups, Spanish conditional).</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="pasos">
    <div class="sec-head"><h2>Next steps</h2><p>What's left to close Phase 0 and relaunch on Oct 6. Items marked B are blockers.</p></div>
    <div class="steps" id="steps"></div>
  </section>

  <section id="fechas">
    <div class="sec-head"><h2>Timeline and phases</h2><p>Dates are projections; the exit condition rules. We never move on "because it's the date".</p></div>
    <div class="tl-wrap"><div class="tl" id="timeline"></div></div>
    <div class="phases" id="phases"></div>
  </section>

  <section id="estrategia">
    <div class="sec-head"><h2>Strategy</h2><p>One campaign with 4 intent groups, because $25/day can't support more and "near me" is nearly all the demand (city names get ~0 searches).</p></div>
    <dl class="cfg">
      <div><dt>Campaign</dt><dd>Towing - Search - Radius (the current one, renamed)</dd></div>
      <div><dt>Type</dt><dd>Search · Search Network only (confirmed)</dd></div>
      <div><dt>Budget</dt><dd class="num">$25/day (~$760/month)</dd></div>
      <div><dt>Bidding</dt><dd>Max. Conversions → if clean tracking leaves &lt;15 conv./month, Max. Clicks with a $10 cap → tCPA at ≥30 conv./30 days</dd></div>
      <div><dt>Conversions</dt><dd>Calls from Ads ≥60 s + form on /thank-you/; Website Calls only if it's a Google forwarding number (if it's a tel: click, secondary)</dd></div>
      <div><dt>Match</dt><dd>Phrase + exact on top terms · no broad (13 keywords move)</dd></div>
      <div><dt>Location</dt><dd>Presence · 20 mi radius from 3645 New River Rd · other countries excluded</dd></div>
      <div><dt>Schedule</dt><dd>24/7 if someone answers at night; otherwise 6 am–11 pm (Eastern, same as the account)</dd></div>
      <div><dt>Off</dt><dd>Search partners, Display, auto-applied recommendations</dd></div>
    </dl>
    <div class="tbl"><table>
      <thead><tr><th>Ad group</th><th>Phase</th><th>Main keywords</th><th class="r">US vol./mo*</th><th>Landing page</th></tr></thead>
      <tbody id="agrows"></tbody>
    </table></div>
    <p class="muted" style="font-size:.88rem; margin-top:10px">* National Semrush volume (no city-level Keyword Planner); the share inside the radius is tiny. Zephyrhills, Dade City and Land O' Lakes get ~0 searches: covered by radius + "near me", no city groups. Grúa ES turns on only if they answer in Spanish and a Spanish page exists.</p>

    <h3 style="margin-top:28px; margin-bottom:10px">Budget by phase</h3>
    <div class="tbl"><table>
      <thead><tr><th>Phase</th><th>Total/month</th><th>What happens</th><th>Exit condition</th></tr></thead>
      <tbody>
        <tr><td><b>P0</b> Cleanup</td><td class="num">$760</td><td>Tracking, negatives, geo with the campaign live</td><td>Conversions verified, negatives, Presence</td></tr>
        <tr><td><b>P1</b> Stabilize</td><td class="num">$760</td><td>New structure, 1 RSA per group</td><td>4 weeks at CPL ≤ $40 and ≥50% real leads</td></tr>
        <tr><td><b>P2</b> Optimize</td><td class="num">$760</td><td>Pause the worst-CPL groups</td><td>CPL ≤ $30 for 4 weeks; IS lost to budget &gt; 20%</td></tr>
        <tr><td><b>P3</b> Scale</td><td class="num">$900–1,050</td><td>$30–35/day (needs a bigger package) + Medium-Duty / Collision if confirmed</td><td>~30 conv./30 days → tCPA at real CPL +10%</td></tr>
        <tr><td><b>P4</b> Remarketing</td><td class="num">+10%</td><td>Visitor audience in observation</td><td>List ≥1,000 users (at this traffic, &gt;6 months)</td></tr>
        <tr><td><b>P5</b> PMax</td><td class="num">—</td><td>Doesn't qualify</td><td>See "Why not yet"</td></tr>
      </tbody>
    </table></div>
  </section>

  <section id="anuncios">
    <div class="sec-head"><h2>Ads</h2><p>1 RSA per ad group (max. 2): at ~94 clicks/month an A/B test is noise (CLAUDE.md #4). H1 pinned to the group keyword; 3 variants were written (speed, price, trust) and the speed one goes live.</p></div>
    <div class="adgrid">
@@SERP@@
    </div>
    <div class="two" style="margin-top:22px">
      <div>
        <h3 style="margin-bottom:8px">Pinned H1 by ad group</h3>
        <div class="tbl"><table><tbody id="h1rows"></tbody></table></div>
      </div>
      <div>
        <h3 style="margin-bottom:8px">Shared headlines</h3>
        <ul class="pool" id="pool"></ul>
        <h3 style="margin:16px 0 8px">Descriptions (Towing Near Me; each group has its own 4)</h3>
        <ul style="margin:0; padding-left:1.1em; font-size:.93rem" id="descs"></ul>
      </div>
    </div>
    <div class="callout" style="margin-top:22px">
      <h3>Assets</h3>
      <ul>
        <li><b>Call</b> (813) 381-0435, Google forwarding number, 24/7 or the hours the client confirms</li>
        <li><b>Sitelinks</b>: Towing Near You, Roadside Assistance, Get a Free Quote, Accident Towing</li>
        <li><b>Callouts</b>: Available 24/7, Family-Owned, Free Quotes, Upfront Pricing, No Hidden Fees, Local to Wesley Chapel, Light &amp; Medium-Duty, You Choose Destination</li>
        <li><b>Snippet</b>: Services: Towing, Accident Towing, Vehicle Recovery, Jump Starts, Flat Tire Change, Fuel Delivery, Medium-Duty Towing</li>
        <li><b>Location / images</b>: location blocked until there's a Business Profile; images only with real photos of the trucks (no stock)</li>
        <li><b>Not promised</b>: licensed &amp; insured, arrival time, review count or years in business, until the client confirms them</li>
      </ul>
    </div>
  </section>

  <section id="negativas">
    <div class="sec-head"><h2>Negatives</h2><p>Proposed, not applied: waiting for Jhombis's OK (via /negatives). Nothing is written to the account without approval.</p></div>
    <div class="two" style="margin-top:0">
      <div>
        <h3 style="margin-bottom:12px">@@NEGTOTAL@@ niche + @@UNI@@ universal (awaiting OK)</h3>
        <div class="negbars" id="negbars"></div>
        <p class="muted" style="font-size:.86rem; margin-top:12px">Checked against the @@KW@@ keywords that stay live: 0 conflicts. Files:</p>
        <p class="muted" style="font-size:.86rem"><span class="mono">data/negatives-nicho.txt</span> · <span class="mono">data/2026-09-29-negatives.txt</span></p>
      </div>
      <div class="callout">
        <h3>Conflicts avoided</h3>
        <p style="margin-top:8px"><span class="kw">county</span> <span class="kw">cheapest</span> <span class="kw">insurance claim</span> <span class="kw">phone number</span></p>
        <p style="font-size:.9rem; color:var(--ink-2); margin-top:8px">Universal negatives NOT applied in this account: "county" would block "pasco county towing" (Wesley Chapel group); "cheapest" would block "cheapest towing near me", which converted; "insurance claim" can be an accident tow; a bare "phone number" would block "towing service phone number". "jerry"/"jerrys" is not negated either (own brand).</p>
      </div>
    </div>
  </section>

  <section id="landing">
    <div class="sec-head"><h2>Landing page</h2><p>11/22 · needs fixes before the relaunch. The thank-you page is the blocker; social proof at 0 is an improvement, not a blocker (/audit-landing rubric).</p></div>
    <div class="two" style="margin-top:0">
      <div>
        <div class="rub" id="rubric"></div>
        <p class="muted" style="font-size:.86rem; margin-top:8px">jerrystowingservice.com: a single page (WordPress + Elementor, Aug 2026), no H1, 6-field form at the bottom, 16 tel: links and a sticky header. Speed not measured (no PageSpeed key).</p>
      </div>
      <div>
        <h3 style="margin-bottom:8px">Landing pages needed</h3>
        <div class="tbl"><table>
          <thead><tr><th>URL</th><th>Status</th><th>For</th></tr></thead>
          <tbody>
            <tr><td class="mono">/thank-you/</td><td><span class="chip st-block">Build · B</span></td><td>Form tracking (P0)</td></tr>
            <tr><td class="mono">/</td><td><span class="chip st-todo">Improve</span></td><td>H1, 3-field form, reviews · Towing Near Me, Cheap, Wesley Chapel</td></tr>
            <tr><td class="mono">/roadside-assistance/</td><td><span class="chip st-todo">Build</span></td><td>Roadside Assistance (/#roadside meanwhile)</td></tr>
            <tr><td class="mono">/es/</td><td><span class="chip st-block">Build if they answer in ES</span></td><td>Grúa ES</td></tr>
            <tr><td class="mono">/medium-duty-towing/</td><td><span class="chip st-pause">Conditional</span></td><td>P3, if confirmed</td></tr>
            <tr><td class="mono">/collision-repair/</td><td><span class="chip st-pause">Conditional</span></td><td>P3, if they do body work</td></tr>
          </tbody>
        </table></div>
      </div>
    </div>
  </section>

  <section id="mercado">
    <div class="sec-head"><h2>Benchmark and competitors</h2><p>28 US towing accounts in the MCC, 90 days (Windsor). Tampa is an expensive market: Jerry's pays $8 a click vs. the $4.87 median, and its CPL is in line with the local comparable.</p></div>
    <div class="tbl"><table>
      <thead><tr><th>Account</th><th>Market</th><th>Bidding</th><th class="r">CPC</th><th class="r">Conv. rate</th><th class="r">CPL</th><th class="r">Conv./mo</th></tr></thead>
      <tbody>
        <tr><td>A (anonymized)</td><td>Tampa, FL · ENHPRM package</td><td>Max. conv. + PMax</td><td class="r">$5.94</td><td class="r">17.8%</td><td class="r"><b>$33.29</b></td><td class="r">24</td></tr>
        <tr><td>B (anonymized)</td><td>US · $2,500 package</td><td>Max. conv. + PMax</td><td class="r">$3.72</td><td class="r">38.6%</td><td class="r"><b>$9.64</b></td><td class="r">151</td></tr>
        <tr><td>C (anonymized)</td><td>US · $1,399 package</td><td>Max. conv.</td><td class="r">$4.51</td><td class="r">37.2%</td><td class="r"><b>$12.13</b></td><td class="r">56</td></tr>
        <tr><td>D (anonymized)</td><td>US · $1,600 package</td><td>Max. conv. + PMax</td><td class="r">$4.46</td><td class="r">24.9%</td><td class="r"><b>$17.88</b></td><td class="r">38</td></tr>
        <tr><td>E (anonymized)</td><td>US · $1,500 package</td><td>Max. conv.</td><td class="r">$6.80</td><td class="r">16.4%</td><td class="r"><b>$41.39</b></td><td class="r">19</td></tr>
        <tr><td>F (anonymized)</td><td>US · $1,500 package</td><td>Max. conv.</td><td class="r">$11.22</td><td class="r">25.8%</td><td class="r"><b>$43.56</b></td><td class="r">17</td></tr>
        <tr><td>MCC median (20 mature accounts)</td><td>US</td><td>—</td><td class="r">$4.87</td><td class="r">28.1%</td><td class="r"><b>$14.59</b></td><td class="r">42</td></tr>
        <tr><td><b>JERRY'S (Sep)</b></td><td>Wesley Chapel, FL</td><td>Max. conv.</td><td class="r"><b>$8.06</b></td><td class="r">20.9%</td><td class="r"><b>$38.50</b></td><td class="r">18</td></tr>
      </tbody>
    </table></div>
    <p class="muted" style="font-size:.86rem; margin-top:8px">38–50% conversion rates in the MCC likely count phone clicks as conversions: MCC CPLs are understated. In A, "near me" Search keywords cost ~$10 a click; PMax pulls the average down.</p>

    <div class="two">
      <div>
        <h3 style="margin-bottom:8px">Competitors in Wesley Chapel / Pasco</h3>
        <div class="tbl"><table>
          <thead><tr><th>Competitor</th><th>Type</th><th>Angle</th></tr></thead>
          <tbody>
            <tr><td>B&amp;D Towing &amp; Recovery</td><td>Local, Tampa</td><td>"Fast and affordable 24/7"; city pages</td></tr>
            <tr><td>Pasco Towing Inc</td><td>Local, Pasco</td><td>"Fast and affordable 24/7"; city pages</td></tr>
            <tr><td>towingwesleychapel.com</td><td>Exact-match domain</td><td>Likely lead-gen</td></tr>
            <tr><td>dependabletowwesleychapel.com</td><td>Exact-match domain</td><td>Likely lead-gen, 24/7</td></tr>
            <tr><td>DRIVE Roadside · True Towing · 24hr-towing</td><td>National aggregators</td><td>24/7, national network; bid hard on "near me"</td></tr>
          </tbody>
        </table></div>
        <p class="muted" style="font-size:.86rem; margin-top:8px">Semrush has no local ads for these domains; reviews not collected.</p>
      </div>
      <div class="callout">
        <h3>Opportunities</h3>
        <ul>
          <li><b>Spanish</b> in A, "servicio de grua" and "grua cerca de mi" convert at $19–25, with a Spanish page.</li>
          <li><b>Medium-duty</b> box trucks and fleets: high ticket, few aggregators.</li>
          <li><b>Local and family-owned</b> vs. national networks that subcontract, if backed by reviews.</li>
        </ul>
        <h3 style="margin-top:14px">Threats</h3>
        <ul>
          <li>Aggregators on "near me": real CPC ~$10, 2.5–3× what Semrush shows.</li>
          <li>No Business Profile or reviews: no map pack, no location asset and no LSA.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="checklist">
    <div class="sec-head"><h2>Checklist</h2><p>Mirror of <span class="mono">clients/jerrys-towing-wesley-chapel/checklist.md</span> as of Oct 1. /weekly-review keeps it current.</p></div>
    <div class="filters" role="group" aria-label="Filters">
      <div class="grp"><span class="lab">Owner</span><span id="f-who"></span></div>
      <div class="grp"><span class="lab">Status</span><span id="f-st"></span></div>
    </div>
    <div id="cl"></div>
  </section>

  <section id="cliente">
    <div class="sec-head"><h2>Client to-dos</h2><p>What we need from Jerry's. Items marked B block part of the plan.</p></div>
    <div class="two" style="margin-top:0">
      <ol class="qlist" id="qlist"></ol>
      <div class="callout">
        <h3>Ready-to-send message</h3>
        <p style="font-size:.9rem; color:var(--ink-2)">To send the client by email or text.</p>
        <textarea class="copyarea" id="clientmsg" readonly aria-label="Message for the client"></textarea>
        <div style="display:flex; gap:10px; align-items:center; margin-top:8px"><button class="copybtn" id="copybtn" type="button">Copy message</button><span id="copystate" class="muted" style="font-size:.85rem" aria-live="polite"></span></div>
      </div>
    </div>
  </section>

  <section id="porque">
    <div class="sec-head"><h2>Why not (yet)</h2></div>
    <div class="why">
      <div><h4>Performance Max</h4><p>Fails 5 of 6 conditions: no stable tCPA, ~18 unverified conv./month, no own photos or video, no spam protection, and $25/day vs. the ~$115 it needs.</p></div>
      <div><h4>Broad</h4><p>Its cost already shows: searches from NY, OH and AZ, Road Rangers, insurers and competitors. "tow truck near me" in phrase: $13.77 CPL; in broad: $41.74.</p></div>
      <div><h4>Display / Demand Gen</h4><p>An emergency service: nobody hires a tow truck from a banner.</p></div>
      <div><h4>Brand campaign</h4><p>"jerrys towing": 1–3 impressions in 38 days. There's no brand demand.</p></div>
      <div><h4>Remarketing</h4><p>~94 clicks/month and a new domain: the audience won't reach 1,000 in 30 days. Towing needs are immediate.</p></div>
      <div><h4>City ad groups</h4><p>Zephyrhills, Dade City and Land O' Lakes get ~0 searches; "towing wesley chapel" ~30/month. Radius + "near me" covers the demand.</p></div>
    </div>
    <div class="callout" style="margin-top:22px">
      <h3>Risks and assumptions</h3>
      <ul>
        <li><b>Economics:</b> with an assumed $125 tow and 50% margin, the "comfortable" CPL is ~$11 and break-even ~$37. A $30–40 CPL may not be profitable.</li>
        <li><b>Tracking:</b> if "Website Calls" is a click, the real CPL is above $60 and Max. Conversions is learning from the wrong signal.</li>
        <li><b>Variance:</b> ~3 clicks/day: a week with no conversions is normal; don't react before D14.</li>
        <li><b>Hurricanes (through Nov 30) and snowbirds (Nov–Apr):</b> demand spikes; have a temporary budget bump ready with the client's OK.</li>
        <li><b>Assumptions:</b> 20 mi radius, 24/7 answering and the services on the site, not yet confirmed by the client.</li>
      </ul>
    </div>
  </section>

  <footer>
    <span>Performance Media Marketing · Jerry's Auto Body Solutions &amp; Towing Service · account 523-801-4243</span>
    <span>Sources: brief, audit-site, benchmark, competitors, strategy, roadmap, checklist and log 2026-09-29 · Windsor Aug 22 → Sep 28, 2026 · Semrush US</span>
  </footer>
</div>'''

CL_EN = [
 'Account 523-801-4243 visible in the PMM MCC', 'Billing active (spending since Aug 22)', 'Auto-applied recommendations turned off',
 'Location = Presence; 20 mi radius from 3645 New River Rd; other countries excluded', 'Network: Search only',
 'Google Tag on the site (AW-18347420212, GTM-5VX6B6KS, GT-5DDGBBK6)', 'Form Fill tested with Tag Assistant (6 conv.; trigger not verified)',
 'Build /thank-you/ and redirect the Elementor form there', 'Calls from Ads with a 60 s minimum (6 conv.; not verified)',
 'Website Calls → secondary if it is a tel: click (9 conv., primary)', 'Secondary conversions set as secondary',
 'GA4 linked and "All visitors" audience imported', 'Hidden UTM + GCLID fields on the form',
 'PMM universal list with exceptions (cheapest, insurance claim, bare "phone number", county) · Jhombis OK',
 'Niche + competitors + out-of-area list (data/negatives-nicho.txt) · Jhombis OK', 'Ad-group negatives so groups don’t overlap',
 'Landing page approved by /audit-landing (11/22, needs fixes)', 'H1 "24/7 Towing in Wesley Chapel, FL"',
 'tel:+18133810435 normalized + sticky call button on mobile', '3-field form (name, phone, vehicle location)', 'Mobile PageSpeed measured',
 'Average ticket, margin and close rate', 'Lead answering process: who answers, how fast, where forms go',
 'Does someone answer between midnight and 6 am? (24/7 or 6 am–11 pm)', 'Do they answer in Spanish? (turns Grúa ES on or off)',
 'Google Business Profile: exists, verified, PMM access?', 'Business Profile linked to Google Ads (location asset)',
 'Real service radius (Tampa, Brandon, Plant City?)', 'Medium-duty, body work, lockouts, RV towing?',
 'Licensed & insured, years in business, real photos of the trucks', 'Tracking number / call tracking approved',
 'LSA: check whether Towing is eligible for 33543 (Oct 3)', 'LSA: if eligible and there’s a Business Profile, apply (Oct 6)',
 'Search campaign created (ENHPRM template; restructured, not rebuilt)', 'Rename campaign → Towing - Search - Radius',
 'Pause Towing Service (B), tow company, tow truck company and 2 Spanish keywords',
 'Ad group 1 → Towing Near Me; broad → phrase + exact (pause the broad ones at the same time)',
 'Build Cheap Towing, Roadside Assistance and Wesley Chapel Towing', 'Ad group 2 → Grúa ES; phrase; turn on or pause per the rule',
 'Ad schedule per the client’s answer (24/7 or 6 am–11 pm)', 'Bidding: Maximize Conversions (no tCPA)',
 'If clean tracking leaves <15 conv./month → Max. Clicks with a $10 CPC cap', '1 RSA per ad group (max. 2), pinned H1, 15H/4D, Good strength or better',
 'Assets: 4 sitelinks, 8 callouts, snippet, call, location (if Business Profile)', 'Final URLs verified (200, https, no redirect)',
 'Daily budget $25', 'Current ads approved', 'New ads approved (check 24 h later)', 'First conversion recorded (Aug 25)',
 '≥1 verified conversion in the new structure',
 'Initial review (day ~38): log 2026-09-29, negatives proposed', 'D7: search terms → negatives; keywords with no impressions flagged',
 'D14: search terms → negatives; >$80 spend with no conversion goes to review', 'D30: search terms; keywords with 0 impressions in 30 days paused',
 'D30: in Towing Near Me, pause the weaker of the 2 RSAs only if the gap is clear', 'D30: client lead-quality report (≥50% real)',
 'Watch hour 5 (clicks with no conversion) and daily spend under $20',
 'Upgrade proposal to ~$35/day with Phase 2 data', '≥30 conversions in 30 days confirmed', 'tCPA = observed real CPA (not the desired one)',
 'Budget per CPA and client capacity', 'Ad schedule bid adjustments with ≥60 conversions', 'Medium-Duty / Collision ad groups if the client confirms them',
 'GA4 "all visitors" audience imported (now)', 'Visitor audience ≥1,000 users in 30 days', 'RLSA in observation on Search',
 'Shared sheet where the client marks which leads became jobs', 'List of closed leads with GCLID', 'Offline conversion import set up',
]
assert len(CL_EN) == len(DES['CL']), (len(CL_EN), len(DES['CL']))
WHO = {'PMM': 'PMM', 'Cliente': 'Client', 'Jhombis': 'Jhombis'}

DATA = {
 'steps': [
  ['Verify the 3 conversions with Tag Assistant', 'Website Calls (Google forwarding number or tel: click?), Form Fill (what fires it?) and Calls from Ads (≥60 s). Anything that isn’t a real lead becomes secondary.', 'PMM', True],
  ['Build /thank-you/ and move Form Fill there', 'Redirect the Elementor form to the thank-you page and fire the conversion on its load.', 'PMM', True],
  ['Location on Presence, 20 mi radius', 'Check in the UI (Windsor doesn’t show it): there were clicks from NY, OH and AZ.', 'PMM', True],
  ['Approve and apply the negatives', f'{NEG_TOTAL} niche + universal with 4 exceptions, via /negatives. Needs Jhombis’s OK.', 'Jhombis', True],
  ['Turn off auto-applied recommendations', 'The ENHPRM template may have them on.', 'PMM', True],
  ['Restructure on Oct 6', '4 ad groups + conditional Grúa ES, broad → phrase + exact, pause 5 keywords, 1 RSA per group.', 'PMM', False],
  ['Landing page: H1, normalized tel:, 3-field form', 'Quality Score improvements; social proof depends on the client’s reviews.', 'PMM', False],
  ['Questions for the client', 'Ticket and close rate, Spanish, night answering, Business Profile, radius and services.', 'Client', False],
  ['✓ Done Sep 29: first account review', 'log/2026-09-29: metrics, search terms and proposed negatives.', 'PMM', False],
  ['✓ Done Oct 1: strategy, roadmap and checklist', 'Aligned with the CLAUDE.md rules: 1 RSA per group and bidding tied to tracking.', 'PMM', False],
 ],
 'mname': {'2026-10-01': 'Oct', '2026-11-01': 'Nov', '2026-12-01': 'Dec', '2027-01-01': 'Jan 2027'},
 'rows': [
  {'k': 'F0', 'label': 'P0 Cleanup', 'bars': [{'a': '2026-10-01', 'b': '2026-10-06', 't': ''}, {'a': '2026-10-06', 'b': '2026-10-15', 't': 'client', 'ghost': True}]},
  {'k': 'F1', 'label': 'P1 Relaunch', 'bars': [{'a': '2026-10-06', 'b': '2026-10-13', 't': '7 days'}]},
  {'k': 'F2', 'label': 'P2 Cleanup reviews', 'bars': [{'a': '2026-10-13', 'b': '2026-11-05', 't': 'D7 · D14 · D30'}, {'a': '2026-11-05', 'b': '2026-12-01', 't': 'goal CPL ≤ $30', 'ghost': True}]},
  {'k': 'F3', 'label': 'P3 tCPA', 'bars': [{'a': '2026-12-01', 'b': '2027-01-15', 't': 'only at $35/day', 'ghost': True}]},
  {'k': 'LAND', 'label': 'Landing page', 'bars': [{'a': '2026-10-01', 'b': '2026-10-10', 't': 'B'}, {'a': '2026-10-10', 'b': '2026-10-31', 't': 'improvements', 'ghost': True}]},
  {'k': 'LSA', 'label': 'LSA', 'bars': [{'a': '2026-10-20', 'b': '2026-11-03', 't': 'if Business Profile', 'ghost': True}]},
  {'k': 'F4', 'label': 'P4 Remarketing', 'bars': [], 'note': 'No date: audience < 1,000'},
  {'k': 'F5', 'label': 'P5 PMax', 'bars': [], 'note': 'Doesn’t qualify'},
 ],
 'phases': [
  {'k': 'F0', 't': 'Cleanup', 'w': 'Oct 1 → Oct 6 (client by Oct 15)', 's': ['run', 'In progress'],
   'c': 'Phase 0 B items ✅: conversions verified, /thank-you/, Presence + 20 mi, negatives, recommendations off.',
   'i': ['Verify Website Calls, Form Fill and Calls from Ads with Tag Assistant', 'Thank-you page and form conversion', f'{NEG_TOTAL} niche + universal negatives, with Jhombis’s OK', 'Client: ticket, Spanish, night hours, Business Profile']},
  {'k': 'F1', 't': 'Search relaunch', 'w': 'Oct 6 → Oct 13', 's': ['todo', 'Pending'],
   'c': '7 days on the new structure, ads approved and ≥1 verified conversion.',
   'i': ['Same campaign, $25/day, Max. Conversions', '4 ad groups + conditional Grúa ES; broad → phrase + exact', '1 RSA per group (max. 2); pause 5 generic keywords']},
  {'k': 'F2', 't': 'Cleanup D7 · D14 · D30', 'w': 'Oct 13 · Oct 20 · Nov 5', 's': ['todo', 'Pending'],
   'c': '3 reviews done, 4 weeks at CPL ≤ $40 and the client confirms ≥50% real leads.',
   'i': ['Search terms → negatives', '>$80 spend with no conversion goes to review', 'Watch hour 5 and days spending < $20', 'Goal to move to P3: CPL ≤ $30 (~Dec 1)']},
  {'k': 'F3', 't': 'tCPA', 'w': '~Jan 15, 2027, only at $35/day', 's': ['block', 'Blocked'],
   'c': '≥30 conversions in 30 days with verified tracking.',
   'i': ['At $25/day the ceiling is ~20 conv./month', 'At $35/day and a $30 CPL → ~35 conv./month', 'tCPA = observed real CPA, not the desired one']},
  {'k': 'F4', 't': 'Remarketing', 'w': 'No date', 's': ['block', 'Blocked'],
   'c': 'Audience ≥1,000 users in 30 days.', 'i': ['~94 clicks/month and a new domain: won’t get there', 'Import the GA4 audience now (no cost)']},
  {'k': 'F5', 't': 'Performance Max', 'w': 'Doesn’t qualify', 's': ['block', 'Blocked'],
   'c': 'Every condition in pmax-cuando-y-como.md.', 'i': ['Fails on: stable tCPA, 30+ verified conv./month, own photos and video, spam protection, budget ≥ $115/day']},
  {'k': 'F6', 't': 'Offline conversions', 'w': 'Out of scope', 's': ['pause', 'Paused'],
   'c': 'Lead log with GCLID (CRM or sheet).', 'i': ['Interim step: a sheet where the client marks which leads became jobs']},
 ],
 'ags': [a if a[0] != 'Grúa ES' else ['Grúa ES', 'Conditional'] + a[2:] for a in DES['ags']],
 'h1': DES['h1'],
 'negs': [['Competitors and third parties', NEGC['comp'], 'var(--orange)'], ['Services not offered', NEGC['nosvc'], 'var(--purple)'],
          ['Buying / jobs / equipment', NEGC['compra'], 'var(--ink-2)'], ['Road Rangers / insurers / clubs', NEGC['publico'], 'var(--red)'],
          ['Out of area', NEGC['area'], 'var(--muted)'], ['Impound / third-party towing', NEGC['impound'], 'var(--blue)']],
 'rub': [['Headline matches the service', 1], ['Short form above the fold (mobile)', 1], ['Click to call', 2], ['Clear offer', 1], ['Social proof', 0],
         ['Trust (license, years)', 1], ['Mobile speed', None], ['Google Tag present', 2], ['Measurable thank-you page', 0], ['Service pages', 1], ['No leaks', 1]],
 'CL': [[c[0], t, WHO[c[2]], c[3], c[4]] for c, t in zip(DES['CL'], CL_EN)],
 'PHT': {'F0': 'Foundation / cleanup', 'F1': 'Search relaunch', 'F2': 'Cleanup D7 · D14 · D30', 'F3': 'Bid optimization (blocked)', 'F4': 'Remarketing', 'F6': 'Offline conversions'},
 'qs': [
  ['<b>How many of September’s 18 contacts became jobs?</b> Without it the $38.50 CPL can’t be turned into profit.', False],
  ['<b>Ticket and margin:</b> average charge for a local tow and for medium-duty.', False],
  ['<b>Do they answer in Spanish?</b> If not, the Spanish group is paused (so far: $308.09 and 3 conversions).', True],
  ['<b>Does someone answer between midnight and 6 am?</b> Decides 24/7 vs. 6 am–11 pm.', False],
  ['<b>Google Business Profile:</b> does it exist and is it verified? Access for PMM. Without it there’s no location in ads, Maps or LSA.', True],
  ['<b>Real service radius:</b> does it include Tampa city, Brandon, Plant City?', False],
  ['<b>Services:</b> medium-duty (box trucks), body work, lockouts, RV towing?', False],
  ['<b>Trust:</b> licensed &amp; insured? Years in business and real photos of the trucks.', False],
 ],
 'msg': DES['msg'],
}
RENDERER = [
 ("n:'Fase 0'}", "n:'Phase 0'}"), ("n:'Fase 1'}", "n:'Phase 1'}"), ("n:'Fase 2'}", "n:'Phase 2'}"), ("n:'Fase 3'}", "n:'Phase 3'}"),
 ("n:'Fase 4'}", "n:'Phase 4'}"), ("n:'Fase 5'}", "n:'Phase 5'}"), ("n:'Fase 6'}", "n:'Phase 6'}"),
 ('title="Bloqueante"', 'title="Blocker"'), ('<b>hoy</b>', '<b>today</b>'), ('<b>Condición de paso</b>', '<b>Exit condition</b>'),
 ("a[1]+' activo':a[1]+' en pausa'", "a[1]+' active':a[1]+' paused'"), ('<em>SIN DATO</em>', '<em>NO DATA</em>'),
 ("let fWho='Todos', fSt='Todos';", "let fWho='All', fSt='All';"),
 ("const whoOpts=['Todos','PMM','Cliente','Jhombis'], stOpts=['Todos','Pendientes','Bloqueantes','Hechos'];", "const whoOpts=['All','PMM','Client','Jhombis'], stOpts=['All','Pending','Blockers','Done'];"),
 ("(fWho==='Todos'||", "(fWho==='All'||"),
 ("(fSt==='Todos' || (fSt==='Hechos'&&x[3]==='done') || (fSt==='Pendientes'&&x[3]!=='done') || (fSt==='Bloqueantes'&&x[4]&&x[3]!=='done'))", "(fSt==='All' || (fSt==='Done'&&x[3]==='done') || (fSt==='Pending'&&x[3]!=='done') || (fSt==='Blockers'&&x[4]&&x[3]!=='done'))"),
 ('hechos</small>', 'done</small>'), ("'hecho':x[3]==='part'?'parcial':'pendiente'", "'done':x[3]==='part'?'partial':'pending'"),
 ('Nada con estos filtros.', 'Nothing matches these filters.'),
 ("'Texto seleccionado: usa Ctrl/Cmd + C.'", "'Text selected: press Ctrl/Cmd + C.'"), ("'Copiado.'", "'Copied.'"),
]
EN = {'title': "Jerry's Towing · Google Ads Plan (EN)", 'body': BODY.replace('@@NEGTOTAL@@', str(NEG_TOTAL)).replace('@@UNI@@', str(len(UNI))).replace('@@KW@@', str(KW_ACTIVE)), 'data': DATA, 'renderer': RENDERER}
