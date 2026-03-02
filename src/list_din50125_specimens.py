from __future__ import annotations

import argparse
from pathlib import Path

from rdflib import Graph


def build_query() -> str:
    return """
PREFIX stsp: <https://w3id.org/sdata/tensile/specimens/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?profile ?notation ?label ?profileClass ?w ?t ?l0 ?W ?l2 ?lg ?l1 ?lt ?r
WHERE {
  ?profile a skos:Concept ;
           skos:notation ?notation ;
           skos:prefLabel ?label ;
           stsp:profileClass ?profileClass ;
           stsp:w ?w ;
           stsp:t ?t ;
           stsp:l0 ?l0 ;
           stsp:W ?W ;
           stsp:l2 ?l2 ;
           stsp:lg ?lg ;
           stsp:l1 ?l1 ;
           stsp:lt ?lt ;
           stsp:r ?r .

  FILTER(STRSTARTS(STR(?notation), "din50125_"))
}
ORDER BY ?notation
"""


def format_decimal(lit: object) -> str:
    return f"{float(lit):.4f}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="List all DIN 50125 specimen profiles from specimen-shapes vocabulary."
    )
    parser.add_argument(
        "--ttl",
        type=Path,
        default=Path("tensiletest/sdata-tensile-specimens.ttl"),
        help="Path to Turtle vocabulary file (default: tensiletest/sdata-tensile-specimens.ttl).",
    )
    args = parser.parse_args()

    graph = Graph()
    graph.parse(args.ttl, format="turtle")

    rows = list(graph.query(build_query()))

    print("DIN 50125 specimen profiles (all lengths in mm)")
    if not rows:
        print("No DIN 50125 profiles found.")
        return 0

    header = (
        "notation | label | class | w | t | l0 | W | l2 | lg | l1 | lt | r"
    )
    print(header)
    print("-" * len(header))

    for row in rows:
        print(
            " | ".join(
                [
                    str(row.notation),
                    str(row.label),
                    str(row.profileClass),
                    format_decimal(row.w),
                    format_decimal(row.t),
                    format_decimal(row.l0),
                    format_decimal(row.W),
                    format_decimal(row.l2),
                    format_decimal(row.lg),
                    format_decimal(row.l1),
                    format_decimal(row.lt),
                    format_decimal(row.r),
                ]
            )
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
