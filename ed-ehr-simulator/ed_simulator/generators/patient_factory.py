import random
import uuid
from faker import Faker

from ed_simulator.domain.patient import Patient

fake = Faker()

class PatientFactory:
    def create(self) -> Patient:
        gender = random.choice(["M", "F"])

        return Patient(
            patient_id=str(uuid.uuid4()),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            gender=gender,
            age=random.randint(1, 90)
        )