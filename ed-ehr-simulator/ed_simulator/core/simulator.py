# from datetime import datetime

# from ed_simulator.core.clock import SimulationClock
# from ed_simulator.core.event_queue import EventQueue
# from ed_simulator.domain.event import Event

# class EDSimulator:
#     def __init__(self, start_time: datetime, duration_hours: int):
#         self.clock = SimulationClock(start_time, duration_hours)
#         self.queue = EventQueue()

#         self.sequence = 0

#     def _emit_test_events(self):
#         """
#         Phase 1 ONLY:
#         We inject synthetic events to validate engine.
#         """
#         base = self.clock.now()

#         self.queue.publish(
#             Event(
#                 timestamp=base,
#                 sequence=self._next_seq(),
#                 patient_id="P001",
#                 encounter_id="E001",
#                 event_type="ARRIVAL",
#                 facility_id="FAC1"
#             )
#         )

#         self.queue.publish(
#             Event(
#                 timestamp=base,
#                 sequence=self._next_seq(),
#                 patient_id="P002",
#                 encounter_id="E002",
#                 event_type="ARRIVAL",
#                 facility_id="FAC1"
#             )
#         )

#         self.queue.publish(
#             Event(
#                 timestamp=base,
#                 sequence=self._next_seq(),
#                 patient_id="P001",
#                 encounter_id="E001",
#                 event_type="TRIAGE",
#                 facility_id="FAC1"
#             )
#         )

#     def _next_seq(self) -> int:
#         self.sequence += 1
#         return self.sequence

#     def run(self):
#         print("\n=== ED SHIFT SIMULATOR STARTED ===\n")

#         # Phase 1: inject test events
#         self._emit_test_events()

#         # Process event stream
#         while self.queue.has_events():
#             event = self.queue.next()
#             print(
#                 f"{event.timestamp.time()} | "
#                 f"{event.patient_id} | "
#                 f"{event.event_type}"
#             )
#         print("\n=== SIMULATION COMPLETE ===\n")


from datetime import datetime

from ed_simulator.core.event_queue import EventQueue
from ed_simulator.generators.patient_factory import PatientFactory
from ed_simulator.generators.arrival_generator import ArrivalGenerator
from ed_simulator.generators.journey_engine import JourneyEngine
from ed_simulator.generators.encounter_factory import EncounterFactory
from ed_simulator.core.bed_manager import BedManager
from ed_simulator.core.provider_manager import ProviderManager

class EDSimulator:
    def __init__(self, start_time: datetime, duration_hours: int):
        self.start_time = start_time
        self.end_time = start_time
        self.end_time = start_time.replace(hour=start_time.hour + duration_hours)

        self.queue = EventQueue()

        self.patient_factory = PatientFactory()
        self.arrival_generator = ArrivalGenerator()
        # self.journey_engine = JourneyEngine() # JourneyEngine initialized with default (20) beds
        self.encounter_factory = EncounterFactory()
        self.bed_manager = BedManager(total_beds=10)
        # self.journey_engine = JourneyEngine(self.bed_manager)  # JourneyEngine initialized with BedManager instance
        self.provider_manager = ProviderManager()
        self.journey_engine = JourneyEngine(
            self.bed_manager,
            self.provider_manager
        )

        self.sequence = 0

    def _next_seq(self):
        self.sequence += 1
        return self.sequence

    def run(self):
        print("\n=== ED SHIFT SIMULATION STARTED ===\n")
        current_time = self.start_time
        facility_id = "FAC1"

        # simulate ~20 patients for now
        for _ in range(20):
            # 1. create patient
            patient = self.patient_factory.create()

            # 2. create encounter
            # encounter_id = f"ENC-{patient.patient_id[:8]}"
            encounter = self.encounter_factory.create(patient.patient_id)

            # 3. build journey
            # events, last_seq = self.journey_engine.build_journey(
            #     patient_id=patient.patient_id,
            #     encounter_id=encounter_id,
            #     start_time=current_time,
            #     sequence_start=self._next_seq(),
            #     facility_id=facility_id
            # )

            events, last_seq = self.journey_engine.build_journey(
                patient_id=patient.patient_id,
                encounter=encounter,
                start_time=current_time,
                sequence_start=self._next_seq(),
                facility_id=facility_id
            )

            # update sequence
            self.sequence = last_seq

            # 4. push to event queue
            for event in events:
                self.queue.publish(event)

            # 5. advance ED clock
            current_time += self.arrival_generator.next_interval()

        # 6. replay ED event stream
        while self.queue.has_events():
            event = self.queue.next()
            print(
                f"{event.timestamp.time()} | "
                f"{event.patient_id[:8]} | "
                f"{event.event_type}"
            )

        print("\n=== SIMULATION COMPLETE ===\n")