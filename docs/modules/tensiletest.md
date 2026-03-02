# Tensile Test

Datei: `tensiletest/sdata-tensile.ttl`

Zugehoerige Probengeometrien: `tensiletest/sdata-tensile-specimens.ttl`

## Klassen

- `TensileTest` (Subklasse von `QuasiStaticTest`)
- `TensileTestResult` (Subklasse von `TestResult`)

## ISO-6892-1-Ausrichtung

`TensileTestResult` verwendet notation-nahe Kennwerte wie:

- `Rm`, `ReH`, `ReL`, `Rp`, `Rt`, `Rr`
- `A`, `Ae`, `Ag`, `Agt`, `At`
- `E`, `Z`, `Su`, `Fm`

Legacy-Namen bleiben ueber `owl:equivalentProperty` abbildbar.

Alle Result-Kennwerte sind zusaetzlich auf `sdata-quantities.ttl` gemappt
(z. B. `sdn:Rm -> sq:Rm`).

Fuer standardisierte Ergebnisablage ist am `TensileTestResult` zusaetzlich
Provenance verpflichtend (`sdt:resultGenerationActivity`, `sdt:resultGeneratedAt`).

## Wichtige Modellregel

`TensileTestResult` ist **kein** `sdata:AttributeQuantityValue`, sondern die
Container-Klasse fuer den Versuchsausgang.
Die einzelnen Result-Properties (`Rm`, `Rp`, `A`, `Fm`, ...) zeigen jeweils auf
eigene Knoten vom Typ `sdata:AttributeQuantityValue`.

## Detaildoku

Eine vollstaendige Referenz fuer `TensileTestResult` inkl. SHACL-Pflichtfeldern und
Legacy-Mapping steht hier:

- [TensileTestResult](tensiletest-result.md)
- [DP600 Tensile Beispiel](tensiletest-dp600.md)
