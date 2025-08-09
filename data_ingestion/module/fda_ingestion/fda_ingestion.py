import requests
from chunk_logger import log_chunk
from utils.credentials import load_api_config
from faers_ingestion import query_adverse_events
from recall_ingestion import query_drug_recalls

def query_drug_label(search_term, limit=5):
    """
    Query FDA drug labeling API for a given search term.
    """
    config = load_api_config("fda")
    api_key = config["api_key"]
    base_url = config["base_url"]

    if not api_key or not base_url:
        raise EnvironmentError("Missing FDA API credentials. Check your .env or api_keys.env file.")

    endpoint = f"{base_url}/drug/label.json"
    params = {
        "search": search_term,
        "limit": limit,
        "api_key": api_key
    }

    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"FDA Drug Labeling error: {response.status_code} - {response.text}")

def extract_drug_info(results):
    """
    Extract relevant fields from FDA drug label results.
    """
    extracted = []
    for item in results.get("results", []):
        openfda = item.get("openfda", {})
        data = {
            "generic_name": openfda.get("generic_name", [""])[0],
            "brand_name": openfda.get("brand_name", [""])[0],
            "purpose": item.get("purpose", [""])[0],
            "warnings": item.get("warnings", [""])[0],
            "dosage": item.get("dosage_and_administration", [""])[0]
        }
        extracted.append(data)
    return extracted

if __name__ == "__main__":
    drug = "ibuprofen"

    # Drug Labeling
    label_raw = query_drug_label(drug)
    label_cleaned = extract_drug_info(label_raw)
    label_chunk = log_chunk(label_cleaned, source="FDA Drug Labeling", query_term=drug)

    print(f"\nDrug Label Chunk: {label_chunk['chunk_id']}")
    for entry in label_chunk["data"]:
        print(f"{entry['generic_name']} ({entry['brand_name']}): {entry['purpose']}")

    # FAERS Adverse Events
    faers_raw = query_adverse_events(drug)
    faers_chunk = log_chunk(faers_raw.get("results", []), source="FAERS", query_term=drug)

    # Drug Recalls
    recall_raw = query_drug_recalls(drug)
    recall_chunk = log_chunk(recall_raw.get("results", []), source="Drug Recalls", query_term=drug)

    # Summary
    print(f"\nFAERS chunk: {faers_chunk['chunk_id']} - {faers_chunk['record_count']} records")
    print(f"Recalls chunk: {recall_chunk['chunk_id']} - {recall_chunk['record_count']} records")