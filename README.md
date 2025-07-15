# TEKS Algebra 1 Backend

This is the backend for the TEKS Algebra 1 quiz generator app.

## Features

- Generates a weekly quiz with 25 questions
- Follows TEKS Algebra 1 standards with easy, medium, and hard questions
- FastAPI-powered REST API

## Endpoints

- `/` - Returns backend status message.
- `/api/generate-weekly-quiz` - Returns a JSON quiz with 25 randomized Algebra 1 questions.

## How to Deploy (Render.com)

1. Create a new Web Service on [Render](https://render.com/).
2. Connect this GitHub repo.
3. Make sure the root contains:
   - `teks_algebra_1_backend.py`
   - `requirements.txt`
   - `render.yaml`
4. Set environment to Python.
5. Deploy!

## Local Development

```bash
pip install -r requirements.txt
uvicorn teks_algebra_1_backend:app --host 0.0.0.0 --port 8000 --reload
```

## License

MIT License