# Script to ingest clinical doctor notes

import pandas as pd
import uuid
import logging
import os
import re
from ...test_rtf import rtf_to_txt as rtf_to_text
from ...utils.export import export_chunks_to_json

DATASETS_DIR = os.path.join("data_ingestion", "dataset")

logger = logging.getLogger(__name__)

def chunk_clinical_note(note: str) -> dict:
    sections = {}
    pattern = r"(History|Assessment|Plan|Impression|Chief Complaint):"

    matches = list(re.finditer(pattern, note, flags=re.IGNORECASE))
    for i, match in enumerate(matches):
        section_name = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(note)
        section_text = note[start:end].strip()
        sections[section_name.lower()] = section_text

    if not sections:
        sections["full_note"] = note.strip()

    return sections

def parse_notes_from_folder(folder_path):
    ingested_chunks = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Handle structured tabular data
        if filename.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif filename.endswith(".jsonl"):
            df = pd.read_json(file_path, lines=True)
        elif filename.endswith(".rtf"):
            with open(file_path, encoding="utf-8", errors="ignore") as f:
                rtf_content = f.read()
                note = rtf_to_text(rtf_content).strip()

                if note:
                    section_chunks = chunk_clinical_note(note)
                    for section, section_text in section_chunks.items():
                        chunk = {
                            "text": section_text,
                            "metadata": {
                                "source_file": filename,
                                "note_type": section,
                                "chunk_id": str(uuid.uuid4()),
                                "section": section
                            }
                        }
                        ingested_chunks.append(chunk)
            continue  # Skip tabular processing for RTF files
        else:
            logger.warning(f"Unsupported format: {filename}")
            continue

        # Process each note in tabular data
        for _, row in df.iterrows():
            note = row.get("clinical_note", "").strip()
            if note:
                section_chunks = chunk_clinical_note(note)
                for section, section_text in section_chunks.items():
                    chunk = {
                        "text": section_text,
                        "metadata": {
                            "patient_id": row.get("patient_id", "unknown"),
                            "note_type": row.get("note_type", section),
                            "timestamp": row.get("timestamp", None),
                            "chunk_id": str(uuid.uuid4()),
                            "section": section
                        }
                    }
                    ingested_chunks.append(chunk)

    return ingested_chunks

def ingest_local_rtf_notes():
    """
    Ingests all .rtf files in the local data_ingestion/dataset directory,
    extracts text, chunks notes, and exports to JSON.
    """
    rtf_dir = os.path.join("data_ingestion", "dataset")
    ingested_chunks = []

    for filename in os.listdir(rtf_dir):
        if filename.endswith(".rtf"):
            file_path = os.path.join(rtf_dir, filename)
            with open(file_path, encoding="utf-8", errors="ignore") as f:
                rtf_content = f.read()
                note = rtf_to_text(rtf_content).strip()
                if note:
                    section_chunks = chunk_clinical_note(note)
                    for section, section_text in section_chunks.items():
                        chunk = {
                            "text": section_text,
                            "metadata": {
                                "source_file": filename,
                                "note_type": section,
                                "chunk_id": str(uuid.uuid4()),
                                "section": section
                            }
                        }
                        ingested_chunks.append(chunk)

    logger.info(f"Ingested {len(ingested_chunks)} notes.")
    export_chunks_to_json(ingested_chunks, output_path="output/clinical_chunks.json")
    return ingested_chunks

if __name__ == "__main__":
    all_chunks = ingest_local_rtf_notes()
    print(f"Ingested {len(all_chunks)} clinical note chunks.")


