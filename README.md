# sdata-testdata

Monorepo fuer modulare SData-Testontologien mit getrennten Namespaces und eigenstaendigen Versionszyklen pro Modul.

## Struktur

```text
sdata-testdata/
├── README.md
├── LICENSE
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
│   ├── sdata-tensile-shapes.ttl
│   ├── sdata-bending-shapes.ttl
│   └── CHANGELOG.md
└── vocabularies/
    ├── iso6892-1-skos.ttl
    ├── specimen-shapes.ttl
    ├── material-models.ttl
    ├── test-standards.ttl
    └── CHANGELOG.md
```

## Namespace-Strategie

- `core/sdata-testdata.ttl` -> `https://w3id.org/sdata/testdata/`
- `tensiletest/sdata-tensile.ttl` -> `https://w3id.org/sdata/tensile/`
- `compressiontest/sdata-compression.ttl` -> `https://w3id.org/sdata/compression/`
- `bendingtest/sdata-bending.ttl` -> `https://w3id.org/sdata/bending/`
- `fatiguetest/sdata-fatigue.ttl` -> `https://w3id.org/sdata/fatigue/`
- `shapes/sdata-tensile-shapes.ttl` -> `https://w3id.org/sdata/shapes/tensile/`
- `shapes/sdata-bending-shapes.ttl` -> `https://w3id.org/sdata/shapes/bending/`

## Import-Kette

```text
MIN -> sdata-core -> sdata-testdata -> sdata-tensile
                                  -> sdata-compression
                                  -> sdata-bending
                                  -> sdata-fatigue
```

Hinweis: `sdata-core` ist als externe Basisschicht modelliert und wird hier nur als Import referenziert.

## Modulprinzip

`sdata-testdata` ist die gemeinsame Zwischenschicht fuer versuchsartuebergreifende Klassen (z. B. allgemeine Testparameter, Probe, Maschine, Ergebnisstruktur). Fachspezifische Ontologien (`tensiletest`, `compressiontest`, `bendingtest`, `fatiguetest`) erweitern diese Basisklassen.

Konsolidierung aus dem Legacy-Tensile-Modell (u. a. `tension_test.py` und `metadata_tensiontest.xlsx`):
- Prozessstruktur: `TestProgram` -> `TestSeries` -> `MechanicalTest`
- Gemeinsame Ressourcen: `Specimen`, `Material`, `TestingMachine`, `Operator`, `Laboratory`
- Serien-/Ist-Parameter: nominal vs. actual fuer `strainRate`, `testingSpeed`, `testingTemperature`, `preDeformation`
- Probe/Geometrie: gauge length, cross-section area, thickness, width, diameter, length, treatment, shape
- Ablauf/Kontext: `testDate`, `testStartTime`, `testEndTime`, `testDirection`, `usesStandard`
- Messdatenmodell: `MeasurementSeries` mit `MeasurementChannel`
- Resultat-Anker: `TestResult`, `maximumForce`, `testPassed`, `remark`

ISO-6892-1-Ausrichtung:
- `tensiletest/TensileTestResult` verwendet notation-nahe KPI-Properties (`Rm`, `ReH`, `ReL`, `Rp`, `Rt`, `Rr`, `A`, `Ae`, `Ag`, `Agt`, `At`, `E`, `Z`, `Su`, `Fm`).
- SHACL-Minimum fuer Zugversuche folgt dem Minimalset aus dem ISO-SKOS: `Rm`, `Rp`, `A`.

## Python/Tests

- Python-Version ist auf `3.12` gepinnt (`.python-version`).
- `pytest` ist als Dev-Dependency in `pyproject.toml` hinterlegt.
- Ausfuehren mit uv:
  - `uv sync --python 3.12 --group dev`
  - `uv run --python 3.12 pytest`

## MkDocs

- MkDocs-Konfiguration: `mkdocs.yml`
- Inhalte: `docs/`
- Ausfuehren mit uv:
  - `uv sync --python 3.12 --group dev --group docs`
  - `uv run --group docs mkdocs serve`
  - `uv run --group docs mkdocs build`
