from pymongo import MongoClient

MONGO_URI = "mongodb+srv://vaishnavi:mongodb@cluster0.vpysv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["resume_db"]
resume_collection = db["resumes"]



