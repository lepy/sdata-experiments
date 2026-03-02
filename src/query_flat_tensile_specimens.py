from __future__ import annotations

import argparse
from pathlib import Path

from rdflib import Graph


def build_query(target_width_mm: float, tolerance_mm: float) -> str:
    return f"""
PREFIX stsp: <https://w3id.org/sdata/tensile/specimens/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>

SELECT ?profile ?label ?w
WHERE {{
  ?profile a skos:Concept ;
           skos:broader stsp:flat ;
           skos:prefLabel ?label ;
           stsp:w ?w .

  FILTER(ABS(xsd:decimal(?w) - {target_width_mm}) <= {tolerance_mm})
}}
ORDER BY ?w
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Filter flat tensile specimen profiles by width in mm."
    )
    parser.add_argument(
        "--ttl",
        type=Path,
        default=Path("tensiletest/sdata-tensile-specimens.ttl"),
        help="Path to Turtle vocabulary file (default: tensiletest/sdata-tensile-specimens.ttl).",
    )
    parser.add_argument(
        "--target-width",
        type=float,
        default=20.0,
        help="Target width in mm (default: 20.0).",
    )
    parser.add_argument(
        "--tolerance",
        type=float,
        default=1.0,
        help="Tolerance in mm (default: 1.0).",
    )
    args = parser.parse_args()

    graph = Graph()
    graph.parse(args.ttl, format="turtle")

    query = build_query(args.target_width, args.tolerance)
    rows = list(graph.query(query))

    print(
        f"Flat specimen profiles with width {args.target_width:.3f} mm "
        f"+/- {args.tolerance:.3f} mm"
    )
    if not rows:
        print("No matches.")
        return 0

    for row in rows:
        profile = str(row.profile)
        label = str(row.label)
        width = float(row.w)
        print(f"- {label} ({profile}) -> w={width:.4f} mm")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
