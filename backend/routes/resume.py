from fastapi import APIRouter, HTTPException
import httpx 
import requests
from models import Resume
from database import resume_collection
from bson import ObjectId

router = APIRouter()

IPSTACK_API_KEY = "d341e8c1c0d4a3ed520f130beeca2b51"

def get_geolocation():
    """Fetches user location from IPStack API"""
    try:
        response = requests.get(f"http://api.ipstack.com/check?access_key={IPSTACK_API_KEY}")
        response.raise_for_status()
        data = response.json()
        return f"{data.get('city', 'Unknown')}, {data.get('region_name', 'Unknown')}, {data.get('country_name', 'Unknown')}"
    except Exception as e:
        print(f"🌍 Error getting location: {e}")
        return "Unknown"

@router.post("/")
async def create_resume(resume: Resume):
    """Stores resume data in MongoDB"""
    try:
        new_resume = resume.dict()
        new_resume["address"] = get_geolocation()  # Async geolocation
       
        print(f"📝 New Resume Data: {new_resume}")  # Check the resume data before saving
        
        result = resume_collection.insert_one(new_resume)
        resume_id = str(result.inserted_id)
        print(f"✅ Resume Saved! ID: {resume_id}")  # Confirm it's saved
        
        return {"message": "Resume Created Successfully!", "resume_id": str(result.inserted_id)}
    except Exception as e:
        print(f"❌ ERROR: {e}")
        raise HTTPException(status_code=500, detail=str(e))
