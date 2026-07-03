import random
from faker import Faker

from pathlib import Path
import sys
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.models.patient import Patient, PatientIdentifier, PatientDemographics
from datetime import date

fake = Faker()

class PatientFactory:
    @staticmethod
    def create() -> Patient:
        gender = random.choice(["Male", "Female"])
        first_name = (
            fake.first_name_male()
            if gender == "Male"
            else fake.first_name_female()
        )
        today = date.today()
        birth_date=fake.date_of_birth()
        age = int(today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)))
        
        return Patient(
            identifier=PatientIdentifier(mrn=f"MRN{random.randint(100000, 999999)}"),
            demographics=PatientDemographics(
                first_name=first_name,
                last_name=fake.last_name(),
                gender=gender,
                birth_date=birth_date,
                age=age,
            ),
        )