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

def generate_question_for_topic(topicId: str, difficulty: str):
    if topicId == "A.5A":  # Solve Linear Equations
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        x = random.randint(1, 10)
        c = a * x + b
        question = f"{a}x + {b} = {c}"
        answer = x
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.3C":  # Graph Linear Functions
        m = random.randint(-5, 5)
        b = random.randint(-5, 5)
        question = f"What is the slope and y-intercept of the function y = {m}x + {b}?"
        answer = {"slope": m, "y_intercept": b}
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.5C":  # Solve Systems of Equations
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        a1, b1 = random.randint(1, 5), random.randint(1, 5)
        a2, b2 = random.randint(1, 5), random.randint(1, 5)
        c1 = a1 * x + b1 * y
        c2 = a2 * x + b2 * y
        eq1 = f"{a1}x + {b1}y = {c1}"
        eq2 = f"{a2}x + {b2}y = {c2}"
        question = f"Solve the system:\n1) {eq1}\n2) {eq2}"
        answer = {"x": x, "y": y}
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.8A":  # Solve Quadratic Equations
        x1 = random.randint(1, 5)
        x2 = random.randint(1, 5)
        question = f"Solve the equation: (x - {x1})(x - {x2}) = 0"
        answer = sorted([x1, x2])
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.9A":  # Exponential Functions
        a = random.randint(1, 5)
        r = random.randint(2, 5)
        question = f"What is the value of the exponential function f(x) = {a} * {r}^x when x = 2?"
        answer = a * (r ** 2)
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.10A":  # Add/Subtract Polynomials
        question = "Simplify: (3x^2 + 2x - 5) + (2x^2 - 3x + 7)"
        answer = "5x^2 - x + 2"
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.11A":  # Simplify Radical Expressions
        question = "Simplify: √(49)"
        answer = 7
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.12A":  # Determine Functions
        question = "Is the relation {(1, 2), (2, 3), (3, 4), (1, 5)} a function?"
        answer = "No"  # x=1 repeats
        return {"question": question, "answer": answer, "difficulty": difficulty}

    # fallback
    return {
        "question": "No question generator implemented yet for this topic.",
        "answer": None,
        "difficulty": difficulty
    }


# For local testing (optional)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("teks_algebra_1_backend:app", host="0.0.0.0", port=8000, reload=True)
