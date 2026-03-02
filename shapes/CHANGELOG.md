# Changelog

## 0.7.0 - 2026-03-02
- Switched result-value SHACL paths to shared `sq:*` quantity properties from `sdata-quantities.ttl`.
- Added `sdata-quantities` imports to core and test-type shape graphs.

## 0.6.0 - 2026-03-02
- Added `sdata-core-shapes.ttl` with reusable constraints for core process, specimen, conditions, measurements, and results.
- Added `sdata-compression-shapes.ttl` and `sdata-fatigue-shapes.ttl`.
- Added `sdata-shapes.ttl` as aggregate imports entrypoint for all shape graphs.
- Strengthened tensile and bending shapes with cardinality, datatype, and numeric range constraints.

## 0.5.0 - 2026-03-02
- Added `sdata-bending-shapes.ttl` with base constraints for `BendingTest` and `BendingTestResult`.

## 0.4.0 - 2026-03-02
- Switched tensile result SHACL minimum set to ISO 6892-1 minimal report KPIs: `Rm`, `Rp`, `A`.

## 0.3.0 - 2026-03-02
- Updated tensile SHACL to require `hasTensileResult` on `TensileTest`.
- Added `TensileTestResultShape` for KPI constraints.

## 0.2.0 - 2026-03-02
- Added shared constraints for `hasSpecimen` and `usesMachine`.
- Added explicit import of `sdata-testdata`.

## 0.1.0 - 2026-03-02
- Initial SHACL shapes scaffold for tensile tests.
