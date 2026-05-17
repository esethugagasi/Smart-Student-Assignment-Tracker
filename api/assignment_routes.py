
from fastapi import APIRouter
from services.assignment_service import AssignmentService
from src.assignment import Assignment

router = APIRouter()

assignment_service = AssignmentService()


@router.get("/api/assignments")
def get_assignments():
    return assignment_service.get_all_assignments()


@router.post("/api/assignments")
def create_assignment():

    assignment = Assignment(
        "A1",
        "Software Engineering Assignment",
        "2026-06-01"
    )

    assignment_service.create_assignment(assignment)

    return {
        "message": "Assignment created",
        "assignment": assignment.__dict__
    }


@router.post("/api/assignments/{assignment_id}/submit")
def submit_assignment(assignment_id: str):

    assignment = assignment_service.submit_assignment(assignment_id)

    return {
        "message": f"Assignment {assignment_id} submitted",
        "assignment": assignment.__dict__
    }
