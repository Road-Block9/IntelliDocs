# Tri9T AI CT-200 Backend

Backend for the CardioTrack CT-200 manual engineering assignment. Module 0
contains only the application scaffold, configuration, database foundation,
health endpoint, and basic tests. PDF ingestion and all domain features are
intentionally deferred.

## Prerequisites

- Python 3.11 or newer
- Git (repository initialization and commits are managed manually)

MongoDB and LLM credentials are optional in Module 0. The app does not contact
either service during startup or health checks.

## Setup

On PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

The default relational database is the local SQLite file `ct200.db`. Creating
an engine does not create or connect to MongoDB. Keep real credentials only in
the ignored `.env` file.

## Run the API

```powershell
python -m uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/health`. Expected response:

```json
{
  "status": "ok",
  "application": "Tri9T AI CT-200 Backend",
  "environment": "development"
}
```

Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Run tests

```powershell
python -m pytest
```

The tests verify the health endpoint and confirm optional MongoDB and LLM
credentials are not required.

## Current limitations

- No PDF extraction, OCR, hierarchy reconstruction, or ingestion exists yet.
- No document, version, node, selection, or generation models exist yet.
- MongoDB and LLM settings are placeholders and no clients are initialized.
- Database migrations and production deployment configuration are not included.
