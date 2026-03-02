# TensileTestResult

Datei: `tensiletest/sdata-tensile.ttl`

Klasse: `sdn:TensileTestResult` (Subklasse von `sdt:TestResult`)

Hinweis: `sdn:TensileTestResult` ist der Ergebnis-Container und **nicht**
`sdata:AttributeQuantityValue`. Die einzelnen Kennwerte am Result sind AQV-Knoten.

## Zweck

`TensileTestResult` fasst die berechneten bzw. berichteten Kennwerte eines Zugversuchs zusammen.
Die Verknuepfung zum Versuch erfolgt ueber:

- `sdn:hasTensileResult` (Domain: `sdn:TensileTest`, Range: `sdn:TensileTestResult`)

## Provenance-Standard (Wer/Wann/Wie)

Fuer einen vollstaendigen, revisionssicheren Ergebnisdatensatz sind am Result
folgende Provenance-Felder vorgesehen:

- `sdt:resultGenerationActivity` -> Aktivitaet, die Kennwerte erzeugt hat
- `sdt:resultGeneratedAt` -> Zeitpunkt der Ergebniserzeugung

Die `sdt:ResultGenerationActivity` selbst beschreibt:

- **Wer**: `sdt:responsibleOperator` (verantwortliche Person)
- **Wann**: `sdt:activityStartTime`, `sdt:activityEndTime`
- **Wie**:
  - `sdt:usedMeasurementSeries` (welche Rohdaten)
  - `sdt:usedTestMethod` (welches Verfahren)
  - `sdt:usedSoftwareTool` + `sdt:softwareVersion` (welches Tool)
  - `sdt:usedProcessingPipeline` + `sdt:parameterSetHash` (welcher Auswerte-Workflow)

Diese Felder sind in den Core-/Tensile-SHACL-Shapes als Pflicht- bzw.
Kardinalitaetsregeln modelliert.

## Pflichtfelder (SHACL)

Gem. `shapes/sdata-tensile-shapes.ttl` sind aktuell mindestens erforderlich:

- `sdn:Rm` (Zugfestigkeit)
- `sdn:Rp` (Dehngrenze)
- `sdn:A` (Bruchdehnung)

Optional validiert:

- `sdn:Fm` (Hoechstkraft)

## ISO-6892-1-nahe Kennwerte

Spannungs-/Festigkeitskennwerte:

| Property | ISO-6892-1 Konzept | Normnahe Bedeutung (aus SKOS) | Einheit / Hinweis |
| --- | --- | --- | --- |
| `sdn:Rm` | `iso6892:Rm` (`R_m`) | Spannung bei Hoechstkraft (Zugfestigkeit). | typ. MPa |
| `sdn:ReH` | `iso6892:ReH` (`R_eH`) | Hoechste Spannung vor dem ersten Kraftabfall (obere Streckgrenze). | typ. MPa; zusammen mit `ReL` zu betrachten |
| `sdn:ReL` | `iso6892:ReL` (`R_eL`) | Kleinste Spannung waehrend des plastischen Fliessens (ohne Einschwingeffekte). | typ. MPa |
| `sdn:Rp` | `iso6892:Rp` (`R_p`) | Spannung bei vorgegebenem Anteil plastischer Extensometer-Dehnung. | haeufig `Rp0,2` |
| `sdn:Rt` | `iso6892:Rt` (`R_t`) | Spannung bei vorgegebenem Anteil gesamter Extensometer-Dehnung. | verwandt mit `Rp` |
| `sdn:Rr` | `iso6892:Rr` (`R_r`) | Spannungsgrenzwert, bei dem eine vorgegebene bleibende Dehnung nach Entlastung nicht ueberschritten wird. | typ. MPa |

Quelle der fachlichen Beschreibungen: `vocabularies/iso6892-1-skos.ttl` (DIN EN ISO 6892-1-nahe SKOS-Modellierung).

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

Alle Result-Properties sind als `owl:ObjectProperty` modelliert und erwarten
`sdata:AttributeQuantityValue` als Range.
Fuer vollstaendige AQV-Knoten sollten pro Kennwert mindestens `rdf:value`,
`qudt:unit`, `rdfs:label` und `dcterms:description` gesetzt werden.

## Verknuepfung zu ISO-SKOS

Viele Properties sind per `rdfs:seeAlso` mit Konzepten aus `iso6892-1-skos.ttl` verbunden,
z. B. `sdn:Rm -> iso6892:Rm`, `sdn:A -> iso6892:A`, `sdn:Z -> iso6892:ReductionOfArea`.

Parallel sind die Properties auf das gemeinsame Quantities-Modul gemappt,
z. B. `sdn:Rm -> sq:Rm`, `sdn:Rp -> sq:Rp`, `sdn:Fm -> sq:Fm`.

Zusatzrelation auf AQV-Knoten:

- `sdn:reportsIso6892Property` (Domain: `sdata:AttributeQuantityValue`, Range: `skos:Concept`)

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
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sdn: <https://w3id.org/sdata/tensile/> .
@prefix sdt: <https://w3id.org/sdata/testdata/> .
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .

ex:result-001 a sdn:TensileTestResult ;
  sdn:Rm ex:q-rm ;
  sdn:Rp ex:q-rp ;
  sdn:A ex:q-a ;
  sdn:Fm ex:q-fm ;
  sdt:resultGenerationActivity ex:gen-activity-001 ;
  sdt:resultGeneratedAt "2026-03-02T09:12:20Z"^^xsd:dateTime .

ex:gen-activity-001 a sdt:ResultGenerationActivity ;
  sdt:activityEndTime "2026-03-02T09:12:20Z"^^xsd:dateTime ;
  sdt:responsibleOperator ex:operator-anna ;
  sdt:usedTestMethod ex:method-iso6892-a ;
  sdt:usedMeasurementSeries ex:measurement-series-001 ;
  sdt:usedSoftwareTool ex:software-tool-001 ;
  sdt:usedProcessingPipeline ex:pipeline-001 .

ex:operator-anna a sdt:Operator ; sdt:identifier "anna.m" .
ex:method-iso6892-a a sdt:TestMethod ; sdt:identifier "ISO6892-1-METHOD-A" .
ex:software-tool-001 a sdt:SoftwareTool ;
  sdt:identifier "sdata-evaluator" ;
  sdt:softwareVersion "2.4.1" .
ex:pipeline-001 a sdt:ProcessingPipeline ;
  sdt:identifier "iso6892-1-default-pipeline" ;
  sdt:parameterSetHash "sha256:..." .
ex:measurement-series-001 a sdt:MeasurementSeries ;
  sdt:samplingFrequency "1000.0"^^xsd:decimal ;
  sdt:hasChannel ex:channel-force .
ex:channel-force a sdt:MeasurementChannel ;
  sdt:channelName "Force" ;
  sdt:channelUnit "N" .

ex:q-rm a sdata:AttributeQuantityValue ;
  rdf:value "512.0"^^xsd:decimal ;
  qudt:unit unit:MPa ;
  rdfs:label "Tensile strength Rm"@en ;
  dcterms:description "Maximum tensile stress according to ISO 6892-1."@en .
ex:q-rp a sdata:AttributeQuantityValue ;
  rdf:value "355.0"^^xsd:decimal ;
  qudt:unit unit:MPa ;
  rdfs:label "Proof strength Rp"@en ;
  dcterms:description "Proof strength (0.2% plastic strain)."@en .
ex:q-a a sdata:AttributeQuantityValue ;
  rdf:value "23.4"^^xsd:decimal ;
  qudt:unit unit:PERCENT ;
  rdfs:label "Percentage elongation after fracture A"@en ;
  dcterms:description "Elongation after fracture."@en .
ex:q-fm a sdata:AttributeQuantityValue ;
  rdf:value "25200.0"^^xsd:decimal ;
  qudt:unit unit:N ;
  rdfs:label "Maximum force Fm"@en ;
  dcterms:description "Maximum force measured during tensile test."@en .
```

## Empfehlung fuer Instanzdaten

- Primar die ISO-nahen Properties (`Rm`, `Rp`, `A`, ...) verwenden.
- Legacy-Properties nur fuer Imports/Altbestandsdaten nutzen.
- SHACL gegen `shapes/sdata-tensile-shapes.ttl` oder den Sammelgraph
  `shapes/sdata-shapes.ttl` laufen lassen.
