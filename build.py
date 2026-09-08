#!/usr/bin/env python3
"""
Generador del sitio de Iván Martín-Fernández.

No hay framework: unas noventa líneas que convierten `contenido/*.md` en HTML con
la plantilla de `tema/`. Se ejecuta con

    python3 build.py          # escribe site/
    python3 build.py --serve  # además, lo sirve en http://localhost:8000

Convenciones del markdown (todas opcionales):

    ---                       front matter
    titulo: Research          el <h1>
    antetitulo: publicaciones el rótulo en mono sobre el título
    entradilla: una línea     el párrafo grande bajo el título
    nav: Research             cómo aparece en la navegación
    orden: 2                  posición en la navegación
    ---

    ## Sección            → rótulo pequeño en mayúsculas, con filete y número
    Párrafo { .lede }     → párrafo de entrada de sección
    ??? note "Título"     → desplegable

    ::: tarjetas          → rejilla de tarjetas (una por elemento de la lista)
    - **Título** texto
    :::

    ::: idea              → bloque de savia
    La frase que importa.
    :::
"""

import argparse
import pathlib
import re
import shutil

import markdown
import yaml

RAIZ = pathlib.Path(__file__).parent
CONTENIDO = RAIZ / "contenido"
TEMA = RAIZ / "tema"
ESTATICO = RAIZ / "estatico"
SALIDA = RAIZ / "site"

EXTENSIONES = [
    "attr_list", "tables", "footnotes", "md_in_html", "sane_lists",
    "pymdownx.details", "pymdownx.superfences", "pymdownx.highlight",
    "pymdownx.smartsymbols",
]


def leer(ruta):
    """Separa el front matter YAML del cuerpo markdown."""
    texto = ruta.read_text(encoding="utf-8")
    meta = {}
    if texto.startswith("---"):
        _, bruto, texto = texto.split("---", 2)
        meta = yaml.safe_load(bruto) or {}
    return meta, texto.lstrip("\n")


def bloques(texto):
    """::: nombre ... :::  →  <div class="nombre" markdown="1"> ... </div>"""
    def envolver(m):
        return f'<div class="{m.group(1)}" markdown="1">\n\n{m.group(2).strip()}\n\n</div>'
    return re.sub(r"(?ms)^::: +(\w[\w -]*)\n(.*?)^:::\s*$", envolver, texto)


def seccionar(html):
    """Envuelve cada <h2> y lo que le sigue en <section>, y lo numera."""
    trozos = re.split(r"(?=<h2)", html)
    salida, n = [], 0
    for i, trozo in enumerate(trozos):
        if not trozo.strip():
            continue
        if trozo.startswith("<h2"):
            n += 1
            trozo = re.sub(
                r"<h2([^>]*)>(.*?)</h2>",
                lambda m: f'<h2{m.group(1)}><span>{m.group(2)}</span>'
                          f'<span class="n">{n:02d}</span></h2>',
                trozo, count=1, flags=re.S,
            )
            salida.append(f"<section>{trozo}</section>")
        else:
            salida.append(f"<section class=\"intro\">{trozo}</section>" if i == 0 else trozo)
    return "\n".join(salida)


def main(serve=False):
    plantilla = (TEMA / "base.html").read_text(encoding="utf-8")
    md = markdown.Markdown(extensions=EXTENSIONES)

    paginas = []
    for ruta in sorted(CONTENIDO.glob("*.md")):
        meta, cuerpo = leer(ruta)
        md.reset()
        cuerpo = bloques(cuerpo)
        paginas.append({
            "slug": "" if ruta.stem == "index" else ruta.stem,
            "meta": meta,
            "html": seccionar(md.convert(cuerpo)),
            "orden": meta.get("orden", 99),
            "nav": meta.get("nav", meta.get("titulo", ruta.stem)),
        })
    paginas.sort(key=lambda p: p["orden"])

    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    SALIDA.mkdir()
    shutil.copytree(ESTATICO, SALIDA, dirs_exist_ok=True)
    shutil.copy(TEMA / "estilos.css", SALIDA / "estilos.css")

    for pag in paginas:
        raiz = "" if pag["slug"] == "" else "../"
        nav = "".join(
            '<a href="{}{}"{}>{}</a>'.format(
                raiz, (p["slug"] + "/") if p["slug"] else "",
                ' class="on" aria-current="page"' if p is pag else "",
                p["nav"])
            for p in paginas
        )
        m = pag["meta"]
        cabecera = ""
        if m.get("antetitulo"):
            cabecera += f'<p class="antetitulo">{m["antetitulo"]}</p>'
        if m.get("titulo"):
            cabecera += f'<h1>{m["titulo"]}</h1>'
        if m.get("entradilla"):
            cabecera += f'<p class="entradilla">{m["entradilla"]}</p>'

        pagina = (plantilla
                  .replace("{{titulo}}", m.get("titulo", "Iván Martín-Fernández"))
                  .replace("{{descripcion}}", m.get("descripcion", ""))
                  .replace("{{raiz}}", raiz)
                  .replace("{{nav}}", nav)
                  .replace("{{cabecera}}", cabecera)
                  .replace("{{contenido}}", pag["html"]))

        destino = SALIDA if pag["slug"] == "" else SALIDA / pag["slug"]
        destino.mkdir(parents=True, exist_ok=True)
        (destino / "index.html").write_text(pagina, encoding="utf-8")
        print(f"  {destino.relative_to(RAIZ)}/index.html")

    print(f"\n{len(paginas)} páginas en site/")

    if serve:
        import http.server, socketserver, os
        os.chdir(SALIDA)
        with socketserver.TCPServer(("", 8000), http.server.SimpleHTTPRequestHandler) as s:
            print("http://localhost:8000  (ctrl-c para parar)")
            s.serve_forever()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--serve", action="store_true", help="servir en localhost:8000")
    main(**vars(ap.parse_args()))
