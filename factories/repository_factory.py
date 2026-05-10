from repositories.inmemory.inmemory_assignment_repository import InMemoryAssignmentRepository


class RepositoryFactory:

    @staticmethod
    def get_assignment_repository(storage_type="MEMORY"):

        if storage_type == "MEMORY":
            return InMemoryAssignmentRepository()

        elif storage_type == "DATABASE":
            raise NotImplementedError("Database repository not implemented")

        else:
            raise ValueError("Invalid storage type")