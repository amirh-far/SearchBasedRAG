from pydantic import BaseModel

class Completion(BaseModel):
    query: str

