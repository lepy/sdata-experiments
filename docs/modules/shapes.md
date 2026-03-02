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
- Tensile: Mindestset `sq:Rm`, `sq:Rp`, `sq:A` plus Kardinalitaeten/Datentypen
- Compression: `sq:CompressiveStrength`, `sq:CompressionModulus`
- Bending: Resultatwerte plus `sq:SupportSpanLength`
- Fatigue: `sq:NumberOfCyclesToFailure`, `sq:CycleFrequency`, `sq:StressRatio`
- Aggregation: `sdata-shapes.ttl` importiert alle Shape-Module
