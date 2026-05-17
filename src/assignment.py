
class Assignment:

    def __init__(self, assignment_id, title, deadline, status="Pending"):
        self.assignment_id = assignment_id
        self.title = title
        self.deadline = deadline
        self.status = status

    def submit(self):
        self.status = "Submitted"

    def update_status(self, status):
        self.status = status

