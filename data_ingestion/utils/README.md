# Utilities Overview

This folder contains reusable modules that support ingestion, tagging, logging, and credential management for the Healthcare Helper pipeline. Each utility is designed to be modular, auditable, and team-friendly.

---

## Modules

### `chunk_logger.py`
Logs metadata for each ingested chunk, including:
- Chunk ID
- Source dataset
- Timestamp
- Traceability tags

Outputs to `logs/chunk_ids.csv` for auditability.

---

### `tagger.py`
Adds metadata tags to chunks based on:
- Source type (e.g. CMS, FDA)
- Ingestion context
- Config-driven rules

Used to enrich chunks before PDF generation or dashboard rendering.

---

### `credentials.py`
Handles secure loading of API keys and environment variables from:
- `utils/api_keys.env`
- `.env` files (if present)

Includes validation logic to prevent missing or malformed credentials.

---

## Other Files

### `api_keys.env`
Stores API keys for local development. **Do not commit this file.**

### `requirements.txt`
Lists Python dependencies used across utilities. This file is now duplicated at the project root for convenience.

### `__init__.py`
Marks this folder as a Python package. You can import utilities like:

```python
from utils.chunk_logger import log_chunks