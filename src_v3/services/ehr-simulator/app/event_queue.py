from heapq import heappush
from heapq import heappop

class EventQueue:
    def __init__(self):
        self.queue = []

    def publish(self, event):
        heappush(
            self.queue,
            (
                event.timestamp,
                event
            )
        )

    def next(self):
        return heappop(
            self.queue
        )[1]

    def empty(self):
        return len(self.queue) == 0