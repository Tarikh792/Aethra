from pypdf import PdfReader

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        text += (page.extract_text() or "") + "\n"

    return text

if __name__ == "__main__":
    text = extract_text("sample.pdf")
    print(text[:500])