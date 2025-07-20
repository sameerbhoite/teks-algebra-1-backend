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
    with open("topics.json") as f:
        topics = json.load(f)
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
    if topicId == "A.5A":
        return generate_solve_linear_equation(difficulty)
    # Add more topics here...
    return {"question": "No questions available", "answer": None, "difficulty": difficulty}


def generate_solve_linear_equation(difficulty: str):
    import random
    x = random.randint(1, 10)
    if difficulty == "easy":
        a = random.randint(1, 5)
        b = a * x
        question = f"{a}x = {b}"
        answer = x
    elif difficulty == "medium":
        a = random.randint(1, 5)
        b = random.randint(1, 10)
        c = a * x + b
        question = f"{a}x + {b} = {c}"
        answer = x
    else:  # hard
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = a * x + random.randint(1, 5)
        d = b * x + random.randint(1, 5)
        question = f"{a}x + {c - a * x} = {b}x + {d - b * x}"
        answer = x

    return {"question": question, "answer": answer, "difficulty": difficulty}

# For local testing (optional)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("teks_algebra_1_backend:app", host="0.0.0.0", port=8000, reload=True)
