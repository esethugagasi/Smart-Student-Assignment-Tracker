
from repositories.inmemory.inmemory_assignment_repository import (
    InMemoryAssignmentRepository
)


class AssignmentNotFoundException(Exception):
    pass


class AssignmentAlreadySubmittedException(Exception):
    pass


class AssignmentService:

    def __init__(self, assignment_repo=None):

        self.assignment_repo = (
            assignment_repo or InMemoryAssignmentRepository()
        )

    def submit_assignment(self, assignment_id):

        assignment = self.assignment_repo.find_by_id(assignment_id)

        if not assignment:
            raise AssignmentNotFoundException(
                f"Assignment {assignment_id} not found"
            )

        if assignment.status == "Submitted":
            raise AssignmentAlreadySubmittedException(
                f"Assignment {assignment_id} already submitted"
            )

        assignment.submit()

        self.assignment_repo.save(assignment)

        return assignment

    def get_all_assignments(self):
        return self.assignment_repo.find_all()

    def create_assignment(self, assignment):
        self.assignment_repo.save(assignment)
        return assignment

