from lib.student import Student

def test_student_initialization():
    student = Student("Bob")
    assert student.name == "Bob"
    assert student.submissions == []

def test_add_submission_updates_list():
    student = Student("Bob")
    student.add_submission("Math Quiz")
    assert "Math Quiz" in student.submissions
    assert student.count_submissions() == 1