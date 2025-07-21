from fastapi import FastAPI, Query
from app.llm_handler import generate_response

app = FastAPI()

@app.get("/chat")
def chat(query: str = Query(..., description="Kullanıcının mesajı")):
    response = generate_response(query)
    return {"response": response}
