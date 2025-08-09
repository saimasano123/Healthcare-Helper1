from ingest import ingest_documents
from chunker import chunk_documents
from embedder import embed_chunks
from export import export_to_json

def run_pipeline(input_path: str, output_path: str):
    docs = ingest_documents(input_path)
    chunks = chunk_documents(docs)
    embedded = embed_chunks(chunks)
    export_to_json(embedded, output_path)

if __name__ == "__main__":
    run_pipeline("data/raw", "data/processed/output.json")
