from datetime import datetime

class HL7Builder:
    def build(self, encounter, event):
        now = event.timestamp.strftime("%Y%m%d%H%M%S")
        # print(f"[Class: HL7Builder] Building HL7 message for event: {event.name} at {now}")
        # print(f"encounter parameters: {encounter}")

        return f"""
MSH|^~\\&|EHR|{encounter.facility.id}|EXPANSE|DR|{now}||{event.hl7}|{encounter.encounter_id}|P|2.5
PID|||{encounter.patient.identifier.mrn}||{encounter.patient.demographics.last_name}^{encounter.patient.demographics.first_name}|||{encounter.patient.demographics.gender}
PV1||E|{encounter.bed.unit}^{encounter.bed.room}^{encounter.bed.bed}||||{encounter.provider.id}
ZED|{encounter.arrival_method}|{encounter.triage_level}|ACTIVE
""".strip()