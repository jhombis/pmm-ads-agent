#!/usr/bin/env python3
"""Resume llamadas de call tracking (CallFire o CallRail) exportadas por los conectores MCP.

Uso:
  python scripts/call_summary.py clients/<slug>/data/calls-callfire-2026-10-08.json --tz America/New_York
  python scripts/call_summary.py data.json --min 60 --gasto 412.50 --ads-conv 9

Entrada: el JSON tal cual lo devuelve el conector (o una lista de esas respuestas):
  - CallFire  callfire_list_calls → {"items": [...]}     (llamadas entrantes al número de tracking)
  - CallRail  callrail_list_calls → {"calls": [...]}

Salida (JSON en stdout y tabla legible en stderr):
  llamadas, llamantes únicos, contestadas, abandonadas/perdidas, calificadas (≥ --min s de
  conversación, una por llamante), repetidas, duración mediana, distribución por día y hora
  (zona del cliente), fuente (solo CallRail) y, si se pasan --gasto/--ads-conv, costo por llamada
  calificada y comparación con las conversiones que reporta Google Ads.
"""
import argparse, json, statistics, sys
from collections import Counter
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

DIAS = ['lun', 'mar', 'mié', 'jue', 'vie', 'sáb', 'dom']


def load(path):
    data = json.load(open(path))
    chunks = data if isinstance(data, list) else [data]
    calls, kind = [], None
    for c in chunks:
        if 'items' in c:
            kind = 'callfire'; calls += c['items']
        elif 'calls' in c:
            kind = 'callrail'; calls += c['calls']
    if not kind:
        sys.exit('No reconozco el formato: se espera {"items": [...]} (CallFire) o {"calls": [...]} (CallRail)')
    return kind, calls


def norm_callfire(c):
    recs = c.get('records') or []
    # XFER_LEG = tramo con el negocio (tiempo real de conversación); XFER = tramo del llamante
    legs = [r.get('duration') or 0 for r in recs if r.get('result') == 'XFER_LEG']
    talk = max(legs) if legs else 0
    result = next((r.get('result') for r in recs if r.get('result') != 'XFER_LEG'), c.get('state'))
    return {
        'ts': datetime.fromtimestamp(c['created'] / 1000, timezone.utc),
        'caller': c.get('fromNumber') or 'Unavailable',
        'answered': talk > 0,
        'talk': talk,
        'result': result,
        'source': None,
        'recording': any(r.get('recordings') for r in recs),
    }


def norm_callrail(c):
    return {
        'ts': datetime.fromisoformat(c['start_time'].replace('Z', '+00:00')),
        'caller': c.get('customer_phone_number') or 'Unavailable',
        'answered': bool(c.get('answered')),
        'talk': c.get('duration') or 0 if c.get('answered') else 0,
        'result': 'voicemail' if c.get('voicemail') else ('answered' if c.get('answered') else 'missed'),
        'source': c.get('source_name') or c.get('source'),
        'recording': bool(c.get('recording')),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('json')
    ap.add_argument('--tz', default='America/New_York', help='Zona horaria del cliente')
    ap.add_argument('--min', type=int, default=60, help='Segundos de conversación para contar como calificada')
    ap.add_argument('--gasto', type=float, help='Gasto de Google Ads del mismo periodo')
    ap.add_argument('--ads-conv', type=float, help='Conversiones de llamada que reporta Google Ads en el periodo')
    a = ap.parse_args()

    kind, raw = load(a.json)
    tz = ZoneInfo(a.tz)
    calls = sorted((norm_callfire(c) if kind == 'callfire' else norm_callrail(c) for c in raw), key=lambda x: x['ts'])
    if not calls:
        print(json.dumps({'fuente': kind, 'llamadas': 0}))
        return

    # Calificada = llamante con al menos una llamada contestada de ≥ --min s (se cuenta una vez).
    # Los números ocultos ("Unavailable") no se pueden deduplicar: cada llamada calificada cuenta.
    known = [c for c in calls if c['caller'] != 'Unavailable']
    qual_callers = {c['caller'] for c in known if c['answered'] and c['talk'] >= a.min}
    qual_hidden = sum(1 for c in calls if c['caller'] == 'Unavailable' and c['answered'] and c['talk'] >= a.min)
    qualified = len(qual_callers) + qual_hidden
    repeats = len(known) - len({c['caller'] for c in known})

    answered = [c for c in calls if c['answered']]
    local = [c['ts'].astimezone(tz) for c in calls]
    out = {
        'fuente': kind,
        'desde': local[0].strftime('%Y-%m-%d'),
        'hasta': local[-1].strftime('%Y-%m-%d'),
        'llamadas': len(calls),
        'llamantes_unicos': len({c['caller'] for c in calls}),
        'contestadas': len(answered),
        'no_contestadas': len(calls) - len(answered),
        'tasa_contestadas': round(len(answered) / len(calls), 3),
        'calificadas_unicas': qualified,
        'umbral_s': a.min,
        'repetidas': repeats,
        'duracion_mediana_s': round(statistics.median([c['talk'] for c in answered])) if answered else 0,
        'cortas_menos_30s': sum(1 for c in answered if c['talk'] < 30),
        'resultados': dict(Counter(c['result'] for c in calls)),
        'por_dia': {DIAS[d]: n for d, n in sorted(Counter(t.weekday() for t in local).items())},
        'por_hora': {f'{h:02d}': n for h, n in sorted(Counter(t.hour for t in local).items())},
        'fuera_de_horario_8_18': sum(1 for t in local if t.hour < 8 or t.hour >= 18),
        'con_grabacion': sum(1 for c in calls if c['recording']),
    }
    if kind == 'callrail':
        out['por_fuente'] = dict(Counter(c['source'] or 'sin fuente' for c in calls))
    if a.gasto is not None:
        out['gasto'] = a.gasto
        out['costo_por_llamada_calificada'] = round(a.gasto / qualified, 2) if qualified else None
    if a.ads_conv is not None:
        out['conv_google_ads'] = a.ads_conv
        out['diferencia_vs_ads'] = round(a.ads_conv - qualified, 1)

    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    print(file=sys.stderr)
    print(f"{kind} · {out['desde']} → {out['hasta']} · {out['llamadas']} llamadas, {out['llamantes_unicos']} llamantes, "
          f"{out['contestadas']} contestadas ({out['tasa_contestadas']:.0%}), {qualified} calificadas ≥{a.min}s, "
          f"{repeats} repetidas, mediana {out['duracion_mediana_s']}s", file=sys.stderr)


if __name__ == '__main__':
    main()
