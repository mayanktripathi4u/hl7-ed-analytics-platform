from datetime import datetime, timedelta

class SimulationClock:
    def __init__(
        self,
        start_time: datetime,
        duration_hours: int
    ):
        self.current_time = start_time
        self.end_time = (
            start_time +
            timedelta(hours=duration_hours)
        )

    def now(self):
        return self.current_time

    def advance(self, minutes: int):
        self.current_time += timedelta(
            minutes=minutes
        )

    def finished(self):
        return self.current_time >= self.end_time