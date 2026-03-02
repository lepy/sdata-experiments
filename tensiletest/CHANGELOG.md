# Changelog

## 0.7.0 - 2026-03-02
- Elevated `TensileTestResult` to full traceable record by requiring provenance linkage (`resultGenerationActivity`, `resultGeneratedAt`) through shared core/shapes model.

## 0.6.0 - 2026-03-02
- Added dedicated tensile specimen geometry vocabulary `sdata-tensile-specimens.ttl` (`https://w3id.org/sdata/tensile/specimens/`).
- Moved standardized tensile profile definitions (ISO/DIN/ASTM/JIS etc.) to tensile module scope.

## 0.5.0 - 2026-03-02
- Added import of `https://w3id.org/sdata/quantities/`.
- Mapped tensile result KPIs to `sdata-quantities.ttl` via `owl:equivalentProperty`.

## 0.4.0 - 2026-03-02
- Aligned `TensileTestResult` with ISO 6892-1 notation-based KPIs (`Rm`, `ReH`, `ReL`, `Rp`, `Rt`, `Rr`, `A`, `Ae`, `Ag`, `Agt`, `At`, `E`, `Z`, `Su`, `Fm`).
- Added explicit mappings from legacy property names to ISO-style properties via `owl:equivalentProperty`.
- Linked ISO-style KPIs to SKOS concepts from `iso6892-1-skos.ttl` via `rdfs:seeAlso`.

## 0.3.0 - 2026-03-02
- Added dedicated `TensileTestResult` and `hasTensileResult` relation.
- Moved tensile KPIs to result scope (yield strengths, UTS, elongation/extension metrics).
- Added legacy-aligned tensile result properties (e.g. `UpperYieldStrength`, `TotalExtensionAtFracture`).

## 0.2.0 - 2026-03-02
- Aligned `TensileTest` with shared `QuasiStaticTest` base class.
- Added `ReductionOfArea`.

## 0.1.0 - 2026-03-02
- Initial tensile ontology scaffold created.
- Added core tensile result properties.
