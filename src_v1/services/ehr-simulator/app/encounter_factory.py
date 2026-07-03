import random
import uuid
from common.models import Encounter, Facility, Provider, Bed, Patient

class EncounterFactory:
    """
    Builds encounter objects based on scenario + generated entities.
    """
    @staticmethod
    def create(
        patient: Patient,
        scenario: dict
    ) -> Encounter:
        return Encounter(
            encounter_id=str(uuid.uuid4()),
            patient=patient,

            provider=Provider(
                id=f"DOC{random.randint(100,999)}",
                first_name="Auto",
                last_name="Provider",
                specialty="Emergency Medicine",
            ),

            facility=Facility(
                id="FAC01",
                name="Nashville General"
            ),

            bed=Bed(
                unit="ED",
                room="AUTO",
                bed=f"B{random.randint(1,50)}"
            ),

            chief_complaint=scenario["encounter"]["chief_complaint"],
            arrival_method=scenario["encounter"]["arrival_method"],
            triage_level=scenario["encounter"]["triage_level"],
            status=scenario["encounter"]["status"],
        )