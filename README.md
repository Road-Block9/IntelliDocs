# Tri9T AI CT-200 Backend

Backend for the CardioTrack CT-200 manual engineering assignment. The current
implementation contains the application scaffold and layout-preserving raw PDF
extraction. PDF interpretation, persistence, and all later domain features are
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
credentials are not required. They also exercise raw extraction with synthetic
PDFs and controlled error cases.

## Extract raw PDF evidence

The extractor records pages, text blocks, bounding boxes, reading order, font
evidence, image counts, selectable-text status, and a conservative OCR-need
signal. It does not classify headings or modify the source PDF.

```powershell
python -m scripts.extract_raw data/ct200_manual.pdf
python -m scripts.extract_raw data/ct200_manual_v2.pdf
```

JSON is written beneath the ignored `generated-output/raw-extraction/`
directory. To request optional OCR, use `--enable-ocr`. OCR is attempted only
on pages that contain images and no selectable text:

```powershell
python -m scripts.extract_raw data/ct200_manual.pdf --enable-ocr
```

Tesseract is optional. If it is unavailable, the JSON and console output state
that clearly while embedded-text extraction continues.

## Current limitations

- OCR candidacy is a conservative generic heuristic: an image-bearing page
  without selectable text. It can miss unusual scans and does not assess text
  quality.
- Font style indicators depend on PDF font flags and font names; mixed-style
  blocks report an indeterminate block-level style while preserving span data.
- Optional OCR requires a working Tesseract installation discoverable on PATH.
- No heading detection, cleanup, hierarchy reconstruction, or ingestion exists.
- No document, version, node, selection, or generation models exist yet.
- MongoDB and LLM settings are placeholders and no clients are initialized.
- Database migrations and production deployment configuration are not included.
