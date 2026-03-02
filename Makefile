SHELL := /bin/bash

UV ?= uv
PYTHON_VERSION ?= 3.12

.PHONY: help venv sync sync-dev sync-docs test docs-serve docs-build ttl-check check clean

help:
	@echo "Available targets:"
	@echo "  make venv        - create .venv with Python $(PYTHON_VERSION)"
	@echo "  make sync        - install project + dev + docs groups"
	@echo "  make sync-dev    - install project + dev group"
	@echo "  make sync-docs   - install project + docs group"
	@echo "  make test        - run pytest"
	@echo "  make docs-serve  - serve MkDocs locally"
	@echo "  make docs-build  - build MkDocs site"
	@echo "  make ttl-check   - parse all Turtle files with rdflib"
	@echo "  make check       - run test + ttl-check + docs-build"
	@echo "  make clean       - remove build/test caches"

venv:
	$(UV) venv --python $(PYTHON_VERSION) .venv

sync:
	$(UV) sync --python $(PYTHON_VERSION) --group dev --group docs

sync-dev:
	$(UV) sync --python $(PYTHON_VERSION) --group dev

sync-docs:
	$(UV) sync --python $(PYTHON_VERSION) --group docs

test:
	$(UV) run --python $(PYTHON_VERSION) pytest

docs-serve:
	$(UV) run --group docs mkdocs serve

docs-build:
	$(UV) run --group docs mkdocs build --strict

ttl-check:
	$(UV) run --python $(PYTHON_VERSION) python scripts/check_ttl.py

check: test ttl-check docs-build

clean:
	rm -rf .pytest_cache site
