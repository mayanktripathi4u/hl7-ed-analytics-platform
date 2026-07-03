import random
from datetime import timedelta

class ArrivalGenerator:
    def next_arrival(self):
        return timedelta(
            minutes=random.randint(3, 12)
        )