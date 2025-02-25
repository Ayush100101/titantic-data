from fastapi import FastAPI
from pydantic import BaseModel
from data_processor import process_question

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask/")
async def ask_question(query: Query):
    question = query.question
    result = process_question(question)
    return result