#!/usr/bin/env python3
"""Índice de informes PMM para el equipo (estilo de knowledge/estilo-informes/).

  python scripts/indice_informes.py            → escribe clients/indice-informes.html

Cruza clients/informes.json (URLs de los artefactos publicados) con el front matter de cada cliente
(brief.md, checklist.md, roadmap.md): nicho, idioma, fase actual, estado y fecha de actualización.
Lo corre /informe después de publicar un plan; el resultado se republica siempre en la misma URL
(`indice_url` de informes.json).
"""
import json, re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLIENTS = ROOT / 'clients'
REG = CLIENTS / 'informes.json'
OUT = CLIENTS / 'indice-informes.html'
TEMPLATE = ROOT / 'knowledge/estilo-informes/plantilla.html'

EXTRA_CSS = """
.ix-tools{display:flex; flex-wrap:wrap; gap:12px 20px; align-items:center; margin:8px 0 14px}
.ix-search{flex:1 1 240px; min-width:0; font:inherit; padding:9px 12px; border:1px solid var(--line); border-radius:8px; background:var(--ground); color:var(--ink)}
.ix-search:focus-visible{outline:2px solid var(--blue); outline-offset:1px}
.ix-name b{display:block}
.ix-name .mono{font-size:.8rem; color:var(--muted)}
.ix-links{display:flex; flex-wrap:wrap; gap:6px}
.ix-link{display:inline-flex; align-items:center; gap:6px; padding:5px 10px; border:1px solid var(--line); border-radius:999px; text-decoration:none; color:var(--blue); font-weight:600; font-size:.86rem; white-space:nowrap}
.ix-link:hover{border-color:var(--blue)}
.ix-link:focus-visible{outline:2px solid var(--blue); outline-offset:1px}
.ix-link .lg{font-family:'JetBrains Mono',ui-monospace,monospace; font-size:.72rem; color:var(--muted)}
.ix-link.old{color:var(--muted); font-weight:400}
.ix-phase{display:inline-flex; align-items:center; gap:7px; white-space:nowrap}
.ix-phase i{width:10px; height:10px; border-radius:50%; background:var(--c)}
.ix-none{color:var(--muted); font-style:italic; font-size:.88rem}
.ix-lang{margin-left:auto}
td.ix-state{max-width:260px; font-size:.86rem; color:var(--ink-2)}
"""

PHASE_COLORS = ['var(--red)', 'var(--orange)', 'var(--yellow)', 'var(--green)', 'var(--sky)', 'var(--purple)', 'var(--muted)']


def front(path):
    if not path.exists():
        return {}
    m = re.match(r'---\n(.*?)\n---', path.read_text(), re.S)
    out = {}
    for line in (m.group(1).splitlines() if m else []):
        if ':' in line:
            k, v = line.split(':', 1)
            out[k.strip().lower()] = v.strip()
    return out


def client_rows(reg):
    rows = []
    for slug, info in reg['clientes'].items():
        b, c, r = (front(CLIENTS / slug / f) for f in ('brief.md', 'checklist.md', 'roadmap.md'))
        fase = r.get('fase_actual') or c.get('fase_actual') or ''
        fechas = [x for x in (b.get('actualizado'), c.get('actualizado'), r.get('actualizado')) if x]
        rows.append({
            'slug': slug,
            'cliente': b.get('cliente') or slug,
            'nicho': (b.get('nicho') or '').split('(')[0].strip(),
            'mercado': info.get('mercado', ''),
            'cuenta': info.get('cuenta', ''),
            'fase': fase,
            'estado': b.get('estado', ''),
            'actualizado': max(fechas) if fechas else '',
            'informes': info.get('informes', []),
        })
    rows.sort(key=lambda x: x['actualizado'], reverse=True)
    return rows


def build():
    reg = json.loads(REG.read_text())
    tpl = TEMPLATE.read_text()
    head = tpl[:tpl.index('</style>')] + EXTRA_CSS + '</style>\n'
    head = re.sub(r'<title>.*?</title>', '<title>Informes PMM</title>', head)
    from informe_html import logo_uri
    rows = client_rows(reg)
    data = json.dumps({'clientes': rows, 'otros': reg.get('otros', []), 'colors': PHASE_COLORS},
                      ensure_ascii=False).replace('</', '<\\/')
    hoy = max((r['actualizado'] for r in rows if r['actualizado']), default='')
    body = f"""
<div class="wrap">
  <header class="mast">
    <div>
      <span class="logo"><img src="{logo_uri()}" alt="Performance Media Marketing"></span>
      <h1 data-t="title">Informes de clientes</h1>
      <p class="sub" data-t="sub">Todos los planes e informes de Google Ads publicados por el agente PMM, por cliente.</p>
    </div>
    <dl class="meta">
      <dt data-t="m_clients">Clientes</dt><dd class="num" id="m-clients"></dd>
      <dt data-t="m_reports">Informes</dt><dd class="num" id="m-reports"></dd>
      <dt data-t="m_updated">Actualizado</dt><dd class="num">{escape(hoy)}</dd>
    </dl>
  </header>

  <section id="clientes">
    <div class="ix-tools">
      <label class="ix-search-wrap" style="flex:1 1 240px; display:flex; min-width:0">
        <span class="lab" style="position:absolute; left:-9999px" data-t="search_label">Buscar</span>
        <input id="q" class="ix-search" type="search" autocomplete="off" placeholder="Buscar cliente, mercado o cuenta">
      </label>
      <div class="filters" role="group" aria-label="Nicho" style="margin:0"><div class="grp"><span class="lab" data-t="niche">Nicho</span><span id="f-niche"></span></div></div>
      <div class="filters ix-lang" role="group" aria-label="Idioma" style="margin:0"><div class="grp"><span id="f-lang"></span></div></div>
    </div>
    <div class="tbl"><table>
      <thead><tr>
        <th data-t="h_client">Cliente</th><th data-t="h_niche">Nicho</th><th data-t="h_market">Mercado</th>
        <th data-t="h_phase">Fase</th><th data-t="h_updated">Actualizado</th><th data-t="h_reports">Informes</th>
      </tr></thead>
      <tbody id="rows"></tbody>
    </table></div>
    <p class="empty-note" id="empty" hidden data-t="empty">Ningún cliente coincide con la búsqueda.</p>
  </section>

  <section id="otros">
    <div class="sec-head"><h2 data-t="others">Otros informes</h2><p data-t="others_sub">Cuentas sin carpeta de cliente en el repo.</p></div>
    <div class="tbl"><table><tbody id="others"></tbody></table></div>
  </section>

  <section id="acceso">
    <div class="callout">
      <h3 data-t="access">Si un enlace no abre</h3>
      <p data-t="access_p">Cada informe es un artefacto privado. Pídele a Jhombis que lo comparta contigo; los informes nuevos aparecen aquí cuando el agente los publica.</p>
    </div>
  </section>

  <footer>
    <span>Performance Media Marketing · <span data-t="foot">Índice de informes</span></span>
    <span data-t="foot_src">Fuente: clients/informes.json y los archivos de cada cliente en pmm-ads-agent</span>
  </footer>
</div>

<script>
(function(){{
  const D = {data};
  const T = {{
    es: {{title:'Informes de clientes', sub:'Todos los planes e informes de Google Ads publicados por el agente PMM, por cliente.', m_clients:'Clientes', m_reports:'Informes', m_updated:'Actualizado', search_label:'Buscar', ph:'Buscar cliente, mercado o cuenta', niche:'Nicho', all:'Todos', h_client:'Cliente', h_niche:'Nicho', h_market:'Mercado', h_phase:'Fase', h_updated:'Actualizado', h_reports:'Informes', empty:'Ningún cliente coincide con la búsqueda.', none:'Sin informe publicado', old:'anterior', extra:'complemento', phase:'Fase', others:'Otros informes', others_sub:'Cuentas sin carpeta de cliente en el repo.', access:'Si un enlace no abre', access_p:'Cada informe es un artefacto privado. Pídele a Jhombis que lo comparta contigo; los informes nuevos aparecen aquí cuando el agente los publica.', foot:'Índice de informes', foot_src:'Fuente: clients/informes.json y los archivos de cada cliente en pmm-ads-agent'}},
    en: {{title:'Client reports', sub:'Every Google Ads plan and report published by the PMM agent, by client.', m_clients:'Clients', m_reports:'Reports', m_updated:'Updated', search_label:'Search', ph:'Search client, market or account', niche:'Niche', all:'All', h_client:'Client', h_niche:'Niche', h_market:'Market', h_phase:'Phase', h_updated:'Updated', h_reports:'Reports', empty:'No client matches the search.', none:'No report published', old:'previous', extra:'add-on', phase:'Phase', others:'Other reports', others_sub:'Accounts without a client folder in the repo.', access:"If a link doesn't open", access_p:'Each report is a private artifact. Ask Jhombis to share it with you; new reports show up here when the agent publishes them.', foot:'Report index', foot_src:"Source: clients/informes.json and each client's files in pmm-ads-agent"}}
  }};
  const NICHE_EN = {{'towing':'Towing','electricista':'Electrician','funeraria / cremación':'Funeral / cremation','taller':'Auto repair','towing / roadside assistance':'Towing / roadside'}};
  const esc = s => String(s ?? '').replace(/[&<>"]/g, m => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[m]));
  const $ = id => document.getElementById(id);
  const group = n => n.startsWith('towing') ? 'towing' : n;
  const niches = [...new Set(D.clientes.map(c=>group(c.nicho)))];
  let lang = 'es', niche = 'all', q = '';
  try {{ const s = JSON.parse(localStorage.getItem('pmm-index') || 'null'); if (s) {{ if (T[s.lang]) lang = s.lang; if (s.niche==='all' || niches.includes(s.niche)) niche = s.niche; }} }} catch(e) {{}}
  const save = () => {{ try {{ localStorage.setItem('pmm-index', JSON.stringify({{lang, niche}})); }} catch(e) {{}} }};
  const nicheLabel = n => lang==='en' ? (NICHE_EN[n] || n) : n.charAt(0).toUpperCase() + n.slice(1);

  function btns(el, opts, cur, set){{
    el.innerHTML = opts.map(([v,l])=>`<button type="button" class="fbtn" aria-pressed="${{v===cur}}" data-v="${{esc(v)}}">${{esc(l)}}</button>`).join('');
    el.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{{ set(b.dataset.v); save(); render(); }}));
  }}
  function link(r){{
    const cls = r.anterior || r.extra ? 'ix-link old' : 'ix-link';
    const tag = r.anterior ? ' · ' + T[lang].old : r.extra ? ' · ' + T[lang].extra : '';
    return `<a class="${{cls}}" href="${{esc(r.url)}}" target="_blank" rel="noopener"><span class="lg">${{esc(r.idioma)}}</span>${{esc(r.titulo)}}${{esc(tag)}} ↗</a>`;
  }}
  function render(){{
    const t = T[lang];
    document.documentElement.lang = lang;
    document.querySelectorAll('[data-t]').forEach(el=>{{ if (t[el.dataset.t]) el.textContent = t[el.dataset.t]; }});
    $('q').placeholder = t.ph;
    btns($('f-niche'), [['all', t.all], ...niches.map(n=>[n, nicheLabel(n)])], niche, v=>niche=v);
    btns($('f-lang'), [['es','ES'],['en','EN']], lang, v=>lang=v);
    const words = q.toLowerCase().split(/\\s+/).filter(Boolean);
    const list = D.clientes.filter(c => (niche==='all' || group(c.nicho)===niche) &&
      words.every(w => [c.cliente, c.slug, c.mercado, c.cuenta, c.nicho].join(' ').toLowerCase().includes(w)));
    $('rows').innerHTML = list.map(c=>{{
      const main = c.informes.filter(r=>!r.anterior && !r.extra), rest = c.informes.filter(r=>r.anterior || r.extra);
      const f = c.fase === '' ? '' : `<span class="ix-phase"><i style="--c:${{D.colors[+c.fase] || 'var(--muted)'}}"></i>${{t.phase}} ${{esc(c.fase)}}</span>`;
      return `<tr>
        <td class="ix-name"><b>${{esc(c.cliente)}}</b>${{c.cuenta ? `<span class="mono">${{esc(c.cuenta)}}</span>` : ''}}</td>
        <td>${{esc(nicheLabel(c.nicho))}}</td>
        <td>${{esc(c.mercado)}}</td>
        <td>${{f}}</td>
        <td class="num" style="white-space:nowrap">${{esc(c.actualizado)}}</td>
        <td>${{c.informes.length ? `<div class="ix-links">${{main.map(link).join('')}}${{rest.map(link).join('')}}</div>` : `<span class="ix-none">${{t.none}}</span>`}}</td>
      </tr>`;
    }}).join('');
    $('empty').hidden = list.length > 0;
    $('others').innerHTML = D.otros.map(o=>`<tr><td class="ix-name"><b>${{esc(o.cliente)}}</b><span class="mono">${{esc(o.fecha || '')}}</span></td><td>${{esc(o.nota || '')}}</td><td><div class="ix-links">${{link(o)}}</div></td></tr>`).join('');
    $('otros').hidden = !D.otros.length;
  }}
  $('m-clients').textContent = D.clientes.length;
  $('m-reports').textContent = D.clientes.reduce((n,c)=>n + c.informes.filter(r=>!r.anterior && !r.extra).length, 0) + D.otros.length;
  $('q').addEventListener('input', e=>{{ q = e.target.value; render(); }});
  render();
}})();
</script>
"""
    # El artefacto agrega su propio <!doctype>/<head>; se publica desde el <title> en adelante.
    head = head[head.index('<title>'):]
    OUT.write_text(head + body)
    print(f'{OUT.relative_to(ROOT)}: {len(rows)} clientes')


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    build()
