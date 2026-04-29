class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email

    def register(self):
        return f"{self.name} registered"

    def login(self):
        return f"{self.name} logged in"