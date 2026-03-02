# Deployment

## Automatischer Docs-Deploy

Die Dokumentation wird ueber GitHub Actions gebaut und mit dem offiziellen
GitHub-Pages-Deploy (`actions/upload-pages-artifact` + `actions/deploy-pages`)
veroeffentlicht.

Workflow-Datei:

- `.github/workflows/deploy-docs.yml`

## Trigger

Der Workflow startet bei:

- Push auf `main` oder `master`, wenn sich Doku-relevante Dateien aendern
- manuellem Start (`workflow_dispatch`)

## Build-Pipeline

1. Checkout Repository
2. Setup Python `3.12`
3. Setup `uv`
4. Install Docs-Dependencies
5. `mkdocs build --strict`
6. Upload von `site/` als Pages-Artifact
7. Deploy auf GitHub Pages

## GitHub Pages Einstellungen

Im GitHub-Repository muss Pages auf `Source: GitHub Actions` konfiguriert sein.
