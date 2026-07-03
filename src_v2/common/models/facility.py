from pydantic import BaseModel

class Facility(BaseModel):
    id: str
    name: str
    city: str
    state: str