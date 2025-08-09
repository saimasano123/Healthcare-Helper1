import os
from ingest import ingest_documents
from chunker import chunk_documents
from embedder import embed_chunks
from export import export_to_json

def run_pipeline(input_path: str, output_path: str):
    print("📥 Ingesting documents...")
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input path '{input_path}' does not exist.")

    docs = ingest_documents(input_path)
    print(f"✅ Ingested {len(docs)} documents.")

    print("✂️ Chunking documents...")
    chunks = chunk_documents(docs)
    print(f"✅ Created {len(chunks)} chunks.")

    print("🧠 Embedding chunks...")
    embedded = embed_chunks(chunks)
    print(f"✅ Embedded {len(embedded)} chunks.")

    print("📤 Exporting to JSON...")
    export_to_json(embedded, output_path)
    print(f"✅ Exported to {output_path}")

if __name__ == "__main__":
    run_pipeline("data/raw", "frontend/public/data/output.json")
