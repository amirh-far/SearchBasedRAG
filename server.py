from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import chat
import uvicorn 


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # or you can specify methods like ["GET", "POST"]
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7007)