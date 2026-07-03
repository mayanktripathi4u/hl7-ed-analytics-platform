from faker import Faker
import random
from common.models import Patient

fake = Faker()

class PatientFactory:
    """
    Generates realistic synthetic ED patients.
    """
    @staticmethod
    def create() -> Patient:
        gender = random.choice(["Male", "Female"])
        if gender == "Male":
            first_name = fake.first_name_male()
        else:
            first_name = fake.first_name_female()

        last_name = fake.last_name()

        return Patient(
            mrn=f"MRN{random.randint(100000, 999999)}",
            first_name=first_name,
            last_name=last_name,
            age=random.randint(1, 95),
            gender=gender,
        )