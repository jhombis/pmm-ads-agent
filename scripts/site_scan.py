#!/usr/bin/env python3
"""Escaneo estructurado del sitio de un cliente para /investigar-cliente y /audit-landing.

Uso:
  python scripts/site_scan.py https://cliente.com > clients/<slug>/data/site-scan.json
  python scripts/site_scan.py https://cliente.com --max 25

Baja la home y hasta --max páginas internas (prioriza las de servicios/ciudades/contacto) y extrae:
título, H1, meta description, teléfonos (tel:), WhatsApp, emails, formularios (campos y action),
JSON-LD (LocalBusiness: dirección, areaServed, horario, rating), tags de tracking, redes sociales
y frases de confianza/oferta (licensed, insured, 24/7, free estimate, garantía, años...).
Requiere acceso de red al dominio del cliente.
"""
import argparse, json, re, sys, urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

UA = "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Mobile Safari/537.36"
PRIORIDAD = re.compile(r"servic|service|repair|install|emergenc|towing|plumb|electric|hvac|roof|"
                       r"about|nosotros|contact|contacto|area|ciudad|city|location|ubicaci|price|precio|"
                       r"review|testimon|reseñ|financ|coupon|oferta|special", re.I)
TRACKING_IDS = {  # devuelve los IDs encontrados
    "ga4": r"\bG-[A-Z0-9]{6,12}\b", "google_ads": r"\bAW-\d{6,12}\b", "gtm": r"\bGTM-[A-Z0-9]{4,8}\b",
    "ua": r"\bUA-\d{4,10}-\d+\b", "meta_pixel": r"fbq\(\s*['\"]init['\"]\s*,\s*['\"](\d+)",
}
TRACKING_FLAGS = {"callrail": r"callrail", "clarity": r"clarity\.ms", "hotjar": r"hotjar"}  # presencia
FRASES = re.compile(r"[^.!?\n]{0,80}\b(licen[cs]ed|insured|bonded|certified|24/7|24 hours|same[- ]day|"
                    r"free (estimate|quote|inspection)|no (service|trip) (fee|charge)|financing|warranty|"
                    r"guarantee|\d+\+? years|family[- ]owned|garant[ií]a|cotizaci[oó]n gratis|a[nñ]os de "
                    r"experiencia|licencia|asegurad|financiaci[oó]n|descuento|\d+% off|coupon)\b[^.!?\n]{0,80}",
                    re.I)
SOCIAL = re.compile(r"(facebook|instagram|youtube|tiktok|linkedin|yelp|google\.com/maps|g\.page|"
                    r"bbb\.org|angi|homeadvisor|nextdoor)", re.I)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""; self.h1 = []; self.h2 = []; self.meta = ""; self.links = []
        self.forms = []; self.jsonld = []; self._tag = None; self._buf = ""; self._form = None
        self.text = []; self._skip = 0  # dentro de <script>/<style>: no es texto visible

    def handle_starttag(self, tag, attrs):
        at = dict(attrs)
        if tag in ("script", "style", "noscript"):
            self._skip += 1
        if tag in ("title", "h1", "h2") or (tag == "script" and at.get("type") == "application/ld+json"):
            self._tag, self._buf = (tag if tag != "script" else "ld"), ""
        if tag == "meta" and at.get("name", "").lower() == "description":
            self.meta = at.get("content", "")
        if tag == "a" and at.get("href"):
            self.links.append(at["href"])
        if tag == "form":
            self._form = {"action": at.get("action", ""), "campos": [], "id": at.get("id", "")}
        if tag in ("input", "select", "textarea") and self._form is not None:
            if at.get("type", "text") not in ("hidden", "submit", "button"):
                self._form["campos"].append(at.get("name") or at.get("placeholder") or at.get("type", tag))

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript") and self._skip:
            self._skip -= 1
        if tag == "form" and self._form is not None:
            self.forms.append(self._form); self._form = None
        if self._tag and (tag == self._tag or (self._tag == "ld" and tag == "script")):
            t = " ".join(self._buf.split())
            if self._tag == "title": self.title = t
            elif self._tag == "h1": self.h1.append(t)
            elif self._tag == "h2": self.h2.append(t)
            elif self._tag == "ld": self.jsonld.append(self._buf)
            self._tag = None

    def handle_data(self, data):
        if self._tag: self._buf += data
        if not self._skip and self._tag != "title": self.text.append(data)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.geturl(), r.read(3_000_000).decode(r.headers.get_content_charset() or "utf-8", "replace")


def ld_items(raw):
    try:
        d = json.loads(raw)
    except Exception:
        return []
    items = d if isinstance(d, list) else d.get("@graph", [d]) if isinstance(d, dict) else []
    keep = ("@type", "name", "telephone", "address", "areaServed", "openingHours",
            "openingHoursSpecification", "aggregateRating", "priceRange", "sameAs", "geo", "foundingDate")
    return [{k: i[k] for k in keep if k in i} for i in items if isinstance(i, dict)]


def scan(url, html):
    p = Page(); p.feed(html)
    text = " ".join(" ".join(p.text).split())
    hrefs = [urljoin(url, h) for h in p.links]
    return {
        "url": url, "title": p.title, "h1": p.h1[:3], "h2": p.h2[:12], "meta_description": p.meta,
        "telefonos": sorted({h[4:].strip() for h in p.links if h.lower().startswith("tel:")}),
        "whatsapp": sorted({h for h in hrefs if "wa.me" in h or "whatsapp" in h.lower()}),
        "emails": sorted({h[7:].split("?")[0] for h in p.links if h.lower().startswith("mailto:")}),
        "formularios": [{**f, "n_campos": len(f["campos"])} for f in p.forms],
        "jsonld": [x for raw in p.jsonld for x in ld_items(raw)],
        "tracking": {**{k: sorted(set(re.findall(v, html)))[:5] for k, v in TRACKING_IDS.items()},
                     **{k: bool(re.search(v, html, re.I)) for k, v in TRACKING_FLAGS.items()}},
        "social": sorted({h for h in hrefs if SOCIAL.search(h)})[:15],
        "frases_confianza_oferta": sorted({m.group(0).strip() for m in FRASES.finditer(text)})[:25],
        "palabras": len(text.split()),
    }, hrefs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url"); ap.add_argument("--max", type=int, default=15)
    a = ap.parse_args()
    url = a.url if a.url.startswith("http") else "https://" + a.url
    out = {"sitio": url, "paginas": [], "errores": [], "internas_no_visitadas": []}
    try:
        final, html = fetch(url)
    except Exception as e:
        out["errores"].append(f"{url}: {e}")
        json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
        sys.exit(2)
    home, hrefs = scan(final, html)
    out["paginas"].append(home)
    dom = urlparse(final).netloc.replace("www.", "")
    internas = []
    for h in hrefs:
        u = urlparse(h)
        if u.netloc.replace("www.", "") == dom and u.scheme.startswith("http") \
                and not re.search(r"\.(jpg|jpeg|png|pdf|webp|svg|zip)$", u.path, re.I):
            clean = f"{u.scheme}://{u.netloc}{u.path}".rstrip("/")
            if clean != final.rstrip("/") and clean not in internas:
                internas.append(clean)
    internas.sort(key=lambda x: 0 if PRIORIDAD.search(x) else 1)
    for u in internas[:a.max]:
        try:
            f, h = fetch(u)
            out["paginas"].append(scan(f, h)[0])
        except Exception as e:
            out["errores"].append(f"{u}: {e}")
    out["internas_no_visitadas"] = internas[a.max:]
    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
