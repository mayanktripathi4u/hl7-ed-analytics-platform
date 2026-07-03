from datetime import datetime, timedelta

from pathlib import Path
import sys
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.models.event import Event #EncounterEvent, EventType

class TimelineEngine:
    # def build(self, start: datetime):
    #     return [
    #         EncounterEvent(
    #             sequence=1,
    #             timestamp=start,
    #             event_type=EventType.ARRIVAL,
    #             hl7_event="ADT^A01",
    #             description="Patient arrived"
    #         ),
    #         EncounterEvent(
    #             sequence=2,
    #             timestamp=start + timedelta(minutes=4),
    #             event_type=EventType.TRIAGE,
    #             hl7_event="ADT^A08",
    #             description="Triage completed"
    #         ),
    #         EncounterEvent(
    #             sequence=3,
    #             timestamp=start + timedelta(minutes=9),
    #             event_type=EventType.BED_ASSIGNED,
    #             hl7_event="ADT^A08",
    #             description="Bed assigned"
    #         ),
    #         EncounterEvent(
    #             sequence=4,
    #             timestamp=start + timedelta(minutes=13),
    #             event_type=EventType.PROVIDER_ASSIGNED,
    #             hl7_event="ADT^A08",
    #             description="Provider assigned"
    #         ),
    #         EncounterEvent(
    #             sequence=5,
    #             timestamp=start + timedelta(minutes=18),
    #             event_type=EventType.TREATMENT_STARTED,
    #             hl7_event="ADT^A08",
    #             description="Treatment started"
    #         ),
    #         EncounterEvent(
    #             sequence=6,
    #             timestamp=start + timedelta(minutes=95),
    #             event_type=EventType.DISCHARGE,
    #             hl7_event="ADT^A03",
    #             description="Patient discharged"
    #         )
    #     ]

    def build(self, start: datetime):
        return [
            Event(sequence=1, timestamp=start, name="ARRIVAL", hl7="ADT^A01"),
            Event(sequence=2, timestamp=start + timedelta(minutes=2), name="TRIAGE", hl7="ADT^A08"),
            Event(sequence=3, timestamp=start + timedelta(minutes=5), name="BED_ASSIGNED", hl7="ADT^A08"),
            Event(sequence=4, timestamp=start + timedelta(minutes=8), name="PROVIDER_ASSIGNED", hl7="ADT^A08"),
            Event(sequence=5, timestamp=start + timedelta(minutes=15), name="TREATMENT_STARTED", hl7="ADT^A08"),
            Event(sequence=6, timestamp=start + timedelta(minutes=95), name="DISCHARGE", hl7="ADT^A03"),
        ]
    