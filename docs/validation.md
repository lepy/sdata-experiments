# Validation

## SHACL

Die SHACL-Dateien unter `shapes/` bilden das erste Validierungsniveau fuer RDF-Instanzen.

## Empfohlener Ablauf

1. Instanzdaten gegen die passenden `NodeShape`-Klassen pruefen
2. Fehler in Test-/Resultatzuordnungen beheben
3. KPI-Mindestmengen pro Testtyp sicherstellen

## Python-Test-Sanity

```bash
uv run --python 3.12 pytest
```
