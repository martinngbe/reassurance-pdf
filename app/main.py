from fastapi import FastAPI
from fastapi.responses import Response
from weasyprint import HTML
from app.models import PdfRequest

app = FastAPI(title="Reassurance PDF Service")

@app.post("/generate")
def generate_pdf(req: PdfRequest):
    # WeasyPrint génère le PDF en mémoire (bytes)
    pdf_bytes = HTML(string=req.html).write_pdf()

    # On renvoie le binaire avec les bons headers
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'attachment; filename="{req.filename}"'
        }
    )

@app.get("/health")
def health():
    return {"status": "ok"}
