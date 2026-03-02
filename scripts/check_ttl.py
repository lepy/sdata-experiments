from __future__ import annotations

from pathlib import Path
import sys

from rdflib import Graph


def iter_ttl_files(root: Path) -> list[Path]:
    return sorted(root.rglob("*.ttl"))


def main() -> int:
    files = iter_ttl_files(Path("."))
    if not files:
        print("No .ttl files found")
        return 0

    failed = False
    for ttl in files:
        try:
            graph = Graph()
            graph.parse(ttl, format="turtle")
            print(f"OK   {ttl}")
        except Exception as exc:  # pragma: no cover
            failed = True
            print(f"FAIL {ttl}: {exc}")

    if failed:
        return 1

    print(f"Parsed {len(files)} Turtle files successfully")
    return 0


if __name__ == "__main__":
    sys.exit(main())
