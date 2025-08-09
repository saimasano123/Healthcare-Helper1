from datetime import datetime, timezone
import uuid

timestamp = datetime.now(timezone.utc).isoformat()

def log_chunk(data, source, query_term):
    return {
        "chunk_id": str(uuid.uuid4()),
        "timestamp": timestamp,
        "source": source,
        "query": query_term,
        "record_count": len(data),
        "metadata": {
            "fields": list(data[0].keys()) if data else [],
            "tags": ["drug_label", "fda_api", query_term.lower()]
        },
        "data": data
    }
