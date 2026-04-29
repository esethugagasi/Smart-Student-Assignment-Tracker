class AssignmentBuilder:
    def __init__(self):
        self.assignment = {}

    def set_title(self, title):
        self.assignment["title"] = title
        return self

    def set_deadline(self, deadline):
        self.assignment["deadline"] = deadline
        return self

    def build(self):
        return self.assignment