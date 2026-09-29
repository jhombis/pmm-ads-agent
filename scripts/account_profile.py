#!/usr/bin/env python3
"""Perfil completo de una cuenta del MCC para /investigar-cliente: configuración, historial,
geo, horarios, conversiones, extensiones, anuncios, keywords, search terms y landings.

Uso:
  python scripts/account_profile.py --customer 1234567890 > clients/<slug>/data/account-profile.json
  python scripts/account_profile.py --customer 1234567890 --dias 180

Cada sección corre por separado: si una consulta falla, se anota el error y se sigue.
Los montos *_micros se dividen entre 1.000.000 para obtener la moneda de la cuenta.
"""
import argparse, json, sys
from datetime import date, timedelta
from pathlib import Path

try:
    from google.ads.googleads.client import GoogleAdsClient
    from google.protobuf.json_format import MessageToDict
except ImportError:
    sys.exit("Falta google-ads: pip install google-ads --break-system-packages")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gaql import flatten  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

ap = argparse.ArgumentParser()
ap.add_argument("--customer", required=True, help="Customer ID sin guiones")
ap.add_argument("--dias", type=int, default=365, help="Ventana de historial (default 365)")
a = ap.parse_args()

hasta = date.today() - timedelta(days=1)
desde = hasta - timedelta(days=a.dias - 1)
RANGO = f"segments.date BETWEEN '{desde}' AND '{hasta}'"

QUERIES = {
    "cuenta": """SELECT customer.id, customer.descriptive_name, customer.currency_code,
        customer.time_zone, customer.auto_tagging_enabled,
        customer.conversion_tracking_setting.conversion_tracking_status
        FROM customer""",
    "historial_mensual": f"""SELECT segments.month, metrics.cost_micros, metrics.impressions,
        metrics.clicks, metrics.conversions, metrics.conversions_value
        FROM customer WHERE {RANGO}""",
    "campanas": f"""SELECT campaign.id, campaign.name, campaign.status,
        campaign.advertising_channel_type, campaign.bidding_strategy_type,
        campaign.target_cpa.target_cpa_micros, campaign_budget.amount_micros,
        campaign.network_settings.target_search_network,
        campaign.network_settings.target_partner_search_network,
        campaign.network_settings.target_content_network,
        campaign.geo_target_type_setting.positive_geo_target_type,
        metrics.cost_micros, metrics.clicks, metrics.conversions
        FROM campaign WHERE {RANGO} AND campaign.status != 'REMOVED'""",
    "geo": """SELECT campaign.name, campaign.status, campaign_criterion.type,
        campaign_criterion.negative, campaign_criterion.location.geo_target_constant,
        campaign_criterion.proximity.radius, campaign_criterion.proximity.radius_units,
        campaign_criterion.proximity.address.city_name,
        campaign_criterion.proximity.address.postal_code
        FROM campaign_criterion
        WHERE campaign_criterion.type IN ('LOCATION', 'PROXIMITY')
          AND campaign.status != 'REMOVED'""",
    "horarios": """SELECT campaign.name, campaign.status,
        campaign_criterion.ad_schedule.day_of_week,
        campaign_criterion.ad_schedule.start_hour, campaign_criterion.ad_schedule.end_hour
        FROM campaign_criterion
        WHERE campaign_criterion.type = 'AD_SCHEDULE' AND campaign.status != 'REMOVED'""",
    "conversiones": f"""SELECT conversion_action.name, conversion_action.type,
        conversion_action.category, conversion_action.status,
        conversion_action.primary_for_goal, conversion_action.counting_type,
        metrics.all_conversions
        FROM conversion_action WHERE {RANGO}""",
    "extensiones": """SELECT asset.type, asset.name, asset.call_asset.phone_number,
        asset.call_asset.country_code, asset.callout_asset.callout_text,
        asset.sitelink_asset.link_text, asset.sitelink_asset.description1,
        asset.structured_snippet_asset.header, asset.structured_snippet_asset.values,
        asset.final_urls
        FROM asset
        WHERE asset.type IN ('CALL', 'CALLOUT', 'SITELINK', 'STRUCTURED_SNIPPET')""",
    "anuncios": f"""SELECT campaign.name, ad_group.name, ad_group_ad.status,
        ad_group_ad.ad.final_urls, ad_group_ad.ad.responsive_search_ad.headlines,
        ad_group_ad.ad.responsive_search_ad.descriptions,
        metrics.impressions, metrics.clicks, metrics.conversions
        FROM ad_group_ad WHERE {RANGO} AND ad_group_ad.status != 'REMOVED'
        ORDER BY metrics.impressions DESC LIMIT 50""",
    "keywords_top": f"""SELECT campaign.name, ad_group.name,
        ad_group_criterion.keyword.text, ad_group_criterion.keyword.match_type,
        metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions
        FROM keyword_view WHERE {RANGO}
        ORDER BY metrics.cost_micros DESC LIMIT 200""",
    "search_terms_top": f"""SELECT search_term_view.search_term,
        metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions
        FROM search_term_view WHERE {RANGO}
        ORDER BY metrics.cost_micros DESC LIMIT 300""",
    "landings": f"""SELECT landing_page_view.unexpanded_final_url,
        metrics.clicks, metrics.cost_micros, metrics.conversions
        FROM landing_page_view WHERE {RANGO}
        ORDER BY metrics.clicks DESC LIMIT 50""",
}

client = GoogleAdsClient.load_from_storage(str(ROOT / "google-ads.yaml"))
svc = client.get_service("GoogleAdsService")


def run(query):
    rows = []
    for batch in svc.search_stream(customer_id=a.customer, query=query):
        for r in batch.results:
            rows.append(flatten(MessageToDict(r._pb, preserving_proto_field_name=True)))
    return rows


out = {"customer_id": a.customer, "desde": str(desde), "hasta": str(hasta), "errores": {}}
for name, q in QUERIES.items():
    try:
        out[name] = run(q)
    except Exception as e:  # una sección rota no tumba el perfil completo
        out[name] = []
        out["errores"][name] = str(e).splitlines()[0][:300]

# Nombres legibles de las ubicaciones segmentadas
geo_ids = sorted({r.get("campaign_criterion.location.geo_target_constant")
                  for r in out["geo"] if r.get("campaign_criterion.location.geo_target_constant")})
if geo_ids:
    try:
        lista = ", ".join(f"'{g}'" for g in geo_ids)
        nombres = {}
        for batch in svc.search_stream(customer_id=a.customer, query=f"""SELECT
                geo_target_constant.resource_name, geo_target_constant.canonical_name,
                geo_target_constant.target_type
                FROM geo_target_constant WHERE geo_target_constant.resource_name IN ({lista})"""):
            for r in batch.results:
                g = r.geo_target_constant
                nombres[g.resource_name] = f"{g.canonical_name} ({g.target_type})"
        for r in out["geo"]:
            gid = r.get("campaign_criterion.location.geo_target_constant")
            if gid:
                r["ubicacion"] = nombres.get(gid, gid)
    except Exception as e:
        out["errores"]["geo_nombres"] = str(e).splitlines()[0][:300]

json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
