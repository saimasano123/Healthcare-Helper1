# Healthcare Helper – Monorepo

A modular AI-powered assistant for healthcare cost transparency and insurance analysis. This monorepo is designed for easy contribution, reproducible development, and clear separation of concerns across frontend, backend, and analysis tools.

---

## Repo Structure
healthcare-helper/ ├
── frontend/              
### React UI for user interaction 
├── backend/               
### FastAPI server for API endpoints and orchestration 
├── insurance-analyzer/   
#### Python tools for parsing and analyzing insurance data 
├── data-ingestion/       
#### Utilities for importing, cleaning, and chunking raw data 
├── vector-db/            
#### Embedding and retrieval logic using a vector database 
├── cost-comparison/      
#### Engine for comparing healthcare costs across providers 
├── tests/                
#### Shared test suite for all modules 
└── README.md 


---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/healthcare-helper.git
cd healthcare-helper
```
### 2. Install dependencies
Each folder is self-contained. Start with:
```
cd frontend
npm install

cd ../backend
pip install -r requirements.txt
```
## Goals
- Transparent healthcare cost comparison
- Modular architecture for easy contribution
- Beginner-friendly onboarding and reproducible environments
- Playful, welcoming UI design

  





