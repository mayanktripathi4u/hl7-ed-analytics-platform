from datetime import datetime, timedelta

class SimulationClock:
    """
    Deterministic simulation clock.
    NO datetime.now() allowed anywhere in system.
    """
    def __init__(self, start_time: datetime, duration_hours: int):
        self.current_time = start_time
        self.end_time = start_time + timedelta(hours=duration_hours)

    def now(self) -> datetime:
        return self.current_time

    def advance(self, minutes: int) -> None:
        self.current_time += timedelta(minutes=minutes)

    def is_finished(self) -> bool:
        return self.current_time >= self.end_time