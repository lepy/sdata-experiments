# sdata-testdata

`sdata-testdata` ist ein Monorepo fuer modulare Ontologien zu mechanischen Pruefdaten.

## Ziele

- Getrennte fachliche Module mit stabilem Namespace
- Gemeinsame, wiederverwendbare Kernschicht (`core`)
- Erweiterbare Testdomaenen (`tensile`, `compression`, `bending`, `fatigue`)
- SHACL-basierte Validierungsschicht

## Moduluebersicht

- `core/`: testspezies-unabhaengige Basisklassen und Properties
- `tensiletest/`: Zugversuch inkl. ISO-6892-1-bezogener Resultatkennwerte
- `compressiontest/`: Druckversuch
- `bendingtest/`: Biegeversuch
- `fatiguetest/`: Ermuedungsversuch
- `shapes/`: SHACL-Regeln
- `vocabularies/`: SKOS-Konzepte (z. B. Geometrien, Standards)

## Einstieg

Siehe [Getting Started](getting-started.md) fuer `uv`-Kommandos und lokale Doku-Builds.
