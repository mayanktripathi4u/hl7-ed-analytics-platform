import uuid
import random

from pathlib import Path
import sys
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.models.encounter import Encounter
from common.models.provider import Provider
from common.models.facility import Facility
from common.models.bed import BedAssignment
from common.models.patient import Patient

class EncounterFactory:
    @staticmethod
    def create(patient: Patient, scenario: dict) -> Encounter:
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
                name="Nashville General",
                city="Nashville",
                state="TN",
            ),

            bed=BedAssignment(
                unit="ED",
                room="TRAUMA",
                bed=f"B{random.randint(1,50)}",
                status="Occupied",
            ),

            chief_complaint=scenario["encounter"]["chief_complaint"],
            arrival_method=scenario["encounter"]["arrival_method"],
            triage_level=scenario["encounter"]["triage_level"],
        )