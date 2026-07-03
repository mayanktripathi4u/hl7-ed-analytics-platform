from pydantic import BaseModel

from .arrival import Arrival
from .bed import BedAssignment
from .clinical import ClinicalStatus
from .disposition import Disposition
from .facility import Facility
from .patient import Patient
from .provider import Provider
from .triage import Triage

class Encounter(BaseModel):
    encounter_id: str
    patient: Patient
    facility: Facility
    provider: Provider
    # arrival: Arrival
    # triage: Triage
    bed: BedAssignment
    # clinical: ClinicalStatus
    # disposition: Disposition

    chief_complaint: str
    arrival_method: str
    triage_level: int