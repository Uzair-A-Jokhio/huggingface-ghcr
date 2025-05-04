from transformers import pipeline 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel 

generator = pipeline('text-generation', model='gpt2')

app = FastAPI()

class Body(BaseModel):
    text: str

@app.get("/")
def root():
    return HTMLResponse("<h1> A Self-documenting API to intreact with gpt2 model and generate text </h1>") 

@app.post("/generate")
def predict(body: Body):
    results = generator(body.text, max_length=32, num_return_sequences=1)
    return results[0]