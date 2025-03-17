from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from schemas.chat import Completion
from agents.coder import pipeline
import marko
    
router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/completion")
async def create_completion(completion:Completion):
    query = completion.query
    response = pipeline(query)
    html_content = marko.convert(response)
    with open("html_response.html", "w") as f:
        f.write(html_content)
    return {
        "status": "OK",
        "message": "saved in /show ur"
    }

@router.get("/show", response_class=HTMLResponse)
async def show():
    with open("html_response.html", "r") as f:
        return f.read()