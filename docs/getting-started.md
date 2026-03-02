# Getting Started

## Voraussetzungen

- `uv`
- Python `3.12`

## Environment einrichten

```bash
uv sync --python 3.12 --group dev --group docs
```

Alternativ:

```bash
make sync
```

## Tests ausfuehren

```bash
uv run --python 3.12 pytest
```

Alternativ:

```bash
make test
```

## TTL-Dateien validieren

```bash
make ttl-check
```

## MkDocs lokal starten

```bash
uv run --group docs mkdocs serve
```

Alternativ:

```bash
make docs-serve
```

## Statischen Build erzeugen

```bash
uv run --group docs mkdocs build
```

Alternativ:

```bash
make docs-build
```
