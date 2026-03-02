# Getting Started

## Voraussetzungen

- `uv`
- Python `3.12`

## Environment einrichten

```bash
uv sync --python 3.12 --group dev --group docs
```

## Tests ausfuehren

```bash
uv run --python 3.12 pytest
```

## MkDocs lokal starten

```bash
uv run --group docs mkdocs serve
```

## Statischen Build erzeugen

```bash
uv run --group docs mkdocs build
```
