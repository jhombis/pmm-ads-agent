#!/usr/bin/env python3
"""Genera una landing a partir de un spec.json (lo escriben /landing y /landing-ghl).

Uso:
  python scripts/landing_build.py clients/<slug>/landings/<pagina>/spec.json
  python scripts/landing_build.py clients/<slug>/landings            # todas las páginas del cliente

Salida en la carpeta del spec:
  ghl-body.html          → GHL: elemento "Custom Code" (página en blanco, ancho completo)
  ghl-head.html          → GHL: Settings de la página → Head Tracking Code
  ghl-seo.md             → valores para Settings → SEO (title, description, slug, imagen social)
  gracias-body.html      → página de gracias: Custom Code
  gracias-head.html      → página de gracias: Head Tracking Code (dispara la conversión)
  preview.html           → página completa para revisar en el navegador (o publicar fuera de GHL)
  gracias-preview.html
  qa.md                  → checklist automático; código de salida 1 si hay bloqueantes
  publicar/              → SOLO esto se sube a Plesk (hosting.tipo = "plesk", lo pone /landing):
                           index.html y gracias/index.html, páginas completas para
                           https://performancemediamarketing.com/<hosting.ruta>/

Sin dependencias externas. El CSS va con prefijo .pmm- dentro de un contenedor propio para no chocar
con los estilos del builder de GHL.
"""
import json, re, sys, unicodedata
from html import escape
from pathlib import Path

PLESK_BASE = "https://performancemediamarketing.com"
PLESK_ROOT = "/var/www/vhosts/performancemediamarketing.com/httpdocs"

# Tipos schema.org por nicho (LocalBusiness si no hay uno específico)
SCHEMA_TYPES = {
    "plumbing": "Plumber", "plomeria": "Plumber", "electrician": "Electrician", "electricista": "Electrician",
    "hvac": "HVACBusiness", "roofing": "RoofingContractor", "locksmith": "Locksmith",
    "auto-repair": "AutoRepair", "taller": "AutoRepair", "towing": "AutomotiveBusiness",
    "dental": "Dentist", "abogado": "LegalService", "lawyer": "LegalService",
}
TXT = {
    "en": {"call": "Call Now", "quote": "Get a Free Quote", "reviews": "reviews", "area": "Areas We Serve",
           "faq": "Frequently Asked Questions", "privacy": "Privacy Policy", "license": "License",
           "form_pending": "GHL form pending: set ghl.form_id in spec.json", "hours": "Hours",
           "thanks_next": "What happens next", "or_call": "Need it faster? Call us now:"},
    "es": {"call": "Llamar ahora", "quote": "Cotización gratis", "reviews": "reseñas", "area": "Zonas que atendemos",
           "faq": "Preguntas frecuentes", "privacy": "Política de privacidad", "license": "Licencia",
           "form_pending": "Formulario GHL pendiente: completar ghl.form_id en spec.json", "hours": "Horario",
           "thanks_next": "Qué sigue", "or_call": "¿Lo necesitas ya? Llámanos:"},
}

CSS = """
.pmm-lp{--p:%(primario)s;--a:%(acento)s;--t:%(texto)s;--bg:%(fondo)s;--mut:#5b6472;--line:#e5e7eb;--soft:#f5f7fa;
font-family:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--t);background:var(--bg);
line-height:1.55;font-size:17px;-webkit-font-smoothing:antialiased}
.pmm-lp *{box-sizing:border-box;margin:0;padding:0}
.pmm-lp img{max-width:100%%;height:auto;display:block}
.pmm-lp a{color:inherit}
.pmm-w{max-width:1120px;margin:0 auto;padding:0 18px}
.pmm-top{position:sticky;top:0;z-index:50;background:var(--bg);border-bottom:1px solid var(--line)}
.pmm-top .pmm-w{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:62px}
.pmm-logo{font-weight:800;font-size:19px;text-decoration:none}
.pmm-logo img{max-height:44px;width:auto}
.pmm-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;font-weight:700;text-decoration:none;
border-radius:10px;padding:13px 20px;font-size:17px;line-height:1.2;border:0;cursor:pointer;text-align:center}
.pmm-btn-call{background:var(--a);color:#fff}
.pmm-btn-ghost{background:transparent;color:var(--p);border:2px solid var(--p)}
.pmm-hero{background:var(--soft);padding:34px 0 40px}
.pmm-hero .pmm-w{display:grid;gap:28px;grid-template-columns:1fr}
.pmm-badge{display:inline-flex;align-items:center;gap:6px;font-size:15px;font-weight:600;color:var(--mut);margin-bottom:12px}
.pmm-stars{color:#f5a623;letter-spacing:1px}
.pmm-lp h1{font-size:clamp(28px,5vw,44px);line-height:1.12;font-weight:800;letter-spacing:-.01em;margin-bottom:14px}
.pmm-sub{font-size:19px;color:var(--mut);margin-bottom:18px}
.pmm-offer{display:inline-block;background:var(--p);color:#fff;font-weight:700;border-radius:8px;padding:8px 14px;margin-bottom:18px}
.pmm-checks{list-style:none;display:grid;gap:8px;margin-bottom:22px}
.pmm-checks li{padding-left:30px;position:relative;font-weight:600}
.pmm-checks li:before{content:"";position:absolute;left:0;top:3px;width:20px;height:20px;border-radius:50%%;
background:var(--p) url("data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%%3E%%3Cpath d='M5 10.5l3 3 7-7' stroke='white' stroke-width='2.4' fill='none'/%%3E%%3C/svg%%3E") center/14px no-repeat}
.pmm-ctas{display:flex;flex-wrap:wrap;gap:10px}
.pmm-card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px;box-shadow:0 6px 24px rgba(16,24,40,.06)}
.pmm-form h2{font-size:22px;margin-bottom:4px}
.pmm-form p{color:var(--mut);font-size:15px;margin-bottom:10px}
.pmm-form-pending{border:2px dashed #d33;color:#d33;padding:30px;border-radius:10px;font-weight:700;text-align:center}
.pmm-heroimg{border-radius:14px;overflow:hidden;margin-top:18px}
.pmm-trust{border-bottom:1px solid var(--line);padding:18px 0}
.pmm-trust .pmm-w{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.pmm-trust div{font-size:15px}.pmm-trust b{display:block;font-size:17px}
.pmm-sec{padding:52px 0}.pmm-sec.pmm-alt{background:var(--soft)}
.pmm-lp h2{font-size:clamp(24px,3.6vw,32px);line-height:1.2;margin-bottom:12px;font-weight:800}
.pmm-lead{color:var(--mut);max-width:760px;margin-bottom:24px}
.pmm-grid{display:grid;gap:16px;grid-template-columns:1fr}
.pmm-grid h3{font-size:19px;margin-bottom:6px}
.pmm-steps{counter-reset:s}.pmm-steps .pmm-card{position:relative;padding-top:52px}
.pmm-steps .pmm-card:before{counter-increment:s;content:counter(s);position:absolute;top:16px;left:20px;width:28px;height:28px;
border-radius:50%%;background:var(--p);color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center}
.pmm-rev p{font-style:italic;margin:8px 0}.pmm-rev small{color:var(--mut)}
.pmm-cities{list-style:none;display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
.pmm-cities li{background:#fff;border:1px solid var(--line);border-radius:999px;padding:6px 14px;font-size:15px}
.pmm-map{margin-top:20px;border-radius:14px;overflow:hidden;border:1px solid var(--line)}
.pmm-map iframe{width:100%%;height:320px;border:0;display:block}
.pmm-faq details{border-bottom:1px solid var(--line);padding:16px 0}
.pmm-faq summary{font-weight:700;cursor:pointer;list-style:none;font-size:18px}
.pmm-faq summary::-webkit-details-marker{display:none}
.pmm-faq summary:after{content:"+";float:right;color:var(--p);font-size:22px;line-height:1}
.pmm-faq details[open] summary:after{content:"–"}
.pmm-faq details p{margin-top:8px;color:var(--mut)}
.pmm-final{background:var(--p);color:#fff;text-align:center}
.pmm-final .pmm-lead{color:rgba(255,255,255,.85);margin:0 auto 22px}
.pmm-final .pmm-btn-ghost{color:#fff;border-color:#fff}
.pmm-final .pmm-ctas{justify-content:center}
.pmm-foot{padding:28px 0 96px;font-size:14px;color:var(--mut);border-top:1px solid var(--line)}
.pmm-foot .pmm-w{display:grid;gap:6px}
.pmm-sticky{position:fixed;left:0;right:0;bottom:0;z-index:60;display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:10px;
background:#fff;box-shadow:0 -4px 18px rgba(0,0,0,.12)}
.pmm-sticky .pmm-btn{padding:14px 10px;font-size:16px}
.pmm-sticky .pmm-btn-ghost{background:var(--p);color:#fff;border-color:var(--p)}
.pmm-hide-m{display:none}.pmm-only-m{display:inline-flex}
@media(min-width:860px){
.pmm-hero .pmm-w{grid-template-columns:1.1fr .9fr;align-items:start}
.pmm-trust .pmm-w{grid-template-columns:repeat(4,1fr)}
.pmm-grid{grid-template-columns:repeat(3,1fr)}
.pmm-sticky{display:none}.pmm-foot{padding-bottom:28px}.pmm-hide-m{display:inline-flex}.pmm-only-m{display:none}}
"""

PHONE_SVG = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 '
             '15.1 0 006.6 6.6l2.2-2.2a1 1 0 011-.25 11.4 11.4 0 003.6.57 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 '
             '011-1h3.5a1 1 0 011 1c0 1.25.2 2.45.57 3.6a1 1 0 01-.25 1z"/></svg>')


def e(s):
    return escape(str(s or ""), quote=True)


def g(d, path, default=""):
    for k in path.split("."):
        if not isinstance(d, dict) or k not in d:
            return default
        d = d[k]
    return d if d not in (None, "") else default


def tel_href(s):
    digits = re.sub(r"[^\d+]", "", s or "")
    return f"tel:{digits}" if digits else ""


def call_btn(s, t, cls="pmm-btn pmm-btn-call", label=None, numero=True):
    tel = g(s, "negocio.telefono")
    shown = g(s, "negocio.telefono_display", tel) if numero else ""
    return (f'<a class="{cls}" href="{e(tel_href(tel))}" data-pmm-call>{PHONE_SVG}'
            f'<span>{e(label or t["call"])} {e(shown)}</span></a>')


def form_block(s, t):
    raw = g(s, "ghl.form_embed_html")
    fid = g(s, "ghl.form_id")
    if raw:
        inner = raw
    elif fid:
        base = g(s, "ghl.form_base", "https://api.leadconnectorhq.com").rstrip("/")
        h = int(g(s, "ghl.form_height", 520))
        inner = (f'<iframe src="{e(base)}/widget/form/{e(fid)}" style="width:100%;height:{h}px;border:none;border-radius:4px" '
                 f'id="inline-{e(fid)}" data-layout="{{\'id\':\'INLINE\'}}" data-trigger-type="alwaysShow" data-trigger-value="" '
                 f'data-activation-type="alwaysActivated" data-activation-value="" data-deactivation-type="neverDeactivate" '
                 f'data-deactivation-value="" data-form-name="{e(g(s, "ghl.form_name", "Lead form"))}" data-height="{h}" '
                 f'data-layout-iframe-id="inline-{e(fid)}" data-form-id="{e(fid)}" title="{e(g(s, "ghl.form_name", "Lead form"))}" '
                 f'loading="lazy"></iframe>\n'
                 # Pasa gclid/utm de la URL al formulario (campos ocultos con Query Key en GHL)
                 '<script>(function(){var f=document.getElementById("inline-' + e(fid) + '");if(f&&location.search){'
                 'f.src+=(f.src.indexOf("?")<0?"?":"&")+location.search.slice(1);}})();</script>\n'
                 f'<script src="{"https://link.msgsndr.com/js/form_embed.js"}"></script>')
    else:
        inner = f'<div class="pmm-form-pending">{e(t["form_pending"])}</div>'
    titulo = g(s, "hero.form_titulo", t["quote"])
    nota = g(s, "hero.form_nota")
    return (f'<div class="pmm-card pmm-form" id="pmm-form"><h2>{e(titulo)}</h2>'
            + (f'<p>{e(nota)}</p>' if nota else "") + inner + "</div>")


def items_grid(items, cls="pmm-grid", card="pmm-card"):
    return f'<div class="{cls}">' + "".join(
        f'<div class="{card}"><h3>{e(i.get("titulo"))}</h3><p>{e(i.get("texto"))}</p></div>' for i in items) + "</div>"


def section(h2, lead, body, alt=False, sid=""):
    return (f'<section class="pmm-sec{" pmm-alt" if alt else ""}"{f" id={chr(34)}{sid}{chr(34)}" if sid else ""}><div class="pmm-w">'
            f'<h2>{e(h2)}</h2>' + (f'<p class="pmm-lead">{e(lead)}</p>' if lead else "") + body + "</div></section>")


def css(s):
    m = {"primario": "#0b5cab", "acento": "#e8590c", "texto": "#111827", "fondo": "#ffffff"}
    m.update({k: v for k, v in (s.get("marca") or {}).items() if k in m and v})
    return "<style>" + " ".join(l.strip() for l in (CSS % m).splitlines()) + "</style>"


def header(s, t):
    neg = s.get("negocio", {})
    logo = (f'<img src="{e(neg["logo_url"])}" alt="{e(neg.get("nombre"))}" width="180" height="44">'
            if neg.get("logo_url") else e(neg.get("nombre")))
    return (f'<header class="pmm-top"><div class="pmm-w"><span class="pmm-logo">{logo}</span>'
            f'{call_btn(s, t, "pmm-btn pmm-btn-call pmm-hide-m")}'
            f'<a class="pmm-btn pmm-btn-call pmm-only-m" style="padding:10px 14px" href="{e(tel_href(g(s, "negocio.telefono")))}" '
            f'data-pmm-call aria-label="{e(t["call"])}">{PHONE_SVG}</a></div></header>')


def footer(s, t):
    neg = s.get("negocio", {})
    d = neg.get("direccion") or {}
    addr = ", ".join(x for x in [d.get("calle"), d.get("ciudad"), d.get("region"), d.get("cp")] if x)
    lines = [f'<b>{e(neg.get("nombre"))}</b>']
    if addr: lines.append(e(addr))
    if neg.get("telefono"): lines.append(f'<a href="{e(tel_href(neg["telefono"]))}" data-pmm-call>{e(neg.get("telefono_display", neg["telefono"]))}</a>')
    if neg.get("horario"): lines.append(f'{e(t["hours"])}: {e(neg["horario"])}')
    if neg.get("licencia"): lines.append(f'{e(t["license"])}: {e(neg["licencia"])}')
    if g(s, "legal.privacidad_url"): lines.append(f'<a href="{e(g(s, "legal.privacidad_url"))}">{e(t["privacy"])}</a>')
    return '<footer class="pmm-foot"><div class="pmm-w">' + "".join(f"<div>{x}</div>" for x in lines) + "</div></footer>"


def call_tracking_js(s):
    # Conversión por clic en tel: (solo si hay etiqueta de llamada y no se usa GTM)
    aw, lbl = g(s, "tracking.google_ads_id"), g(s, "tracking.conversion_label_call")
    if not (aw and lbl) or g(s, "tracking.gtm_id"):
        return ""
    return ('<script>document.addEventListener("click",function(ev){var a=ev.target.closest&&ev.target.closest("[data-pmm-call]");'
            f'if(a&&window.gtag){{gtag("event","conversion",{{send_to:"{e(aw)}/{e(lbl)}"}});}}}});</script>')


def body(s):
    t = TXT[s.get("idioma", "en")]
    h = s.get("hero", {})
    neg = s.get("negocio", {})
    r = neg.get("rating") or {}
    out = [f'<div class="pmm-lp">{css(s)}', header(s, t)]

    badge = ""
    if r.get("valor") and r.get("total"):
        badge = (f'<div class="pmm-badge"><span class="pmm-stars">★★★★★</span> {e(r["valor"])} · {e(r["total"])} '
                 f'{e(t["reviews"])}{" " + e(r["fuente"]) if r.get("fuente") else ""}</div>')
    img = h.get("imagen") or {}
    hero_img = (f'<div class="pmm-heroimg"><img src="{e(img["src"])}" alt="{e(img.get("alt"))}" width="{e(img.get("ancho", 1200))}" '
                f'height="{e(img.get("alto", 800))}" fetchpriority="high"></div>') if img.get("src") else ""
    out.append(
        '<section class="pmm-hero"><div class="pmm-w"><div>' + badge + f'<h1>{e(h.get("h1"))}</h1>'
        + (f'<p class="pmm-sub">{e(h.get("subtitulo"))}</p>' if h.get("subtitulo") else "")
        + (f'<div class="pmm-offer">{e(h.get("oferta"))}</div>' if h.get("oferta") else "")
        + ('<ul class="pmm-checks">' + "".join(f"<li>{e(b)}</li>" for b in h.get("bullets", [])) + "</ul>" if h.get("bullets") else "")
        + '<div class="pmm-ctas">' + call_btn(s, t, label=h.get("cta_llamar"))
        + f'<a class="pmm-btn pmm-btn-ghost" href="#pmm-form">{e(h.get("cta_form") or t["quote"])}</a></div>'
        + hero_img + "</div>" + form_block(s, t) + "</div></section>")

    if s.get("confianza"):
        out.append('<div class="pmm-trust"><div class="pmm-w">' + "".join(
            f'<div><b>{e(c.get("titulo"))}</b>{e(c.get("texto"))}</div>' for c in s["confianza"]) + "</div></div>")
    alt = False
    for key in ("incluye", "por_que"):
        sec = s.get(key)
        if sec and sec.get("items"):
            out.append(section(sec.get("h2"), sec.get("intro"), items_grid(sec["items"]), alt)); alt = not alt
    if (s.get("proceso") or {}).get("pasos"):
        p = s["proceso"]
        out.append(section(p.get("h2"), p.get("intro"), items_grid(p["pasos"], "pmm-grid pmm-steps"), alt)); alt = not alt
    revs = [x for x in (s.get("resenas") or {}).get("items", []) if x.get("texto")]
    if revs:
        cards = "".join(f'<div class="pmm-card pmm-rev"><span class="pmm-stars">{"★" * int(x.get("estrellas", 5))}</span>'
                        f'<p>“{e(x["texto"])}”</p><small>— {e(x.get("autor"))}{", " + e(x["fuente"]) if x.get("fuente") else ""}</small></div>'
                        for x in revs)
        out.append(section(s["resenas"].get("h2"), s["resenas"].get("intro"), f'<div class="pmm-grid">{cards}</div>', alt)); alt = not alt
    z = s.get("zona") or {}
    if z.get("ciudades"):
        mapa = (f'<div class="pmm-map"><iframe src="{e(z["mapa_embed_url"])}" loading="lazy" title="{e(neg.get("nombre"))}" '
                'referrerpolicy="no-referrer-when-downgrade"></iframe></div>') if z.get("mapa_embed_url") else ""
        out.append(section(z.get("h2") or t["area"], z.get("texto"),
                           '<ul class="pmm-cities">' + "".join(f"<li>{e(c)}</li>" for c in z["ciudades"]) + "</ul>" + mapa, alt))
        alt = not alt
    f = s.get("faq") or {}
    if f.get("items"):
        out.append(section(f.get("h2") or t["faq"], None, '<div class="pmm-faq">' + "".join(
            f'<details><summary>{e(q.get("q"))}</summary><p>{e(q.get("a"))}</p></details>' for q in f["items"]) + "</div>", alt))
    c = s.get("cta_final") or {}
    out.append(f'<section class="pmm-sec pmm-final"><div class="pmm-w"><h2>{e(c.get("h2") or h.get("h1"))}</h2>'
               + (f'<p class="pmm-lead">{e(c.get("texto"))}</p>' if c.get("texto") else "")
               + f'<div class="pmm-ctas">{call_btn(s, t, label=h.get("cta_llamar"))}'
               f'<a class="pmm-btn pmm-btn-ghost" href="#pmm-form">{e(h.get("cta_form") or t["quote"])}</a></div></div></section>')
    out.append(footer(s, t))
    out.append(f'<nav class="pmm-sticky">{call_btn(s, t, numero=False)}'
               f'<a class="pmm-btn pmm-btn-ghost" href="#pmm-form">{e(t["quote"])}</a></nav>')
    out.append(call_tracking_js(s))
    if g(s, "ghl.chat_widget_html"):
        out.append(g(s, "ghl.chat_widget_html"))
    out.append("</div>")
    return "\n".join(x for x in out if x)


def tag_snippets(s):
    gtm, aw, ga4 = g(s, "tracking.gtm_id"), g(s, "tracking.google_ads_id"), g(s, "tracking.ga4_id")
    if gtm:
        return ("<!-- Google Tag Manager -->\n<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),"
                "event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;"
                f"j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{e(gtm)}');</script>")
    ids = [x for x in (aw, ga4) if x]
    if not ids:
        return ""
    return (f'<script async src="https://www.googletagmanager.com/gtag/js?id={e(ids[0])}"></script>\n<script>window.dataLayer=window.dataLayer||[];'
            "function gtag(){dataLayer.push(arguments);}gtag('js',new Date());"
            + "".join(f"gtag('config','{e(i)}');" for i in ids) + "</script>")


def jsonld(s):
    neg, pag = s.get("negocio", {}), s.get("pagina", {})
    d = neg.get("direccion") or {}
    stype = neg.get("schema_type") or SCHEMA_TYPES.get((s.get("nicho") or "").lower(), "LocalBusiness")
    biz = {"@type": stype, "@id": (neg.get("url_sitio") or pag.get("url_final", "")).rstrip("/") + "/#business",
           "name": neg.get("nombre"), "telephone": neg.get("telefono"), "url": neg.get("url_sitio") or pag.get("url_final")}
    if d: biz["address"] = {"@type": "PostalAddress", "streetAddress": d.get("calle"), "addressLocality": d.get("ciudad"),
                            "addressRegion": d.get("region"), "postalCode": d.get("cp"), "addressCountry": d.get("pais")}
    if neg.get("logo_url"): biz["image"] = neg["logo_url"]
    if neg.get("gbp_url"): biz["sameAs"] = [neg["gbp_url"]]
    if neg.get("horario_schema"): biz["openingHours"] = neg["horario_schema"]
    ciudades = (s.get("zona") or {}).get("ciudades", [])
    if ciudades: biz["areaServed"] = [{"@type": "City", "name": c} for c in ciudades]
    graph = [biz, {"@type": "Service", "name": pag.get("servicio"), "serviceType": pag.get("servicio"),
                   "provider": {"@id": biz["@id"]}, "url": pag.get("url_final"),
                   "areaServed": biz.get("areaServed", pag.get("ciudad"))}]
    faq = (s.get("faq") or {}).get("items", [])
    if faq:
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q.get("q"),
                     "acceptedAnswer": {"@type": "Answer", "text": q.get("a")}} for q in faq]})
    clean = lambda o: {k: clean(v) if isinstance(v, dict) else [clean(x) if isinstance(x, dict) else x for x in v] if isinstance(v, list) else v
                       for k, v in o.items() if v not in (None, "", [], {})}
    return ('<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [clean(x) for x in graph]},
            ensure_ascii=False).replace("</", "<\\/") + "</script>")


def head(s):
    pag = s.get("pagina", {})
    parts = ['<!-- PMM · pegar en Settings → Head Tracking Code de esta página -->',
             '<meta name="viewport" content="width=device-width, initial-scale=1">']
    if pag.get("url_final"): parts.append(f'<link rel="canonical" href="{e(pag["url_final"])}">')
    if pag.get("indexar") is False: parts.append('<meta name="robots" content="noindex, follow">')
    parts += ['<link rel="preconnect" href="https://api.leadconnectorhq.com">', tag_snippets(s), jsonld(s)]
    return "\n".join(p for p in parts if p) + "\n"


def gracias_body(s):
    t = TXT[s.get("idioma", "en")]
    gr = s.get("gracias") or {}
    pasos = gr.get("pasos") or []
    return "\n".join([f'<div class="pmm-lp">{css(s)}', header(s, t),
        f'<section class="pmm-sec"><div class="pmm-w" style="max-width:760px"><h1>{e(gr.get("h1"))}</h1>'
        + (f'<p class="pmm-sub">{e(gr.get("texto"))}</p>' if gr.get("texto") else "")
        + (f'<h2 style="margin-top:24px">{e(t["thanks_next"])}</h2>' + items_grid(pasos, "pmm-grid pmm-steps") if pasos else "")
        + f'<p style="margin:28px 0 12px;font-weight:700">{e(t["or_call"])}</p>{call_btn(s, t)}</div></section>',
        footer(s, t), call_tracking_js(s), "</div>"])


def gracias_head(s):
    aw, lbl = g(s, "tracking.google_ads_id"), g(s, "tracking.conversion_label_form")
    parts = ['<!-- PMM · Head Tracking Code de la página de GRACIAS -->', '<meta name="robots" content="noindex, nofollow">',
             '<meta name="viewport" content="width=device-width, initial-scale=1">', tag_snippets(s)]
    if g(s, "tracking.gtm_id"):
        parts.append("<script>window.dataLayer=window.dataLayer||[];dataLayer.push({event:'pmm_lead_form'});</script>"
                     "<!-- En GTM: activador Custom Event = pmm_lead_form → etiqueta de conversión de Google Ads -->")
    elif aw and lbl:
        parts.append(f"<script>gtag('event','conversion',{{send_to:'{e(aw)}/{e(lbl)}'}});</script>")
    return "\n".join(p for p in parts if p) + "\n"


def preview(s, body_html, head_html, title, desc):
    lang = s.get("idioma", "en")
    og = g(s, "pagina.og_image")
    return (f'<!doctype html>\n<html lang="{e(lang)}"><head><meta charset="utf-8"><title>{e(title)}</title>'
            f'<meta name="description" content="{e(desc)}">'
            f'<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">'
            + (f'<meta property="og:image" content="{e(og)}">' if og else "")
            + f"\n{head_html}</head><body style=\"margin:0\">\n{body_html}\n</body></html>\n")


def qa(s, body_html):
    pag, h = s.get("pagina", {}), s.get("hero", {})
    kw = (pag.get("keyword_principal") or "").lower()
    title, desc, slug = pag.get("title", ""), pag.get("meta_description", ""), pag.get("slug", "")
    visible = re.sub(r"<style>.*?</style>|<script.*?</script>|<svg.*?</svg>", " ", body_html, flags=re.S)
    words = len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", visible)))
    plain = lambda x: unicodedata.normalize("NFKD", x.lower()).encode("ascii", "ignore").decode()  # sin tildes
    kw_words = [w for w in re.findall(r"\w+", plain(kw)) if len(w) > 2]
    has = lambda txt: bool(kw_words) and all(w in plain(txt) for w in kw_words)
    checks = [  # (bloqueante, ok, descripción)
        (True, bool(g(s, "negocio.telefono")), "Teléfono con clic para llamar"),
        (True, bool(g(s, "ghl.form_id") or g(s, "ghl.form_embed_html")), "Formulario GHL embebido (ghl.form_id)"),
        (True, bool(g(s, "legal.privacidad_url")), "Enlace a política de privacidad (requisito de Google Ads al pedir datos)"),
        (True, bool(g(s, "tracking.gtm_id") or (g(s, "tracking.google_ads_id") and g(s, "tracking.conversion_label_form"))),
         "Conversión de formulario configurada (GTM o AW-ID + etiqueta)"),
        (True, bool(h.get("h1")) and has(h.get("h1", "")), f"H1 contiene la keyword principal «{kw}»"),
        (True, "PENDIENTE" not in json.dumps(s, ensure_ascii=False) and "TODO" not in body_html, "Sin textos PENDIENTE/TODO"),
        (False, 30 <= len(title) <= 60, f"Title 30–60 caracteres (tiene {len(title)})"),
        (False, has(title), "Title contiene la keyword"),
        (False, 70 <= len(desc) <= 160, f"Meta description 70–160 caracteres (tiene {len(desc)})"),
        (False, bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug)), f"Slug limpio ({slug or 'vacío'})"),
        (False, bool(g(s, "tracking.conversion_label_call") or g(s, "tracking.gtm_id")), "Conversión por clic en llamada"),
        (False, bool((s.get("resenas") or {}).get("items")) or bool(g(s, "negocio.rating.total")), "Prueba social visible"),
        (False, all(x.get("fuente") for x in (s.get("resenas") or {}).get("items", [])), "Cada reseña indica su fuente (no inventadas)"),
        (False, bool(h.get("oferta")), "Oferta concreta en el hero"),
        (False, bool((s.get("faq") or {}).get("items")), "FAQ (contenido + schema)"),
        (False, words >= 400 or pag.get("indexar") is False, f"Contenido suficiente para indexar ({words} palabras; ≥400 o noindex)"),
        (False, all(re.search(r'alt="[^"]+"', i) for i in re.findall(r"<img[^>]*>", body_html)), "Todas las imágenes con alt"),
        (False, len(body_html.encode()) < 60_000, f"Peso del bloque body {len(body_html.encode()) // 1024} KB (<60 KB)"),
        (False, bool(g(s, "gracias.h1")), "Página de gracias definida"),
    ]
    bloq = [c for c in checks if c[0] and not c[1]]
    lines = [f"# QA — {pag.get('slug', '')}", "", f"**Bloqueantes abiertos: {len(bloq)}**", ""]
    lines += [f"- [{'x' if ok else ' '}] {'**BLOQUEANTE** ' if b and not ok else ''}{d}" for b, ok, d in checks]
    return "\n".join(lines) + "\n", len(bloq)


def seo_md(s, gr_slug):
    pag = {k: v.replace("|", "\\|") if isinstance(v, str) else v for k, v in s.get("pagina", {}).items()}
    return f"""# SEO para GHL — {pag.get('servicio', '')}

Pegar en GHL → página → **Settings → SEO Meta Data** (y en la ruta/path del paso).

| Campo GHL | Valor |
|---|---|
| Path / slug | `{pag.get('slug', '')}` |
| Title | {pag.get('title', '')} |
| Description | {pag.get('meta_description', '')} |
| Keywords | {', '.join(pag.get('keywords_secundarias', []) or [pag.get('keyword_principal', '')])} |
| Social image | {pag.get('og_image', '—')} |
| Indexar | {'no (noindex en head)' if pag.get('indexar') is False else 'sí'} |
| URL final (Ads) | {pag.get('url_final', '')} |
| Página de gracias (path) | `{gr_slug}` |

Formulario GHL → **On submit: Open URL** → `{(s.get('gracias') or {}).get('url') or (pag.get('url_final') or '').rsplit('/', 1)[0] + '/' + gr_slug}`
"""


def plesk_setup(s, spec_path):
    """Hosting en performancemediamarketing.com/<ruta>/: fija la URL final y la de gracias.
    Por defecto noindex: el dominio es de PMM, no del cliente (ver docs/publicar-plesk.md)."""
    h = s.setdefault("hosting", {})
    if h.get("tipo", "ghl") != "plesk":  # sin hosting = GHL (specs anteriores a /landing)
        return None
    pag = s.setdefault("pagina", {})
    ruta = (h.get("ruta") or pag.get("slug") or "").strip("/")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*(/[a-z0-9]+(-[a-z0-9]+)*)?", ruta):
        sys.exit(f"{spec_path}: hosting.ruta inválida ({ruta!r}); usar <cliente> o <cliente>/<servicio>, minúsculas y guiones")
    h.update(tipo="plesk", ruta=ruta)
    pag["url_final"] = f"{PLESK_BASE}/{ruta}/"
    pag.setdefault("indexar", False)
    s.setdefault("gracias", {})["url"] = f"{PLESK_BASE}/{ruta}/gracias/"
    return ruta


def build(spec_path):
    spec_path = Path(spec_path)
    s = json.loads(spec_path.read_text())
    s.setdefault("idioma", "en")
    if s["idioma"] not in TXT:
        sys.exit(f"{spec_path}: idioma debe ser en|es")
    out = spec_path.parent
    ruta = plesk_setup(s, spec_path)
    pag = s.get("pagina", {})
    gr_slug = g(s, "gracias.slug", (pag.get("slug") or "pagina") + ("-thank-you" if s["idioma"] == "en" else "-gracias"))
    if ruta:
        gr_slug = f"{ruta}/gracias"
    b, hd = body(s), head(s)
    gb, gh = gracias_body(s), gracias_head(s)
    files = {
        "ghl-body.html": b, "ghl-head.html": hd, "ghl-seo.md": seo_md(s, gr_slug),
        "gracias-body.html": gb, "gracias-head.html": gh,
        "preview.html": preview(s, b, hd, pag.get("title", ""), pag.get("meta_description", "")),
        "gracias-preview.html": preview(s, gb, gh, g(s, "gracias.h1"), ""),
    }
    report, n = qa(s, b)
    files["qa.md"] = report
    if ruta:
        strip = lambda h: re.sub(r"<!-- PMM · [^>]*-->\n?", "", h)
        files["publicar/index.html"] = preview(s, b, strip(hd), pag.get("title", ""), pag.get("meta_description", ""))
        files["publicar/gracias/index.html"] = preview(s, gb, strip(gh), g(s, "gracias.h1"), "")
        files["publicar/MANIFIESTO.txt"] = (
            f"URL: {pag['url_final']}\nGracias: {s['gracias']['url']}\n"
            f"{PLESK_ROOT}/{ruta}/index.html          <- publicar/index.html\n"
            f"{PLESK_ROOT}/{ruta}/gracias/index.html  <- publicar/gracias/index.html\n"
            "No subir nada más (spec.json, qa.md, ghl-*, preview.html quedan en el repo).\n")
    for name, content in files.items():
        (out / name).parent.mkdir(parents=True, exist_ok=True)
        (out / name).write_text(content)
    print(f"{out}: {len(b.encode()) // 1024} KB body · bloqueantes QA: {n}")
    return n


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    p = Path(sys.argv[1])
    specs = [p] if p.is_file() else sorted(p.glob("*/spec.json"))
    if not specs:
        sys.exit(f"No hay spec.json en {p}")
    total = sum(build(x) for x in specs)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
