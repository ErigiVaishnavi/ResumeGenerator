from pydantic import BaseModel

class Resume(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    education: str
    experience: str
    skills: str
    projects: str
    references: str = None
    template: str
    profile_picture: str = None
