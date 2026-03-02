# Changelog

## 0.8.0 - 2026-03-03
- Added explicit MIN import (`https://w3id.org/min`) in `sdata-testdata.ttl`.
- Added exemplaric FORMA-aligned classes for test semantics:
  - `TestFormalModel` (`min:Structura`)
  - `TestAcceptanceCriterion` (`min:Norma`)
  - `TestGoverningLaw` (`min:Lex`)
- Added FORMA bridge properties:
  - `methodEncodesFormalModel` subPropertyOf `min:encodes`
  - `formalModelFormalizesTest` subPropertyOf `min:formalizes`
  - `acceptanceCriterionEvaluatesResult` subPropertyOf `min:evaluates`
  - `governingLawGovernsTest` subPropertyOf `min:governs`

## 0.7.0 - 2026-03-02
- Aligned `sdata-testdata.ttl` class hierarchy with `sdata-core`:
  - test programs/series/results/channels/methods/conditions as `sdata:InformationArtifact`
  - tests as `sdata:MaterialProcess`
  - specimens/machines as `sdata:MaterialArtifact`
  - result generation as `sdata:InformationProcess`
- Added generic core-property links:
  - `maximumForce`, `testPassed` as subproperties of `sdata:hasQuantity`
  - `remark` as subproperty of `sdata:description`

## 0.6.0 - 2026-03-02
- Removed local `core/sdata-quantities.ttl`; quantities are now sourced from external `sdata-ontology` repo (`sdata-quantity` v0.1.0, namespace `https://w3id.org/sdata/quantities/`).

## 0.5.0 - 2026-03-02
- Added provenance model for result generation:
  - `ResultGenerationActivity`, `SoftwareTool`, `ProcessingPipeline`
  - `resultGenerationActivity`, `resultGeneratedAt`
  - `usedMeasurementSeries`, `usedTestMethod`, `usedSoftwareTool`, `usedProcessingPipeline`, `responsibleOperator`
  - `activityStartTime`, `activityEndTime`, `softwareVersion`, `parameterSetHash`
- Added local provenance semantics in `sdata-testdata` for result-generation tracking.

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
