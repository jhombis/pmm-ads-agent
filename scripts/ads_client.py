"""Cliente de Google Ads compartido: usa google-ads.yaml si existe; si no, variables de entorno.

Variables (útiles en entornos efímeros como Claude Code en la nube, donde el yaml se pierde):
  GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET,
  GOOGLE_ADS_REFRESH_TOKEN, GOOGLE_ADS_LOGIN_CUSTOMER_ID (MCC sin guiones), GOOGLE_ADS_USE_PROTO_PLUS=True
"""
import os, sys
from pathlib import Path

try:
    from google.ads.googleads.client import GoogleAdsClient
except ImportError:
    sys.exit("Falta google-ads: pip install google-ads --break-system-packages")

CONFIG = Path(__file__).resolve().parent.parent / "google-ads.yaml"


def get_client():
    if CONFIG.exists():
        return GoogleAdsClient.load_from_storage(str(CONFIG))
    if os.getenv("GOOGLE_ADS_REFRESH_TOKEN"):
        os.environ.setdefault("GOOGLE_ADS_USE_PROTO_PLUS", "True")
        return GoogleAdsClient.load_from_env()
    sys.exit("No hay google-ads.yaml ni variables GOOGLE_ADS_*. Ver docs/setup-google-ads-api.md")
