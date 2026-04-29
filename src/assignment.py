class Assignment:
    def __init__(self, assignment_id, title, deadline):
        self.assignment_id = assignment_id
        self.title = title
        self.deadline = deadline
        self.status = "Pending"

    def update_status(self, status):
        self.status = status