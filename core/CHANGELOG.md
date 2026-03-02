# Changelog

## 0.6.0 - 2026-03-02
- Removed local `core/sdata-quantities.ttl`; quantities are now sourced from external `sdata-ontology` repo (`sdata-quantity` v0.1.0, namespace `https://w3id.org/sdata/quantities/`).

## 0.5.0 - 2026-03-02
- Added provenance model for result generation:
  - `ResultGenerationActivity`, `SoftwareTool`, `ProcessingPipeline`
  - `resultGenerationActivity`, `resultGeneratedAt`
  - `usedMeasurementSeries`, `usedTestMethod`, `usedSoftwareTool`, `usedProcessingPipeline`, `responsibleOperator`
  - `activityStartTime`, `activityEndTime`, `softwareVersion`, `parameterSetHash`
- Linked provenance semantics to PROV-O terms (`prov:*`) via imports/equivalent/subProperty relations.

## 0.4.0 - 2026-03-02
- Added `sdata-quantities.ttl` as shared quantities ontology.
- Added import of `https://w3id.org/sdata/quantities/` in `sdata-testdata.ttl`.
- Linked `sdt:maximumForce` to `sq:Fm` via `owl:equivalentProperty`.

## 0.3.0 - 2026-03-02
- Reworked `sdata-testdata` using legacy tensile metadata as source for cross-test concepts.
- Added process hierarchy classes: `TestProgram`, `TestSeries`, `MechanicalTest`.
- Added shared nominal/actual properties (strain rate, speed, temperature, pre-deformation).
- Added specimen geometry and treatment properties plus links to SKOS vocabularies.
- Added operator/laboratory context and measurement series/channel structure.

## 0.2.0 - 2026-03-02
- Expanded shared model into a true cross-test layer.
- Added common classes for methods, standards, conditions, and measurement series.
- Added shared properties for test lifecycle, specimen geometry, conditions, and generic result flags.

## 0.1.0 - 2026-03-02
- Initial module scaffold created.
- Added shared `sdata-testdata` ontology with base classes and properties.
