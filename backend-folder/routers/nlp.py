# routers/nlp.py

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class QueryRequest(BaseModel):
    text: str

class EntitiesResponse(BaseModel):
    procedure: str = None
    location: str = None
    insurance: str = None

@router.post("/query", response_model=EntitiesResponse)
async def extract_entities(request: QueryRequest):
    # Yahan apna NER model ya dummy code likho
    # Example dummy return:
    return EntitiesResponse(procedure="knee surgery", location="Dallas", insurance="BlueCross")
