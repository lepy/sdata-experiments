# Core

Dateien:

- `core/sdata-testdata.ttl`
- extern: `https://w3id.org/sdata/quantities/` (aus `sdata-ontology` repo, v0.1.0)

## Zweck

Gemeinsame Modellierung fuer alle Testarten:

- Prozessstruktur: `TestProgram` -> `TestSeries` -> `MechanicalTest`
- Ressourcen: `Specimen`, `Material`, `TestingMachine`, `Operator`, `Laboratory`
- Kontext: Methode, Standard, Bedingungen, Zeitstempel
- Messstruktur: `MeasurementSeries`, `MeasurementChannel`
- Generischer Ergebnisanker: `TestResult`
- Ergebnis-Provenance: `ResultGenerationActivity`, `SoftwareTool`, `ProcessingPipeline`

`sdata-testdata.ttl` ist dabei explizit auf `sdata-core` ausgerichtet
(z. B. `InformationArtifact`, `MaterialArtifact`, `MaterialProcess`, `InformationProcess`).

## MIN FORMA (exemplarisch)

Zusätzlich nutzt das Core-Modul exemplarisch den FORMA-Zweig aus MIN:

- `TestFormalModel` als `min:Structura` (z. B. Auswerte-/Identifikationsmodell)
- `TestAcceptanceCriterion` als `min:Norma` (Soll-/Grenzkriterium)
- `TestGoverningLaw` als `min:Lex` (naturgesetzliche Regularität)

Brueckenrelationen:

- `methodEncodesFormalModel` `rdfs:subPropertyOf min:encodes`
- `formalModelFormalizesTest` `rdfs:subPropertyOf min:formalizes`
- `acceptanceCriterionEvaluatesResult` `rdfs:subPropertyOf min:evaluates`
- `governingLawGovernsTest` `rdfs:subPropertyOf min:governs`

## Wichtige Beziehungen

- `hasSeries`, `hasTest`, `partOfProgram`, `partOfSeries`
- `hasSpecimen`, `usesMachine`, `usesStandard`, `hasCondition`
- `hasResult`, `hasMeasurementSeries`, `hasChannel`
- `resultGenerationActivity`, `resultGeneratedAt`
- `usedMeasurementSeries`, `usedTestMethod`, `usedSoftwareTool`, `usedProcessingPipeline`, `responsibleOperator`

## Quantities

Die externe `sdata-quantity`-Ontologie (`https://w3id.org/sdata/quantities/`) bietet zentrale
Kennwert-Properties (z. B. `sq:Rm`, `sq:CompressiveStrength`, `sq:FlexuralStrength`,
`sq:NumberOfCyclesToFailure`), die in Result-Modulen per `owl:equivalentProperty` genutzt werden.
