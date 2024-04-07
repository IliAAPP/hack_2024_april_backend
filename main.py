from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

app = FastAPI()

model = AutoModelForQuestionAnswering.from_pretrained("facebook/bart-base")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-base")

origins = [
    "http://localhost",
    "http://127.0.0.1:3000",
    "http://10.1.1.31:3000",
    "http://192.168.253.151:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Authorization"],
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}


@app.get("/authorization")
def authorization():
    return {"message": "Authorization"}


@app.post("/routes")
def routes():
    return {"message": "Страница со всеми маршрутами"}


@app.get("/routes/save_routes")
def routes_save_routes():
    return {"message": "Страница с сохранением маршрутов"}


@app.get("/routes/route_data")
def routes_route_data():
    return {"message": "Данные о маршрутах"}


def answer_question(question):
    inputs = tokenizer(question, return_tensors="pt")
    outputs = model(**inputs)
    answer = tokenizer.decode(outputs.start_logits.argmax(-1), skip_special_tokens=True)
    return answer


@app.get("/answer")
async def answer_endpoint(question: str):
    answer = await answer_question(question)
    return {"answer": answer}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run
