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

def generate_question (topicId: str, difficulty: str):
def generate_question_for_topic(topicId: str, difficulty: str):
    if topicId == "A.5A":  # Solve Linear Equations
        if difficulty == 'easy':
            x = random.randint(1, 10)
            a = random.randint(1, 5)
            b = a * x
            question = f"Solve: {a}x = {b}"
            answer = x
        elif difficulty == 'medium':
            x = random.randint(1, 10)
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            c = a * x + b
            question = f"Solve: {a}x + {b} = {c}"
            answer = x
        else:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            x = random.randint(1, 10)
            c = a * x + b
            d = a * x
            question = f"Solve: {a}x + {b} = {d + b}"
            answer = x
        return {"question": question, "answer": round(answer, 2), "difficulty": difficulty}

    elif topicId == "A.3C":  # Graph Linear Functions
        m = random.randint(-5, 5)
        b = random.randint(-10, 10)
        question = f"What is the y-intercept of y = {m}x + {b}?"
        return {"question": question, "answer": b, "difficulty": difficulty}

    elif topicId == "A.3D":  # Graph Linear Inequalities
        m = random.randint(-3, 3)
        b = random.randint(-5, 5)
        inequality = random.choice(["<", "<=", ">", ">="])
        question = f"Graph the inequality: y {inequality} {m}x + {b}. What is the boundary line equation?"
        return {"question": question, "answer": f"y = {m}x + {b}", "difficulty": difficulty}

    elif topicId == "A.5C":  # Solve Systems of Equations
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        a1, b1 = random.randint(1, 5), random.randint(1, 5)
        a2, b2 = random.randint(1, 5), random.randint(1, 5)
        c1 = a1 * x + b1 * y
        c2 = a2 * x + b2 * y
        question = f"Solve the system:\n{a1}x + {b1}y = {c1}\n{a2}x + {b2}y = {c2}"
        answer = f"x = {x}, y = {y}"
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.7A":  # Factor Quadratics
        x1 = random.randint(1, 10)
        x2 = random.randint(1, 10)
        a = 1
        b = -(x1 + x2)
        c = x1 * x2
        question = f"Factor: x^2 + {b}x + {c}"
        answer = f"(x - {x1})(x - {x2})"
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.8A":  # Solve Quadratic Equations
        x1 = random.randint(1, 5)
        x2 = random.randint(1, 5)
        question = f"Solve: x^2 - {(x1 + x2)}x + {x1 * x2} = 0"
        answer = f"x = {x1}, x = {x2}"
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.8C":  # Graph Quadratic Functions
        h = random.randint(-5, 5)
        k = random.randint(-5, 5)
        question = f"What is the vertex of the quadratic function y = (x - {h})^2 + {k}?"
        return {"question": question, "answer": f"({h}, {k})", "difficulty": difficulty}

    elif topicId == "A.9A":  # Exponential Functions
        a = random.randint(1, 3)
        b = random.randint(2, 5)
        question = f"Write the exponential function for initial value {a} and growth factor {b}."
        return {"question": question, "answer": f"y = {a} * {b}^x", "difficulty": difficulty}

    elif topicId == "A.9B":  # Interpret Scatterplots
        question = "What does a positive correlation in a scatterplot indicate?"
        return {"question": question, "answer": "As x increases, y increases", "difficulty": difficulty}

    elif topicId == "A.10A":  # Add/Subtract Polynomials
        question = "Simplify: (3x^2 + 2x + 1) + (2x^2 - x + 4)"
        answer = "5x^2 + x + 5"
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.10B":  # Multiply Polynomials
        question = "Expand: (x + 2)(x + 3)"
        answer = "x^2 + 5x + 6"
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.10C":  # Divide Polynomials
        question = "Divide: (x^2 + 5x + 6) ÷ (x + 2)"
        answer = "x + 3"
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.10F":  # Difference of Squares
        question = "Factor: x^2 - 16"
        answer = "(x - 4)(x + 4)"
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.11A":  # Simplify Radicals
        question = "Simplify: √49"
        answer = "7"
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.11B":  # Simplify Exponents
        question = "Simplify: (x^2)^3"
        answer = "x^6"
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.12A":  # Determine Functions
        question = "Is the relation {(1,2), (2,3), (3,4)} a function?"
        answer = "Yes"
        return {"question": question, "answer": answer, "difficulty": difficulty}

    elif topicId == "A.2B":  # Evaluate Expressions
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        question = f"Evaluate: |{a - b}|"
        answer = abs(a - b)
        return {"question": question, "answer": answer, "difficulty": difficulty}

    else:
        return {"question": "Invalid topic selected.", "answer": "", "difficulty": difficulty}


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
