from fastapi import FastAPI
import requests

app = FastAPI()

OLLAMA_URL = "http://ollama:11434/api/generate"

@app.get("/")
def home():
    return {"message": "LLM API Running"}

@app.post("/ask")
def ask_llm(prompt: str):
    response = requests.post(OLLAMA_URL, json={
        "model": "phi",
        "prompt": prompt,
        "stream": False
    })
    return response.json()
