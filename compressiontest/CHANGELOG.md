# Changelog

## 0.6.0 - 2026-03-02
- Continued `sq:*` mappings against external `sdata-quantity` ontology (`https://w3id.org/sdata/quantities/`, sdata-ontology v0.1.0).

## 0.5.0 - 2026-03-02
- Added dedicated compression specimen geometry vocabulary `sdata-compression-specimens.ttl` (`https://w3id.org/sdata/compression/specimens/`).

## 0.4.0 - 2026-03-02
- Added import of `https://w3id.org/sdata/quantities/`.
- Mapped compression result properties to `sdata-quantities.ttl` via `owl:equivalentProperty`.

## 0.3.0 - 2026-03-02
- Added dedicated `CompressionTestResult` and `hasCompressionResult` relation.
- Scoped compression KPIs to result entities.

## 0.2.0 - 2026-03-02
- Aligned `CompressionTest` with shared `QuasiStaticTest` base class.
- Added `StrainAtCompressiveStrength`.

## 0.1.0 - 2026-03-02
- Initial compression ontology scaffold created.
