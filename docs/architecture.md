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
- MIN/FORMA wird im Core exemplarisch genutzt (Structura/Norma/Lex) fuer Modell, Kriterium und Gesetz im Versuchskontext

## Batch-Modell

- Ein Batch wird als `TestSeries` modelliert.
- Mehrere `MechanicalTest`-Instanzen gehoeren ueber `hasTest` zur selben Serie.
- `seriesId` ist die technische Batch-ID.
- Material-/Schmelzchargen koennen zusaetzlich ueber `identifier` auf `Material` oder `Specimen` gefuehrt werden.

## MIN FORMA im Core

In `core/sdata-testdata.ttl` sind folgende FORMA-Elemente angebunden:

- `sdt:TestFormalModel` `rdfs:subClassOf min:Structura`
- `sdt:TestAcceptanceCriterion` `rdfs:subClassOf min:Norma`
- `sdt:TestGoverningLaw` `rdfs:subClassOf min:Lex`

Und als Brueckenrelationen:

- `sdt:methodEncodesFormalModel` `rdfs:subPropertyOf min:encodes`
- `sdt:formalModelFormalizesTest` `rdfs:subPropertyOf min:formalizes`
- `sdt:acceptanceCriterionEvaluatesResult` `rdfs:subPropertyOf min:evaluates`
- `sdt:governingLawGovernsTest` `rdfs:subPropertyOf min:governs`
