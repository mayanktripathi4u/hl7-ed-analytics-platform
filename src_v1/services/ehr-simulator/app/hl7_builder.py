from datetime import datetime
from pathlib import Path
import random

from jinja2 import Environment, FileSystemLoader
from common.models import Encounter

class HL7Builder:
    def __init__(self):
        template_dir = Path(__file__).parent.parent / "templates"
        env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.template = env.get_template("adt_a01.j2")

    def build(self, encounter: Encounter) -> str:
        now = datetime.now()
        sex = "M" if encounter.patient.gender == "Male" else "F"
        dob = now.replace(year=now.year - encounter.patient.age)

        return self.template.render(
            encounter=encounter,
            timestamp=now.strftime("%Y%m%d%H%M%S"),
            dob=dob.strftime("%Y%m%d"),
            sex=sex,
            control_id=f"MSG{random.randint(100000,999999)}",
        )