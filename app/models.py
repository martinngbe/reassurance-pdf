from pydantic import BaseModel

class PdfRequest(BaseModel):
    html: str
    filename: str = "document.pdf"
