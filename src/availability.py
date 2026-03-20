class AvailabilityChecker:
    def __init__(self):
        self.availability = {
            "Alice": [(9, 12), (14, 18)],
            "Bob": [(10, 13), (15, 17)],
            "Charlie": [(9, 11), (13, 16)]
        }

    def is_available(self, participant, start, end):
        # If participant not found → assume full availability
        if participant not in self.availability:
            return True

        for slot in self.availability.get(participant, []):
            if start >= slot[0] and end <= slot[1]:
                return True
        return False