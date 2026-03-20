from src.availability import AvailabilityChecker
from src.meeting import Meeting

class Scheduler:
    def __init__(self):
        self.availability_checker = AvailabilityChecker()

    def schedule_meeting(self, title, start, end, participants):
        unavailable = []

        for person in participants:
            if not self.availability_checker.is_available(person, start, end):
                unavailable.append(person)

        if len(unavailable) == 0:
            return {
                "status": "success",
                "meeting": Meeting(title, start, end, participants)
            }
        else:
            suggestions = self.find_available_slots(participants)
            return {
                "status": "conflict",
                "unavailable": unavailable,
                "suggestions": suggestions
            }

    def find_available_slots(self, participants):
        possible_slots = []

        # check slots from 9 to 18
        for start in range(9, 18):
            end = start + 1
            all_available = True

            for person in participants:
                if not self.availability_checker.is_available(person, start, end):
                    all_available = False
                    break

            if all_available:
                possible_slots.append(f"{start}-{end}")

        return possible_slots if possible_slots else ["No common slots available"]