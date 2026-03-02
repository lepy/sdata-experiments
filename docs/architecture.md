# Architektur

## Import-Kette

```text
MIN -> sdata-core -> sdata-quantities
                 -> sdata-testdata -> sdata-tensile
                                  -> sdata-compression
                                  -> sdata-bending
                                  -> sdata-fatigue
```

`core/sdata-testdata.ttl` ist die gemeinsame Zwischenschicht fuer versuchsartuebergreifende Modellanteile.
Alle TTL-Module und Shape-/Vokabular-Graphen importieren zusaetzlich direkt `https://w3id.org/sdata/core/`.

## Designprinzip

- Namespaces sind fachlich stabil
- Module sind logisch getrennt, aber ueber `owl:imports` verbunden
- Resultatklassen liegen in den fachlichen Testmodulen
- Resultatkennwerte sind ueber `https://w3id.org/sdata/quantities/` (externes `sdata-quantity`) vereinheitlicht
- SHACL in `shapes/` bleibt von OWL-Modellen getrennt
