# Core

Datei: `core/sdata-testdata.ttl`

## Zweck

Gemeinsame Modellierung fuer alle Testarten:

- Prozessstruktur: `TestProgram` -> `TestSeries` -> `MechanicalTest`
- Ressourcen: `Specimen`, `Material`, `TestingMachine`, `Operator`, `Laboratory`
- Kontext: Methode, Standard, Bedingungen, Zeitstempel
- Messstruktur: `MeasurementSeries`, `MeasurementChannel`
- Generischer Ergebnisanker: `TestResult`

## Wichtige Beziehungen

- `hasSeries`, `hasTest`, `partOfProgram`, `partOfSeries`
- `hasSpecimen`, `usesMachine`, `usesStandard`, `hasCondition`
- `hasResult`, `hasMeasurementSeries`, `hasChannel`
