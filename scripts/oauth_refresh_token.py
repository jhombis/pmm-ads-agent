#!/usr/bin/env python3
"""Genera el refresh token de OAuth para la Google Ads API (cliente OAuth tipo "Desktop app").

Funciona en dos pasos para poder correrlo en un entorno remoto sin navegador:

  1) Imprimir la URL de autorización:
     python scripts/oauth_refresh_token.py --client-secrets client_secret.json url

  2) Abrir la URL en tu navegador, autorizar con la cuenta Google que administra el MCC.
     El navegador termina en http://localhost:8080/?code=...  (la página no carga: es normal).
     Copiar la URL completa de la barra de direcciones y canjearla:
     python scripts/oauth_refresh_token.py --client-secrets client_secret.json code "http://localhost:8080/?state=...&code=...&scope=..."

     Con --write-yaml también escribe google-ads.yaml (en .gitignore, permisos 600) usando
     GOOGLE_ADS_DEVELOPER_TOKEN y GOOGLE_ADS_LOGIN_CUSTOMER_ID del entorno o --developer-token / --login-customer-id.

En lugar de --client-secrets se pueden usar las variables GOOGLE_ADS_CLIENT_ID y GOOGLE_ADS_CLIENT_SECRET.
"""
import argparse, json, os, sys, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCOPE = "https://www.googleapis.com/auth/adwords"
REDIRECT = "http://localhost:8080"
AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"


def client_creds(path):
    if path:
        d = json.loads(Path(path).read_text())
        d = d.get("installed") or d.get("web") or d
        return d["client_id"], d["client_secret"]
    cid, sec = os.getenv("GOOGLE_ADS_CLIENT_ID"), os.getenv("GOOGLE_ADS_CLIENT_SECRET")
    if not (cid and sec):
        sys.exit("Falta --client-secrets o GOOGLE_ADS_CLIENT_ID / GOOGLE_ADS_CLIENT_SECRET")
    return cid, sec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--client-secrets")
    ap.add_argument("--developer-token", default=os.getenv("GOOGLE_ADS_DEVELOPER_TOKEN"))
    ap.add_argument("--login-customer-id", default=os.getenv("GOOGLE_ADS_LOGIN_CUSTOMER_ID"))
    ap.add_argument("--write-yaml", action="store_true")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("url")
    c = sub.add_parser("code")
    c.add_argument("redirect", help="URL completa de localhost:8080 o solo el valor de code=")
    a = ap.parse_args()
    cid, sec = client_creds(a.client_secrets)

    if a.cmd == "url":
        q = {"client_id": cid, "redirect_uri": REDIRECT, "response_type": "code", "scope": SCOPE,
             "access_type": "offline", "prompt": "consent", "state": "pmm-ads"}
        print(AUTH_URL + "?" + urllib.parse.urlencode(q))
        return

    code = a.redirect
    if code.startswith("http"):
        qs = urllib.parse.parse_qs(urllib.parse.urlparse(code).query)
        if "error" in qs:
            sys.exit(f"Google devolvió error: {qs['error'][0]}")
        code = qs["code"][0]
    body = urllib.parse.urlencode({"code": code, "client_id": cid, "client_secret": sec,
                                   "redirect_uri": REDIRECT, "grant_type": "authorization_code"}).encode()
    try:
        tok = json.load(urllib.request.urlopen(urllib.request.Request(TOKEN_URL, data=body), timeout=30))
    except urllib.error.HTTPError as e:
        sys.exit(f"Error al canjear el código ({e.code}): {e.read().decode()}")
    rt = tok.get("refresh_token")
    if not rt:
        sys.exit("Google no devolvió refresh_token (¿el código ya se usó? Repite el paso 1).")

    if a.write_yaml:
        if not (a.developer_token and a.login_customer_id):
            sys.exit("Para --write-yaml falta el developer token y el login customer id (MCC).")
        path = ROOT / "google-ads.yaml"
        path.write_text(
            f'developer_token: "{a.developer_token}"\n'
            f'client_id: "{cid}"\n'
            f'client_secret: "{sec}"\n'
            f'refresh_token: "{rt}"\n'
            f'login_customer_id: "{a.login_customer_id.replace("-", "")}"\n'
            "use_proto_plus: true\n")
        path.chmod(0o600)
        print(f"Escrito {path} (no se sube al repo: está en .gitignore).")
    else:
        print("refresh_token:", rt)


if __name__ == "__main__":
    main()
