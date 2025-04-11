from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from fstapi.schemas.chat import Completion
from agents.coder import pipeline
import marko
import json
from json2html import *

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/completion")
async def create_completion(completion:Completion):
    query = completion.query
    response, rag_context, web_res = pipeline(query)
    html_content = marko.convert(response)
    html_content += "<br><br>"
    html_content += "<h2>RAG Context</h2>"
    html_content += "<h3>Local Database Search</h3>"
    html_content += marko.convert(rag_context)
    html_content += "<h3>Web Search Results</h3>"

    web_text = ""
    for result in web_res:
        for key, value in result.items():
            web_text += f"### {key}\n {value}\n\n"
        web_text += "----\n"

    html_content += marko.convert(web_text)

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