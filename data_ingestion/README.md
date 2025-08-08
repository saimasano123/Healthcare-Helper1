# Healthcare Helper: Data Ingestion

## Data Ingestion Module – Healthcare AI Assistant

This module ingests structured healthcare datasets such as CMS procedure cost data and FDA adverse event reports. It is designed for modularity, metadata-rich logging, and secure credential handling to support downstream RAG integration.

---

## Folder Structure

healthcare-helper-data-ingestion/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── config/
│   ├── endpoints.yaml
├── dataset/
│   └── Sample Physicial Clinical Note
├── logs/
│   └── chunk_ids.csv
├── utils/
│   ├── README
│   ├── tagger
│   ├── api_keys
│   ├── export
│   ├── chunk_logger
│   └── credentials
├── test_rtf
├── requirements
├── README
└── main

## Key Functionalities

- Load source-specific configurations via `.env` and `config_loader.py`
- Ingest data from local files, remote URLs, or API endpoints
- Validate schemas and gracefully handle missing/malformed fields
- Chunk ingested data for RAG-ready storage and retrieval
- Log chunk-level metadata for traceability and auditability

---

## Usage

Ensure your `.env` file contains required environment variables. Example:

```env
CMS_API_KEY=your_key_here
FDA_API_KEY=your_key_here
```

Then run the pipeline:

```bash
python main.py
```

---

## Contributors

- Cassy Cormier

---

## Contributing

1. Fork the repo and clone your fork locally.
2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the pipeline or test modules using sample data in `data/`.
4. Submit a pull request with a clear description of your changes.

---

## Clone the Repository

```bash
git clone https://github.com/your-username/healthcare-helper-data-ingestion.git
cd healthcare-helper-data-ingestion
```

> Replace `your-username` with your actual GitHub username or organization name.

---

## Required Python Modules

Make sure you have Python 3.9+ installed. Then install dependencies:

```bash
pip install -r requirements.txt
```

If you're not using a virtual environment yet, it's recommended:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

## Key Dependencies

| Module           | Purpose                                                  |
|------------------|----------------------------------------------------------|
| `pandas`         | Data manipulation and cleaning                           |
| `requests`       | API calls to CMS and other data sources                  |
| `PyYAML`         | Configuration loading from `.yaml` files                 |
| `python-dotenv`  | Secure handling of environment variables and API keys    |
| `loguru`         | Structured logging with traceability                     |
| `reportlab`      | PDF generation for coverage summaries and ingestion reports |
| `qrcode`         | Embedding QR codes into PDFs                             |
| `fastapi`        | Optional: for serving ingestion status or metadata via a local API |

---

## 🧾 Configuration

- **Endpoints**: Defined in `config/endpoints.yaml`
- **Credentials**: Stored in `utils/api_keys.env` and `config/fda_api.env`
- **Logging**: Outputs to `logs/chunk_ids.csv` for traceability

---

<<<<<<< HEAD
## 🛠Utilities
=======
## Running the Ingestion Pipeline
To execute the FDA ingestion pipeline from PowerShell, set the PYTHONPATH to the project root so that top-level folders like module/ and utils/ are properly recognized:

```powershell
$env:PYTHONPATH = "."
python module\fda_ingestion\fda_ingestion.py
```

```bash
export PYTHONPATH=.
python module/fda_ingestion/fda_ingestion.py
```

This ensures that imports like from chunk_logger import log_chunk resolve correctly across the project.

## Utilities
>>>>>>> 22566e9635f4d9906a33fcc88212b9b8a255fb79

All reusable modules live in `utils/`:

| File                | Purpose                                  |
|---------------------|------------------------------------------|
| `chunk_logger.py`   | Logs chunk metadata and trace IDs        |
| `tagger.py`         | Adds metadata tags to ingested chunks    |
| `credentials.py`    | Loads and validates API keys securely    |
| `config_loader.py`  | Loads YAML-based ingestion configs       |

---

## Repo Hygiene

- Logs and processed data are excluded via `.gitignore`
- Credentials are stored in `.env`-style files and **never committed**
- Modular utilities are documented and reusable

---

## Dev Container Support

This repo includes a `.devcontainer` setup for reproducible, VM-like environments in VS Code. Just open the folder in a container and you're ready to go — no local Python required.

---

