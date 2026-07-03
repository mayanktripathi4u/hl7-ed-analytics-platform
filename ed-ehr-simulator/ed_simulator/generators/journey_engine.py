# from datetime import timedelta

# from ed_simulator.domain.event import Event

# class JourneyEngine:
#     def build_journey(
#         self,
#         patient_id: str,
#         encounter_id: str,
#         start_time,
#         sequence_start: int,
#         facility_id: str
#     ):
#         events = []

#         def add(minutes, event_type, seq):
#             events.append(
#                 Event(
#                     timestamp=start_time + timedelta(minutes=minutes),
#                     sequence=seq,
#                     patient_id=patient_id,
#                     encounter_id=encounter_id,
#                     event_type=event_type,
#                     facility_id=facility_id
#                 )
#             )

#         seq = sequence_start

#         # ED workflow (baseline deterministic path)
#         add(0, "ARRIVAL", seq); seq += 1
#         add(5, "TRIAGE", seq); seq += 1
#         add(12, "BED_ASSIGNED", seq); seq += 1
#         add(18, "PROVIDER_ASSIGNED", seq); seq += 1
#         add(30, "TREATMENT_STARTED", seq); seq += 1
#         add(90, "DISCHARGE", seq); seq += 1

#         return events, seq


import random
from datetime import timedelta

from ed_simulator.domain.event import Event
from ed_simulator.core.bed_manager import BedManager
from ed_simulator.core.provider_manager import ProviderManager


class JourneyEngine:
    def __init__(self, bed_manager: BedManager, provider_manager: ProviderManager):
        # self.bed_manager = BedManager()
        self.bed_manager = bed_manager
        self.provider_manager = provider_manager
        print(f"[JourneyEngine] Initialized with {self.bed_manager.total_beds} beds.")

    def build_journey(
        self,
        patient_id,
        encounter,
        start_time,
        sequence_start,
        facility_id
    ):
        events = []
        seq = sequence_start

        esi = encounter.esi_level

        # -----------------------
        # BASE TIMING MODEL
        # -----------------------
        triage_delay = max(1, 10 - esi)  # high acuity = faster triage
        bed_delay = random.randint(5, 20) + (esi * 2)
        # provider_delay = random.randint(3, 15)
        provider = self.provider_manager.assign_provider(patient_id)
        provider_delay = random.randint(5, 20) + (self.provider_manager.active_workload[provider] * 2)
        
        treatment_time = random.randint(20, 120)

        # -----------------------
        # ARRIVAL
        # -----------------------
        events.append(Event(
            timestamp=start_time,
            sequence=seq,
            patient_id=patient_id,
            encounter_id=encounter.encounter_id,
            event_type="ARRIVAL",
            facility_id=facility_id
        ))
        seq += 1

        # -----------------------
        # TRIAGE
        # -----------------------
        events.append(Event(
            timestamp=start_time + timedelta(minutes=triage_delay),
            sequence=seq,
            patient_id=patient_id,
            encounter_id=encounter.encounter_id,
            event_type="TRIAGE",
            facility_id=facility_id
        ))
        seq += 1

        # -----------------------
        # BED ASSIGNMENT (may fail realistically later)
        # -----------------------
        # events.append(Event(
        #     timestamp=start_time + timedelta(minutes=bed_delay),
        #     sequence=seq,
        #     patient_id=patient_id,
        #     encounter_id=encounter.encounter_id,
        #     event_type="BED_ASSIGNED",
        #     facility_id=facility_id
        # ))
        if self.bed_manager.request_bed(patient_id):
            events.append(Event(
                timestamp=start_time + timedelta(minutes=bed_delay),
                sequence=seq,
                patient_id=patient_id,
                encounter_id=encounter.encounter_id,
                event_type="BED_ASSIGNED",
                facility_id=facility_id
            ))
        else:
            events.append(Event(
                timestamp=start_time + timedelta(minutes=bed_delay),
                sequence=seq,
                patient_id=patient_id,
                encounter_id=encounter.encounter_id,
                event_type="BOARDING",
                facility_id=facility_id
            ))
        seq += 1

        # -----------------------
        # PROVIDER ASSIGNMENT
        # -----------------------
        events.append(Event(
            timestamp=start_time + timedelta(minutes=bed_delay + provider_delay),
            sequence=seq,
            patient_id=patient_id,
            encounter_id=encounter.encounter_id,
            event_type="PROVIDER_ASSIGNED",
            facility_id=facility_id
        ))
        seq += 1

        # -----------------------
        # TREATMENT
        # -----------------------
        events.append(Event(
            timestamp=start_time + timedelta(minutes=bed_delay + provider_delay + 5),
            sequence=seq,
            patient_id=patient_id,
            encounter_id=encounter.encounter_id,
            event_type="TREATMENT_STARTED",
            facility_id=facility_id
        ))
        seq += 1

        # -----------------------
        # DISPOSITION (CRITICAL CHANGE)
        # -----------------------
        disposition_choice = self._determine_disposition(esi)

        events.append(Event(
            timestamp=start_time + timedelta(minutes=bed_delay + provider_delay + treatment_time),
            sequence=seq,
            patient_id=patient_id,
            encounter_id=encounter.encounter_id,
            event_type=disposition_choice,
            facility_id=facility_id
        ))

        return events, seq + 1

    def _determine_disposition(self, esi):
        # realistic ED outcomes
        if esi == 1:
            return random.choice(["ADMISSION", "TRANSFER"])
        if esi == 2:
            return random.choices(
                ["ADMISSION", "DISCHARGE"],
                weights=[70, 30]
            )[0]
        if esi == 3:
            return random.choices(
                ["DISCHARGE", "ADMISSION"],
                weights=[80, 20]
            )[0]
        return "DISCHARGE"