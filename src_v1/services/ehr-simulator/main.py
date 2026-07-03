from pathlib import Path
import sys
import yaml
from rich import print

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.models import Scenario
from app.patient_factory import PatientFactory
from app.encounter_factory import EncounterFactory

from app.hl7_builder import HL7Builder
from app.hl7_writer import HL7Writer

def load_scenario(path: Path) -> Scenario:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return Scenario.model_validate(data)

def main():
    scenario_path = Path(__file__).resolve().parent / "scenarios" / "trauma_alert.yaml"
    scenario = load_scenario(scenario_path)
    print()
    # print("Scenario Loaded")
    # print("-----------------------")
    # print(f"Scenario : {scenario.name}")
    # print(f"Patient  : {scenario.encounter.patient.first_name} "
    #       f"{scenario.encounter.patient.last_name}")
    # print(f"MRN       : {scenario.encounter.patient.mrn}")
    # print(f"Complaint : {scenario.encounter.chief_complaint}")
    # print(f"Facility  : {scenario.encounter.facility.name}")
    # print(f"Bed       : {scenario.encounter.bed.room}")
    # print(f"Triage    : {scenario.encounter.triage_level}")

    print("\n[bold green]Loaded Scenario:[/bold green]")
    print(scenario.name)

    # STEP 1: generate patient
    patient = PatientFactory.create()

    # STEP 2: build encounter
    encounter = EncounterFactory.create(
        patient=patient,
        scenario=scenario.model_dump()
    )

    print("\n[bold cyan]Generated Encounter:[/bold cyan]")
    print(f"Patient     : {encounter.patient.first_name} {encounter.patient.last_name}")
    print(f"MRN         : {encounter.patient.mrn}")
    print(f"Complaint   : {encounter.chief_complaint}")
    print(f"Arrival     : {encounter.arrival_method}")
    print(f"Triage      : {encounter.triage_level}")
    print(f"Facility    : {encounter.facility.name}")
    print(f"Bed         : {encounter.bed.bed}")
    print(f"Provider    : {encounter.provider.first_name} {encounter.provider.last_name}")
    print(f"EncounterID : {encounter.encounter_id}")

    # print()

    builder = HL7Builder()
    message = builder.build(encounter)
    writer = HL7Writer()
    file = writer.write(encounter.encounter_id, message)
    print()
    print("HL7 Generated")
    print(file)


if __name__ == "__main__":
    main()