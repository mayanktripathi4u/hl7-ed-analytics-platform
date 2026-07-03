from collections import defaultdict
import heapq

class ProviderManager:
    """
    Simulates limited ED physicians with workload balancing.
    """
    def __init__(self, providers=None):
        self.providers = providers or [
            "DR_SMITH",
            "DR_JONES",
            "DR_PATEL",
            "DR_LI"
        ]

        # min-heap based workload
        self.workload_heap = [(0, p) for p in self.providers]
        heapq.heapify(self.workload_heap)

        self.active_workload = defaultdict(int)

    def assign_provider(self, patient_id):
        workload, provider = heapq.heappop(self.workload_heap)
        self.active_workload[provider] += 1

        # push back with updated workload
        heapq.heappush(
            self.workload_heap,
            (self.active_workload[provider], provider)
        )
        return provider

    def complete_case(self, provider):
        self.active_workload[provider] -= 1

        # rebuild heap safely (simple approach for simulation)
        self.workload_heap = [
            (self.active_workload[p], p)
            for p in self.providers
        ]
        heapq.heapify(self.workload_heap)