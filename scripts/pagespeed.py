#!/usr/bin/env python3
"""PageSpeed Insights: python scripts/pagespeed.py <url> [--strategy mobile|desktop]. Usa PAGESPEED_API_KEY si existe."""
import argparse, json, os, sys, urllib.parse, urllib.request

ap = argparse.ArgumentParser()
ap.add_argument("url"); ap.add_argument("--strategy", default="mobile")
a = ap.parse_args()
params = {"url": a.url, "strategy": a.strategy, "category": "performance"}
if os.getenv("PAGESPEED_API_KEY"): params["key"] = os.environ["PAGESPEED_API_KEY"]
u = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?" + urllib.parse.urlencode(params)
d = json.load(urllib.request.urlopen(u, timeout=120))
lr = d["lighthouseResult"]; au = lr["audits"]
out = {
    "url": a.url, "strategy": a.strategy,
    "score": round(lr["categories"]["performance"]["score"] * 100),
    "LCP": au["largest-contentful-paint"]["displayValue"],
    "CLS": au["cumulative-layout-shift"]["displayValue"],
    "TBT": au["total-blocking-time"]["displayValue"],
    "peso_kb": round(au["total-byte-weight"]["numericValue"] / 1024),
    "oportunidades": [x["title"] for k, x in au.items() if x.get("details", {}).get("type") == "opportunity" and x.get("score", 1) < 0.9][:8],
}
print(json.dumps(out, indent=2, ensure_ascii=False))
