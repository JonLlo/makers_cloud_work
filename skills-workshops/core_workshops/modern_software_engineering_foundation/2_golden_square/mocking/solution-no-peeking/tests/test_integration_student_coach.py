from lib.coach import Coach
from lib.student import Student

def test_coach_and_student_interaction():
    coach = Coach("Alice")
    student = Student("Bob")
    
    coach.add_student(student)
    coach.upload_submission_for_students("Workshop 1")
    
    # Verifying the actual data moved through the real objects
    assert student.submissions == ["Workshop 1"]
    assert coach.count_submissions() == 1
    assert coach.print_student_names() == "Bob"
