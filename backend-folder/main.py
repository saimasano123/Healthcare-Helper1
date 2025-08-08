from fastapi import FastAPI
from routers import insurance, nlp  # dono routers import kar liye

app = FastAPI(
    title="Healthcare AI Assistant Backend",
    description="API backend for insurance analysis and cost comparison",
    version="1.0"
)

app.include_router(insurance.router, prefix="/api/insurance", tags=["Insurance"])
app.include_router(nlp.router, prefix="/api/nlp", tags=["NLP"])  # nlp router bhi add kar diya

@app.get("/")
def root():
    return {"message": "Backend is working!"}
