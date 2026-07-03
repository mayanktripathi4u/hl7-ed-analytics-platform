from pydantic import BaseModel

class ClinicalStatus(BaseModel):
    status: str
    trauma_alert: bool = False
    stroke_alert: bool = False
    sepsis_alert: bool = False
    behavioral_health: bool = False