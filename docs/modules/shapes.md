# Shapes

Dateien:

- `shapes/sdata-shapes.ttl`
- `shapes/sdata-core-shapes.ttl`
- `shapes/sdata-tensile-shapes.ttl`
- `shapes/sdata-compression-shapes.ttl`
- `shapes/sdata-bending-shapes.ttl`
- `shapes/sdata-fatigue-shapes.ttl`

## Zweck

SHACL-Validierung fuer Instanzdaten.

## Aktueller Fokus

- Core: Prozessstruktur (`TestProgram -> TestSeries -> MechanicalTest`), IDs, Datentypen
- Tensile: Mindestset `Rm`, `Rp`, `A` plus Kardinalitaeten/Datentypen
- Compression: `CompressiveStrength`, `CompressionModulus`
- Bending: Resultatwerte plus `SupportSpanLength`
- Fatigue: `NumberOfCyclesToFailure`, `CycleFrequency`, `StressRatio`
- Aggregation: `sdata-shapes.ttl` importiert alle Shape-Module
