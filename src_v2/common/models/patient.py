from pydantic import BaseModel
from datetime import date

class PatientIdentifier(BaseModel):
    mrn: str

class PatientDemographics(BaseModel):
    first_name: str
    last_name: str
    gender: str
    birth_date: date
    age: int

class Patient(BaseModel):
    identifier: PatientIdentifier
    demographics: PatientDemographics