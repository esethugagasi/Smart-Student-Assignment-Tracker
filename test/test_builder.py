from creational_patterns.builder import AssignmentBuilder

def test_builder():
    assignment = AssignmentBuilder().set_title("Math").set_deadline("Tomorrow").build()
    assert assignment["title"] == "Math"