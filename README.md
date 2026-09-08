# imartinf.github.io

Sitio personal de Iván Martín-Fernández. Sin framework: un generador de noventa
líneas (`build.py`) que convierte markdown en HTML con el sistema visual IMF.

## Trabajar en local

```bash
uv sync
uv run python build.py --serve      # http://localhost:8000
```

O sin uv: `pip install markdown pymdown-extensions pyyaml && python3 build.py --serve`.

## Publicar

`git push` a `main`. La acción de `.github/workflows/deploy.yml` construye y publica.

> La primera vez hay que ir a **Settings → Pages** del repo y poner *Source: GitHub Actions*.
> La rama `gh-pages` que quedó de mkdocs se puede borrar después.

## Estructura

```
contenido/       las páginas, en markdown. Añadir un .md = añadir una página.
tema/base.html   la plantilla. Cinco marcadores: {{titulo}}, {{nav}}, {{cabecera}}…
tema/estilos.css el sistema visual entero. Nada lo sobrescribe.
estatico/        se copia tal cual a la raíz del sitio (imágenes, la hoja de la ACB)
build.py         el generador
```

## Cómo se escribe una página

```markdown
---
titulo: Research                 el <h1>
antetitulo: Publicaciones        el rótulo en mono sobre el título
entradilla: Una línea de qué es  el párrafo grande de debajo
nav: Research                    cómo aparece en la navegación
orden: 2                         posición en la navegación
---

## Una sección
```

Las secciones se numeran solas (`01`, `02`…): el número lo pone `build.py`, no se escribe.

Bloques disponibles:

```markdown
::: idea
La frase que quieres destacar.
:::

::: tarjetas
- **Título** texto de la tarjeta
- **Otro** otra tarjeta
:::

??? note "Abstract"
    Texto plegado.
```

Y clases sueltas: `{ .lede }` en un párrafo de entrada, `{ .boton }` o
`{ .boton .primario }` en un enlace, `class="retrato"` en una imagen.

El párrafo que va justo detrás de un `###` se compone solo como ficha —autores, venue y
DOI— sin tener que marcarlo.

## El sistema visual

Colores y tipografía salen de `identidad-imf/tokens.json`. Si cambias un token allí,
actualiza `tema/estilos.css`.
