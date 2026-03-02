# Quantities

Datei: `core/sdata-quantities.ttl`

Namespace: `https://w3id.org/sdata/quantities/`

## Zweck

Zentrale, wiederverwendbare Kennwert-Properties fuer Resultate ueber alle Testtypen.

## Enthaltene Kennwertgruppen

- Tensile: `Rm`, `ReH`, `ReL`, `Rp`, `Rt`, `Rr`, `A`, `Ae`, `Ag`, `Agt`, `At`, `E`, `Z`, `Su`, `Fm`
- Compression: `CompressiveStrength`, `CompressionModulus`, `StrainAtCompressiveStrength`
- Bending: `FlexuralStrength`, `FlexuralModulus`, `MaximumDeflectionAtFailure`, `SupportSpanLength`
- Fatigue: `NumberOfCyclesToFailure`, `StressRatio`, `CycleFrequency`

## Nutzung in den Testmodulen

Die jeweiligen Modul-Properties bleiben bestehen, sind aber auf Quantities gemappt,
z. B.:

- `sdn:Rm owl:equivalentProperty sq:Rm`
- `sdc:CompressiveStrength owl:equivalentProperty sq:CompressiveStrength`
- `sdb:FlexuralStrength owl:equivalentProperty sq:FlexuralStrength`
- `sdf:NumberOfCyclesToFailure owl:equivalentProperty sq:NumberOfCyclesToFailure`

Damit bleiben bestehende Daten kompatibel und zugleich auf eine gemeinsame Kennwertbasis ausrichtbar.
