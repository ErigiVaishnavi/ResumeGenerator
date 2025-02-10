from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.resume import router as resume_router  
from pdf_generator import router as pdf_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)

# API routes
app.include_router(resume_router, prefix="/resume", tags=["resume"])
app.include_router(pdf_router, prefix="/pdf", tags=["pdf"])

@app.get("/")
def home():
    return {"message": "Resume Generator API is running!"}
