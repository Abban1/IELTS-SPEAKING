# main.py (partial)
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from utils import generate_ielts_speaking
from database import speaking_collection
from datetime import datetime

app = FastAPI(title="IELTS Speaking Test Generator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate-speaking")
def generate_speaking(
    level: str = Query("Academic", description="Academic or General"),
    context_question: str = Query(None, description="Reference context for Part 2 and Part 3")
):
    # Generate task
    prompt = generate_ielts_speaking(level, context_question)

    # Save to MongoDB
    document = {
        "level": level,
        "context_question": context_question,
        "questions": prompt,
        "created_at": datetime.utcnow()
    }
    result = speaking_collection.insert_one(document)

    return {
        "success": True,
        "id": str(result.inserted_id),
        "level": level,
        "context_question": context_question,
        "questions": prompt
    }
