# Changelog

## 0.6.0 - 2026-03-02
- Continued `sq:*` mappings against external `sdata-quantity` ontology (`https://w3id.org/sdata/quantities/`, sdata-ontology v0.1.0).

## 0.5.0 - 2026-03-02
- Added dedicated fatigue specimen geometry vocabulary `sdata-fatigue-specimens.ttl` (`https://w3id.org/sdata/fatigue/specimens/`).

## 0.4.0 - 2026-03-02
- Added import of `https://w3id.org/sdata/quantities/`.
- Mapped fatigue properties to `sdata-quantities.ttl` via `owl:equivalentProperty`.

## 0.3.0 - 2026-03-02
- Added dedicated `FatigueTestResult` and `hasFatigueResult` relation.
- Scoped cycles-to-failure to fatigue result entities.

## 0.2.0 - 2026-03-02
- Aligned `FatigueTest` with shared `CyclicTest` base class.
- Added `StressRatio` and `CycleFrequency`.

## 0.1.0 - 2026-03-02
- Initial fatigue ontology scaffold created.
