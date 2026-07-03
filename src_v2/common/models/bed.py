from pydantic import BaseModel

class BedAssignment(BaseModel):
    unit: str
    room: str
    bed: str
    status: str