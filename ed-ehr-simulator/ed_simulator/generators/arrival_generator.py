import random
from datetime import timedelta

class ArrivalGenerator:
    def next_interval(self) -> timedelta:
        # simple model: 2–10 min between arrivals
        return timedelta(minutes=random.randint(2, 10))