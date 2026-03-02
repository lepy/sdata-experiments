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
