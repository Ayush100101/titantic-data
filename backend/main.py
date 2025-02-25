from fastapi import FastAPI
from pydantic import BaseModel
from data_processor import process_question

app = FastAPI()

class Query(BaseModel):
    question: str

@app.get("/")
async def root():
    return {"message": "Titanic Chatbot API is running! Use /ask/ to interact."}

@app.post("/ask/")
async def ask_question(query: Query):
    return process_question(query.question)
