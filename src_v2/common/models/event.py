from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel

# class EventType(str, Enum):
#     ARRIVAL = "ARRIVAL"
#     TRIAGE = "TRIAGE"
#     BED_ASSIGNED = "BED_ASSIGNED"
#     PROVIDER_ASSIGNED = "PROVIDER_ASSIGNED"
#     TREATMENT_STARTED = "TREATMENT_STARTED"
#     LAB_ORDERED = "LAB_ORDERED"
#     IMAGING_ORDERED = "IMAGING_ORDERED"
#     OBSERVATION = "OBSERVATION"
#     ADMISSION = "ADMISSION"
#     TRANSFER = "TRANSFER"
#     DISCHARGE = "DISCHARGE"


# class EncounterEvent(BaseModel):
#     sequence: int
#     timestamp: datetime
#     event_type: EventType
#     hl7_event: str
#     description: str

class Event(BaseModel):
    sequence: int
    timestamp: datetime
    name: str
    hl7: str