# Setup: Google Ads API desde el MCC de PMM

Developer token ya aprobado (acceso básico o estándar). Falta solo credenciales OAuth y el archivo de config.

## 1. Credenciales OAuth (una vez)
1. Google Cloud Console → proyecto de PMM → APIs & Services → habilitar **Google Ads API**.
2. Credentials → Create → **OAuth client ID** → tipo *Desktop app*. Descargar `client_secret.json`.
3. OAuth consent screen: usuario de prueba = la cuenta Google que administra el MCC.

## 2. Refresh token
```bash
pip install google-ads --break-system-packages
python scripts/oauth_refresh_token.py --client-secrets client_secret.json
```
Abre el navegador, autoriza con la cuenta del MCC, imprime el refresh token.

## 3. Archivo `google-ads.yaml` (en la raíz del repo, en `.gitignore`)
```yaml
developer_token: "XXXXXXXX"
client_id: "....apps.googleusercontent.com"
client_secret: "...."
refresh_token: "1//...."
login_customer_id: "1234567890"   # ID del MCC de PMM sin guiones
use_proto_plus: true
```

## 4. Probar
```bash
python scripts/gaql.py --customer 1234567890 --query "SELECT customer.descriptive_name FROM customer"
python scripts/mcc_accounts.py            # lista todas las cuentas del MCC con etiquetas
```

## 5. Etiquetar cuentas para /benchmark-interno
En Google Ads → Cuentas → Etiquetas: crear `nicho:towing`, `nicho:plumbing`, `pais:US`, `pais:CO`, etc. y asignarlas. `mcc_accounts.py --nicho towing --pais US` filtra por ellas.

## Operaciones por skill
| Skill | Servicios de la API |
|---|---|
| benchmark-interno | GoogleAdsService.search (customer_client, campaign, ad_group, keyword_view, metrics) |
| strategy | KeywordPlanIdeaService.generate_keyword_ideas |
| build-campaign | CampaignBudgetService, CampaignService, AdGroupService, AdGroupCriterionService, AdGroupAdService, AssetService, CampaignAssetService, SharedSetService, CampaignCriterionService |
| weekly-review | search_term_view, campaign, ad_group_ad, metrics |
| negatives | SharedSetService, SharedCriterionService, CampaignSharedSetService, CampaignCriterionService |

## Cuotas
Acceso básico: 15.000 operaciones/día. Suficiente para 54 cuentas si los exports de métricas van por Windsor.ai y la API se usa para escritura y Keyword Planner.

## Seguridad
- `google-ads.yaml` y `client_secret.json` nunca al repo.
- Toda escritura primero con `validate_only=True`.
- Campañas nuevas siempre en PAUSA.
