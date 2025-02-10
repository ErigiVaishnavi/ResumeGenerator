from pydantic import BaseModel

class Resume(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    education: list
    experience: list
    skills: list
    projects: list
