from pydantic import BaseModel

class LLMResult(BaseModel):
    smell_type: str
    explanation: str
