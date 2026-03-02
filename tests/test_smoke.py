from pathlib import Path


def test_pyproject_exists() -> None:
    assert Path("pyproject.toml").exists()


def test_core_ontology_exists() -> None:
    assert Path("core/sdata-testdata.ttl").exists()
