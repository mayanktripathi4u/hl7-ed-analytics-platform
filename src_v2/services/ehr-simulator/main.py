# from datetime import datetime

# timeline = TimelineEngine()

# events = timeline.build(datetime.now())

# for event in events:
#     print(
#         event.sequence,
#         event.timestamp,
#         event.event_type,
#         event.hl7_event
#     )


from datetime import datetime
from rich import print

from app.patient_factory import PatientFactory
from app.encounter_factory import EncounterFactory
from app.timeline_engine import TimelineEngine
from app.hl7_builder import HL7Builder
from app.hl7_writer import HL7Writer


def main():
    print("\n[bold green]ED SIMULATOR STARTED[/bold green]\n")

    scenario = {
        "encounter": {
            "chief_complaint": "Motor Vehicle Accident",
            "arrival_method": "Ambulance",
            "triage_level": 1,
        }
    }

    # 1. Patient
    patient = PatientFactory.create()

    # 2. Encounter
    encounter = EncounterFactory.create(patient, scenario)

    # 3. Timeline
    timeline = TimelineEngine().build(datetime.now())

    builder = HL7Builder()
    writer = HL7Writer()

    print("[bold cyan]EVENT STREAM[/bold cyan]\n")

    for event in timeline:
        hl7 = builder.build(encounter, event)
        filename = f"{event.sequence:03d}_{event.hl7.replace('^','_')}.hl7"
        path = writer.write(filename, hl7)
        print(f"{event.timestamp.time()} | {event.name:<20} | {event.hl7} | {path.name}")

    print("\n[bold green]SIMULATION COMPLETE[/bold green]\n")

if __name__ == "__main__":
    main()