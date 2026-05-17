from services.assignment_service import AssignmentService
from src.assignment import Assignment


def test_submit_assignment():

    service = AssignmentService()

    assignment = Assignment(
        "A1",
        "Math Assignment",
        "Tomorrow"
    )

    service.assignment_repo.save(assignment)

    submitted_assignment = service.submit_assignment("A1")

    assert submitted_assignment.status == "Submitted"