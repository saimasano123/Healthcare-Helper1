from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import insurance, nlp

app = FastAPI(
    title="Healthcare AI Assistant Backend",
    description="API backend for insurance analysis and cost comparison",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(insurance.router, prefix="/api/insurance", tags=["Insurance"])
app.include_router(nlp.router, prefix="/api/nlp", tags=["NLP"])  # nlp router bhi add kar diya

@app.get("/")
def root():
    return {"message": "Backend is working!"}
    