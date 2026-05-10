from repositories.inmemory.inmemory_assignment_repository import InMemoryAssignmentRepository
from src.assignment import Assignment


def test_save_assignment():

    repo = InMemoryAssignmentRepository()

    assignment = Assignment("A1", "Math", "Tomorrow")

    repo.save(assignment)

    assert repo.find_by_id("A1") == assignment


def test_delete_assignment():

    repo = InMemoryAssignmentRepository()

    assignment = Assignment("A1", "Math", "Tomorrow")

    repo.save(assignment)

    repo.delete("A1")

    assert repo.find_by_id("A1") is None