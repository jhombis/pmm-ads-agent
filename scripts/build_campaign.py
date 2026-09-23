#!/usr/bin/env python3
"""Crea una campaña Search completa desde un build-spec.json en UN lote atómico (GoogleAdsService.Mutate).

Uso:
  python scripts/build_campaign.py clients/<slug>/data/build-spec.json            # validate_only (por defecto)
  python scripts/build_campaign.py clients/<slug>/data/build-spec.json --execute  # crea de verdad

Crea: listas compartidas de negativas (y las vincula), presupuesto, campaña (solo red de Búsqueda,
presencia, idioma, programación en la zona horaria de la cuenta, puja), ad groups, keywords,
negativas de enrutamiento, 1 RSA por grupo con H1 pinneado, sitelinks, callouts, snippet y extensión
de llamada existente. Con --execute y `pause_campaign_after_enable` en el spec, pausa esa campaña
después de crear la nueva.
"""
import json, sys
from ads_client import get_client

spec = json.load(open(sys.argv[1]))
EXECUTE = '--execute' in sys.argv
client = get_client()
CID = spec['customer_id']
E = client.enums
ops = []
_tmp = [0]


def tmp():
    _tmp[0] -= 1
    return _tmp[0]


def mop(kind):
    o = client.get_type('MutateOperation')
    ops.append(o)
    return getattr(o, kind)


MT = {'EXACT': E.KeywordMatchTypeEnum.EXACT, 'PHRASE': E.KeywordMatchTypeEnum.PHRASE, 'BROAD': E.KeywordMatchTypeEnum.BROAD}
c = spec['campaign']

# Presupuesto
budget_rn = f'customers/{CID}/campaignBudgets/{tmp()}'
b = mop('campaign_budget_operation').create
b.resource_name = budget_rn
b.name = c['name'] + ' budget'
b.amount_micros = int(c['daily_budget_usd'] * 1_000_000)
b.delivery_method = E.BudgetDeliveryMethodEnum.STANDARD
b.explicitly_shared = False

# Campaña
camp_rn = f'customers/{CID}/campaigns/{tmp()}'
k = mop('campaign_operation').create
k.resource_name = camp_rn
k.name = c['name']
k.status = E.CampaignStatusEnum[c['status']]
k.advertising_channel_type = E.AdvertisingChannelTypeEnum.SEARCH
k.campaign_budget = budget_rn
k.network_settings.target_google_search = True
k.network_settings.target_search_network = False
k.network_settings.target_content_network = False
k.network_settings.target_partner_search_network = False
k.geo_target_type_setting.positive_geo_target_type = E.PositiveGeoTargetTypeEnum.PRESENCE
k.geo_target_type_setting.negative_geo_target_type = E.NegativeGeoTargetTypeEnum.PRESENCE
k.contains_eu_political_advertising = E.EuPoliticalAdvertisingStatusEnum.DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING
bid = c['bidding']
if bid['type'] == 'TARGET_SPEND':
    k.target_spend.cpc_bid_ceiling_micros = int(bid['cpc_bid_ceiling_usd'] * 1_000_000)
elif bid['type'] == 'MAXIMIZE_CONVERSIONS':
    k.maximize_conversions.target_cpa_micros = 0

# Criterios de campaña: geo (presencia), idioma, programación
for gid in c['geo_presence']:
    cc = mop('campaign_criterion_operation').create
    cc.campaign = camp_rn
    cc.location.geo_target_constant = f'geoTargetConstants/{gid}'
cc = mop('campaign_criterion_operation').create
cc.campaign = camp_rn
cc.language.language_constant = f'languageConstants/{c["language"]}'
sch = c['schedule_account_tz']
days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'] if sch['days'] == 'ALL' else sch['days']
for d in days:
    cc = mop('campaign_criterion_operation').create
    cc.campaign = camp_rn
    cc.ad_schedule.day_of_week = E.DayOfWeekEnum[d]
    cc.ad_schedule.start_hour = sch['start_hour']
    cc.ad_schedule.start_minute = E.MinuteOfHourEnum.ZERO
    cc.ad_schedule.end_hour = sch['end_hour']
    cc.ad_schedule.end_minute = E.MinuteOfHourEnum.ZERO

# Listas compartidas de negativas
for name, items in spec['shared_negative_lists'].items():
    ss_rn = f'customers/{CID}/sharedSets/{tmp()}'
    ss = mop('shared_set_operation').create
    ss.resource_name = ss_rn
    ss.name = name
    ss.type_ = E.SharedSetTypeEnum.NEGATIVE_KEYWORDS
    for text, m in items:
        sc = mop('shared_criterion_operation').create
        sc.shared_set = ss_rn
        sc.keyword.text = text
        sc.keyword.match_type = MT[m]
    link = mop('campaign_shared_set_operation').create
    link.campaign = camp_rn
    link.shared_set = ss_rn

# Ad groups, keywords, negativas de enrutamiento, RSA
for ag in spec['ad_groups']:
    ag_rn = f'customers/{CID}/adGroups/{tmp()}'
    a = mop('ad_group_operation').create
    a.resource_name = ag_rn
    a.name = ag['name']
    a.campaign = camp_rn
    a.status = E.AdGroupStatusEnum[ag['status']]
    a.type_ = E.AdGroupTypeEnum.SEARCH_STANDARD
    a.ad_rotation_mode = E.AdGroupAdRotationModeEnum.OPTIMIZE  # rotación: optimizar (a nivel ad group)
    seen = set()
    for text, m in ag['keywords']:
        if (text, m) in seen:
            continue
        seen.add((text, m))
        kw = mop('ad_group_criterion_operation').create
        kw.ad_group = ag_rn
        kw.status = E.AdGroupCriterionStatusEnum.ENABLED
        kw.keyword.text = text
        kw.keyword.match_type = MT[m]
    for text in ag.get('negatives_phrase', []):
        n = mop('ad_group_criterion_operation').create
        n.ad_group = ag_rn
        n.negative = True
        n.keyword.text = text
        n.keyword.match_type = MT['PHRASE']
    r = ag['rsa']
    ad = mop('ad_group_ad_operation').create
    ad.ad_group = ag_rn
    ad.status = E.AdGroupAdStatusEnum.ENABLED
    ad.ad.final_urls.append(r['final_url'])
    rsa = ad.ad.responsive_search_ad
    rsa.path1 = r.get('path1', '')
    rsa.path2 = r.get('path2', '')
    for h in r['headlines']:
        t = client.get_type('AdTextAsset')
        t.text = h['text']
        if h.get('pin'):
            t.pinned_field = E.ServedAssetFieldTypeEnum[h['pin']]
        rsa.headlines.append(t)
    for d in r['descriptions']:
        t = client.get_type('AdTextAsset')
        t.text = d
        rsa.descriptions.append(t)

# Assets de campaña
A = spec['assets']
for link_text, url, d1, d2 in A['sitelinks']:
    a_rn = f'customers/{CID}/assets/{tmp()}'
    s = mop('asset_operation').create
    s.resource_name = a_rn
    s.sitelink_asset.link_text = link_text
    s.sitelink_asset.description1 = d1
    s.sitelink_asset.description2 = d2
    s.final_urls.append(url)
    l = mop('campaign_asset_operation').create
    l.campaign = camp_rn
    l.asset = a_rn
    l.field_type = E.AssetFieldTypeEnum.SITELINK
for text in A['callouts']:
    a_rn = f'customers/{CID}/assets/{tmp()}'
    s = mop('asset_operation').create
    s.resource_name = a_rn
    s.callout_asset.callout_text = text
    l = mop('campaign_asset_operation').create
    l.campaign = camp_rn
    l.asset = a_rn
    l.field_type = E.AssetFieldTypeEnum.CALLOUT
if A.get('structured_snippet'):
    a_rn = f'customers/{CID}/assets/{tmp()}'
    s = mop('asset_operation').create
    s.resource_name = a_rn
    s.structured_snippet_asset.header = A['structured_snippet']['header']
    s.structured_snippet_asset.values.extend(A['structured_snippet']['values'])
    l = mop('campaign_asset_operation').create
    l.campaign = camp_rn
    l.asset = a_rn
    l.field_type = E.AssetFieldTypeEnum.STRUCTURED_SNIPPET
if A.get('reuse_call_asset_id'):
    l = mop('campaign_asset_operation').create
    l.campaign = camp_rn
    l.asset = f'customers/{CID}/assets/{A["reuse_call_asset_id"]}'
    l.field_type = E.AssetFieldTypeEnum.CALL

print(f'Plan: 1 presupuesto, 1 campaña ({c["status"]}), {len(spec["ad_groups"])} ad groups, '
      f'{sum(len(set(map(tuple, a["keywords"]))) for a in spec["ad_groups"])} keywords, '
      f'{len(spec["ad_groups"])} RSA, {len(spec["shared_negative_lists"])} listas de negativas '
      f'({sum(len(v) for v in spec["shared_negative_lists"].values())} términos) → {len(ops)} operaciones')

gas = client.get_service('GoogleAdsService')
from google.ads.googleads.errors import GoogleAdsException
try:
  resp = gas.mutate(request={'customer_id': CID, 'mutate_operations': ops, 'validate_only': not EXECUTE})
except GoogleAdsException as ex:
    from collections import Counter
    msgs = Counter()
    for e in ex.failure.errors:
        idx = [f.index for f in e.location.field_path_elements if f.field_name == 'mutate_operations']
        kind = ops[idx[0]]._pb.WhichOneof('operation') if idx else '?'
        msgs[(kind, str(e.error_code).strip(), e.message)] += 1
        pf = e.details.policy_finding_details
        for entry in pf.policy_topic_entries:
            ev = [t for x in entry.evidences for t in x.text_list.texts]
            msgs[(kind, 'policy_topic', f'{entry.topic} {entry.type_.name} evidence={ev}')] += 1
    for (kind, code, msg), n in msgs.most_common():
        print(f'{n}x [{kind}] {code} :: {msg}')
    sys.exit(1)
if not EXECUTE:
    print('validate_only: OK')
    sys.exit(0)
camp_created = next(r.campaign_result.resource_name for r in resp.mutate_operation_responses
                    if r.campaign_result.resource_name)
print('campaña creada:', camp_created)

old = spec.get('pause_campaign_after_enable')
if old and c['status'] == 'ENABLED':
    op = client.get_type('CampaignOperation')
    op.update.resource_name = client.get_service('CampaignService').campaign_path(CID, old)
    op.update.status = E.CampaignStatusEnum.PAUSED
    op.update_mask.paths.append('status')
    client.get_service('CampaignService').mutate_campaigns(customer_id=CID, operations=[op])
    print('campaña anterior pausada:', old)
