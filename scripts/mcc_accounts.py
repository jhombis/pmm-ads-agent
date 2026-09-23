#!/usr/bin/env python3
"""Lista cuentas cliente del MCC con sus etiquetas. Filtra por --nicho y --pais (etiquetas nicho:* / pais:*)."""
import argparse, csv, sys
from ads_client import get_client

client = get_client()
svc = client.get_service("GoogleAdsService")
mcc = client.login_customer_id

ap = argparse.ArgumentParser()
ap.add_argument("--nicho"); ap.add_argument("--pais")
a = ap.parse_args()

q = """SELECT customer_client.id, customer_client.descriptive_name,
       customer_client.currency_code, customer_client.status, customer_client.applied_labels
       FROM customer_client WHERE customer_client.level = 1 AND customer_client.status = 'ENABLED'"""
labels = {}
for b in svc.search_stream(customer_id=mcc, query="SELECT label.resource_name, label.name FROM label"):
    for r in b.results:
        labels[r.label.resource_name] = r.label.name

w = csv.writer(sys.stdout); w.writerow(["id", "nombre", "moneda", "etiquetas"])
for b in svc.search_stream(customer_id=mcc, query=q):
    for r in b.results:
        c = r.customer_client
        tags = [labels.get(l, l) for l in c.applied_labels]
        if a.nicho and f"nicho:{a.nicho}" not in tags: continue
        if a.pais and f"pais:{a.pais}" not in tags: continue
        w.writerow([c.id, c.descriptive_name, c.currency_code, ";".join(tags)])
