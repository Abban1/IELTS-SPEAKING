# database.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  # loads MONGO_URI and DB_NAME

MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME", "ielts_db")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Collection for IELTS Speaking tasks
speaking_collection = db["generated_speaking_tasks"]
