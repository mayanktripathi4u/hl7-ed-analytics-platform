from dataclasses import dataclass

@dataclass
class Patient:
    patient_id: str
    first_name: str
    last_name: str
    gender: str
    age: int