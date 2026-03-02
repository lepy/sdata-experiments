# sdata-testdata

Monorepo fuer modulare SData-Ontologien zu mechanischen Pruefdaten.

## Quickstart

```bash
make sync
make test
make ttl-check
make docs-build
```

Oder mit `uv` direkt:

```bash
uv sync --python 3.12 --group dev --group docs
uv run --python 3.12 pytest
uv run --python 3.12 python scripts/check_ttl.py
uv run --group docs mkdocs build --strict
```

## Projektstruktur

```text
sdata-testdata/
├── README.md
├── LICENSE
├── pyproject.toml
├── .python-version
├── Makefile
├── mkdocs.yml
├── .github/workflows/deploy-docs.yml
├── scripts/
│   └── check_ttl.py
├── core/
│   ├── sdata-testdata.ttl
│   └── CHANGELOG.md
├── tensiletest/
│   ├── sdata-tensile.ttl
│   ├── examples/
│   └── CHANGELOG.md
├── compressiontest/
│   ├── sdata-compression.ttl
│   └── CHANGELOG.md
├── bendingtest/
│   ├── sdata-bending.ttl
│   ├── examples/
│   └── CHANGELOG.md
├── fatiguetest/
│   ├── sdata-fatigue.ttl
│   └── CHANGELOG.md
├── shapes/
│   ├── sdata-shapes.ttl
│   ├── sdata-core-shapes.ttl
│   ├── sdata-tensile-shapes.ttl
│   ├── sdata-compression-shapes.ttl
│   ├── sdata-bending-shapes.ttl
│   ├── sdata-fatigue-shapes.ttl
│   └── CHANGELOG.md
├── vocabularies/
│   ├── iso6892-1-skos.ttl
│   ├── specimen-shapes.ttl
│   ├── material-models.ttl
│   ├── test-standards.ttl
│   └── CHANGELOG.md
├── docs/
│   ├── index.md
│   ├── getting-started.md
│   ├── architecture.md
│   ├── validation.md
│   └── modules/
└── tests/
    └── test_smoke.py
```

## Namespaces

- `core/sdata-testdata.ttl` -> `https://w3id.org/sdata/testdata/`
- `tensiletest/sdata-tensile.ttl` -> `https://w3id.org/sdata/tensile/`
- `compressiontest/sdata-compression.ttl` -> `https://w3id.org/sdata/compression/`
- `bendingtest/sdata-bending.ttl` -> `https://w3id.org/sdata/bending/`
- `fatiguetest/sdata-fatigue.ttl` -> `https://w3id.org/sdata/fatigue/`
- `shapes/sdata-core-shapes.ttl` -> `https://w3id.org/sdata/shapes/core/`
- `shapes/sdata-tensile-shapes.ttl` -> `https://w3id.org/sdata/shapes/tensile/`
- `shapes/sdata-compression-shapes.ttl` -> `https://w3id.org/sdata/shapes/compression/`
- `shapes/sdata-bending-shapes.ttl` -> `https://w3id.org/sdata/shapes/bending/`
- `shapes/sdata-fatigue-shapes.ttl` -> `https://w3id.org/sdata/shapes/fatigue/`
- `shapes/sdata-shapes.ttl` -> `https://w3id.org/sdata/shapes/`

## Import-Kette

```text
MIN -> sdata-core -> sdata-testdata -> sdata-tensile
                                  -> sdata-compression
                                  -> sdata-bending
                                  -> sdata-fatigue
```

Hinweis: `sdata-core` ist extern und wird in `core/sdata-testdata.ttl` als Import referenziert.

## Modellprinzip

`core/sdata-testdata.ttl` ist die gemeinsame Zwischenschicht fuer versuchsartuebergreifende Inhalte:

- Prozess: `TestProgram -> TestSeries -> MechanicalTest`
- Ressourcen: `Specimen`, `Material`, `TestingMachine`, `Operator`, `Laboratory`
- Kontextdaten: IDs, Zeitstempel, Methode, Standard, Bedingungen
- Messdaten: `MeasurementSeries`, `MeasurementChannel`
- Ergebnisanker: `TestResult`

Die Testmodule (`tensiletest`, `compressiontest`, `bendingtest`, `fatiguetest`) erweitern darauf fachspezifisch.

## Tensile / ISO 6892-1

`tensiletest/sdata-tensile.ttl` ist auf notation-nahe ISO-Kennwerte ausgerichtet (`Rm`, `ReH`, `ReL`, `Rp`, `Rt`, `Rr`, `A`, `Ae`, `Ag`, `Agt`, `At`, `E`, `Z`, `Su`, `Fm`) und mit `iso6892-1-skos.ttl` verknuepft.

## SHACL

- `shapes/sdata-core-shapes.ttl`: Basiskonsistenz (IDs, Kardinalitaeten, Datentypen)
- `shapes/sdata-*-shapes.ttl`: testtypspezifische KPI-Regeln
- `shapes/sdata-shapes.ttl`: Sammelgraph fuer alle Shape-Module

TTL-Validation mit Parser:

```bash
make ttl-check
```

## Python-Setup

- Python: `==3.12.*`
- Runtime-Dependency: `rdflib`
- Dev: `pytest`
- Docs: `mkdocs`

## Makefile Targets

```bash
make help
```

Wichtige Targets:

- `make venv` - `.venv` mit Python 3.12 erzeugen
- `make sync` - Runtime + dev + docs installieren
- `make test` - `pytest` ausfuehren
- `make ttl-check` - alle `.ttl` mit `rdflib` parsen
- `make docs-serve` - MkDocs lokal starten
- `make docs-build` - statische Doku bauen
- `make check` - `test + ttl-check + docs-build`

## MkDocs + Deployment

- Lokale Doku: `mkdocs.yml` + `docs/`
- GitHub Action: `.github/workflows/deploy-docs.yml`
- Deploy-Ziel: `gh-pages` Branch

Voraussetzung im Repo: GitHub Pages auf `gh-pages` aktivieren.
