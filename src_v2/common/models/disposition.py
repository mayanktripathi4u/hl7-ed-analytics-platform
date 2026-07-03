from pydantic import BaseModel

class Disposition(BaseModel):
    current: str
    expected: str