"""Utilidades para los informes HTML de PMM (estilo en knowledge/estilo-informes/).

  python scripts/informe_html.py new <destino-es.html> <destino-en.html>
      Copia la plantilla a las dos rutas (EN con lang="en") y ya con el logo insertado.
  python scripts/informe_html.py embed <archivo.html> [...]
      Reemplaza {{PMM_LOGO}} por el logo PMM en base64 (el artefacto no puede cargar archivos locales).
  python scripts/informe_html.py check <es.html> <en.html>
      Valida antes de publicar: logo, tokens de color, modo oscuro, pie PMM, enlace cruzado
      entre idiomas y que no queden {{MARCADORES}}.
"""
import base64, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STYLE = ROOT / 'knowledge/estilo-informes'
LOGO = STYLE / 'pmm-logo.webp'
TEMPLATE = STYLE / 'plantilla.html'


def logo_uri():
    return 'data:image/webp;base64,' + base64.b64encode(LOGO.read_bytes()).decode()


def embed(path):
    p = Path(path)
    s = p.read_text()
    if '{{PMM_LOGO}}' not in s:
        print(f'{p}: sin {{{{PMM_LOGO}}}} (¿ya insertado?)')
        return
    p.write_text(s.replace('{{PMM_LOGO}}', logo_uri()))
    print(f'{p}: logo insertado')


def new(es, en):
    t = TEMPLATE.read_text().replace('{{PMM_LOGO}}', logo_uri())
    for dest, lang in ((es, 'es'), (en, 'en')):
        d = Path(dest)
        if d.exists():
            sys.exit(f'{d} ya existe; no se sobrescribe')
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_text(t.replace('<html lang="es">', f'<html lang="{lang}">'))
        print(f'{d}: creado desde la plantilla')


def check(es, en):
    ok = True
    ref = TEMPLATE.read_text()
    ref_root = re.search(r':root\{.*?\}', ref, re.S).group(0)
    for path, other in ((es, en), (en, es)):
        s = Path(path).read_text()
        errs = []
        if 'data:image/webp;base64,' not in s or 'alt="Performance Media Marketing"' not in s:
            errs.append('falta el logo PMM embebido (correr embed)')
        if ref_root not in s:
            errs.append('los tokens de color de :root no coinciden con la plantilla')
        if 'prefers-color-scheme: dark' not in s or ':root[data-theme="dark"]' not in s:
            errs.append('falta el modo oscuro')
        if 'Red+Hat+Display' not in s:
            errs.append('faltan las tipografías (Red Hat Display / Source Sans 3 / JetBrains Mono)')
        if not re.search(r'<footer>.*Performance Media Marketing', s, re.S):
            errs.append('falta el pie "Performance Media Marketing"')
        left = sorted(set(re.findall(r'\{\{[^}]+\}\}', s)))
        if left:
            errs.append(f'marcadores sin reemplazar: {", ".join(left[:5])}' + (' …' if len(left) > 5 else ''))
        if not re.search(r'href="https://claude\.ai/(code/)?artifact/[^"]+"', s):
            errs.append(f'sin enlace a la otra versión ({Path(other).name}); poner su URL de artefacto')
        print(f'{path}: ' + ('OK' if not errs else 'ERRORES'))
        for e in errs:
            print('  -', e)
        ok &= not errs
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    cmd, args = (sys.argv[1], sys.argv[2:]) if len(sys.argv) > 1 else ('', [])
    if cmd == 'embed' and args:
        for a in args:
            embed(a)
    elif cmd == 'new' and len(args) == 2:
        new(*args)
    elif cmd == 'check' and len(args) == 2:
        check(*args)
    else:
        sys.exit(__doc__)
