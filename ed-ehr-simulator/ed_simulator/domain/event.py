from dataclasses import dataclass
from datetime import datetime

@dataclass(order=True)
class Event:
    """
    Core ED event flowing through the system.
    This becomes Kafka/PubSub payload later.
    """
    timestamp: datetime
    sequence: int

    patient_id: str
    encounter_id: str
    event_type: str

    facility_id: str