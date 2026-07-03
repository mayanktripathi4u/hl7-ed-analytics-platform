from pathlib import Path

class HL7Writer:
    def __init__(self):
        self.output = Path("output")
        self.output.mkdir(exist_ok=True)

    def write(self, encounter_id: str, message: str):
        filename = self.output / f"{encounter_id}.hl7"
        filename.write_text(message)
        return filename