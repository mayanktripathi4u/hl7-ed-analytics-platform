import heapq
from typing import List

from ed_simulator.domain.event import Event

class EventQueue:
    """
    Priority queue sorted by timestamp.
    This simulates real ED interleaving of patient events.
    """
    def __init__(self):
        self._heap: List[Event] = []

    def publish(self, event: Event) -> None:
        heapq.heappush(self._heap, event)

    def has_events(self) -> bool:
        return len(self._heap) > 0

    def next(self) -> Event:
        return heapq.heappop(self._heap)