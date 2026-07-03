from pydantic import BaseModel

class Triage(BaseModel):
    esi_level: int
    chief_complaint: str
    priority: str