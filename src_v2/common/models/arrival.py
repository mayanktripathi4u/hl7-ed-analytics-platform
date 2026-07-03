from pydantic import BaseModel
from datetime import datetime

class Arrival(BaseModel):
    method: str
    timestamp: datetime