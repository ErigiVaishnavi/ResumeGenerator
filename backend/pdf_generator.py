from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from database import resume_collection
import os
from bson import ObjectId  # Import this to convert the string ID
from fpdf import FPDF

router = APIRouter()

# 📂 Ensure PDF storage directory exists
PDF_DIR = "generated_pdfs"
os.makedirs(PDF_DIR, exist_ok=True)

@router.get("/resume/{resume_id}/download", response_class=FileResponse)
async def download_resume(resume_id: str):
    """Generate and return a PDF resume"""
    try:
        object_id = ObjectId(resume_id)  # Convert string to ObjectId
    except:
        raise HTTPException(status_code=400, detail="Invalid Resume ID format")

    resume = resume_collection.find_one({"_id": object_id})
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found in the database")

    pdf_file = os.path.join(PDF_DIR, f"{resume_id}.pdf")

    #  Check if the PDF file exists before returning
    if not os.path.exists(pdf_file):
        print(f"❌ PDF File Not Found: {pdf_file}")
        raise HTTPException(status_code=404, detail="Generated PDF not found on the server")

    print(f"✅ Serving PDF File: {pdf_file}")
    return FileResponse(pdf_file, filename="Resume.pdf", media_type="application/pdf")


def generate_pdf(resume, pdf_file):
    """ Generate a PDF resume using FPDF """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Resume", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Name: {resume['name']}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {resume['email']}", ln=True)
    pdf.cell(200, 10, txt=f"Phone: {resume['phone']}", ln=True)
    pdf.cell(200, 10, txt=f"Address: {resume['address']}", ln=True)
    pdf.cell(200, 10, txt=f"Education: {resume['education']}", ln=True)
    pdf.cell(200, 10, txt=f"Experience: {resume['experience']}", ln=True)
    pdf.cell(200, 10, txt=f"Skills: {resume['skills']}", ln=True)
    pdf.cell(200, 10, txt=f"Projects: {resume['projects']}", ln=True)

    pdf.output(pdf_file)    
    
    print(f"✅ PDF Successfully Generated: {pdf_file}")


