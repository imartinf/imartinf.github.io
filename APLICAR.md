# Cómo aplicar esto al repo

Esta carpeta **es** el repo nuevo. Lo más limpio es vaciar `imartinf.github.io` de todo lo
viejo y copiar esto encima, respetando rutas.

MkDocs se va del todo. En su lugar hay un `build.py` de noventa líneas: lee `contenido/*.md`,
los mete en `tema/base.html` y escribe `site/`. Nada sobrescribe al sistema visual porque no
hay nada más.

## Se queda (contenido que se ha migrado)

    contenido/index.md        antes docs/index.md + docs/contact.md
    contenido/research.md     antes docs/pubs.md
    contenido/talks.md        antes docs/slides.md
    contenido/cv.md           nuevo
    estatico/assets/retrato.jpg   antes docs/assets/1690915534962.jpeg
    estatico/acb/index.html       la hoja de prompts del taller, intacta

## Se borra

    docs/                     entero
    mkdocs.yml
    main.py
    site/                     estaba commiteado pese al .gitignore
    .DS_Store
    .vscode/
    uv.lock                   se regenera

Para lo que estaba commiteado:

    git rm -r --cached site docs .vscode
    git rm --cached .DS_Store main.py mkdocs.yml uv.lock

## Comprobar

    uv sync
    uv run python build.py --serve      # http://localhost:8000

Sin uv: `pip install markdown pymdown-extensions pyyaml && python3 build.py --serve`.

## Publicar

`git push` a `main` y la acción de `.github/workflows/deploy.yml` lo hace.

**La primera vez**: Settings → Pages → *Source: GitHub Actions*. Después se puede borrar la
rama `gh-pages` que dejó mkdocs.

## Pendiente de ti

- `contenido/index.md` — año de defensa; confirmar «where I now teach».
- `contenido/research.md` — año de la tesis y enlace al PDF del tomo.
- `contenido/cv.md` — copiar el PDF bueno a `estatico/assets/cv-imf.pdf` y descomentar el botón.
