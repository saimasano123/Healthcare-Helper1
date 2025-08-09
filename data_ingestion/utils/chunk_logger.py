import csv
import uuid
from datetime import datetime

def log_chunk_ids(chunks, logfile="logs/chunk_ids.csv"):
    """Logs chunk_id, procedure_code, and timestamp to CSV."""
    with open(logfile, mode="a", newline="") as file:
        writer = csv.writer(file)
        for chunk in chunks:
            meta = chunk.get("metadata", {})
            writer.writerow([
                meta.get("chunk_id"),
                meta.get("procedure_code"),
                meta.get("retrieved_on", datetime.utcnow().isoformat() + "Z")
            ])


def log_chunk(data, source, query_term):
    """
    Wraps data in a chunk with metadata for traceability.
    """
    chunk_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat() + "Z"

    chunk = {
        "chunk_id": chunk_id,
        "record_count": len(data),
        "metadata": {
            "chunk_id": chunk_id,
            "source": source,
            "query_term": query_term,
            "retrieved_on": timestamp,
            "tags": [source, query_term]
        },
        "data": data
    }

    return chunk
