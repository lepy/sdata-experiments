# Architektur

## Import-Kette

```text
MIN -> sdata-core -> sdata-testdata -> sdata-tensile
                                  -> sdata-compression
                                  -> sdata-bending
                                  -> sdata-fatigue
```

`core/sdata-testdata.ttl` ist die gemeinsame Zwischenschicht fuer versuchsartuebergreifende Modellanteile.

## Designprinzip

- Namespaces sind fachlich stabil
- Module sind logisch getrennt, aber ueber `owl:imports` verbunden
- Resultatklassen liegen in den fachlichen Testmodulen
- SHACL in `shapes/` bleibt von OWL-Modellen getrennt
