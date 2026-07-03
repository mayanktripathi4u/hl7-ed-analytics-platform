import random
import uuid

from ed_simulator.domain.encounter import Encounter

class EncounterFactory:
    COMPLAINTS = [
        "Chest Pain",
        "Motor Vehicle Accident",
        "Abdominal Pain",
        "Shortness of Breath",
        "Fever",
        "Headache",
        "Fracture",
        "Sepsis Alert"
    ]

    def create(self, patient_id: str) -> Encounter:
        complaint = random.choice(self.COMPLAINTS)

        # severity model (simple weighted randomness)
        esi = random.choices(
            population=[1, 2, 3, 4, 5],
            weights=[5, 15, 40, 25, 15],
            k=1
        )[0]

        return Encounter(
            encounter_id=f"ENC-{uuid.uuid4().hex[:8]}",
            patient_id=patient_id,
            chief_complaint=complaint,
            arrival_mode=random.choice(["AMBULANCE", "WALK_IN"]),
            esi_level=esi
        )