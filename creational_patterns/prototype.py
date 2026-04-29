import copy

class AssignmentPrototype:
    def __init__(self, title):
        self.title = title

    def clone(self):
        return copy.deepcopy(self)