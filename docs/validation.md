# Validation

## SHACL

Die SHACL-Dateien unter `shapes/` bilden das erste Validierungsniveau fuer RDF-Instanzen.

- Einstiegspunkt fuer alle Shapes: `shapes/sdata-shapes.ttl`
- Core-Regeln: `shapes/sdata-core-shapes.ttl`
- Testtypspezifische Regeln: `shapes/sdata-*-shapes.ttl`

## Empfohlener Ablauf

1. Instanzdaten gegen die passenden `NodeShape`-Klassen pruefen
2. Fehler in Test-/Resultatzuordnungen beheben
3. KPI-Mindestmengen pro Testtyp sicherstellen

## Parser-Check fuer Turtle-Dateien

```bash
make ttl-check
```

## Test-Sanity

```bash
make test
```
