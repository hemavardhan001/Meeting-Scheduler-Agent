class Meeting:
    def __init__(self, title, start_time, end_time, participants):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.participants = participants

    def __str__(self):
        return f"{self.title} | {self.start_time}-{self.end_time} | Participants: {', '.join(self.participants)}"