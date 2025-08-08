# Inusrance-Plan-Analyzer
Insurance Analyzer using OCR
This project extracts insurance information (deductible, copay, coverage, etc.) from uploaded documents using OCR and Python.
## Features
- OCR using Tesseract (in Colab)
- Regex-based field extraction
- Returns structured insurance details

## Getting Started
1. Open `notebooks/ocr_extraction_demo.ipynb` in Google Colab
2. Upload a sample image or insurance document
3. Run the notebook and review the extracted output


### Installation
No local installation needed. The project runs fully on Google Colab.

### Usage
1. Open the notebook at `notebooks/ocr_extraction.ipynb` in Google Colab:  
   [Open in Colab](https://colab.research.google.com/github/saimasano123/Inusrance-Plan-Analyzer/blob/main/notebooks/ocr_extraction.ipynb)
2. Upload a sample insurance document image (photo or scanned PDF converted to image).
3. Run all notebook cells sequentially to perform OCR and extract insurance fields.
4. Review the extracted data displayed in the output cells.

### Example Fields Extracted
- Plan Type (e.g., PPO, HMO)
- Deductible amounts
- Copay details
- Out-of-pocket Maximums

## Sample Input
Place sample insurance card images in the `data/` folder or upload directly in Colab.

## How It Works
- Uses Tesseract OCR to convert images to text.
- Applies regex patterns to extract specific insurance information from raw OCR text.
- Structures the extracted data for further analysis or visualization.

### Install Tesseract OCR

This project requires the Tesseract OCR engine to be installed on your system.

- **Windows:** Download and install from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
- **macOS:** Use Homebrew to install  
  ```bash
  brew install tesseract
