# Wordle - Cloud-based Wordle Game Application

## READMEs describing the UI and Backend
- UI - ReactJS w/ React Bootstrap and Redux Toolkit
- Backend - python django

## Deployed on GCP using:
- Cloud Run
- Cloud Build
- Cloud SQL
- Cloud Storage
- Container Registry
- Secret Manager

Deployment chart
graph TB
    A[Local Machine] -->|Build| B(Cloud Build)
    B -->|Push container image| C(Container Registry)
    B -->|Store static files| D(Cloud Storage Bucket)
    C -->|Run image| E(Cloud Run)
    D -->|Get static files| E
    E <-->|DB Communication| F[(CloudSQL)]
    G(Secret Manager) -->|Get secrets| E
    E <-->|Send requests| H(Users)

## Group Members:
Adam Kaczmarski
Ayesha Kayani
Vijay Kesireddy
