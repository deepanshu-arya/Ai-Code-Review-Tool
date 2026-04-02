from pydantic import BaseModel

class CodeRequest(BaseModel):
    code: str

class CodeResponse(BaseModel):
    review: str
    score: str
    improved_code: str
    language: str