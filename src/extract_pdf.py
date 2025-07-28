import pdfplumber
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

def extract_text_from_pdf(pdf_path):
    pages_data = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and text.strip():
                pages_data.append({
                    "page_num": i + 1,
                    "text": text
                })
    return pages_data
