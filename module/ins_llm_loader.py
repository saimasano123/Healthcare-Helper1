# insurance_llm_loader.py

import os
import pandas as pd
import requests
from PIL import Image
from pdf2image import convert_from_path
import pytesseract

from langchain.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# 🔑 Set your OpenAI API key
import os
openai_api_key = os.getenv("OPENAI_API_KEY")

def load_insurance_data(path: str):
    df = pd.read_csv(path)
    loader = CSVLoader(file_path=path)
    docs = loader.load()
    return df, docs

def chunk_documents(docs, chunk_size=300, chunk_overlap=30):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)

def build_vector_db(chunks):
    embedding = OpenAIEmbeddings()
    db = Chroma.from_documents(chunks, embedding)
    return db.as_retriever(search_kwargs={"k": 3})

def setup_llm_chain(retriever):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def get_drugs_for_symptom(symptom: str):
    url = "https://api.fda.gov/drug/drugsfda.json"
    params = {"search": f"products.active_ingredient:{symptom}", "limit": 10}
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if "results" in data:
            return [item["products"][0]["brand_name"].lower() for item in data["results"]]
    except:
        pass
    return []

def extract_text_from_card(file_path: str):
    if file_path.endswith(".pdf"):
        images = convert_from_path(file_path)
        return "\n".join([pytesseract.image_to_string(img) for img in images])
    else:
        img = Image.open(file_path)
        return pytesseract.image_to_string(img)

def lookup_insurance(df, name_input: str):
    name_input = name_input.lower()
    matches = df[
        df["COMPANY NAME"].str.lower().str.contains(name_input) |
        df["PLAN NAME"].str.lower().str.contains(name_input)
    ]
    return matches

def match_plans_by_symptom(df, drugs):
    if not drugs:
        return pd.DataFrame()
    return df[df["COVERAGE"].str.lower().str.contains('|'.join(drugs))]

# Optional: Add a main() function for CLI or script usage
if __name__ == "__main__":
    # Example usage
    insurance_path = "data/insurance.csv"
    df, docs = load_insurance_data(insurance_path)
    chunks = chunk_documents(docs)
    retriever = build_vector_db(chunks)
    qa_chain = setup_llm_chain(retriever)

    # You can now call lookup_insurance(), get_drugs_for_symptom(), etc.
