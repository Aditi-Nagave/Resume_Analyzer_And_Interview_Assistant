from pypdf import PdfReader
import docx

def parse_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def parse_docx(file_path):

    doc = docx.Document(file_path)

    return "\n".join(
        [para.text for para in doc.paragraphs]
    )