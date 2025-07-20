from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Query
import random
import json

app = FastAPI()

# Allow CORS from Netlify frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load topics from JSON file
with open("topics.json") as f:
    topics = json.load(f)

@app.get("/")
def home():
    return {
        "message": "TEKS Algebra 1 Backend is running. Use /api/topics to get all topics or /api/generate-quiz?topicId=... to get a quiz."
    }

@app.get("/api/topics")
def get_topics():
    return {"topics": topics}

@app.get("/api/generate-quiz")
def generate_quiz(topicId: str = Query(..., description="Topic ID from topics.json")):
    topic = next((t for t in topics if t["id"] == topicId), None)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    difficulties = ['easy'] * 10 + ['medium'] * 10 + ['hard'] * 5
    random.shuffle(difficulties)
    quiz = [generate_question(topicId, d) for d in difficulties]

    return {
        "topic": topic,
        "quiz": quiz
    }

def generate_question(topicId: str, difficulty: str):
    # Replace this logic with actual TEKS-aligned question generation for the topicId
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    if difficulty == 'easy':
        question = f"{a} + {b}"
        answer = a + b
    elif difficulty == 'medium':
        question = f"{a} * {b}"
        answer = a * b
    else:
        question = f"Solve for x: {a}x + {b} = 0"
        answer = round(-b / a, 2)

    return {
        "topicId": topicId,
        "question": question,
        "answer": answer,
        "difficulty": difficulty
    }

# For local testing (optional)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("teks_algebra_1_backend:app", host="0.0.0.0", port=8000, reload=True)
