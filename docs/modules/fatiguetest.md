# Fatigue Test

Datei: `fatiguetest/sdata-fatigue.ttl`

Zugehoerige Probengeometrien: `fatiguetest/sdata-fatigue-specimens.ttl`

## Klassen

- `FatigueTest` (Subklasse von `CyclicTest`)
- `FatigueTestResult` (Subklasse von `TestResult`)

## Kennwerte

- `NumberOfCyclesToFailure`
- `StressRatio`
- `CycleFrequency`

Die Kennwerte sind auf `https://w3id.org/sdata/quantities/` gemappt
(`sq:NumberOfCyclesToFailure`, `sq:StressRatio`, `sq:CycleFrequency`).
