from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
import random
import json

app = FastAPI()

# Load topics from topics.json
try:
    with open("topics.json") as f:
        topics = json.load(f)
except FileNotFoundError:
    topics = []

@app.get("/")
def home():
    return {"message": "TEKS Algebra 1 Backend is running."}

@app.get("/api/topics")
def get_topics():
    return {"topics": topics}

# Dummy quiz generator using topicId
@app.get("/api/generate-quiz/{topic_id}")
def generate_quiz(topic_id: str):
    matching_topics = [t for t in topics if t["id"] == topic_id]
    if not matching_topics:
        raise HTTPException(status_code=404, detail="Topic not found")

    # This would be replaced with real question logic per topic
    difficulties = ['easy'] * 10 + ['medium'] * 10 + ['hard'] * 5
    random.shuffle(difficulties)
    
    quiz = []
    for diff in difficulties:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        if diff == 'easy':
            question = f"What is {a} + {b}?"
            answer = a + b
        elif diff == 'medium':
            question = f"What is {a * 2} - {b}?"
            answer = a * 2 - b
        else:
            question = f"What is {a} * {b}?"
            answer = a * b
        quiz.append({
            "question": question,
            "answer": answer,
            "difficulty": diff
        })

    return {"topic": matching_topics[0]["name"], "quiz": quiz}
