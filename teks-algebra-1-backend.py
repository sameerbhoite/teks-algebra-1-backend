from fastapi import FastAPI
import random
import sys

app = FastAPI()

def generate_linear_equation(difficulty):
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    if difficulty == 'easy':
        question = f"{a} + {b}"
        answer = a + b
    elif difficulty == 'medium':
        a *= 2
        b *= 3
        question = f"{a} - {b}"
        answer = a - b
    else:  # hard
        a *= random.randint(2, 5)
        b *= random.randint(2, 5)
        question = f"{a} * {b}"
        answer = a * b

    return {"question": question, "answer": round(answer, 2), "difficulty": difficulty}

@app.get("/")
def home():
    return {
        "message": "TEKS Algebra 1 Backend is running. Use /api/generate-weekly-quiz to get a quiz."
    }

@app.get("/api/generate-weekly-quiz")
def generate_weekly_quiz():
    quiz = []
    difficulties = ['easy'] * 10 + ['medium'] * 10 + ['hard'] * 5
    random.shuffle(difficulties)

    for diff in difficulties:
        quiz.append(generate_linear_equation(diff))

    return {"quiz": quiz}

@app.get("/api/python-version")
def get_python_version():
    return {"python_version": sys.version}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("teks_algebra_1_backend:app", host="0.0.0.0", port=8000, reload=True)