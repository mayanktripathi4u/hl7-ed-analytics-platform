from pydantic import BaseModel

class Provider(BaseModel):
    id: str
    first_name: str
    last_name: str
    specialty: str