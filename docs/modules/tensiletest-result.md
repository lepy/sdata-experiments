# TensileTestResult

Datei: `tensiletest/sdata-tensile.ttl`

Klasse: `sdn:TensileTestResult` (Subklasse von `sdt:TestResult`)

## Zweck

`TensileTestResult` fasst die berechneten bzw. berichteten Kennwerte eines Zugversuchs zusammen.
Die Verknuepfung zum Versuch erfolgt ueber:

- `sdn:hasTensileResult` (Domain: `sdn:TensileTest`, Range: `sdn:TensileTestResult`)

## Pflichtfelder (SHACL)

Gem. `shapes/sdata-tensile-shapes.ttl` sind aktuell mindestens erforderlich:

- `sdn:Rm` (Zugfestigkeit)
- `sdn:Rp` (Dehngrenze)
- `sdn:A` (Bruchdehnung)

Optional validiert:

- `sdn:Fm` (Hoechstkraft)

## ISO-6892-1-nahe Kennwerte

Spannungs-/Festigkeitskennwerte:

- `sdn:Rm`
- `sdn:ReH`
- `sdn:ReL`
- `sdn:Rp`
- `sdn:Rt`
- `sdn:Rr`

Dehnungskennwerte:

- `sdn:A`
- `sdn:Ae`
- `sdn:Ag`
- `sdn:Agt`
- `sdn:At`

Weitere Kennwerte:

- `sdn:E`
- `sdn:Z`
- `sdn:Su`
- `sdn:Fm`

Alle Datentyp-Properties sind auf `xsd:decimal` modelliert (ausgenommen keine).

## Verknuepfung zu ISO-SKOS

Viele Properties sind per `rdfs:seeAlso` mit Konzepten aus `iso6892-1-skos.ttl` verbunden,
z. B. `sdn:Rm -> iso6892:Rm`, `sdn:A -> iso6892:A`, `sdn:Z -> iso6892:ReductionOfArea`.

Parallel sind die Properties auf das gemeinsame Quantities-Modul gemappt,
z. B. `sdn:Rm -> sq:Rm`, `sdn:Rp -> sq:Rp`, `sdn:Fm -> sq:Fm`.

Zusatzrelation:

- `sdn:reportsIso6892Property` (Range: `skos:Concept`)

## Legacy-Mapping

Zur Rueckwaertskompatibilitaet sind Legacy-Namen per `owl:equivalentProperty` auf
ISO-nahe Properties gemappt:

- `YieldStrength -> Rp`
- `UpperYieldStrength -> ReH`
- `LowerYieldStrength -> ReL`
- `UltimateTensileStrength -> Rm`
- `ElongationAtBreak -> A`
- `PlasticExtensionAtMaximumForce -> Ag`
- `TotalExtensionAtMaximumForce -> Agt`
- `TotalExtensionAtFracture -> At`
- `MinimumCrossSectionAfterFracture -> Su`
- `ReductionOfArea -> Z`

Zusatz:

- `Fm` ist zusaetzlich auf `sdt:maximumForce` gemappt.

## Beispiel (Turtle)

```ttl
@prefix ex: <https://example.org/data/> .
@prefix sdn: <https://w3id.org/sdata/tensile/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:result-001 a sdn:TensileTestResult ;
  sdn:Rm "512.0"^^xsd:decimal ;
  sdn:Rp "355.0"^^xsd:decimal ;
  sdn:A "23.4"^^xsd:decimal ;
  sdn:Fm "25200.0"^^xsd:decimal .
```

## Empfehlung fuer Instanzdaten

- Primar die ISO-nahen Properties (`Rm`, `Rp`, `A`, ...) verwenden.
- Legacy-Properties nur fuer Imports/Altbestandsdaten nutzen.
- SHACL gegen `shapes/sdata-tensile-shapes.ttl` oder den Sammelgraph
  `shapes/sdata-shapes.ttl` laufen lassen.
