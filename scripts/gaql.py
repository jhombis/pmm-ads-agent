#!/usr/bin/env python3
"""Ejecuta una consulta GAQL contra una cuenta del MCC y devuelve CSV o JSON.

Uso:
  python scripts/gaql.py --customer 1234567890 --query "SELECT campaign.name, metrics.cost_micros FROM campaign WHERE segments.date DURING LAST_30_DAYS"
  python scripts/gaql.py --customer 1234567890 --file scripts/queries/benchmark.gaql --format json > clients/x/data/2026-09-22-campaigns.json
"""
import argparse, csv, json, sys
from pathlib import Path

from ads_client import get_client


def flatten(row, prefix=""):
    out = {}
    for k, v in row.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            out.update(flatten(v, key))
        else:
            out[key] = v
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--customer", required=True, help="Customer ID sin guiones")
    ap.add_argument("--query")
    ap.add_argument("--file")
    ap.add_argument("--format", choices=["csv", "json"], default="csv")
    a = ap.parse_args()
    query = a.query or Path(a.file).read_text()
    if not query:
        sys.exit("Falta --query o --file")

    client = get_client()
    svc = client.get_service("GoogleAdsService")
    from google.protobuf.json_format import MessageToDict

    rows = []
    for batch in svc.search_stream(customer_id=a.customer, query=query):
        for r in batch.results:
            rows.append(flatten(MessageToDict(r._pb, preserving_proto_field_name=True)))

    if a.format == "json":
        json.dump(rows, sys.stdout, indent=2, ensure_ascii=False)
    else:
        if not rows:
            return
        keys = sorted({k for r in rows for k in r})
        w = csv.DictWriter(sys.stdout, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
