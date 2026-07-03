from __future__ import annotations
from typing import Optional
from pydantic import BaseModel

class Patient(BaseModel):
    mrn: str
    first_name: str
    last_name: str
    age: int
    gender: str


class Provider(BaseModel):
    id: str
    first_name: str
    last_name: str
    specialty: str


class Facility(BaseModel):
    id: str
    name: str


class Bed(BaseModel):
    unit: str
    room: str
    bed: str


class Encounter(BaseModel):
    encounter_id: str
    patient: Patient
    provider: Provider
    facility: Facility
    bed: Bed
    chief_complaint: str
    arrival_method: str
    triage_level: int
    status: str


class Scenario(BaseModel):
    name: str
    event: str
    # encounter: Encounter
    encounter: dict   # simplified for now (we will refine later)