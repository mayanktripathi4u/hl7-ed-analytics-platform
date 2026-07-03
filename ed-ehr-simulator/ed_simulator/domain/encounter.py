from dataclasses import dataclass

@dataclass
class Encounter:
    encounter_id: str
    patient_id: str

    chief_complaint: str
    arrival_mode: str

    esi_level: int