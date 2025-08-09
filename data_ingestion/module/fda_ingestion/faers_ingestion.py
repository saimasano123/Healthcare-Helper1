import os
import requests
from dotenv import load_dotenv
from chunk_logger import log_chunk
from utils.credentials import load_api_config

def query_adverse_events(search_term, limit=5):
    """
    Query FDA FAERS (adverse event reporting) API for a given drug.
    """
    config = load_api_config("fda")
    api_key = config["api_key"]
    base_url = config["base_url"]

    if not api_key or not base_url:
        raise EnvironmentError("Missing FDA API credentials. Check your .env or api_keys.env file.")

    endpoint = f"{base_url}/drug/event.json"
    params = {
        "search": f"patient.drug.medicinalproduct:{search_term}",
        "limit": limit,
        "api_key": api_key
    }

    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"FDA FAERS error: {response.status_code} - {response.text}")