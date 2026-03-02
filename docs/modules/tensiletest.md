# Tensile Test

Datei: `tensiletest/sdata-tensile.ttl`

## Klassen

- `TensileTest` (Subklasse von `QuasiStaticTest`)
- `TensileTestResult` (Subklasse von `TestResult`)

## ISO-6892-1-Ausrichtung

`TensileTestResult` verwendet notation-nahe Kennwerte wie:

- `Rm`, `ReH`, `ReL`, `Rp`, `Rt`, `Rr`
- `A`, `Ae`, `Ag`, `Agt`, `At`
- `E`, `Z`, `Su`, `Fm`

Legacy-Namen bleiben ueber `owl:equivalentProperty` abbildbar.

## Detaildoku

Eine vollstaendige Referenz fuer `TensileTestResult` inkl. SHACL-Pflichtfeldern und
Legacy-Mapping steht hier:

- [TensileTestResult](tensiletest-result.md)
