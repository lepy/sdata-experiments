# Tensile Test Beispiel (DP600)

Datei im Repo: `examples/dp600.ttl`

Dieses Beispiel zeigt einen vollstaendigen Zugversuch mit:

- `sdt:TestProgram -> sdt:TestSeries -> sdn:TensileTest`
- `sdn:TensileTestResult` als Ergebnis-Container
- Result-Kennwerten als separate `sdata:AttributeQuantityValue`-Knoten

## Vollstaendiges Beispiel (Turtle)

```ttl
@prefix ex: <https://example.org/data/dp600/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix sdt: <https://w3id.org/sdata/testdata/> .
@prefix sdn: <https://w3id.org/sdata/tensile/> .
@prefix sq: <https://w3id.org/sdata/quantities/> .
@prefix stsp: <https://w3id.org/sdata/tensile/specimens/> .
@prefix vocts: <https://w3id.org/sdata/vocabularies/test-standards/> .

ex:program-dp600 a sdt:TestProgram ;
  sdt:programId "PRG-DP600-2026" ;
  sdt:hasSeries ex:series-dp600-tensile .

ex:series-dp600-tensile a sdt:TestSeries ;
  sdt:seriesId "SER-DP600-TEN-01" ;
  sdt:partOfProgram ex:program-dp600 ;
  sdt:hasTest ex:tensile-test-001 .

ex:material-dp600 a sdt:Material ;
  sdt:identifier "DP600" ;
  sdt:remark "Dual phase steel" .

ex:specimen-a1 a sdt:Specimen ;
  sdt:identifier "DP600-A1" ;
  sdt:hasMaterial ex:material-dp600 ;
  sdt:specimenShape stsp:iso6892_b1_1 ;
  sdt:specimenThickness "1.20"^^xsd:decimal ;
  sdt:specimenWidth "20.00"^^xsd:decimal ;
  sdt:specimenLength "120.00"^^xsd:decimal .

ex:machine-zwick-01 a sdt:TestingMachine ;
  sdt:identifier "ZWICK-Z250-01" .

ex:operator-anna a sdt:Operator ;
  sdt:identifier "anna.m" .

ex:lab-berlin a sdt:Laboratory ;
  sdt:identifier "LAB-BERLIN-01" .

ex:method-iso6892-a a sdt:TestMethod ;
  sdt:identifier "ISO6892-1-METHOD-A" .

ex:condition-rt a sdt:TestCondition ;
  sdt:testTemperature "23.0"^^xsd:decimal ;
  sdt:testHumidity "45.0"^^xsd:decimal .

ex:channel-force a sdt:MeasurementChannel ;
  sdt:channelName "Force" ;
  sdt:channelUnit "N" ;
  sdt:channelDatatype "xsd:decimal" .

ex:channel-extension a sdt:MeasurementChannel ;
  sdt:channelName "Extension" ;
  sdt:channelUnit "mm" ;
  sdt:channelDatatype "xsd:decimal" .

ex:measurement-series-001 a sdt:MeasurementSeries ;
  sdt:samplingFrequency "1000.0"^^xsd:decimal ;
  sdt:hasChannel ex:channel-force, ex:channel-extension .

ex:software-tool-001 a sdt:SoftwareTool ;
  sdt:identifier "sdata-evaluator" ;
  sdt:softwareVersion "2.4.1" .

ex:pipeline-001 a sdt:ProcessingPipeline ;
  sdt:identifier "iso6892-1-default-pipeline" ;
  sdt:parameterSetHash "sha256:1f8b8e9d4ec7bc2a9d7b4efdd86ad6f8ab03d4a33739d4a4261f4b640df83d8f" .

ex:result-generation-001 a sdt:ResultGenerationActivity ;
  sdt:activityStartTime "2026-03-02T09:12:02Z"^^xsd:dateTime ;
  sdt:activityEndTime "2026-03-02T09:12:20Z"^^xsd:dateTime ;
  sdt:usedMeasurementSeries ex:measurement-series-001 ;
  sdt:usedTestMethod ex:method-iso6892-a ;
  sdt:usedSoftwareTool ex:software-tool-001 ;
  sdt:usedProcessingPipeline ex:pipeline-001 ;
  sdt:responsibleOperator ex:operator-anna .

ex:tensile-test-001 a sdn:TensileTest ;
  sdt:testId "TEN-DP600-001" ;
  sdt:partOfSeries ex:series-dp600-tensile ;
  sdt:hasSpecimen ex:specimen-a1 ;
  sdt:usesMachine ex:machine-zwick-01 ;
  sdt:performedBy ex:operator-anna ;
  sdt:performedAt ex:lab-berlin ;
  sdt:usesMethod ex:method-iso6892-a ;
  sdt:usesStandard vocts:ISO6892_1 ;
  sdt:hasCondition ex:condition-rt ;
  sdt:hasMeasurementSeries ex:measurement-series-001 ;
  sdt:testDate "2026-03-02"^^xsd:date ;
  sdt:testStartTime "2026-03-02T09:00:00Z"^^xsd:dateTime ;
  sdt:testEndTime "2026-03-02T09:12:00Z"^^xsd:dateTime ;
  sdn:hasTensileResult ex:tensile-result-001 ;
  sdt:hasResult ex:tensile-result-001 .

ex:tensile-result-001 a sdn:TensileTestResult ;
  sq:Rm ex:q-rm ;
  sq:Rp ex:q-rp ;
  sq:A ex:q-a ;
  sq:ReH ex:q-reh ;
  sq:ReL ex:q-rel ;
  sq:Agt ex:q-agt ;
  sq:At ex:q-at ;
  sq:Z ex:q-z ;
  sq:Fm ex:q-fm ;
  sdt:testPassed ex:q-test-passed ;
  sdt:resultGenerationActivity ex:result-generation-001 ;
  sdt:resultGeneratedAt "2026-03-02T09:12:20Z"^^xsd:dateTime ;
  sdt:remark "DP600 tensile sample, room temperature." .

ex:q-rm a sdata:AttributeQuantityValue ;
  rdf:value "612.0"^^xsd:decimal ;
  qudt:unit unit:MPa ;
  rdfs:label "Tensile strength Rm"@en ;
  dcterms:description "Maximum tensile stress according to ISO 6892-1."@en .
ex:q-rp a sdata:AttributeQuantityValue ;
  rdf:value "402.0"^^xsd:decimal ;
  qudt:unit unit:MPa ;
  rdfs:label "Proof strength Rp"@en ;
  dcterms:description "Proof strength (0.2% plastic strain) according to ISO 6892-1."@en .
ex:q-a a sdata:AttributeQuantityValue ;
  rdf:value "18.5"^^xsd:decimal ;
  qudt:unit unit:PERCENT ;
  rdfs:label "Percentage elongation after fracture A"@en ;
  dcterms:description "Total elongation measured after fracture."@en .
ex:q-reh a sdata:AttributeQuantityValue ;
  rdf:value "410.0"^^xsd:decimal ;
  qudt:unit unit:MPa ;
  rdfs:label "Upper yield strength ReH"@en ;
  dcterms:description "Upper yield strength according to ISO 6892-1."@en .
ex:q-rel a sdata:AttributeQuantityValue ;
  rdf:value "396.0"^^xsd:decimal ;
  qudt:unit unit:MPa ;
  rdfs:label "Lower yield strength ReL"@en ;
  dcterms:description "Lower yield strength according to ISO 6892-1."@en .
ex:q-agt a sdata:AttributeQuantityValue ;
  rdf:value "11.4"^^xsd:decimal ;
  qudt:unit unit:PERCENT ;
  rdfs:label "Total extension at maximum force Agt"@en ;
  dcterms:description "Total extension at the moment of maximum force."@en .
ex:q-at a sdata:AttributeQuantityValue ;
  rdf:value "19.2"^^xsd:decimal ;
  qudt:unit unit:PERCENT ;
  rdfs:label "Total extension at fracture At"@en ;
  dcterms:description "Total extension measured at fracture."@en .
ex:q-z a sdata:AttributeQuantityValue ;
  rdf:value "38.0"^^xsd:decimal ;
  qudt:unit unit:PERCENT ;
  rdfs:label "Reduction of area Z"@en ;
  dcterms:description "Reduction of cross-sectional area after fracture."@en .
ex:q-fm a sdata:AttributeQuantityValue ;
  rdf:value "24500.0"^^xsd:decimal ;
  qudt:unit unit:N ;
  rdfs:label "Maximum force Fm"@en ;
  dcterms:description "Maximum force measured during tensile test."@en .
ex:q-test-passed a sdata:AttributeQuantityValue ;
  rdf:value "true"^^xsd:boolean ;
  qudt:unit unit:UNITLESS ;
  rdfs:label "Test passed"@en ;
  dcterms:description "Boolean pass/fail outcome of quality criteria."@en .
```
