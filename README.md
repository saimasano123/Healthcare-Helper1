<<<<<<< HEAD
# Healthcare-Helper
A collaborative, modular AI assistant for healthcare cost transparency and insurance analysis. Includes a React frontend, FastAPI backend, and insurance analyzer tools — all in one unified repo for easy development and contribution.

## Repo Structure
healthcare-helper/ 
├── frontend/              
# React UI for user interaction 
├── backend/               
# FastAPI server for API endpoints and orchestration 
├── insurance-analyzer/   
# Python tools for parsing and analyzing insurance data 
├── data-ingestion/       
# Utilities for importing, cleaning, and chunking raw data 
├── vector-db/            
# Embedding and retrieval logic using a vector database 
├── cost-comparison/      
# Engine for comparing healthcare costs across providers 
├── tests/                
# Shared test suite for all modules 
└── README.md 



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

• 	Transparent healthcare cost comparison
• 	Modular architecture for easy contribution
• 	Beginner-friendly onboarding and reproducible environments
• 	Playful, welcoming UI design






=======
# Healthcare AI Assistant – Frontend

A simple, visually appealing React.js frontend for interacting with our Healthcare-Helper AI Assistant. Users can submit natural language queries and optionally upload insurance documents for analysis. The assistant returns grounded, data-informed responses via a FastAPI backend.

---

## Features

- Natural language query input
- Insurance document upload (OCR-ready)
- Integration with FastAPI backend
- Clean, responsive UI with minimal dependencies

---

## Tech Stack

| Layer       | Tool/Library         |
|-------------|----------------------|
| Frontend    | React.js             |
| Styling     | CSS (custom)         |
| Backend API | FastAPI              |
| OCR         | Tesseract (backend)  |
| RAG Stack   | LangChain + ChromaDB |
| LLM         | GPT-5 (via API)      |

---

## Installation

```bash
# Clone the repo
git clone https://github.com/prescottcassy/hh-frontend.git
cd hh-frontend

# Install dependencies
npm install

# Start the development server
npm start

# When running test
npm install --save-dev @testing-library/react
```

## Accessibility Considerations

We aim to make this tool inclusive and usable for all users. Planned accessibility enhancements include:

- Ensuring all interactive elements are keyboard-navigable.
- Using semantic HTML tags for better screen reader support.
- Providing clear focus states for buttons and inputs.

## Future Improvements

- Connect the query form to a backend endpoint for real-time AI responses.
- Add drag-and-drop support for file uploads with preview thumbnails.
- Implement form validation and error handling for better UX.
- Add loading indicators and animations to improve feedback.
- Modularize styles using CSS modules or a design system.
- Add unit and integration tests for all components.
- Improve accessibility with keyboard navigation and ARIA attributes.

## Contributor Guidelines

We welcome contributions from classmates and future collaborators! Here's how to get started:

## Coding Style
- Use **functional components** and **React hooks**.
- Keep components **modular** and **single-purpose**.
- Prefer **semantic HTML** and accessible markup.

## Naming Conventions
- Use **PascalCase** for component files (e.g. `QueryForm.jsx`).
- Use **camelCase** for variables and functions.
- Keep filenames descriptive and consistent.

## Questions or Feedback?
Open an issue or reach out to Cassy at **cassy.cormier@icloud.com**
>>>>>>> ddf71eb (Add front end README)

