from collections import deque

class BedManager:
    """
    Simulates finite ED bed capacity.
    """
    def __init__(self, total_beds: int = 20):

        self.total_beds = total_beds
        self.occupied = {}
        self.waiting_queue = deque()

    def available_beds(self):
        return self.total_beds - len(self.occupied)

    def request_bed(self, patient_id):
        if self.available_beds() > 0:
            self.occupied[patient_id] = True
            return True

        self.waiting_queue.append(patient_id)
        return False

    def release_bed(self, patient_id):
        if patient_id in self.occupied:
            del self.occupied[patient_id]

        # assign next patient in queue
        if self.waiting_queue:
            next_patient = self.waiting_queue.popleft()
            self.occupied[next_patient] = True
            return next_patient
        return None

    def occupancy_rate(self):
        return len(self.occupied) / self.total_beds