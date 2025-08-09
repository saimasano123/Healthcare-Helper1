import os
import requests
from dotenv import load_dotenv
from chunk_logger import log_chunk
from config_loader import API_KEY, BASE_URL



def query_drug_recalls(search_term, limit=5):
    endpoint = f"{BASE_URL}/drug/enforcement.json"
    params = {
        "search": f"product_description:{search_term}",
        "limit": limit,
        "api_key": API_KEY
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"FDA Recall error: {response.status_code} - {response.text}")
    
