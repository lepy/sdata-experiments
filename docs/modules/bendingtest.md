# Bending Test

Datei: `bendingtest/sdata-bending.ttl`

Zugehoerige Probengeometrien: `bendingtest/sdata-bending-specimens.ttl`

## Klassen

- `BendingTest` (Subklasse von `QuasiStaticTest`)
- `BendingTestResult` (Subklasse von `TestResult`)

## Kennwerte

- `FlexuralStrength`
- `FlexuralModulus`
- `MaximumDeflectionAtFailure`
- `SupportSpanLength`

Die Result-Kennwerte sind auf `sdata-quantities.ttl` gemappt
(`sq:FlexuralStrength`, `sq:FlexuralModulus`, `sq:MaximumDeflectionAtFailure`).
