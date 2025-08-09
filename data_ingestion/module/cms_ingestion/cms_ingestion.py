# Script to ingest cms healthcare data
from urllib import response
import pandas as pd
import requests
import os
import logging
from utils.tagger import tag_chunk
from utils.credentials import load_api_config
from utils.chunk_logger import log_chunk_ids
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_cms_data(prefix="cms_api") -> pd.DataFrame | None:
    config = load_api_config(prefix)
    api_key = config["key"]
    api_url = config["url"]

    if not api_key or not api_url:
        logger.error(f"Missing API config for {prefix}.")
        return None

    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(api_url, headers=headers)

    print(f"[DEBUG] Status Code: {response.status_code}")
    print(f"[DEBUG] Response Text: {response.text[:200]}")  # Preview first 200 chars

    if response.status_code != 200:
        logger.error(f"Failed to fetch CMS data: {response.status_code}")
        return None

    try:
        data = response.json()
        df = pd.DataFrame(data)  # Adjust this if the response is nested
        return df
    except Exception as e:
        logger.exception(f"Error parsing CMS response: {e}")
        return None
    
def safe_float(val):
    try: 
        return float(str(val).strip())
    except (ValueError, TypeError):
        return None
    
def clean_cms_row(row):
    try:
        procedure_code = row.get("HCPCS_CD", "").strip()
        if not procedure_code or procedure_code == "*":
            raise ValueError("Invalid or missing HCPCS_CD")
        
        cost_raw = row.get("PSPS_SUBMITTED_CHARGE_AMT", "").strip()
        cost_avg = safe_float(row.get("PSPS_SUBMITTED_CHARGE_AMT"))
        if cost_avg is None:
            raise ValueError("No cost value")

        return {
            "procedure_name": "", 

            "procedure_code": str(procedure_code).strip(),
            "location": "", 

            "cost_avg": float(row.get("PSPS_SUBMITTED_CHARGE_AMT")),
            "source_name": "CMS",
            "source_url": "https://data.cms.gov"
        }
    except Exception as e:
        logger.warning(f"Skipping row due to error: {e} | Row snapshot: {row}")
        return None


def chunk_and_tag(row):
    """Chunk CMS row into retrievable format."""
    text = f"{row['procedure_name']} typically costs around ${row['cost_avg']} in {row['location']}."
    return tag_chunk(
        text=text,
        procedure_name=row['procedure_name'],
        procedure_code=row['procedure_code'],
        location=row['location'],
        cost_avg=row['cost_avg'],
        source_name=row['source_name'],
        source_url=row['source_url']
    )

def ingest_pipeline():
    """Pipeline for ingesting CMS data exclusively from the API."""
    df = fetch_cms_data("cms_api")

    if df is None:
        logger.error("No data fetched from CMS API. Exiting pipeline.")
        return []

    tagged_chunks = [
        chunk_and_tag(cleaned) 
        for _, row in df.iterrows() 
        if (cleaned := clean_cms_row(row)) is not None 
    ]
    
    log_chunk_ids(tagged_chunks)  # Preserve traceability
    return tagged_chunks

if __name__ == "__main__":
    chunks = ingest_pipeline()
    print(f"Ingested {len(chunks)} tagged chunks.")
