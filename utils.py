import os
import fitz  # PyMuPDF
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("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")

def extract_text_from_pdf(file_path):
    file_path = os.path.join(os.path.dirname(__file__), "brochure-general-housing-allowance.pdf")
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text