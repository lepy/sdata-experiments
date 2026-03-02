# Vocabularies

Verzeichnis: `vocabularies/`

## Enthalten

- `specimen-shapes.ttl` (z. B. `flat`, `round`, `tubular`, `hexa`)
- `specimen-shapes.ttl` enthaelt zusaetzlich Flat-Tensile-Profile
  (u. a. ISO 527, DIN 50125, ISO 6892, ASTM E8/E8M) als SKOS-Konzepte
  mit Geometrieparametern `w`, `t`, `l0`, `W`, `l2`, `lg`, `l1`, `lt`, `r`
- `material-models.ttl`
- `test-standards.ttl` (inkl. `ISO 178`, `ISO 6892-1`, `ISO 6892-2`)
- `iso6892-1-skos.ttl` als detailliertes tensile Fachvokabular

## Einheitenmodell fuer Probenparameter

Die Geometrieparameter der Flat-Profile sind als `xsd:decimal` modelliert und
tragen am Property jeweils `qudt:unit unit:MilliM` (Millimeter).
Dadurch sind Einheiten explizit maschinenlesbar und eine spaetere automatische
Einheitenkonvertierung bleibt eindeutig moeglich.

## Rolle im Modell

Vokabulare liefern kontrollierte Konzepte, die von OWL-Modulen referenziert werden.
