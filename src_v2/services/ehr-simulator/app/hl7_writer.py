from pathlib import Path

class HL7Writer:
    def __init__(self):
        self.output_dir = Path("services/ehr-simulator/output")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def write(self, filename: str, content: str):
        file_path = self.output_dir / filename
        file_path.write_text(content)
        return file_path